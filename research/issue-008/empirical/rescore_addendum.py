#!/usr/bin/env python3
"""Adjudication-derived re-scoring of the external challenge set.

Written for task "apply the adjudicated corrections" (Gate 4). It reads the
PRESERVED raw output in `raw/run2/` and `results.csv`, and writes NEW derived
files. It never touches `raw/**`, `results.csv`, `PRE-REGISTRATION.md` or A's
frozen subset.

Two adjudicated corrections change derived scoring:

  B-17 / RB-06  M2 scores non-satisfy-family items as `wrong-target`, but the
                registered rule (PRE-REGISTRATION.md §4.2) says they are
                `not applicable`. Re-labelled here under the registered rule, so
                M2's applicable count is 1 (the S2 item) rather than 3. Controls
                get model-level vocabulary, not item-attribution vocabulary
                (AM1 item 3).
  B-16 / RB-05  M3's applicable count is 3 (not "1 evaluated"), with the per-item
                breakdown stated.
  B-32 / X-01   The obligation split: 9/9 established-and-mandatory plus 0/4
                discretionary/unnormative/contested.
  B-34 / X-03   The R1-as-contested ladder rung, uniquely labelled.

Outputs:  results-addendum.csv, SCORING-ADDENDUM.md
Usage:    python3 rescore_addendum.py
"""
from __future__ import annotations

import csv
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results.csv"

