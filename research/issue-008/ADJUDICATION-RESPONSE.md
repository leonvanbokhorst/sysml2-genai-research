# Researcher B — response to the Gate-4 adjudication (execution record)

**Task:** apply the adjudicated corrections to my own artefacts. **Not** a new investigation: no new
evidence, no new research question, no git, no edit to Researcher A's artefacts, none to raw validator
output, none to any frozen artefact.
**Date:** 2026-11-13. **Source:** `research/relational/adjudication/ADJUDICATION.md`,
`rulings.json`, `CORRECTIONS.md` Part 2 (B-1…B-35).
**Form applied:** PROTOCOL.md Amendment A1 — prose corrections are **dated addenda that keep the
original text visible**, on whose ruling and why; **front-matter pointers** are the remedy for stale
headline pages. Frozen artefacts stay byte-identical; derived scoring goes to new dated files.

**Result: 35 items — 34 APPLIED, 1 APPLIED-PARTLY, 0 DISSENTED.** No item was left unapplied and no
ruling is contested on the evidence.

---

## 1. Where each item went

| # | Ruling | Status | Artefact and what was done |
|---|---|---|---|
| **B-1** | CC-05, A2B-01 | **APPLIED** | Report **front matter** added (§ "ADJUDICATED CORRECTIONS"), naming the four superseded headline sentences; **inline pointer immediately after** the §1 "no evidence at all" sentence; full restatement in **A11.1**. |
| **B-2** | A2B-02 | **APPLIED** | **A11.4** adds the two output surfaces (`diagnostics[]` vs `checks[]`) and the five standings to the measurement definitions; pointer added to the §3.1 measures row. |
| **B-3** | A2B-03 | **APPLIED** | **A11.5**; F1 labelled "authored family" in §3.2 pointer and §1 pointer block; exit-0 reserved-keyword sub-class stated with probe P1. |
| **B-4** | A2B-04 | **APPLIED** | **A11.6**: both rates (3/4 authored, 3/5 cross-corpus), the `check…` **MAY** obligation, and the vacuously-holding report. |
| **B-5** | A2B-05, A2B-06 | **APPLIED** | **A11.7**: three-way resolution statement; prelude confound recorded as **measured**, with the message that distinguishes it. |
| **B-6** | A2B-07, A2B-09 | **APPLIED** | **A11.8**: per-mutant construct-frequency assumption + the census (constraints 0/18, unit literals 0/18, metadata 0/18, `connection def` 0/18, explicit `end` 0/18, short names 0/18, `satisfy` 18/18). |
| **B-7** | RB-03, A2B-08 | **APPLIED** | **A11.14**: the pre-freeze **calibration probes** named as expectation knowledge (`q1`→F6, `m1`→F8-01, `m2`→F8-02, `t1`→F6 severity); audit relabelled "informed, not blind, weak by construction". |
| **B-8** | A2B-09 | **APPLIED** | **A11.9**: F4 = **declared multiplicity**; R1 (chain through a multi-valued usage) never sampled. |
| **B-9** | A2B-10 | **APPLIED** | **A11.10**: A9's disclosure extended to the **32 mutant files** (same mtime; `mutants.sha256` verifies). |
| **B-10** | A2B-11, RB-08 | **APPLIED** | **A11.11**: corrected to **23 of 28** (any severity) and **20 of 23** (error-bearing); claim restated as relevance, not precision. `analysis.json` now carries the distribution. |
| **B-11** | B2A-16 | **APPLIED** | **A11.12**: **3/18 import SI, 0/18 import ISQ, 0/18 write a unit literal**. |
| **B-12** | RB-01 | **APPLIED** | `empirical/REPORT.md` **§14.1**; `empirical/run-log.md` **§2 corrected in place with the old sentence quoted** and **§7** added. States that `9458406e` is **post-AM1 (14:36:04Z, after run1)**, that the pre-run value was overwritten, and that pre-registration rests on **content + AM1's disclosure + run1/run2 identity of the detected set**. |
| **B-13** | RB-02 | **APPLIED** | **A11.13**: `[4..2]` is an **empty, unsatisfiable range**, so the detection is true; *"an empty range is not obviously ill-formed"* deleted; **22/32** given as the named-constraint-only alternative; "no spurious error" qualified. Inline pointer at §3.5. |
| **B-14** | RB-03 | **APPLIED** | **`research/issue-008/METHODOLOGY-ADDENDUM-1.md`** written and referenced from A11.14. `METHODOLOGY-FROZEN.md` **unchanged** (hash still `2c80d63e…`). |
| **B-15** | RB-04 | **APPLIED** | **A11.15** + `results/known-good-triage.md` dated correction: KG-04 reclassified **(iv) unresolved / specification-ambiguous**; pointers corrected to **§7.6.3 / §7.6.5** (not §7.6.1) and **KerML §8.3.2.4.5**; the identified reason stated. |
| **B-16** | RB-05 | **APPLIED** | **`empirical/SCORING-ADDENDUM.md` §2** and `empirical/REPORT.md` **§14.2**: **M3 = 3 applicable / 10 n/a**, with the per-item breakdown (2 not detected, 1 weaker signal). |
| **B-17** | RB-06 | **APPLIED** | Registered rule implemented in **`empirical/results-addendum.csv`** via `empirical/rescore_addendum.py`: non-satisfy M2 items → **`not applicable`**, so **M2 applicable = 1** (S2 only); controls use **model-level** vocabulary. No detection count changes. |
| **B-18** | RB-07 | **APPLIED** | `empirical/run_external.py` now uses **exclusive creation** (`open(..., "x")`) for raw output; the docstring claim is now implemented; change logged in `empirical/run-log.md`. |
| **B-19** | RB-08 | **APPLIED** | **A11.16**; `analysis.py` re-run: F5-01 moved from `silent` to **`incidental` (warning-only)**. New split **23 detected / 2 wrong-severity / 1 misleading / 2 incidental / 4 silent**. One exclusion order fixed in `SCORING-ADDENDUM.md` §4. |
| **B-20** | RB-09 | **APPLIED** | **A11.17**: self-reported UTC clocks are no longer used as ordering evidence; filesystem order stated (methodology 14:06:07Z → mutants 14:13:00Z → run1 14:13:03Z). |
| **B-21** | RB-10 | **APPLIED** | **A11.18** + code comment in `harness/analysis.py`: `spec_status` is **post-hoc, single-coder, mechanical**. |
| **B-22** | RB-11 | **APPLIED** | **A11.19**: base concentration (**9 of 32 mutants edit `KG-01`**; top three carry **19 of 32**), the known-good corpus is their parent, and it was **iterated to tool-silence before the freeze**. |
| **B-23** | RB-12 | **APPLIED** | `research/issue-008/README.md`: the false "No empirical challenge set … nothing here was informed by A" section replaced with the actual state and the addenda that record A's influence. |
| **B-24** | CC-06 | **APPLIED** | **A11.20** (and §A11.1): "and nothing more" replaced; execution failures and property checks named. |
| **B-25** | CC-07 | **APPLIED** | **A11.21**: P4 restated as **site-dependent enforcement**, with the live rival reading that F5-01 may not instantiate the constraint (X-01). |
| **B-26** | CC-08 | **APPLIED** | **A11.22**: ceiling scoped to the **default `-validate` path**, with the engine-strength vocabulary. |
| **B-27** | CC-09 | **APPLIED** | **A11.23**: §11.5 rewritten — **two** of the four decided by no mode tested, one by `-satisfy`, one undecided; the oracle conclusion kept. |
| **B-28** | CC-10 | **APPLIED** | **A11.24** + inline pointer at §8.1: the third separator — **invocation, encoding, engine**. |
| **B-29** | CC-11 | **APPLIED** | §11.1: inline correction inserted, original visible; **A11.2**. |
| **B-30** | CC-12, A2B-01 | **APPLIED** | §2 P3 cell: "**corrected by A2, and further corrected by A11.1**" added beside the original verdict. |
| **B-31** | CC-13 (REJECTED) | **APPLIED-PARTLY** | Optional editorial only; the adjudicator **rejected** the underlying criticisms. Recorded in **A11.25** that the encoding-dependence observation *strengthens* A11.1/A10.5 rather than correcting them. No example text added to §A2, because the ruling says none is required. |
| **B-32** | X-01 | **APPLIED** | **`empirical/SCORING-ADDENDUM.md` §3**, `empirical/REPORT.md` **§14.3**, A11.26: **9/9 established+mandatory + 0/4 discretionary/unnormative/contested**; the aggregate is **not** a detection-gap measure. |
| **B-33** | X-02 (UNRESOLVED) | **APPLIED** | **`empirical/REPORT.md` §14.4** and report front matter: both readings reported; **the layer boundary is no longer stated as a property of the instrument**. |
| **B-34** | X-03 (UNRESOLVED) | **APPLIED** | **`empirical/SCORING-ADDENDUM.md` §4**, `empirical/REPORT.md` §14.5: ladder **L1 9/13 · L2 9/12 · L3 9/11[C] · L4 9/11[R1] · L5 9/9**, uniquely suffixed, one exclusion order. |
| **B-35** | X-04 (UNRESOLVED) | **APPLIED** | **A11.20**, `empirical/REPORT.md` §14.6: every verdict quoted with **invocation + engine + standing**; verdicts declared **not self-certifying**. |

