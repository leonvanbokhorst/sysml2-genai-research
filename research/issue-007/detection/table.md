# Detection table — coded errors vs OpenSysML v0.12.1 diagnostics

Primary population: `coding/errors.csv`, frozen **before** this run (14 records). A record counts as **detected** only if the tool emitted at least one diagnostic whose line falls inside the record's `line_range`; a diagnostic elsewhere in the file is not credited to it. Silence neither removes nor reclassifies a coded error.

| Class | Coded errors | Detected | Silent | Recall on this corpus |
|---|---|---|---|---|
| I1 | 1 | 0 | 1 | 0/1 |
| N1 | 5 | 4 | 1 | 4/5 |
| N2 | 1 | 1 | 0 | 1/1 |
| R1 | 2 | 0 | 2 | 0/2 |
| S1 | 3 | 3 | 0 | 3/3 |
| S2 | 1 | 0 | 1 | 0/1 |
| T1 | 1 | 1 | 0 | 1/1 |

| Model | Error | Class | Lines | Detected | Diagnostic |
|---|---|---|---|---|---|
| T1-C1 | T1-C1-E01 | N1 | 64 | no | — |
| T1-C2 | T1-C2-E01 | S1 | 41 | yes | syntax@41;syntax@41 |
| T1-C3 | T1-C3-E01 | I1 | 37-39 | no | — |
| T2-C1 | T2-C1-E01 | S1 | 48-51 | yes | syntax@48;syntax@49;syntax@50;syntax@51 |
| T2-C2 | T2-C2-E01 | S2 | 33 | no | — |
| T3-C1 | T3-C1-E01 | N2 | 4,5,9,10,14,15,19,20,32 | yes | unresolved@4;unresolved@5;unresolved@9;unresolved@10;unresolved@14;unresolved@15;unresolved@19;unresolved@20;unresolved@32 |
| T3-C2 | T3-C2-E01 | S1 | 23,33 | yes | reserved-keyword-name@23 |
| T3-C2 | T3-C2-E02 | N1 | 44 | yes | unresolved@44 |
| T4-C1 | T4-C1-E01 | T1 | 42-44 | yes | endpoint-not-a-node@43;syntax@44;syntax@44;syntax@44 |
| T4-C1 | T4-C1-E02 | R1 | 51 | no | — |
| T4-C2 | T4-C2-E01 | N1 | 32 | yes | unresolved@32 |
| T4-C3 | T4-C3-E01 | R1 | 56 | no | — |
| T5-C2 | T5-C2-E01 | N1 | 32 | yes | unresolved@32 |
| T6-C2 | T6-C2-E01 | N1 | 40 | yes | unresolved@40 |

---

The post-inspection additions were found by inspection **after** the detection run drew attention to them, and each was verified against SysML 2.0 §8.2.2.1.2 (reserved keywords) or the attribute-typing prose (§7.7.1) / `checkAttributeUsageSpecialization` (8.3.7.3). Corrections applied here are listed in `coding/errors-corrections.csv` (Gate-2 response); the frozen population in `coding/errors.csv` is untouched.

| Class | Coded errors | Detected | Silent | Recall on this corpus |
|---|---|---|---|---|
| I1 | 1 | 0 | 1 | 0/1 |
| N1 | 4 | 4 | 0 | 4/4 |
| N2 | 1 | 1 | 0 | 1/1 |
| R1 | 2 | 0 | 2 | 0/2 |
| S1 | 8 | 8 | 0 | 8/8 |
| S2 | 1 | 0 | 1 | 0/1 |
| T1 | 1 | 1 | 0 | 1/1 |
| T2 | 1 | 1 | 0 | 1/1 |

| Model | Error | Class | Lines | Detected | Diagnostic |
|---|---|---|---|---|---|
| T1-C2 | T1-C2-E01 | S1 | 41 | yes | syntax@41;syntax@41 |
| T1-C3 | T1-C3-E01 | I1 | 37-39 | no | — |
| T2-C1 | T2-C1-E01 | S1 | 48-51 | yes | syntax@48;syntax@49;syntax@50;syntax@51 |
| T2-C2 | T2-C2-E01 | S2 | 33 | no | — |
| T2-C2 | T2-C2-P02 | S1 | 17 | yes | reserved-keyword-name@17 |
| T3-C1 | T3-C1-E01 | N2 | 4,5,9,10,14,15,19,20,32 | yes | unresolved@4;unresolved@5;unresolved@9;unresolved@10;unresolved@14;unresolved@15;unresolved@19;unresolved@20;unresolved@32 |
| T3-C2 | T3-C2-E01 | S1 | 23,24,33 | yes | reserved-keyword-name@23;reserved-keyword-name@24 |
| T3-C2 | T3-C2-E02 | N1 | 44 | yes | unresolved@44 |
| T4-C1 | T4-C1-E01 | T1 | 42-43 | yes | endpoint-not-a-node@43 |
| T4-C1 | T4-C1-E02 | R1 | 51 | no | — |
| T4-C1 | T4-C1-P03 | S1 | 44,49 | yes | syntax@44;syntax@44;syntax@44;reserved-keyword-name@49 |
| T4-C2 | T4-C2-E01 | N1 | 32 | yes | unresolved@32 |
| T4-C3 | T4-C3-E01 | R1 | 56 | no | — |
| T5-C2 | T5-C2-E01 | N1 | 32 | yes | unresolved@32 |
| T5-C3 | T5-C3-P02 | T2 | 11 | yes | usage-typing@11 |
| T6-C1 | T6-C1-P01 | S1 | 26 | yes | reserved-keyword-name@26 |
| T6-C2 | T6-C2-E01 | N1 | 40,42 | yes | unresolved@40;unresolved@42;unresolved@42 |
| T6-C2 | T6-C2-P02 | S1 | 22 | yes | reserved-keyword-name@22 |
| T6-C3 | T6-C3-P01 | S1 | 26 | yes | reserved-keyword-name@26 |