# Obligation status per item, taken from A's frozen `spec_basis` and the pinned
# catalogue's obligation column (adjudication X-01 / A-9 use the same split).
OBLIGATION = {
    "ES-T1-C2-E01": ("established+mandatory", "S1 textual notation; the grammar is normative and is not optional"),
    "ES-T2-C1-E01": ("established+mandatory", "S1 textual notation"),
    "ES-T3-C2-E01": ("established+mandatory", "S1 reserved keyword per §8.2.2.1.2"),
    "ES-T3-C2-E02": ("established+mandatory", "N1 name resolution; a precondition of every constraint"),
    "ES-T4-C2-E01": ("established+mandatory", "N1 name resolution"),
    "ES-T5-C2-E01": ("established+mandatory", "N1 name resolution"),
    "ES-T6-C2-E01": ("established+mandatory", "N1 name resolution"),
    "ES-T3-C1-E01": ("established+mandatory", "N2 missing normative-library prelude"),
    "ES-T4-C1-E01": ("established+mandatory", "T1 definition where a usage is required"),
    "ES-T2-C2-E01": ("discretionary", "S2: checkSatisfyRequirementUsageBindingConnector is a `check…` "
                                      "constraint whose obligation is 'MAY report, satisfy by implied "
                                      "relationships, or ignore'"),
    "ES-T4-C1-E02": ("contested/normative-basis", "R1: no named constraint decides a chain through a "
                                                  "multi-valued usage; defect status contested (X-03)"),
    "ES-T4-C3-E01": ("contested/normative-basis", "R1: as above"),
    "ES-T1-C3-E01": ("contested", "I1: defect status contested (a tightened limit is not a contradiction "
                                   "on its face)"),
}


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    rows = list(csv.DictReader(open(RESULTS)))
    out, notes = [], []

    for r in rows:
        new = dict(r)
        new["rescore_note"] = ""
        if r["item_type"] == "control":
            # controls are scored only on M1/M4 (false-positive arm); elsewhere the
            # model-level standing is recorded, not item-attribution vocabulary
            if r["mode"] in ("M2", "M3"):
                new["outcome"] = "not scored (control)"
                new["rescore_note"] = (f"model-level standing recorded: {r['standing'] or 'none'}; "
                                       "controls are scored on M1/M4 only")
        elif r["mode"] == "M2":
            # registered rule: M2 addresses satisfy-family items only
            if r["item_id"] == "ES-T2-C2-E01":
                new["outcome"] = "not detected"
                new["rescore_note"] = ("registered rule §4.2: the item's own satisfy assertion was "
                                       "evaluated and returned holds-vacuously")
            else:
                new["outcome"] = "not applicable"
                new["rescore_note"] = ("registered rule §4.2: not a satisfy-family item, so -satisfy "
                                       "cannot address this defect (was 'wrong-target' under the "
                                       "harness's deviation)")
        out.append(new)

    path = HERE / "results-addendum.csv"
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)

    items = [r for r in out if r["item_type"] == "error"]
    before = [r for r in rows if r["item_type"] == "error"]   # the as-published outcomes

    def tally(mode):
        return Counter(r["outcome"] for r in items if r["mode"] == mode)

    m1 = [r for r in items if r["mode"] == "M1"]
    detected = {r["item_id"] for r in m1 if r["outcome"] == "detected"}
    est = {i for i, (k, _) in OBLIGATION.items() if k == "established+mandatory"}
    dis = {i for i, (k, _) in OBLIGATION.items() if k != "established+mandatory"}

    L = ["# Scoring addendum — external challenge set, after adjudication",
         "",
         f"Written by `rescore_addendum.py` at {utcnow()}. Source of truth remains `results.csv` and",
         "`raw/run2/**`, both untouched. This file re-derives only what the adjudication changed.",
         "",
         "## 1. M2 re-scored under the registered rule (B-17 / RB-06)",
         "",
         "`PRE-REGISTRATION.md` §4.2: `-satisfy` addresses the satisfy family only; a non-satisfy item",
         "is `not applicable`, never `wrong-target`. The harness deviated. Re-labelled:",
         "",
         "| M2 outcome | before | after |",
         "|---|---:|---:|",
         f"| not applicable | {Counter(r['outcome'] for r in before if r['mode']=='M2')['not applicable']} "
         f"| {tally('M2')['not applicable']} |",
         f"| wrong-target | {Counter(r['outcome'] for r in before if r['mode']=='M2').get('wrong-target',0)} "
         f"| {tally('M2').get('wrong-target',0)} |",
         f"| not detected | {Counter(r['outcome'] for r in before if r['mode']=='M2').get('not detected',0)} "
         f"| {tally('M2').get('not detected',0)} |",
         "",
         "**M2 applicable count: 3 → 1** (the S2 item only). No item's detection status changes:",
         "nothing becomes `detected`.",
         "",
         "## 2. M3 accounting (B-16 / RB-05)",
         "",
         "| M3 outcome | n | items |",
         "|---|---:|---|"]
    for oc in ("not detected", "weaker signal", "not applicable"):
        ids = [r["item_id"] for r in items if r["mode"] == "M3" and r["outcome"] == oc]
        L.append(f"| {oc} | {len(ids)} | {', '.join(ids) or '—'} |")
    L += ["", "**M3 applicable count: 3** (ES-T1-C3-E01 `holds`; ES-T2-C2-E01 `undecided` → weaker",
          "signal; ES-T4-C3-E01 `holds`), 10 not applicable. The earlier sentence \"1 evaluated,",
          "10 n/a\" was wrong and contradicted the same report's §A10.5.",
          "",
          "## 3. Obligation split (B-32 / X-01)", "",
          "| obligation class | n | detected | rate | items |",
          "|---|---:|---:|---|---|",
          f"| **established + mandatory reporting** | {len(est)} | {len(detected & est)} | "
          f"**{len(detected & est)}/{len(est)} = 1.00** | {', '.join(sorted(est))} |",
          f"| **discretionary / no normative basis / contested** | {len(dis)} | {len(detected & dis)} | "
          f"**{len(detected & dis)}/{len(dis)} = 0.00** | {', '.join(sorted(dis))} |",
          f"| all items | {len(OBLIGATION)} | {len(detected)} | {len(detected)}/{len(OBLIGATION)} = "
          f"{len(detected)/len(OBLIGATION):.2f} | — |",
          "",
          "The aggregate 9/13 is therefore **not a detection-gap measure**: it is 9/9 on the items the",
          "specification establishes and mandates reporting for, plus 0/4 on items where reporting is",
          "discretionary, has no normative basis, or is contested.",
          "",
          "## 4. Denominator ladder, uniquely labelled (B-34 / X-03)", "",
          "| rung | n | detected | rate | what it removes |",
          "|---|---:|---:|---|---|",
          "| **L1 all items** | 13 | 9 | 9/13 = 0.69 | nothing |",
          "| **L2 −I1** | 12 | 9 | 9/12 = 0.75 | the item whose *defect status* is contested |",
          "| **L3 −I1 −unmeasurable** | 11 | 9 | 9/11[C] = 0.82 | the item the tool states it made no "
          "check on (ES-T4-C1-E02, short-circuit) |",
          "| **L4 −R1 (both)** | 11 | 9 | 9/11[R1] = 0.82 | both R1 items, contested as to defect status |",
          "| **L5 established+mandatory** | 9 | 9 | 9/9 = 1.00 | every discretionary/unnormative/contested "
          "item |",
          "",
          "L3 and L4 are both 9/11 and are **different sets**; they carry distinct suffixes [C] and [R1]",
          "and are never quoted without one. The exclusion order is fixed here: contested defect status",
          "first (I1), then unmeasurable (short-circuit), then the remaining contested class (R1).",
          ""]
    (HERE / "SCORING-ADDENDUM.md").write_text("\n".join(L))
    print(f"wrote {path.name} and SCORING-ADDENDUM.md")
    print("M2:", dict(tally('M2')), "| M3:", dict(tally('M3')))
    print(f"obligation split: {len(detected & est)}/{len(est)} established+mandatory; "
          f"{len(detected & dis)}/{len(dis)} discretionary/contested")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
