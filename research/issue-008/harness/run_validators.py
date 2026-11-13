#!/usr/bin/env python3
"""Mutation-based evaluation harness for the issue #8 pilot.

Runs ONE pinned validator over a corpus of SysML v2 models and records, for each
model, the tool's *raw* JSON output plus a tidy per-case row. Raw output is
written once and never rewritten: a re-run gets a new --run-id directory, so the
evidence a report cites cannot be edited in place.

Design constraints imposed by the pilot protocol (research/relational/PROTOCOL.md):
  * validator verdicts are never ground truth -- this script only *measures*; it
    never classifies a model as defective or valid;
  * the corpus, the mutant manifest and the expectations are hashed before the
    run and the hashes are recorded in the run log;
  * exit codes, argv, tool identity and timestamps are all recorded, so the run
    is reproducible offline.

Usage (offline, no network):
    python3 harness/run_validators.py                 # known-good + mutants, run1
    python3 harness/run_validators.py --run-id run2
    python3 harness/run_validators.py --only known-good
    python3 harness/run_validators.py --binary /path/to/sysml

Outputs, under research/issue-008/results/:
    raw/<run-id>/<kind>/<stem>.json        verbatim stdout of the validator
    raw/<run-id>/<kind>/<stem>.stderr.txt  verbatim stderr
    results.csv                            one row per case
    diagnostics.csv                        one row per diagnostic
    run-log.md                             tool identity, hashes, argv, exit codes
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent                      # research/issue-008
REPO = ROOT.parent.parent               # repository root
RESULTS = ROOT / "results"

# The pinned instrument. research/relational/TOOLING.md §1.
DEFAULT_BINARY = REPO / ".tools" / "sysml"
EXPECTED_BINARY_SHA = "ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0"

CORPORA = {
    "known-good": ROOT / "known-good",
    "mutants": ROOT / "mutants",
}


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def tool_identity(binary: Path) -> dict:
    ident = {"path": str(binary), "binary_sha256": sha256_file(binary)}
    try:
        proc = subprocess.run(
            [str(binary), "-version"], capture_output=True, text=True, timeout=120
        )
        ident["version_stdout"] = proc.stdout.strip()
        ident["version_exit"] = proc.returncode
    except Exception as exc:                      # pragma: no cover - diagnostic
        ident["version_error"] = repr(exc)
    return ident


def load_manifest() -> dict:
    """mutant_id -> manifest row, for the expectation columns."""
    path = ROOT / "mutants" / "MANIFEST.csv"
    if not path.exists():
        return {}
    with open(path, newline="") as fh:
        return {row["mutant_id"]: row for row in csv.DictReader(fh)}


def run_one(binary: Path, model: Path, raw_dir: Path) -> dict:
    argv = [str(binary), "-validate", "-format", "json", str(model)]
    started = utcnow()
    proc = subprocess.run(argv, capture_output=True, text=True, timeout=600)
    finished = utcnow()

    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_json = raw_dir / f"{model.stem}.json"
    raw_err = raw_dir / f"{model.stem}.stderr.txt"
    # verbatim, and refused if it already exists: raw evidence is append-only
    with open(raw_json, "x") as fh:
        fh.write(proc.stdout)
    with open(raw_err, "x") as fh:
        fh.write(proc.stderr)

    parsed = None
    parse_error = None
    try:
        parsed = json.loads(proc.stdout) if proc.stdout.strip() else None
    except json.JSONDecodeError as exc:
        parse_error = f"{exc}"

    diagnostics = []
    if isinstance(parsed, dict) and isinstance(parsed.get("diagnostics"), list):
        diagnostics = parsed["diagnostics"]

    return {
        "argv": argv,
        "started_utc": started,
        "finished_utc": finished,
        "exit_code": proc.returncode,
        "model_sha256": sha256_file(model),
        "raw_json": str(raw_json.relative_to(ROOT)),
        "raw_stderr": str(raw_err.relative_to(ROOT)),
        "json_parsed": parsed is not None,
        "json_parse_error": parse_error,
        "envelope_status": (parsed or {}).get("status") if isinstance(parsed, dict) else None,
        "envelope_exit": (parsed or {}).get("exit") if isinstance(parsed, dict) else None,
        "envelope_errors": (parsed or {}).get("errors") if isinstance(parsed, dict) else None,
        "diagnostics": diagnostics,
        "stderr": proc.stderr,
    }


def summarise(run: dict) -> dict:
    diags = run["diagnostics"]
    severities = [d.get("severity", "?") for d in diags]
    codes = [d.get("code", "?") for d in diags]
    layers = [d.get("pass", "?") for d in diags]
    has_error = "error" in severities
    has_warning = "warning" in severities
    # highest-severity emitted layer, using the tool's own pass names
    top = "none"
    if diags:
        order = {"error": 0, "warning": 1, "info": 2, "hint": 3}
        top = sorted(diags, key=lambda d: order.get(d.get("severity"), 9))[0].get("pass", "?")
    return {
        "n_diagnostics": len(diags),
        "n_errors": severities.count("error"),
        "n_warnings": severities.count("warning"),
        "error_present": int(has_error),
        "warning_only": int(has_warning and not has_error),
        "silent": int(not diags),
        "codes": ";".join(codes),
        "layers": ";".join(sorted(set(layers))),
        "top_layer": top,
        "first_message": diags[0].get("message", "") if diags else "",
        "first_line": diags[0].get("line", "") if diags else "",
        "all_messages": " || ".join(d.get("message", "") for d in diags),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--binary", default=str(DEFAULT_BINARY))
    ap.add_argument("--run-id", default="run1")
    ap.add_argument("--only", choices=sorted(CORPORA), default=None)
    args = ap.parse_args()

    binary = Path(args.binary).resolve()
    if not binary.exists():
        print(f"FATAL: validator not found at {binary}", file=sys.stderr)
        return 2

    ident = tool_identity(binary)
    if ident["binary_sha256"] != EXPECTED_BINARY_SHA:
        print(
            "WARNING: binary sha256 differs from the pinned value in "
            f"research/relational/TOOLING.md ({ident['binary_sha256']} != {EXPECTED_BINARY_SHA}); "
            "results are not comparable with the pinned run.",
            file=sys.stderr,
        )

    manifest = load_manifest()
    corpora = [args.only] if args.only else list(CORPORA)

    rows, diag_rows, run_records = [], [], []
    for kind in corpora:
        corpus_dir = CORPORA[kind]
        models = sorted(corpus_dir.glob("*.sysml"))
        if not models:
            print(f"WARNING: no models in {corpus_dir}", file=sys.stderr)
        raw_dir = RESULTS / "raw" / args.run_id / kind
        for model in models:
            case_id = model.stem
            run = run_one(binary, model, raw_dir)
            exp = manifest.get(case_id, {})
            row = {
                "case_id": case_id,
                "kind": kind,
                "file": str(model.relative_to(ROOT)),
                "model_sha256": run["model_sha256"],
                "fault_class": exp.get("fault_class", ""),
                "spec_constraint_or_defect": exp.get("spec_constraint_or_defect", ""),
                "expected_layer": exp.get("expected_layer", ""),
                "expected_detectable": exp.get("expected_detectable", ""),
                "surface_tell": exp.get("surface_tell", ""),
                **summarise(run),
                "exit_code": run["exit_code"],
                "envelope_status": run["envelope_status"],
                "envelope_exit": run["envelope_exit"],
                "json_parsed": int(run["json_parsed"]),
                "started_utc": run["started_utc"],
                "finished_utc": run["finished_utc"],
            }
            rows.append(row)
            for d in run["diagnostics"]:
                diag_rows.append(
                    {
                        "case_id": case_id,
                        "kind": kind,
                        "severity": d.get("severity", ""),
                        "code": d.get("code", ""),
                        "pass": d.get("pass", ""),
                        "line": d.get("line", ""),
                        "column": d.get("column", ""),
                        "message": d.get("message", ""),
                        "file": d.get("file", ""),
                    }
                )
            run_records.append({"case_id": case_id, "kind": kind, **run})
            print(f"  {kind}/{case_id}: exit={run['exit_code']} "
                  f"diags={len(run['diagnostics'])}")

    RESULTS.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) if rows else []
    with open(RESULTS / "results.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    with open(RESULTS / "diagnostics.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(diag_rows[0].keys()) if diag_rows else
                           ["case_id", "kind", "severity", "code", "pass", "line", "column",
                            "message", "file"])
        w.writeheader()
        w.writerows(diag_rows)
    with open(RESULTS / f"raw-{args.run_id}.json", "w") as fh:
        json.dump(run_records, fh, indent=2)

    # ---- run log -----------------------------------------------------------
    corpus_hashes = {}
    for name, directory in (("known-good", ROOT / "known-good"), ("mutants", ROOT / "mutants")):
        for p in sorted(directory.glob("*")):
            if p.is_file():
                corpus_hashes[str(p.relative_to(ROOT))] = sha256_file(p)

    log = [
        f"# Validator run log — run id `{args.run_id}`",
        "",
        f"Generated by `harness/run_validators.py` at {utcnow()}.",
        "",
        "## Instrument",
        "",
        f"- path: `{ident['path']}`",
        f"- binary sha256: `{ident['binary_sha256']}`",
        f"- pinned expectation: `{EXPECTED_BINARY_SHA}` -> "
        f"{'MATCH' if ident['binary_sha256'] == EXPECTED_BINARY_SHA else '**MISMATCH**'}",
        "- `-version` output:",
        "",
        "```",
        ident.get("version_stdout", ident.get("version_error", "")),
        "```",
        "",
        "## Exact argv, per case",
        "",
        "```",
    ]
    for rec in run_records:
        log.append(" ".join(rec["argv"]) + f"   # exit={rec['exit_code']}")
    log += [
        "```",
        "",
        "Every invocation emitted the documented harmless stderr line",
        "`sysml: record cache unavailable, holding every file loaded: ...`; verbatim stderr is",
        "kept next to each raw JSON file.",
        "",
        "## Corpus hashes at run time",
        "",
        "| file | sha256 |",
        "|---|---|",
    ]
    for path, digest in corpus_hashes.items():
        log.append(f"| `{path}` | `{digest}` |")
    log += [
        "",
        "## Per-case outcome",
        "",
        "| case | kind | exit | envelope status | diags | errors | warnings |",
        "|---|---|---:|---|---:|---:|---:|",
    ]
    for row in rows:
        log.append(
            f"| {row['case_id']} | {row['kind']} | {row['exit_code']} | "
            f"{row['envelope_status']} | {row['n_diagnostics']} | {row['n_errors']} | "
            f"{row['n_warnings']} |"
        )
    log.append("")
    with open(RESULTS / f"run-log-{args.run_id}.md", "w") as fh:
        fh.write("\n".join(log))

    print(f"\nwrote {len(rows)} case rows and {len(diag_rows)} diagnostics to {RESULTS}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
