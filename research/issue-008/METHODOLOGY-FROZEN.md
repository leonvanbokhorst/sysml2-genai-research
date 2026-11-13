# METHODOLOGY — FROZEN before any mutant existed and before any validator ran on the corpus

**Research issue:** [#8](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/8),
*How reliable are SysML v2 validators as measuring instruments?* — **pilot only**.
**Author:** Researcher B (independent agent, own context).
**Authored (UTC):** 2026-11-13T13:5xZ. **Frozen (UTC):** 2026-11-13T14:08Z.
**Hash of this file is quoted in `reports/issue-008-validator-reliability-pilot.md` before the first
validator run over the corpus.** No edit after freezing except a dated amendment in §14.

**Independence statement (required by `research/relational/PROTOCOL.md` §4, Gate 1).**
This document was written **before** I read, received, or was told anything about Researcher A's
findings for issue #7. I have not opened `research/issue-007/**` or
`research/relational/cross-reviews/**`, and I have received no message from Researcher A or from
the Team Lead relaying A's results. No mutant, expectation, hypothesis or metric below was
informed by any other researcher's work. A's frozen empirical subset reaches me later, as a
**separate external challenge set** (§11) that cannot change anything in this document.

---

## 1. Research question (as scoped for this pilot)

If plausible, specification-derived faults are injected one at a time into known-good SysML v2
models, **which fault classes does the available open validator detect, at what severity and
layer, with what message quality — and which classes does no available checker catch?**

The second half is the part with consequences for the main research question: a validator pass
rate is only interpretable if the classes it cannot see are known.

**This is a calibration of the specific instrument pinned in §6, at that version, against this
corpus. It is not a measurement of "validators", of SysML v2 validation in general, or of the
OpenSysML project's conformance. It cannot close issue #8**, whose "what would count as
convincing evidence" asks for a second coder on mutant validity, a published regenerable corpus,
a second validator, and a corpus representative of real generation errors. None of those is
delivered here. The pilot's contribution is the *method and its first numbers*, plus an
instrument for others to re-run.

## 2. What this pilot does and does not claim

| Claim | In scope |
|---|---|
| Per-fault-class detection rate of the pinned instrument, with denominators | yes |
| Detection *layer* and *severity* actually emitted, vs expected | yes |
| Classes that no available checker catches, split into tooling gap vs oracle gap | yes |
| False-positive behaviour on a small independent known-good corpus | yes |
| That the fault model represents real GenAI generation errors | **no** — synthetic; A's corpus is the check on that and arrives later |
| That the instrument is (in)correct, or that it should be fixed | **no** — explicitly excluded by issue #8 |
| A conformance verdict on any implementation | **no** — excluded |
| Anything about Syside (licence-gated) or the OMG pilot (no JVM) | **no** — logged as access boundaries |

## 3. Fault model and its derivation (the load-bearing design decision)

Issue #8 says the validity of the whole approach rests on the fault model. It is derived from
**two sources that predate this pilot and are independent of the instrument**:

1. `catalogue/classified.csv` — 623 named well-formedness constraints extracted from the
   normative XMI, each with spec, kind (`derive`/`check`/`validate`), context metaclass, clause,
   dependency class (A/B/U), obligation (SHALL/MAY/SHOULD) and published-OCL executability.
2. `catalogue/prose-only-names.csv` — 38 constraint names that occur in the specification PDF
   but are defined in neither XMI, of which 31 state conditions in normative Clause 8.4 prose.
3. `evidence/spec-tooling.md` §3.3, §6 — documented implementation behaviour (thirteen constraints
   previously unchecked; one admitted suppression; no type checking or inference in the
   reference implementation; implicit binding connectors not constructed; multiplicity bounds
   marked TODO; `CauseAndEffect` metadata mis-typing silently ignored; control-node succession
   rules unimplemented).

The classes are stratified by the layer at which the fault *should* be visible, taking the
instrument's own four advertised layers (documented in `TOOLING.md` §1 and confirmed by
`-explain`) as the ordering for the confusion view, **not** as the ground truth:

| ID | Fault class | Specification basis (retrieved) | Expected detection layer |
|---|---|---|---|
| F1 | Syntax / textual-notation defect | SysML 2.0 §8.2 textual notation BNF (a *notation* condition, not an OCL constraint) | Syntax |
| F2 | Unresolved reference (typo'd or omitted declaration) | KerML 1.0 §8.3.3 names/membership resolution; not itself a named OCL constraint | Name resolution |
| F3 | Usage typed by a definition of the wrong kind | Clause prose only: SysML 2.0 §7.11.2 ("a part usage must only be defined by item definitions…"), §7.12.2 ("a port usage must only be defined by port definitions"), §7.7.1. **No constraint of this shape exists in the 623-row catalogue** (searched: no row whose prose is of the form "must only be defined by"; `checkAttributeUsageDataTypeSpecialization` is prose-only and renamed) | Typing |
| F4 | Multiplicity / cardinality violation | KerML 1.0 `validateFeatureEndMultiplicity` §8.3.3.3.4 (SHOULD, class A); `validateMultiplicityRangeBoundResultTypes` §8.3.4.11.2 (SHOULD, class B). Two sub-cases (inverted bounds; redefinition widening) are **not** covered by any catalogue constraint — recorded, not hidden | Typing / constraints |
| F5 | Violation of a *named* constraint | `validateFeatureValueOverriding` KerML §8.3.4.10.2 (SHOULD, A); `validateSatisfyRequirementUsageReference` SysML §8.3.21.10 (SHOULD, A); `validateDecisionNodeIncomingSuccessions` SysML §8.3.17.7 (SHOULD, A — reached only via `[TODO]` methods in the reference implementation's own source, per `validator-coverage.json`); `validatePortDefinitionNestedUsagesNotComposite` (prose-only, SysML §8.4.8.1, **missing from the metamodel**) | Constraints |
| F6 | Quantity / unit dimensional inconsistency | SysML 2.0 model libraries ISQ/SI (normative) + type conformance; **no catalogue constraint names dimension conformance** (searched `Quantity`/`Dimension`: no row) | Typing |
| F7 | Structural / architectural defect that no layer names | **None** — deliberately: unreachable state, satisfied-but-violated requirement, missing interconnection implied by the model's own requirement text, unsatisfiable guard. Ground truth here is the model's own requirement text plus engineering adequacy, and is labelled as such | none expected |
| F8 | Metadata / annotation mis-typing | KerML 1.0 `validateMetadataFeatureMetaclass` §8.3.4.12.3 (SHOULD, A), `validateMetadataFeatureMetaclassNotAbstract` §8.3.4.12.3; SysML §7.4.3, §8.3.27. **This is the documented "silently ignored" case** (`evidence/spec-tooling.md` §3.3(f), third-party) | Constraints |

Four mutants per class, 32 in total. **Class-level design intent, not a prediction**: F1 and F2
are earlier-layer faults and should be the reference point that calibrates the rest; F7 is the
negative control that measures the ceiling.

**Why these eight and not others.** They partition the instrument's own advertised layers, so a
result can say *where* detection stops rather than only *how much* is caught. They also separate
two things the literature conflates: a fault the specification names and the tool does not check
(tooling gap), and a fault the specification does not name at all (oracle gap). That separation
is the pilot's actual dependent variable, and it is why F3/F6/F7 were included even though they
are expected to be undetectable.

## 4. Mutant construction and plausibility criteria

**Construction rules (each mutant is one edit of one base model):**

1. Derived from a known-good model in `known-good/`, so the only difference is the injected
   defect and a diff is computable.
2. **Exactly one deliberate defect.** No incidental changes of formatting, naming or ordering.
3. Plausible for a *generator*, not adversarial for a parser: each mutant's `plausibility` column
   states the concrete generator behaviour that would produce it (confusing two constructs,
   emitting a name that was never declared, copying a unit from the wrong quantity, assuming a
   requirement's bound holds because the `satisfy` link exists, and so on). No buffer overruns, no
   pathological nesting, no unbalanced-quote fuzzing.
4. **Surface-tell flag, recorded before the run.** Every mutant is marked `surface_tell = yes/no`:
   yes if the defect is lexically conspicuous (a visibly missing semicolon, a keyword typo), no if
   the file still looks like ordinary SysML v2 to a reader who is not comparing against the base.
   This exists because a mutant that announces itself measures nothing about the checker. It is
   reported as a stratum, not corrected away — the honest alternative to pretending it is absent.
5. Base-model reuse means mutants are **not independent of each other**; per-class counts are
   therefore reported with the class as the unit of aggregation and this is stated wherever
   percentages appear.

**Pre-registered expectation fields, authored from the specification and the model text only,
before any validator run over the corpus** (`mutants/MANIFEST.csv`):

`mutant_id, base_model, fault_class, spec_constraint_or_defect, expected_layer, expected_detectable, rationale, plausibility, surface_tell, sha256`

`expected_detectable` ∈ {yes, no, uncertain}, and the reason must be spec-side (the condition is
named / not named / the outcome depends on whether the tool materialises the construct), never
instrument-side-observed.

**Freeze procedure.** `mutants/MANIFEST.csv` and every mutant file are hashed into
`mutants/expectations.sha256` and `mutants/mutants.sha256` **before the first run over the
corpus**. Hashes are quoted in the report. Expectations are never revised after seeing results;
if a revision is genuinely needed it is appended as a dated row in `mutants/MANIFEST-REVISIONS.md`
with the reason and both values are reported.

## 5. Known-good corpus and its independence basis

Ten small models (target 10–30 lines) in `known-good/`, each with a `PROVENANCE.md` stating:
where the text came from, **exactly which declarations are quoted from the source and which I
supplied**, and a **constraint-level argument for why it is believed valid** — not "the validator
accepted it". Independence basis, in descending strength:

- **Type S — specification example.** Quoted from the pinned SysML 2.0 Part 1 PDF
  (`formal/2026-03-02`, sha256 `46e6c047…a84a83a`, retrieved via the copy already verified against
  the catalogue's pinned hash at `/tmp/sysml/sysml-2.0-language.pdf`). Declarations the fragment
  references but does not declare are supplied by me and listed per model. This is independent of
  both the mutant author and the instrument.
- **Type A — authored pattern.** Canonical constructs I wrote (quantity/unit usage over the
  normative ISQ/SI libraries), **labelled authored**, with the argument that they violate no
  constraint I can name, listed constraint by constraint. Weaker independence, stated as such.

Every firing on a known-good model is triaged into exactly one of:
**(i) genuine defect I missed** (then the model is not known-good; recorded, and excluded from the
false-positive denominator with the reason), **(ii) validator over-reach / legal-but-flagged**,
**(iii) confound** (missing import, library resolution, feature-name shadowing of a unit symbol,
harness artefact). Only (ii) counts as a false positive. The triage is reported, not just the
raw count.

## 6. Instruments, pinned

| Instrument | Version / identity | Status |
|---|---|---|
| OpenSysML CLI | `sysml v0.12.1`, commit `b2f0e9b802a334369da94312c35cefbd8726d3bf`, binary sha256 `ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0`, asset sha256 `0f16d282ec50bfda916e74ef102e5b257bf2c9964f6e44df9db495db4fc96210` | primary; the only instrument |
| OMG SysML v2 Pilot Implementation | targets SysML 2.1 Beta 2 / KerML 1.1 Beta 2 | **bounded attempt**, 20 minutes, JVM absent and no CLI release asset — outcome logged in `second-validator-attempt.md` |
| Syside (Sensmetry) | commercial | **access boundary** — licence required, not bypassed, out of scope |

**One-instrument warning, stated here and repeated in the report:** every rate below is a
property of *this binary at this version*. It is not "the false-negative rate of SysML v2
validators".

## 7. Pre-registered hypotheses

Stated before the run; each is falsifiable and each is reported as held / not held / partly held.

- **H1.** F1 (syntax) and F2 (unresolved) mutants are detected as errors in 8/8 cases. These are
  the instrument's core business and both layers are advertised.
- **H2.** F3 (kind mismatch) and F4 (multiplicity) error-detection is between 50% and 100% per
  class — expected to be *less* reliable than H1 because F3 has no named constraint and F4 has
  two sub-cases with none.
- **H3.** F5 (named constraints) is the most variable class: at least one of the four is caught
  as an error and at least one is not, i.e. 1–3 of 4. Rationale: obligation is graded
  (SHOULD/MAY), one target is reached only through `[TODO]` methods in the reference
  implementation, and one is prose-only.
- **H4.** F6 (quantity/unit) is detected in at least 2 of 4, and at least one of the four is
  caught only as a *warning*, not an error.
- **H5.** F7 (structural/architectural) is detected as an error in **0 of 4**, and at least 2 of
  the 4 produce *no diagnostic at all*. This is the pilot's central prediction.
- **H6.** F8 (metadata mis-typing) is detected in at least 3 of 4 — the documented
  "silently ignored" behaviour is the *pilot implementation's*, and this instrument advertises
  metadata codes, so the gap may not transfer.
- **H7.** Overall error-severity sensitivity across 32 mutants is between 0.50 and 0.85 inclusive.
  (A near-1.0 result would falsify the reliability concern; near-0 would suggest the corpus is
  unfair rather than the tool blind.)
- **H8.** Mutants flagged `surface_tell = yes` are detected at a **higher** rate than those
  flagged `no`; the difference is reported with its (small-N) uncertainty, and no causal claim is
  made.
- **H9.** At least two fault classes have (a) no mutant detected by any available checker **and**
  (b) no named constraint in the 623-row catalogue or the 38-row prose-only register — i.e. an
  *oracle* gap, not a tooling gap.

## 8. Measurement definitions (fixed before the run)

Fixed now so that no definition can be chosen to fit an outcome.

- **Diagnostic** — one entry in the JSON envelope's `diagnostics[]`, with `severity`, `code`,
  `pass`, `line`, `column`, `message`.
- **Detected (as error)** — the run's diagnostics contain ≥1 entry with `severity == "error"`.
  This is the primary measure. The JSON `exit` code is recorded but is not the criterion, because
  a nonzero exit can also arise from a warning policy.
- **Detected at the wrong severity** — no error-severity diagnostic, but ≥1 `warning`-severity
  diagnostic. Reported per class; counted as **not detected** for the primary measure.
- **Relevant vs incidental** — for each mutant I record whether the diagnostic is *about the
  injected defect* (`relevant`) or merely *present* (`incidental`: the run errored, but on a
  condition unrelated to the injected one). This judgement is post-hoc and made against the
  frozen `spec_constraint_or_defect` text; it can never change `expected_detectable`. Both
  numbers are reported: "any error" (mechanical, no judgement) and "relevant error" (judged).
- **Silent** — zero diagnostics of any severity.
- **Layer confusion** — expected layer (§3) × the `pass` field of the highest-severity emitted
  diagnostic. Emitted layers are the instrument's own (`syntax`, `name-resolution`, `typing`,
  constraints by code family, `none`).
- **Message quality**, pre-stated criterion. A relevant diagnostic is
  - **naming** if its `code` or `message` names the violated condition or the defective construct
    in terms a reader could act on (e.g. names the feature, the unit, the kind); or
  - **generic** if it says only that something is wrong at a location, with no identification.
  *Misleading* is reserved for the case where the emitted error is **incidental** (it names a
  different condition than the injected one), which is what would send a reviewer to the wrong
  place. These three categories are exhaustive by construction.
- **Short-circuit** is recorded as a measured property: `did not analyse cleanly; no check was
  made`. A mutant whose defect triggers a syntax/name error cannot also test later layers; this
  is reported as a ceiling on what later classes can demonstrate, not as a tool defect.

## 9. Metrics and denominators

Let *n_c* = mutants in class *c* (4), *N* = 32, *G* = known-good models (10).

| Metric | Definition | Denominator |
|---|---|---|
| M1 per-class error sensitivity | relevant error-detected mutants / *n_c* | per class, *n_c* = 4 |
| M2 per-class any-error | any-error mutants (mechanical, before relevance triage) / *n_c* | per class |
| M3 per-class any-signal | mutants with ≥1 diagnostic of any severity / *n_c* | per class |
| M4 overall error sensitivity | relevant error-detected / *N* | 32 |
| M5 severity misses | mutants detected only as warnings / *N* | 32 |
| M6 silence | mutants with no diagnostic / *N* | 32 |
| M7 false-positive rate | known-good models with ≥1 over-reach error / *G* (after triage) | 10 |
| M8 oracle gap | classes with M1 = 0, split by whether a named constraint exists | 8 classes |
| M9 surface-tell stratum | M1 restricted to `surface_tell = yes` vs `no` | per stratum |

**Uncertainty.** Wilson score 95% intervals are reported for every proportion. At *n_c* = 4 these
intervals span roughly 0.15–0.85 for a point estimate of 0.5 — that width **is** the finding and
is not hidden behind a point estimate. No significance test is applied to the surface-tell
stratum; the difference and its interval overlap are reported as descriptive only.

## 10. Analysis plan (fixed)

1. Run the harness over `known-good/` and `mutants/`; raw JSON preserved unedited per file.
2. Re-derive every rate from the tidy CSV, not from the raw files by hand.
3. Per class: M1–M3 with intervals; then the expected-layer × emitted-layer confusion view.
4. Per mutant: detected / wrong-severity / incidental / silent, plus message-quality label.
5. Oracle-gap table: each class with its *specification* status (named constraint / prose-only /
   not named), so a zero can be read as tooling gap or oracle gap. **This table is the
   deliverable.**
6. Surface-tell stratum.
7. Known-good triage table.
8. Explicit limitations: one instrument; N = 32; author-as-mutator; mutants synthetic and derived
   from 10 bases; version skew (2.0/1.0 catalogue vs a tool whose `-version` states v0.12.1 and
   whose README states a SysML 2.1/KerML 1.1 target); author had read the instrument's `-explain`
   code list; relevance triage is post-hoc and single-coder.

## 11. Exclusions (from issue #8, honoured)

- Not a bug report against OpenSysML and not a conformance assessment. Diagnostics are recorded
  as observations, never as defects to be filed.
- No attempt to fix, extend or improve any validator, and no domain rules added.
- No adversarial inputs: plausibility rule §4.3 excludes them by construction, and any mutant that
  fails the plausibility criterion at review is marked, not deleted.
- No paid or enterprise licence; Syside's licence check is not bypassed.
- No claim of representativeness: the fault model is derived from the specification, *not*
  validated against observed generation errors. That validation is issue #7's job and arrives as
  the separate external challenge set in the later phase; it is out of scope here and its absence
  is a stated limitation of every rate in this pilot.

## 12. Threats to validity (enumerated before the results, deliberately)

1. **Author-as-mutator.** One agent authored the base models, injected the faults, wrote the
   expectations, wrote the harness and judged relevance. No independent second coder (issue #8
   asks for one). Mitigation: expectations hashed before the run; the mechanical "any error"
   measure is reported next to the judged one; the mutant diffs are published for anyone to
   re-judge.
2. **Surface tell.** A mutant can be caught for a reason other than the injected defect. Flagged
   per mutant, stratified in §9/M9.
3. **Unfair fault model.** If the classes were chosen to be undetectable, the sensitivity figure
   would be an artefact. Mitigation: two classes (F1, F2) are the instrument's advertised core
   and are expected at 8/8; the per-class table shows the spread rather than one number.
4. **One-instrument risk.** No second validator. Version skew and implementation-specific
   behaviour cannot be separated from SysML v2 validation as such.
5. **Version skew.** The catalogue is SysML 2.0 / KerML 1.0. The instrument's self-description is
   a SysML 2.1 / KerML 1.1 implementation, and the pinned binary reports only `v0.12.1`. A mutant
   may legitimately differ between 2.0 and 2.1 beta semantics; where I know of such a case it is
   flagged in the mutant's rationale, and no such case is claimed to be settled.
6. **The author had read the instrument's `-explain` code list** before writing expectations
   (logged in `results/calibration/PRE-FREEZE-CALIBRATION.md`). This biases expectations *towards*
   the instrument's advertised capability. It cannot be undone; it is disclosed. The expectation
   is nonetheless anchored to a specification constraint, and H5/H9 predict silence despite the
   author having seen the code list.
7. **Small N.** 32 mutants, 10 known-good models, 4 per class. Every rate is coarse; the report
   says so wherever a rate appears.
8. **Base-model reuse.** Mutants within a class share bases, so they are not independent samples.
9. **Known-good ≠ correct.** The known-good corpus is small models believed valid by constraint
   argument. A hidden defect would understate the false-positive rate (it would look like a
   false positive) — hence the triage categories in §5.
10. **Short-circuit ceiling.** If early layers fire on later-layer mutants, later classes are
    measured on a subset. Reported per mutant.
11. **Scope of "available"** — one instrument. The claim is about *this* tool. Two other candidate
    instruments exist and are unavailable for lawful, non-bypassing reasons; that is itself part
    of the answer to "available validators".

## 13. Artefact plan

```
research/issue-008/
  METHODOLOGY-FROZEN.md          this file
  README.md                      index + reproduce commands
  known-good/*.sysml + PROVENANCE.md per model
  mutants/*.sysml + MANIFEST.csv + mutants.sha256 + expectations.sha256
  harness/run_validators.py      runnable offline, never edits raw output
  results/raw/<model>/<case>.json  unedited validator output
  results/results.csv            tidy per-mutant/per-case rows
  results/run-log.md             tool identity, hashes, argv, timestamps, exit codes
  results/analysis.md/.json      the analysis
  results/calibration/           pre-freeze probes (not corpus)
  results/known-good-triage.md   the (i)/(ii)/(iii) triage
  second-validator-attempt.md    bounded attempt + exact failure
reports/issue-008-validator-reliability-pilot.md
```

## 14. Amendments

None at freeze. Any later amendment is appended here with UTC date, reason, and the superseded
text quoted, and is reported in the report and in the PR.

*Pre-freeze correction, 2026-11-13T14:08Z:* the first draft carried a forward-dated freeze
timestamp (14:10Z) taken from the shell clock before the file was finished. It was corrected to
the actual freeze time **before the file was hashed into `methodology.sha256` and before any hash
was quoted in any other artefact**. No other text was changed.
