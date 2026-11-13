# External challenge set — per item, per pre-registered mode

Generated from `results.csv` (run2) by the analysis step; raw output per cell in `raw/run2/`.
Outcome vocabulary and attribution rules are fixed in `PRE-REGISTRATION.md` §4.
`n/a` = the mode cannot address the item (not applicable); it is never `silent`.

## Error items (n = 13)

| item | model | class | layer | contested | M1 | M2 | M3 | M4 |
|---|---|---|---|---|---|---|---|---|
| ES-T1-C2-E01 | T1-C2 | S1 | syntax/parse | no | detected | not applicable | not applicable | detected |
| ES-T1-C3-E01 | T1-C3 | I1 | semantic/behavioural | yes | silent | wrong-target | not detected | silent |
| ES-T2-C1-E01 | T2-C1 | S1 | syntax/parse | no | detected | not applicable | not applicable | detected |
| ES-T2-C2-E01 | T2-C2 | S2 | constraint/OCL | no | wrong-target | not detected | weaker signal | wrong-target |
| ES-T3-C1-E01 | T3-C1 | N2 | name resolution | no | detected | not applicable | not applicable | detected |
| ES-T3-C2-E01 | T3-C2 | S1 | syntax/parse | no | detected | not applicable | not applicable | detected |
| ES-T3-C2-E02 | T3-C2 | N1 | name resolution | no | detected | not applicable | not applicable | detected |
| ES-T4-C1-E01 | T4-C1 | T1 | type/typing | no | detected | not applicable | not applicable | detected |
| ES-T4-C1-E02 | T4-C1 | R1 | type/typing | yes | wrong-target | not applicable | not applicable | wrong-target |
| ES-T4-C2-E01 | T4-C2 | N1 | name resolution | no | detected | not applicable | not applicable | detected |
| ES-T4-C3-E01 | T4-C3 | R1 | type/typing | yes | silent | wrong-target | not detected | silent |
| ES-T5-C2-E01 | T5-C2 | N1 | name resolution | no | detected | not applicable | not applicable | detected |
| ES-T6-C2-E01 | T6-C2 | N1 | name resolution | no | detected | not applicable | not applicable | detected |

## Controls (4 scored clean-tier, 3 frozen-clean-only reported descriptively)

| control | tier | M1 | M4 | M2 | M3 |
|---|---|---|---|---|---|
| CTRL-T1-C1 | clean | — | — | — | — |
| CTRL-T2-C3 | clean | — | — | — | — |
| CTRL-T3-C3 | clean | — | — | — | — |
| CTRL-T5-C1 | clean | — | — | — | — |
| CTRL-T5-C3 | frozen-clean-only | — | — | — | — |
| CTRL-T6-C1 | frozen-clean-only | — | — | — | — |
| CTRL-T6-C3 | frozen-clean-only | — | — | — | — |

## Detail column (exact codes / standings)

### ES-T1-C2-E01 — T1-C2 (S1)
- **M1** `detected` — exit 2; syntax@41;syntax@41
- **M2** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M3** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M4** `detected` — exit 2; syntax@41;syntax@41

### ES-T1-C3-E01 — T1-C3 (I1)
- **M1** `silent` — exit 0; zero diagnostics in the model
- **M2** `wrong-target` — exit 0; holds-vacuously: not a satisfy-family item; model standing: holds-vacuously
- **M3** `not detected` — exit 0; holds: object standing: holds
- **M4** `silent` — exit 0; zero diagnostics in the model

### ES-T2-C1-E01 — T2-C1 (S1)
- **M1** `detected` — exit 2; syntax@48;syntax@49;syntax@50;syntax@51
- **M2** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M3** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M4** `detected` — exit 2; syntax@48;syntax@49;syntax@50;syntax@51

### ES-T2-C2-E01 — T2-C2 (S2)
- **M1** `wrong-target` — exit 0; reserved-keyword-name@17
- **M2** `not detected` — exit 0; holds-vacuously: satisfy standing: holds-vacuously
- **M3** `weaker signal` — exit 2; undecided: checked, no verdict
- **M4** `wrong-target` — exit 2; reserved-keyword-name@17

### ES-T3-C1-E01 — T3-C1 (N2)
- **M1** `detected` — exit 2; unresolved@4;unresolved@5;unresolved@9;unresolved@10;unresolved@14;unresolved@15;unresolved@19;unresolved@20;unresolved@32
- **M2** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M3** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M4** `detected` — exit 2; unresolved@4;unresolved@5;unresolved@9;unresolved@10;unresolved@14;unresolved@15;unresolved@19;unresolved@20;unresolved@32

### ES-T3-C2-E01 — T3-C2 (S1)
- **M1** `detected` — exit 2; reserved-keyword-name@23;reserved-keyword-name@24
- **M2** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M3** `not applicable` — exit n/a; no package-level object
- **M4** `detected` — exit 2; reserved-keyword-name@23;reserved-keyword-name@24

### ES-T3-C2-E02 — T3-C2 (N1)
- **M1** `detected` — exit 2; unresolved@44
- **M2** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M3** `not applicable` — exit n/a; no package-level object
- **M4** `detected` — exit 2; unresolved@44

### ES-T4-C1-E01 — T4-C1 (T1)
- **M1** `detected` — exit 2; endpoint-not-a-node@43
- **M2** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M3** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M4** `detected` — exit 2; endpoint-not-a-node@43

### ES-T4-C1-E02 — T4-C1 (R1)
- **M1** `wrong-target` — exit 2; endpoint-not-a-node@43;syntax@44;syntax@44;syntax@44;reserved-keyword-name@49
- **M2** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M3** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M4** `wrong-target` — exit 2; endpoint-not-a-node@43;syntax@44;syntax@44;syntax@44;reserved-keyword-name@49

### ES-T4-C2-E01 — T4-C2 (N1)
- **M1** `detected` — exit 2; unresolved@32
- **M2** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M3** `not applicable` — exit n/a; no package-level object
- **M4** `detected` — exit 2; unresolved@32

### ES-T4-C3-E01 — T4-C3 (R1)
- **M1** `silent` — exit 0; zero diagnostics in the model
- **M2** `wrong-target` — exit 0; holds-vacuously: not a satisfy-family item; model standing: holds-vacuously
- **M3** `not detected` — exit 0; holds: object standing: holds
- **M4** `silent` — exit 0; zero diagnostics in the model

### ES-T5-C2-E01 — T5-C2 (N1)
- **M1** `detected` — exit 2; unresolved@32
- **M2** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M3** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M4** `detected` — exit 2; unresolved@32

### ES-T6-C2-E01 — T6-C2 (N1)
- **M1** `detected` — exit 2; unresolved@40
- **M2** `not applicable` — exit 2; none: model does not analyse cleanly; no verdict can be formed
- **M3** `not applicable` — exit n/a; no package-level object
- **M4** `detected` — exit 2; unresolved@40

### CTRL-T1-C1 — T1-C1 (clean)

### CTRL-T2-C3 — T2-C3 (clean)

### CTRL-T3-C3 — T3-C3 (clean)

### CTRL-T5-C1 — T5-C1 (clean)

### CTRL-T5-C3 — T5-C3 (frozen-clean-only)

### CTRL-T6-C1 — T6-C1 (frozen-clean-only)

### CTRL-T6-C3 — T6-C3 (frozen-clean-only)