**APPLIED 34 · APPLIED-PARTLY 1 (B-31, optional and on a rejected criticism) · DISSENTED 0.**

---

## 2. Corrected headline numbers, old → new

No numerator moved. What moved is what each number is allowed to say, and one denominator's reading.

| measure | as published | after adjudication | why |
|---|---|---|---|
| synthetic, default `-validate` | **23/32 = 0.72 [0.55, 0.84]** | **unchanged** | B-13 confirms F4-01 is a true detection |
| synthetic, "named-constraint-only" criterion | not stated | **22/32 = 0.69** | B-13: the alternative criterion neither pilot uses, now stated |
| outcome split | 23 / 2 / 1 / 1 / **5 silent** | **23 / 2 / 1 / 2 / 4 silent** | B-19: F5-01 is warning-only, not silent |
| diagnostics per defect | "24 of 28 produce exactly one" | **23 of 28 (any severity); 20 of 23 (error-bearing)** | B-10 |
| F5 | 3/4 (+3/5 in an addendum) | **3/4 authored and 3/5 cross-corpus, both printed**, with the MAY obligation | B-4 |
| F1 / F2 / F4 / F8 | class-level rates | **authored-family / four-sites / declared-multiplicity / metadata**, each with its scope | B-3, B-5, B-8 |
| external, default path | **9/13 = 0.69** | **9/13 retained**, but read as **9/9 established+mandatory + 0/4 discretionary/contested** | B-32 / X-01 |
| external ladder | 9/13 → 9/12 → 9/11 | **9/13 · 9/12[−I1] · 9/11[C] · 9/11[R1] · 9/9 + 0/4** | B-34 / X-03 |
| external M2 | "0 detected, 1 evaluated, 10 n/a" | **0 detected, applicable = 1** (S2, `holds-vacuously`) | B-17 |
| external M3 | "0 detected, 1 undecided, 10 n/a" | **0 detected, applicable = 3** (1 weaker signal) | B-16 |
| known-good arm | 0/10 errors, 1/10 warnings as "over-reach" | **0/10 unchanged**; the warning reclassified **unresolved / spec-ambiguous** | B-15 |
| pre-registration | "hash-proven before the first run" | **content-evidenced, not hash-proven** | B-12 |
| P3 / §1 / §11.1 / §11.5 / §4.2 | as written | addendum-corrected, originals visible, pointers in place | B-1, B-27, B-29, B-30, B-26, B-33 |

