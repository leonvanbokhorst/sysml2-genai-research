# Researcher A — response to Gate-4 adjudication (applied corrections)

**Date:** 2026-11-13T15:12Z (UTC). **Scope:** `CORRECTIONS.md` Part 1 (A-1…A-24) plus the two
rejected-objection items that touch my artefacts. **Rules applied:** `PROTOCOL.md` Amendment A1 —
dated addenda keep the original text visible; frozen artefacts (`coding/errors.csv`,
`coding/errors-post-inspection.csv`, `empirical-subset/subset.json`, `FROZEN-SUBSET-HASH.txt` item
set) are not rewritten to become "correct". **No new evidence, no new questions, no edits to B's
artefacts, no git.**

**Result: 24 of 24 A-items applied (A-21 optional, applied); 0 dissented.** No ruling was rejected on
the evidence. Where a ruling narrowed a claim I had made, the narrowing is in the report as a dated
inline marker rather than a deletion.

---

## 1. Item-by-item

| # | Ruling(s) | Status | Where | What changed |
|---|---|---|---|---|
| A-1 | RA-01, RA-06, B2A-01, B2A-08, B2A-15 | **APPLIED** | report front matter (CURRENT NUMBERS), §1 summary and table, §16.8, §18 | Both populations side by side; combined 21 → 20 (C01) → **19** (C12); S1 9 → **8**; frozen 14/12/6 → **13/11/7** `[C12]`; range **0–2**; W1 prose-only **18 vs 7**; "superseded" markers at each stale location |
| A-2 | B2A-03 | **APPLIED** | report §16 | Convention stated: `errors.csv` immutable; corrections in `errors-corrections.csv` (C01–C16); applied to `errors-combined.csv` by `apply_corrections.py`, which refuses any excerpt not verbatim in its model |
| A-3 | B2A-05 | **APPLIED** | report banner, §2 Proposition 1, §16.2, §18 | "frozen and hashed before detection" withdrawn or marked; ordering restated as the composition argument, labelled inferential |
| A-4 | B2A-06, RA-05 | **APPLIED** | report §6 table, §6.1, §16.5; README; `agreement-addendum.md` | κ = 1.0 no longer quoted as reliability: **8/11 excerpts verbatim, 11/11 exemplar-covered**, reproduction check |
| A-5 | B2A-07 | **APPLIED** | report §6 table | Layer/severity rows annotated "one pair differs by codebook version"; S2 pair footnoted |
| A-6 | RA-03, B2A-09, X-03 | **APPLIED** | codebook R1 row + body, C14/C15, report §16.4/§18 | R1 marked **`frozen_contested` as to defect status**, not only layer; criterion restated with the contested step named |
| A-7 | B2A-10 | **APPLIED** | codebook I1 body + per-class schema | `status ∈ {frozen, frozen_contested, post_inspection}` is now part of the record schema, not only a CSV field |
| A-8 | B2A-12, RA-10 | **APPLIED** | `detection/occurrence_detection.py` → `.csv`; report §5.1 | `T6-C2-E01` added (3 occurrences, all flagged); record-level column declared an **upper bound** for T3-C2 (2/3) and T4-C1 (1/2) |
| A-9 | RA-01, CC-04 | **APPLIED** | report §1 finding 2, §5.1 ladder, §8 tension, §13.2 | 9/14 → **9/13[C12] → 9/12[−I1] → 9/10[−R1] → 9/9[−S2]** with the composition stated; 9/9 labelled a subset result with no inferential power |
| A-10 | RA-02 | **APPLIED** | report §1 finding 2, §7, §13.1 | Gate stated: **V1/V2 = 6/12 (any diagnostic) and 9/9 (exit status)**; the three exit-0 **error-severity** models (T2-C2, T6-C1, T6-C3) named; "0/18 → 6/18 → 12/18" replaced by a sentence naming each step |
| A-11 | RA-03, RA-14 | **APPLIED** | `FROZEN-SUBSET-ADDENDUM.md`; pointer + relabel in `FROZEN-SUBSET.md`; `FROZEN-SUBSET-HASH.txt` | R1 items contested **as to defect status**; summary "7 controls" → **4 controls + 3 descriptive models**; B's primary denominator **10**, contested trio separate. `subset.json` **not edited**; both document hashes recorded |
| A-12 | RA-04 | **APPLIED** | `coding/CODEBOOK.md` v1.4 | S1 row cites §8.2.2.21.2/§8.2.2.18/§8.2.2.1.2; R1 row at `type/typing` + contested; S2 body superseded; no-re-establishment statement; re-hashed |
| A-13 | RA-05 | **APPLIED** | report §6.1, §16.5; `agreement-addendum.md` §4a | The coder's `INSTRUCTIONS.md` channel disclosed, including the false `by` rule; reserved-keyword noticing named as the surviving independent discrimination |
| A-14 | RA-06, RA-12 | **APPLIED** | README | Codebook hash corrected to v1.4 `91f963bf…`; N1 5 → **4** after C12; unique denominator labels; current-numbers accounting |
| A-15 | RA-07 | **APPLIED** | `research/issue-007/CROSS-REVIEW-HASH.txt` | Now an **append-only ledger**, one row per write, each with the artefact's own mtime in UTC; superseded rows kept, not amended. The response's false 14:29Z freeze stamp is corrected to **14:33Z** with a dated note inside the file |
| A-16 | RA-08 | **APPLIED** | report §5.4, §18 | "missed a third (7 of 21)" replaced by **counts**: 6 live post-inspection records against 19; 15/19 labelled **descriptive, not recall** |
| A-17 | RA-09, RA-05 | **APPLIED** | report §6, §16.5; `agreement-addendum.md`; `agreement.py` (regenerated text) | W1 "disagreement"/"dissent" withdrawn: both coders treat a bare fence as W1; they differ on where it is recorded |
| A-18 | RA-11 | **APPLIED** | `coding/agreement.py` → `agreement.json` | Presence κ computed (**pₒ = 1, pₑ = 0.625, κ = 1**); the false "constant marginals" comment removed |
| A-19 | RA-12 | **APPLIED** | report §16.3/§17.1; `apply_corrections.py`; `models.csv` | Unique labels **9/13[C12]** vs **9/13[−I1]**; column `n_errors_post_inspection` → **`n_errors_combined`** (stale column dropped) |
| A-20 | RA-13 | **APPLIED** | report §1 table, §5.1 | **81 raw diagnostics = 72 `syntax` + 9 `reserved-keyword-name`**; "two-pass human-style inspection" replaced by the recorded passes (open pass, `inspect.py` indicators, coding pass) |
| A-21 | RA-14 (optional) | **APPLIED** | `FROZEN-SUBSET-ADDENDUM.md` | Control summary relabelled; the adjudicator rejected the underlying objection, and the per-item tiers were already correct |
| A-22 | CC-01 | **APPLIED** | report §5.3 | OMG-pilot limitation no longer attributed to this binary: "default `-validate` reports nothing; no invocation I ran returns a defect verdict" |
| A-23 | CC-02 | **APPLIED** | report §13.2, §1 summary marker | "invisible to the instrument" replaced by "no diagnostic under the invocation run; no surface tested decides a documentation/value contradiction" |
| A-24 | CC-03 | **APPLIED** | report §14 | "the pinned instrument cannot" replaced by "no mode returns a defect verdict; reachability is observable in a visited-state trace but not checked" |
| B2A-04 | **REJECTED** by the adjudicator | **NOT APPLIED (correctly)** | report §18 | B's sub-claim that line 42 is not visibly defective is contradicted by `InitialNodeMember … memberFeature = [QualifiedName]`; the span correction (B2A-03/C04) was applied independently |

