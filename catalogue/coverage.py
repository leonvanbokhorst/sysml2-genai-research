#!/usr/bin/env python3
"""Cross-check the catalogue against the pilot validator inventory.

Inputs:
  classified.csv            the catalogue (623 named constraints)
  validator-inventory.csv   one row per @Check method, with the constraint names
                            the pilot's own source attributes to it

Output: validator-coverage.json

Matching is exact on the constraint identifier after stripping the pilot's
trailing underscore convention and the "[TODO]" annotation.  This is a LOWER
BOUND on implementation coverage: the pilot demonstrably uses older or
differently spelled identifiers for some constraints (e.g.
validateReferenceUsageIsReferential vs validateReferenceUsageIsReference), and
it may implement a condition under another constraint's diagnostic code.  Both
are recorded, not silently repaired.  A further and larger limit: the pilot
targets KerML 1.1 Beta 2 / SysML 2.1 Beta 2 from 2026-07, whose normative text
is not published, so an unmatched pilot identifier is not necessarily
implementation-specific.
"""

import csv, json
from collections import Counter
from pathlib import Path

here = Path(__file__).parent
cat = list(csv.DictReader(open(here / "classified.csv")))
inv = list(csv.DictReader(open(here / "validator-inventory.csv")))
names = {r["name"]: r for r in cat}

implemented, todo = set(), set()
for row in inv:
    for tok in row["constraint_implemented"].split(";"):
        tok = tok.strip()
        if not tok or tok == "none_named_in_source":
            continue
        if "[TODO]" in tok:
            todo.add(tok.replace("[TODO]", "").strip())
        else:
            implemented.add(tok.rstrip("_"))

named = implemented | todo
matched = named & set(names)
unmatched = sorted(named - set(names))

out = {
    "catalogue_total": len(cat),
    "catalogue_by_spec_kind": {},
    "covered_by_spec_kind": {},
    "validator_distinct_named_constraints": len(named),
    "validator_names_matching_catalogue_exactly": len(matched),
    "validator_names_not_in_catalogue": unmatched,
    "todos_named_in_catalogue": sorted((todo & set(names))),
    "catalogue_names_only_reached_via_todo": sorted((todo & set(names)) - implemented),
    "note": (
        "Exact-name matching only; lower bound. Pilot targets unpublished 2.1 Beta 2, "
        "so unmatched names are not necessarily implementation-specific."
    ),
}

for spec in ("SysML 2.0", "KerML 1.0"):
    for kind in ("derive", "check", "validate"):
        rs = [r for r in cat if r["spec"] == spec and r["kind"] == kind]
        hit = [r for r in rs if r["name"] in named]
        out["catalogue_by_spec_kind"][f"{spec} / {kind}"] = len(rs)
        out["covered_by_spec_kind"][f"{spec} / {kind}"] = len(hit)

# How many catalogue constraints are matched under *some* pilot identifier that
# is a near-renaming?  Report only exact; leave interpretation to the report.
with open(here / "validator-coverage.json", "w") as f:
    json.dump(out, f, indent=2)
print(json.dumps({k: out[k] for k in (
    "catalogue_total", "validator_distinct_named_constraints",
    "validator_names_matching_catalogue_exactly",
    "validator_names_not_in_catalogue")}, indent=2))
print(json.dumps(out["covered_by_spec_kind"], indent=2))