**The one sentence a reader should carry away, corrected:** *under the default `-validate` invocation
of this one binary, 23/32 of my authored mutants produced a relevant error; of the observed items in
the external set, the tool detected all 9 whose defect status is established and whose reporting is
mandatory, and none of the 4 that are discretionary, normatively unfounded or contested. The four F7
misses are conditions no catalogue constraint names, and across all modes tested one of them is
detected, one checked and left undecided, and two decided by no mode at all.*

---

## 3. New and changed hashes

| artefact | sha256 | note |
|---|---|---|
| `reports/issue-008-validator-reliability-pilot.md` | `06dd07f403383354832b730e16fda59e35e059d80032dfba9283c5aab0104302` | front matter + A11 + 8 inline pointers |
| `research/issue-008/README.md` | `edad37e9005d617aa2b6607fe0be692d45bbe5f7a20e1c1f17debbedbdab16ae` | B-23 |
| `research/issue-008/METHODOLOGY-ADDENDUM-1.md` | `c58c2bab9c1ca90fa5636eae58c6baef7a73dc560539aab2b644ff668afbdcb2` | new (B-14) |
| `research/issue-008/METHODOLOGY-FROZEN.md` | `2c80d63e8800be9ca67a051aaffdbc4b6c56c1b576002fc4446fe82862e6f00b` | **unchanged, byte-identical** |
| `research/issue-008/mutants/MANIFEST.csv` | `a9f479748aea10c76460421031a384ddda779d4c78ea1cb6a5fe2f208f157be7` | **unchanged**; 32 mutant hashes verify OK |
| `research/issue-008/results/analysis.md` | `c7609e700d9355dc2d48efaaf7982a303baea86b1a2e2f319aca736f3a81ad4b` | regenerated (B-19, B-10) |
| `research/issue-008/results/analysis.json` | `8be300161d25cc70f982d48b85b825e7e726b8056e867d6619550ca64893cedf` | regenerated; now carries `diagnostics_per_defect` |
| `research/issue-008/results/triage.csv` | `ce17ef6f509bafeb2eb02baad6d4fb263b41c1fa16b5206f3356a2a9d5b26b0a` | regenerated (F5-01 → incidental) |
| `research/issue-008/results/known-good-triage.md` | `9c4bf7596012a0d30eb095a913cdd3d270eabfce807d3e12b1dc491eb0a9122d` | B-15 |
| `research/issue-008/empirical/REPORT.md` | `296f1826199df659a1710618b42a43a76868c8e9ddabc80cb6289c3958f51341` | front matter + §14 |
| `research/issue-008/empirical/SCORING-ADDENDUM.md` | `0b626318d1f12e7295d0e0f50a030adec46afa757b734e4f042cd1731f4f3c0d` | new (B-16/17/32/34) |
| `research/issue-008/empirical/results-addendum.csv` | `b30ae1cea59de8e1af01aac2b0526df8d46b3eb8b1a8a1e361cc4dec1df29d15` | new derived file |
| `research/issue-008/empirical/rescore_addendum.py` | *(regenerates the two rows above)* | new |
| `research/issue-008/empirical/run-log.md` | `2ea17a35b66d487fcfb23c9e145c945c8031220555103d1aa497f8bba73cf533` | §2 corrected, §7 added (B-12), B-18 logged |
| `research/issue-008/empirical/run_external.py` | `8e3c1499e60f0839cddcef612bd67fb805a9c2726d8b64c058a1e92e1526f1f3` | refuse-if-exists implemented (B-18) |
| `research/issue-008/empirical/PRE-REGISTRATION.md` | `9458406e7db665ac42f5a3a896a7dc05b094b0fb6e8ef3a4ab9ed9db7e6acfbc` | **not edited** — its provenance is now corrected in the *reporting* files, not by rewriting the artefact |

