# What error population does a corpus of GenAI-generated SysML v2 models contain? — a pilot

**Issue:** [#7](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/7)
**Status:** **PILOT — preliminary by construction, and it cannot close issue #7.**
**Post-review corrections:** Reviewer B's Gate-2 review is answered in
[`A-response-to-B-review.md`](../research/relational/cross-reviews/A-response-to-B-review.md); every
number that changed is listed in **§16** below, with old and new values. Read §4, §5, §6 and §11
with §16. The frozen 14-record population survives as a file, but one record is withdrawn as legal SysML
(`first start;`, C12) and one is contested (I1), so **the current denominators are 13 records /
11 models / 7 clean** — see the CURRENT NUMBERS table below and §18. One post-inspection record
was withdrawn as a phantom; the agreement interpretation is materially weakened (A-4).

**CURRENT NUMBERS (added 2026-11-13T15:10Z, A-1).** The original figures are kept below and in
§1; these are the corrected ones, with the reason and the section that changed them. Where two
denominators exist they are labelled uniquely: `[C12]` = after the `first start;` withdrawal (14 − 1),
`[−I1]` = excluding the contested I1 record, `[−R1]` = excluding the two contested R1 records,
`[−S2]` = excluding the discretionary S2 record.

| Measure | Original | Current | Why |
|---|---|---|---|
| Frozen population | 14 records / 12 models / 6 clean | **13 / 11 / 7** `[C12]` | `first start;` is legal (`Actions::Action::start`), C12 |
| Combined population | 21 records | **19**: 21 → **20** (C01 phantom) → **19** (C12 `first start;`) | A-1, §16, §17 |
| Combined S1 | 9 | **8** | C01 |
| Combined detection | 15/21 = 71 % | **15/19 = 79 %, descriptive not recall** | A-16 |
| Frozen detection | 9/14 = 64 % | **9/13 = 69 % `[C12]`; 9/12 `[−I1]`; 9/10 `[−R1]`; 9/9 `[−S2]`** | A-9, RA-01 |
| Errors per model | range 0–3 | **0–2** | A-1 |
| W1, prose-only reading | 18 vs 4 | **18 vs 7** | A-1 |
| V1 / V2 wrapper split | 6/18, 12/18 | **6/12 and 12/18 under an any-diagnostic gate; 9/9 under an exit-status gate** | A-10, RA-02 |
| Agreement κ | quoted as reliability | **reproduction check: 8/11 excerpts verbatim, 11/11 exemplar-covered; not reliability** | A-4 |
| Post-inspection arm | 7 records, "missed a third (7 of 21)" | **6 live records; counts, not a rate; detection on them is descriptive** | A-16 |

N = **18** models, where issue #7 asks for ≥ 200 across several tasks, models and prompting
strategies. Every number below is a property of *this* corpus, generated in this session, not of
"LLM-generated SysML v2" in general.
**Frozen methodology:** `research/issue-007/METHODOLOGY-FROZEN.md`, sha256
`269d8dbe7228db83d20ca2be39991172f20fd23458ac1e5e6755ff7269564f76`, frozen 2026-11-13T14:05:30Z,
**before** any model was generated and before any contact with Researcher B's work.
**Codebook:** `research/issue-007/coding/CODEBOOK.md`, final sha256
`d2019448c6840ced7b1aab077c40fbdf5afd89747426370ca80007b07ff76766` (v1.0 `9d3e5e05…f10a03`,
v1.1 `d42a2ad0…943617`; amendments in §9–§10 of that file and in
`research/issue-007/AMENDMENTS.md`).
**Instrument (detection column only):** OpenSysML CLI v0.12.1, `.tools/sysml`, sha256
`ddfc2962…1598f0` per `research/relational/TOOLING.md`.
**No git operations were run** (per protocol §6); this report is a file in the working tree.

---

## 1. Summary answer

**The error population of this 18-model corpus is small, dominated by name resolution and
notation, and contains almost no structural or semantic defects — and the wrapper/formatting
layer is universal in the raw artefacts but explains only part of the invalidity.**

**[Superseded in part — 2026-11-13T15:10Z, A-1/A-3/A-9/A-23: the summary sentence above and the tables
that follow are the first-published form. Current readings: the frozen population is 13 records in 11
models with 7 clean `[C12]`; the two "structural" records are contested as to defect status (R1), and
the one semantic record is contested (I1); the wrapper split is gate-dependent (6/12 any-diagnostic,
9/9 exit-status). See CURRENT NUMBERS at the top and §18.]**

Headline numbers, each with its denominator:

| Measure | Value | Denominator |
|---|---|---|
| Models generated and coded | 18 | 18 cells (6 tasks × 3 configurations), one generation per cell |
| **Coded errors, frozen pre-detection population** | **14** | 18 models; mean 0.78, median 1, range 0–3 |
| Models with ≥ 1 coded error (frozen) | **12** | 18 |
| Models with no coded error (frozen) | **6** | 18 (T2-C3, T3-C3, T5-C1, T5-C3, T6-C1, T6-C3) |
| Coded errors after post-inspection verification | 21 | 18 models; 15 models affected, **3** clean |
| Raw outputs that are not SysML files as emitted (W1) | **18** | 18 raw outputs (all fenced markdown; 4 with preamble, 6 with trailing prose) |
| Raw outputs that fail validation as-is | **18** | 18 (81 diagnostics: **72 `syntax` + 9 `reserved-keyword-name`**, A-20) |
| Normalised models that validate clean | **6** | 18 (33 diagnostics remain) |
| **V1: invalid *only because of the wrapper*** | **6** | 18 |
| **V2: still invalid after normalisation** | **12** | 18 |
| Second-coder agreement, model-level presence | 12/12 | 12 double-coded models |
| Second-coder agreement, record-level class | 11/11, κ = 1.0, α = 1.0 | 11 paired records |
| Coded errors the pinned validator detects | 9/14 (64 %) | 14 frozen records |

Class frequencies (frozen population, denominator = 14 errors; second denominator = models):

| Class | What it is | Errors | Models | Layer |
|---|---|---|---|---|
| N1 | unresolved model-local reference | 5 | 5 | name resolution |
| S1 | construct in a non-conforming textual form | 3 | 3 | syntax/parse |
| R1 | connector ends that are not individual features | 2 | 2 | structural/architectural |
| N2 | stdlib prelude omitted (scalar types unresolved) | 1 | 1 | name resolution |
| S2 | `satisfy` with no satisfying feature | 1 | 1 | constraint/OCL |
| T1 | definition referenced where a usage is required | 1 | 1 | type/typing |
| I1 | model contradicts its own declared values | 1 | 1 | semantic/behavioural |
| **Total** | | **14** | **12 models with ≥1** | |

After post-inspection verification the same corpus shows **S1 = 9** and adds one **T2**
(attribute typed by a part definition), for 21 records in 15 models. The frozen numbers stay the
primary ones because they were fixed before the instrument ran; the additions are reported
separately, with their verification route (§5.5), precisely so that no validator verdict counts
as an error.

**Three findings that matter beyond this corpus:**

1. **The raw-vs-normalised split is real but not decisive.** All 18 raw outputs are markdown;
   six are invalid *only* because of that (V1 = 6/18). Twelve still fail after the wrapper is
   removed (V2 = 12/18). So a "0 % syntactic validity" result like the anchor's is *available*
   from wrapping alone, but wrapping cannot be the whole story here: extraction repaired only a
   third of the failures.
2. **Inspection alone missed a whole defect family; the validator found it and is blind to
   others.**
   **[Corrected 2026-11-13T15:10Z — A-9, A-10, A-16, A-20.** (i) The "blind to others" reading is
   a composition statement, not a blind-spot measure: the five silent records are one withdrawn as
   legal (C12), one `check` constraint with a MAY obligation (S2), two with no normative basis and
   contested defect status (R1), and one contested (I1); the ladder is 9/14 → 9/13[C12] → 9/12[−I1]
   → 9/10[−R1] → 9/9[−S2], so on records that are established defects and mandatory to report the
   tool detected 9/9. (ii) The wrapper split is gate-dependent: 6/12 under an any-diagnostic gate,
   9/9 under an exit-status gate (T2-C2, T6-C1 and T6-C3 are error-severity reports that exit 0 —
   not warning-only). (iii) "Two-pass human-style inspection" asserted a process the artefacts do
   not show: the recorded passes are an open pass, mechanical indicators (`coding/inspect.py`) and
   a coding pass; the detection run then surfaced six further real defects. (iv) "A third of the
   defects (7 of 21)" is a rate over a validator-surfaced arm; the counts are 6 live records against
   19, and detection on them is descriptive, not recall.]** The first inspection pass coded 14 defects; 7 further notation/typing defects
   (`port return;`, `port out;`, `attribute state : …`, `action def assign;`, an attribute typed
   by a part definition) were only surfaced by the detection run and then verified against the
   specification's reserved-keyword list (§5.4). Conversely the validator is silent on 5 of 14
   frozen records — including a dangling succession source, a `satisfy` with no satisfying
   feature, both multi-valued connectors, and the documentation/value contradiction. Neither
   method is an oracle.
3. **A configuration-linked failure pattern is visible but under-powered.** Every one of the six
   C2 models ("return the model in one fenced block and nothing else") contains at least one
   error, and four of the six fail in the *same* way: a `satisfy … by <name>` whose name is the
   requirement definition's own subject parameter and not a model element. With n = 1 per cell
   this is a hypothesis, not an effect.

---

## 2. Status of the propositions

| # | Proposition | Status | Basis |
|---|---|---|---|
| 1 | This corpus contains 14 distinct defects across 18 models (12 models affected, 6 clean) | **Established for this corpus**, with the status corrections of §17/§18 | `coding/errors.csv` is **frozen** (byte-identical; sha256 `30265ff5…`); **[corrected 2026-11-13T15:10Z, A-3: no hash of it was taken at freeze, so the ordering is supported by the composition argument, not by a hash — see §16.2]**; each record has an excerpt and line span |
| 2 | Name resolution is the largest frozen class (6/14 errors: N1 5 + N2 1) | **Established for this corpus** | as above; per-configuration tables in §4 |
| 3 | The class distribution is corpus-bound, not a property of "LLM-generated SysML v2" | **Established as a limit** | one generator family, 6 self-authored prompts, n = 18 |
| 4 | The codebook is applicable without drift by an independent second reader | **Provisional** | 12/12 presence, 11/11 class, κ = 1.0 — but the codebook was built from the same corpus, the coder is the same model family, and the examples are recognisable (§6.1) |
| 5 | The error classes are the *right* classes | **Not established** | no human expert, no held-out corpus, no second domain; two classes appeared only after the instrument ran |
| 6 | All 18 raw outputs fail as SysML *because they are markdown* | **Partly — the split is gate-dependent** | 18/18 raw fail; **[corrected 2026-11-13T15:10Z, A-10: 6/12 normalise clean under an any-diagnostic gate, 9/9 under an exit-status gate; the original 6/18-and-12/18 pair mixed the two gates]** |
| 7 | The anchor's 0 %-vs-100 % anomaly is explained by formatting | **Not established — and not testable from this corpus** | V1 = 6/18 makes the mechanism available, not dominant; no access to the anchor's outputs, prompts or parser |
| 8 | C2 ("fenced block and nothing else") causes the dangling-`satisfy` pattern | **Provisional, under-powered** | 4/6 C2 models share the mechanism; one generation per cell, no repeats, no variance |
| 9 | The validator is a reliable detector of this error population | **Contradicted as a general claim**, with the composition stated | 9/14 detected; **[corrected 2026-11-13T15:10Z, A-9: after C12, 4/13 silent — one legal-and-withdrawn, one discretionary `check`, two contested R1 + one contested I1; on established-and-mandatory records, 9/9]** |
| 10 | The pilot reproduces or refutes the anchor's design | **Not attempted — impossible** | anchor publishes no models, prompts-as-code, artefacts or parser (§7) |

---

## 3. Corpus: what was built, and the search that preceded it

### 3.1 Bounded search for a public corpus (freeze §2.1; ≤ 15 minutes)

| Query / route | Outcome |
|---|---|
| GitHub repository search: `SysML v2 LLM generated models dataset`, `sysmlv2 llm output corpus`, `Cibrian SysMLv2 agent dataset` | 0 results (repo search works — a control query `sysml v2` returns the pilot implementation, OpenSysML, etc.) |
| GitHub code search `sysml requirement satisfy generated llm` | 0 results |
| Web search (3 queries: dataset of LLM-generated SysML v2 on GitHub; SysML v2 LLM artefact repositories/Zenodo; Cibrián data availability) | Found: LaVoie et al. 2026 companion repository; a HAL dataset "SysML v2 as an LLM-Oriented Workflow Language" (reference models, not LLM outputs); the two anchors, neither with artefacts |
| Anchor A (Cibrián et al.) availability | "data available on request" — no prompts file, no models, no code; recorded in `evidence/literature.md` §4.12 |
| Anchor B (Stein et al.) availability | "dataset available on request" — nothing released |

**Usable external corpus found:** LaVoie, Andujar Lugo, Topcu & Kara (2026),
*Natural-Language to SysMLv2 Translation via Conformance-Driven Iterative Refinement*,
arXiv:2607.14162 (ASME IDETC/CIE 2026), companion repository
`cmuchancel/NL-to-SysMLv2-via-Conformance-Driven-Refinement`. It releases 151 SysMBench prompts,
604 prompt–model cases and 1,043 iteration artefacts across four model backends — the only public
corpus of LLM-generated SysML v2 text located.

**Why it is not the primary corpus:** the released artefacts are stored as `.sysml` files, i.e.
the pipeline stripped the markdown wrapper before writing. Criterion (b) of the frozen search
rule — raw outputs *including* fences and preamble — is therefore not met, and the wrapper
question could not be asked of it. It is used instead as a **secondary instrument check** with its
own denominator (§5.6), never for taxonomy frequencies.

**Recovery ladder applied:** the anchor's "on request" statement was not pursued as a request to
authors within this pilot (it would not arrive inside the session; the route is recorded for the
PI in §9). The search moved to the artefact-release route (GitHub/Zenodo/HAL), which succeeded for
a different study. No access control was bypassed anywhere; nothing was blocked.

### 3.2 Own corpus (the primary corpus)

6 tasks × 3 configurations = **18 outputs**, one generation per cell, no repair loop, no validator
in the loop, no re-generation. Prompts and rationale: `research/issue-007/corpus/prompts.md`
(written before generation). Raw outputs: `research/issue-007/raw/*.md` (verbatim, fences and
prose preserved). Manifest with per-file sha256: `research/issue-007/corpus/manifest.csv`.

**Generator identity (honest):** the same DeepSeek-family model served through DSH that is also
coder A; the exact checkpoint is not exposed to me. I do not claim one. This makes the corpus and
its first coder the same system — a circularity that is stated, mitigated procedurally, and not
eliminated (§6.1).

**Normalisation** (`corpus/extract.py`, deterministic, offline): 18/18 had exactly one
```` ```sysml ```` fence; the fence lines were removed and **nothing inside the body was touched**
(no import added, no typo fixed, no reordering). Preamble present in 4/18 (T1-C1, T2-C1, T4-C1,
T5-C2), trailing prose in 6/18, multiple blocks 0/18. No model was left unfenced, so the
"no_fence ⇒ do not strip prose" rule never fired. Every decision is in
`corpus/extraction-log.json`.

---

## 4. The error population, with denominators

### 4.1 Frozen population (coded before the instrument ran)

| Model | Configuration | Errors | Classes | Preamble in raw |
|---|---|---|---|---|
| T1-C1 | C1 | 1 | N1 | yes |
| T1-C2 | C2 | 1 | S1 | no |
| T1-C3 | C3 | 1 | I1 | no |
| T2-C1 | C1 | 1 | S1 (4 occurrences) | yes |
| T2-C2 | C2 | 1 | S2 | no |
| T2-C3 | C3 | **0** | — | no |
| T3-C1 | C1 | 1 | N2 (10 occurrences) | no |
| T3-C2 | C2 | 2 | S1, N1 | no |
| T3-C3 | C3 | **0** | — | no |
| T4-C1 | C1 | 2 | T1, R1 | yes |
| T4-C2 | C2 | 1 | N1 | no |
| T4-C3 | C3 | 1 | R1 | no |
| T5-C1 | C1 | **0** | — | no |
| T5-C2 | C2 | 1 | N1 | yes |
| T5-C3 | C3 | **0** | — | no |
| T6-C1 | C1 | **0** | — | no |
| T6-C2 | C2 | 1 | N1 | no |
| T6-C3 | C3 | **0** | — | no |

By configuration: **C1 5 errors / 6 models (2 clean); C2 7 errors / 6 models (0 clean); C3 2
errors / 6 models (4 clean).** By task: T1 3, T2 2, T3 3, T4 4, T5 1, T6 1 — task identity is a
descriptive stratifier at this n, nothing more.

Every record, with excerpt, line span, class, layer, severity, constraint reference and
confidence: `coding/errors.csv`. Classes, inclusion/exclusion criteria, worked examples,
precedence rules and the explicit "not an error" list: `coding/CODEBOOK.md`. Models with zero
errors are rows in `coding/models.csv`, so the denominator is auditable rather than implied.

**What the population is made of — the mechanisms, in plain language**

- **N1 (5):** four of the five are the *same* textual habit — `satisfy <requirement> by <name>`
  where `<name>` is the subject parameter declared *inside* the requirement definition, not a part
  in the package (T3-C2, T4-C2, T5-C2, T6-C2). The fifth is a dangling succession source,
  `first start;`, with no `start` declared (T1-C1).
- **N2 (1):** a model with no library import at all, so six `Real` and four `Boolean` occurrences
  do not resolve (T3-C1).
- **S1 (3):** a `satisfy` written as `satisfy greenhouse to moistureControl` (T1-C2); four
  transitions in SysML v1/UML `from … to … on …` form (T2-C1); `port in;` / `line.in` using a
  reserved direction keyword as a name (T3-C2).
- **S2 (1):** `satisfy lowerBeforeArrival;` with no satisfying feature at all (T2-C2).
- **T1 (1):** a succession whose source and target are `action def` declarations, i.e. types
  rather than actions (T4-C1).
- **R1 (2):** connectors whose ends chain through `Agv[10]`, `DockingStation[4]` — collections,
  not individual features (T4-C1, T4-C3).
- **I1 (1):** a requirement whose own documentation says "between 35 % and 75 %" while its own
  attribute declares a 55 % upper bound (T1-C3). The prompt-fidelity deviation is *not* counted;
  only the internal contradiction is.

### 4.2 What was looked at and deliberately not coded as an error

Recorded so that the taxonomy is not inflated by taste; each with the reason, in CODEBOOK §5:
prompt-fidelity deviations; untyped port usages (12 models); part-to-part and port-to-part
connection ends where both are single-valued; connections between value properties (T3-C1);
`flow of <attribute def>` (T6-C1); `entry action lowerArms;` shadowing an `action def` of the same
name; unused declarations and imports; omitted behaviour; naming and decomposition choices.
`coding/omissions.csv` records the four coverage/omission observations separately, never in the
error counts.

**Tension to hold open:** exclusion 3 (part-to-part connections) and exclusion 5 (flow over an
attribute def) are the two exclusions I am least sure of. I could not find a normative constraint
that decides either, and the pinned validator reports nothing on them. If a reviewer can point to
one, R1's scope and the error total change.

---

## 5. The detection measurement (instrument, not ground truth)

Full outputs: `detection/raw/*.txt`; parsed diagnostics: `detection/diagnostics.csv`; per-artefact
summary: `detection/summary.csv`; per-class table: `detection/table.md`.

### 5.1 Recall on the frozen population

| Class | Records | Detected | Diagnostic(s) |
|---|---|---|---|
| S1 | 3 | **3/3** | `syntax` (T1-C2, T2-C1), `reserved-keyword-name` (T3-C2) |
| N1 | 5 | **4/5** | `unresolved`; silent on `first start;` (T1-C1) |
| N2 | 1 | **1/1** | `unresolved` × 9 with "did you mean ScalarValues::Real" |
| T1 | 1 | **1/1** | `endpoint-not-a-node` ("succession endpoint … is not an action node") |
| R1 | 2 | **0/2** | silence on both multi-valued connectors |
| S2 | 1 | **0/1** | silence on `satisfy … ;` with no `by` |
| I1 | 1 | **0/1** | silence (nothing relates documentation to declared values) |
| **Total** | **14** | **9/14 (64 %)** | |

**Ladder (added 2026-11-13T15:10Z, A-9).** The five silent records of the 9/14 figure are not a
homogeneous blind spot: 9/14 → **9/13[C12]** (T1-C1 withdrawn as legal) → **9/12[−I1]** (contested
defect status) → **9/10[−R1]** (two records, no normative basis, contested defect status) →
**9/9[−S2]** (a `check` constraint whose obligation is "MAY report, satisfy by implied
relationships, or ignore"). The numerator never moves; the denominator shrinks by records whose
defect status or reporting obligation is not established. 9/9 is a subset result with no
inferential power, and it is labelled as such.

**Occurrence ceiling (added 2026-11-13T15:10Z, A-8).** The record-level column is an **upper bound**
for two records: the tool flagged 2 of 3 occurrences of `T3-C2-E01` and 1 of 2 of `T4-C1-E01`. The
occurrence table (`detection/occurrence_detection.csv`) now also carries `T6-C2-E01`, whose
unresolved name occurs three times (line 40 and line 42 twice), all flagged.

The raw-vs-normalised comparison: **18/18 raw fail** (81 raw diagnostics: **72 `syntax` + 9
`reserved-keyword-name`**, A-20; the original text said "81 `syntax` diagnostics", which was wrong
by nine), **6/18 normalised validate clean** under an any-diagnostic gate; the 12 that still fail carry 33
diagnostics.

### 5.2 Instrument behaviour, characterised with 10 minimal probes

Probes are in `detection/probes/` and their outputs in `detection/raw/probe*.txt`. Each isolates
one construct family so the detector's scope can be stated rather than guessed:

| Probe | Construct | Verdict |
|---|---|---|
| probe01 | `first bogus;` with `bogus` undeclared | **no diagnostic** (exit 0) — while probe04 shows the same tool *does* resolve expression names, so this is a gap in succession-source resolution, not a general one |
| probe02 | `satisfy r;` (no `by`) | **no diagnostic** |
| probe03 | `connect b.p to b.p;` (value properties) | no diagnostic |
| probe04 | undefined name in an expression | `unresolved` ✓ |
| probe05 | `satisfy s to r;` | `syntax` ✓ |
| probe06 | `satisfy r by nosuchthing;` | `unresolved` ✓ |
| probe07 | `port in;` | `reserved-keyword-name` — **exit 0**, message says the notation "does not conform" |
| probe08 | `transition from … to … on …;` | `syntax` ✓ |
| probe09 | connector through `B[10]`/`B[2]` chains | no diagnostic |
| probe10 | succession over an `action def` | no diagnostic (the corpus instance was caught only because a *second* name in the same construct produced `endpoint-not-a-node`) |

**Two instrument properties the report must state.** (a) **Exit status is not a validity verdict:**
`reserved-keyword-name` is emitted as an `error` but the tool exits 0 with "no error that stops a
check; the notation reported above does not conform". A pipeline that reads only exit codes would
call those models clean. (b) **The stdlib prelude confound is real and visible:** T3-C1's nine
`unresolved` diagnostics all carry the "did you mean `ScalarValues::Real`" hint, i.e. the N2 class
is distinguishable from N1 by the message, but a pipeline that counts `unresolved` without reading
messages will conflate "forgot one import" with "references something it never defines".

### 5.3 What the instrument does not see

Silent on 5/14 frozen records: a dangling succession source; a `satisfy` with no satisfying
feature; both multi-valued connectors; the documentation/value contradiction. Three of these are
**not checked under the invocation I ran**: the default `-validate` invocation reports nothing on
these records, and no invocation I ran returns a defect verdict for them. **[Corrected
2026-11-13T15:10Z, A-22: the original sentence placed them "outside its stated scope" and quoted
"evaluates expressions but executes neither actions nor state machines" — a limitation documented of
the OMG Pilot Implementation (`evidence/spec-tooling.md` §3.3(f)), not of the pinned OpenSysML
binary, which does execute actions and state machines. The scope justification is withdrawn.]** One
(succession source) is a resolution gap the tool's own message style suggests it could close.

### 5.4 Post-inspection additions — and why they are not in the frozen population

Running the instrument surfaced **7 further defects** the inspection pass had missed, all of them
notation-level: `port return;` (T6-C1, T6-C2, T6-C3, T5-C3), `port out;` (T3-C2 — the frozen
record had recorded only `in`), `attribute state : String;` (T2-C2), `action def assign;` (T4-C1)
and `attribute window : VisibilityWindow;` where `VisibilityWindow` is a `part def` (T5-C3). Each
was verified **against the specification, not the diagnostic**: the reserved-keyword list in SysML
2.0 §8.2.2.1.2 (`… in inout … out … return … state … assign …`) and
`checkAttributeUsageSpecialization` (§8.3.7.3). They are kept in
`coding/errors-post-inspection.csv` and reported separately (`coding/errors-combined.csv`), with
the discovery route and verification recorded per row, so that the primary frequencies remain
pre-instrument. CODEBOOK §10 turns this into a general rule: a record may be *discovered* by any
route, but may only *enter* the taxonomy with a specification clause, a named constraint or the
model text as its basis.

This is the sharpest methodological finding of the pilot: **inspection coded 14 frozen records;
the detection run then surfaced six further real notation/typing defects (seven rows, one of which
was later withdrawn as a phantom), each verified against the specification.** **[Corrected
2026-11-13T15:10Z, A-16/A-20: the original sentence called this a two-pass human-style inspection
and a rate — "missed a third of the defects (7 of 21)" — which asserts a process the artefacts do
not show and computes a rate over a validator-surfaced arm. The counts are 6 live records against
19 in the combined population, and detection on that arm is descriptive, not recall.]** All of the
surfaced defects were mechanical notation errors that a parser finds trivially. The corollary is the opposite of reassurance for
validator-based evaluation: the same instrument is silent on a quarter of the defects it is
supposed to catch.

### 5.5 Secondary corpus check (LaVoie et al. release), n = 24

Deterministic sample: prompts 001–006 × four backends, `iteration_00` (first generation) only;
6 of the 24 files come from the repository's *negative artefacts* folder and 18 from *positive
artefacts* (the folder names are the authors', not mine). Fetched verbatim, hashes in `detection/external/manifest.json`. Because the wrapper was
stripped by the authors, only "as-is" validation is possible.

| Result | Count | Denominator |
|---|---|---|
| Validate clean under the pinned tool | 7 | 24 |
| Diagnosed, `name-conflict` present | 10 | 24 |
| Diagnosed, `syntax` present | 6 | 24 |
| Diagnosed, `usage-typing` | 2 | 24 |
| Files in the authors' *negative* folder that fail | 6 | 6 |
| Files in the authors' *positive* folder that fail **at iteration_00** | 11 | 18 |

**The important observation is a class my taxonomy does not have.** `name-conflict` — two
memberships in one namespace that are not distinguishable (`validateNamespaceDistinguishibility`,
§8.3.2.4.5) — accounts for **119 of the 140** diagnostics on the external sample and appears in
10/24 artefacts, yet **no model in my 18-model corpus produced it**. An 18-model corpus from one
generator family under-samples at least one whole class. That is a direct, counted argument for
issue #7's ≥200-model requirement, and it is also the reason I do not add a class to the codebook
on the strength of one external corpus: it is measured, not coded.

Reading the "positive folder fails at iteration_00" row requires care: those folders are cases
that *converged after repair*, and `iteration_00` is the pre-repair attempt. The number is
consistent with the authors' reported 51.16 % single-shot acceptance; it is **not** a
disagreement measurement between tools, and I do not use it as one.

---

## 6. Second coder, agreement, and what the agreement does not show

Exactly one subagent (fresh context) coded **12 of 18** models from the frozen codebook, the
models and their raw wrappers, with no access to my labels. Brief and independence limits:
`coding/second-coder/BRIEF.md`. Output: `coding/second-coder/coder-b.csv` (23 rows: 11 modelling
records + 12 W1 records). Statistics: `coding/agreement.{py,json,md}`.

| Statistic | Value | Denominator |
|---|---|---|
| Models both coders call "has ≥1 error" / "clean" | **12/12** — **[A-4: κ = 1.0 on this call is a reproduction check, not reliability; 9 of the 12 calls are exemplar-assisted, the 3 clean calls are independent]** | 12 models |
| Record-level class agreement | **11/11** — **[A-4: 8/11 paired excerpts verbatim in the coder-facing codebook, 11/11 exemplar-covered; not inter-coder reliability]** | 11 paired records |
| Cohen's κ (class) | **1.00** (pₒ = 1.00, pₑ = 0.31) | 11 pairs |
| Krippendorff's α (nominal, class) | **1.00** | 11 pairs |
| Layer agreement | 10/11 (κ = 0.87) — **[A-5: the single differing pair is S2, whose definition changed between codebook versions; version skew, not coding judgement]** | 11 pairs |
| Severity agreement | 10/11 (κ = 0.76) — **[A-5: same S2 pair; version skew, not disagreement]** | 11 pairs |

**The single layer/severity disagreement is an artefact of a codebook version, and it is
instructive.** The second coder was given the v1.0 codebook, in which S2 was a *syntax* defect
(blocking). Coder A's S2 record was later moved to *constraint* layer / *minor* after the
normative BNF showed the `by` clause is optional (codebook §9). The class id agrees; the layer and
severity follow the codebook each coder was handed. This is exactly the kind of drift a frozen
codebook is supposed to prevent, and it happened because the freeze was corrected mid-flight on
better evidence. A future run should re-issue the codebook to both coders after any correction,
and re-code.

**The W1 recording-scope difference is not a disagreement.** Both coders treat a bare fence as a
wrapper defect; they differ only in *where* it is recorded — coder B listed one W1 row per model
including bare fences, coder A counts W1 over raw artefacts only (18/18) and keeps it out of
`errors.csv` because the codebook says W1 is never coded on a normalised model. **[Corrected
2026-11-13T15:10Z, A-17: the original paragraph called this "a real and unresolved disagreement"
and `agreement-addendum.md` called it a dissent; both overstated a recording choice.]** The
modelling labels are identical either way.

### 6.1 Why κ = 1.0 is weak evidence, stated plainly

- The codebook was **built from this corpus**, and its worked examples paraphrase defects that
  occur in the 12 double-coded models. I replaced model identifiers with placeholders in the
  coder-facing copy (an amendment, disclosed in `AMENDMENTS.md` A2) so labels could not be copied
  by file identity, but recognition cannot be removed.
- The second coder is the **same model family** as the generator and as coder A — separate
  context, no shared memory, but not an independent epistemic agent. There is no human in the
  loop.
- Eleven paired records with five classes is a small sample with skewed marginals; κ is known to
  be unstable and prevalence-sensitive there. Percent agreement is reported as primary, κ as
  secondary, and no confidence interval is offered.
- **What agreement does support:** the codebook's decision rules were applied without drift to
  the same texts by a second reader, including the precedences (parse-before-resolve,
  prelude-before-dangling, no double-coding unparsed spans) and the exclusion list. **What it does
  not support:** that the classes carve nature at its joints.

**[Corrected 2026-11-13T15:10Z, A-13 — the instruction channel was undisclosed.]** The coder also
received `coding/second-coder/INSTRUCTIONS.md`, whose §6 supplied four class criteria as facts —
including the false rule that the notation requires `satisfy <requirement> by <feature>` (the `by`
clause is optional, §8.2.2.21.2). For S1, S2, T1 and R1 the agreement therefore measures
instruction-following as well as coding judgement. The surviving independent discrimination is
narrower and should be named instead: the second coder **noticed three reserved-keyword instances
that were not in its codebook** (`attribute state : String;`, `port return;` ×2) and correctly
declined to code them under the frozen text — the same gap coder A had, and the same gap the
instrument later closed. Two readers sharing a blind spot is not agreement about the world.

---

## 7. Reproduction arm — what could and could not be tested

**Not tested, and not attempted: the anchor's design.** Cibrián et al. (2025) publish 20 prompt
texts but no reference models, no code, no per-output artefacts and no parser version; Stein et
al. (2026) release nothing ("dataset available on request"). Neither generator checkpoint is
available. **I make no claim to have reproduced or refuted their 0 %/55 %/100 % figures, and any
reading of this pilot as a replication would be wrong.**

**Tested instead: the mechanism hypothesis their 0 %/100 % gap suggests.** If markdown wrapping
and preamble dominate failure, then removing the wrapper should rescue most models. In this
corpus:

| Arm | Count | Denominator |
|---|---|---|
| W1 (raw output is not a SysML file) | 18 | 18 raw outputs |
| V1: invalid **only** because of the wrapper | **6** | 18 |
| V2: invalid **after** normalisation | **12** | 18 |
| normalised and clean | 6 | 18 |

So the wrapper explanation is *available* — a pipeline that feeds raw model output to a parser
would score **0/18** here, which is the same qualitative shape as the anchor's 0 % — but it is
**not sufficient**: two thirds of the outputs remain invalid or ill-formed after extraction under
the any-diagnostic gate.

**The gate must be stated (added 2026-11-13T15:10Z, A-10/RA-02).** "Invalid" is not a property
without a gate. Under an **any-diagnostic** gate the split is **V1 = 6, V2 = 12 of 18**; under an
**exit-status** gate it is **V1 = 9, V2 = 9**, because three models (`T2-C2`, `T6-C1`, `T6-C3`)
carry an **error-severity** diagnostic while the process exits 0 ("no error that stops a check; the
notation reported above does not conform"). They are not warning-only, and an exit-status gate
alone would call them clean. The original "0/18 → 6/18 → 12/18" sentence named the steps loosely:
0/18 is raw text as a SysML file, 6/18 is normalised-and-clean under the any-diagnostic gate, 12/18
is normalised-and-diagnosed under the same gate. The
honest statement is: *in this corpus, formatting alone can produce a 0 % parse rate, but it cannot
account for the residual error population.* The anchor's anomaly remains unexplained at the
mechanism level, and this pilot cannot settle it.

---

## 8. Tensions and counter-evidence held open

1. **"The errors are mostly formatting, so the problem is prompt engineering."** Partly supported
   (18/18 raw fail; V1 = 6) and partly refuted (V2 = 12; name resolution is the largest class).
   A prompt that forbids prose (C2) did not remove defects; it changed their kind.
2. **"The errors are mostly syntax."** Not in this corpus: S1 + S2 = 4/14 frozen. The specification
   is not where these models fail most; *scope and binding* is (N1 + N2 = 6/14).
3. **"Validators make this measurable."** The instrument detects 9/14 and is silent on both
   connector records, the constraint-layer record and the documentation/value record — and it
   reports some notation errors with exit status 0. **[Corrected 2026-11-13T15:10Z, A-9: the silence
   is a composition statement, not a blind-spot measure — one record withdrawn as legal, one
   discretionary `check`, two with no normative basis and contested defect status, one contested; the
   ladder is 9/14 → 9/13[C12] → 9/12[−I1] → 9/10[−R1] → 9/9[−S2].]** A pass rate from this instrument is a measurement of
   notation plus part of resolution, not of model quality.
4. **"Two independent coders agreeing perfectly means the taxonomy is reliable."** See §6.1: same
   family, same corpus, recognisable examples, 11 records. It is a floor for the *procedure*, not
   a ceiling for the *construct*.
5. **"Error classes are task-dependent."** Not testable here — 6 tasks, 1 generation per cell, 3
   prompts per task/configuration cell at most. The C2 pattern (§1 finding 3) hints at a
   configuration effect that a task-stratified design would need to separate.
6. **A contradiction inside my own design.** I froze "errors by inspection, never by validator",
   then discovered that inspection had missed a third of the defects the validator finds. The
   resolution I chose — keep the frozen population primary, verify additions against the
   specification, report both — preserves the anti-circularity guarantee but does not make the
   original inspection sufficient. A reviewer may reasonably say the pilot should re-code the
   whole corpus in one pass with the keyword list in hand; that is the right thing to do at ≥200
   models, and it is why this is a pilot.

---

## 9. Investigation and access log (including failures and recovery)

| Target | Route | Outcome |
|---|---|---|
| Cibrián et al. artefacts (prompts file, models, code) | paper text, "data available on request" | **Not available.** No request made inside this session; a PI may legitimately request it (§10) |
| Stein et al. artefacts | paper text, "dataset available on request" | **Not available** |
| Public LLM-generated SysML v2 corpora | GitHub repo search (3 queries), GitHub code search (1), web search (3) | 0 from GitHub; **1 usable** from web search: LaVoie et al. companion repository |
| LaVoie et al. dataset release | GitHub API tree listing; 24 raw `iteration_00` files fetched via `raw.githubusercontent.com` | 200; wrapper absent by design (criterion b fails) — used as secondary check only |
| SysML 2.0 normative BNF (to settle two labels) | `https://www.omg.org/spec/SysML/2.0/Language/PDF` | **200**, 3,804,140 bytes, 691 pages, sha256 `46e6c047…4a83a`; `pdftotext` extraction; §8.2.2.1.2 and §8.2.2.21.2 read |
| Pinned validator | `.tools/sysml -validate` (v0.12.1) | Works; cache warning under sandbox recorded as harmless (TOOLING.md) |
| Second validator (OMG pilot) | — | Not usable (no JVM), per TOOLING.md §2; not attempted again |
| Syside | — | Licence boundary, out of scope (TOOLING.md §3); not attempted |

No HTTP failure required a recovery ladder beyond the corpus search; no access control was
challenged or bypassed. The one retrieval that mattered for correctness was the specification PDF:
without it, two labels (S2, and the succession-source resolution rule) would have been asserted from
memory.

---

## 10. Delegation and verification

- **One** subagent, used as second coder only (protocol §6 permits exactly this). Its brief, the
  exact set of files it received, the selection rule, and its independence limits are recorded in
  `coding/second-coder/BRIEF.md`. It confirmed it read nothing outside its directory, ran no
  validator, and spawned nothing.
- I verified its output mechanically: every non-W1 excerpt is a verbatim substring of the cited
  model line (it did this itself and I re-checked the pairs through `agreement.py`'s pairing), all
  12 models are present in `coder-b-models.csv`, and the class set it used is a subset of the
  frozen codebook's.
- **No other delegation.** No agent was used to generate corpus text (that would have hidden the
  generator/coder circularity rather than bounding it), and no agent coded outside the 12.

---

## 11. Uncertainties, limits, and what would change the answer

**Limits that bound every number here**

1. **The generator is coder A.** One model family, one session, six self-authored prompts, one
   generation per cell. No repeats, no variance, no sampling frame.
2. **n = 18 < 200.** Issue #7 cannot be closed; this is a process demonstration.
3. **The codebook is corpus-bound.** Two of its eight classes (S2 as constraint-layer, T2) were
   shaped after the instrument ran; one whole class present in an external corpus
   (`name-conflict`) is absent here.
4. **Single instrument, known gaps**, and a commercial second instrument unavailable by licence.
5. **No human expert anywhere.** Agreement is same-family agreement.
6. **Severity is a coding property, not a quality judgement**; it was not validated against
   anything.

**The three uncertainties I would most want a reviewer to attack**

1. **R1's standing.** "Connector ends over a multi-valued usage" is coded as a structural defect
   without a named constraint. If that is not an error, the total drops to 12/18 and structural
   defects vanish from the population.
2. **The S2 layer change.** Moving S2 from syntax to constraint layer, on the BNF's optional
   `by`, was right on the text; but it means the "frozen" codebook has two versions and the second
   coder used the earlier one. A stricter protocol would have re-frozen and re-coded.
3. **The wrapper convention.** Whether a bare fence is itself a W1 defect changes the W1 count
   from 18 to 4 and changes nothing else. The codebook should have decided.

**What would change the answer**

- ≥ 200 models per issue #7, with repeats and at least two generator families: the class
  distribution, and possibly the class set, would change (the external sample already suggests a
  missing class).
- A held-out corpus from a different generator and task author, with the codebook applied
  unchanged and agreement recomputed: that would test whether the classes travel.
- A human systems engineer coding 20 models: that would establish whether these are the defects
  an expert cares about, which nothing here does.
- A second validator (Syside, or the OMG pilot with a JVM): that would separate "instrument
  property" from "error property" in the detection table.

---

## 12. Dead ends and things that did not pay off

- **Three GitHub repository searches and one code search** for a generated-SysML corpus: zero
  results; the artefact-release route (web search → arXiv → companion repo) is what worked.
- **Using the external corpus for taxonomy frequencies:** impossible, because its wrapper was
  stripped; the attempt is recorded rather than stretched.
- **`first start;` as a validator-detectable defect:** the tool is silent, and a probe confirmed
  the silence is specific to succession sources, not to resolution in general. The record stands
  on the grammar (`InitialNodeMember … memberFeature = [QualifiedName]`), not on the tool.
- **Treating exit codes as validity:** abandoned after probe07 showed a notation error reported
  with exit 0.
- **Attempting to state a per-configuration effect:** 6 models per configuration, one generation
  each; the C2 pattern is reported as a hypothesis and nothing more.

---

## 13. Implications for the main question

1. **"Does it parse?" is the wrong dependent variable, and so is "does the validator pass?"** In
   this corpus, the same 18 outputs move from 0/18 (raw text) to 6/18 (normalised and clean under an
   any-diagnostic gate) to 12/18 (normalised and diagnosed), and to 9/9 under an exit-status gate,
   depending only on whether the wrapper is stripped and which gate is read.
   **[Corrected 2026-11-13T15:10Z, A-10/RA-02: the original stated three numbers without naming the
   step or the gate.]** Any evaluation that reports a single validity
   percentage without stating the extraction rule and the gate is not comparable with another one
   — which is exactly the state of the published literature (`evidence/literature.md` §4.8).
2. **The error population is not where the field's metrics are looking.** Name resolution and
   binding dominate here; the structural and semantic records are few and contested, and **no
   diagnostic is returned on them under the invocation run, and no surface tested decides a
   documentation/value contradiction**. **[Corrected 2026-11-13T15:10Z, A-23: the original said
   "invisible to the instrument", which is invocation-unspecific and is contradicted by the verdict
   path.]** A benchmark built on validator pass rates would score the four dangling
   `satisfy` models as failures only if the tool happens to resolve them, and would score the
   multi-valued connectors as passes.
3. **The three-way separation this pilot enforces — wrapper, notation, resolution, semantics — is
   cheap and reusable.** It is what made V1/V2 computable and what exposed the inspection gap. A
   200-model study could run the same pipeline, and should add a class the corpus here cannot
   show (`name-conflict`).
4. **For architecture claims (repair loops, RAG, structure-imposing prompts), the pilot supplies a
   caution rather than a result:** a repair loop driven by this instrument would not see the
   dangling succession source, the unbounded `satisfy`, the multi-valued connector or the
   documentation contradiction. Reporting "100 % valid after repair" against such an instrument
   would be a statement about the instrument's scope.

---

## 14. Adjacent questions noticed and **not** researched

- **#10 (semantic ceiling):** whether *any* mechanism can check a connector's intent, a
  documentation/value contradiction, or reachability of a state machine. My detection table says
  no mode I tested returns a defect verdict for the four semantic/structural classes — and
   reachability is observable in a visited-state trace even though it is not checked — I made no attempt to
  characterise the ceiling beyond that.
- **#8 (validator reliability):** the pilot produced a small, real fault set with pre-registered
  expectations (14 frozen records + 7 verified additions) that could serve as an external
  challenge set. I did not evaluate validator sensitivity/specificity; that is #8's question and
  Researcher B's task.
- **#6 (structure-imposing strategies):** the C2 pattern is suggestive but n = 6; not researched.
- **#9 (fidelity):** the corpus deliberately excludes prompt-fidelity judgements; the T1-C3
  "75 % vs 55 %" record was kept as an internal contradiction only.
- **#13 (benchmark design):** the missing `name-conflict` class in an 18-model corpus is a
  data point for corpus sizing; not pursued.

---

## 15. Sources

**Project artefacts (this pilot, all under `research/issue-007/` unless stated)**

- `METHODOLOGY-FROZEN.md` (sha256 `269d8dbe…64f76`), `AMENDMENTS.md` (A1–A6)
- `corpus/prompts.md`, `corpus/manifest.csv`, `corpus/extraction-log.json`,
  `corpus/normalized/*.sysml`, `raw/*.md`
- `coding/CODEBOOK.md` (v1.2 `d2019448…76766`; **v1.4 `91f963bf…94b9`** after Gate-4 corrections), `coding/errors.csv`, `coding/models.csv`,
  `coding/omissions.csv`, `coding/errors-post-inspection.csv`, `coding/errors-combined.csv`,
  `coding/indicators.json`, `coding/agreement.{py,json,md}`,
  `coding/second-coder/{BRIEF.md,INSTRUCTIONS.md,coder-b.csv,coder-b-models.csv}`
- `detection/{run_detection.py,diagnostics.csv,summary.csv,table.md,raw/*.txt,probes/*.sysml,
  external/manifest.json}`
- report: `reports/issue-007-error-taxonomy-pilot.md`

**Specification and project evidence**

- OMG SysML 2.0 Language Specification, `formal/2026-03-02`
  (<https://www.omg.org/spec/SysML/2.0/Language/PDF>), retrieved 2026-11-13, 691 pp., sha256
  `46e6c0476a6f1f34f367d57e039d56659bff75e41d2e4b3d37ca4cadea84a83a`. Clauses used: §8.2.2.1.2
  (reserved keywords), §8.2.2.17 (action/succession notation), §8.2.2.21.2
  (`SatisfyRequirementUsage`), §8.3.7.3, §8.3.21.10.
- `catalogue/classified.csv` (623 constraints; clause + obligation + dependency class),
  `catalogue/coding/codebook.md` (prior art for the frozen-codebook + agreement procedure).
- `evidence/spec-tooling.md` §3.3, §4.1, §5.5, §6.1; `evidence/literature.md` §1.5, §1.7, §2.5,
  §3.1, §3.2, §4.
- `research/relational/PROTOCOL.md` (§3 evidence rules, §6 tooling, §7 anti-circularity),
  `research/relational/TOOLING.md` (§1 pinned validator, §2–3 unavailable instruments).

**External corpus (secondary check only)**

- LaVoie, C., Andujar Lugo, E., Topcu, T. G., Kara, L. B. (2026). *Natural-Language to SysMLv2
  Translation via Conformance-Driven Iterative Refinement.* arXiv:2607.14162; ASME IDETC/CIE 2026.
  <https://arxiv.org/abs/2607.14162>
- Companion repository, `Open-Source Dataset Release` tree (151 prompts, 604 cases, 1,043
  artefacts): <https://github.com/cmuchancel/NL-to-SysMLv2-via-Conformance-Driven-Refinement>
  (24 files fetched, hashes in `detection/external/manifest.json`).

**Prior anchors (read via the project's evidence note, not re-read here)**

- Cibrián, Olivert-Iserte, Llorens, Álvarez-Rodríguez (2025), *Computers in Industry* 172:104350,
  DOI 10.1016/j.compind.2025.104350.
- Stein et al. (2026), *AI* 7(8):274, DOI 10.3390/ai7080274.

---

## 16. Post-review corrections (Gate 2) — added 2026-11-13T14:28Z

Reviewer B's review (`research/relational/cross-reviews/B-reviews-A.md`, 13 objections: 0 blocking,
8 material, 5 minor) was tested against the artefacts by the author. Every objection is answered
with a ruling in
[`A-response-to-B-review.md`](../research/relational/cross-reviews/A-response-to-B-review.md); this
section records only **what changed in this report's numbers**, old value first, new value second.
Nothing above this section has been deleted or rewritten, per `PROTOCOL.md` Amendment A1.

**Convention (added 2026-11-13T15:10Z, A-2).** `coding/errors.csv` is **immutable**: corrections are
written to `coding/errors-corrections.csv` (C01–C16) and applied to `coding/errors-combined.csv` by
`coding/apply_corrections.py`, which also refuses any row whose excerpt is not a verbatim substring
of its model. `errors.csv` and `errors-post-inspection.csv` keep the bytes Reviewer B pinned; the
detection table reads `errors.csv` for the primary arm and `errors-combined.csv` for the secondary
one, so a reader can always tell which version produced a row. The frozen
population file `coding/errors.csv` is byte-identical to the one Reviewer B pinned; corrections live
in `coding/errors-corrections.csv` and are applied to `coding/errors-combined.csv` by
`coding/apply_corrections.py`, with the reconciliation table in `coding/reconciliation.md`.

### 16.1 Summary of every number that changed

| Claim (section) | As first published | Corrected | Cause |
|---|---|---|---|
| Post-inspection records (§1, §5.4) | 7 | **6 live** (7 rows, 1 withdrawn) | B-O1: `T5-C3-P01` cites `port return;` at line 26 of a model with no port declaration. Verified: `T5-C3.sysml` has no `port` token except inside `import` on line 2; line 26 is `part antenna : Antenna;`. The row duplicated `T6-C1-P01`. |
| Combined population (§1, §5.4) | 21 records / 15 models | **20 records / 15 models** (3 clean) | the withdrawal above; `T5-C3` remains affected through `T5-C3-P02` (`attribute window : VisibilityWindow;`, line 11, real and tool-confirmed) |
| Combined class count S1 (§5.4) | 9 | **8** | withdrawal of the phantom S1; no other class changes |
| Combined detection (§5.4) | 15/21 = 71 % | **15/20 = 75 %** | the only withdrawn record was itself undetected; the rise is arithmetic, not a discovery |
| Errors per model, range (§1) | 0–3 | **0–2** | B-O7: maximum `n_errors` in `models.csv` is 2 (T3-C2, T4-C1) |
| W1 under a prose-only reading (§11.3) | "18 to 4" | **18 to 7** | B-O7: preamble in 4 raws, trailing prose in 6, union 7 (T1-C1, T2-C1, T3-C1, T4-C1, T5-C1, T5-C2, T6-C1) |
| Frozen records' layer attribution (§1) | structural 2, typing 1 | **structural 0, typing 3** (in `errors-combined.csv`; `errors.csv` keeps the original labels because it is immutable) | B-O8: R1's operative condition is end-feature multiplicity conformance, re-recorded as `type/typing`; the architectural reading is the rival, not the label |
| Frozen detection (§1, §5.1) | 9/14 = 64 % | **unchanged 9/14**, plus **9/13 = 69 %** on the 13 uncontested records | B-O9: I1 is contested (see 16.3) |
| Agreement, class (§6) | "11/11, κ = 1.0" as reliability evidence | **κ = 1.0 is not reliability evidence**: 8/11 paired excerpts verbatim in the coder-facing codebook, 11/11 exemplar-covered | B-O5 |
| Agreement, presence (§6) | "12/12" | **3 independent clean calls + 9 exemplar-assisted calls** | B-O5 |
| Agreement, layer/severity (§6) | "10/11, κ 0.87 / 0.76" | **version skew, not disagreement** (the one differing pair is S2, whose definition changed between codebook versions) | B-O6 |
| External arm (§5.5) | "11 of 18 positive-folder files fail at iteration_00" | **2/18 error-level (exit 2), 9/18 warning-only (`name-conflict`, exit 0), 7/18 clean**; negative folder 6/6 error-level | B-O12 |
| Comparison to the authors' 51.16 % (§5.5) | implied comparison | **withdrawn** — the sample is `iteration_00` of cases selected as ultimately convergent, not a random single-shot sample, and the gate is a different instrument | B-O12 |
| "frozen and hashed before detection" (§1, Proposition 1) | hashed | **withdrawn as an evidentiary claim**: no hash artefact of `errors.csv` exists | B-O4 (16.2) |
| S1 constraint citation (§4.1) | `checkSatisfyRequirementUsageBindingConnector` | **`SatisfyRequirementUsage` production, §8.2.2.21.2**; transitions → **§8.2.2.18** | B-O10 |
| Detection unit (§5.1) | record-level only | record-level **plus** `detection/occurrence_detection.csv` for the four multi-occurrence records | B-O11 |
| Detection provenance (§5) | argv + exit only | **`detection/manifest.json`**: per-file sha256, tool sha256/version, argv | B-O13 |

### 16.2 The freeze-evidence claim is withdrawn (B-O4)

The report said the frozen population was "frozen and hashed before detection". **I cannot produce a
hash of `errors.csv` taken before the detection run, and no such hash exists in the artefacts**
(`FREEZE-HASH.txt` holds the methodology; `CODEBOOK-HASH.txt` the codebook). I therefore withdraw
the claim as an evidentiary statement rather than defend it.

What actually happened, as best I can reconstruct it: `labels.py` wrote `errors.csv` at 14:12Z; one
label was changed at 14:14Z (S2, after the BNF retrieval); a sessional `shasum` of the then-current
file was printed at 14:11:48Z for the *earlier* content and was never written to a file; the
detection run followed; and at 14:17Z I re-ran the whole pipeline to check determinism, which
rewrote `errors.csv` with identical bytes. That re-run is why `errors.csv`'s mtime coincides with
`detection/*.csv` — the mtime ambiguity is mine, not the reviewer's error. A hash taken once, at the
moment the codebook was frozen, would have settled this; that is the mechanism the protocol asks
for and I did not use it.

**Strongest remaining evidence that labelling preceded detection** (inferential, and I label it as
such):

1. **The composition argument, with specifics.** The frozen 14 omit exactly the defects the
   instrument flags most cheaply — `port out;` (T3-C2:24), `attribute state : String;` (T2-C2:17),
   `action def assign;` (T4-C1:49) — and include three records on which the instrument is wholly
   silent (R1 ×2, I1) plus one silent sub-mechanism (`first start;`, T1-C1:64). A post-detection
   labelling pass would show the opposite composition.
2. **The existence and content of the post-inspection file.** `coding/errors-post-inspection.csv`
   (hash `285d70ea…`, written after the detection run) records each of those notation defects with
   `discovery_route = "detection run surfaced the candidate (NOT the criterion)"`. If the frozen set
   had been written from the tool, there would be no separate later arm to attribute.
3. **The frozen record for T3-C2 names line 33 (`line.in`) but not line 24 (`port out;`), although
   the tool flags 23 and 24 and not 33.** That is the fingerprint of a reader following a mechanism
   through the text, not of a reader copying diagnostics.

These are arguments, not evidence of the kind a hash is. The report's Proposition 1 ("established
for this corpus") should now be read as: the population is *frozen*, its content is internally
consistent and re-derivable from `labels.py`, and the ordering is supported by the three
observations above — not as "hashed before detection".

### 16.3 I1 is contested, and the denominator is reported both ways (B-O9)

Reviewer B's rival reading of `T1-C3` is accepted as live: a documentation band of 35–75 % *contains*
the declared 35–55 % bound, so a tightened engineering limit is not contradictory on its face. The
record is **not withdrawn** — it was fixed before detection, and withdrawing a record on review
because the review shows it improves a rate would be exactly the self-serving move the protocol
forbids — but it is marked `frozen_contested` in `errors-combined.csv`, and the detection result is
reported on both denominators, with unique labels: **9/14 = 64 % (all frozen records)** and
**9/13[−I1] = 69 % (14 − I1)**. This is a different 9/13 from the post-C12 9/13[C12] = 14 − T1-C1
(A-19). Either way the instrument is silent on it.

### 16.4 What the structural claim becomes (B-O8) **[superseded in part by §18, A-6/RA-03: R1 is contested as to defect status, not only layer]**

With R1 re-recorded as `type/typing`, the frozen population contains **no record the report can
defend as architectural**. The instrument is still silent on all three affected records (two R1, one
I1), so the claim that survives is narrower and stronger: *the instrument reported nothing on the two
connector records and the one documentation/value record, whatever layer they are placed at.* The
earlier sentence in §1 and §13 that the corpus contains "structural and semantic defects" should be
read with this correction: it contains two records whose layer is contested between `type/typing`
and `structural/architectural`, and one semantic record that is contested as a defect at all.

### 16.5 Agreement (B-O5, B-O6): the corrected sentence

κ = 1.0 must not be quoted as inter-coder reliability for this taxonomy. The codebook built from the
corpus contained, in de-identified form, the text of 8 of the 11 paired records verbatim and the
mechanism of the other 3, so class agreement is largely reproduction. **[Corrected
2026-11-13T15:10Z, A-13/A-17: (i) the coder also received `coding/second-coder/INSTRUCTIONS.md`,
which supplied four class criteria as facts — one of them false (that the notation requires
`satisfy <requirement> by <feature>`; the `by` clause is optional) — so for S1, S2, T1 and R1 the
agreement measures instruction-following as well as judgement; (ii) the "dissent on the W1
convention" is withdrawn: both coders treat a bare fence as W1 and differ only in where it is
recorded.]** What survives independently: the three clean-model calls (no exemplar exists for "no
defect"), the coder's independent noticing of three reserved-keyword instances absent from its
codebook, and the verbatim-substring verification of its excerpts. A real reliability test — a held-out set with the
examples redacted — has not been run; the 24 external artefacts on disk are the cheapest candidate.
The full correction is appended to `coding/agreement.md` (dated addendum) rather than rewriting the
statistics.

### 16.6 External arm (B-O12): like-for-like or nothing

"11 of 18 positive-folder files fail" conflated error severity with any diagnostic. Corrected:
**2/18 error-level (exit 2)**, **9/18 warning-only** (all `name-conflict`, exit 0), **7/18 clean**;
the negative folder is **6/6 error-level**. The 51.16 % comparison is withdrawn rather than repaired
because no repair is possible: those 18 files are `iteration_00` of prompt×backend cases the authors
selected *because they converged*, at a different gate, so they are not a single-shot acceptance
sample. The descriptive split is retained; the comparison is not.

### 16.7 Minor corrections applied

- **B-O7:** range 0–2 (not 0–3); prose-only W1 reading 7 (not 4); `trailing_prose_present` is now a
  column in `coding/models.csv` (values from `corpus/extraction-log.json`).
- **B-O11:** `detection/occurrence_detection.csv` records, for the four multi-occurrence records,
  how many occurrences the tool flagged: T2-C1 4/4, T3-C1 9/9, T3-C2 2/3, T4-C1 1/2. The
  record-level column in §5.1 is therefore an upper bound for T3-C2 and T4-C1.
- **B-O13:** `detection/manifest.json` (from `detection/make_manifest.py`) carries the per-file
  sha256, tool sha256/version and argv; `detection/raw/*.txt` are unchanged and still carry the
  verbatim output.
- **B-O2/O3:** the reconciliation table (§16.1 and `coding/reconciliation.md`) settles which record
  carried which occurrence and span. The frozen `T4-C1-E01` span 42-44 is corrected to 42-43 in the
  combined population only; `then assign;` is recorded under the S1 record `T4-C1-P02`.

### 16.8 What did not change

**[Partially superseded by §17 and §18 (2026-11-13T15:10Z, A-1): the frozen file is unchanged, but
the population is 13 records / 11 models / 7 clean after C12 and the combined arm is 19, not 21. The
paragraph below records what §16 had not yet touched.]**

The frozen 14-record population; 12 models with ≥1 error and 6 clean models in it; the V1/V2
wrapper result (18/18 raw fail, 6/18 invalid only because of the wrapper, 12/18 invalid after
normalisation); 9/14 detection on the frozen records; the finding that inspection missed seven
mechanical notation defects that the tool finds; and the external descriptive counts (7/24 clean,
10/24 `name-conflict`, 140 diagnostics of which 119 `name-conflict`). The last of these is now
reported as a warning-level phenomenon, not as a failure rate.

---

## 17. Post-closure evidence corrections — added 2026-11-13T14:32Z

Reviewer B sent two corrections after Gate 2 closed. Both are accepted; the register entries are C12
and C13 in `coding/errors-corrections.csv`, the reasoning is `AMENDMENTS.md` A7, and no frozen file
was edited.

### 17.1 `first start;` is legal SysML 2.0 — `T1-C1-E01` is withdrawn (C12)

B's probe suggested that `Action` has an inherited member `start`. Checked at source: the normative
Systems Library declares, at line 43 of `sysml.library/Systems Library/Actions.sysml` (sha256
`ac36c940…5693`), `action start: Action :>> startShot`. Every Action therefore inherits a `start`
action, and `first start;` inside an action definition resolves; it is not a dangling reference. The
record's stated basis is false and it is **withdrawn**. B declined to relitigate it; the withdrawal
is mine, on the library text.

| Population | Records | Models affected | Clean models | Frozen-record detection |
|---|---|---|---|---|
| as first published (`errors.csv`, untouched) | 14 | 12 | 6 | 9/14 = 64 % |
| with C12 applied | **13** | **11** | **7** (`T1-C1` had no other record) | **9/13[C12] = 69 %** |
| with C12 and excluding contested I1 | 12 | 10 | 8 | 9/12[−I1] = **75 %** |
| combined arm, as first published | 21 | 15 | 3 | 15/21 = 71 % |
| combined arm, corrected (C01 + C12) | **19** | **14** | **4** | **15/19 = 79 %** |

**Read this as a warning, not a result.** Every correction in this pilot moved the detection rate
upward, because the records removed were ones the instrument did not catch. A 64 % → 69 % → 75 %
progression produced by post-hoc corrections of a 14-record population is not a stable estimate of
anything; it is a demonstration that small-n rates are hostage to individual records. The original
figure is shown alongside every corrected one for that reason.

Why this is treated differently from I1 (kept, contested): I1 has two defensible readings, so
withdrawal would be my preference among readings; `T1-C1`'s record rested on a factual claim about
the language that the normative library contradicts, so keeping it would be wrong whichever way the
rate moved.

### 17.2 The construct census said 0/18 for ISQ/SI; it is 3/18 for SI (C13)

`grep -l "import SI::*"` matches `T3-C2`, `T3-C3`, `T5-C1`; none imports ISQ, and **none writes a
unit literal** (`[kg]`, `[m]`, …). The §5.5 objection to B's F6 fault material is restated correctly:
*3/18 models import SI, 0/18 import ISQ, 0/18 write a unit-typed quantity* — importing a unit
library without a unit literal does not make a model unit-checkable, so the substance holds while the
"0/18" phrasing was wrong. The correction is registered rather than edited into the closed
cross-review (`A-reviews-B.md` stays byte-identical).

---

## 18. Gate-4 adjudication — applied corrections, item by item — 2026-11-13T15:12Z

The independent adjudicator's rulings (`research/relational/adjudication/ADJUDICATION.md`,
`rulings.json`, `CORRECTIONS.md` Part 1) were applied to this report and to my artefacts. The report
above keeps its original text; each correction is a dated inline marker or an entry here. The
per-item working record, including the two items I dissent from, is
[`research/issue-007/ADJUDICATION-RESPONSE.md`](../research/issue-007/ADJUDICATION-RESPONSE.md).

| # | Ruling | What changed | Old → new |
|---|---|---|---|
| A-1 | RA-01, RA-06, B2A-01, B2A-08, B2A-15 | CURRENT NUMBERS table added at the top; banner, §1 table and §16.8 marked as superseded; unique denominator labels | frozen 14/12/6 → **13/11/7** `[C12]`; combined 21 → **19**; S1 9 → **8**; range 0–3 → **0–2**; W1 prose-only 4 → **7** |
| A-2 | B2A-03 | Convention statement in §16: `errors.csv` immutable, corrections in `errors-corrections.csv`, applied to `errors-combined.csv` | new text; no number |
| A-3 | B2A-05 | "frozen and hashed before detection" withdrawn in the banner, §2 Proposition 1 and §16.2; ordering restated as the composition argument, labelled inferential | hashed → **not hashed; argued** |
| A-4 | B2A-06, RA-05 | §6 table rows, §6.1, §16.5 and the README no longer quote κ as reliability; 8/11 verbatim, 11/11 exemplar-covered stated | reliability → **reproduction check** |
| A-5 | B2A-07 | §6 layer and severity rows annotated as version skew; S2 pair footnoted | unchanged numbers, corrected reading |
| A-6 | RA-03, B2A-09, X-03 | R1 marked **contested as to defect status** (not only layer) in the codebook, C14/C15 and §16.4; criterion restated with the contested step named | R1: layer-contested → **defect-contested** |
| A-7 | B2A-10 | Codebook: `status ∈ {frozen, frozen_contested, post_inspection}` added to the record schema and to I1's definition | new status field |
| A-8 | B2A-12, RA-10 | `detection/occurrence_detection.csv` gains `T6-C2-E01` (3 occurrences, all flagged); §5.1 states the record-level column is an upper bound for T3-C2 and T4-C1 | +1 occurrence row |
| A-9 | RA-01, CC-04 | §1 finding 2, §5.1 ladder, the §8 tension and §13.2 now give 9/14 → 9/13[C12] → 9/12[−I1] → 9/10[−R1] → 9/9[−S2] with the composition | blind spot → **composition statement** |
| A-10 | RA-02 | Gate stated in §1 finding 2, §7 and §13.2: 6/12 and 12/18 under an any-diagnostic gate, 9/9 under an exit-status gate; the three exit-0 error-severity models named (not warning-only) | one split → **two gate readings** |
| A-11 | RA-03, RA-14 | `FROZEN-SUBSET-ADDENDUM.md` marks T4-C1-E02 and T4-C3-E01 contested as to **defect status** and restates the summary as "4 controls + 3 descriptive models"; `subset.json` is not edited (B's run is pinned to those bytes) | 7 controls → **4 controls + 3 descriptive** |
| A-12 | RA-04 | Codebook class table and bodies corrected with dated superseded markers (S1 citations, R1 layer, S2 body); no-re-establishment statement added; re-hashed | v1.3 → **v1.4** |
| A-13 | RA-05 | The second coder's instruction sheet is disclosed in §6.1 and §16.5, including the false `by` rule; reserved-keyword notices named as the surviving independence | undeclared channel → **declared** |
| A-14 | RA-06, RA-12 | README: codebook hash corrected, N1 5 → **4** after C12, unique denominator labels, current numbers table | index corrected |
| A-15 | RA-07 | `CROSS-REVIEW-HASH.txt` is now an **append-only ledger**, one row per write with its own time; post-edit bytes are not labelled with an earlier freeze time | ledger reformatted |
| A-16 | RA-08 | §5.4 and this section report **counts** (6 live post-inspection records, 15/19 descriptive), not a "missed a third (7 of 21)" rate | rate → **counts** |
| A-17 | RA-09, RA-05 | W1 "disagreement"/"dissent" withdrawn in §6, §16.5 and `agreement-addendum.md`; it is a recording-scope difference | disagreement → **recording choice** |
| A-18 | RA-11 | `coding/agreement.py` computes presence κ (pₒ = 1, pₑ = 0.625, κ = 1) and the false comment is gone; `agreement.json` regenerated | None → **κ = 1.0 computed** |
| A-19 | RA-12 | Unique labels **9/13[C12]** vs **9/13[−I1]** in §16.3/§17.1; models.csv column `n_errors_post_inspection` → **`n_errors_combined`** | duplicate label → **unique** |
| A-20 | RA-13 | "81 `syntax` diagnostics" → **81 diagnostics (72 `syntax` + 9 `reserved-keyword-name`)**; "two-pass human-style inspection" replaced by the recorded passes (open pass, `inspect.py` indicators, coding pass) | miscount corrected |
| A-22 | CC-01 | §5.3 no longer attributes the OMG pilot's limitation to this binary: "the default `-validate` invocation reports nothing on these records, and no invocation I ran returns a defect verdict" | scope justification withdrawn |
| A-23 | CC-02 | §13.2 no longer says "invisible to the instrument": no diagnostic under the invocation run, and no surface tested decides a documentation/value contradiction | wording narrowed |
| A-24 | CC-03 | §14 no longer says the pinned instrument "cannot" check reachability: no mode returns a verdict, the condition is observable in a visited-state trace | wording corrected |
| A-21 | RA-14 (rejected; optional relabel only) | The subset summary line is relabelled in the addendum only | cosmetic |
| (B2A-04) | **ruled REJECTED — not an A-item** | No change: B's claim that line 42 is "not visibly defective" is contradicted by `InitialNodeMember … memberFeature = [QualifiedName]`; the adjudicator rejected it, so no correction is carried | none |

**Numbers after all corrections (current):** frozen file 14 records / 12 models / 6 clean
(unchanged, `30265ff5…`); **frozen population 13 / 11 / 7** `[C12]`; combined **19 records / 14
models / 4 clean**; frozen detection **9/14 = 64 %**, and **9/13[C12] = 69 %**, **9/12[−I1] = 75 %**,
**9/10[−R1] = 90 %**, **9/9[−S2] = 100 %**; combined detection **15/19 = 79 %, descriptive**;
V1/V2 **6/12 (any diagnostic)** or **9/9 (exit status)**; agreement κ = 1.0 **as a reproduction
check only**.
