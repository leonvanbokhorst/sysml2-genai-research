# Reconciliation after the Gate-2 corrections

Frozen population (`errors.csv`, never edited): **14 records**.
Post-inspection arm (`errors-post-inspection.csv`, never edited): **7 rows**, of which **1 withdrawn** (C01) → **6 live**.
Corrected combined population (`errors-combined.csv`): **19 records**.

| Population | Records | Models with ≥1 | Models clean |
|---|---|---|---|
| frozen | 14 | 12 | 6 |
| post-inspection (live) | 6 | 6 | 12 |
| combined (corrected) | 19 | 14 | 4 |

## Class counts, frozen vs corrected combined

| Class | Frozen | Combined (corrected) |
|---|---|---|
| I1 | 1 | 1 |
| N1 | 5 | 4 |
| N2 | 1 | 1 |
| R1 | 2 | 2 |
| S1 | 3 | 8 |
| S2 | 1 | 1 |
| T1 | 1 | 1 |
| T2 | 0 | 1 |

## Records touched by a correction

| Record | Correction | Field | Old → New |
|---|---|---|---|
| T5-C3-P01 | C01 | row | withdrawn |
| T3-C2-E01 | C02 | line_range | `23,33` → `23,24,33` |
| T3-C2-E01 | C03 | evidence_excerpt | `port in;` → `port in; / port out; / line.in` |
| T4-C1-E01 | C04 | line_range | `42-44` → `42-43` |
| T4-C1-E02 | C05 | layer | `structural/architectural` → `type/typing` |
| T4-C3-E01 | C06 | layer | `structural/architectural` → `type/typing` |
| T1-C3-E01 | C07 | status | `frozen` → `frozen_contested` |
| T1-C2-E01 | C08 | spec_constraint | `checkSatisfyRequirementUsageBindingConnector (8.3.21.10)` → `SatisfyRequirementUsage textual production (SysML 2.0 §8.2.2.21.2)` |
| T2-C1-E01 | C09 | spec_constraint | `TransitionUsage textual notation (8.3.18.9)` → `States textual notation, transition productions (SysML 2.0 §8.2.2.18)` |
| T5-C3-P02 | C10 | notes | `An attribute usage is typed by a PartDefinition (VisibilityWindow) ins` → `An attribute usage is typed by a PartDefinition (VisibilityWindow) ins` |
| T1-C1-E01 | C12 | row | withdrawn |
| T4-C1-E02 | C14 | status | `frozen` → `frozen_contested` |
| T4-C3-E01 | C15 | status | `frozen` → `frozen_contested` |
| T6-C2-E01 | C16 | line_range | `40` → `40,42` |