**Not touched, verified after the edits:** `raw/run1/**`, `raw/run2/**`, `results/results.csv`,
`results/diagnostics.csv`, all 32 mutant files, `MANIFEST.csv`, `METHODOLOGY-FROZEN.md`,
`empirical/PRE-REGISTRATION.md`, A's frozen subset, A's artefacts, and every file under
`research/relational/adjudication/` and `cross-reviews/`.

---

## 4. What I think is the strongest remaining weakness

After the corrections, the weakest part of my own work is no longer a claim — it is the **design's
power to support any claim about validators in general**, and three of the corrections converge on it:

1. **The per-class picture is confounded with obligation and I cannot separate them** (B-33 / X-02,
   unresolved). Every miss in both corpora is simultaneously a semantic-layer condition and one that
   is discretionary, unnamed or contested. The unconfounded residue is thin — "within what the
   specification establishes and mandates, this tool detected 9/9 and 9/9" — and it is a statement
   about *reporting obligations being met*, which is a much smaller claim than "validators cannot see
   semantics".
2. **My fault model lives on a construct surface my own external corpus does not occupy** (B-6/B-22).
   Four of eight classes are untestable against observation; 9 of 32 mutants edit one 23-line model;
   the known-good corpus was iterated to tool-silence before the freeze, so it is not independent of
   the mutant arm and its 0/10 cannot estimate a false-positive rate.
3. **The pre-registration is content-evidenced, not hash-proven** (B-12), and the audit behind the
   expectations is **informed by the same probes** that later "confirmed" it (B-7/B-14). The numbers
   are insulated from that; the *interpretation* of the numbers is not.

Put in one sentence: **the pilot can say what one binary does on two small corpora it helped make,
and cannot yet say what a validator is.** The missing instrument is not a second validator — it is a
construct-frequency census over ≥200 independently generated models, plus a held-out coder.