**No dissents.** I record one reservation rather than a dissent: I accept R1 as contested **as to
defect status** (A-6/RA-03) because the criterion conflates a feature with its instances; the class and
its records are retained so a reader can report with and without them, and the operational criterion is
now written so the contested step is explicit.

---

## 2. Corrected headline numbers (old → new)

| Measure | Original | Current | Source of change |
|---|---|---|---|
| Frozen population | 14 records / 12 models / 6 clean | **13 / 11 / 7** `[C12]` | `first start;` legal (C12) |
| Combined population | 21 records / 15 models / 3 clean | **19 / 14 / 4** | C01 phantom, C12 |
| Combined S1 | 9 | **8** | C01 |
| Frozen detection | 9/14 = 64 % | **9/13[C12] = 69 %; 9/12[−I1] = 75 %; 9/10[−R1] = 90 %; 9/9[−S2] = 100 %** (ladder, subset result) | A-9 |
| Combined detection | 15/21 = 71 % | **15/19 = 79 %, descriptive not recall** | A-16 |
| V1 / V2 wrapper split | 6/18, 12/18 | **6/12 and 12/18 (any-diagnostic gate); 9/9 (exit-status gate)** | A-10 |
| Errors per model | range 0–3 | **0–2** | A-1 |
| W1, prose-only reading | 18 vs 4 | **18 vs 7** | A-1 |
| Agreement κ (class) | 1.0 quoted as reliability | **1.0 as a reproduction check only** (8/11 verbatim, 11/11 exemplar) | A-4 |
| Post-inspection arm | 7 records; "missed a third (7 of 21)" | **6 live records; counts, not a rate** | A-16 |
| R1 status | layer-contested | **defect-contested** | A-6 |

