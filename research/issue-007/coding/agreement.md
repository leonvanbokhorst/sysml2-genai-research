# Agreement between coder A and the independent second coder

Double-coded models: **12** of 18 (selection rule in `second-coder/BRIEF.md`).
W1 (wrapper) is excluded from record pairing and reported separately — see the note at the end.

## Headline

| Statistic | Value |
|---|---|
| Model-level agreement: error present / none | **12/12** (100.0%) |
| Record-level class agreement | **11/11** (100.0%) |
| Cohen's κ (class, 11 paired records) | **1.0** (po=1.000, pe=0.306) |
| Krippendorff's α (nominal, class) | **1.0** |
| Layer agreement | 10/11 (90.9%), κ=0.8659 |
| Severity agreement | 10/11 (90.9%), κ=0.7556 |

κ = 1.0 here must not be read as strong evidence of reliability: the corpus is small, the
codebook was built from it, and one class (`S2`) was redefined after coding. The honest
reading is that the codebook is *applicable without drift* by a second reader on this
corpus — not that the taxonomy is right (see report §Limits).

## Model-level calls

| Model | A: any error (n) | B: any error (n) | Agree |
|---|---|---|---|
| T1-C1 | yes (1) | yes (1) | ✓ |
| T1-C2 | yes (1) | yes (1) | ✓ |
| T2-C1 | yes (1) | yes (1) | ✓ |
| T2-C2 | yes (1) | yes (1) | ✓ |
| T3-C2 | yes (2) | yes (2) | ✓ |
| T3-C3 | no (0) | no (0) | ✓ |
| T4-C1 | yes (2) | yes (2) | ✓ |
| T4-C2 | yes (1) | yes (1) | ✓ |
| T5-C1 | no (0) | no (0) | ✓ |
| T5-C2 | yes (1) | yes (1) | ✓ |
| T6-C2 | yes (1) | yes (1) | ✓ |
| T6-C3 | no (0) | no (0) | ✓ |

## Record-level pairing

| Model | # | A class | B class | A layer / B layer | A sev / B sev | Agree |
|---|---|---|---|---|---|---|
| T1-C1 | 1 | N1 | N1 | name resolution / name resolution | blocking / blocking | ✓ |
| T1-C2 | 1 | S1 | S1 | syntax/parse / syntax/parse | blocking / blocking | ✓ |
| T2-C1 | 1 | S1 | S1 | syntax/parse / syntax/parse | blocking / blocking | ✓ |
| T2-C2 | 1 | S2 | S2 | constraint/OCL / syntax/parse | minor / blocking | ✓ |
| T3-C2 | 1 | S1 | S1 | syntax/parse / syntax/parse | blocking / blocking | ✓ |
| T3-C2 | 2 | N1 | N1 | name resolution / name resolution | blocking / blocking | ✓ |
| T4-C1 | 1 | T1 | T1 | type/typing / type/typing | major / major | ✓ |
| T4-C1 | 2 | R1 | R1 | structural/architectural / structural/architectural | major / major | ✓ |
| T4-C2 | 1 | N1 | N1 | name resolution / name resolution | blocking / blocking | ✓ |
| T5-C2 | 1 | N1 | N1 | name resolution / name resolution | blocking / blocking | ✓ |
| T6-C2 | 1 | N1 | N1 | name resolution / name resolution | blocking / blocking | ✓ |

## Disagreements and conventions

- **T2-C2 #1** — class A=S2 / B=S2; layer A=constraint/OCL / B=syntax/parse; severity A=minor / B=blocking. A: `satisfy lowerBeforeArrival;` | B: `satisfy lowerBeforeArrival;`. Explanation: the second coder used the v1.0 codebook copy, in which S2 was still a syntax defect; coder A's S2 record was relabelled to the constraint layer after retrieving the normative BNF (codebook §9). The class id agrees; the layer and severity follow the codebook version each coder was given.

### W1 convention (not a disagreement about the models)

- Coder A codes W1 only for **raw artefacts** and counts it over the 18 raw outputs: **18/18 are markdown and fail as-is**, with 4 also carrying preamble prose.
- Coder B coded W1 for **12/12** models — including bare fences — and excluded W1 from its `n_errors`, exactly as the codebook instructs. This is a **recording-scope difference, not a disagreement** (corrected 2026-11-13T15:16Z, A-17): both coders treat a bare fence as W1; they differ only in whether the W1 row is kept in the per-model list or counted only over raw artefacts. The modelling labels are identical.
- The codebook should still say explicitly whether a bare fence is a wrapper defect for a raw-text consumer; it currently leaves the reading implicit.

---

**Interpretation corrections (Gate-2 response):** `agreement-addendum.md` — the
statistics above are unchanged, but κ = 1.0 is **not** reliability evidence: the
coder-facing codebook contained 8 of the 11 paired excerpts verbatim and the mechanism
of the other 3. Read the addendum before quoting any figure here.

