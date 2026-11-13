# Adjudication — every challenge to the #7 and #8 pilots, ruled on the evidence

**Role:** independent adjudicator (did not produce any artefact under challenge).
**Scope:** the challenges filed in `research/relational/cross-reviews/**`, `reviews/**` and
`critique/**` against the two pilots; nothing outside those pilots is adjudicated, and no new
research question is opened.
**Pinned at:** 2026-11-13T14:51:34Z. Re-verified unchanged at 2026-11-13T15:03:54Z (§2.3).
**Write scope:** `research/relational/adjudication/**` only. No researcher artefact was edited, no
git command was run, no subagent was spawned.
**Validator used:** `.tools/sysml`, OpenSysML v0.12.1, binary sha256
`ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0` — to reproduce observations,
never as ground truth. Every run I made is listed in §2.4.

---

## 1. Summary

### 1.1 What was adjudicated

| Source family | Challenges in | Consolidated rulings |
|---|---:|---:|
| Researcher A → B (`A-reviews-B.md`, O1–O13) + B's responses | 13 | **12** (one merged pair, one carried to UNRESOLVED) |
| Researcher B → A (`B-reviews-A.md`, O1–O13) + A's responses, plus B's two post-closure notes | 15 | **16** (one objection split, because its two halves get opposite rulings) |
| Reviewer A (`reviewer-a-issue-007.md`, M-1…M-6, P-1, m-1…m-6, Adj-1) | 14 | **14** |
| Reviewer B (`reviewer-b-issue-008.md`, RB-01…RB-12) | 12 | **12** |
| Semantic-ceiling critic (`CLAIMS.csv` C01–C20) | 20 | **13** (eight "no overstatement" verdicts consolidated into one) |
| Critic status propositions S1–S10 | 10 | **10** |
| Cross-cutting findings raised by this task ("neither pilot noticed") | — | **4** |
| **Total** | **~84** | **81** |

**Outcome:** **64 challenges ACCEPTED, 3 REJECTED, 4 UNRESOLVED** (the four unresolved are the
`name-conflict` / implicit-redefinition question raised by A's O13 and B's O13, and three
cross-cutting findings of my own); **10 status propositions UPHELD**. Rulings and corrections are one machine record each in
[`rulings.json`](rulings.json); the edit list for the Lead is [`CORRECTIONS.md`](CORRECTIONS.md).

Rejection is rare here, and that is not deference: every cross-review objection that turns on the
instrument was re-derived by running the pinned binary myself on the cited model or an equivalent
probe (§2.4 runs 1–11), and every arithmetic objection was recomputed from the raw CSV — not
accepted on the reviewer's word. Two of the three rejections are cases where the challenger's own
artefact or the specification text disproves their sub-claim, and one is a hypothetical harm that
did not occur. Acceptance is also not a compliment: several accepted rulings correct the *researcher
who was challenged* in a direction that helps the challenger, and two correct the *challenger* (the
9/9 subset is a post-hoc subset with no inferential power, and Reviewer A's "warning-only"
description of three models is factually wrong).

### 1.2 The three most consequential rulings

1. **RA-01 (M-1) — the 9/14 "validator blind spot" is composed entirely of one withdrawn, one
   discretionary and two contested records; the instrument detects 9/9 of the records whose defect
   status is established and whose reporting obligation is mandatory.** Arithmetic shown in §3.1
   and §7.1. **Headline effect: A's central critical claim does not survive as a blind-spot
   measure; the numerator stays 9 and the honest denominator becomes a ladder ending at 9/9.**
2. **RA-02 (M-2) — the V1/V2 wrapper split (6/12) is gate-dependent: under an exit-status gate it
   is 9/9, and the report never states the gate.** **Headline effect: A's second headline number
   acquires two readings (6/12 any-diagnostic; 9/9 exit-status), and neither is "the" answer
   without the gate.** (I correct Reviewer A's own description of the three models in the process —
   they are exit-0 *error*-severity, not warning-only.)
3. **RB-02 — F4-01 (`[4..2]`) is counted as a detection while the same error is cited as the
   instrument being stricter than the specification; both cannot be right.** **Headline effect:
   none to 23/32 — I rule the model text is defective (the spec's own definition of a range makes
   `[4..2]` empty), so the count stands and P5's wording must change; the alternative reading
   (22/32) is stated because the only way to reach it is to adopt a defect criterion the pilots do
   not use.**

Two further rulings the Lead should treat as headline-adjacent: **X-01** (B's external arm has the
same composition problem as A's, unremarked by anyone: its four misses are all discretionary or
contested, so 9/13 is really 9/9 established plus 0/4 discretionary) and **RA-03 / X-03** (R1's
defect status, not merely its layer, is contested — Reviewer A's finding goes beyond what A
conceded).

### 1.3 The two headlines, adjudicated

| Claim as filed | Adjudication | Most defensible form |
|---|---|---|
| A: "the validator detects 9/14 (64%) — silent on 5 of 14 — neither method is an oracle" | **Partly supportable.** The count reproduces exactly; the *reading* does not. After A's own C12 it is 9/13; the four remaining misses are S2 (a `check` constraint with a MAY obligation: "MAY report, satisfy by implied relationships, or ignore"), R1 ×2 (no normative basis found; and the criterion as worded conflates a feature with its instances), I1 (contested). | *"At the default `-validate` invocation the tool reported nothing on 4 of the 13 frozen records — all four with discretionary, normatively unfounded or contested status — and reported 9/9 of the 9 records whose defect status is established and whose reporting is mandatory. On one of the four it positively reports the requirement as holding, vacuously."* |
| B: "23/32 = 0.72 [0.55, 0.84] relevant error-severity detection; detection stops at the constraint/semantic layer" | **Supportable only with three labels attached.** The count reproduces (I re-derived it from `diagnostics.csv`: 23 mutants with ≥1 error, F4-01 among them). But it is one invocation of one engine, on mutants the author wrote, and the per-class picture is confounded with the *obligation* the specification attaches to each condition. | *"Under the default `-validate` invocation of this one binary, 23/32 of my authored mutants produced a relevant error (F4-01 counted as a defect). The four F7 misses are conditions no catalogue constraint names; the F5/F6 misses are discretionary or site-dependent. Of the observed items in the external set, the tool detected all 9 whose defect status is established and none of the 4 that are discretionary or contested."* |

**No headline numerator moves.** A's 9 is 9 in every version; B's 23 is 23 unless one adopts a
"named-constraint-only" defect criterion, which neither pilot uses (then 22). What moves is what the
numbers are *allowed to say*. That is the finding.

### 1.4 What the run as a whole establishes

Four propositions survive everything:

1. The pinned instrument is silent on 4 records that a careful reader called defects and that a
   second agent re-read — but all four are discretionary or contested, so **no detection gap over
   established, mandatory-report defects is demonstrated in either corpus** (A: 9/9; B external:
   9/9).
2. **The instrument's verdict surface is much wider than the surface both pilots measured.** Under
   `-satisfy`, `-instantiate … -validate=`, `-action`, `-state`, `-analysis` and `-engine smt` it
   decides requirement satisfaction, contradiction with bound values, dimension errors, execution
   failures and invariants — and under one engine (`check`) it returns a **false `holds` on an
   invariant its own SMT engine witnesses as violated** (reproduced, §2.4 run 1). Both pilots ran
   one mode; neither can say "the instrument cannot".
3. **Exit status is not a validity verdict** (error-severity diagnostics with exit 0), and severity
   is a separate axis. Reproduced in both pilots and by both reviewers.
4. **A pass is not a semantic pass**: a prose-only requirement returns `holds (vacuous)`, exit 0 —
   positively reported as holding. Reproduced on A's own S2 model (§2.4 run 8).

---

## 2. Method and pinned hashes

### 2.1 How rulings were made

- Every challenge was tested against the **artefact it names**, not against the other party's
  account of it. Where a challenge is about the instrument, I re-ran the instrument (§2.4). Where
  it is arithmetic, I recomputed from the raw CSV. Where it is about the specification, I quoted the
  pinned PDF text at `/tmp/sysml/` (hashes verified against `catalogue/README.md` §1 and against
  `TOOLING.md` for the binary).
- No majority voting, no model authority: all thirteen A→B and B→A objections were re-derived, and
  where the two cross-reviews conflict (A's 9/9 reading vs B's 0.72) the underlying factual
  question was adjudicated, not averaged (§7.1).
- "Unresolved" was used where the artefacts cannot decide the question and no legitimate retrieval
  or run available to me would. Unresolved items keep both readings visible with a named settler.
- Duplicates across sources are consolidated: each ruling names every source that raises it.
- No researcher artefact was edited. Corrections are instructions in
  [`CORRECTIONS.md`](CORRECTIONS.md), owned by the Lead.

### 2.2 Pinned artefacts (sha256, computed 2026-11-13T14:51:34Z)

| Artefact | sha256 |
|---|---|
| `research/relational/PROTOCOL.md` | `183a2c887d8361c36d81291735077e43d9751a845c26ec1595fab37d628594a7` |
| `research/relational/gate-log.md` | `87b4974095510b84478ef3ddd972c871524d29fe3d4a3261b7525db847b45202` |
| `research/relational/TOOLING.md` | `95e969c12e899af2a0fbbd697ab579601bd011ed85f7f7f3f63577c81b3edb9f` |
| `reports/issue-007-error-taxonomy-pilot.md` (810 lines) | `edf02fc6173da7f563aa2fad82ee8946a70498932ed28b27813ed3ea152cc2fd` |
| `reports/issue-008-validator-reliability-pilot.md` (848 lines) | `41c743e7eda27fa0de678df67f28cbaefe2a2374bdc2ed105fb31487e2630fcc` |
| `research/issue-008/empirical/REPORT.md` | `21252e16684928b1cb50707bb9f92dad323846f9bcae4288c64c864bf4130e8e` |
| `research/issue-007/METHODOLOGY-FROZEN.md` | `269d8dbe7228db83d20ca2be39991172f20fd23458ac1e5e6755ff7269564f76` |
| `research/issue-007/AMENDMENTS.md` | `34855cdfde7c71ce826b7db06ca667cfc5c828b8a038001b274d89e1d39fe559` |
| `research/issue-007/coding/CODEBOOK.md` (v1.3) | `106e620d6c6808f980f2f58d6e79f574bcd350dcf41978a4083df0cdd9063314` |
| `research/issue-007/coding/errors.csv` (frozen 14) | `30265ff57bdd1f4036304c6acbc1026678d36f0b3604c925a7b538455fc815f6` |
| `research/issue-007/coding/errors-post-inspection.csv` (7) | `285d70ea816eb3d73da9a954faba5f54d05292103da3c740abb9763da7851f74` |
| `research/issue-007/coding/errors-corrections.csv` (C01–C13) | `c551040564049eee7e358dfba63b0584c42a2807aca9986c2a417576566489ec` |
| `research/issue-007/coding/reconciliation.md` | `c99c1b072e912f8a702ec01ce44d59997d46c882aeb1114f2de80328d1cca272` |
| `research/issue-007/detection/summary.csv` | `556c7afd6e2c7a179ee0a4e3d85d1ef23a8ecacda19c2c8c213e542ffad3adee` |
| `research/issue-007/detection/diagnostics.csv` | (re-derived; counts in §2.4/§3) |
| `research/issue-007/detection/table.md` | `7b7a7cc1a5ff26a35d1e9f3a6392bc30c675d01ee1cc6d0a99c3feb29efebb72` |
| `research/issue-008/METHODOLOGY-FROZEN.md` | `2c80d63e8800be9ca67a051aaffdbc4b6c56c1b576002fc4446fe82862e6f00b` |
| `research/issue-008/mutants/MANIFEST.csv` | `a9f479748aea10c76460421031a384ddda779d4c78ea1cb6a5fe2f208f157be7` |
| `research/issue-008/results/analysis.md` | `ee630030d23baf07c150aa0a7962c783d7708184ca9c3315c75be0ea43b02d0f` |
| `research/issue-008/results/triage.csv` | `e4db5f1a3f4550af8b3d85df5a7920728158f5ff4172156d49f3ce1d2d54815b` |
| `research/issue-008/results/known-good-triage.md` | `3feeb8c85636fb11fb6f9022da3eb5493eadc2ba0a82f309ab18fcc581b08901` |
| `research/issue-008/empirical/PRE-REGISTRATION.md` (contains AM1) | `9458406e7db665ac42f5a3a896a7dc05b094b0fb6e8ef3a4ab9ed9db7e6acfbc` |
| `research/issue-008/empirical/run-log.md` | `a3fca89887bceb95207dcb4eaee4e3d2c337bd286721b1178a9c6ddc4fd4f1d4` |
| `research/issue-008/empirical/results.csv` | `96e1b0b7272569218946db848ace85e2ebac4a8183a1fa2584dc665fd6c5a875` |
| `research/relational/empirical-subset/FROZEN-SUBSET.md` | `fce76f47776293b39a008209f950293b71431dc7e1e117de991288aaec0c6c03` |
| `research/relational/empirical-subset/subset.json` | `bc2b92a5fdff6e976ae7156b13beba3535f0895e4a41268cf76c1551a6c3dfaa` |
| `A-reviews-B.md` | `05ca64ccaa4ceae4032ca36aa22f2090c5565449d021764a9da480bbbb1a8102` |
| `B-reviews-A.md` | `de2d99cea17587a9603e9602303873556db9b00f93d8101451c0db57be9af0b1` |
| `A-response-to-B-review.md` | `965924fe8e2bce7a1387aef44060bfe7292219461f6cdaaf353c9d61151ebd45` |
| `B-response-to-A-review.md` | `3ccbfce43320a870611479bdd127a9d1b5b37cfd3b8be98ff88b62cace2612bb` |
| `reviews/reviewer-a-issue-007.md` | `8e3b099246f0c53d38f73116e744b7372e9e37d32a31ffecf43b7683fb6631e7` |
| `reviews/reviewer-b-issue-008.md` | `2090ba1c60f166f2664f65664244a682b1911de3bcd0a0d14b094d857a753fc1` |
| `critique/semantic-ceiling-critique.md` | `e549ca6ea56c6a655f1bc7ba14f51b0dda3c3e658c509c7d3a4959c91093958a` |
| `critique/CLAIMS.csv` | `47eecedc856c758957d6e64d103fe6d2073600659f235d5399c248276a2d8179` |
| `.tools/sysml` | `ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0` |
| `/tmp/sysml/sysml-2.0-language.pdf` | `46e6c0476a6f1f34f367d57e039d56659bff75e41d2e4b3d37ca4cadea84a83a` |
| `/tmp/sysml/kerml-1.0.pdf` | `3bcc96f989bfa9d05cd28e026df3351b795fe8d494187b87bff3db7d96373697` |

The two PDFs match `catalogue/README.md` §1; the binary matches `TOOLING.md` §1.

### 2.3 Stability of the tree

