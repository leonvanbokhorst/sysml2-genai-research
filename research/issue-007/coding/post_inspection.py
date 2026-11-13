#!/usr/bin/env python3
"""Post-inspection additions: defects verified against the normative BNF but found only after
the detection run drew attention to them.

PROVENANCE RULE (important, stated in the report): these records are NOT part of the frozen
pre-detection population in errors.csv, and they were not accepted on a validator's authority.
Each was verified against the SysML 2.0 textual notation itself: the reserved-keyword list in
§8.2.2.1.2 (formal/2026-03-02) and the attribute-typing constraint
`checkAttributeUsageSpecialization` (§8.3.7.3). The validator's diagnostic only made me look.

Writes: coding/errors-post-inspection.csv, coding/errors-combined.csv, and adds two columns to
coding/models.csv (n_errors_post_inspection, classes_post_inspection).

Usage: python3 research/issue-007/coding/post_inspection.py
"""
import csv
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIELDS = ["model_id", "error_id", "class", "layer", "severity",
          "evidence_excerpt", "line_range", "spec_constraint", "notes",
          "discovery_route", "verification"]

ADDED = [
    ("T2-C2", "S1", "syntax/parse", "blocking",
     "attribute state : String;", "17",
     "SysML 2.0 §8.2.2.1.2 reserved-keyword list ('state')",
     "Reserved keyword used as an unquoted feature name; the ID terminal does not admit it. "
     "Independent of the S2 record on line 33. confidence=high",
     "detection run surfaced; verified against the reserved-keyword list"),
    ("T4-C1", "S1", "syntax/parse", "blocking",
     "action def assign; / then assign;", "44,49",
     "SysML 2.0 §8.2.2.1.2 reserved-keyword list ('assign'); §8.2.2.17 AssignActionUsage",
     "'assign' is a reserved keyword: `then assign;` parses as an assignment operator and the "
     "declaration `action def assign;` is not a name. This is separate from the kind mismatch on "
     "lines 42-43 (T1 record). confidence=high",
     "detection run surfaced; verified against the reserved-keyword list"),
    ("T5-C3", "S1", "syntax/parse", "blocking",
     "port return;", "26",
     "SysML 2.0 §8.2.2.1.2 reserved-keyword list ('return')",
     "Reserved keyword as an unquoted port name. confidence=high",
     "detection run surfaced; verified against the reserved-keyword list"),
    ("T5-C3", "T2", "type/typing", "major",
     "attribute window : VisibilityWindow;", "11",
     "checkAttributeUsageSpecialization (8.3.7.3)",
     "An attribute usage is typed by a PartDefinition (VisibilityWindow) instead of a value/"
     "attribute type; an AttributeUsage must specialize Base::dataValues. confidence=high",
     "detection run surfaced; verified against the catalogue constraint"),
    ("T6-C1", "S1", "syntax/parse", "blocking",
     "port return;", "26",
     "SysML 2.0 §8.2.2.1.2 reserved-keyword list ('return')",
     "Reserved keyword as an unquoted port name. confidence=high",
     "detection run surfaced; verified against the reserved-keyword list"),
    ("T6-C2", "S1", "syntax/parse", "blocking",
     "port return;", "22",
     "SysML 2.0 §8.2.2.1.2 reserved-keyword list ('return')",
     "Reserved keyword as an unquoted port name. confidence=high",
     "detection run surfaced; verified against the reserved-keyword list"),
    ("T6-C3", "S1", "syntax/parse", "blocking",
     "port return;", "26",
     "SysML 2.0 §8.2.2.1.2 reserved-keyword list ('return')",
     "Reserved keyword as an unquoted port name. confidence=high",
     "detection run surfaced; verified against the reserved-keyword list"),
]

EXTENDED = [
    ("T3-C2", "T3-C2-E01", "S1",
     "port in; (line 23) and port out; (line 24) are both reserved keywords used as feature "
     "names; the frozen record listed only 'in'. Occurrence count corrected from 1 to 2; class, "
     "layer and severity unchanged."),
    ("T4-C1", "T4-C1-E01", "T1",
     "The frozen T1 record's excerpt spanned lines 42-44 and mentioned 'assign'. After §8.2.2.1.2 "
     "was checked, 'assign' is a reserved keyword (own record, S1) and the kind mismatch is "
     "confined to `first checkCharge` / `then checkAvailability` (lines 42-43). The class and "
     "severity are unchanged; the span and note are corrected here."),
]


def main() -> None:
    frozen = list(csv.DictReader((HERE / "errors.csv").open(encoding="utf-8")))
    added = []
    per_model = Counter(r["model_id"] for r in frozen)
    for (model, cls, layer, sev, excerpt, lines, constraint, notes, route) in ADDED:
        per_model[model] += 1
        added.append({"model_id": model, "error_id": f"{model}-P{per_model[model]:02d}",
                      "class": cls, "layer": layer, "severity": sev,
                      "evidence_excerpt": excerpt, "line_range": lines,
                      "spec_constraint": constraint, "notes": notes,
                      "discovery_route": "detection run surfaced the candidate (NOT the criterion)",
                      "verification": route})

    with (HERE / "errors-post-inspection.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(added)

    combined = [{**r, "population": "frozen_pre_detection"} for r in frozen] + \
               [{**r, "population": "post_inspection_verified"} for r in added]
    with (HERE / "errors-combined.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS + ["population"])
        w.writeheader()
        w.writerows(combined)

    # models.csv: add post-inspection columns without touching the frozen ones
    models_path = HERE / "models.csv"
    rows = list(csv.DictReader(models_path.open(encoding="utf-8")))
    fields = list(rows[0].keys())
    for extra in ("n_errors_post_inspection", "classes_post_inspection"):
        if extra not in fields:
            fields.append(extra)
    by_model = {}
    for r in combined:
        by_model.setdefault(r["model_id"], []).append(r["class"])
    for r in rows:
        r["n_errors_post_inspection"] = str(len(by_model.get(r["model_id"], [])))
        r["classes_post_inspection"] = ";".join(sorted(by_model.get(r["model_id"], [])))
    with models_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print("frozen records:", len(frozen), "| added:", len(added),
          "| combined:", len(combined))
    print("combined models with >=1 error:", len(by_model), "of 18")
    print("combined class counts:", dict(Counter(r["class"] for r in combined)))
    print("combined layer counts:", dict(Counter(r["layer"] for r in combined)))
    print("combined severity:", dict(Counter(r["severity"] for r in combined)))
    for (m, rec_id, cls, note) in sorted(EXTENDED, key=lambda x: x[0]):
        print(f"correction {m} {rec_id} [{cls}]: {note[:90]}...")


if __name__ == "__main__":
    main()
