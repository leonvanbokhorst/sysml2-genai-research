#!/usr/bin/env python3
"""Coder A's labels for the 18-model pilot corpus, encoded as data.

Writes coding/errors.csv (one row per distinct defect mechanism) and coding/models.csv
(one row per model, including the zero-error models, so the denominator is auditable).
Also writes coding/omissions.csv: coverage/omission observations kept deliberately OUTSIDE
the error population (METHODOLOGY-FROZEN.md §10).

Labels follow CODEBOOK.md v1.0. Detection columns in models.csv are filled later by
detection/run_detection.py; this script leaves them empty.

Usage: python3 research/issue-007/coding/labels.py
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent

FIELDS = ["model_id", "error_id", "class", "layer", "severity",
          "evidence_excerpt", "line_range", "spec_constraint", "notes"]

ERRORS = [
    # model, class, layer, severity, excerpt, lines, constraint, notes
    ("T1-C1", "N1", "name resolution", "blocking",
     "first start;", "64", "",
     "No action usage named 'start' is declared; declared actions are sense/compare/openValve/"
     "runPump/closeValve. The succession source is a dangling reference. confidence=high"),
    ("T1-C2", "S1", "syntax/parse", "blocking",
     "satisfy greenhouse to moistureControl;", "41",
     "checkSatisfyRequirementUsageBindingConnector (8.3.21.10)",
     "Operand order reversed and 'to' used instead of 'by'; the notation is 'satisfy <req> by "
     "<feature>'. confidence=high"),
    ("T1-C3", "I1", "semantic/behavioural", "minor",
     "doc /* Soil moisture shall be kept between 35% and 75% ... */ / attribute upperBound : Real = 55.0;",
     "37-39", "",
     "The requirement's own documentation and its own attribute declare different upper bounds. "
     "The prompt-fidelity deviation is NOT counted (exclusion 1). confidence=high"),
    ("T2-C1", "S1", "syntax/parse", "blocking",
     "transition from idle to lowering on detection.approaching;", "48-51",
     "TransitionUsage textual notation (8.3.18.9)",
     "4 occurrences (lines 48-51) of SysML v1/UML 'from ... to ... on/when' transition notation. "
     "Names inside the unparsed spans (detection, leftArm) are not double-coded (precedence 2). "
     "confidence=high"),
    ("T2-C2", "S2", "constraint/OCL", "minor",
     "satisfy lowerBeforeArrival;", "33",
     "checkSatisfyRequirementUsageBindingConnector (8.3.21.10)",
     "The 'by' clause is OPTIONAL in the BNF (SysML 2.0 formal/2026-03-02, 8.2.2.21.2), so this "
     "is not a parse defect: it is a satisfy usage with no satisfying feature, violating the "
     "discretionary check constraint that requires a binding from the subject parameter. "
     "Relabelled from syntax/blocking to constraint/minor in codebook v1.1 after the BNF was "
     "retrieved. confidence=high (grammar read directly)"),
    ("T3-C1", "N2", "name resolution", "blocking",
     "attribute innerDiameter : Real;", "4,5,9,10,14,15,19,20,32", "",
     "No library import at all; 10 occurrences (6x Real, 4x Boolean) are unresolved standard-"
     "library scalar types. Counted once per model (coding unit). confidence=high"),
    ("T3-C2", "S1", "syntax/parse", "blocking",
     "port in;", "23,33",
     "",
     "'in' is a reserved feature-direction keyword used as a declared port name (line 23) and "
     "then referenced as a chain (line 33, line.in). 2 occurrences, one mechanism. "
     "confidence=medium"),
    ("T3-C2", "N1", "name resolution", "blocking",
     "satisfy alarmTiming by pump;", "44", "",
     "'pump' exists only as the subject parameter of requirement def AlarmTiming (line 37); there "
     "is no part usage pump in the package, so the satisfy's satisfying feature does not resolve. "
     "confidence=high"),
    ("T4-C1", "T1", "type/typing", "major",
     "first checkCharge; / then checkAvailability; / then assign;", "42-44", "",
     "checkCharge, checkAvailability and assign are declared as action DEFINITIONS at lines "
     "47-49; a succession requires action USAGES. 3 occurrences, one mechanism. confidence=medium"),
    ("T4-C1", "R1", "structural/architectural", "major",
     "connection powerLink connect controller.fleet.battery.power to controller.fleet.dock.power;",
     "51", "validateFeatureEndMultiplicity (8.3.3.3.4) - adjacent, not decisive",
     "fleet is Agv[10]; the connector end traverses a multi-valued usage, so the connector does "
     "not relate individual features. No named constraint decides chains over multi-valued "
     "usages, so this is coded as a structural defect from the model text. confidence=medium"),
    ("T4-C2", "N1", "name resolution", "blocking",
     "satisfy returnToDock by fleet;", "32", "",
     "'fleet' exists only as the subject parameter of requirement def ReturnToDockBelowFifteen "
     "(line 25); no part usage is declared in the package. confidence=high"),
    ("T4-C3", "R1", "structural/architectural", "major",
     "connection batteryToDock connect fleet.vehicles.battery.power to fleet.stations.power;",
     "56", "validateFeatureEndMultiplicity (8.3.3.3.4) - adjacent, not decisive",
     "vehicles is Agv[10] and stations is DockingStation[4]; both ends traverse multi-valued "
     "usages. confidence=medium"),
    ("T5-C2", "N1", "name resolution", "blocking",
     "satisfy insideWindow by station;", "32", "",
     "'station' exists only as the subject parameter of requirement def InsideVisibilityWindow "
     "(line 26); the model's only instance is 'gs : GroundStation' (line 46). confidence=high"),
    ("T6-C2", "N1", "name resolution", "blocking",
     "satisfy maintainTemperature by heating;", "40", "",
     "'heating' exists only as the subject parameter of requirement def MaintainIndoorTemperature "
     "(line 33); no part usage is declared. confidence=high"),
]

MODELS = [
    # model, task, config, wrapper_status, preamble, n_errors, classes
    ("T1-C1", "T1", "C1", "fenced", "yes", "N1"),
    ("T1-C2", "T1", "C2", "fenced", "no", "S1"),
    ("T1-C3", "T1", "C3", "fenced", "no", "I1"),
    ("T2-C1", "T2", "C1", "fenced", "yes", "S1"),
    ("T2-C2", "T2", "C2", "fenced", "no", "S2"),
    ("T2-C3", "T2", "C3", "fenced", "no", ""),
    ("T3-C1", "T3", "C1", "fenced", "no", "N2"),
    ("T3-C2", "T3", "C2", "fenced", "no", "N1;S1"),
    ("T3-C3", "T3", "C3", "fenced", "no", ""),
    ("T4-C1", "T4", "C1", "fenced", "yes", "T1;R1"),
    ("T4-C2", "T4", "C2", "fenced", "no", "N1"),
    ("T4-C3", "T4", "C3", "fenced", "no", "R1"),
    ("T5-C1", "T5", "C1", "fenced", "no", ""),
    ("T5-C2", "T5", "C2", "fenced", "yes", "N1"),
    ("T5-C3", "T5", "C3", "fenced", "no", ""),
    ("T6-C1", "T6", "C1", "fenced", "no", ""),
    ("T6-C2", "T6", "C2", "fenced", "no", "N1"),
    ("T6-C3", "T6", "C3", "fenced", "no", ""),
]

OMISSIONS = [
    # model, observation, why it is not an error
    ("T4-C2", "Model defines parts only as definitions; no system instance exists, which is what "
               "the satisfy then tries to name.", "Omission/coverage, not a text defect; the "
               "unresolved reference it causes IS coded as N1."),
    ("T6-C2", "No instance of HeatingSystem is declared.", "Omission/coverage only; N1 covers the "
               "defect it causes."),
    ("T4-C1", "No transport job element is modelled although the prompt mentions job assignment.",
     "Coverage of the prompt, not well-formedness (exclusion 1)."),
    ("T5-C1", "Antenna pointing is not constrained in the model, only described in documentation.",
     "Coverage/elaboration, not a text defect."),
]


def main() -> None:
    rows, eid = [], {}
    for (model, cls, layer, sev, excerpt, lines, constraint, notes) in ERRORS:
        eid[model] = eid.get(model, 0) + 1
        rows.append({"model_id": model, "error_id": f"{model}-E{eid[model]:02d}",
                     "class": cls, "layer": layer, "severity": sev,
                     "evidence_excerpt": excerpt, "line_range": lines,
                     "spec_constraint": constraint, "notes": notes})
    with (HERE / "errors.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)

    by_model = {r["model_id"]: [] for r in rows}
    for r in rows:
        by_model[r["model_id"]].append(r["class"])
    mfields = ["model_id", "task", "configuration", "wrapper_status", "preamble_present",
               "n_errors", "error_classes", "parses_as_is", "raw_only_invalid"]
    with (HERE / "models.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=mfields)
        w.writeheader()
        for (model, task, cfg, wrap, pre, classes) in MODELS:
            w.writerow({"model_id": model, "task": task, "configuration": cfg,
                        "wrapper_status": wrap, "preamble_present": pre,
                        "n_errors": len(by_model.get(model, [])),
                        "error_classes": ";".join(by_model.get(model, [])),
                        "parses_as_is": "", "raw_only_invalid": ""})

    with (HERE / "omissions.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["model_id", "observation", "why_not_an_error"])
        w.writerows(OMISSIONS)

    from collections import Counter
    print(f"errors: {len(rows)} in {len({r['model_id'] for r in rows})} models")
    print("by class:", dict(Counter(r["class"] for r in rows)))
    print("by layer:", dict(Counter(r["layer"] for r in rows)))
    print("by severity:", dict(Counter(r["severity"] for r in rows)))
    print("zero-error models:", sum(1 for m in MODELS if m[5] == ""))


if __name__ == "__main__":
    main()
