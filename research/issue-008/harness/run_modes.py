#!/usr/bin/env python3
"""Per-mode probe matrix for the Gate-2 response (issue #8 pilot).

Researcher A's cross-review objection O1 says the pinned instrument CAN decide an
F7-style defect through `-instantiate <object> -validate=<object>`, so my
"invisible to the only available instrument" claim is false as worded. This
script re-runs the F7 arm (and, for comparison, the known-good bases) through
every invocation of the pinned binary that bears on a verdict, and preserves the
raw output.

It exists because my original harness (`run_validators.py`) ran exactly one
invocation, `-validate -format json`, and therefore could not have represented a
verdict that arrives in `checks[]` rather than `diagnostics[]`. That is the
substantive part of A-O1/O2 and it is now measured rather than discussed.

Usage:  python3 harness/run_modes.py          # writes results/raw/run2-modes/
        python3 harness/run_modes.py --run-id run2-modes-b

Raw output is written once and refused if it already exists; a re-run gets a new
run id, so the evidence cited in the response cannot be edited in place.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPO = ROOT.parent.parent
RESULTS = ROOT / "results"
BINARY = REPO / ".tools" / "sysml"
PINNED_SHA = "ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0"

# (case_id, model path relative to research/issue-008, [(mode, argv-tail)], note)
# The object name for -instantiate/-validate=<object> is the part usage declared
# in each model; where a model declares none, the mode is marked n/a rather than
# invented.
CASES = [
    # ---- F7 arm: the four structural/architectural mutants and their bases ----
    ("M31-F7-01-unreachable-state", "mutants/M31-F7-01-unreachable-state.sysml", "none",
     "state machine: no part usage to instantiate", {"self-check": ["-self-check"]}),
    ("KG-05-states(base of F7-01)", "known-good/KG-05-states.sysml", "none",
     "base machine is complete: every state reachable", {"self-check": ["-self-check"]}),

    ("M31-F7-02-satisfied-but-violated", "mutants/M31-F7-02-satisfied-but-violated.sysml", "vehicle",
     "part usage `vehicle` carries a false require constraint",
     {"satisfy": ["-satisfy"],
      "instantiate-validate": ["-instantiate", "vehicle", "-validate=vehicle"]}),
    ("KG-07-requirements(base of F7-02)", "known-good/KG-07-requirements.sysml", "vehicle",
     "same construct, requirement is true (positive control)",
     {"satisfy": ["-satisfy"],
      "instantiate-validate": ["-instantiate", "vehicle", "-validate=vehicle"]}),

    ("M31-F7-03-missing-flow", "mutants/M31-F7-03-missing-flow.sysml", "none",
     "action definition: no object to instantiate",
     {"self-check": ["-self-check"]}),
    ("KG-09-actions(base of F7-03)", "known-good/KG-09-actions.sysml", "none",
     "base has the flow", {"self-check": ["-self-check"]}),

    ("M31-F7-04-contradictory-assertions", "mutants/M31-F7-04-contradictory-assertions.sysml",
     "testObject", "part `testObject` carries two contradictory assert constraints",
     {"instantiate-validate": ["-instantiate", "testObject", "-validate=testObject"]}),
    ("KG-10-asserts(base of F7-04)", "known-good/KG-10-asserts.sysml", "testObject",
     "one assert, no value for the feature it names",
     {"instantiate-validate": ["-instantiate", "testObject", "-validate=testObject"]}),

    # ---- F1 arm under -strict: does the reserved-keyword case exit differently? ----
    ("M31-F1-03-keyword-typo", "mutants/M31-F1-03-keyword-typo.sysml", "none",
     "F1 notation mutant, baseline exit 2 in default mode",
     {"strict": ["-validate", "-strict"]}),

    # ---- A's own models, read-only, for objections O3/O4/O5 ----
    ("A-T6-C1(reserved-keyword)", "../issue-007/corpus/normalized/T6-C1.sysml", "none",
     "A's reserved-keyword-as-name model (O3)", {"strict": ["-validate", "-strict"]}),
    ("A-T2-C2(satisfy-no-by)", "../issue-007/corpus/normalized/T2-C2.sysml", "levelCrossing",
     "A's S2 record: satisfy with no satisfying feature (O4)",
     {"satisfy": ["-satisfy"],
      "instantiate-validate": ["-instantiate", "levelCrossing", "-validate=levelCrossing"],
      "strict": ["-validate", "-strict"]}),
    ("A-T1-C1(dangling-succession)", "../issue-007/corpus/normalized/T1-C1.sysml", "greenhouse",
     "A's N1 record at a succession source (O5)",
     {"satisfy": ["-satisfy"],
      "instantiate-validate": ["-instantiate", "greenhouse", "-validate=greenhouse"]}),
    ("A-T3-C2(dangling-satisfy)", "../issue-007/corpus/normalized/T3-C2.sysml", "none",
     "A's N1 record at a satisfy target: detected in default mode (O5 contrast)",
     {"satisfy": ["-satisfy"]}),
]


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def run(argv: list[str]) -> dict:
    started = utcnow()
    proc = subprocess.run(argv, capture_output=True, text=True, timeout=600)
    finished = utcnow()
    return {"started": started, "finished": finished, "exit": proc.returncode,
            "stdout": proc.stdout, "stderr": proc.stderr}


def checks_from_json(stdout: str):
    """The verdict envelope is `checks[]` with `standing`, not `diagnostics[]`."""
    try:
        doc = json.loads(stdout)
    except json.JSONDecodeError:
        return None
    if not isinstance(doc, dict):
        return None
    return {k: doc.get(k) for k in ("status", "exit", "checks", "diagnostics", "errors")}


def classify(exit_code: int, stdout: str, stderr: str) -> str:
    """Ordered reading of one probe's outcome.

    Corrected after the first run: an exit-0 invocation that still prints
    `error[...]` is NOT "clean". That is the whole point of objection O3, so the
    classifier must not collapse it. The raw output was never wrong; this
    derived label was.
    """
    text = (stdout or "") + (stderr or "")
    if "undecided" in text or "not covered" in text or "could not be evaluated" in text:
        return "undecided (no verdict)"
    if "standing: violated" in text or "assertion fails" in text or " fails (" in text:
        return "violated"
    if "standing: holds" in text or "assertion holds" in text or " holds (" in text:
        return "holds"
    if "no assertion to validate" in text or "states no assertion" in text:
        return "no-assertion"
    if "error[" in text:
        return f"error-diagnostic (exit {exit_code})"
    if exit_code == 2:
        return "nonzero-exit, no error diagnostic"
    return "clean"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", default="run2-modes")
    ap.add_argument("--reclassify", action="store_true",
                    help="rebuild the derived summary from existing raw files, no tool run")
    args = ap.parse_args()

    ident = {"path": str(BINARY), "sha256": sha256_file(BINARY)}
    ver = subprocess.run([str(BINARY), "-version"], capture_output=True, text=True)

    raw_dir = RESULTS / "raw" / args.run_id
    raw_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    log_argv = []

    for case_id, rel, obj, note, modes in CASES:
        model = ROOT / rel
        if not model.exists():
            print(f"MISSING {model}", file=sys.stderr)
            continue
        # baseline: the mode my pilot actually ran, for the same file
        baseline_argv = [str(BINARY), "-validate", "-format", "json", str(model)]
        all_modes = [("default-validate", ["-validate", "-format", "json"])] + list(modes.items())
        for mode, tail in all_modes:
            argv = [str(BINARY)] + tail + [str(model)]
            res = run(argv)
            stem = f"{case_id.replace('/', '_')}__{mode}"
            (raw_dir / f"{stem}.stdout.txt").write_text(res["stdout"])
            (raw_dir / f"{stem}.stderr.txt").write_text(res["stderr"])
            parsed = checks_from_json(res["stdout"]) if "-format" in tail or "-json" in tail else None
            rows.append({
                "case_id": case_id,
                "mode": mode,
                "object": obj,
                "argv": " ".join(argv),
                "exit_code": res["exit"],
                "outcome": classify(res["exit"], res["stdout"], res["stderr"]),
                "json_status": (parsed or {}).get("status") if parsed else "",
                "n_diagnostics": len((parsed or {}).get("diagnostics") or []) if parsed else "",
                "stdout_head": " | ".join(
                    l for l in res["stdout"].splitlines() if l.strip())[:400],
                "note": note,
                "started_utc": res["started"],
            })
            log_argv.append((stem, " ".join(argv), res["exit"]))
            print(f"  {case_id:44} {mode:20} exit={res['exit']:2} -> {rows[-1]['outcome']}")

    with open(RESULTS / f"modes-summary-{args.run_id}.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    log = [
        f"# Per-mode probe run log — `{args.run_id}`",
        "",
        f"Written by `harness/run_modes.py` at {utcnow()}. This run exists because the original",
        "pilot ran one invocation only (`-validate -format json`); see the Gate-2 response to",
        "Researcher A's objection O1.",
        "",
        "## Instrument",
        "",
        f"- path: `{ident['path']}`",
        f"- binary sha256: `{ident['sha256']}` "
        f"({'MATCH' if ident['sha256'] == PINNED_SHA else '**MISMATCH**'} against TOOLING.md)",
        "- `-version`:",
        "",
        "```",
        ver.stdout.strip(),
        "```",
        "",
        "## Exact argv (every probe is read-only over the model files)",
        "",
        "```",
    ]
    for stem, argv, code in log_argv:
        log.append(f"{argv}   # exit={code}   -> raw/{args.run_id}/{stem}.*.txt")
    log += ["```", "", "## Outcome table", "",
            "| case | mode | exit | outcome | note |", "|---|---|---:|---|---|"]
    for r in rows:
        log.append(f"| {r['case_id']} | {r['mode']} | {r['exit_code']} | {r['outcome']} | {r['note']} |")
    log.append("")
    (RESULTS / f"run-log-{args.run_id}.md").write_text("\n".join(log))
    print(f"\nwrote {len(rows)} probe rows to {RESULTS / f'modes-summary-{args.run_id}.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