The tree **did not move during this adjudication**: every artefact above re-hashed to the same value
at 2026-11-13T15:03:54Z as at 14:51:34Z. That matters because the tree moved twice during earlier
phases (Reviewer A's P-1, Reviewer B's boundary note, and A's own acknowledgement that its pipeline
re-run overwrote an addendum). All rulings below cite the pinned bytes, which are the bytes both
reviewers reviewed (`edf02fc6…`, `41c743e7…`, `8e3b0992…`, `2090ba1c…`, `e549ca6e…`), so no ruling
depends on a version the reviewers did not see. Files that changed *before* my pin are recorded in
each ruling where relevant (A's response hash, A's combined CSV, A's codebook).

### 2.4 Runs I made myself (independent reproductions)

All with `.tools/sysml` (v0.12.1, `ddfc2962…`), 2026-11-13T14:52–15:02Z, read-only, from the
repository root; output compared to the stored raw files.

| # | argv | result | what it settles |
|---|---|---|---|
| 1 | `-action Seq -engine check -check-property within15 critique/probes/p08b-invariant-violated.sysml` | `no violation, exhaustive (3 states, 2 moves, depth 2)`, `outcome: x = 20.0`, `standing: holds (bounded …)`, **exit 0** | the false `holds` is real |
|  | same, `-engine smt` | `at step 2 … assertion evaluated to false: x <= 15.0`, `standing: violated (witnessed …)`, **exit 1** | same model, contradictory verdict |
|  | same, `-engine all` | `violated …; all: check not covered (check claimed holds (bounded) but smt witnessed violated; the interpreter's witness stands)`, exit 1 | the tool names its own disagreement |
| 2 | `-instantiate gauge -validate=gauge critique/probes/p07b-assertions-contradictory.sysml` | `1 of 2 assertions fails`, `standing: violated (witnessed …)`, exit 1 | contradictory assertions with bound values **are** decided |
| 3 | `-instantiate gauge -validate=gauge critique/probes/p07c-assertions-unbound.sysml` | `2 of 2 assertions undecided`, `standing: not covered`, exit 2 | encoding (a bound value) flips decided↔undecided |
| 4 | `-action Pipe -engine run critique/probes/p02d-flow-unwired.sysml` | `execution failed … multiplicity violation: 0 value(s) bound to a feature with multiplicity lower bound 1`, exit 2 | a missing flow **is** decided when the sink reads it |
| 5 | `-satisfy critique/probes/p03a…` / `p03b…` | `holds`, exit 0 / `fails … Required condition evaluated to false`, exit 1 | requirement satisfaction is decided when encoded as a `require constraint` |
| 6 | `-state Mission -advance 100 -engine check critique/probes/p01b-state-terminal-unreachable.sysml` | `outcome: finalState running; visits idle, running` — `done` absent; exit 0, no violation | unreachability is **observable**, never a verdict |
| 7 | `-validate critique/probes/p12-fixed-binding-redefinition.sysml` | `error[feature-value-overriding]`, exit 2 | the F5-01 diagnostic **exists and fires** where the redefinition is explicit |
| 8 | `-satisfy research/issue-007/corpus/normalized/T2-C2.sysml` | `✓ satisfy lowerBeforeArrival holds … (vacuous: requirement … states no required constraint)`, exit 0 | a prose-only requirement is reported as **holding** |
| 9 | `-validate -format json research/issue-008/results/probes-gate2/P3-succession-source-declared.sysml` | `warning[name-conflict]: Duplicate of inherited member name 'start' from Action` | `Action` inherits `start`; C12's premise is right on instrument evidence |
| 10 | `-validate research/issue-008/mutants/M31-F5-01-feature-value-overriding.sysml` | one `warning[name-conflict]`, `no errors`, exit 0 | F5-01's only signal is the base's own warning |
| 11 | `-analysis over critique/probes/p11-verification-case.sysml` | `distance = [50.0]`, `assertion distance <= 40.0: not satisfied`, verdict `inconclusive — bound no VerdictKind value`, exit 2 | verification postconditions are evaluated per assertion |

**Recounts from raw tables (no tool):** 18 normalised models → 6 clean, 12 with any diagnostic,
**9 with a non-zero exit status**, and 3 with an error-severity diagnostic at exit 0 (T2-C2,
T6-C1, T6-C3); raw diagnostics = 72 `syntax` + 9 `reserved-keyword-name` = 81; external = 18
positive (2 error-level, 9 `name-conflict`-only warnings at exit 0, 7 clean) + 6 negative
(6/6 error-level); mutants with ≥1 error = 23, with any diagnostic = 28, diagnostics-per-mutant
distribution 1→23, 2→3, 3→1, 5→1 (so "24 of 28" is wrong and the correct count depends on the
reading: 23 of 28 by any severity, 20 of 23 error-bearing by errors); external M2/M3 evaluated
items = **3 each**, not 1. **Construct census over A's 18 normalised models** (my own grep):
`require`/`assert constraint` **0/18**, metadata annotation **0/18**, `connection def` **0/18**,
unit literal **0/18**, `satisfy` **18/18**, `import SI::` **3/18** — B's census reproduces.

---

## 3. Accepted challenges, with corrections

Format: **claim** → **ruling** → evidence → reasoning → residual uncertainty → required correction.
Line numbers refer to the pinned bytes in §2.2.

### 3.1 A → B

#### A2B-01 — F7-02 is detectable by the pinned instrument; "invisible to the only available instrument" is unsupported
**Sources:** `A-reviews-B.md` §5 O1 (blocking); B's `B-response-to-A-review.md` §1–§2; report
`issue-008…§A2` (lines 473–521); also R-B C4b/C17 and critic C07/C20.
**Ruling: ACCEPTED.** A's reproduction is exact and B's own acceptance is verified.
**Evidence:** A-reviews-B line 196–206; my run 2.4/5; report A2 lines 484–495; positive control
`KG-07` → `holds`, exit 0.
**Reasoning:** the same binary returns `violated` on the mutant and `holds` on its known-good base
under `-satisfy` **and** `-instantiate vehicle -validate=vehicle`, so the invocation discriminates
the mutant from its base. What B measured is the blindness of one verb (`-validate`), not of the
instrument. B's correction (A2) and the P3 restatement are honest and complete.
**Residual uncertainty:** F7-02 is decidable *only because B authored a checkable
`require constraint`*; a prose-only requirement returns `holds (vacuous)` (my run 2.4/8), so the
verdict path's reach in real generation may be near zero (0/18 in A's corpus).
**Correction required:** none outstanding — A2 is correct; the *front* of B's report must point at
it (see CC-05/CC-12 and CORRECTIONS B-1).

#### A2B-02 — the instrument's verdict is multi-valued; a binary measure cannot represent "checked and undecided"
**Sources:** `A-reviews-B.md` §5 O2; B's response §3; report A3 (lines 525–547); critic S4/C19.
**Ruling: ACCEPTED.**
**Evidence:** my run 2.4/3 (`2 of 2 assertions undecided`, `standing: not covered`, exit 2) versus
run 2.4/2 (`1 of 2 assertions fails`, `violated`, exit 1) on models differing only in whether the
feature is bound; report A3 lines 531–544.
**Reasoning:** `checks[]` with a `standing` is a different output surface from `diagnostics[]` with
codes, and "undecided" is neither silent nor detected. B added a five-valued category and
correctly noted that "undecided" does not discriminate F7-04 from its base (2 vs 1 undecided), so
it is a shape signal, not a verdict.
**Residual uncertainty:** the five categories are demonstrated on four mutants and a handful of
probes; no claim about their frequency is possible.
**Correction:** none outstanding (A3 stands); the §3.1 measurement definitions should name the
standing vocabulary (CORRECTIONS B-2), and the base-vs-mutant non-discrimination must stay in the
text.

#### A2B-03 — a notation error can be reported at `error` severity with exit 0; F1's 4/4 is a statement about B's four mutants
**Sources:** `A-reviews-B.md` §5 O3 (and O9); report A4 (lines 551–585); R-A M-2; critic C06.
**Ruling: ACCEPTED.**
**Evidence:** `detection/summary.csv` rows T2-C2, T6-C1, T6-C3: `exit_code=0`,
`n_error=1`, `nonblocking_notation_only=yes`, code `reserved-keyword-name`; A's `probe07` and B's
`P1` reproduce it; `-strict` converts the exit to 2. My run 2.4/9 shows the same code on a
Gate-2 probe.
**Reasoning:** B's four F1 mutants are parse breakages that all exit 2; the empirically dominant
notation mechanism in A's corpus (7 of 9 notation records: a reserved keyword used as a name) is a
different sub-class with different exit behaviour. F1 4/4 therefore does not generalise to
"notation", and the severity discussion in B's §3.3 covered only the warning case.
**Residual uncertainty:** none material; the sub-class has 7 instances in A's corpus and one
independent probe.
**Correction:** already applied as A4; ensure §3.2's F1 row carries "authored family" (B-3).

#### A2B-04 — F5's 3/4 is a property of B's mutant family; the empirical satisfy defect is missed and positively reported as holding
**Sources:** `A-reviews-B.md` §5 O4; report A5 (589–610) and A10.1 (779); empirical REPORT §6.2.
**Ruling: ACCEPTED**, on B's own condition that the cross-corpus item is labelled and never merged
into the frozen denominator.
**Evidence:** my run 2.4/8 (`holds … vacuous`, exit 0 on A's `T2-C2`); empirical raw
`ES-T2-C2-E01__M2`; report A5.
**Reasoning:** B's F5-02 (`satisfy Vehicle by vehicle`) violates
`validateSatisfyRequirementUsageReference` and is caught; A's S2 (`satisfy lowerBeforeArrival;`)
violates a different named constraint and is not caught — worse, the tool reports the requirement as
holding and explains the vacuity by the requirement's *body*, not the missing binding. Two rates
(3/4 authored; 3/5 cross-corpus) must both be printed, which B does.
**Residual uncertainty:** S2's constraint is a `check` with the obligation "MAY report, satisfy by
implied relationships, or ignore" (`catalogue/classified.csv` row
`checkSatisfyRequirementUsageBindingConnector`), so the item is discretionary; a tool that creates
the implied binding is not failing at its job. That does not weaken the finding that the *output*
would mislead a reader.
**Correction:** keep both rates; add the obligation status of the constraint so the reader can see
it is discretionary (B-4, A-9).

#### A2B-05 — resolution coverage is site-dependent; succession sources are not resolved at all
**Sources:** `A-reviews-B.md` §5 O5; report A1 (432–448) and A6 (614–644); empirical REPORT §10.
**Ruling: ACCEPTED.**
**Evidence:** probe `P2-succession-source-undefined` and the `/tmp/p2b.sysml` variant (`first zzz;`)
both exit 0 with zero diagnostics, reproduced in B's run log; `P5-satisfy-target-undefined` →
`error[unresolved]`, exit 2; A's four `satisfy`-target N1 items are 4/4 detected.
**Reasoning:** an arbitrary undefined name at a succession source is as silent as the library name,
so the gap is at the site, not the name — the strongest form of A's objection, and B stated it
better than A did. F2 4/4 is four sites, not a class.
**Residual uncertainty:** four sites plus one silent site is a small census; other reference
positions (flow ends, connector ends, metadata arguments) are untested.
**Correction:** A6 stands; the three-way statement (type/expression/satisfy references resolved;
succession sources not) must appear wherever F2 is quoted (B-5).

#### A2B-06 — the missing-prelude class is absent from B's corpus, and the documented confound is real
**Sources:** `A-reviews-B.md` §5 O6; report A6 second half; `TOOLING.md` §1.
**Ruling: ACCEPTED**, with B's refinement accepted too.
**Evidence:** probe `P4-missing-prelude` → two `error[unresolved]`, each naming
`ScalarValues::…` and instructing the reader to import the package; A's `T3-C1` diagnostics carry
the same "did you mean `ScalarValues::Real`" text (`detection/diagnostics.csv`).
**Reasoning:** B's bases all import the prelude, so B could not test the confound `TOOLING.md`
warns about; the probe shows the confound is *distinguishable by message* and *not* distinguishable
by counting `unresolved`. Both halves are true and both matter for anyone computing a pass rate.
**Residual uncertainty:** the message-text discriminator is an implementation property of this
binary, not of the language.
**Correction:** A6 stands; state the confound as measured, not avoided (B-5).

#### A2B-07 — the fault model samples the specification's demonstration surface, not the generation surface
**Sources:** `A-reviews-B.md` §5 O7 and §3; report A7 (648–690); R-B C37/C40; B's own §8.4.
**Ruling: ACCEPTED** as a scope limitation (not an error in the mutants).
**Evidence:** B's census over the 18 normalised models (report A7, lines 655–671): `satisfy` 18/18;
`require`/`assert constraint` 0/18; unit literal 0/18 (SI imported in 3/18); metadata 0/18;
`connection def` 0/18; explicit `end` 0/18; short name 0/18. My recount of the same models by
grep confirms the 0/18 cells for constraints, metadata and `connection def`.
**Reasoning:** F4, F6, F8 and most of F5/F7 live on constructs this corpus never emits, so per-class
rates for those classes are untestable against observation — which B's external arm then
demonstrated rather than merely argued. The *layer* statement travels; the class distribution does
not.
**Residual uncertainty:** A's prompts are simple by construction, so the census may under-sample the
constructs; that cuts both ways and is stated by both researchers.
**Correction:** A7 stands; B's §3.1 and §8 must carry the construct-frequency assumption per mutant
(B-6).

