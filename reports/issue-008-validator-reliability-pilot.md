# Validator reliability pilot: mutation-based evaluation of one open SysML v2 validator

**Issue:** [#8](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/8) — *How reliable are
SysML v2 validators as measuring instruments?*
**Status:** **PRELIMINARY PILOT. It does not close #8 and cannot.** Issue #8's own "what would count as
convincing evidence" asks for a second coder on mutant validity, a mutant corpus validated against
observed generation errors, and a second instrument. This pilot delivers the method, a published
corpus, and a first calibrated set of numbers for **one** instrument; it delivers none of those three.
**Author:** Researcher B (independent agent, own context).
**Instrument:** OpenSysML CLI `sysml v0.12.1`, commit `b2f0e9b8…`, binary sha256
`ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0`.
> **ADJUDICATED CORRECTIONS (Gate 4, 2026-11-13T15:10Z) — READ BEFORE QUOTING THIS REPORT.**
> The adjudicator (`research/relational/adjudication/`) accepted **35 corrections** to this report.
> The originals are kept visible throughout (PROTOCOL.md Amendment A1); each correction is in
> **Addendum A11** below, and the headline pages carry inline pointers to it. The four sentences most
> often quoted are **superseded** and their corrected forms are:
> (i) §1 *"no evidence at all about whether the model's structure means what it claims"* → the
> default `-validate` path only; the verdict path decides asserted conditions (**B-1**);
> (ii) §11.1 *"for four out of four structural defects tested it means nothing at all"* → three of
> four return no verdict and the fourth is decided only where the requirement encodes a constraint
> (**B-29**);
> (iii) §2 P3 *"invisible to the only available instrument — Established"* → corrected by A2
> (**B-30**);
> (iv) §3.5 *"an empty range is not obviously ill-formed"* → `[4..2]` is empty and therefore
> unsatisfiable, so the count stands and the wording was what had to go (**B-13**).
> Three structural caveats also apply to every number here: the per-class picture is **confounded
> with the obligation the specification attaches to each condition** and the layer reading is held as
> one of two (**B-33**); the expectation audit is **informed, not blind** (**B-7/B-14**); and the
> known-good arm is **not independent** of the mutant arm (**B-22**).

**Evidence base:** `research/issue-008/` (frozen methodology, corpus, mutants, raw validator output,
triage, analysis). Every number below is recomputable from `results/raw/run1/` with
`harness/analysis.py`.

> **Read this first.** Every rate in this report is a calibration of *that binary at that version,
> against 32 synthetic mutants derived from 10 small models authored by the same agent that wrote
> the expectations*. It is **not** "the false-negative rate of SysML v2 validators". The second
> instrument (the OMG reference implementation) was not obtained — it publishes no CLI artefact and
> no JVM is installed — so the one-instrument limitation is not a caveat, it is the boundary of what
> this pilot measured.

---

## 1. Answer

**In one paragraph.** Against 32 single-defect, specification-derived mutants, the pinned
OpenSysML validator detected **23/32 (0.72, 95% Wilson [0.55, 0.84])** at error severity, and
identified the injected defect in a further 2 cases only at warning severity. It was perfect on the
two layers it advertises first (syntax 4/4, name resolution 4/4) and on metadata mis-typing (4/4),
and it caught things the specification does **not** name (an inverted multiplicity range, a
dimensionally impossible product). It **detected none of the four structural/architectural defects**
(0/4, [0.00, 0.49]): an unreachable state, a `satisfy` link whose requirement is false, a missing
data flow, and two contradictory assertions all validated cleanly. One *named, SHOULD-report*
constraint was silently missed (KerML `validateFeatureValueOverriding`), and two kind-mismatch
defects produced either a warning about a different condition or a warning five lines away from the
defect. On the known-good arm it produced **0 error-severity false positives in 10 models** and one
warning that a specification-verbatim example does not deserve.

**What a pass means, calibrated.** For this instrument and this corpus, a clean validation is
evidence about notation, names, typing and per-constraint well-formedness — and it is **no evidence
at all** about whether the model's structure means what it claims.
**[Superseded for the instrument as a whole — see A11.1 / B-1. True of the default `-validate`
invocation, which is what this pilot ran; `-satisfy`, `-instantiate … -validate=` and the engine
modes decide asserted conditions, and A2 records that correction. The corrected sentence is: *the
default path is no evidence about structural meaning; the verdict path decides exactly those
conditions the model itself encodes.*]** That is the short answer to the
main question's validation half.

**Frozen pre-registration** (quoted before the first validator run over the corpus, so no
expectation could be fitted to a result):

| artefact | sha256 |
|---|---|
| `research/issue-008/METHODOLOGY-FROZEN.md` | `2c80d63e8800be9ca67a051aaffdbc4b6c56c1b576002fc4446fe82862e6f00b` |
| `research/issue-008/mutants/MANIFEST.csv` (expectations) | `a9f479748aea10c76460421031a384ddda779d4c78ea1cb6a5fe2f208f157be7` |
| `research/issue-008/harness/author_manifest.py` | `40c75cef580464e69c854823dbfb0a942ad178cb0f8c89b0a0f41c370e484432` |
| `research/issue-008/harness/make_mutants.py` | `see mutants/expectations.sha256` |
| 32 mutant files | `see mutants/mutants.sha256` |

The methodology hash was computed at 14:08Z and the manifest hash at 14:13Z on 2026-11-13; the first
run over the corpus is `results/run-log-run1.md`. No expectation was revised.

## 2. Status of the propositions

| # | Proposition | Status on the retrieved evidence |
|---|---|---|
| P1 | The instrument detects notation and name-resolution defects essentially completely | **Established for this corpus** (8/8; the 4 syntax and 4 unresolved mutants all error-detected, with plausible hints) |
| P2 | Detection falls away as the fault moves from mechanism to meaning | **Established for this corpus** — 1.00 / 1.00 / 0.50 / 0.75 / 0.75 / 0.75 / 0.00 / 1.00 by class. The monotone reading is *not* clean (F8 metadata scores 1.00), so the claim is "the mechanism layers are near-perfect and the architectural layer is blind", not "sensitivity decreases monotonically" |
| P3 | At least one class of plausible model defect is invisible to the only available instrument — **corrected by A2, and further corrected by A11.1: see there; the form below is the original and is superseded** | **Established for the default `-validate` path** (original: "Established" — F7 0/4, all four silent); across all modes tested it is 1 violated / 1 undecided / 2 no verdict, and none of the four is named by a constraint in the 623-row catalogue or the 38-row prose-only register |
| P4 | Some specification-named SHOULD constraints are not enforced | **Established for at least one** — KerML `validateFeatureValueOverriding` (§8.3.4.10.2, class A, SHOULD) was missed; and `validateFeatureEndMultiplicity` (§8.3.3.3.4, SHOULD) fired only as a *warning* |
| P5 | The instrument enforces conditions the specification does not name | **Established** — the inverted multiplicity range `[4..2]` was reported as an **error** although no catalogue constraint forbids it, and dimensional consistency (nothing in the catalogue names it) was enforced to a level that caught a wrong *product* dimension |
| P6 | Therefore validator pass rates in the literature measure less than they claim | **Not established here.** The logical step requires the external challenge set (issue #7's observed error population) and the corpus-representativeness study. This pilot supplies the instrument calibration that such a claim would need; it does not make the claim |
| P7 | These numbers are a property of "SysML v2 validators" | **Not established and not claimed** — one instrument, version-pinned, no second measurement |
| P8 | The fault model is representative of real GenAI generation errors | **Not established** — the fault model is specification-derived by design; representativeness is exactly what Researcher A's frozen subset is for (later phase, out of scope here) |

## 3. Evidence

### 3.1 Design in one table

| Element | What was done |
|---|---|
| Fault model | 8 classes derived from `catalogue/classified.csv` (623 named constraints), `catalogue/prose-only-names.csv` (38 prose-only names) and `evidence/spec-tooling.md` §3.3/§6 — not from the instrument |
| Mutants | 32 = 8 classes × 4, each **one** injected defect in one of 10 known-good bases, regenerable with `harness/make_mutants.py` (which asserts each substitution matches exactly once) |
| Expectations | `mutants/MANIFEST.csv`, authored from the specification and model text only, hashed before the run: 24 expected detectable, 6 expected not, 2 uncertain; 3 flagged as having a conspicuous surface tell |
| Known-good corpus | 10 models, 9 of them quoting the pinned SysML 2.0 PDF (`formal/2026-03-02`, sha256 `46e6c047…a84a83a`), each with a `PROVENANCE.md` giving a **constraint-level** validity argument and listing which declarations I supplied |
| Instrument | OpenSysML `sysml -validate -format json`, exit codes and full argv recorded per case in `results/run-log-run1.md` |
| Measures | Fixed before the run: relevant error-severity detection (primary), any-error, any-signal, wrong-severity, misleading, incidental, silent; Wilson 95% intervals on every proportion. **Corrected by A11.4 (B-2):** the verdict path's five standings (`holds` / `holds-vacuously` / `violated` / `undecided` / `no assertion`) and the two output surfaces (`diagnostics[]` vs `checks[]`). **And by A11.19 (B-22):** 9 of 32 mutants edit one 23-line model and the known-good corpus is their parent, so the intervals do not represent cluster structure |

### 3.2 Per-class result (primary measure: relevant error-severity detection)

| fault class | n | detected | 95% CI | any signal |
|---|---:|---|---|---|
| F1 syntax / notation | 4 | **4** | 1.00 [0.51, 1.00] | 4/4 |
| F2 unresolved reference | 4 | **4** | 1.00 [0.51, 1.00] | 4/4 |
| F3 kind / type mismatch | 4 | **2** | 0.50 [0.15, 0.85] | 4/4 |
| F4 multiplicity | 4 | **3** | 0.75 [0.30, 0.95] | 4/4 |
| F5 named constraint | 4 | **3** | 0.75 [0.30, 0.95] | 4/4 |
| F6 quantity / unit | 4 | **3** | 0.75 [0.30, 0.95] | 4/4 |
| F7 structural / architectural | 4 | **0** | 0.00 [0.00, 0.49] | 0/4 |
| F8 metadata / annotation | 4 | **4** | 1.00 [0.51, 1.00] | 4/4 |
| **overall** | **32** | **23** | **0.72 [0.55, 0.84]** | **28/32 = 0.88** |

The intervals are the honest unit here: at n = 4, "0.75" and "0.50" are not distinguishable, and
"1.00" is compatible with a true rate as low as 0.51.

**Class-table corrections (A11.5–A11.9, A11.13):** F1 4/4 is the **authored family** (four parse
breakages, all exit 2), not notation in general; F2 4/4 is **four reference sites**, and succession
sources are not resolved at all; F4 is **declared multiplicity**, and R1-style connection ends were
never sampled; F5 has **two** rates, 3/4 authored and 3/5 cross-corpus; and F4-01 is a **defect**
(an empty range is unsatisfiable), so the count stands.

### 3.3 The three-way split issue #8 asked for

- **Not detected (5):** F7-01 unreachable state, F7-02 satisfied-but-violated requirement, F7-03
  missing flow, F7-04 contradictory assertions, F5-01 feature-value overriding.
- **Detected only at the wrong severity (2):** F4-02 end-feature multiplicity (KerML
  `validateFeatureEndMultiplicity` is SHOULD-report; emitted as `warning[end-feature-multiplicity]`),
  F6-03 incommensurable sum (emitted as `warning[incommensurable-operands]`). In both cases a CI gate
  on exit status would pass the mutant.
- **Detected with a misleading or unhelpful message (2):**
  - F3-01 `part fuelOutPort : FuelingPort;` (a part usage typed by a port definition). The only
    diagnostic is `warning[name-conflict]: Duplicate of inherited member name 'self' from Part, Port`
    — at the right line, naming the wrong condition. A reviewer following it would look at
    inheritance, not at the kind pairing. This is the "detection gap is not what kills adoption"
    case in miniature.
  - F3-04 `subject v : MaximumMass;`. The only diagnostic is
    `warning[bound-feature-types]` located on the `satisfy … by …` line five lines below the defect.
    The message is true of a downstream consequence and does not name the injected condition.

Every emitted **error** was about the injected defect (any-error 23/32 = relevant error 23/32), so the
corpus contains **no case of a spurious error on a mutant**; the misleading cases are all
warning-severity.

### 3.4 The deliverable: which conditions no available checker catches, and why

`spec_status` is a reading of each mutant's frozen `spec_constraint_or_defect` text — i.e. it was
fixed before the run, not chosen to fit the outcome.

| specification status of the condition | n | detected as error | what was missed |
|---|---:|---:|---|
| **named constraint in the 623-row catalogue** | 10 | 8 | `validateFeatureValueOverriding` (silent), `validateFeatureEndMultiplicity` (warning only) |
| **prose-only — named in the PDF, absent from the metamodel** | 4 | 2 | part-typed-by-port-definition (misleading warning), subject-typed-by-requirement (incidental warning) |
| **only the normative ISQ/SI libraries constrain it** | 4 | 3 | incommensurable sum (warning only) |
| **only the notation / resolution mechanism constrains it** | 8 | 8 | — |
| **nothing names it — catalogue, prose register or library** | 6 | 2 | all four F7 defects; plus the two that *were* caught (inverted bounds, feature-value count) despite nothing naming them |

**Corrected by A11.24 (B-28):** a **third separator** belongs between "tool gap" and "language gap"
— **invocation, encoding and engine**. The same condition is decided under `-satisfy` and not under
`-validate`; an unbound feature is undecidable while a bound one is decided; `-engine check` and
`-engine smt` can disagree. **And by A11.18 (B-21):** `spec_status` is a **post-hoc, single-coder,
mechanical reading** of the frozen MANIFEST text, not a pre-run field.

**Reading it.** Two of the three kinds of gap in issue #8's framing are present and are *not* the
same phenomenon:

1. **Tooling gap — the specification names it, the instrument does not enforce it (2 mutants).**
   `validateFeatureValueOverriding` is a class-A, model-local, SHOULD-report constraint with a
   published OCL body; the model that violates it validates silently. This is the cheapest possible
   defect to find conceptually and it is not found. It is also the construct Sensmetry's documented
   divergence register uses to show the reference implementation mishandling the same case — so the
   gap is not unique to this tool, though two implementations are not corroboration of a class-wide
   claim.
2. **Oracle gap — nothing in the specification names it (4 mutants, all of F7).** Unreachable state,
   a satisfy link whose requirement is false, a subaction input with no supplier, two contradictory
   assertions: the specification's well-formedness surface says nothing, so an implementation is not
   failing at its job by staying silent. No amount of "more rules" fixes this without adding
   semantics the standard does not contain.
3. **A third category the framing did not anticipate: named-in-prose-only (2 of 4 missed).** The
   port-composite and subject-typing conditions exist as normative Clause 8.4 prose with no
   metamodel constraint. One was enforced anyway (F5-04, `port-owned-usage-composite`, found), one
   produced a misleading warning (F3-01). This is evidence that the absence of an OCL constraint does
   not predict what a tool checks — the `prose-only-names.csv` register is a live risk surface, not a
   dead letter.

### 3.5 The counterintuitive result, reported because it cuts against the tidy story

**The instrument is stricter than the specification in one place and looser in another.** The
inverted multiplicity range `[4..2]` was reported as an **error**
(`multiplicity-range: lower bound exceeds upper bound`), although no constraint in the 623-row
catalogue forbids it — §7.6.3 requires bounds to be naturals and says nothing about their order, and
an empty range is not obviously ill-formed. Meanwhile `validateFeatureValueOverriding`, which *is*
named and SHOULD-report, was not enforced. Strictness and specification-faithfulness are different
axes, exactly as the Syside divergence register argues in the opposite direction. A study that
measured only "does it catch things?" would have called both good.

**Corrected by A11.13 (B-13):** the sentence above says the tool was *stricter than the
specification* on `[4..2]` while counting the same diagnostic as a detection. Both cannot be right.
The adjudication holds that `[4..2]` is an **empty, unsatisfiable range** — so the model is defective
and the detection is true; "an empty range is not obviously ill-formed" is withdrawn. The alternative
arithmetic under a named-constraint-only criterion is **22/32**. And **A11.21 (B-25)**: the
`validateFeatureValueOverriding` miss is **site-dependent**, with a live rival reading that F5-01 may
not instantiate the constraint at all.

### 3.6 Known-good arm (false positives, after triage)

**Corrected by A11.15 (B-15):** the KG-04 warning below is reclassified from "over-reach" to
**unresolved / specification-ambiguous**, because the premise "a same-named member is a legal implicit
redefinition" is not established (KerML §8.3.2.4.5 forbids the construct as written; SysML §7.13.4
uses it). The error-level figure that follows is unaffected.

- **Error-level: 0/10.** No known-good model produced an error.
- **Warning-level: 1/10.** `KG-04-featurevalues` emits
  `warning[name-conflict]: Duplicate of inherited member name 'cutoff'` on a line quoted **verbatim**
  from §7.13.4's `TestWithCutoff` example. Triaged as **(ii) legal-but-flagged** with a stated
  reservation (a tool may warn where the specification is silent) in
  `results/known-good-triage.md`. It is counted in the warning-level rate, not argued away.
- **Two pre-freeze corrections, recorded so the corpus is not presented as infallible:** `sum`/`size`
  needed `SequenceFunctions::*`/`RealFunctions::*` (a *confound*, exactly the missing-import trap
  `TOOLING.md` warns about), and the specification's own §7.17.2 example reads
  `bind picture = focus.picture` although `focus` declares `out image` — an **unresolved reference in
  the adopted standard's example text**, repaired by one token and reported as an incidental
  observation about the source material.

## 4. Counter-evidence and tensions

Recorded because a report with no tensions is a report that did not look.

1. **"Your mutants are the tool's own vocabulary."** I read the instrument's `-explain` code list
   during pre-freeze calibration (logged, and disclosed in the methodology §12.6). That biases my
   expectations *towards* the tool. The mitigation is that expectations are anchored to specification
   constraints and that H5/H9 predicted silence anyway; the residual risk is real, and a reviewer
   should treat the expectation audit (§5) as softer evidence than the detection counts.
2. **"The 0/4 on F7 is a definitional trick."** Partly true and worth stating in the tool's favour:
   F7 defects are not well-formedness violations, so a specification-faithful validator *should* pass
   them. The finding is not "the tool is broken"; it is "the ceiling of automated SysML v2 validation
   here is typing plus per-constraint well-formedness, and architectural meaning is outside it". Issue
   #10 is the right home for the stronger claim.
3. **"A false-positive rate of 0/10 from 10 tiny models is uninformative."** Correct. Ten hand-built
   10–30 line models that all validate cannot estimate a false-positive rate; they can only falsify a
   gross one. The finding is bounded to "no gross over-reach on ordinary legal constructs, including
   conjugated ports, explicit multiplicities, metadata annotations, control nodes and feature values".
4. **"Two of your 'misses' are warnings — isn't that detection?"** For a CI gate, no: the tool exits 0
   on both, so a pipeline that gates on exit status classifies them as valid. For a human reviewer,
   yes. That is why severity is a separate axis and why §3.3 is a three-way split rather than a
   binary — but a reader who prefers "warning counts as detected" would report 25/32 instead of
   23/32, and that number should be available rather than argued about.
5. **The strongest rival explanation for the F7 silence is corpus unfairness, not instrument
   blindness.** I cannot separate them with this design. It is separable with the external challenge
   set, and that is the single most important follow-up.
6. **One implementation's behaviour is not the language's.** F5-04 (prose-only condition enforced) and
   F4-01 (un-named rule enforced) show that "the specification does not name it" does not predict
   silence; conversely F5-01 shows "the specification names it" does not predict enforcement. Anyone
   using these results as a conformance statement would be misusing them.

## 5. Pre-registered hypotheses: did they hold?

All nine were written into `METHODOLOGY-FROZEN.md` §7 before the run and are quoted with the outcome.

| # | Prediction | Outcome | Verdict |
|---|---|---|---|
| H1 | F1 + F2 detected as errors in 8/8 | 8/8 | **held** |
| H2 | F3 and F4 error-detection between 50% and 100% | 50%, 75% | **held** (F3 exactly on the boundary) |
| H3 | F5: at least one caught, at least one not (1–3 of 4) | 3 caught, 1 silent | **held** |
| H4 | F6: ≥2 of 4 detected, ≥1 only as a warning | 3 detected; F6-03 warning only | **held** |
| H5 | F7: 0 of 4 as errors, ≥2 silent | 0/4 errors, **4/4 silent** | **held exactly** |
| H6 | F8: ≥3 of 4 detected | 4/4 | **held** |
| H7 | Overall error sensitivity in [0.50, 0.85] | 0.72 | **held** |
| H8 | Surface-tell mutants detected at a higher rate | tell=yes 3/3 = 1.00 [0.44, 1.00], tell=no 20/29 = 0.69 [0.51, 0.83]; intervals overlap | **direction held, not established** — n = 3 vs 29, descriptive only |
| H9 | ≥2 classes with zero detection **and** no named constraint | only F7 qualifies; six mutants have no named condition at all but two of them were caught | **not held as stated** |

**H9 failed, and the refinement is more useful than the hypothesis.** I predicted that uncaughtness
would track the specification's silence. It does not: of the 6 mutants whose condition nothing in the
specification names, 2 were caught as errors, and the one fully-invisible class (F7) is small. What
actually predicts detection is **layer**, not specification silence. That is a better finding, and it
is the one the analysis reports.

### Expectation audit (the pre-registration's own error rate)

Of the 24 mutants I expected to be detectable *at all*: **24/24 produced some diagnostic**, and
19/24 produced an *error*. Of the 6 I expected to be undetectable: 4 were silent, and **2 were
reported as errors — my expectations there were wrong** (F4-01 inverted bounds and F6-02 missing
unit). Both errors of mine are informative rather than embarrassing: they predicted the specification
would be silent where the implementation chose to be strict. The 2 "uncertain" predictions resolved
to caught (F4-04) and caught (F5-04). Full audit in `results/analysis.md` §5.

## 6. Investigation and access log (including recovery)

| Resource | Attempted | Outcome |
|---|---|---|
| OpenSysML v0.12.1 CLI | present at `.tools/sysml`; hash verified against `TOOLING.md` | used throughout; hash recorded in `results/run-log-run1.md`, MATCH |
| Pinned SysML 2.0 PDF `formal/2026-03-02` | hash-verified copy already present at `/tmp/sysml/sysml-2.0-language.pdf`; sha256 matches `catalogue/README.md` §1 | used for every Type-S provenance quote; exact clauses and page numbers cited per model |
| OMG pilot implementation | 20-minute bounded attempt: `java -version` (no runtime), `/usr/libexec/java_home` (none), no `mvn`/`gradle`, GitHub releases API for tag `2026-09.1` | **not obtained** — no CLI asset exists, only a Jupyter kernel zip + `.kpar` libraries; lawfully obtainable in principle, not within the box. Exact log: `second-validator-attempt.md` |
| Syside | not attempted | **access boundary** — licence key required; not bypassed, results out of scope (`TOOLING.md` §3) |
| `DeciSym/sysmlv2-validator` | considered, rejected | a wrapper around the pilot, needs Java 21 + Maven; not an independent instrument |
| `-explain` diagnostic inventory | run once during pre-freeze calibration | used to fix the measurement definitions; disclosed as a threat (§4.1) |
| Malformed member subclause §7.6.1 | **not retrieved in full** | the KG-04 over-reach judgement rests on §7.6.3/§7.6.5 and on the specification's own example; a bounded gap, listed in §9 |
| Robots.txt exception | **not needed** — no web crawling was required | every retrieval was a direct API/URL request or an artefact already verified in-repo |

No access control was bypassed, no client spoofed, no paywall or licence circumvented. Degradations
are stated in §8, not repaired silently.

## 7. Delegation and verification

**No delegation.** No subagents were spawned and no other agent's output was used. Every artefact —
provenance, mutants, expectations, harness, triage, analysis — was produced and checked by this
session. That is a *weakness* as well as a simplification: issue #8 asks for an independent second
coder on whether each mutant instantiates the fault class it claims, and there is none here. It is
recorded as the second-largest limitation after the one-instrument problem.

What I verified personally: the instrument's binary hash; the specification PDF hash against the
catalogue's pinned value; that each mutant's substitution matched exactly once (asserted in
`make_mutants.py`); that the harness never rewrites raw output (it uses exclusive file creation and a
per-run directory); that every rate in `analysis.md` is recomputed from `results.csv` rather than
transcribed.

## 8. Uncertainties and limits

1. **One instrument.** No second measurement exists, so "the tool missed X" cannot be separated from
   "SysML v2 validation cannot express X" except through the specification-oracle table, which is a
   textual argument, not a second measurement.
2. **Author-as-mutator.** The same agent wrote the bases, injected the faults, wrote the expectations,
   ran the harness and judged relevance. Procedural independence only.
3. **N = 32, 4 per class; 10 known-good models.** Every per-class rate has a Wilson interval spanning
   ≳0.6 of the unit interval. The report uses them as descriptions, never as estimates with
   two-decimal precision.
4. **Synthetic mutants.** Rendered plausible by construction and stated rationale, but *not* validated
   against observed generation errors. Representativeness is untested and is the next phase's job.
5. **Version skew.** The catalogue is SysML 2.0 / KerML 1.0; the instrument self-describes against a
   later revision and the binary reports only `v0.12.1`. A mutant may legitimately differ across the
   revisions, and where I know of such a case it is flagged in the mutant rationale; none is claimed
   settled.
6. **The expectation author had seen the instrument's code inventory** (§4.1).
7. **Relevance triage is post-hoc and single-coder.** It labels *what the tool did* — it was never
   allowed to change an expectation — but two of the five "misses" rest on my judgement that a warning
   names a different condition.
8. **Short-circuit measured, not eliminated.** A syntax or name error suppresses later passes
   (`did not analyse cleanly; no check was made`). Each mutant has one defect, so this affected no
   result, but it is a property of the instrument that a reader of any pass/fail metric should know.
9. **The KG-04 over-reach judgement rests on a clause I read partially** (§7.6.1 not read in full).
10. **A warning-level "false positive" is a soft category.** I count it and disclose it rather than
    claiming a clean 0/10.

## 9. What would change the answer

- **A second instrument.** If the pilot implementation (or Syside under a licence) were run on the
  same 32 mutants, the F7 result would either replicate (making it a statement about SysML v2
  validation) or become instrument-specific. This is the single highest-value follow-up, and the
  harness takes a `--binary` argument for exactly that.
- **The external challenge set.** If Researcher A's observed generation errors cluster in layers the
  instrument catches, the 0.72 understates real-world coverage; if they cluster in F7-shaped defects,
  it overstates it. The pilot's fault model would then be replaced by an observed one.
- **An independent second coder on the mutants.** If a coder judges that, say, F3-01 is not a
  well-formedness defect at all, F3's rate changes from 0.50 to 0.33 or 0.67.
- **Rendering every mutant as a diff and checking there is exactly one semantic change** — my
  substitutions are asserted unique, but "one textual substitution" is not the same as "one defect" in
  a reader's judgement, and a reviewer should test that.
- **Reading §7.6.1 in full** would settle the KG-04 over-reach classification.
- **A larger, more diverse known-good corpus** (specification Annex examples beyond the ten clauses I
  used) would turn 0/10 into a usable false-positive estimate.

## 10. Dead ends and things that did not work

- **The OMG pilot implementation** (§6): no JVM, no CLI asset. A JDK alone would not have been
  enough — there is no validator entry point to invoke, only a Jupyter kernel whose validation verb
  the earlier evidence pass could not verify. Two candidates that looked like second instruments
  (`sysmlv2-validator`, `sysmlv2tool`) are wrappers around the pilot and cannot serve as independent
  witnesses.
- **`checkConnectorTypeFeaturing` (KerML §8.3.4.5.3)** was on my list of named constraints to
  instantiate and I could not construct a *faithful* violating model: the documented failing case in
  the release notes is a filter expression whose implied binding connectors violate it, which is not a
  defect a generator plausibly produces. Rather than force a mutant that would not instantiate the
  constraint, I dropped it. This is a coverage hole in F5 and is stated as one.
- **Metaclass-restricted metadata** (`metadata def X :> SysML::RequirementUsage`) does not resolve in
  this instrument's library surface, so the documented "metadata applied to an element type its
  metaclass does not admit" could not be instantiated directly; the abstract-metaclass case was used
  instead.
- **`[0.5]` as a multiplicity bound** turned out to be caught by the *typing* layer rather than the
  multiplicity layer, reorganising an expectation I had written as a layer claim. Recorded in the
  layer-confusion table rather than quietly corrected.
- **A strict type check on default feature values** (KG-04's `cutoff : Integer default = 0.75 *
  averageScore`) never fired, so that base carries a construct I flagged as risky and which proved
  harmless. Recorded because a negative result about my own corpus is data too.

## 11. Implications for the main question

1. **A validator pass is evidence about four layers and no others.** For this instrument: notation,
   names, typing, and per-constraint well-formedness. Any evaluation that reports "N% of generated
   models validated" is reporting a number about those four layers. The report's calibrated sentence
   is: *a pass means the model is expressible, resolvable, consistently typed and satisfies the
   constraints this tool implements; it does not mean the model's structure, requirements or
   behaviour are adequate, and for four out of four structural defects tested it means nothing at
   all.*
   **[Superseded — see A11.2 / B-29. Corrected form: *a pass of the **default `-validate`
   invocation** means the model is expressible, resolvable, consistently typed and satisfies the
   constraints this tool implements; it does not mean the model's structure, requirements or
   behaviour are adequate. For the four structural defects tested it returns **no verdict for three**
   and **detects the fourth only where the requirement encodes a constraint**; the defects are
   weakly observable in traces or empty results (`-state` sits in an unreachable state, `-action`
   completes with an empty result).*]**
2. **Both error rates matter and both are now bounded.** False negatives concentrate at the semantic
   end (0.00 on F7); false positives were 0/10 at error severity with one spec-verbatim warning. The
   ICSE-2013 concern this brief cites — that false alarms and warning presentation stop adoption
   before detection gaps do — is not refuted, but on this corpus the detection gap is the larger
   measured quantity.
3. **Severity is a measurable property, not an implementation detail.** Two mutants were "detected"
   and yet would pass a CI gate; two more were detected at the right line with the wrong condition. A
   benchmark that records only pass/fail would have scored these four as either 4 detections or 4
   passes, and both readings would be wrong.
4. **The stricter tool is not the more faithful one, and vice versa.** Measured within one tool: an
   un-named rule enforced (strict) while a named SHOULD constraint was not (loose). This is direct
   support for issue #8's refusal to treat any single implementation as the oracle, and for issue #2's
   framing of strictness and faithfulness as different axes.
**Corrected by A11.23 (B-27):** the four F7 conditions are **two decided by no mode tested, one
decided by `-satisfy`, one checked and left undecided** — not "four invisible". The oracle conclusion
below survives.

5. **The oracle problem is now concrete rather than rhetorical.** Four defect classes that any
   systems engineer would call wrong are invisible, and the specification does not name any of them.
   A generation-evaluation framework that wants to score them must supply an oracle from outside
   SysML v2's well-formedness surface — expert judgement, execution, or an authored property
   specification. That is a scoping input for issues #9, #10 and #13, not a defect report against a
   tool.

## 12. Adjacent questions noticed but not researched

Logged, not pursued — each is outside this brief.

1. **Do the two implementations disagree on exactly these mutants?** (issue #2). The harness is
   already parameterised by binary; the missing piece is an instrument, not a method.
2. **Is the F7 silence *stable* across model size?** My F7 mutants are 10–30 lines. On a 500-line
   model the same defects may attract incidental diagnostics, which would look like detection.
3. **Do LLM-generated models actually contain F7-shaped defects?** (issue #7). Determines whether the
   0.00 matters more or less than the 0.50.
4. **Does the misleading-message category predict reviewer behaviour?** (issue #14). My F3-01 case is
   a ready-made stimulus: correct line, wrong condition, warning severity.
5. **Could constraint evaluation (`assert constraint`) close part of the F7 gap?** The instrument
   evaluates expressions and has an `-validate=<object>` mode for assertions about an object, which I
   did not exercise. It is a plausible bridge from "well-formed" to "true", and testing it is a
   separate bounded study.
6. **What does a `-strict` run do to the known-good corpus?** The mode exists and I did not use it; it
   would test whether the warning-level over-reach becomes an error-level one.

## 13. Sources

All retrieved, none invented. Where a claim rests on a file in this repository, the file and section
are named; the raw validator output is the primary evidence for every detection claim.

**Instrument and its identity**
- OpenSysML CLI `sysml v0.12.1`, commit `b2f0e9b802a334369da94312c35cefbd8726d3bf`, build
  2026-11-06_03:25:57 — `sysml -version`, recorded verbatim in `research/issue-008/results/run-log-run1.md`.
- Its own diagnostic inventory — `sysml -explain`, enumerated 2026-11-13 (logged in
  `results/calibration/PRE-FREEZE-CALIBRATION.md` as a pre-freeze capability read).

**Specifications (pinned, hash-verified against `catalogue/README.md` §1)**
- SysML 2.0 Part 1, `formal/2026-03-02`, sha256 `46e6c0476a6f1f34f367d57e039d56659bff75e41d2e4b3d37ca4cadea84a83a`.
  Clauses read and quoted: §7.2.2, §7.6.3, §7.6.5, §7.7.1-7.7.2, §7.11.2, §7.12.2-7.12.3, §7.13.2-7.13.4,
  §7.17.2-7.17.3, §7.18.2-7.18.3, §7.20.3, §7.21.2, §8.2, §8.3.21.10, §8.4.8.1. Page numbers cited per
  model in `known-good/*.PROVENANCE.md`.
- KerML 1.0, `formal/2026-03-01`, sha256 `3bcc96f989bfa9d05cd28e026df3351b795fe8d494187b87bff3db7d96373697`
  — read through the catalogue's extraction of its constraints, not as a separate full text.

**Project artefacts (the fault model's derivation)**
- `catalogue/classified.csv` — 623 named constraints with spec, kind, context metaclass, clause,
  dependency class, obligation, published-OCL executability.
- `catalogue/prose-only-names.csv` — 38 names in the PDF but not the metamodel; the source of the
  `prose_only` category and of `validatePortDefinitionNestedUsagesNotComposite`.
- `catalogue/validator-coverage.json` — the `[TODO]`-only constraint list cited in F5-03's rationale
  (and note: that list is the *reference implementation's*, not this instrument's).
- `catalogue/silence-register.md`, `catalogue/README.md` §1/§3/§6.
- `evidence/spec-tooling.md` §3.2, §3.3, §6 — the documented behaviour of the reference
  implementation and the divergence register, used to choose fault classes and to frame H6.
- `research/relational/PROTOCOL.md`, `research/relational/TOOLING.md`, `QUESTION.md`, `LANDSCAPE.md`,
  GitHub issues #8, #2 and #10 (the latter two for framing only, not researched).

**This pilot's own evidence (primary)**
- `research/issue-008/results/raw/run1/{known-good,mutants}/*.json` — 42 unedited validator outputs.
- `research/issue-008/results/results.csv`, `diagnostics.csv`, `triage.csv`, `analysis.json`,
  `analysis.md`, `known-good-triage.md`, `run-log-run1.md`, `raw-run1.json`.

---

## Addendum A1 — 2026-11-13T14:30Z — dated correction after Gate-1 cross-review of issue #7

**Nothing frozen is revised.** The methodology (`2c80d63e…`) and the mutant expectations
(`a9f47974…`) stand unchanged; no mutant, expectation, metric or number above is altered. This
addendum records what reading Researcher A's frozen issue #7 artefacts (after Gate 1 opened) changed
in **my interpretation**, as the protocol requires.

**1. My F2 result was over-generalised, and A's corpus falsifies the general form.** Above I report
resolution-layer detection at 4/4 and describe F2 as "unresolved reference". A's corpus contains a
dangling **succession source** — `first start;` at `research/issue-007/corpus/normalized/T1-C1.sysml:64`
— on which the same pinned validator is completely silent. I re-ran the tool on that model myself
(exit 0, zero diagnostics) and A verified the same silence with a dedicated minimal probe. So the
correct statement of my result is: **the instrument resolves type references and feature references
in expressions completely (4/4 mutants), and does not resolve succession sources at all.** P1 in §2
and the F2 row in §3.2 must be read with that qualifier. This is a real narrowing of my claim and it
came entirely from A's corpus, not from my own.

**2. My F7 "oracle gap" is corroborated, with a frequency calibration I did not have.** A's frozen
population contains 2 structural records (R1 — connector ends traversing multi-valued usages) and one
semantic contradiction (I1) out of 14: 3/14 = 21 %, of which the structural share is 2/14 = 14 %.
My F7 is 4/32 = 12.5 % of a corpus I built. Those are close enough that my uniform
one-class-in-eight allocation is not badly unfair, which was the specific threat to validity I
flagged in §8.3. What I now state more sharply: structural and semantic defects are a *minority* of
observed defects but a *majority* of the undetectable ones.

**3. A genuine tension between the two pilots, left unresolved for the adjudicator.**
`name-conflict` is my only false positive (§3.6: `warning[name-conflict]` on a line quoted verbatim
from the specification's own `TestWithCutoff` example, §7.13.4) and it is A's headline missing class
(119 of 140 diagnostics on a public external corpus, 10 of 24 artefacts). Both readings can be true
at once, and that is the finding: the diagnostic does not distinguish an illegal duplicate from a
legal implicit redefinition, so it is unusable as a defect signal in either direction. I did not
discover this from A; I found the false positive first and could not name the mechanism. A's external
data supplies the volume. Recorded here so the reviewers see that the two pilots disagree and that
the disagreement is itself evidence about the instrument.

**4. Unchanged.** The ceiling claim of §11.1, the severity-is-a-measurable-property result (§11.3),
and the one-instrument limitation are all unaffected by A's work; A's silent-on-5-of-14 result
reinforces rather than challenges them.

---

## Addendum A2 — 2026-11-13T14:40Z — the F7 claim is corrected: one of the four defects **is** detected, by a mode I did not run

**Origin:** Researcher A's Gate-2 objection O1 (blocking). Reproduced by me with my own invocation;
raw output and argv in `research/issue-008/results/raw/run2-modes/`, run log
`results/run-log-run2-modes.md`.

**Original claim (kept visible, not deleted).** §1: *"a clean validation is evidence about
notation, names, typing and per-constraint well-formedness — and it is **no evidence at all** about
whether the model's structure means what it claims."* §2, P3: *"At least one class of plausible model
defect is invisible to the only available instrument — **Established** — F7 0/4, all four silent."*

**What was measured (table from real runs, 2026-11-13T14:31–14:36Z, binary `ddfc2962…1598f0`):**

| mutant | default `-validate` | `-satisfy` | `-instantiate <obj> -validate=<obj>` | `-self-check` | behavioural | outcome |
|---|---|---|---|---|---|---|
| F7-01 unreachable state | clean, exit 0 | — | n/a (no object) | clean, exit 0 | `-state OperationalStates`: starts, stays in `off`, exit 0 | no verdict |
| F7-02 satisfied-but-violated | clean, exit 0 | **violated, exit 1** | **violated, exit 1** | — | — | **DETECTED** |
| F7-03 missing flow | clean, exit 0 | — | n/a (no object) | clean, exit 0 | `-action TakePicture`: completes, `Results: picture = []` | no verdict |
| F7-04 contradictory assertions | clean, exit 0 | — | **undecided, exit 2** | — | — | **checked, no verdict** |

Positive control: the F7-02 base (`KG-07-requirements`) returns `holds`, exit 0, under both
`-satisfy` and `-instantiate -validate=vehicle`. So the invocation discriminates mutant from base and
the detection is not spurious.

**Corrected claim.** A pass of the **default `-validate` invocation** is no evidence about whether a
requirement encoded as a `require constraint` holds of the model's declared values, nor about
reachability, flow completeness or assertion consistency — that is what this pilot measured, and
what 23/32 refers to. The instrument's **verdict surface is wider**: `-satisfy` and
`-instantiate <object> -validate=<object>` evaluate requirement satisfaction and return a standing;
`-state` and `-action` execute state machines and actions. On these four mutants: **one is detected
(violated), one is checked and left undecided, two produce no verdict in any mode tested.** The
honest one-line version is: *the default path is blind to architectural meaning; the verdict path
decides exactly those defects the generator encoded as a checkable constraint, and nothing more.*

**P3 restated.** "Established for two of four F7 mutants under every mode tested (unreachable state,
missing flow); contradicted for one (satisfied-but-violated is detected by `-satisfy`); undetermined
for one (contradictory assertions are checked and returned as undecided, with the same standing as
their known-good parent)."

**Why the second half matters and is A's own O7.** F7-02 is decidable only because I authored the
requirement with `require constraint { massActual <= massRequired }` and bound both values. A
requirement whose body is only a `doc` sentence states no assertion, and the tool says so —
`holds (vacuous)`. So the verdict path's reach is bounded by what generation produced, and in A's
corpus the relevant encoding construct appears **0/18**.

**Effect on numbers.** F7, default path: 0/4 — **unchanged**. F7 across all modes tested:
**1 violated / 1 undecided / 2 no verdict**. Overall relevant detection, default path: 23/32 = 0.72
— **unchanged, now explicitly labelled "default path"**. Overall across the modes tested:
**24/32 = 0.75 [0.58, 0.87]**, with the caveat that only the F7 arm was re-run in other modes.

---

## Addendum A3 — 2026-11-13T14:40Z — the outcome space is five-valued, not binary

**Origin:** A's O2. **Original claim (kept visible).** §8 defines *detected (as error)*, *detected at
the wrong severity*, *relevant vs incidental* and *silent*; the last term means "zero diagnostics of
any severity". §3.3 therefore lists F7-04 under "not detected".

**What was measured.** `-instantiate testObject -validate=testObject` on F7-04:
`? KG10Asserts::testObject is not shown valid: 2 of 2 assertions undecided / standing: not covered
(2 undecided)`, exit 2. On its base KG-10: `1 of 1 assertions undecided`. On A's S2 model under
`-satisfy`: `holds … (vacuous: requirement states no required constraint)`.

**Corrected claim.** The verdict path returns a **standing**, and the pilot now records five
categories alongside the diagnostic-based measure (never instead of it): `holds`,
**`holds-vacuously`**, `violated`, **`undecided / not covered`**, `no assertion to state`. "Undecided"
is a distinct outcome from "silent": the instrument checked and could not decide.

**Refinement recorded against the objection's own direction.** "Undecided" does **not** discriminate
F7-04 from its base — both are undecided, differing only in the assertion count (2 vs 1). Calling it
detection would be wrong; calling it silence, as I did, is also wrong. It is a shape signal with no
verdict, and the table says so.

**Effect on numbers.** F7-04 reclassified from *silent* to *undecided*. F7-02 from *silent* to
*detected* (A2). No percentage other than the F7 row and the mode-aware overall changes.

---

## Addendum A4 — 2026-11-13T14:40Z — a notation sub-class I never tested: reserved keyword used as a name, reported as an error that exits 0

**Origin:** A's O3 (and O9, O10 on construct frequency). **Original claim (kept visible).** §3.2: F1
syntax/notation 4/4 = 1.00, described as a property of the notation layer. §1: "it was perfect on the
two layers it advertises first (syntax 4/4, name resolution 4/4)".

**What was measured (my own probe, not A's corpus)** — `results/probes-gate2/P1-reserved-keyword-name.sysml`,
raw in `results/raw/run2-modes/P1-reserved-keyword-name__*.txt`:

| invocation | exit | diagnostic |
|---|---:|---|
| `-validate -format json` | **0** | `error[reserved-keyword-name]` (`port return;`) |
| `-validate -strict` | **2** | the same diagnostic |

My F1-03 mutant exits 2 in **both** modes; A's `T6-C1` behaves like the probe. So notation defects
split by exit behaviour: a *parse* failure exits 2; a *notation-conformance* error may be reported at
severity `error` and still exit 0, and only `-strict` converts it.

**Corrected claim.** F1's 4/4 is a statement about **the four mutants I authored** (missing
semicolon, extra brace, keyword typo, unquoted short name) — all of which exit 2. It is **not** a
statement about notation defects in general. The empirically dominant notation mechanism in A's
corpus (7 of 9 notation records) is a reserved keyword used as an unquoted name, which my corpus
never produced and which **exits 0**. A pipeline gating on exit status would score my F1 mutants as
failures and the empirical notation class as passes.

**Also recorded (A's O9, O10):** a per-mutant **construct-frequency assumption** is now stated
rather than implied. F1-04 (`<'1.1'>` short name), F4-02 (explicit `end` feature in a `connection
def`), F6 (unit-typed quantities), F8 (metadata annotations) and F7-04 (`assert constraint`) all live
on constructs that appear **0/18** in A's observed corpus. They are retained as specification-surface
probes; they are not evidence about what generators emit. And F4 is relabelled **declared
multiplicity**, not connection-end structure — A's R1 (a chain through a multi-valued usage) remains
a class my corpus never sampled.

**Effect on numbers.** F1 4/4 **unchanged for the authored family**; no longer stated as a
layer-level generalisation.

---

## Addendum A5 — 2026-11-13T14:40Z — F5's 3/4 is a property of my mutant family, not of the satisfy family

**Origin:** A's O4. **Original claim (kept visible).** §3.2: F5 3/4 = 0.75; §3.4: "named constraint in
the 623-row catalogue | 10 | 8 | `validateFeatureValueOverriding` (silent), `validateFeatureEndMultiplicity`
(warning only)".

**What was measured.** On A's frozen S2 record (`research/issue-007/corpus/normalized/T2-C2.sysml`,
read-only): `-validate` reports **nothing** on the satisfy at line 33; `-satisfy` reports
`✓ satisfy lowerBeforeArrival holds … (vacuous: requirement … states no required constraint)`; and
`-instantiate levelCrossing -validate=levelCrossing` returns `undecided`. So the defect — a satisfy
usage with no satisfying feature, against `checkSatisfyRequirementUsageBindingConnector`
(§8.3.21.10, class A, SHOULD) — is not merely missed: **the instrument positively reports the
requirement as holding**, and its explanation is about the requirement's empty body, not about the
missing binding. A reader of that output would conclude the model is fine.

**Corrected claim.** F5 has **two** rates and both are printed: **3/4 = 0.75 on the four mutants I
authored**, and **3/5 = 0.60** when A's S2 record is added as an explicitly **cross-corpus** item.
The cross-corpus item is never merged into the frozen denominator (its provenance is A's coding, not
my `MANIFEST.csv`); the union is labelled wherever it appears. P4 gains the satisfy example.

**Effect on numbers.** F5 3/4 = 0.75 → **3/5 = 0.60 cross-corpus**; 3/4 unchanged on the authored
family.

---

## Addendum A6 — 2026-11-13T14:40Z — F2 is site-dependent, and the prelude confound is now measured

**Origin:** A's O5 and O6. **Original claim (kept visible).** §2 P1: "The instrument detects notation
and name-resolution defects essentially completely — Established (8/8 … 4 unresolved mutants all
error-detected)". §3.2: F2 4/4 = 1.00. (Addendum A1 already narrowed this once; A6 completes it and
publishes the probes.)

**What was measured** (`results/probes-gate2/`, raw in `results/raw/run2-modes/`):

| probe | construct | exit | diagnostics |
|---|---|---:|---|
| `P2-succession-source-undefined` | `first start;`, `start` undeclared | 0 | **none** |
| variant `/tmp/p2b.sysml` (transcript in the run log) | `first zzz;`, an obviously undefined name | 0 | **none** |
| `P3-succession-source-declared` | the same text with `action start;` declared | 0 | `warning[name-conflict]` only |
| `P5-satisfy-target-undefined` | `satisfy limit by nosuchtank;` | **2** | `error[unresolved]` |
| `P4-missing-prelude` | `Real`/`Boolean` with no library import | **2** | 2 × `error[unresolved]`, each naming `ScalarValues::…` and telling the reader to import the package |

**Corrected claim.** Resolution coverage is **site-dependent**: **4/4 at the four sites I tested**
(type reference, parameter reference in a binding, redefinition target, undeclared type) and **0/1 at
a succession source**, where the site is not resolved at all — `first zzz;` is as silent as
`first start;`, so this is a gap in the site, not a name that happens to resolve. F2's sensitivity is
no longer stated as a property of "unresolved reference".

**On the prelude confound (A's O6).** I have no prelude-deletion mutant, so the confound `TOOLING.md`
warns about was untested by my corpus. The probe above shows it is **distinguishable**: the message
names the missing import, so a pipeline that reads messages can separate "forgot the import" from
"names something it never declares", while a pipeline counting `unresolved` cannot. A stated
limitation becomes a measured property.

**Effect on numbers.** F2 4/4 = 1.00 unchanged **at the sites tested**; the class-level claim is
withdrawn.

---

## Addendum A7 — 2026-11-13T14:40Z — the fault model samples the specification's surface, not the generation surface

**Origin:** A's O7 (and O13, O10). **Original claim (kept visible).** §8.4: "Synthetic mutants.
Rendered plausible by construction and stated rationale, but *not* validated against observed
generation errors." §3.1: the fault model is "derived from the specification, not from the
instrument".

**What was measured (census over A's 18 normalised models, run by me):**

| construct | models (of 18) |
|---|---|
| `satisfy` | **18/18** |
| `action def`/`action` | 10/18 |
| `state def`/`state` | 6/18 |
| `ISQ::`/`SI::` **import** | 3/18 |
| a **unit literal** in a value | **0/18** |
| `require constraint` / `assert … constraint` / `constraint { }` | **0/18** |
| metadata annotation `@X` | **0/18** |
| `connection def` | **0/18** |
| explicit `end` feature | **0/18** |
| short name `<'…'>` | **0/18** |

Correction to A's own count: the `ISQ::`/`SI::` **imports** are present in 3 of 18 models (T3-C2,
T3-C3, T5-C1), though none writes a unit literal. The substance of A's claim holds — no model *uses*
units — but "0/18 use ISQ/SI libraries" is not exact.

**Corrected claim.** The fault model measures defects **on the specification's demonstration
surface** (constraints, units, metadata, connection definitions, short names) while the observed
generation surface is declaration + requirement usage + connection shorthand + some behaviour. Every
rate in this report is a sensitivity figure **for the surface sampled**. A construct-frequency census
over ≥200 generated models is the missing instrument for reweighting it, and the direction of the
reweighting is unknown a priori: if generation rarely emits checkable constraints (0/18 here), the
F7-02 detection I now credit is real but rare in practice.

**Candidate class, recorded not adopted (A's O13).** `name-conflict` is absent from my model and
appears at double-digit rates in A's external sample (10 of 24 artefacts, 119 of 140 diagnostics —
reproduced). But my known-good arm shows it fires on a line quoted verbatim from the specification's
own `TestWithCutoff` example (§7.13.4), where a same-named member in a specializing definition is a
legal implicit redefinition. The diagnostic does not distinguish an illegal duplicate from a legal
implicit redefinition, so adopting it would import a signal that is wrong in one direction. It
becomes a **candidate class pending hand-coding against §7.6.3/§7.6.5** — A's own proposal.

**Effect on numbers.** None. The interpretation of every rate acquires a stated domain.

---

## Addendum A8 — 2026-11-13T14:40Z — what the expectation audit can and cannot claim, and relevance is not precision

**Origin:** A's O8 and O12. **Original claims (kept visible).** §5: "Of the 24 mutants I expected to
be detectable *at all*: 24/24 produced some diagnostic, and 19/24 produced an error." §3.3: "Every
emitted **error** was about the injected defect … so the corpus contains **no case of a spurious
error on a mutant**".

**Corrected wording (expectation audit).** The audit is **softened in one direction**: I read the
instrument's `-explain` code inventory before authoring expectations, and the signature of that is
visible — 24/24 expected-detectable produced a signal, and **both** of my expectation errors sit in
the "expected undetectable" bucket and both are cases where the tool is **stricter** than I predicted
(F4-01 inverted bounds, F6-02 missing unit). Expectations written with the tool's vocabulary in view
tend to *under*-predict detection, which can hide: (i) how much of the codebook I anticipated rather
than derived, and (ii) classes where a specification-faithful tool would stay silent and this one
does not. The detection numbers themselves (23/32) are computed from raw diagnostics and do not
depend on the expectations. `expected_layer` uses the **instrument's own layer vocabulary** (`names`,
`typing`, `constraints`), so the layer-confusion table is partly a comparison of the tool with
itself, and is labelled as such.

**Corrected wording (relevance).** The equality any-error = relevant-error is a property of a
one-substitution corpus, **not** evidence that the tool does not over-report. Diagnostics per
defect, from `results/diagnostics.csv`:

| error diagnostics in one mutant | mutants |
|---:|---:|
| 0 | 5 |
| 1 | 20 |
| 2 | 1 |
| 3 | 1 (F1-03 keyword typo) |
| 5 | 1 (F1-04 unquoted short name) |

30 error diagnostics over 28 signalling mutants; **24 of 28 produce exactly one**, and one defect
produced five. The claim is about **relevance, not precision**, and the report now says so.

**Effect on numbers.** None. Two interpretive claims are downgraded to disclosures.

---

## Addendum A9 — 2026-11-13T14:40Z — `MANIFEST.csv` was rewritten after the run, by me, and it is logged here

**Origin:** A's O11. **Fact.** `mutants/expectations.sha256` was written at **14:13:00Z**; the first
validator run (`results/raw-run1.json`) at **14:13:03Z**; `mutants/MANIFEST.csv` has mtime
**14:15:56Z** — after the run it pre-registers.

**Cause, named rather than speculated.** I ran my own documented reproduce step
(`python3 harness/author_manifest.py`, README "reproduce 2") to demonstrate that the generator is
idempotent. It rewrites `MANIFEST.csv` byte-identically; `shasum -a 256 -c mutants/expectations.sha256`
verifies OK against the current file, and the content is the pre-run content.

**Decision.** The rewrite is recorded here rather than by editing the run log or the freeze
artefacts, because those are the evidence. A reviewer who wants the strongest available form of the
guarantee should note that the hash chain survives (the MANIFEST hash in `expectations.sha256` is
pre-run and still matches) but that **an idempotent regeneration of a pre-registration artefact after
the run is a process error even when the content is unchanged** — a future run must either skip the
reproduce step or log it at the time.

**Effect on numbers.** None.

---

## Addendum A10 — 2026-11-13T14:56Z — External challenge set (A's frozen observed errors)

**Origin:** task-6. Researcher A froze 13 observed error items and 7 controls from the corrected
issue #7 population (`research/relational/empirical-subset/`, `frozen_utc` 2026-11-13T14:33:20Z,
`subset.json` sha256 `bc2b92a5…c3dfaa`). I verified every recorded hash before running — `subset.json`,
`models/manifest.csv`, all 36 per-file sha256 + byte counts, and the frozen copies against A's live
corpus: **no mismatch**. Full detail, the pre-registered invocation set and the per-item matrix:
`research/issue-008/empirical/` (`PRE-REGISTRATION.md` frozen at `9458406e…6acfbc` **before the first
run**, `REPORT.md`, `results.csv`, `per-item-per-mode.md`, `raw/run2/**`, `run-log.md`).

**Original text of this report is preserved. Nothing above is edited.** This addendum records only
what the external measurement adds, and where the two frames disagree.

### A10.1 Result

Default `-validate` path, 13 observed items: **9/13 = 0.69 [0.42, 0.87]** — 9/12 = 0.75 excluding the
contested I1 item, 9/11 = 0.82 excluding it and the one short-circuited item. For comparison, my
synthetic primary measure is 23/32 = 0.72 [0.55, 0.84] and the mode-aware figure 24/32 = 0.75.

| observed class | n | detected | outcome of misses |
|---|---:|---:|---|
| S1 notation | 3 | **3** | — |
| N1 unresolved | 4 | **4** | — |
| N2 missing prelude | 1 | **1** | — |
| T1 kind (definition where usage required) | 1 | **1** | — |
| S2 named `check…` constraint | 1 | **0** | the model's only diagnostic is a *different* defect; under `-satisfy` the tool reports the requirement as **holding vacuously** |
| R1 connector over a multi-valued usage | 2 | **0** | one **unmeasurable**: the JSON envelope says "did not analyse cleanly; no check was made"; the other is a clean, silent miss |
| I1 documentation/value contradiction | 1 | **0** | silent |
| **total** | **13** | **9** | |

Per registered mode: M2 `-satisfy` **0 detected** (1 item evaluated, `holds-vacuously`; 10 not
applicable); M3 `-instantiate … -validate=` **0 detected** (1 `undecided`; 10 not applicable);
M4 `-validate -strict` **9/13, the same items as M1**, with exit codes changing from 0 to 2 on two
models — Gate 2's exit-code finding reproduced on observed data.

### A10.2 Synthetic vs observed: class names are not identical, so only the layer comparison carries

The two frames were coded independently under different codebooks. My mapping (fixed in
`PRE-REGISTRATION.md` §6, before the run) is partial: **F1↔S1**, **F2↔{N1,N2}**, **F3↔T1**,
**F5↔S2**; **F4, F6 and F8 have no observed counterpart at all**, and **F7↔{R1,I1} is weak and
contested** (A now labels R1 `type/typing`, with `structural/architectural` as the rival layer).
Pooled over the mapped classes the observed rate (9/10 = 0.90) is **not lower** than the synthetic
one (13/16 = 0.81); the aggregate near-agreement of 0.69 and 0.72 is a **coincidence of composition**.

What replicates is the **layer boundary**:

| layer | synthetic | observed | agreement |
|---|---|---|---|
| notation / parse | F1 4/4 | S1 3/3 | both fully detected |
| name resolution | F2 4/4 (at four sites; 0/1 at succession sources after Gate 2) | N1+N2 5/5 | both fully detected at sampled sites |
| typing | F3 2/4, F4 3/4 | T1 1/1 | mostly detected |
| constraint / OCL | F5 3/4 | S2 0/1 | **disagree in direction** (n = 1) |
| semantic / structural | F7 0/4 default, 1/4 mode-aware | I1+R1 0/3 | both ~fully missed |

### A10.3 What this does to P6 and P8

- **P6** ("validator pass rates measure less than the literature claims"): my pre-registered rule was
  "supported if mapped-class observed detection is ≥0.15 below synthetic". It is not — observed is
  *higher*. **P6 is therefore neither supported nor refuted by the external set; it stays where it
  was.** The structural reason is stated in `empirical/REPORT.md` §8: the observed corpus is dominated
  by the classes the instrument handles, so its aggregate is high by construction. What the external
  set *does* support is the practical form of the claim — a pass is evidence about four layers and no
  others — because every miss sits at constraint/semantic/structure.
- **P8** ("the fault model is representative"): **weakened, not settled, and now with a direction.**
  Four of my eight classes have no observed counterpart (F4, F6, F8 none; F7 only contested), which
  the construct census on the 18 frozen models explains: **0/18** contain a `require`/`assert`
  constraint, a unit literal, a metadata annotation, a `connection def`, an explicit `end` feature or a
  short name; **3/18** import `ISQ`/`SI` without writing a unit; **18/18** contain `satisfy`. So the
  classes with my most favourable synthetic rates are exactly the classes observation cannot test. The
  **layer** generalisation travels; the **class distribution** does not; representativeness remains
  unestablished and still needs a construct-frequency census over ≥200 generated models.

### A10.4 Controls

Four clean-tier controls under M1: **0/4 produced an error diagnostic and 0/4 a warning** — no triage
needed. That falsifies gross over-reach on four short models; it does not estimate a false-positive
rate. The three `frozen-clean-only` models are **not** scored (their diagnostics are not false
positives): all three produce exactly the post-inspection defect A verified after the frozen
population closed (`usage-typing@11`; `reserved-keyword-name@26` twice). That is a point in the
instrument's favour, on data A generated, and a point against inspection-only coding.

### A10.5 Corrections to this report's own earlier generalisations

- **A1/A6's F2 claim narrows once more.** All four observed N1 items are *satisfy-target* references
  and all are detected; my four F2 sites are detected; Gate 2 showed succession sources are not
  resolved at all. The three-way statement is now: **type references, expression references and
  satisfy targets are resolved; succession sources are not.**
- **A2's mode-aware F7 figure is not transferable.** F7-02 was detected in the object mode because I
  authored it with a checkable `require constraint`. In the observed corpus **no model encodes one**
  (0/18), so M2/M3 were applicable to 3 items each and returned no detection. The verdict path's reach
  is bounded by what generation wrote, exactly as A10.3 argues.
- **A9's short-circuit caveat is not theoretical.** One of the 13 observed items (`ES-T4-C1-E02`) is
  unmeasurable on the default path because the tool states it "did not analyse cleanly; no check was
  made". It is scored as a miss under the registered rule and reported as **unmeasurable** in
  interpretation, with the denominator ladder 9/13 → 9/12 → 9/11 shown rather than chosen between.

---

## Addendum A11 — 2026-11-13T15:10Z — Adjudicated corrections (Gate 4)

**Source:** `research/relational/adjudication/` (`ADJUDICATION.md`, `rulings.json`, `CORRECTIONS.md`
Part 2, items B-1…B-35). Each item below quotes the text it supersedes — the original stays visible
in the body of this report — states old → new, and names the ruling. **Nothing is deleted and no
number in the body is silently changed.** Derived scorings live in new files
(`empirical/results-addendum.csv`, `empirical/SCORING-ADDENDUM.md`); raw output and
`results/results.csv` are untouched. `METHODOLOGY-FROZEN.md` stays byte-identical; the B-14
disclosure is in `research/issue-008/METHODOLOGY-ADDENDUM-1.md`.

### A11.1 Headline sentence — the pass claim, scoped to the invocation (B-1 / CC-05, A2B-01)

**Superseded (still printed in §1 and pointed from there):** *"a clean validation is evidence about
notation, names, typing and per-constraint well-formedness — and it is **no evidence at all** about
whether the model's structure means what it claims."*

**Corrected:** *"A pass of the **default `-validate` invocation** is evidence about notation, names,
typing and per-constraint well-formedness, and no evidence about whether the model's structure means
what it claims. The instrument's **verdict surface is wider**: `-satisfy`,
`-instantiate <object> -validate=<object>` and the engine modes decide conditions the model itself
asserts — and, separately, report execution failures and property checks where the model's own
bindings force the issue."* The second half of that correction is **B-24** (below); the adjudicator
rejected only the phrase "and nothing more".

### A11.2 §11.1 — "for four out of four … it means nothing at all" (B-29 / CC-11)

**Corrected**, inline at §11.1: insert "default `-validate`" before "pass", and replace "means
nothing at all" with *"returns no verdict for three of the four and detects the fourth only where the
requirement encodes a constraint; the defects are weakly observable in traces or empty results."*
The four F7 outcomes across all modes tested are unchanged: 1 violated, 1 undecided, 2 no verdict.

### A11.3 §2 P3 — pointer, not deletion (B-30 / CC-12, A2B-01)

The P3 cell now reads *"corrected by A2, and further corrected by A11.1: see there; the form below is
the original and is superseded"*, with the original verdict retained verbatim beside it. Amendment A1
requires the original to stay visible; the remedy for a retracted headline is a pointer.

### A11.4 Measurement definitions — two output surfaces and five standings (B-2 / A2B-02)

**§3.1 defined one measure, typed on diagnostics.** Added to the measurement definitions:

- **Two output surfaces.** `diagnostics[]` carries `severity`/`code`/`line`/`message`;
  `checks[]` carries a **`standing`** per subject. The primary measure in §8/§9 is typed on the
  first and cannot represent the second.
- **Five standings:** `holds` / **`holds-vacuously`** / `violated` / **`undecided (not covered)`** /
  **`no assertion to state`**. `undecided` is neither "detected" nor "silent": the instrument checked
  and returned no verdict.
- A verdict is quoted only with its invocation, engine and standing label (B-35, A11.20).

### A11.5 F1 — "authored family", and the exit-0 sub-class (B-3 / A2B-03)

**§3.2 F1 row and §1 corrected to:** F1 **4/4 is the authored family** — four parse breakages
(missing `;`, extra brace, keyword typo, unquoted short name), all of which exit 2. The empirically
dominant notation mechanism (a reserved keyword used as a name; 7 of A's 9 notation records) is a
**different sub-mechanism** and is reported at **error severity with exit 0** (probe P1; `-strict`
makes it exit 2). Neither the count nor the exit-status discussion transfers to "notation in
general".

### A11.6 F5 — two rates and the obligation (B-4 / A2B-04)

**§3.2 F5 row corrected to print both:** **3/4 = 0.75 on the authored family** and **3/5 = 0.60 on
the cross-corpus union** with A's S2 record (labelled, never merged into the frozen denominator). And
the obligation is stated: `checkSatisfyRequirementUsageBindingConnector` (§8.3.21.10) is a **`check…`
constraint — "MAY report, satisfy by implied relationships, or ignore"** — so its non-reporting is
not a conformance failure. Under `-satisfy` the instrument reports that requirement as **holding,
vacuously**, and explains the vacuity via the requirement's empty body, not the missing binding.

### A11.7 F2 — the three-way resolution statement and the measured confound (B-5 / A2B-05, A2B-06)

**§2 P1 and §3.2 F2 corrected.** The single claim "unresolved reference 4/4" becomes: **type
references, expression references and `satisfy` targets are resolved (4/4 mutants; 5/5 observed
items); succession sources are resolved not at all (0/1 observed, and an arbitrary undefined name
there is equally silent).** The missing-prelude confound is **measured**, not avoided: the diagnostic
names the import (`unresolved reference: Real — did you mean ScalarValues::Real? … import its
package`), so a pipeline reading messages can separate it from a dangling name, and one counting
`unresolved` cannot.

### A11.8 Construct-frequency assumption and scope (B-6 / A2B-07, A2B-09)

Added to §3.1 and §8: the fault model measures defects on the **specification's demonstration
surface**. Census over A's 18 frozen models: `satisfy` **18/18**; `require`/`assert` constraint
**0/18**; unit literal **0/18**; metadata annotation **0/18**; `connection def` **0/18**; explicit
`end` feature **0/18**; short name **0/18**. Four of eight classes therefore have **no observed
counterpart**, and per-mutant construct-frequency assumptions are now stated in the class table.

### A11.9 F4 is "declared multiplicity"; R1 was never sampled (B-8 / A2B-09)

**§3.2 F4 and §A4/§A7 corrected:** F4 is **declared multiplicity** (bounds, end-feature multiplicity,
feature-value count), **not** connection-end structure. A's R1 — a connector end whose feature chain
traverses a multi-valued usage — was **never sampled** by my corpus. F4-02 in particular is a
declared-multiplicity violation on an explicit end feature, a different condition from R1 with a
different outcome.

### A11.10 A9 — the disclosure extends to the 32 mutant files (B-9 / A2B-10)

**§A9 corrected:** the idempotent reproduce step rewrote **`mutants/*.sysml` as well as
`MANIFEST.csv`** (same mtime 14:15:56Z; `mutants/mutants.sha256` verifies OK against the current
files). A9 named only `author_manifest.py`. Content is unchanged; the process error is the same one.

### A11.11 Diagnostics per defect — relevance, not precision (B-10 / A2B-11, RB-08)

**§A8 corrected.** The sentence *"24 of 28 produce exactly one"* was wrong under either reading.
Measured: **28 mutants carry ≥1 diagnostic; 23 of those carry exactly one (any severity); among the
23 error-bearing mutants, 20 carry exactly one error.** One defect produced five diagnostics
(F1-04). The claim is **relevance, not precision** — a single-defect corpus makes any-error equal
relevant-error almost by construction, and it is not evidence that the tool does not over-report.

### A11.12 The census, corrected in the addendum itself (B-11 / B2A-16)

**§A7 corrected:** **3/18 import `SI`** (T3-C2, T3-C3, T5-C1), **0/18 import `ISQ`**, **0/18 write a
unit literal**. The earlier phrasing "ISQ/SI libraries 3/18" is imprecise and the correction had been
left to A's register.

### A11.13 F4-01 is a defect, not over-reach (B-13 / RB-02)

**§3.5 corrected — this is the one internal contradiction the adjudicator found in my own reasoning.**
I counted F4-01 (`[4..2]`) as a **detection** while citing the same diagnostic as the instrument being
*stricter than the specification*. Both cannot be right. The adjudication settles it against me:
`[4..2]` is an **empty range**, the specification's own definition of a range makes it
unsatisfiable, so the model text **is** defective, the error is a **true detection**, and the
sentence *"an empty range is not obviously ill-formed"* is deleted. What survives is the narrower
true claim: **no catalogue constraint names the condition**, so the instrument reports an
**unnamed but semantically impossible** condition. **Alternative arithmetic:** under a
"named-constraint-only" defect criterion — which neither pilot uses — F4 would be **2/4** and the
total **22/32**. And *"no case of a spurious error on a mutant"* is conditional on the semantic
reading.

### A11.14 Expectation knowledge beyond `-explain` (B-7, B-14 / RB-03)

**§4.1 and §A8 corrected; methodology addendum written** (`METHODOLOGY-ADDENDUM-1.md`). The
pre-freeze **calibration probes**, not only `-explain`, supplied construct-level detection
knowledge that pre-determined two classes' flags: `q1` recorded
`error[incommensurable-binding]` (→ **F6's "yes"**), `m1` recorded `error[metadata-metaclass]`
(→ **F8-01**), `m2` recorded `error[metadata-owning-type-feature]` (→ **F8-02**), `t1` recorded
`warning[bound-feature-types]` (→ the F6 severity expectation). The audit is therefore relabelled
**"informed, not blind, and weak by construction"**; the detection counts are unaffected because they
come from raw diagnostics.

### A11.15 KG-04 is unresolved / spec-ambiguous, not over-reach (B-15 / RB-04)

**§3.6 and `results/known-good-triage.md` corrected.** "Over-reach" required that a same-named
member in a specializing definition is a **legal implicit redefinition**, which is **not
established**: KerML `validateNamespaceDistinguishibility` (§8.3.2.4.5) forbids the construct as
written, while the specification's own §7.13.4 `TestWithCutoff` example uses it. The warning on
KG-04 is reclassified **unresolved / specification-ambiguous**; the settling pointers are
**§7.6.3 and §7.6.5** (not §7.6.1, which is "Definition and Usage Overview") and KemML §8.3.2.4.5.
The underlying question is adjudication X-01 (unresolved). The known-good **error** rate (0/10) is
unaffected — this is a warning.

### A11.16 "5 silent" → 4 silent + 1 warning-only (B-19 / RB-08)

**§3.3 and §A8 corrected.** Under the frozen definition ("silent" = zero diagnostics of any
severity), **F5-01 is not silent**: it carries `warning[name-conflict]`, inherited from its base
model. The split is now **4 silent** (the four F7 mutants) **+ 1 incidental at warning severity**
(F5-01), which is consistent with the same page's any-signal figure. `results/analysis.md` and
`results/analysis.json` have been regenerated with this correction: detection counts unchanged
(23 detected, 2 wrong-severity, 1 misleading, **2 incidental**, **4 silent**).

### A11.17 Ordering evidence: filesystem, not self-reported clocks (B-20 / RB-09)

Several times in this report and its addenda are **self-reported** and some post-date the file's own
last write (A2's stated run window; the addenda headers; AM1's date). They are unreliable as
ordering evidence and are no longer used for it. The orderings the protocol depends on are
independently established from the **filesystem**: methodology (mtime 14:06:07Z) before the mutant
corpus (14:13:00Z) before the first run (14:13:03Z), and the analysis is generated after the run.
Where an ordering claim matters it now cites the filesystem or an append-only log, never a hand-typed
UTC string.

### A11.18 `spec_status` is post-hoc and single-coder (B-21 / RB-10)

**§3.4 corrected.** `spec_status` ("named constraint" / "prose-only" / "library semantics" /
"notation" / "nothing names it") is **not** a MANIFEST column and was **not** fixed before the run.
It is a **single-coder, post-hoc reading of the frozen `spec_constraint_or_defect` text, assigned by
a mechanical rule**. The underlying text is frozen and the buckets are checkable, but the provenance
sentence "fixed before the run" overstated it. `harness/analysis.py` now says so in the code.

### A11.19 Base concentration, and the known-good corpus was iterated (B-22 / RB-11)

**§3.1 and §8 corrected.** The known-good corpus is **not independent of the mutant generator**: it is
the parent of all 32 mutants, **9 of 32 mutants edit one 23-line model (`KG-01`)**, and the top three
bases carry **19 of 32**. It was also **iterated to tool-silence before the freeze** (two models were
edited after the tool flagged them). The 0/10 error rate reproduces and is unaffected; but the
per-class Wilson intervals do **not** represent this cluster structure, and "independent of the mutant
generator" must carry the qualification.

### A11.20 A2's "and nothing more" (B-24 / CC-06) and verdict self-certification (B-35 / X-04)

**§A2 corrected:** the clause *"exactly those defects the generator encoded as a checkable
constraint, and **nothing more**"* is replaced by *"… and, separately, **execution failures and
property checks where the model's own bindings force the issue**"*. The adjudicator rejected the
critic's `assert`-constraint counterexample (an assert **is** a checkable constraint) but accepted
that execution and property checks fall outside the encoded-constraint description.

**And, from X-04:** a verdict is **not self-certifying**. The adjudicator reproduced `-engine check`
returning `holds` on an invariant that `-engine smt` witnessed as violated. Every verdict quoted in
this report must therefore name **invocation + engine + standing**, and "the instrument decides X" is
shorthand for "invocation I, engine E, returns standing S".

### A11.21 P4 is site-dependent, with a rival reading (B-25 / CC-07)

**§2 P4 corrected.** *"Some specification-named SHOULD constraints are not enforced"* overstates the
class: the `feature-value-overriding` diagnostic **exists and fires where the redefinition is
explicit**. The corrected claim is **site-dependent enforcement**: `validateFeatureValueOverriding`
is missed at the site I tested (an implicit redefinition). And a **rival reading** is recorded that I
cannot exclude: F5-01 may not instantiate the constraint at all, because a same-named declaration may
not be a redefinition — the same unresolved question as `name-conflict` (X-01). Neither reading is
established.

### A11.22 The ceiling is the ceiling of the default path (B-26 / CC-08)

**§4.2 corrected:** *"the ceiling **of the default `-validate` path** is typing plus per-constraint
well-formedness; beyond it the instrument decides conditions the model itself asserts, at the
strength its engine reports (`observed`, `bounded`, `proved`, `witnessed`)."* The original sentence
described one verb.

### A11.23 Two of four, not four of four (B-27 / CC-09)

**§11.5 rewritten:** the paragraph asserting that four structural/semantic classes are "invisible and
the specification does not name any of them" is corrected to: **two of the four are decided by no mode
tested; one is decided by `-satisfy`; one is checked and left undecided — and for all four the oracle
must be authored into the model or supplied by an expert.** The oracle conclusion in the same
paragraph survives and is the part worth keeping.

### A11.24 A third separator: invocation, encoding, engine (B-28 / CC-10)

**§8.1 and §9 corrected.** The pilot separated *tooling gap* from *oracle gap* only through the
specification-oracle table. A **third separator** is added: **invocation, encoding and engine** —
the same condition can be decided under `-satisfy` and not under `-validate`; an unbound feature is
undecidable while a bound one is decided; `-engine check` and `-engine smt` can disagree. Each
separator is cheaper than the textual argument, and none was enumerated.

### A11.25 Optional example additions (B-31 / CC-13, OPTIONAL)

Not applied as corrections — the adjudicator **rejected** the underlying criticisms and recorded
"no overstatement". The encoding-dependence observation (contradictory assertions and missing flow
generalise it) is noted here as strengthening A11.1/A10.5 rather than correcting them.

### A11.26 Items applied in other files

| item | ruling | where |
|---|---|---|
| B-12 pre-registration hash | RB-01 | `empirical/REPORT.md` §14.1; `empirical/run-log.md` §7 |
| B-16/B-17 M2/M3 accounting and registered-rule deviation | RB-05, RB-06 | `empirical/results-addendum.csv`, `empirical/SCORING-ADDENDUM.md`, `empirical/REPORT.md` §14.2 |
| B-18 harness immutability | RB-07 | `empirical/run_external.py` (exclusive creation implemented) |
| B-23 README contradiction | RB-12 | `research/issue-008/README.md` |
| B-32 obligation split | X-01 | `empirical/SCORING-ADDENDUM.md` §3, `empirical/REPORT.md` §14.3 |
| B-33 layer vs obligation | X-02 (unresolved) | `empirical/REPORT.md` §14.4, and §8 of this report |
| B-34 R1 ladder rung | X-03 (unresolved) | `empirical/SCORING-ADDENDUM.md` §4, `empirical/REPORT.md` §14.5 |
| B-35 verdict self-certification | X-04 (unresolved) | A11.20, `empirical/REPORT.md` §14.6 |
| B-7/B-14 methodology disclosure | RB-03 | `research/issue-008/METHODOLOGY-ADDENDUM-1.md` |

### A11.27 What did **not** change

The numerator. **23/32 = 0.72 [0.55, 0.84]** on the default path stands (22/32 only under a
named-constraint-only criterion that neither pilot uses). The external arm's 9 stays 9. F7's default
0/4, F1's 4/4 on the authored family, F2's 4/4 at the sites tested, F8's 4/4, the known-good 0/10 —
all reproduce. What changed is **what the numbers are permitted to say**: their invocation, their
composition, their obligation structure, and the independence of the audit behind them.
