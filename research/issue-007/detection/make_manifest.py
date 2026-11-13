#!/usr/bin/env python3
"""Two record-keeping artefacts Reviewer B asked for (O11, O13), computed offline.

1. detection/occurrence_detection.csv — occurrence-level detection for the multi-occurrence
   records, so "detected" can be read as "the tool saw k of n occurrences".
2. detection/manifest.json — per-file sha256, tool identity and argv for every artefact the
   detection run touched (frozen plan §7.2 asked for this; the raw/*.txt files carry only argv
   and exit code and are left byte-identical).

Usage: python3 research/issue-007/detection/make_manifest.py
"""
import csv
import hashlib
import json
import subprocess
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPO = ROOT.parent.parent
TOOL = REPO / ".tools" / "sysml"

# occurrence lines per record, read from the corrected population (see coding/errors-corrections.csv)
OCCURRENCES = {
    "T2-C1-E01": [48, 49, 50, 51],          # four transitions
    "T3-C1-E01": [4, 5, 9, 10, 14, 15, 19, 20, 32],   # Real/Boolean uses
    "T3-C2-E01": [23, 24, 33],              # port in; port out; line.in
    "T4-C1-E01": [42, 43],                  # first checkCharge; then checkAvailability;
    "T6-C2-E01": [40, 42],                  # satisfy by heating; two connection ends at 42
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    version = subprocess.run([str(TOOL), "-version"], capture_output=True, text=True).stdout.strip()
    diag = defaultdict(set)
    for d in csv.DictReader((HERE / "diagnostics.csv").open(encoding="utf-8")):
        if d["scope"] == "normalised":
            diag[d["artifact"].replace(".normalised", "")].add(int(d["line"]))

    rows = []
    for eid, lines in OCCURRENCES.items():
        model = eid.split("-E")[0]
        seen = [ln for ln in lines if ln in diag.get(model, set())]
        rows.append({"error_id": eid, "model_id": model,
                     "occurrences": len(lines), "occurrence_lines": " ".join(map(str, lines)),
                     "occurrences_flagged": len(seen),
                     "flagged_lines": " ".join(map(str, seen)),
                     "occurrence_complete": "yes" if len(seen) == len(lines) else "no"})
    with (HERE / "occurrence_detection.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    artefacts = []
    for scope, pattern in (("normalised", ROOT / "corpus" / "normalized" / "*.sysml"),
                           ("raw", ROOT / "raw" / "*.md"),
                           ("external", HERE / "external" / "*.sysml"),
                           ("probe", HERE / "probes" / "*.sysml")):
        for p in sorted(pattern.parent.glob(pattern.name)):
            artefacts.append({"scope": scope, "file": str(p.relative_to(REPO)),
                              "sha256": sha(p), "bytes": p.stat().st_size})
    manifest = {
        "instrument": {"path": str(TOOL.relative_to(REPO)),
                       "sha256": sha(TOOL),
                       "version_output": version},
        "argv": [str(TOOL.relative_to(REPO)), "-validate", "<file>"],
        "note": "per-file sha256 for every artefact the detection run touched; the raw/*.txt "
                "outputs are byte-identical to the ones pinned in B-reviews-A.md",
        "artefacts": artefacts,
    }
    (HERE / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"occurrence rows: {len(rows)}; artefacts hashed: {len(artefacts)}")
    for r in rows:
        print(f"  {r['error_id']}: {r['occurrences_flagged']}/{r['occurrences']} occurrences flagged")


if __name__ == "__main__":
    main()