#### A2B-08 — reading the `-explain` inventory bounds what the expectation audit can claim
**Sources:** `A-reviews-B.md` §5 O8 and §4.2; report A8 (694–728); R-B RB-03 (which extends it to
the pre-freeze calibration log); critic C18 (credit).
**Ruling: ACCEPTED.**
**Evidence:** `results/calibration/PRE-FREEZE-CALIBRATION.md` (lines on `-explain`, and the `m1`/`m2`
metadata firings); report §4.1 lines 189–193 names only `-explain`; A8 lines 701–712.
**Reasoning:** the detection counts are computed from raw diagnostics and are insulated from the
expectations, so the headline is safe; the *audit* is not, and the signature of anchoring is visible
(24/24 expected-detectable produced a signal; both expectation errors lie in the "expected
undetectable" bucket and both err towards the tool being stricter). A's diagnosis is right; RB-03
shows the pre-freeze calibration log is a larger channel than `-explain` alone.
**Residual uncertainty:** the audit's weakness is a matter of degree; no artefact can show what the
author was thinking, only what it had seen.
**Correction:** A8 stands; extend the disclosure to the calibration probes (B-7, RB-03).

#### A2B-09 — F1-04 and F4-02 are spec-idiom constructs, not the empirical counterparts
**Sources:** `A-reviews-B.md` §5 O9 and O10 (minor); report A4/A7.
**Ruling: ACCEPTED.**
**Evidence:** short names `<'…'>` 0/18 in A's corpus; `connection def` with explicit `end` 0/18;
F4-02's only diagnostic is a warning; A's R1 is a chain through a multi-valued usage in a `connect`.
**Reasoning:** F1-04 cannot be produced by a generator that never writes a short name, and F4-02 is
declared-multiplicity, not connection-end structure. Both are legitimate specification-surface
probes; neither may be counted as evidence about generation.
**Residual uncertainty:** whether a generator asked for quantities/constraints *would* emit short
names is untested.
**Correction:** A4/A7 stand; F4 must be labelled "declared multiplicity" wherever the class table is
reproduced (B-8).

#### A2B-10 — `MANIFEST.csv`'s mtime post-dates the run that it pre-registers
**Sources:** `A-reviews-B.md` §5 O11; report A9 (732–750); R-B C20, which adds that the 32 mutant
files carry the same rewritten mtime.
**Ruling: ACCEPTED.**
**Evidence:** `expectations.sha256` 14:13:00Z; first run 14:13:03Z; `MANIFEST.csv` mtime 14:15:56Z;
`shasum -c` OK today (report A9); R-B's finding that `mutants/*.sysml` share the mtime and
`mutants.sha256` also verifies.
**Reasoning:** content is unchanged (hash chain intact), and B names the cause (its own documented
reproduce step, run to demonstrate idempotence). But an idempotent rewrite of a pre-registration
artefact after the run is a process error even when content is identical, and A9 names only
`author_manifest.py` when the mutants were rewritten too.
**Residual uncertainty:** none — hash chain verifies.
**Correction:** A9 must include the mutant files in the disclosure (B-9).

#### A2B-11 — "every emitted error was about the injected defect" measures the design, not specificity
**Sources:** `A-reviews-B.md` §5 O12; report A8 second half (713–726); R-B RB-08.
**Ruling: ACCEPTED.**
**Evidence:** `results/diagnostics.csv`: 30 error diagnostics over 23 error-bearing mutants; one
mutant yields 3 (`F1-03`) and one yields 5 (`F1-04`); recomputed distribution in §2.4.
**Reasoning:** with one injected defect per mutant, any-error = relevant-error is close to
tautological; the cascade cases show one defect can produce five diagnostics, so the sentence must
be labelled "relevance, not precision". A's requested table exists but its arithmetic is wrong
(RB-08).
**Residual uncertainty:** relevance judgement is single-coder and post-hoc.
**Correction:** restate as relevance; correct the counts (B-10).

### 3.2 B → A

#### B2A-01 — `T5-C3-P01` cites an excerpt that does not occur in its model
**Sources:** `B-reviews-A.md` O1; A's response §1; report A §16.1 (line 648); R-A claim 4.
**Ruling: ACCEPTED.**
**Evidence:** `grep -n port research/issue-007/corpus/normalized/T5-C3.sysml` returns only line 2
(`import`); line 26 is `part antenna : Antenna;`; the row duplicates `T6-C1-P01`. A concedes,
withdraws the row (C01) and answers the more interesting question: the substring check existed and
was applied to the delegate's output, not to A's own additions.
**Reasoning:** an excerpt that is not a substring of its own model cannot stand whatever the class
label; the withdrawal is correct and the process finding (check not applied to one's own rows) is
the real result.
**Residual uncertainty:** whether other post-inspection rows would survive the check if it were
re-run at source; A's `apply_corrections.py` now enforces it, and it passes on the 19 combined rows.
**Correction:** C01 stands; combined arm 21→20 and S1 9→8 must replace the stale §1/§5.4 numbers
(A-1).

#### B2A-02 — §5.4 describes eight post-inspection defects but the file has seven, and a real `port out;` occurrence is recorded nowhere
**Sources:** `B-reviews-A.md` O2; A's response §2; codebook §11.1; `reconciliation.md`.
**Ruling: ACCEPTED** (correction), while **rejecting B's "missing row" framing** — which is a
framing dispute, not a factual one, and A's reconciliation shows the occurrence was folded rather
than omitted.
**Evidence:** `errors-post-inspection.csv` has 7 rows; T3-C2 lines 23 (`port in;`), 24
(`port out;`), 33 (`line.in`); the frozen row's span was `23,33`, so line 24 appeared in prose
only. My validator run on T3-C2 flags 23 and 24 and not 33 (A's `occurrence_detection.csv` records
2/3).
**Reasoning:** B is right on both counts that matter — the phantom inflates S1, and a real
occurrence was described but not recorded — and A's C02/C03 fix both. Calling it a missing *row*
is wrong under the codebook's coding unit (mechanisms, not occurrences), so the fix is an
occurrence-list correction, which is what was done.
**Residual uncertainty:** none material.
**Correction:** none outstanding on the numbers; §5.4's "seven further defects" must become "six
live records" (A-1).

#### B2A-03 — the frozen T1 row (42–44) contradicts codebook §10.4's "narrowed to 42–43"
**Sources:** `B-reviews-A.md` O3; A's response §2; codebook §11.2.
**Ruling: ACCEPTED.**
**Evidence:** `errors.csv` T4-C1-E01 `line_range = 42-44` with `then assign;` in the excerpt;
codebook §10.4 claimed the span was narrowed; codebook §11.2 now records that §10.4's claim was
false and that the narrowing is C04 in the corrections file.
**Reasoning:** two artefacts cannot both be true; A's convention (frozen file immutable,
corrections in a dated register) resolves it, and the convention is now stated. A reader can tell
which version the detection table used only because the convention is stated.
**Residual uncertainty:** none.
**Correction:** C04 stands; the convention must also appear in the report's §16 (A-2).

#### B2A-04 — "line 42 (`first checkCharge;`) is not visibly defective as written"
**Sources:** `B-reviews-A.md` O3, sub-claim; A's response §2.
**Ruling: REJECTED.**
**Evidence:** A quotes `InitialNodeMember : MemberPrefix 'first' memberFeature = [QualifiedName]`
(SysML 2.0 §8.2.2.17.2), a cross-reference to a *feature*; `checkCharge` is declared `action def`
(line 47–49), i.e. a type, not a feature. The tool's `endpoint-not-a-node` at line 43 shows the tool
treats these as action-node endpoints while being silent at the source (the succession-source gap,
probe01). My run on the declared-succession probe reproduces the silence and the inherited-member
warning.
**Reasoning:** the record's claim is a kind mismatch on a succession endpoint, and a definition is
not a feature; the syntax tree does not admit a definition there. B's inference from the tool's
silence is invalid here because the tool is independently known not to resolve succession sources
(A2B-05), which is exactly the case where silence cannot be read as "legal".
**Residual uncertainty:** A's reading depends on `[QualifiedName]` resolving only to features; the
metamodel states `memberFeature` is a `Feature`, so the constraint is on the reference target and I
find no route by which a definition satisfies it.
**Correction:** none — B's sub-claim is wrong and should not be carried into any correction. A's
span correction (B2A-03) stands on its own.

#### B2A-05 — no hash evidences the pre-detection freeze of `errors.csv`
**Sources:** `B-reviews-A.md` O4; A's response §1 (claim withdrawn); report §16.2; R-A claim 12
("unverifiable").
**Ruling: ACCEPTED**, as a withdrawal of an evidentiary claim.
**Evidence:** `FREEZE-HASH.txt` holds the methodology hash; `CODEBOOK-HASH.txt` the codebook;
`errors.csv` mtime 14:17Z coincides with `detection/*.csv` because A re-ran the pipeline for
determinism (report §16.2, lines 666–701). No hash artefact exists.
**Reasoning:** the protocol makes a hash at freeze the mechanism, and the mechanism was not used.
The composition argument (the frozen 14 omit exactly the cheap tool-flagged defects and include
records the tool cannot see) is good inferential evidence and A labels it as such; but it is an
argument. Note that C12 removes one of the three "silent" records the composition argument used, so
the argument is weaker after A's own correction, not stronger.
**Residual uncertainty:** the ordering is not knowable from the artefacts; the mtimes were reset by
re-runs.
**Correction:** the report's Proposition 1 and the banner must not say "hashed before detection"
(A-3).

#### B2A-06 — κ = 1.0 is contaminated by verbatim codebook exemplars
**Sources:** `B-reviews-A.md` O5; A's response §1 (8/11, not 7/11); report §16.5; R-A M-5;
`agreement-addendum.md`.
**Ruling: ACCEPTED** (A's count of 8/11 is more accurate than B's 7/11; verified by R-A and not
contested by B).
**Evidence:** `coding/second-coder/CODEBOOK.md` contains `first start;`, `satisfy greenhouse to
moistureControl;`, `satisfy lowerBeforeArrival;`, `port in;`, `satisfy alarmTiming by pump;`,
`first checkCharge;`, the `connection powerLink …` line, and the transition line across a line
break; the remaining three are the `subject pump : InfusionPump;` exemplar's sub-mechanism.
**Reasoning:** the coder-facing codebook is a de-identified answer key for essentially every paired
record, so class agreement on those records is reproduction, not reliability. A's downgrade is
correct and, unusually, worse for A than the reviewer's version.
**Residual uncertainty:** what survives (three clean calls, the reserved-keyword notices) is
genuine discrimination but is not a reliability statistic.
**Correction:** κ must not be quoted as inter-coder reliability in report §6/§16, the README or the
subset (A-4).

#### B2A-07 — the layer/severity agreement figures measure version skew
**Sources:** `B-reviews-A.md` O6; A's response §2 (accepted); report §16.1.
**Ruling: ACCEPTED.**
**Evidence:** the coder-facing copy is v1.0 (S2 = "syntax/parse, blocking"); the differing pair is
S2, whose definition A changed after reading the BNF (`by` is optional, §8.2.2.21.2).
**Reasoning:** exactly one pair differs and it differs because the two coders were handed different
definitions, so 10/11 measures version skew, not disagreement. The related point stands too: "11/11
class agreement" includes a pair that agreed on an identifier whose definition was later found
false.
**Residual uncertainty:** a re-coding under one version would test whether any real disagreement
exists; not run.
**Correction:** annotate the two rows; the second coder's INSTRUCTIONS also asserted the false rule
(RA-05, A-5).

#### B2A-08 — three recomputable numeric slips (range, W1 prose-only count, missing column)
**Sources:** `B-reviews-A.md` O7; A's response §2; report §16.1, §16.7.
**Ruling: ACCEPTED.**
**Evidence:** `models.csv` maximum `n_errors` = 2 (T3-C2, T4-C1); preamble 4 / trailing prose 6 /
union 7; `trailing_prose_present` added as a column.
**Reasoning:** all three recompute as B says; none changes a conclusion, and A applied all three.
**Residual uncertainty:** none.
**Correction:** applied; ensure the §1 table carries 0–2 and 18→7 (A-1).

#### B2A-09 — R1's layer label is an authored placement and its admission criterion is not operationalised
**Sources:** `B-reviews-A.md` O8; A's response §2 (partly accepted, criterion stated); C05/C06;
R-A M-3 (extends to defect status); critic C02.
**Ruling: ACCEPTED**, and the challenge is **stronger than A conceded**: it goes to defect status,
not only to layer (see RA-03/X-03).
**Evidence:** `errors.csv` T4-C1-E02 notes the cited `validateFeatureEndMultiplicity` is "adjacent,
not decisive"; `CODEBOOK.md` says no named constraint decides feature chains over multi-valued
usages; A's stated criterion ("after resolving its feature chain, it denotes more than one
feature") conflates a feature with its instances — `controller.fleet.battery.power` denotes the one
feature `power` whose featuring instances number ten.
**Reasoning:** the operational criterion is an authored rule with no normative basis, and as worded
it does not distinguish "the end denotes many features" from "the end denotes one feature through a
multi-valued featuring". A's re-layering to `type/typing` is the right layer call but does not
establish that the construct is ill-formed. The tool is silent on both instances either way, so no
detection number moves.
**Residual uncertainty:** whether a connection end through a multi-valued feature is ill-formed
under KerML's connector-end rules — unresolved (X-03); the nearest named rule
(`validateFeatureEndMultiplicity`) constrains end features' own multiplicity, not traversed ones.
**Correction:** mark R1 `frozen_contested` as to **defect status** (not only layer) and restate the
criterion in terms a third party can apply (A-6).

#### B2A-10 — I1's "no reading reconciles" is asserted; a reconciling reading exists
**Sources:** `B-reviews-A.md` O9; A's response §2 (contested, not withdrawn); R-A §4.2.
**Ruling: ACCEPTED**, on the record's status, not on withdrawal.
**Evidence:** `errors.csv` T1-C3-E01 excerpt: doc "between 35% and 75%", `upperBound : Real = 55.0`;
no constraint relates documentation to values (`deriveElementDocumentation` relates documentation to
content, not values); `errors-corrections.csv` C07 marks it `frozen_contested`.
**Reasoning:** a documented band of 35–75% that contains a declared 35–55% bound is not
contradictory on its face; A's original justification only holds if the doc sentence is read as
asserting the value of `upperBound`, which the text does not compel. A's refusal to withdraw it (the
correction would flatter the rate) is the right protocol move, and reporting 9/14 and 9/13 side by
side is honest. R-A's refinement is right: the codebook's definition ("no reading reconciles") is not
met, so the contested status belongs in the codebook, not only in a CSV field.
**Residual uncertainty:** the defect-status question is genuinely two-way; no constraint decides it.
**Correction:** add a "contested" status to the codebook and keep both denominators (A-7).

#### B2A-11 — two specification citations do not support their classes
**Sources:** `B-reviews-A.md` O10; A's response §2; C08/C09/C10.
**Ruling: ACCEPTED.**
**Evidence:** `errors.csv` T1-C2-E01 cites `checkSatisfyRequirementUsageBindingConnector`
(8.3.21.10), a `check` with a MAY obligation about implied bindings, for a *notation* defect decided
by the `SatisfyRequirementUsage` production (§8.2.2.21.2); T2-C1-E01 cites §8.3.18.9 (abstract
syntax) for a notation violation, while the textual notation is §8.2.2.18.
**Reasoning:** a class whose point is "the notation does not admit this text" must cite the
notation production, not a discretionary semantic constraint. A corrected both, and labelled T2's
`checkAttributeUsageSpecialization` (class B/MAY) with the §7.7.1 prose as the decisive basis —
which is the right treatment.
**Residual uncertainty:** none.
**Correction:** C08/C09/C10 stand; the codebook's S1 class table still cites the wrong clauses
(RA-04).

#### B2A-12 — detection is counted per record, never per occurrence
**Sources:** `B-reviews-A.md` O11; A's response §2.
**Ruling: ACCEPTED.**
**Evidence:** `detection/occurrence_detection.csv`: T2-C1 4/4, T3-C1 9/9, T3-C2 2/3, T4-C1 1/2.
**Reasoning:** "detected" can rest on one of three occurrences; the record-level column is an upper
bound for two records, and A says so. The occurrence table omits T6-C2 (R-A m-3).
**Residual uncertainty:** occurrence counting is itself a coding judgement.
**Correction:** A-8 (add T6-C2 to the occurrence table and the ceiling wording).

#### B2A-13 — the external arm's "11 of 18 positive-folder files fail" is, for 9 of the 11, a statement about warnings
**Sources:** `B-reviews-A.md` O12; A's response §2 (comparison withdrawn); report §16.6.
**Ruling: ACCEPTED.**
**Evidence:** my recount of `detection/summary.csv`: positive folder = 2 error-level
(`usage-typing`, one with `name-conflict` too), 9 `name-conflict`-only at exit 0, 7 clean; negative
6/6 error-level. 119 of 140 external diagnostics are `name-conflict` warnings.
**Reasoning:** "fail" was defined as "any diagnostic present", which conflates warning with error
and applies a stricter standard to the external arm than A applies elsewhere (probe07). The 51.16%
comparison is not like-for-like — the files are `iteration_00` of cases selected because they
converged — and withdrawing it is right.
**Residual uncertainty:** whether the `name-conflict` warnings are defects (§5.1).
**Correction:** applied; the warning-level framing must also survive into the codebook/README (A-1).

#### B2A-14 — the detection run does not record the per-file sha256 and tool identity the frozen plan required
**Sources:** `B-reviews-A.md` O13; A's response §2.
**Ruling: ACCEPTED.**
**Evidence:** `METHODOLOGY-FROZEN.md` §7.2; `detection/manifest.json` now carries tool path, sha256,
`-version`, argv and per-file sha256 for all 70 artefacts.
**Reasoning:** the raw files carried argv and exit status (which is why B could reproduce the run)
but not model hashes, so a change to a normalised model after the run would be invisible. The
practice existed in the same pipeline for the external arm.
**Residual uncertainty:** `manifest.json` was written after the run, so it pins the current models,
not the models as run — the same limitation A conceded for `errors.csv`, but harmless because all 18
normalised bodies are verbatim substrings of the raws (R-A verified).
**Correction:** applied.

#### B2A-15 — `first start;` is legal SysML 2.0; the record is withdrawn
**Sources:** B's post-closure note (a); `AMENDMENTS.md` A7.1; C12; report §17.1.
**Ruling: ACCEPTED.**
**Evidence:** my run 2.4/9: a locally declared `action start;` produces
`warning[name-conflict]: Duplicate of inherited member name 'start' from Action` — instrument
evidence that `Action` inherits `start`, independent of the library text A cites
(`sysml.library/Systems Library/Actions.sysml` line 43, sha256 `ac36c940…5693`) and of R-A's
independent fetch of the same file.
**Reasoning:** the record's stated basis ("no action usage named `start` is declared") is false; the
name resolves to the inherited action. Withdrawal lowers the population to 13 and moves the rate
*upward*, against A's interest, which is the strongest single act of discipline in the run. Note
this also removes one of the three "silent" records from the composition argument for the freeze.
**Residual uncertainty:** the library is not stored in the repository, so a reader cannot check it
offline; the instrument warning is the check available in-tree.
**Correction:** C12 stands; every place quoting 14/12/6 must show 13/11/7 as well (A-1).

#### B2A-16 — the construct census said 0/18 for ISQ/SI; it is 3/18 for SI
**Sources:** B's post-closure note (b); `AMENDMENTS.md` A7.2; C13.
**Ruling: ACCEPTED.**
**Evidence:** `grep -l "import SI::"` matches T3-C2, T3-C3, T5-C1; no model imports ISQ; no model
writes a unit literal.
**Reasoning:** the substance (no unit-typed quantity in the corpus) survives; the "0/18" phrasing
was wrong and is corrected in the register rather than by editing the frozen cross-review, which is
the right convention.
**Residual uncertainty:** none.
**Correction:** applied; B's A7 already carries the corrected census (B-11).

### 3.3 Reviewer A (independent review of #7)

