#!/usr/bin/env python3
"""Cross-check the catalogue against the pilot validator inventory.

Inputs:
  classified.csv            the catalogue (623 named constraints)
  validator-inventory.csv   one row per @Check method, with the constraint names
                            the pilot's own source attributes to it

Output: validator-coverage.json

WHAT THIS MEASURES.  This is **identifier coverage**: the number of catalogue
constraint names that the pilot's source attributes to a check, matched exactly
after normalising the pilot's annotations.  It is NOT implementation coverage,
enforcement coverage or conformance coverage.  A name in a comment or a
diagnostic-code constant does not demonstrate that the check executes, that it
executes correctly, or that it would fire on a violating model.  No validator was
built or run for this study.

Two further limits are recorded rather than repaired:
  * 7 of the 156 matches occur only in TODO-only @Check methods (no executable
    enforcement), so the non-TODO exact-name match count is 149.
  * the pilot has targeted KerML 1.1 Beta 2 / SysML 2.1 Beta 2 since 2026-07,
    whose normative text is unpublished.  An unmatched pilot identifier is not
    necessarily implementation-specific.

Matching is exact on the constraint identifier after stripping the pilot's
trailing underscore convention and the "[TODO]" annotation.  This is a lower
bound: the pilot demonstrably uses older or differently spelled identifiers for
some constraints (e.g. validateReferenceUsageIsReferential vs
validateReferenceUsageIsReference), and it may implement a condition under
another constraint's diagnostic code.
"""

import csv, json
from pathlib import Path

here = Path(__file__).resolve().parent
cat = list(csv.DictReader(open(here / "classified.csv")))
inv = list(csv.DictReader(open(here / "validator-inventory.csv")))
names = {r["name"] for r in cat}

implemented, todo = set(), set()
for row in inv:
    for tok in row["constraint_implemented"].split(";"):
        tok = tok.strip()
        if not tok or tok == "none_named_in_source":
            continue
        if "[TODO]" in tok:
            todo.add(tok.replace("[TODO]", "").strip().rstrip("_"))
        else:
            implemented.add(tok.rstrip("_"))

named = implemented | todo
matched = named & names
matched_non_todo = matched & implemented
matched_todo_only = matched - implemented
unmatched = sorted(named - names)

out = {
    "measure": "identifier coverage only; not implementation, enforcement or conformance coverage",
    "runtime_tested": False,
    "catalogue_total": len(cat),
    "validator_distinct_identifier_names": len(named),
    "catalogue_identifiers_matched_exactly": len(matched),
    "matched_in_active_check": len(matched_non_todo),
    "matched_only_in_todo_methods": len(matched_todo_only),
    "identifier_coverage_ratio": round(len(matched) / len(cat), 4),
    "identifier_coverage_note": (
        "156/623 = 25.0% of catalogue names appear in the pilot's own validation "
        "source, 149 of them in non-TODO methods. This does not demonstrate "
        "execution, correct enforcement, or conformance; it is name matching "
        "across a 2.0/2.1 revision skew."
    ),
    "by_spec_kind": {},
    "validator_names_not_in_catalogue": unmatched,
    "todos_named_in_catalogue": sorted((todo & names)),
    "catalogue_names_only_reached_via_todo": sorted(matched_todo_only),
}

for spec in ("SysML 2.0", "KerML 1.0"):
    for kind in ("derive", "check", "validate"):
        rs = [r for r in cat if r["spec"] == spec and r["kind"] == kind]
        non = [r for r in rs if r["name"] in implemented]
        only = [r for r in rs if r["name"] in matched_todo_only]
        out["by_spec_kind"][f"{spec} / {kind}"] = {
            "catalogue": len(rs),
            "matched_in_active_check": len(non),
            "matched_only_in_todo_methods": len(only),
            "identifier_coverage": len(non) + len(only),
        }

with open(here / "validator-coverage.json", "w") as f:
    json.dump(out, f, indent=2)
print(json.dumps({k: out[k] for k in (
    "catalogue_total", "validator_distinct_identifier_names",
    "catalogue_identifiers_matched_exactly",
    "matched_in_active_check", "matched_only_in_todo_methods")}, indent=2))
print(json.dumps(out["by_spec_kind"], indent=2))