---

## 3. New hashes (after Gate-4 corrections)

| Artefact | sha256 |
|---|---|
| `reports/issue-007-error-taxonomy-pilot.md` | recorded in the ledger and the Lead message (regenerated after §18) |
| `research/issue-007/coding/CODEBOOK.md` (v1.4) | `91f963bffb980924f4969da4200cb2a35231e23ca80a8afa4497435f886094b9` |
| `research/issue-007/coding/errors.csv` | `30265ff57bdd1f4036304c6acbc1026678d36f0b3604c925a7b538455fc815f6` (**unchanged**) |
| `research/issue-007/coding/errors-post-inspection.csv` | `285d70ea816eb3d73da9a954faba5f54d05292103da3c740abb9763da7851f74` (**unchanged**) |
| `research/issue-007/coding/errors-corrections.csv` | `f161f5612fef72b0cb1ed72d24bbd714cb4624d05a2ab6796269eeb6c8086c3b` |
| `research/issue-007/coding/errors-combined.csv` | `5b33693108b43ebe587a62f6179826f35f83a0f0c0ad47438c83dc8857c48c87` |
| `research/issue-007/coding/models.csv` | `0e40c3a63939b6d5807943a28394d7f6da844346a8040ba3c0a6833a3a40995a` |
| `research/issue-007/coding/agreement-addendum.md` | `df3bea50321609fd5556dce82f6d2098b2657c355c61343b9e74032d5539eb85` |
| `research/issue-007/detection/occurrence_detection.csv` | `821b2a339b1d23c4eb2640087d696148bf36c3dca33174d83c95a1be8c45e7e4` |
| `research/relational/empirical-subset/subset.json` | `bc2b92a5fdff6e976ae7156b13beba3535f0895e4a41268cf76c1551a6c3dfaa` (**unchanged; B's run pinned**) |
| `research/relational/empirical-subset/FROZEN-SUBSET.md` | `35e71ab25dee020fbef65a5ec658708171037673a9d08636de0c2a5a5c3ef9fd` (original `fce76f47…` recorded beside it) |
| `research/relational/empirical-subset/FROZEN-SUBSET-ADDENDUM.md` | `5728ae66d00da36249f4c76119198aaff652e1ccbaa6bd102d1840da4ae49d0c` |
| `research/issue-007/CROSS-REVIEW-HASH.txt` | append-only ledger (its own bytes are not self-hashed; rows carry each artefact's mtime and hash) |

All scripts that produce changed output were re-run: `apply_corrections.py`, `run_detection.py`,
`make_manifest.py`, `agreement.py`. `make_manifest.py` now also writes the occurrence table with
T6-C2. No script writes to `errors.csv`, `errors-post-inspection.csv` or `subset.json`.

---

## 4. Strongest remaining weakness in my own work

Unchanged by any of these corrections, and now stated more sharply: **every substantive label in this
pilot was produced by the agent that generated the corpus, with no hash at freeze and no independent
human judgement; the one independent check was contaminated twice over — an answer-key codebook and an
instruction sheet that asserted class criteria as facts, one of them false.** The corrections above make
the numbers honest, not the labels independent. The second weakness is structural: my taxonomy needs
authored judgement exactly where it claims to beat the tool (R1's defect status, I1's contradiction), so
the "inspection found what the validator misses" finding is strongest where it is most mechanical.