#### RA-01 (M-1) — the 9/14 blind spot is composed of one withdrawn, one discretionary and two contested records; established, mandatory-report records are detected 9/9
**Sources:** `reviewer-a-issue-007.md` M-1, claims 3 and 10; report §5.1/§5.3/§17; C12; C07;
`catalogue/classified.csv`.
**Ruling: ACCEPTED.**
**Evidence and arithmetic:** frozen 14 = N1 5, S1 3, N2 1, T1 1, R1 2, S2 1, I1 1. C12 removes
T1-C1 (N1) → 13. The five silent records in the published table are: T1-C1 (`first start;`,
**withdrawn as legal**), S2 (**a `check` with the obligation "MAY report, satisfy by implied
relationships, or ignore"**), R1 ×2 (**no named constraint; defect status contested**, RA-03), I1
(**contested**, B2A-10). Removing those leaves S1 3 + N1 4 + N2 1 + T1 1 = **9 records, of which
the tool detects 9/9** (§5.1 per class: S1 3/3, N1 4/5 with the miss being the withdrawn record,
N2 1/1, T1 1/1). The ladder: 9/14 → 9/13 (C12) → 9/12 (−I1) → 9/10 (−R1) → **9/9 (−S2's
discretionary reporting)**.
**Reasoning:** every silent record is one the report itself now marks withdrawn, discretionary or
contested, so the sentence "silent on 5 of 14 … neither method is an oracle" is arithmetically
right and interpretatively wrong: it presents a disagreement with disputed records as a blind-spot
measurement. The correction does not require deciding S2/R1/I1 in A's favour — it requires that the
composition be shown. I add two cautions of my own: (i) 9/9 is a *post-hoc subset* and must not be
read as a sensitivity estimate; the nine records span only notation, resolution and typing, so the
subset is exactly the region the instrument is known to cover; (ii) this is the same composition
problem that affects B's external arm, which nobody noticed (X-01).
**Residual uncertainty:** whether S2/R1/I1 are defects at all is not settled (X-03); if any of them
is an established defect, the 9/9 claim narrows accordingly (it would become 9/N with the record
counted as a miss).
**Correction:** replace the blind-spot sentence in §1 finding 2, §5.3 and §13.2 with the ladder and
the composition, and label 9/9 a subset result (A-9).

#### RA-02 (M-2) — the V1/V2 split is gate-dependent
**Sources:** `reviewer-a-issue-007.md` M-2, claim 5, §5 item 2; report §1 lines 43–47, §7
410–422, §13.
**Ruling: ACCEPTED**, with a factual correction to the challenger's description.
**Evidence:** `detection/summary.csv`: 18 normalised models; 6 with zero diagnostics; 12 with ≥1
diagnostic; **9 with a non-zero exit status**; three (T2-C2, T6-C1, T6-C3) carry
`n_error=1`, code `reserved-keyword-name`, **exit 0**, `nonblocking_notation_only=yes`. So
V1/V2 = **6/12 under an any-diagnostic or error-severity gate**, and **9/9 under an exit-status
gate**.
**Reasoning:** the substance is right and it is the sharpest internal inconsistency in A's report:
A insists (probe07) that exit status is not a validity verdict, then counts three exit-0 models as
"invalid" without stating a gate, while applying an exit-code gate to the external arm. **But R-A's
description is wrong**: the three models are not "warning-only", they are *error*-severity
non-blocking reports. That distinction matters here, because it is precisely A's own finding that
error severity can coexist with exit 0 — so the correct statement is "gate = any diagnostic vs gate
= non-zero exit", not "warning vs error". I also note that "V1 = 9" is only meaningful if "valid"
means "the tool exits 0", which A elsewhere argues is not a validity verdict; the honest fix is to
report both readings and say what each measures.
**Residual uncertainty:** none about the counts; which gate *should* be used is a definitional
choice that belongs in the report, not in adjudication.
**Correction:** state the gate in §1, §7 and §13; report V1/V2 as 6/12 (any diagnostic) and 9/9
(exit status); correct "0/18 → 6/18 → 12/18" in §13 to name what each step measures (A-10).

#### RA-03 (M-3) — R1's re-layering does not establish that R1 is an error
**Sources:** `reviewer-a-issue-007.md` M-3 and §4.2; `B-reviews-A.md` O8; A's response O8;
`FROZEN-SUBSET.md` line 66–67; `subset.json`.
**Ruling: ACCEPTED.**
**Evidence:** `CODEBOOK.md` R1 body ("no named constraint decides feature chains over multi-valued
usages"); `errors.csv` T4-C1-E02 ("adjacent, not decisive"); the operational criterion quoted in
`FROZEN-SUBSET.md`; my reading of KerML §8.3.4.11.2 and `validateFeatureEndMultiplicity` (the
constraint constrains an end feature's own multiplicity, not the multiplicity of a usage traversed
by a chain).
**Reasoning:** A conceded the layer and stated a criterion, but the criterion is authored and, as
worded, conflates a feature with its instances: `controller.fleet.battery.power` resolves to one
feature (`power`) whose featuring instances number ten through `fleet : Agv[10]`. The frozen subset
then tells B that R1 is "not disputed as defects", which propagates the unestablished status into
B's external arm and into its denominator. The narrow claim that survives — the tool reported
nothing on both connector records — is true and is what the report should say.
**Residual uncertainty:** whether such a connector end is ill-formed under KerML's connector-end
rules (X-03).
**Correction:** mark R1 contested as to defect status, correct the criterion wording, and mark it as
contested-as-defect in `subset.json` (A-11).

#### RA-04 (M-4) — codebook v1.3 is internally inconsistent
**Sources:** `reviewer-a-issue-007.md` M-4 and §4.3.
**Ruling: ACCEPTED.**
**Evidence:** `CODEBOOK.md` line 34 (S2 table: "Required semantic binding absent where the
notation's clause is optional") versus lines 78–87 (S2 body: heading "**Mandatory clause
omitted** … a clause the notation requires is absent"); line 39 (R1 layer
`structural/architectural`) versus C05/C06 and §11.3 (`type/typing`); line 33 (S1 cites
`checkSatisfyRequirementUsageBindingConnector` and §8.3.18.9) versus C08/C09.
**Reasoning:** the class table and the class bodies are the parts a new coder uses; §11 records the
corrections in prose without updating them, so v1.3 would reproduce the pre-correction labels. The
second coder's S2 label is the demonstration: handed v1.0, it coded S2 as syntax/blocking, exactly
as the stale body still instructs. The codebook is issue #7's stated reusable deliverable, so this
is not cosmetic.
**Residual uncertainty:** re-running `agreement.py` against a corrected codebook cannot recover an
independent agreement statistic (the exemplars remain); it would only show internal consistency.
**Correction:** update the table and bodies with dated "superseded" markers, re-hash, and state that
agreement cannot be re-established without a held-out set (A-12).

#### RA-05 (M-5) — the second coder was given an answer key **and** an instruction sheet asserting the class criteria, including a false rule
**Sources:** `reviewer-a-issue-007.md` M-5 and §4.4; `B-reviews-A.md` O5/O6; A's §16.5.
**Ruling: ACCEPTED**, and the review **understates** its own point.
**Evidence:** `coding/second-coder/INSTRUCTIONS.md` line 61–64: *"SysML v2 facts you may rely on:
the textual notation requires `satisfy <requirement> by <feature>`; a feature chain through a
multi-valued usage is not a single feature; `Real`, `Integer`, `Boolean`, `String` are
standard-library scalar types that must be imported or qualified; a definition is a type, not an
occurrence."* The first is false (the `by` clause is optional in §8.2.2.21.2 — A's own v1.1); the
second is A's contested R1 criterion; the third and fourth are the N2 and T1 criteria. The
instruction sheet also tells the coder to record disagreements in `notes` and apply the rule anyway
(rule 4).
**Reasoning:** this is worse than an answer key for the *excerpts*: the four class decision rules
were supplied as facts, so class agreement measures instruction-following for those classes. It also
undercuts the "version skew, not disagreement" explanation of the S2 pair (B2A-07): the coder had
the false rule from two channels. A's §16.5 names neither the instruction sheet nor the fact that
the R1 criterion was supplied — a point that bears directly on RA-03.
**Residual uncertainty:** what survives is still genuine (three clean calls; the independent
noticing of three reserved-keyword instances; verbatim excerpt verification) but is not a
reliability statistic.
**Correction:** disclose the instruction channel in §6.1/§16.5, drop the W1 "dissent" claim (m-2),
and name the reserved-keyword notices as the surviving independence (A-13).

#### RA-06 (M-6) — the report's summary sections were not updated after A's own corrections
**Sources:** `reviewer-a-issue-007.md` M-6, §5 item 7; claims 1, 2, 3, 7.
**Ruling: ACCEPTED.**
**Evidence:** report line 8 (banner: "the frozen 14-record population survives"); §1 table lines
39–50 (14 records, 21 combined, S1 9, 9/14); §2 line 98 ("`coding/errors.csv`, frozen and hashed
before detection"); §2 line 103 ("All 18 raw outputs fail as SysML *because they are markdown*");
§5.4 line 291 ("7 further defects"); §16.8 (asserts the frozen 14 "unchanged"); README line 33
(CODEBOOK v1.3 = `fc476b1c…`, actual `106e620d…`) and line 23 ("N1 … (5)").
**Reasoning:** Amendment A1 legitimately preserves superseded text, but it does not license a
reader-facing summary that states superseded values without a marker; the first screen tells a
reader the opposite of §17. This is a presentation defect with an evidentiary consequence —
a downstream citation takes the headline, not the addendum.
**Residual uncertainty:** none.
**Correction:** add a "current numbers" table and "superseded by §17" markers at every listed
location, and fix the README hashes (A-1, A-14).

#### RA-07 (P-1) — artefact instability during review, including a response edited after declaring itself frozen
**Sources:** `reviewer-a-issue-007.md` P-1 and §6; `B-reviews-A.md` boundary note; A's response §4.
**Ruling: ACCEPTED** as a process finding.
**Evidence:** `CROSS-REVIEW-HASH.txt` (read at pin) records
`965924fe… A-response-to-B-review.md (frozen 2026-11-13T14:29Z)`, but that file's final paragraph
describes C12–C13, which are dated **14:31Z** and are registered in `errors-corrections.csv`; the
file also declares written "14:23Z, read at 14:23Z". So the bytes labelled "frozen 14:29Z" contain
material that post-dates 14:29Z. R-A additionally records observed hash movement
(`c0528b36…`→`965924fe…`; report `3f0a8cfe…`→`f507ed49…`→`edf02fc6…`; codebook
`fc476b1c…`→`106e620d…`; combined `21a75728…` (20 rows)→`56f4467a…` (19 rows)).
**Reasoning:** the current ledger is internally consistent (every recorded hash matches the file at
my pin), so no evidence was lost and no ruling depends on a phantom version. But a file declared
frozen was edited, and the ledger then labelled the post-edit bytes with the earlier freeze time —
which defeats the purpose of a hash ledger. A's own response §4 admits a pipeline re-run overwrote
an addendum, which is the same failure mode.
**Residual uncertainty:** I cannot recover the intermediate bytes, so I cannot say what changed
beyond what A describes; my rulings cite only the pinned final bytes.
**Correction:** publish an append-only ledger with a row per write; corrections go to a new dated
file, never to a "frozen" one (Lead + A, A-15).

#### RA-08 (m-1) — the "inspection missed a third" rate and the 15/19 combined detection rate are selection-biased
**Sources:** `reviewer-a-issue-007.md` m-1, §3.2; `subset.json` `excluded`; report §5.4/§17.1.
**Ruling: ACCEPTED.**
**Evidence:** the six live post-inspection records were discovered *by the validator* and then
verified against the specification (report §5.4; codebook §10.3); A's own subset excludes them as
"non-independent for a detection measurement".
**Reasoning:** the factual finding (inspection missed six real notation/typing defects) is solid and
is the pilot's most valuable result; the *rate* "7 of 21" is not a miss-rate for inspection because
the denominator includes the records the tool surfaced. Likewise 15/19 = 79% is descriptive: all six
tool-surfaced records are detected by construction, so it cannot be read as recall.
**Residual uncertainty:** a held-out inspection would give a real miss-rate; not run.
**Correction:** restate as counts ("inspection coded 14; the tool surfaced 6 further real
defects"), label 15/19 descriptive, and fix "7 of 21" → 6 of 20/19 (A-16).

#### RA-09 (m-2) — the W1 "convention disagreement" is not a disagreement
**Sources:** `reviewer-a-issue-007.md` m-2 and §4.4; `agreement.md` lines 59–63; report §6 line 366,
§16.5.
**Ruling: ACCEPTED.**
**Evidence:** `agreement.md` §"W1 convention (not a disagreement about the models)": coder A codes
W1 over the 18 raw outputs; coder B coded W1 for 12/12 including bare fences; both treat a bare
fence as W1. The codebook's include clause names a fenced block as sufficient.
**Reasoning:** the two coders differ on *where W1 is recorded* (raw artefact vs model record) and
whether it enters `n_errors`, not on whether a bare fence is a wrapper defect. Calling it an
unresolved disagreement overstates a recording-scope choice; the residual genuine ambiguity (does
the prose-only reading change the count, 18 vs 7) is a different question.
**Residual uncertainty:** the codebook should still decide the recording convention; that is a
codebook task, not a disagreement.
**Correction:** drop "dissent on the W1 convention" from §16.5 and "real and unresolved" from §6
(A-17).

#### RA-10 (m-3) — a `T6-C2` occurrence is omitted
**Sources:** `reviewer-a-issue-007.md` m-3.
**Ruling: ACCEPTED.**
**Evidence:** `detection/diagnostics.csv` T6-C2: `unresolved` at line 40 (once) and line 42
(twice); `errors.csv` T6-C2-E01 records line 40 only; `occurrence_detection.csv` covers four
records and not T6-C2.
**Reasoning:** the same name `heating` is unresolved three times; the record's span is one
occurrence and the occurrence table omits the model. Record-level detection is unaffected.
**Residual uncertainty:** occurrence counting is a coding judgement, but here the mechanism is the
same name at three sites.
**Correction:** widen the record's occurrence list and add T6-C2 to the occurrence table (A-8).

#### RA-11 (m-4) — the presence κ is hard-coded `None` with a false comment
**Sources:** `reviewer-a-issue-007.md` m-4.
**Ruling: ACCEPTED.**
**Evidence:** `coding/agreement.py` lines 141–142: `"kappa": None,  # constant marginals (every
model has an error on both sides)`. The marginals are 9 error / 3 clean on each side, so the
comment is false.
**Reasoning:** presence κ is computable (pₒ = 1, pₑ = 0.625, κ = 1) and its suppression is
unexplained; the false comment is the kind of small error that erodes trust in the reported
statistics. No number moves.
**Residual uncertainty:** presence agreement is anyway uninformative here (every model is paired).
**Correction:** compute it or state a correct reason, and fix the comment (A-18).

#### RA-12 (m-5) — denominator labels collide and a models.csv column misdescribes its content
**Sources:** `reviewer-a-issue-007.md` m-5 and §4.2.
**Ruling: ACCEPTED.**
**Evidence:** report line 655/710 ("9/13 = 69%" = 14 − I1) and line 787 ("9/13 = 69%" = 14 − C12)
are two different 13s; README line 23 calls the first "the 13 uncontested records" while the frozen
population is 13 only after C12; `apply_corrections.py` line 105 overwrites
`n_errors_post_inspection` with the combined count.
**Reasoning:** both 13s happen to give 9/13 because both removed records were undetected, which
hides the collision; a reader cannot tell which denominator is meant. A column named
"post_inspection" holding a combined count will mislead any recomputation.
**Residual uncertainty:** none.
**Correction:** unique labels (9/13[C12]; 9/13[−I1]) and rename the column (A-19).

#### RA-13 (m-6) — "81 `syntax` diagnostics" and "two-pass inspection"
**Sources:** `reviewer-a-issue-007.md` m-6 and §2.3.
**Ruling: ACCEPTED.**
**Evidence:** `detection/diagnostics.csv` raw scope: 72 `syntax` + 9 `reserved-keyword-name` = 81
(recounted); report lines 44 and 251 say "81 `syntax` diagnostics". No artefact records two
distinct inspection passes (only `inspect.py` indicators, `_audit-view.txt`, `labels.py`).
**Reasoning:** the label is wrong by 9 diagnostics and becomes self-contradictory with the report's
own insistence that the reserved-keyword class is separate from parse failure. The "two-pass"
formulation asserts a process the artefacts do not evidence; what is evidenced is an open pass,
mechanical indicators and a coding pass.
**Residual uncertainty:** A may have made two passes; the artefacts cannot show it.
**Correction:** "81 raw diagnostics (72 syntax + 9 reserved-keyword-name)"; describe the inspection
as recorded (A-20).

#### RA-14 (Adj-1) — the subset's "7 controls" include three models A says are not controls, so B's specificity could be contaminated
**Sources:** `reviewer-a-issue-007.md` Adj-1.
**Ruling: REJECTED** (as a challenge to B's measurement); the underlying labelling is already
correct.
**Evidence:** `FROZEN-SUBSET.md` lines 49–57 label the three `frozen-clean-only` and mark each "NOT A
CONTROL"; lines 80–83 instruct that a diagnostic on them is not a false positive and that they must
not be scored; `empirical/REPORT.md` §5 and addendum A10.4 score only the four clean-tier controls
and report the three descriptively.
**Reasoning:** the harm R-A hypothesised did not occur, and the frozen file forecloses it twice. The
count "7 controls" in the summary line is loose, but the tiers are explicit and the consumer
followed them. R-A's second half — that R1 is contested only as to layer — is right and is
adjudicated under RA-03; it does not make Adj-1 a defect in B's arm.
**Residual uncertainty:** none.
**Correction:** none for B. (The Lead may relabel the subset's summary line "4 controls + 3
descriptive models" for clarity — A-21, cosmetic.)

### 3.4 Reviewer B (independent review of #8)

#### RB-01 — the external pre-registration's "frozen" hash is post-AM1; the pre-run hash was overwritten
**Sources:** `reviewer-b-issue-008.md` RB-01, §3.3–§3.4; report A10 line 761; `empirical/REPORT.md`
lines 6–7; `run-log.md` §2.
**Ruling: ACCEPTED.**
**Evidence:** `PRE-REGISTRATION.md` (sha256 `9458406e…`) contains AM1 at lines 227–251, which states
"the first execution of `run_external.py` (`raw/run1/`) completed, and its output revealed three
defects"; file mtimes: `PRE-REGISTRATION.md` birth 14:35:13Z, mtime **14:36:04Z**;
`PRE-REGISTRATION.sha256` mtime **14:36:04Z**; `raw/run1` 14:35:38–41Z; `raw/run2` 14:36:04Z. So
`9458406e…` was computed at 14:36:04Z, **after** the first run, and the `.sha256` file's freeze-time
value was overwritten.
**Reasoning:** the sentence "frozen at `9458406e…` before the first run" cannot be true of that hash,
and `run-log.md` §2's claim that the two recorded versions differ "only in a header timestamp" is
contradicted by the AM1 amendment sitting inside the hashed file. The amendment itself is
conservative (it moves items from "not detected" to "not applicable" and fixes a serialisation) and
run1→run2 changed no M1 outcome — verified independently by R-B and consistent with
`results.csv` — but the hash chain offered as proof of pre-registration does not establish it.
**Residual uncertainty:** the pre-AM1 bytes are lost; I cannot verify the claim that they differed
only by a header timestamp.
**Correction:** state that the pre-run hash is unrecoverable and that pre-registration rests on
content + AM1's disclosure + the run1/run2 identity; correct `run-log.md` §2; publish AM1 in a
separate file in future runs (B-12).

#### RB-02 — F4-01 (`[4..2]`) is used both as a detection and as evidence of over-reach
**Sources:** `reviewer-b-issue-008.md` RB-02, C15; report §2 P5 (line 67), §3.5 (161–168), §3.3
(line 120–122).
**Ruling: ACCEPTED** (the inconsistency is real and must be resolved in the text). **The count does
not move: I rule the model text defective**, so F4-01 remains a detection and P5's wording changes.
**Evidence:** F4-01's diagnostic is `error[multiplicity-range]: multiplicity lower bound exceeds
upper bound on wheels`; P5 says "no constraint in the 623-row catalogue forbids it — §7.6.3 requires
bounds to be naturals and says nothing about their order, and **an empty range is not obviously
ill-formed**". Retrieved text (KerML 1.0 §8.3.4.11.2, `/tmp/sysml/kerml-1.0.txt` lines 14257–14260):
*"A MultiplicityRange is a Multiplicity whose value is defined to be the (inclusive) range of
natural numbers given by the result of a lowerBound Expression and the result of an upperBound
Expression"*; and §8.4.4.12.2 (line 17267): *"A MultiplicityRange … constrains the cardinality of
its typeWithMultiplicity to be within this range … the range of values that are greater than or
equal to … expr_1 and less than or equal to … expr_2"*. For 4 > 2 that range is empty and no
cardinality can satisfy it. The two constraints on bounds
(`validateMultiplicityRangeBoundResultTypes`, line 14372; `validateMultiplicityRangeBounds`, line
14384) constrain typing/non-negativity and owned-member order only — so no *named* constraint
forbids it.
**Reasoning:** the two readings are mutually exclusive as B wrote them: either `[4..2]` is a defect
(then counting the error as a detection is right and "not obviously ill-formed" is wrong), or it is
not a defect (then it is a spurious error and "no case of a spurious error on a mutant" is false,
F4 = 2/4, overall 22/32). Adjudicating the underlying question: the specification's own definition
makes the declaration unsatisfiable, which is a defect of the model whatever the catalogue names, so
the detection stands at **23/32** and the offending sentence is the one to remove. The remaining
valid part of P5 — the instrument enforces a condition no *catalogue constraint* names — is true
and is worth keeping; the dimensional-consistency example carries it better.
**Residual uncertainty:** whether a tool *must* report an empty range is not specified; a
specification-faithful validator could be silent, and readers who adopt "named-constraint-only" as
the defect criterion will legitimately reach 22/32. The report must state which criterion it uses —
it does not.
**Correction:** delete "an empty range is not obviously ill-formed"; restate §3.5/P5 as "reports an
unnamed but semantically impossible condition (an empty multiplicity range), which no catalogue
constraint forbids"; state that F4-01 is counted as a detection under the semantic reading and that
the alternative reading yields 22/32; qualify "no spurious error on a mutant" as conditional on
that reading (B-13).

#### RB-03 — the expectation audit overstates its independence; the pre-freeze calibration already showed F6/F8 firing
**Sources:** `reviewer-b-issue-008.md` RB-03, C12, C40, C41, §3.6; report §4.1, §8.6, A8;
`results/calibration/PRE-FREEZE-CALIBRATION.md`; `gate-log.md` Gate 1.
**Ruling: ACCEPTED.**
**Evidence:** the calibration file (14:06–14:08Z, before the methodology freeze at 14:08:53Z)
records construct-level detections: `q1` → `incommensurable-binding` fires as **error** (F6);
`m1` (`@SafetyCase` on a `part def`) → `error[metadata-metaclass]` (F8-01); `m2` (`levl` typo in a
metadata body) → `error[metadata-owning-type-feature]` (F8-02); `t1` → `warning[bound-feature-types]`
(the "wrong severity" outcome). The report's §4.1 names only the `-explain` code list; the gate log
characterises the probes as establishing "output shape, exit codes and short-circuit behaviour".
**Reasoning:** F6's and F8's "expected detectable = yes" flags were written after the same
mechanisms were observed firing. That does not touch the counts (23/32 is computed from raw
diagnostics) but it makes the audit near-tautological for those classes, which is a stronger
statement than B's own `-explain` disclosure. The calibration file itself flags the threat; the
report and gate log do not carry it.
**Residual uncertainty:** F4-01 and F6-02 remain genuinely unpredicted, and both err towards the
tool being stricter — the direction a spec-anchored forecast should err.
**Correction:** name the behavioural probes as a source of expectation knowledge in report §4.1,
methodology §12.6, gate-log Gate 1 and A8; keep the audit but label it "informed, not blind, and
weak by construction" (B-14). **This also corrects the gate log, which is the Lead's file — see
CORRECTIONS L-1.**

#### RB-04 — KG-04's over-reach classification is a contestable judgement, and its "what would settle it" pointer is mis-targeted
**Sources:** `reviewer-b-issue-008.md` RB-04, C6; `known-good-triage.md` §"The one firing";
report §3.6 and A10.3; critic C10 and p12.
**Ruling: ACCEPTED.**
**Evidence:** the line `attribute cutoff : Rational default = 0.75 * averageScore;` is verbatim from
§7.13.4 (`/tmp/sysml/sysml-2.0-language.txt` lines 5215–5216; `TestRecord` at 5182 declares
`cutoff : Integer default = …`). §7.6.5 (line 3439) provides the implicit-name rule *only* "if
neither a name or a short name are given in the declaration of a usage with an owned redefinition";
here the name is declared and no `:>>`/`redefines` is written. KerML
`validateNamespaceDistinguishibility` (line 8463) requires all memberships of a namespace to be
distinguishable, and the default `isDistinguishableFrom` (line 8154) compares names and metaclasses
— there is **no override** for feature memberships. B's promised settling clause, SysML §7.6.1, is
titled "Definition and Usage Overview" (line 2752) and does not contain the naming rules.
**Reasoning:** on the literal text, two same-named `AttributeUsage` memberships of one namespace are
not distinguishable, so the tool's warning may be *correct* — which means "over-reach" is not
established. But the specification's own example uses exactly this construct, which means either the
example is defective or the constraint is intended to admit implicit redefinition; that ambiguity is
the real state of the question. B's triage already hedges ("not evidence of a wrong verdict"); §3.6
and A10.3 state it as fact.
**Residual uncertainty:** this is the same unresolved question as the `name-conflict` class (§5.1);
no retrieval available to me settles it because the two normative texts conflict.
**Correction:** reclassify KG-04's warning as "unresolved / spec-ambiguous" rather than
over-reach; correct the pointer to §7.6.3/§7.6.5 and KerML §8.3.2.4.5; state in A10.3 that
`name-conflict` is ambiguous in both directions for a reason now identified (B-15).

#### RB-05 — the external M2/M3 accounting is arithmetically wrong and internally contradictory
**Sources:** `reviewer-b-issue-008.md` RB-05, C24; `empirical/REPORT.md` lines 46–47; report A10.1
(784–785) versus A10.5 (843).
**Ruling: ACCEPTED.**
**Evidence:** `empirical/results.csv`: M2 = 10 `not applicable`, 1 `not detected` (S2), 2
`wrong-target` (I1, T4-C3) → **3 evaluated**; M3 = 10 `not applicable`, 2 `not detected`, 1
`weaker signal` → **3 evaluated**. The headline tables say "1 evaluated, 10 not applicable"
(which sums to 11, not 13) while A10.5 says "applicable to 3 items each".
**Reasoning:** a straight column-sum error, and "applicability" is the honest form of the M2/M3 null
result, so it must be right. No detection count changes.
**Correction:** both documents to 3 evaluated / 10 n/a, with the per-item breakdown (B-16).

#### RB-06 — the external scoring does not follow the registered rule for non-satisfy-family items
**Sources:** `reviewer-b-issue-008.md` RB-06, C25; `PRE-REGISTRATION.md` §4.2; `run_external.py`
lines 222–231.
**Ruling: ACCEPTED.**
**Evidence:** §4.2 registers `not applicable` for any non-satisfy-family item in M2; the harness
returns `wrong-target` (2 items) and, in M3, `not detected` for 6 controls and 2 items; AM1 item 3
says controls must not use the item-attribution vocabulary, yet 6 of 7 controls carry
`wrong-target` in M2.
**Reasoning:** the deviation does not inflate detection (nothing becomes "detected"), but it makes
"applicable to 3 items" true only under the harness's reading, not the registered one, and it
violates the amendment's own rule for controls. Under §4.2, M2's applicable count is 1 (S2) and
M3's is 3.
**Residual uncertainty:** none.
**Correction:** re-label under §4.2 (M2 applicable = 1) or add a dated addendum justifying
`wrong-target` for non-satisfy items; relabel the controls (B-17).

#### RB-07 — the external harness's immutability claim is false
**Sources:** `reviewer-b-issue-008.md` RB-07, C21b.
**Ruling: ACCEPTED.**
**Evidence:** `run_external.py` lines 165, 191–192, 260, 292 use `mkdir(exist_ok=True)` and
`Path.write_text(...)` with no existence check; the docstring claims output is "refused if it
already exists". The synthetic harness uses `open(..., "x")` (`run_validators.py`).
**Reasoning:** a cited raw run can be silently overwritten by re-running the documented command,
which is an evidence-integrity claim the code does not implement. It did not happen (run1 is
preserved and run2 is on disk), but the claim must be fixed before anyone cites the raw files by
hash.
**Residual uncertainty:** none.
**Correction:** implement refuse-if-exists or delete the claim; log the change (B-18).

#### RB-08 — three arithmetic/label errors: "24 of 28", "5 silent", and the ladder's exclusion order
**Sources:** `reviewer-b-issue-008.md` RB-08, C13, C14, C23; A8 line 725; `analysis.md` lines 12,
23; `empirical/REPORT.md` §1 vs §6.1.
**Ruling: ACCEPTED.**
**Evidence:** recomputed from `results/diagnostics.csv`: diagnostics per mutant 1→23, 2→3, 3→1,
5→1 (28 signalling mutants); error-bearing mutants 23, of which 20 produce exactly one error;
F5-01 carries one `warning[name-conflict]` (`M31-F5-01-feature-value-overriding.json`), so under the
frozen definition ("silent = zero diagnostics of any severity", methodology §8) it is not silent —
the split is **4 silent + 1 warning-only**. "24 of 28" is wrong under both readings (23 by any
severity, 20 by errors among the error-bearing). The ladder's first exclusion is I1 in
`empirical/REPORT.md` §1 and the short-circuited item in §6.1.
**Reasoning:** none of the three touches a proportion in the headline, but the "5 silent" also
contradicts the same page's "any-signal 28/32", and a reader comparing the two would see the
inconsistency. The ladder order matters for a reader reconstructing 9/11.
**Correction:** correct to 23 of 28 (any severity) / 20 of 23 (errors); replace "5 silent" with
"4 silent + F5-01 incidental at warning severity"; use one exclusion order and state it (B-19).

#### RB-09 — B's stated UTC times are unreliable and several are forward-dated
**Sources:** `reviewer-b-issue-008.md` RB-09, C36.
**Ruling: ACCEPTED.**
**Evidence:** `raw/run2-modes/**` mtimes 14:24:50–14:26:00Z and `run-log-run2-modes.md` header
"Written … 14:24:51Z", versus report A2's "2026-11-13T14:31–14:36Z"; addenda A2–A9 dated 14:40Z in
a file whose last write is 14:38:04Z; A10 dated 14:56Z in the same file; the Gate-2 response dated
14:40Z; and in the external arm, AM1 is dated 14:39Z in a file whose mtime is 14:36:04Z.
**Reasoning:** ordering claims that the protocol cares about (methodology before mutants; expectations
before the run) are independently established from the filesystem and are not affected — but
self-reported times that post-date the file's own last write cannot be evidence of anything.
**Residual uncertainty:** the cause is a clock/authoring convention I cannot reconstruct; the
filesystem order is usable and I used it.
**Correction:** stop quoting self-reported times for ordering; use filesystem order or an append-only
timestamped log (B-20).

#### RB-10 — `spec_status` is post-hoc, not a frozen field
**Sources:** `reviewer-b-issue-008.md` RB-10, C16.
**Ruling: ACCEPTED** (minor).
**Evidence:** `harness/analysis.py` holds the six-bucket `spec_status` as a hard-coded dict; it is
not a column of `MANIFEST.csv`.
**Reasoning:** the buckets are transparent and checkable, and the underlying text is frozen, but
"fixed before the run, not chosen to fit the outcome" overstates the provenance of the *bucket
assignment*. It is a single-coder reading of frozen text, which is what it should say.
**Correction:** add the bucket assignment to a dated file or restate as post-hoc-but-mechanical
(B-21).

#### RB-11 — the known-good arm is not independent of the mutant arm
**Sources:** `reviewer-b-issue-008.md` RB-11, C37, §4 finding 1.
**Ruling: ACCEPTED** (minor).
**Evidence:** the 10 known-good models are the mutant parents; 9 of 32 mutants edit one 23-line
model (`KG-01`); the corpus was iterated to tool-silence before the freeze (two pre-freeze firings,
both tool-correct).
**Reasoning:** the 0/10 reproduces and is not affected, but base concentration means the per-class
Wilson intervals do not represent the cluster structure, and "independent of the mutant generator"
needs the qualification. The known-good arm cannot estimate a false-positive rate in any case
(10 small models).
**Correction:** state the base concentration and the iterate-to-silence history in §3.1/§8 (B-22).

#### RB-12 — the README contradicts the artefacts and there is no pointer from the summaries to the addenda
**Sources:** `reviewer-b-issue-008.md` RB-12, C34.
**Ruling: ACCEPTED.**
**Evidence:** `research/issue-008/README.md` lines 97–98: "**No empirical challenge set** … nothing
here was informed by Researcher A's work", in a file that lists `empirical/**` at lines 53–59 and
was last written after A10.
**Reasoning:** this is the most concrete internal contradiction in either repository index, and it
is exactly the sentence a reader would use to decide whether the pilot met its independence
requirements. Combined with the missing forward pointer, it means the index misdescribes the work.
**Correction:** fix the README section and add a top-of-report pointer to A2/A3 for the F7/P3/§11.1
claims (B-23).

### 3.5 Semantic-ceiling critic

#### CC-01 (C01) — the undetected records are said to be "outside the instrument's stated scope" because it "executes neither actions nor state machines"
**Sources:** `CLAIMS.csv` C01; report #7 §5.3 (lines 281–287).
**Ruling: ACCEPTED.**
**Evidence:** `evidence/spec-tooling.md` line 138 attributes the sentence to "the pilot" (the OMG
Pilot Implementation), citing the OpenSysML differential as a *third party*; line 208 says the same
about "the pilot", with OpenSysML self-assessing "since no external referee executes behavior". My
runs 2.4/1 and 2.4/11 execute an action and analyse a verification case on the pinned binary.
**Reasoning:** A transfers a documented limitation of a *different* program to the instrument it
measured. The instrument executes actions and state machines; what it fails to do is return a
*verdict* for these records. This is the single most consequential attribution error in the run
because it is the mechanism by which a tool limitation becomes a claim about automated validation.
**Residual uncertainty:** the pinned binary's *coverage* of execution semantics is not characterised
by either pilot; "executes" is not "executes correctly".
**Correction:** replace the sentence with "the default `-validate` invocation reports nothing on
these records, and no invocation I ran returns a defect verdict for them" (A-22).

#### CC-02 (C02) — structural/semantic defects are "invisible to the instrument"
**Sources:** `CLAIMS.csv` C02; report #7 §13.2 (lines 551–555).
**Ruling: ACCEPTED.**
**Evidence:** runs 2.4/2 (contradictory assertions → `violated`), 2.4/4 (missing flow → execution
failure when read), 2.4/5 (violated requirement) — none available to A's default-path measurement.
**Reasoning:** supported for the two specific records under the default path only; "invisible to the
instrument" is invocation-unspecific and false for other semantic shapes. The narrow claim — nothing
in the surfaces tested decides a documentation/value contradiction — survives and is the one worth
keeping.
**Correction:** "no diagnostic on these records under the invocation run; and no surface tested
decides a documentation/value contradiction" (A-23).

#### CC-03 (C03) — "the instrument cannot check state-machine reachability"
**Sources:** `CLAIMS.csv` C03; report #7 §14 (lines 570–573).
**Ruling: ACCEPTED** (on "cannot").
**Evidence:** my run 2.4/6: `-state Mission -advance 100` prints `outcome: finalState running;
visits idle, running` (no `done`), exit 0, no violation; the critic's p01c shows non-termination
reported as a failing linearization under `-schedule explore`.
**Reasoning:** unreachability is not reported as a defect verdict, but it is observable in the
visited-state set and non-termination has a verdict. "Cannot" conflates "no verdict" with
"unobservable"; the hedged framing ("my detection table says") is careful but the word is not.
**Residual uncertainty:** whether reachability is expressible as a property at all is "not
established" — no flag states an *eventual* property in the material read.
**Correction:** "no mode returns a defect verdict; the condition is observable in a trace but not
checked" (A-24).

#### CC-04 (C04) — the instrument is silent on 5 of 14 frozen records
**Sources:** `CLAIMS.csv` C04; report #7 §5.1.
**Ruling: ACCEPTED** as an accurate default-path measurement, **with a superseded label**.
**Evidence:** reproduced (A's detection table is byte-identical to my recomputation); C12 withdraws
one of the five, making it 4 of 13.
**Reasoning:** the claim was true when written and is true of the frozen file; it is no longer the
population A's own corrections describe. The correction is a label, not a number.
**Correction:** keep 5/14 and add "4 of the 13 after C12" plus the composition (A-9, merged with
RA-01).

#### CC-05 (C07) — "a clean validation is no evidence at all about whether the model's structure means what it claims"
**Sources:** `CLAIMS.csv` C07; report #8 §1 (lines 40–43); report A2.
**Ruling: ACCEPTED.**
**Evidence:** run 2.4/5 (same model clean under `-validate`, `violated` under `-satisfy`).
**Reasoning:** the substance is right for the default path; the absolute phrasing is false of the
instrument, as B's own A2 concedes and corrects. Because §1 is the headline position and A2 is 450
lines below with no pointer, the uncorrected form is what a reader takes away.
**Correction:** §1 must carry the A2 wording or a pointer (B-1).

#### CC-06 (C08) — the verdict path decides "exactly those defects the generator encoded as a checkable constraint, and nothing more"
**Sources:** `CLAIMS.csv` C08; report A2 lines 497–505.
**Ruling: ACCEPTED** (the "nothing more" clause only).
**Evidence:** run 2.4/4: a missing data flow is decided by `-action` as an execution failure when
the sink reads the input — no constraint is encoded; run 2.4/1: an invariant is decided by
`-check-property` under the SMT engine; run 2.4/11: a verification postcondition is evaluated per
assertion.
**Reasoning:** I do not accept the critic's p07b example as a counterexample — an `assert
constraint` **is** a checkable constraint, so contradictory assertions with bound values fall inside
B's description. But execution failures and property checks do not, so "and nothing more" is
overstated. The first half of A2 (the default path is blind; the verdict path decides what the model
asserts) is correct and is the pilot's most useful result.
**Correction:** replace "and nothing more" with "…and, separately, execution failures and property
checks where the model's own bindings force the issue"; add the p02d/p08b examples (B-24).

#### CC-07 (C10) — `validateFeatureValueOverriding` is "not enforced"
**Sources:** `CLAIMS.csv` C10; report #8 §2 P4, §3.4; critic p12.
**Ruling: ACCEPTED** (site-dependence; P4's example needs qualification).
**Evidence:** run 2.4/7: `error[feature-value-overriding]` fires on `attribute :>> x = 2.0;` when the
supertype's value is fixed with `=`; run 2.4/10: B's F5-01 produces only the base's
`warning[name-conflict]`, and its "redefinition" is not written with `:>>`.
**Reasoning:** the diagnostic exists and fires where the redefinition is explicit, so "not enforced"
is a statement about one site. Two rival readings are live and neither is established: (i)
enforcement is site-dependent (same shape as F2's resolution gap), or (ii) B's mutant does not
violate the constraint because the same-named declaration is not a redefinition — which is the same
unresolved question as `name-conflict` (§5.1). R-B held P4 at "supported for the first example";
that is too generous once p12 is in evidence.
**Residual uncertainty:** settles with §5.1; until then P4's satisfy example (A2B-04) and the
`end-feature-multiplicity` warning-only case are its stronger evidence.
**Correction:** restate P4 as "at least one named SHOULD constraint was missed at the site tested,
and enforcement of `validateFeatureValueOverriding` is site-dependent"; record the rival reading that
F5-01 may not instantiate the constraint (B-25).

#### CC-08 (C11) — "the ceiling of automated SysML v2 validation here is typing plus per-constraint well-formedness"
**Sources:** `CLAIMS.csv` C11; report #8 §4.2 (lines 196–198).
**Ruling: ACCEPTED.**
**Evidence:** runs 2.4/1 (SMT invariant), 2.4/2 (assertion evaluation), 2.4/11 (verification
postcondition), plus `-action`/`-state` execution; B's own A2 breaks the statement and §4.2 was not
amended.
**Reasoning:** the instrument's decision surface includes execution, assertions on objects, SMT
property checks and verification-case postconditions, so "typing plus well-formedness" is a
description of one verb. The correct scope is the default `-validate` invocation, with the verdict
surface described separately and its strength labels (`observed`, `bounded`, `proved`, `witnessed`)
preserved.
**Residual uncertainty:** the reach of the verdict surface for *generated* models is near zero in
A's corpus (0/18 `require constraint`), which limits the practical significance, not the accuracy.
**Correction:** "the ceiling *of the default `-validate` path* is typing plus per-constraint
well-formedness; beyond it the instrument decides conditions the model itself asserts, at the
strength its engine reports" (B-26).

#### CC-09 (C12) — four defect classes are invisible
**Sources:** `CLAIMS.csv` C12; report #8 §11.5 (lines 367–372).
**Ruling: ACCEPTED.**
**Evidence:** A2/A3 record one detected and one undecided; run 2.4/1 and 2.4/4.
**Reasoning:** the sentence contradicts the same document's addenda for two of the four. The oracle
conclusion in the same paragraph — that scoring these conditions needs an oracle from outside the
well-formedness surface — survives, and is the part worth keeping.
**Correction:** rewrite §11.5 as "two of four are decided by no mode tested; one is decided by
`-satisfy`; one is checked and left undecided — and for all four the oracle must be authored into
the model or supplied by an expert" (B-27).

#### CC-10 (C13) — tool gap and language gap are separable only through the specification-oracle table
**Sources:** `CLAIMS.csv` C13; report #8 §8.1 (lines 279–281).
**Ruling: ACCEPTED.**
**Evidence:** the same tool with a different invocation decides the same class (`-validate` clean vs
`-satisfy` violated); the same tool with a different encoding decides or does not (`p07c` undecided
vs `p07b` violated); the same tool with a different engine contradicts itself (`check` holds vs
`smt` violated).
**Reasoning:** invocation, encoding and engine are each a separator the pilot did not enumerate, and
each is cheaper than the textual argument. R-B's later finding that the tool has a
`feature-value-overriding` diagnostic it did not fire (run 2.4/7) is a fourth instance.
**Correction:** add the third separator to §8.1 and to §9's "what would change the answer" (B-28).

#### CC-11 (C15) — "for four out of four structural defects tested it means nothing at all"
**Sources:** `CLAIMS.csv` C15; report #8 §11.1 (lines 347–353).
**Ruling: ACCEPTED** for a wording correction (the claim is true of the default path, false of the
instrument).
**Evidence:** as CC-05/CC-08.
**Reasoning:** this is the report's own "calibrated sentence" and the most quotable one; as printed
it lacks the qualifier that makes it true. "Means nothing at all" is also stronger than the evidence
— the F7 mutants *are* observable in traces (unreachable state) or produce empty results (missing
flow), which is weak signal, not nothing.
**Correction:** insert "default `-validate`" before "pass", and "returns no verdict for three of the
four and detects the fourth only where the requirement encodes a constraint" (B-29).

#### CC-12 (C20) — the original P3 ("invisible … Established") is retained visibly
**Sources:** `CLAIMS.csv` C20; protocol Amendment A1.
**Ruling: ACCEPTED**, as a presentation requirement.
**Evidence:** report §2 P3 line 65 unqualified; A2 restates it at lines 507–510.
**Reasoning:** Amendment A1 requires the original claim to remain visible and forbids rewriting it,
which is right; the consequence is that the document contains both forms and the headline position
holds the retracted one. The fix is a pointer, not a deletion.
**Correction:** add "corrected by A2" in the P3 cell (B-30).

#### CC-13 — the eight claims the critic judged not overstated (C05, C06, C09, C14, C16, C17, C18, C19)
**Sources:** `CLAIMS.csv` C05, C06, C09, C14, C16, C17, C18, C19.
**Ruling: REJECTED** as challenges — there is no overstatement to correct, and I verified the ones
that depend on the binary.
**Evidence:** C06 reproduced (run 2.4/9-adjacent: `reserved-keyword-name` at error severity, exit 0
on T6-C1 per `summary.csv`); C14 reproduced (units: warning at the default gate, error under object
check); C17 reproduced (run 2.4/8, `holds … vacuous`); C09/C05/C16/C18 are appropriately cautious by
construction.
**Reasoning:** recording these as rejected matters as much as recording the accepted ones: the
adjudication should not manufacture corrections where the pilot already scoped its claim. One
substantive addition — the critic's C19 observation that the encoding dependence **generalises** (to
contradictory assertions and missing flow) is a *strengthening* for B's A2/A10.5, not a correction;
I recommend the Lead carry it into the synthesis (see §7.4) but it is not a defect in B's text.
**Correction:** none required. Optional: add the p07b/p02d instances to A2 as further examples
(B-31, editorial).

### 3.6 Critic status propositions S1–S10

These are ruled as status assignments; **ACCEPTED** means the assignment stands as stated. All ten
are upheld, six of them on evidence I reproduced myself.

| id | proposition | ruling | my evidence |
|---|---|---|---|
| CS-01 (S1) | the instrument executes actions and state machines | **ACCEPTED** | run 2.4/1 (`-action Seq` executes and reports a step-level violation), 2.4/6 (`-state Mission -advance`), 2.4/11 (`-analysis over`) |
| CS-02 (S2) | requirement satisfaction is decided when the requirement carries a `require constraint` | **ACCEPTED** | runs 2.4/5 (`holds` exit 0 vs `fails … Required condition evaluated to false` exit 1) |
| CS-03 (S3) | a prose-only requirement is reported as holding vacuously | **ACCEPTED** | run 2.4/8 on A's S2 model: `holds … (vacuous: requirement … states no required constraint)`, exit 0 |
| CS-04 (S4) | contradictory assertions are decided when bound and undecided when unbound | **ACCEPTED** | runs 2.4/2 and 2.4/3 on models differing only in a feature value |
| CS-05 (S5) | a property-checkable invariant is decidable — and the bounded engine returns a false `holds` | **ACCEPTED** | run 2.4/1: `check` → `holds (bounded)`, exit 0; `smt` → `violated (witnessed)`, exit 1; `all` names the conflict |
| CS-06 (S6) | unreachability is never a verdict, only observable | **ACCEPTED** | run 2.4/6: `outcome: finalState running; visits idle, running`, exit 0 |
| CS-07 (S7) | "the semantic ceiling" is not a property of the language, and the premise is misattributed | **ACCEPTED** | `evidence/spec-tooling.md` line 138/208 versus runs 2.4/1 and 2.4/11 (CC-01) |
| CS-08 (S8) | the ceiling is not a property of "SysML v2 tooling" | **ACCEPTED** | one instrument, one version; no second measurement exists |
| CS-09 (S9) | what can be established is a function of encoding × invocation × engine × reading | **ACCEPTED** for this instrument, on eleven demonstrations | runs 2.4/1–2.4/11; the encoding pairs (2.4/2 vs 2.4/3; 2.4/5), the engine pair (2.4/1), the invocation pairs (2.4/5 vs default) |
| CS-10 (S10) | the defect ground truth is authored; detectability is measured, not authored | **ACCEPTED** | `MANIFEST.csv` (hashed pre-run) vs `results.csv` (measured); A's `errors.csv` vs `detection/table.md` |

**One qualification on CS-09.** The proposition is demonstrated but its *practical* weight depends
on a construct census: all eleven demonstrations encode the condition in the model, and A's corpus
contains **0/18** models with a `require`/`assert constraint` (verified in both B's census and A's).
So "the ceiling is where the model stops asserting" is right, and the observed generation surface
barely asserts anything. B's A10.5 says this; the critic's §7 says it; it should be the first
sentence of any synthesis.

### 3.7 Cross-cutting rulings raised by this adjudication

#### X-01 — B's external arm has the same composition problem as A's frozen population, and nobody noticed
**Sources:** none — this is my consolidation of RA-01 applied to `empirical/REPORT.md` §3 and
report A10.1.
**Ruling: ACCEPTED** as a correction required to B's external headline.
**Evidence:** the four misses are S2 (a `check` constraint with a MAY obligation), R1 ×2 (no named
constraint; defect status contested, RA-03) and I1 (contested, B2A-10); the detected nine are
S1 ×3, N1 ×4, N2 ×1, T1 ×1. So 9/13 = 9/9 established + 0/4 discretionary/contested, with one of
the four also unmeasurable by short-circuit.
**Reasoning:** B applied the layer reading ("every miss sits at the constraint/semantic/structural
layer") but not the obligation reading, which is available from the same table. Both readings fit
the 9/13; the obligation reading is the more informative one because it is not confounded by class
composition, and it is the same correction R-A made to A (RA-01). The aggregate 0.69 vs 0.72
agreement is a composition artefact — B says so — but the *composition* being an obligation split is
a stronger statement than "different class distributions".
**Residual uncertainty:** with n = 4 misses, "obligation predicts detection" is a description of
this set, not an established predictor (X-02).
**Correction:** add the obligation-split line to `empirical/REPORT.md` §1/§3 and report A10.1, and
state that the aggregate 9/13 is not a detection-gap measure (B-32).

#### X-02 — layer versus obligation as the predictor of detection: UNRESOLVED
See §5.2.

#### X-03 — R1's defect status: UNRESOLVED
See §5.3.

#### X-04 — whether the bounded engine's false `holds` is systematic: UNRESOLVED
See §5.4.

---

## 4. Rejected challenges

#### 4.1 B2A-04 — "line 42 is not visibly defective as written"
Rejected in §3.2/B2A-04: a definition is not a feature, and the tool's silence at a succession source
is an independently established gap, so silence cannot be read as legality. B's sub-claim rests on
the very instrument property A2B-05 establishes.

#### 4.2 RA-14 — the subset's controls contaminate B's specificity
Rejected in §3.3/RA-14: the frozen file labels the three models "NOT A CONTROL" and instructs that
diagnostics on them are not false positives; B scored only the four clean-tier controls and reported
the three descriptively. The hypothesised harm is foreclosed by the artefact. (The label "7
controls" in the summary line is loose; a cosmetic relabel is offered, not required.)

#### 4.3 CC-13 — the eight claims the critic found not overstated
Rejected in §3.5/CC-13: there is nothing to correct. Recorded so that the adjudication does not
manufacture work; the two that depend on the binary (C06, C14) were reproduced.

---

## 5. Unresolved

Unresolved means: the artefact set cannot decide the question, no legitimate retrieval or run
available to me would, and both readings stay visible. Each names what would settle it and who could
obtain it.

### 5.1 A2B-12 — Is a same-named declaration in a specializing definition (the `name-conflict` diagnostic) a defect? And does the corresponding implicit redefinition violate `validateFeatureValueOverriding`?

**The disagreement.** A: `name-conflict` appears in 10 of 24 independently generated artefacts and
is therefore a missing class in B's fault model (A's O13). B: the same diagnostic is the only false
positive in its known-good arm, firing on a specification-verbatim example (§7.13.4), so it is
unusable as a defect signal (B's O13/A7). R-B: the over-reach judgement is plausible but not
established, and B's settling pointer is mis-targeted (RB-04). The critic: the tool has a
`feature-value-overriding` diagnostic that fires elsewhere, so F5-01's silence may be
site-dependence *or* a mutant that does not violate the constraint (C10).
**What I established that none of them did.** The two observations are **one mechanism**, not two
phenomena: all **119 of 119** external `name-conflict` diagnostics have the form *"Duplicate of
inherited member name 'X' from Y"* (recounted), and so does B's KG-04 warning. The construct in A's
external sample is visible in the model text — `part vehicleFleet : Fleet { part vehicles : … { … }
}` re-declares the inherited `vehicles` — which is structurally the same as the spec's own
`TestWithCutoff :> TestRecord { attribute cutoff : … }`. So A's "missing class" and B's "false
positive" are the same diagnostic on the same construct.
**Why it is still unresolved.** On the letter of KerML `validateNamespaceDistinguishibility`
(§8.3.2.4.5) read with the default `isDistinguishableFrom` (no override for feature memberships),
two same-named `AttributeUsage` memberships of one namespace are not distinguishable, so the warning
may be **correct** and A's class may be real. But SysML §7.6.5 provides the implicit-name route
(`redefines X` with no declared name) as the language's intended way to re-declare with the same
name, and §7.13.4's example does not use it — so either the example is defective or the constraint is
meant to admit the construct. The same ambiguity decides whether F5-01 instantiates
`validateFeatureValueOverriding` (CC-07): if a same-named declaration is not a redefinition, F5-01
does not violate the constraint and P4's first example fails for a different reason than the one
given.
**What would settle it.** A normative ruling (OMG SysML/KerML RTF or a SysML expert) on whether a
same-named declaration in a specializing definition is (a) an illegal duplicate, (b) an implicit
redefinition, or (c) legal-but-discouraged; alternatively, a run of the OMG pilot implementation
under a JVM on the 10 external artefacts plus KG-04, since a second implementation's treatment
would discriminate "spec says duplicate" from "one tool is over-eager". Hand-coding the 10 artefacts
against §7.6.3/§7.6.5 (B's own proposal) would classify them but cannot settle the normative
question without one of the above.
**Who could obtain it.** The PI (a question to the OMG RTF or a SysML expert; the OMG pilot under a
JDK, which was not obtainable in this environment — `TOOLING.md` §2). Costs: a week's latency for the
RTF route, an afternoon for the JVM route.

### 5.2 X-02 — Is the "layer boundary" a property of the instrument, or of the specification's obligation structure?

**The disagreement.** B: "what predicts detection is layer, not specification silence" (report §5,
H9 failed, lines 230–236; A7). R-A/A: the misses are concentrated at "structural/semantic" layers
(RA-01). My finding: in *both* corpora every miss is a condition whose reporting the specification
leaves discretionary (S2, a `check` with a MAY obligation), names nowhere (R1 ×2, F7), or whose
defect status is contested (I1) — so layer and obligation are perfectly confounded in both
populations. B's H9 tested the obligation hypothesis and found two counterexamples (F4-01 inverted
bounds, F4-04 feature-value count: unnamed but caught), so neither predictor is clean.
**Why it matters.** It decides how B's headline may be quoted. "Detection stops at the semantic
layer" invites the reading "validators cannot see semantics"; the obligation reading invites
"validators see what the specification tells them to see", which is a different claim about what a
pass means and the one the evidence supports without residue.
**What would settle it.** A crossed design: mutants at each layer in two conditions (a named
constraint with a SHOULD/SHALL obligation vs an unnamed semantically-equivalent condition), with the
invocation fixed in advance; and the inverse cell (a named, mandatory condition at the semantic
layer). Report per-cell detection with intervals. A construct census is not enough.
**Who could obtain it.** A follow-up issue #8 study (Researcher B's own "highest-value follow-up",
report §9); the harness is already parameterised by binary and the mutant generator asserts
single substitutions. Cost: days, not weeks. No access boundary.

### 5.3 X-03 — Is R1 (a connection end whose feature chain traverses a multi-valued usage) a defect at all?

**The disagreement.** A: yes — "the end does not denote individual features", with
`validateFeatureEndMultiplicity` as "adjacent, not decisive" basis and an authored operational
criterion (`FROZEN-SUBSET.md` lines 66–67). R-A: the criterion conflates a feature with its
instances and no constraint decides it, so R1 is contested as a *defect*, not only as to layer.
B: uses A's labelling, so the contest propagates into its denominator (two of its four misses).
**Why it matters.** If R1 is not a defect, A's structural claim disappears (it already has, after
C05/C06, on layer) and B's external denominator falls from 13 to 11, making the established rate
9/11 rather than 9/13 — the ladder's rungs move. If it is a defect, the installed reading stands and
the tool has a genuine silent miss at the typing/multiplicity layer.
**What would settle it.** A normative grounding of KerML's connector-end rules: does a `connect`
end that is a feature chain through a usage with multiplicity >1 denote a single feature (the chain
resolves to one feature) or a collection (the chain selects many instances)? The two relevant texts
are KerML §7.3.4.6 (feature chains) and the connector/end rules in KerML §8.3.4.5; the retrieved PDF
supports both readings depending on whether "denotes" is read at the feature or the instance level.
A ruling from the OMG SysML/KerML RTF, an implementation's handling (the OMG pilot
implementation's `checkConnectorTypeFeaturing`, which B could not instantiate), or a human SysML
expert would settle it.
**Who could obtain it.** The PI (a question to the OMG RTF or a SysML expert); the OMG pilot
implementation under a JVM, which is lawfully obtainable but was not obtainable in this environment
(`TOOLING.md` §2).

### 5.4 X-04 — Is the bounded engine's false `holds` systematic?

**The disagreement.** None, yet: the critic reports one model on which `-engine check` says `holds
(bounded …)` while `-engine smt` witnesses `violated`, and `-engine all` names the conflict (I
reproduced all three). Neither pilot ran more than one engine, so neither can say whether this is a
one-off probe artefact, an engine-strength mislabel, or a systematic unsoundness in the bounded
search.
**Why it matters.** Both pilots' detection measures are diagnostics-based and unaffected. But
B's verdict-path result (A2, A10.5) and any future "gate on the validator" recommendation rest on
the verdict surface being trustworthy; the critic's finding is a one-model demonstration that a
*negative* verdict is not self-certifying. If it is systematic, every "holds" in the run's verdict
modes inherits an unknown error rate.
**What would settle it.** A small mutant family over invariants (10–20 models, each with a violating
assignment and a matching positive control) run under `-engine check`, `smt`, `all`, and
`-validate=<object>`, reporting agreement/contradiction per model. This is a #8-shaped study of a
*verdict* engine rather than a diagnostics engine, and the harness exists.
**Who could obtain it.** The PI (the binary is pinned in-tree; one afternoon), or a follow-up #8
task; the critic's own raw files give the template.

### 5.5 Not adjudicable at all (recorded, not unresolved)

- **Whether A's labelling preceded the detection run.** No hash of `errors.csv` exists; mtimes were
  reset by re-runs; the composition argument is inferential and weakened by C12. The claim is
  **withdrawn** (B2A-05) and the residual question is not answerable from these artefacts by anyone.
  Only a future run with `coding/errors.csv.sha256` written at freeze can answer it, and that is a
  forward-looking fix, not a settle-criterion for this one.
- **Whether each of A's 18 outputs was a separate model turn.** `manifest.csv`'s
  `generation_timestamp_utc` is the raw file's mtime; no generation log exists.
- **Search completeness for the external corpus.** "The only public corpus located" is a bounded
  search, not an exhaustive one; A states it as bounded.
- **Which pilot's corpus is "more representative".** Neither; see §7.3.

---

## 6. Consequences for each pilot

### 6.1 Pilot A (issue #7)

**Changed because of challenge**

| What | Change | Where |
|---|---|---|
| The detection headline | "silent on 5 of 14 — neither method is an oracle" becomes the ladder 9/14 → 9/13 → 9/12 → 9/10 → **9/9**, with the composition of the silent records shown | report §1 finding 2, §5.3, §13.2; README |
| The wrapper headline | must state the gate: **6/12 any-diagnostic, 9/9 exit-status**; §13's "0/18 → 6/18 → 12/18" must name what each step measures | report §1, §7, §13 |
| The R1 record | layer moved to `type/typing` (C05/C06) **and** defect status marked contested; the operational criterion restated; propagated to `subset.json` | codebook, corrections, subset |
| The I1 record | contested; both denominators (9/14, 9/13[−I1]); contested status belongs in the codebook | report §16.3; codebook |
| The T1-C1 record | **withdrawn** (C12): population 13/11/7; rate 9/13 | report §17 |
| The phantom record | **withdrawn** (C01): combined 20, S1 8 | report §16.1, §5.4 |
| The agreement study | κ = 1.0 **is not reliability evidence**: 8/11 excerpts verbatim in the coder-facing codebook, 11/11 exemplar-covered, **and** the instruction sheet supplied four class criteria as facts, one of them false | report §6.1, §16.5; agreement addendum |
| The freeze claim | "frozen and hashed before detection" **withdrawn**; ordering is argued, not hashed | cover banner, §2 Prop 1, §16.2 |
| Two citations | S1 → notation productions; T2's MAY obligation stated | errors register C08–C10 |
| Occurrence counting | occurrence column added; T6-C2 missing; record-level is an upper bound for two records | detection/occurrence_detection.csv |
| Provenance | per-file sha256 + tool identity in `detection/manifest.json` | detection/ |
| The inspection-gap rate | "7 of 21" → six live tool-surfaced records; 15/19 labelled descriptive | report §5.4, §13 |
| The external arm | 2 error-level / 9 warning-only / 7 clean; the 51.16% comparison withdrawn | report §16.6 |
| The codebook | internally inconsistent (S2 body, R1 table, S1 citations); must carry "superseded" markers and a "contested" status | `CODEBOOK.md` |

**Did not change despite challenge**

- **The frozen 14-row file and the 12/6 split** — byte-identical (`30265ff5…`); B verified every
  excerpt and R-A reproduced the counts. C12 withdraws a record *from the population*, not from the
  file; both must be reported.
- **9/14 as the registered number** — kept beside every corrected version. A's refusal to withdraw
  I1 because the correction would flatter the rate is correct procedure and is upheld.
- **The finding that inspection missed real mechanical notation defects** — six live records,
  tool-flagged, specification-verified; the strongest result in the pilot.
- **The wrapper is universal and not sufficient** — 18/18 raw fail, 6/18 rescued by extraction.
- **The C2 configuration pattern** — descriptive, correctly hedged at n = 1 per cell.
- **No claim of replication** of the anchor — correctly refused; the 0% mechanism remains an
  untested hypothesis.
- **The generator = coder circularity and the one-instrument limit** — exemplary disclosure, unchanged.

**Headline effect.** No numerator moves. The *interpretive* headline moves: A's "9/14 blind spot" is
not supportable as a blind-spot measure and becomes "9/9 on established, mandatory-report records;
4 discretionary/contested misses, one of them positively reported as holding". The wrapper headline
gains a second reading (9/9) that A must print beside 6/12. The agreement figure is demoted from
evidence to disclosure.

### 6.2 Pilot B (issue #8)

**Changed because of challenge**

| What | Change | Where |
|---|---|---|
| F7 | default path 0/4 **unchanged**; across modes: **1 violated / 1 undecided / 2 no verdict**; P3 restated | report A2/A3 (done); body needs a pointer |
| The headline | **23/32 = 0.72 unchanged**, labelled "default `-validate` path", **F4-01 counted as a defect under the semantic reading**; 22/32 stated if a named-constraint-only criterion is used | report §1, §3.5 |
| F5 | 3/4 authored **and** 3/5 cross-corpus; the constraint's MAY obligation stated | report A5 |
| F2 | 4/4 at four sites; **0/1 at succession sources**; class-level claim withdrawn | report A6 |
| F1 | 4/4 for the authored family; reserved-keyword sub-class exits 0 | report A4 |
| F4 | relabelled declared multiplicity; connection-end structure unsampled | report A4/A7 |
| The expectation audit | informed, not blind: the pre-freeze calibration already showed F6/F8 firing; "24/24" near-tautological | report §4.1, methodology §12.6, gate log, A8 |
| The external pre-registration | the "frozen" hash is post-AM1; the pre-run hash is unrecoverable; `run-log` §2's description is wrong | empirical REPORT, run-log, A10 |
| The external arm's M2/M3 accounting | **3 evaluated / 10 n/a**, not 1/10; scoring deviates from §4.2 for non-satisfy items and controls | empirical REPORT, A10.1 |
| The external headline | add the obligation split: 9/9 established, 0/4 discretionary/contested; the aggregate is not a detection-gap measure | empirical REPORT §1/§3, A10.1 |
| Arithmetical slips | "24 of 28" → 23 (or 20 of 23); "5 silent" → 4 silent + 1 warning-only; one ladder order | report A8, analysis.md, empirical REPORT |
| KG-04 | warning reclassified "unresolved / spec-ambiguous", not over-reach; pointer corrected to §7.6.3/§7.6.5 and KerML §8.3.2.4.5 | known-good-triage, report §3.6/A10.3 |
| P4 | site-dependent enforcement; F5-01 may not instantiate the constraint | report §2 P4, §3.4 |
| P5 | "empty range is not obviously ill-formed" **withdrawn** | report §3.5 |
| §4.2, §11.1, §11.5 | "ceiling is typing plus well-formedness", "means nothing at all", "four classes invisible" — all require the default-path qualifier or rewriting | report §§4.2, 11 |
| Harness | the external harness's immutability claim is false and must be implemented or deleted | `run_external.py` |
| Known-good arm | base concentration (9/32 from KG-01) and iterate-to-silence history stated | report §3.1/§8 |
| `spec_status` | post-hoc, single-coder, not a frozen field | report §3.4 |
| README | "No empirical challenge set … nothing here was informed by Researcher A's work" is false | `research/issue-008/README.md` |

**Did not change despite challenge**

- **23/32** — reproduced independently by me, R-B (re-ran the binary over all 32) and R-A (checked
  samples). F4-01's status is the only reading on which it could move, and I rule the model text
  defective.
- **28/32 any-signal**, **0/10 known-good errors**, **9/13 external**, **9/12 and 9/11 rungs** —
  all reproduce.
- **The severity-as-a-measurable-property result** and the **exit-status finding** — the most useful
  results in either pilot; both reproduced by me.
- **The one-instrument boundary** — stated repeatedly and correctly; no correction needed.
- **The P6 refusal** (the external set does not support its own strongest claim) — exemplary, and the
  single most credible move in the run.
- **The single-defect mutant discipline** — 30/32 exact, 2 composite edits (F4-04, F8-01) which R-B
  flagged and which do not change a count.
- **The layer replication on the external corpus** — the finding stands; only its *interpretation*
  gains the obligation confound (§5.1/X-02).

**Headline effect.** The numerator does not move (23/32 default; 24/32 mode-aware). What moves is the
label: "default path, F4-01 counted as a defect" and "the boundary is at what the specification
names, as much as at the layer". The external arm's headline moves in presentation: 9/13 must be
read as 9/9 established + 0/4 discretionary/contested, and the M2/M3 applicability is 3, not 1.

### 6.3 Does any headline number move?

| Number | Moves? | To what |
|---|---|---|
| A: 9/14 detected | **No** (registered number kept) | 9/13 after C12; 9/9 on established+mandatory; all three shown |
| A: 6/12 V1/V2 | **Presentation only** | 6/12 any-diagnostic **and** 9/9 exit-status |
| A: 7 of 21 inspection gap | **Yes, label** | six live tool-surfaced records; 6 of 20/19 |
| A: κ = 1.0 | No | demoted to a reproduction check |
| A: 21 combined / S1 9 | **Yes** | 20 / S1 8 (C01), then 19 / S1 8 (C12) |
| B: 23/32 = 0.72 | **No** | stays 23/32, relabelled; 22/32 only under a criterion neither pilot uses |
| B: F7 0/4 | No (default) | 1 violated / 1 undecided / 2 no verdict across modes |
| B: F5 3/4 | No | 3/5 on the labelled cross-corpus union |
| B: external 9/13 | **No** | 9/13 with the obligation split shown; 9/11 if R1 falls (X-03) |
| B: external M2/M3 "1 evaluated" | **Yes** | 3 evaluated / 10 n/a |
| B: "24 of 28" / "5 silent" | **Yes** | 23 of 28 (or 20 of 23) / 4 silent + 1 warning-only |
| Either: "the ceiling is X" | **Yes, framing** | "the ceiling of the default `-validate` path is typing plus per-constraint well-formedness; the verdict surface is wider and its `holds` is not self-certifying" |

---

## 7. Cross-cutting findings

### 7.1 (i) Did either pilot claim more than its method establishes? What is the corrected wording?

**Both did, in the same shape**: each measured one invocation of one binary and named the instrument,
the language or the ceiling in its conclusion. Four corrected sentences:

1. **(A, detection)** — *Was:* "the validator is silent on 5 of 14 … neither method is an oracle."
   **Corrected:** "at the default `-validate` invocation the tool reported nothing on 4 of the 13
   frozen records; all four are discretionary (a `check` constraint with a MAY obligation), without
   a normative basis (R1 ×2) or contested (I1). It detected 9/9 of the records whose defect status is
   established and whose reporting is mandatory. On S2 it positively reports the requirement as
   holding, vacuously. This is a default-invocation measurement, not a property of the instrument:
   under `-satisfy` the same tool decides requirement satisfaction, and under `-engine smt` it
   decides invariants the `-validate` path cannot see."
2. **(A, wrapper)** — *Was:* "6/18 invalid only because of the wrapper, 12/18 still invalid after
   normalisation." **Corrected:** "18/18 raw outputs fail as-is; 6/18 normalised models produce no
   diagnostic; **under an exit-status gate V1 = 9 and V2 = 9**, because three error-severity
   `reserved-keyword-name` reports exit 0. The gate must be stated for either number to mean
   anything."
3. **(B, headline)** — *Was:* "23/32 = 0.72 sensitivity … four structural defects invisible."
   **Corrected:** "under the default `-validate` invocation, 23/32 authored mutants produced a
   relevant error (F4-01 counted as a defect: `[4..2]` is an empty range and therefore
   unsatisfiable, though no catalogue constraint names it). Across modes, one of the four F7 mutants
   is detected, one is checked and undecided, two produce no verdict. What a pass establishes is
   notation, resolution, typing and the constraints this tool implements — and nothing about
   adequacy, behaviour, or the conditions the model does not state."
4. **(B, external arm)** — *Was:* "9/13 = 0.69, statistically indistinguishable from 0.72, layer
   boundary replicates." **Corrected:** "9/13 = 0.69 on 13 observed items, of which 9 have
   established defect status and mandatory reporting (detected 9/9); the 4 misses are one
   discretionary constraint, two items without a normative basis and one contested. The aggregate
   agreement with 0.72 is a composition artefact; what replicates is the pattern that detection
   tracks what the specification names and mandates, not the layer."

### 7.2 (ii) Are the headlines supportable as stated? (adjudicated in §1.3, arithmetic in §3.3/RA-01 and §3.5)

A's is **not** supportable as a blind-spot measure; its most defensible form is the ladder with the
composition shown. B's **is** supportable with three labels (default path; F4-01's reading; one
instrument) plus the obligation confound. Neither is a fabrication and neither collapses: the
qualitative findings — the wrapper is universal and insufficient; inspection misses mechanical
notation defects; a pass is not a semantic pass; exit status is not a validity verdict — all survive
every ruling in this document.

### 7.3 (iii) Anti-circularity: is each pilot's ground truth independent of the instrument it measures?

**A — independent in construction, unverifiable in ordering, and not independently verified.**
- No frozen label is derived from a validator verdict: the frozen 14 omit exactly the cheap
  tool-flagged notation defects and include records the tool cannot see (composition argument,
  inferential but strong before C12, weaker after). The detection run edits no label.
- But no hash evidences the ordering (B2A-05); one class (T2) was added after the detection run
  (validator-surfaced, spec-verified); the post-inspection arm is validator-surfaced by
  construction and is correctly excluded from B's set; and the second coder is an answer key plus
  asserted criteria, not an independent check (RA-05). So the *only* independence A has is its own
  inspection against the specification — which is the thing a second coder was supposed to test.
**B — the instrument does not define the defect, but the defect set's validity is authored and
unverified.**
- Mutant defect status and expectations were hashed before the run (verified: methodology 14:08:53Z,
  MANIFEST 14:13:00Z, first run 14:13:03Z), and validator silence never reclassified a mutant. That
  is the anti-circularity rule met.
- But: the expectations were informed by construct-level probes (RB-03); `spec_status` is post-hoc
  (RB-10); the known-good arm is the mutant parents (RB-11); two mutants carry composite edits and
  F5-01 may not instantiate its constraint (CC-07); and no second coder judged whether each mutant
  instantiates its class (issue #8's own criterion).
- The **external set** is genuinely A's, not B's, and predates B's run — that is real independence of
  authorship. But B had run 15 of the 18 models at Gate 2 and the agents had exchanged reviews before
  the subset was frozen, so the *predictions* were informed. B states this.
**Net:** neither pilot's ground truth is circular *in the validator-defines-defect sense*; neither is
independently verified in the human-expert sense. The one genuinely independent witness in the run
is the second coder's three clean-model calls and its independent noticing of three reserved-keyword
instances — plus the specification text, which is the oracle both pilots actually use.

### 7.4 (iv) Representativeness and the oracle: what neither corpus can establish

Both corpora are small and author-labelled (18 models, one generator family, six self-authored
prompts, one generation per cell; 32 mutants from 10 hand-authored bases, 9 derived from one 23-line
model). **Neither can establish:**

1. the frequency or class distribution of errors in "LLM-generated SysML v2" — A's numbers are
   properties of its own six prompts, and B's are properties of its own ten bases;
2. the sensitivity or specificity of "SysML v2 validators" — one binary, one version, one
   invocation set per measurement;
3. that the fault model is representative — four of B's eight classes have no observed counterpart
   and the construct census is 0/18 for constraints, unit literals, metadata, `connection def`,
   explicit `end` features and short names;
4. any false-positive rate — 0/10 known-good and 0/4 clean controls falsify gross over-reach, and
   nothing more;
5. that the classes are the *right* classes — no human expert anywhere; the generator, coder, mutant
   author and selector are one agent (A) or one agent plus one informed reader (B);
6. whether the layer boundary is a property of the instrument or of the obligation structure (§5.2);
7. anything about models that do not state a machine-checkable condition — the tool reports `holds
   (vacuous)`, so "validator pass" and "semantic pass" are different objects;
8. the stability of any rate under re-encoding — B's mutants are one encoding each, and the encoding
   flips detection (runs 2.4/2 vs 2.4/3; 2.4/5);
9. whether the two pilots' agreement at 0.64–0.72 reflects the world or the composition — both
   populations are dominated by classes the instrument handles (X-01).

### 7.5 (v) Process integrity

| Mechanism | A | B |
|---|---|---|
| Freeze hash of the *method* | written, hashed, verified | written, hashed, verified |
| Freeze hash of the *ground truth* | **absent** (claim withdrawn) | present and pre-run for the synthetic arm |
| Pre-registration hash of the external rules | n/a | **post-AM1; pre-run hash overwritten** (RB-01) |
| Addenda preserve originals | yes; but summary sections were not updated (RA-06) | yes; but the front of the report and the README were not updated (RB-12) |
| Artefact stability | **unstable during Gate 2 and Gate 3**; a "frozen" response was edited and the ledger labelled the later bytes with the earlier time (P-1) | stable except the idempotent MANIFEST/mutant rewrite (A2B-10) and a false immutability claim in the external harness (RB-07) |
| Answer-key contamination | **yes** — 8/11 verbatim, 11/11 exemplar-covered, plus asserted criteria (RA-05) | expectations informed by calibration probes (RB-03); no answer key for mutant validity because there is no second coder |
| Forward-dated times | the response's declared window (14:23–14:29Z) precedes the content it carries (C12–C13 at 14:31Z) | several (RB-09) |
| Access boundaries | none challenged | none challenged (Syside licence respected; OMG pilot unavailable, logged) |

Neither pilot's numbers are compromised by these failures; the *evidential weight* of the freeze
claims is. The adjudication's rulings cite only bytes that both reviewers saw and that are stable at
my pin.

### 7.6 (vi) Is the `name-conflict` cross-pilot tension resolvable on current evidence?

**Partly — the two observations are one mechanism; whether that mechanism is a defect is
unresolved.**

- **What resolves.** I checked the messages in `detection/diagnostics.csv`: all 119 external
  `name-conflict` diagnostics have the form *"Duplicate of inherited member name 'X' from Y"*, the
  same form as B's KG-04 warning (`cutoff` from `TestRecord`). So A's headline missing class and B's
  only false positive are the **same construct**: a same-named declaration inside a specializing
  definition that re-declares an inherited member without `:>>`/`redefines`. That is a genuine
  consolidation neither researcher made, and it changes the character of the tension: it is not
  "one pilot's signal is another's noise" but "one diagnostic with one mechanism, whose normative
  status is ambiguous".
- **What does not resolve.** On the retrieved text: KerML `validateNamespaceDistinguishibility`
  (§8.3.2.4.5) requires all memberships of a namespace to be distinguishable, and the default
  `isDistinguishableFrom` compares declared names and metaclass conformance with **no override** for
  feature memberships — so two same-named `AttributeUsage` memberships of one namespace are not
  distinguishable, and the warning is *correct on the letter*. But SysML §7.13.4's own example
  (lines 5215–5216) uses exactly this construct, and §7.6.5 provides the implicit-name route
  (`redefines X` with no declared name) that the language intends — so either the example is
  defective or the constraint is meant to admit implicit redefinition. A normative ruling, not a
  retrieval, is needed.
- **Consequence for the taxonomy.** A was right not to add the class on the strength of one external
  corpus, and B was right not to adopt it. It stays a **candidate**, and the reason is now sharper
  than either stated: the diagnostic may be *right*, and the models may be *wrong*, in a way the
  specification contradicts by example. The same ambiguity decides whether F5-01 instantiates
  `validateFeatureValueOverriding` (CC-07), because that turns on whether a same-named declaration is
  a redefinition.

---

## 8. What could not be adjudicated, and why

1. **The pre-detection ordering of A's labels** (§5.4): no hash, mtimes reset, argument inferential.
   Recorded as "not verifiable", not false.
2. **The original detection-run time and the original post-inspection file**: the current
   `detection/raw/*.txt` were regenerated; no run log records the first run. A's claim that
   `errors-post-inspection.csv` postdates it is author-asserted.
3. **Whether A's 18 outputs were separate model turns**: `manifest.csv`'s generation timestamp is the
   file mtime; all 18 were written within 32 seconds; no generation log.
4. **The second coder's reasoning**: only outputs exist; the inputs (and the instruction sheet) are
   now known, which is enough to bound the evidential weight but not to assess how it decided.
5. **The external LaVoie corpus's provenance beyond the manifest**: local files match A's recorded
   hashes; neither B nor R-A re-fetched from upstream; I did not either (no need, and the arm is
   descriptive).
6. **Whether the `-engine check` false `holds` is a bug, a mislabelled strength, or a probe
   artefact**: I reproduced the observation, not the cause; I read no source (§5.3).
7. **Whether reachability/liveness is expressible at all in this tool**: no flag states an
   *eventual* property in the material read; "not established" rather than "not expressible".
8. **The OMG pilot implementation's behaviour on any of this**: no JVM, no CLI asset (B's
   `second-validator-attempt.md`, reproduced by R-B); an access/environment boundary, logged.
9. **Syside**: licence boundary; not attempted; out of scope by `TOOLING.md` §3.
10. **Whether either pilot's classes "carve nature at its joints"**: no human expert; nothing in the
    artefacts can substitute.

---

## 9. Sources

**Pinned artefacts:** all rows of §2.2, with hashes and the 14:51:34Z/15:03:54Z stability check.

**Retrieved specification text (quoted above):**
- OMG SysML 2.0 Part 1, `formal/2026-03-02`, sha256 `46e6c047…a84a83a` — §7.6.5 Effective Names
  (txt 3439–3470), §7.13.4 default feature values (txt 5178–5220), §8.2.2.17.2 succession notation
  (cited by A), §8.2.2.18 states notation, §8.2.2.21.2 `SatisfyRequirementUsage`.
- OMG KerML 1.0, `formal/2026-03-01`, sha256 `3bcc96f9…373697` — §8.3.2.4.5
  `validateNamespaceDistinguishibility` (txt 8463–8470), `isDistinguishableFrom` (8154–8170),
  §8.3.4.11.2 MultiplicityRange (14257–14290), §8.4.4.12.2 Multiplicity ranges (17267–17290),
  `validateMultiplicityRangeBoundResultTypes` (14372–14381), `validateMultiplicityRangeBounds`
  (14384–14396), `validateFeatureEndMultiplicity` (catalogue row; §8.3.3.3.4).

**Project artefacts read:** `PROTOCOL.md` (§3, §4, §6, §7, Amendment A1); `gate-log.md` (Gates 0–4);
`TOOLING.md`; issues #7, #8, #10 (`gh issue view`); both pilot reports; `research/issue-007/**`
(methodology, amendments, codebook, coding CSVs, reconciliation, second-coder instructions and
codebook, detection summary/diagnostics/table/occurrence file, external manifest);
`research/issue-008/**` (methodology, MANIFEST, analysis, triage, known-good triage, calibration log,
run logs, probes-gate2, empirical PRE-REGISTRATION/run-log/results.csv/REPORT); the four
cross-reviews; both independent reviews; the semantic-ceiling critique, `CLAIMS.csv`, its probes,
raw outputs and RUNLOG.

**Nothing in this document is cited from memory.** Where a claim rests on a run, the argv and exit
status are given (§2.4); where it rests on a file, the file and section are named; where it rests on
the specification, the retrieved text is quoted.
