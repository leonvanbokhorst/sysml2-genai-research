#!/usr/bin/env python3
"""Draw the stratified 60-constraint sample used for the two-coder agreement study.

Deterministic: random.Random(20261113), 10 constraints per (specification, kind).
The sample file contains no pre-computed class or dependency flags.
"""
import csv, random
from pathlib import Path

rows = list(csv.DictReader(open(Path(__file__).resolve().parents[1] / "constraints.csv")))
rng = random.Random(20261113)
out = []
for spec in ["SysML 2.0", "KerML 1.0"]:
    for kind in ["derive", "check", "validate"]:
        pool = sorted(
            (r for r in rows if r["spec"] == spec and r["kind"] == kind),
            key=lambda r: r["name"],
        )
        for r in rng.sample(pool, min(10, len(pool))):
            out.append(
                {
                    "sample_id": f"{spec.split()[0][:3].upper()}-{kind[:3].upper()}-{len(out)+1:02d}",
                    "spec": r["spec"],
                    "name": r["name"],
                    "kind": r["kind"],
                    "context_metaclass": r["context_metaclass"],
                    "clause": r["pdf_clause"],
                    "prose": r["prose"],
                    "ocl_body": r["ocl_body"],
                }
            )
out.sort(key=lambda r: r["sample_id"])
with open(Path(__file__).parent / "sample.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["sample_id", "spec", "name", "kind", "context_metaclass", "clause", "prose", "ocl_body"], lineterminator="\n")
    w.writeheader(); w.writerows(out)
print(len(out), "rows ->", Path(__file__).parent / "sample.csv")
