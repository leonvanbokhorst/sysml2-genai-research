#!/usr/bin/env python3
"""External challenge set: run A's frozen empirical subset through the pinned validator.

This harness implements `PRE-REGISTRATION.md` and nothing else. It does not decide
what is an error: `subset.json` is ground truth, and this script only measures what
the instrument does at the locations and in the modes registered in advance.

Usage:
    python3 run_external.py --verify-only      # hashes only, no validator run
    python3 run_external.py                    # the full registered run
    python3 run_external.py --run-id x2        # a later run gets its own raw dir

Raw output is written once and refused if it already exists, so a cited run cannot
be edited in place.

Registered modes (PRE-REGISTRATION.md §3):
    M1  -validate -format json                      primary
    M2  -satisfy                                    verdict path, satisfy family
    M3  -instantiate <obj> -validate=<obj>          verdict path, object assertions
    M4  -validate -strict                           secondary
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ISSUE8 = HERE.parent
REPO = ISSUE8.parent.parent
SUBSET = REPO / "research" / "relational" / "empirical-subset"
BINARY = REPO / ".tools" / "sysml"
PINNED_SHA = "ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0"
FROZEN = {"subset.json": "bc2b92a5fdff6e976ae7156b13beba3535f0895e4a41268cf76c1551a6c3dfaa",
          "models/manifest.csv": "a968ff34079a35cdab943dd72415853a4f05617eb353b8deb5665f93ae26b0cb"}

OBJECT_RE = re.compile(r"^    (part|item|occurrence)\s+(?!def\b)([A-Za-z_][A-Za-z0-9_]*)\s*(?::|;|=)")


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_range(spec: str) -> set[int]:
    """'41' -> {41}; '48-51' -> {48..51}; '4,5,9' -> {4,5,9}; mixed forms unioned."""
    out: set[int] = set()
    for part in str(spec).replace(" ", "").split(","):
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            out.update(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    return out


def object_name(model: Path) -> str | None:
    """PRE-REGISTRATION.md §3.1, applied mechanically. None => M3 not applicable."""
    for line in model.read_text().splitlines():
        if line.startswith("    ref ") or line.lstrip().startswith("private"):
            continue
        m = OBJECT_RE.match(line)
        if m:
            return m.group(2)
    return None


def verify() -> tuple[bool, list[str]]:
    lines = ["| artefact | recorded | recomputed | verdict |", "|---|---|---|---|"]
    ok = True
    for rel, want in FROZEN.items():
        got = sha(SUBSET / rel)
        good = got == want
        ok &= good
        lines.append(f"| `{rel}` | `{want}` | `{got}` | {'**OK**' if good else '**MISMATCH**'} |")
    rows = list(csv.DictReader(open(SUBSET / "models" / "manifest.csv")))
    bad = []
    for r in rows:
        p = Path(r["frozen_path"])
        p = p if p.is_absolute() else REPO / p
        good = p.exists() and sha(p) == r["sha256"] and p.stat().st_size == int(r["bytes"])
        if not good:
            bad.append(r["frozen_path"])
    ok &= not bad
    lines.append(f"| {len(rows)} files in `models/manifest.csv` | per-row sha256 + bytes | "
                 f"{'all match' if not bad else 'MISMATCH: ' + str(bad)} | "
                 f"{'**OK**' if not bad else '**MISMATCH**'} |")
    return ok, lines


def run(argv: list[str]) -> dict:
    started = utcnow()
    proc = subprocess.run(argv, capture_output=True, text=True, timeout=600)
    return {"argv": argv, "started": started, "finished": utcnow(), "exit": proc.returncode,
            "stdout": proc.stdout, "stderr": proc.stderr}


def standing_from(text: str) -> str:
    """Five-valued reading, PRE-REGISTRATION.md §4.2."""
    t = text or ""
    if "standing: violated" in t or "assertion fails" in t:
        return "violated"
    if "standing: not covered" in t or "undecided" in t:
        return "undecided"
    if "vacuous" in t:
        return "holds-vacuously"
    if "standing: holds" in t or "assertion holds" in t or re.search(r"✓ .* holds", t):
        return "holds"
    if "states no" in t or "no assertion" in t:
        return "no-assertion"
    return "none"


def score_m1(diags: list[dict], item_range: set[int]) -> tuple[str, str]:
    """PRE-REGISTRATION.md §4.1. Returns (outcome, detail)."""
    if not diags:
        return "silent", "zero diagnostics in the model"
    in_range_err = [d for d in diags if d.get("severity") == "error" and d.get("line") in item_range]
    if in_range_err:
        return "detected", ";".join(f"{d['code']}@{d['line']}" for d in in_range_err)
    in_range_warn = [d for d in diags if d.get("severity") == "warning" and d.get("line") in item_range]
    if in_range_warn:
        return "weaker signal", ";".join(f"{d['code']}@{d['line']}" for d in in_range_warn)
    errs = [d for d in diags if d.get("severity") == "error"]
    if errs:
        return "wrong-target", ";".join(f"{d['code']}@{d['line']}" for d in errs)
    return "weaker signal", ";".join(f"{d['code']}@{d['line']}" for d in diags)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", default="run1")
    ap.add_argument("--verify-only", action="store_true")
    args = ap.parse_args()

    ok, vlines = verify()
    print("verification:", "OK" if ok else "MISMATCH")
    if not ok:
        print("STOP: a frozen file does not match. Not running. Tell the Lead.", file=sys.stderr)
        print("\n".join(vlines), file=sys.stderr)
        return 2
    if args.verify_only:
        print("\n".join(vlines))
        return 0

    subset = json.load(open(SUBSET / "subset.json"))
    items = [i for i in subset["items"] if i["item_type"] == "error"]
    controls = [i for i in subset["items"] if i["item_type"] == "control"]

    tool = {"path": str(BINARY), "sha256": sha(BINARY)}
    version = subprocess.run([str(BINARY), "-version"], capture_output=True, text=True).stdout.strip()

    raw_root = HERE / "raw" / args.run_id
    raw_root.mkdir(parents=True, exist_ok=True)   # a re-run needs a new --run-id
    rows, argv_log = [], []

    def do_item(item: dict) -> None:
        model = REPO / item["normalized_path"]
        obj = object_name(model)
        rng = parse_range(item["line_range"]) if item.get("line_range") else set()
        modes = [
            ("M1", ["-validate", "-format", "json"]),
            ("M2", ["-satisfy"]),
            ("M3", ["-instantiate", obj, f"-validate={obj}"] if obj else None),
            ("M4", ["-validate", "-strict", "-format", "json"]),
        ]
        for mode, tail in modes:
            if tail is None:
                rows.append(dict(item_id=item["item_id"], item_type=item["item_type"],
                                 error_class=item.get("error_class") or "",
                                 layer=item.get("layer") or "",
                                 contested=item.get("contested", ""), mode=mode,
                                 outcome="not applicable", detail="no package-level object",
                                 standing="", exit_code="", n_diagnostics="", object="",
                                 argv="", model=item["source_model"]))
                continue
            argv = [str(BINARY)] + tail + [str(model)]
            res = run(argv)
            stem = f"{item['item_id']}__{mode}"
            # Adjudication B-18 / RB-07: the docstring claimed raw output is refused
            # if it already exists; it was not. Implemented as exclusive creation, so a
            # re-run cannot silently overwrite cited evidence.
            with open(raw_root / f"{stem}.stdout.txt", "x") as fh:
                fh.write(res["stdout"])
            with open(raw_root / f"{stem}.stderr.txt", "x") as fh:
                fh.write(res["stderr"])
            argv_log.append((stem, " ".join(argv), res["exit"]))
            diags = []
            if mode in ("M1", "M4"):
                try:
                    doc = json.loads(res["stdout"])
                    diags = doc.get("diagnostics") or []
                except json.JSONDecodeError:
                    pass
                outcome, detail = score_m1(diags, rng)
                if item["item_type"] == "control":
                    # a control has no item location, so the item-attribution vocabulary
                    # ("wrong-target") is meaningless; label the model instead.
                    errs = [d for d in diags if d.get("severity") == "error"]
                    warns = [d for d in diags if d.get("severity") == "warning"]
                    if errs:
                        outcome, detail = "diagnostic (error)", ";".join(
                            f"{d['code']}@{d['line']}" for d in errs)
                    elif warns:
                        outcome, detail = "diagnostic (warning only)", ";".join(
                            f"{d['code']}@{d['line']}" for d in warns)
                    else:
                        outcome, detail = "clean model", "zero diagnostics"
                standing = ""
            else:
                standing = standing_from(res["stdout"] + res["stderr"])
                # verdict modes: a satisfied item's own standing decides
                satisfy_family = (row_class := (item.get("error_class") == "S2")
                                  or (item.get("error_class") == "N1"
                                      and "satisfy" in (item.get("evidence_excerpt") or "")))
                if mode == "M2":
                    if not any("satisfy" in l for l in (res["stdout"] + res["stderr"]).splitlines()):
                        outcome, detail = "not applicable", "model states no satisfaction assertion"
                    elif row_class and standing == "violated":
                        outcome, detail = "detected", f"its satisfy assertion is violated"
                    elif row_class:
                        outcome, detail = "not detected", f"satisfy standing: {standing}"
                    else:
                        outcome, detail = "wrong-target", (
                            f"not a satisfy-family item; model standing: {standing}")
                else:  # M3
                    if standing == "no-assertion":
                        outcome, detail = "not applicable", "object states no assertion"
                    elif standing == "violated":
                        outcome, detail = "wrong-target", (
                            "object assertion violated, but not the item's defect")
                    elif standing == "undecided":
                        outcome, detail = "weaker signal", "checked, no verdict"
                    else:
                        outcome, detail = "not detected", f"object standing: {standing}"
                # a verdict cannot be formed on a model that does not analyse cleanly
                if standing == "none" and "error[" in (res["stderr"] or ""):
                    outcome, detail = "not applicable", "model does not analyse cleanly; no verdict can be formed"
                detail = detail if standing == "" else f"{standing}: {detail}"
            rows.append(dict(item_id=item["item_id"], item_type=item["item_type"],
                             error_class=item.get("error_class") or "",
                             layer=item.get("layer") or "",
                             contested=item.get("contested", ""), mode=mode,
                             outcome=outcome, detail=detail, standing=standing,
                             exit_code=res["exit"], n_diagnostics=len(diags),
                             object=obj or "", argv=" ".join(argv), model=item["source_model"]))
            print(f"  {item['item_id']:16} {mode} exit={res['exit']:>2} {outcome:16} {detail[:70]}")

    for it in items:
        do_item(it)
    for it in controls:
        do_item(it)

    with open(HERE / "results.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    log = [f"# External challenge-set run log — `{args.run_id}`", "",
           f"Written by `empirical/run_external.py` at {utcnow()}.", "",
           "## 1. Frozen artefact verification", "", *vlines, "",
           f"`frozen_utc` recorded by A: {subset['frozen_utc']}.", "",
           f"**Result:** {'all hashes verified; run proceeded' if ok else 'MISMATCH; run stopped'}.",
           "",
           "## 2. Pre-registration hashes", "",
           "| version | sha256 | note |", "|---|---|---|",
           "| first draft | `0106e08276103e9afbfa6d37015f04f57d2f1a5fc0a4976feb22c2555254f6f2` | header carried a forward-dated written-time; superseded before any run |",
           f"| **frozen** | `{sha(HERE / 'PRE-REGISTRATION.md')}` | the version this run implements |",
           "", "No rule, mode, expectation or scoring definition differs between the two versions; "
           "only the header timestamp and a note were changed, before the first run.", "",
           "## 3. Instrument", "",
           f"- path: `{tool['path']}`", f"- binary sha256: `{tool['sha256']}` "
           f"({'MATCH' if tool['sha256'] == PINNED_SHA else '**MISMATCH**'} against TOOLING.md)",
           "- `-version`:", "", "```", version, "```", "",
           "## 4. Exact argv, every invocation", "", "```"]
    for stem, argv, code in argv_log:
        log.append(f"{argv}   # exit={code}   -> raw/{args.run_id}/{stem}.*.txt")
    log += ["```", "", "## 5. Object used for M3 (mechanical rule, PRE-REGISTRATION §3.1)", "",
            "| item | object | object source |", "|---|---|---|"]
    seen = set()
    for r in rows:
        if r["mode"] == "M3" and r["model"] not in seen:
            seen.add(r["model"])
            log.append(f"| {r['item_id']} | {r['object'] or '*(none — n/a)*'} | {r['model']} |")
    log.append("")
    (HERE / "run-log.md").write_text("\n".join(log))
    print(f"\nwrote {len(rows)} rows to results.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
