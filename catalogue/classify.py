#!/usr/bin/env python3
"""Apply the frozen dependency-class frame and produce the catalogue.

This is the reproducible backbone of the classification.  It implements the
decision rules from catalogue/coding/codebook.md, using only signals that a
third party can re-derive from the pinned XMI:

  A  dependency class A: model-local
     -> no model-library literal, no library helper, no library-path resolution.
        This is a claim about what a checker needs, not that the published OCL
        executes as written.
  B  dependency class B: library/semantic dependency
     -> a quoted 'Package::Element' literal (other than a metamodel enumeration),
        a library helper call, or resolution against a library path
  U  undecidable as published
     -> the OCL body is a placeholder (e.g. TBD)

The script records executability separately in `executable_ocl_status`, derived
from the curated `ocl-defects.csv`; it does not change the dependency class.

Class C (informative only) and D (absent) live in separate registers; C is
derived in extract_constraints.py (pdf-only-names.csv) and D is the
specification-silence register.

The script also writes the obligation dimension taken from the specification's
own 8.3.1 taxonomy: derive = "shall always enforce", check = "may ... report ...
or ignore", validate = "should report".  That dimension is independent of A/B.

Usage:
    python3 classify.py [--catalogue constraints.csv] [--defects ocl-defects.csv] [--out classified.csv]
"""

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

CLASS_LABEL = {
    "A": "dependency class A — model-local (no external library/semantic dependency; intended decidable from the abstract syntax)",
    "B": "dependency class B — library/semantic dependency (requires the normative model library or semantic layer)",
    "U": "undecidable as published — placeholder body",
}

OBLIGATION = {
    "derive": "SHALL enforce (derivation is mandatory for a conformant abstract-syntax tool)",
    "check": "MAY report, satisfy by implied relationships, or ignore (explicitly discretionary)",
    "validate": "SHOULD report violations",
}


def classify(row):
    if (row["ocl_body"] or "").strip().upper() in ("TBD", ""):
        return "U", "placeholder or empty OCL body"
    lib = row["uses_library_literal"] == "1" or row["uses_library_helper"] == "1"
    if lib:
        return "B", "names a model-library element or library helper"
    if row["uses_resolution"] == "1":
        return "A", "model-level name resolution only (no library element)"
    return "A", "OCL over metamodel properties and standard OCL only"


def main():
    ap = argparse.ArgumentParser()
    here = Path(__file__).resolve().parent
    ap.add_argument("--catalogue", type=Path, default=here / "constraints.csv")
    ap.add_argument("--defects", type=Path, default=here / "ocl-defects.csv")
    ap.add_argument("--out", type=Path, default=here / "classified.csv")
    ap.add_argument("--summary", type=Path, default=here / "classification-summary.json")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.catalogue)))
    defects = defaultdict(list)
    if args.defects.exists():
        for d in csv.DictReader(open(args.defects)):
            defects[d["name"]].append(d)

    out = []
    for r in rows:
        cls, basis = classify(r)
        dr = defects.get(r["name"], [])
        high = [d for d in dr if d.get("confidence") == "high"]
        row = dict(r)
        row["class"] = cls
        row["class_label"] = CLASS_LABEL[cls]
        row["class_basis"] = basis
        row["obligation"] = OBLIGATION[r["kind"]]
        row["published_ocl_defects"] = len(dr)
        row["high_confidence_ocl_defects"] = len(high)
        # Separate dimension: the dependency class does NOT assert that the
        # published OCL executes as written.  This column records the shallow
        # audit result independently.
        if high:
            row["executable_ocl_status"] = "defective as published (high-confidence defect)"
        elif dr:
            row["executable_ocl_status"] = "possible defect (medium-confidence only)"
        else:
            row["executable_ocl_status"] = "no known defect found (not a proof of executability)"
        out.append(row)

    cols = list(rows[0].keys()) + [
        "class", "class_label", "class_basis", "obligation", "published_ocl_defects",
        "high_confidence_ocl_defects", "executable_ocl_status",
    ]
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(out)

    summary = {
        "total": len(out),
        "by_spec_kind_class": {},
        "by_spec_kind": {},
        "by_class": dict(Counter(r["class"] for r in out)),
        "by_executable_ocl_status": dict(Counter(r["executable_ocl_status"] for r in out)),
        "by_obligation": dict(Counter(r["obligation"] for r in out)),
        "constraints_with_published_defect": sum(1 for r in out if r["published_ocl_defects"]),
        "constraints_with_high_confidence_defect": sum(1 for r in out if int(r["high_confidence_ocl_defects"])),
    }
    for key in ("by_spec_kind", "by_spec_kind_class"):
        d = defaultdict(Counter)
        for r in out:
            k = (r["spec"], r["kind"])
            if key == "by_spec_kind":
                d[k]["n"] += 1
            else:
                d[k][r["class"]] += 1
        summary[key] = {f"{s} / {k}": dict(v) for (s, k), v in sorted(d.items())}

    with open(args.summary, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(json.dumps({k: summary[k] for k in ("total", "by_class", "constraints_with_published_defect", "constraints_with_high_confidence_defect")}, indent=2))
    print(json.dumps(summary["by_spec_kind_class"], indent=2))


if __name__ == "__main__":
    main()
