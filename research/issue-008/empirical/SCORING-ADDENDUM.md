# Scoring addendum — external challenge set, after adjudication

Written by `rescore_addendum.py` at 2026-11-13T15:05:57Z. Source of truth remains `results.csv` and
`raw/run2/**`, both untouched. This file re-derives only what the adjudication changed.

## 1. M2 re-scored under the registered rule (B-17 / RB-06)

`PRE-REGISTRATION.md` §4.2: `-satisfy` addresses the satisfy family only; a non-satisfy item
is `not applicable`, never `wrong-target`. The harness deviated. Re-labelled:

| M2 outcome | before | after |
|---|---:|---:|
| not applicable | 10 | 12 |
| wrong-target | 2 | 0 |
| not detected | 1 | 1 |

**M2 applicable count: 3 → 1** (the S2 item only). No item's detection status changes:
nothing becomes `detected`.

## 2. M3 accounting (B-16 / RB-05)

| M3 outcome | n | items |
|---|---:|---|
| not detected | 2 | ES-T1-C3-E01, ES-T4-C3-E01 |
| weaker signal | 1 | ES-T2-C2-E01 |
| not applicable | 10 | ES-T1-C2-E01, ES-T2-C1-E01, ES-T3-C1-E01, ES-T3-C2-E01, ES-T3-C2-E02, ES-T4-C1-E01, ES-T4-C1-E02, ES-T4-C2-E01, ES-T5-C2-E01, ES-T6-C2-E01 |

**M3 applicable count: 3** (ES-T1-C3-E01 `holds`; ES-T2-C2-E01 `undecided` → weaker
signal; ES-T4-C3-E01 `holds`), 10 not applicable. The earlier sentence "1 evaluated,
10 n/a" was wrong and contradicted the same report's §A10.5.

## 3. Obligation split (B-32 / X-01)

| obligation class | n | detected | rate | items |
|---|---:|---:|---|---|
| **established + mandatory reporting** | 9 | 9 | **9/9 = 1.00** | ES-T1-C2-E01, ES-T2-C1-E01, ES-T3-C1-E01, ES-T3-C2-E01, ES-T3-C2-E02, ES-T4-C1-E01, ES-T4-C2-E01, ES-T5-C2-E01, ES-T6-C2-E01 |
| **discretionary / no normative basis / contested** | 4 | 0 | **0/4 = 0.00** | ES-T1-C3-E01, ES-T2-C2-E01, ES-T4-C1-E02, ES-T4-C3-E01 |
| all items | 13 | 9 | 9/13 = 0.69 | — |

The aggregate 9/13 is therefore **not a detection-gap measure**: it is 9/9 on the items the
specification establishes and mandates reporting for, plus 0/4 on items where reporting is
discretionary, has no normative basis, or is contested.

## 4. Denominator ladder, uniquely labelled (B-34 / X-03)

| rung | n | detected | rate | what it removes |
|---|---:|---:|---|---|
| **L1 all items** | 13 | 9 | 9/13 = 0.69 | nothing |
| **L2 −I1** | 12 | 9 | 9/12 = 0.75 | the item whose *defect status* is contested |
| **L3 −I1 −unmeasurable** | 11 | 9 | 9/11[C] = 0.82 | the item the tool states it made no check on (ES-T4-C1-E02, short-circuit) |
| **L4 −R1 (both)** | 11 | 9 | 9/11[R1] = 0.82 | both R1 items, contested as to defect status |
| **L5 established+mandatory** | 9 | 9 | 9/9 = 1.00 | every discretionary/unnormative/contested item |

L3 and L4 are both 9/11 and are **different sets**; they carry distinct suffixes [C] and [R1]
and are never quoted without one. The exclusion order is fixed here: contested defect status
first (I1), then unmeasurable (short-circuit), then the remaining contested class (R1).
