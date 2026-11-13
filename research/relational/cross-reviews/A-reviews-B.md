# A reviews B — do the synthetic mutants represent errors that actually occur?

**Reviewer:** Researcher A (issue #7 pilot: observed error population)
**Author under review:** Researcher B (issue #8 pilot: mutation-based validator evaluation)
**Date:** 2026-11-13T14:22Z (UTC), after Gate 1 passed and Gate 2 opened.
**Scope of this review:** the representativeness and realism of B's fault model and mutants, the
independence of B's pre-registered expectations, and whether B's fault model omits error classes my
corpus contains — with what each omission does to B's sensitivity figure.
**Independence:** I wrote this before `research/relational/cross-reviews/B-reviews-A.md` existed, and
I have not read it. I have not read B's methodology in full, only `METHODOLOGY-FROZEN.md` §7/§12 via
the report's quotations and the artefacts named below; I state where that limits my judgement.
**What I read:** `reports/issue-008-validator-reliability-pilot.md`; `research/issue-008/mutants/
MANIFEST.csv`, `FREEZE.md`, `mutants.sha256`, `expectations.sha256`, 13 mutant files in full;
`harness/author_manifest.py` (tail) and `harness/make_mutants.py` (structure, via MANIFEST
rationales); `results/results.csv` and `results/run-log-run1.md`; `known-good/KG-05`, `KG-07`,
`KG-09`; and my own corpus, coding and detection artefacts under `research/issue-007/`.
**Write scope:** this file, and probe evidence under
`research/issue-007/detection/cross-review-probes/`. **I edited nothing of B's.**

---

## 1. Bottom line

**B's mutants are better built than their representativeness warrants, and one headline claim is
falsified by an invocation B disclosed but did not run.**

The construction is careful: single-defect substitutions, specification-anchored bases with
provenance, expectations frozen and hashed before the first run (I verified both hashes and the
timeline), pre-registered hypotheses that are allowed to fail (H9 does fail), and a report that
volunteers most of its own weaknesses. Measured against the error population that actually occurred
in my corpus, however, B's fault model names eight plausible families but instantiates each in one
specific, specification-flavoured form — and several of the specific forms are not the ones a
generator produces. My corpus's dominant reference defect is a dangling `satisfy … by <name>`; B
tests type-reference typos. My corpus's dominant notation defect is a reserved keyword used as a
name; B tests a missing semicolon and an extra brace. Those substitutions are not cosmetic: the
detection outcomes differ (dangling `satisfy` 4/4 detected, dangling succession source 0/1 silent;
reserved-keyword is an *error-severity* diagnostic with **exit 0** in default mode, unlike every
mutant in F1).

And the strongest claim — that four structural defects are **invisible to the only available
instrument** — is not supported as worded. Under `-instantiate vehicle -validate=vehicle`, the
pinned binary reports

```
✗ satisfy vehicleMaximumMass by vehicle fails (on KG07Requirements::vehicle ID: 1)
  Required condition evaluated to false: massActual <= massRequired
✗ KG07Requirements::vehicle is not valid: 1 of 1 assertion fails
[exit 1]
```

on B's own F7-02 mutant, and `holds` / `exit 0` on its known-good base. The class is detectable by
that instrument, with a correct positive control; what B measured is the blindness of the **default
`-validate` path**, not of the instrument. The verdict arrives in a different envelope
(`{"status": "fails", "checks": [...]}`, not `diagnostics[]` with error codes), so B's primary
measure could not have counted it even if the mode had been run — which is itself part of the
objection (O2). Evidence and commands: §5 O1, probe log in
`research/issue-007/detection/cross-review-probes/PROBES.md`.

**Objection counts: 13 — 1 blocking, 7 material, 5 minor.** Table at §6.

---

## 2. Representativeness, class by class (mandate item 1)

For each of B's classes: does my corpus contain the class at all; and does B's mutant instantiate
that class or a different condition wearing the class name? My evidence is
`research/issue-007/coding/errors.csv` (frozen, 14 records) and `errors-post-inspection.csv`
(7 further records verified against SysML 2.0 §8.2.2.1.2).

| B class | In my corpus? | My records | Does B's mutant instantiate the same condition? |
|---|---|---|---|
| **F1 syntax / notation** | **Yes** — 3 frozen / 9 combined (S1) | T1-C2 `satisfy greenhouse to moistureControl;` (E01); T2-C1 `transition from … to … on …` (E01, 4 occurrences); T3-C2 `port in;`/`line.in` (E01); post-inspection: T2-C2 `attribute state : String;`, T4-C1 `action def assign;`, T6-C1/T6-C2/T6-C3 `port return;`, T5-C3 `port return;` | **Partly.** Missing semicolon (F1-01), extra brace (F1-02) and keyword typo (F1-03) instantiate notation defects, but **none of the four is the empirical mechanism**: **7 of my 9 notation records (7 models)** are *reserved keyword used as an unquoted name* (a *distinct* diagnostic, `reserved-keyword-name`), 1 is a wrong keyword in a construct (`to` for `by`), 1 is a SysML-v1 idiom. F1-04 (unquoted shortname) is a notation defect my corpus never produces (§5 O9). |
| **F2 unresolved reference** | **Yes** — 5 frozen (N1) + 1 (N2) | T1-C1 `first start;` (dangling succession source); T3-C2/T4-C2/T5-C2/T6-C2 `satisfy … by <subject parameter of the requirement def>`; T3-C1 missing `ScalarValues` prelude (10 occurrences) | **Partly, and site-dependently.** F2-01/02/03 are typos in type, parameter and redefinition targets; F2-04 is an undeclared type. All four are *type-position* references. The empirical dominant site is the **satisfying feature of a `satisfy`**, and the second is a **succession source**; detection differs by site: my satisfy-site records are 4/4 detected, my succession-source record is silent (§5 O5). |
| **F3 kind / type mismatch** | **Yes** — 2 frozen/combined (T1, T2) | T4-C1 `first checkCharge;` where `checkCharge` is an `action def` (T1); T5-C3 `attribute window : VisibilityWindow;` where `VisibilityWindow` is a `part def` (T2, post-inspection) | **Yes for one of the four.** F3-02 (`attribute` typed by a `part def`) is **the same condition as my T2**, reached independently by mutation; that is genuine corroboration. F3-01 (part typed by port def) is the mirror case and plausible. F3-03 (state replaced by action) and F3-04 (subject typed by a requirement) are different conditions; my corpus has no instance of either. |
| **F4 multiplicity** | **No** — my corpus uses multiplicities legally (`[2]`, `[10]`, `[1..*]`) | — | **Neither instantiates my adjacent class.** My structural defect R1 is a connector whose *end expression chains through* a multi-valued usage (`T4-C1:51`, `T4-C3:56`), which the tool passes silently. B's F4-02 puts an explicit multiplicity on an `end part` feature, which the tool reports as a *warning*. Different condition, different outcome; F4 says nothing about R1. |
| **F5 named constraint** | **Yes** — 1 frozen (S2) | T2-C2 `satisfy lowerBeforeArrival;` with no satisfying feature — `checkSatisfyRequirementUsageBindingConnector` (§8.3.21.10), class A, SHOULD; **silent** under the pinned tool | **No.** F5-02 is a *wrong-kind* satisfy target (`satisfy Vehicle by vehicle`), which is `validateSatisfyRequirementUsageReference`, and it is **detected**. My S2 is the same construct family, a *different named constraint*, and is **not** detected. Adding S2 to F5 changes F5 from 3/4 = 0.75 to **3/5 = 0.60** (§4). |
| **F6 quantity / unit** | **No** — 0/18 of my models use units or ISO/ISQ libraries | — | Not assessable from my corpus. B's three quantity mutants are internally coherent as defects; whether generators asked for "structure + requirement + behaviour" emit unit-typed quantities at all is untested — my eighteen did not. |
| **F7 structural / architectural** | **Yes** — 3 frozen (R1×2, I1) | T4-C1/T4-C3 multi-valued connectors (R1); T1-C3 requirement documentation "35 %–75 %" against its own `upperBound = 55.0` (I1) | **No, but the direction replicates.** None of B's four F7 mutants is R1 or I1, yet both classes are **silent** under every invocation I tried — independent corroboration that the default path is blind to structural/semantic defects. B's F7-02, however, is *not* silent under `-instantiate` (§5 O1), and F7-04 becomes "undecided", not silent (O2). |
| **F8 metadata / annotation** | **No** — 0/18 models contain a metadata annotation; my prompts never asked for one | — | Not assessable from my corpus. B's F8-02 (`levle = 3;` in a metadata body) is a realistic typo *within a construct my corpus never emits*. |

**Reading.** Six of B's eight classes have an empirical counterpart in my corpus, but in only one
class (F3, via F3-02) does a B mutant instantiate the *same condition* as an observed error. In F1,
F2, F4 and F5 the mutant tests a neighbouring condition, and in three of those the detection outcome
differs from the observed class. That is the central representativeness objection: **B's classes are
right; its instances are specification-flavoured specimens of them.**

---

## 3. Mutant realism, sampled (mandate item 2)

I read 13 mutants in full: all four F7, plus F1-04, F2-04, F3-01, F3-04, F4-02, F5-01, F5-02,
F6-03, F8-02. Judgement: *could a generator plausibly emit this text?* — with the caveat that "a
generator" here means a single-shot LLM asked for structure + requirement + behaviour, i.e. what my
corpus is.

| Mutant | File:line of the injected defect | Plausible generator output? | Why |
|---|---|---|---|
| F1-04 unquoted shortname | `M31-F1-04-unquoted-shortname.sysml:13` `requirement def <1.1> MaximumMass` | **Weakly** | Short-name quoting `<'…'>` is a spec-idiom construct; 0/18 of my models used a short name at all. A generator is more likely to omit the *whole* short name than to unquote it. |
| F2-04 missing declaration | `…F2-04-missing-declaration.sysml:20` `part wheels[4] : Wheel;` with `Wheel` undeclared | **Yes** | Exactly the shape of 4 of my 5 N1 records (a name used, never declared), though at a different site (type vs satisfy target). |
| F3-01 part typed by port def | `…F3-01-part-typed-by-portdef.sysml:15` `part fuelOutPort : FuelingPort;` | **Yes** | Kind confusion between `part` and `port` is a plausible single-token slip; I emitted the mirror case (`attribute : PartDef`) myself. |
| F3-04 subject typed by requirement | `…F3-04-subject-typed-by-requirement.sysml:33` `subject v : MaximumMass;` | **Yes** | The two names are both in scope and semantically adjacent; a generator reaching for "the vehicle thing" can pick the requirement definition. |
| F4-02 end-feature multiplicity | `…F4-02-end-feature-multiplicity.sysml:11` `end part hub : Hub[2];` | **Plausible but unobserved** | Requires a `connection def` with explicit `end` features — a construct 0/18 of my models wrote. The "hub is plural" story is coherent; the construct surface is not the one generators reach for. |
| F5-01 feature-value overriding | `…F5-01-feature-value-overriding.sysml:13,17` `attribute cutoff : Integer = 0.75 * averageScore;` vs `:> TestRecord` with `default =` | **Plausible** | The `=`/`default =` distinction is a documented generator trap, and this is the Sensmetry case; but it depends on redefinition-with-feature-value, absent from my corpus. |
| F5-02 satisfy reference | `…F5-02-satisfy-reference.sysml:38` `satisfy Vehicle by vehicle;` | **Yes** | My corpus's satisfy errors are the same family (wrong *what* after `by`), and this one is the more "semantically adjacent" slip. Good mutant. |
| F6-03 incommensurable sum | `…F6-03-incommensurable-sum.sysml:13-14` `EnergyValue = unladenMass + ratedSpeed;` | **Yes** | Adding quantities of different dimensions is a classic LLM slip; but it requires unit-typed attributes, which my prompts never elicited. |
| F7-01 unreachable state | base `KG-05-states.sysml:17` deleted; the mutant keeps only `first starting then on;` (`M31-F7-01-unreachable-state.sysml:17`) | **Yes** | I checked the base (`KG-05-states.sysml:17-18`): it does contain `first off then starting;`, so the deletion is the single change and the base machine is reachable. A generator that emits states and forgets one transition produces exactly this. **Cleared.** |
| F7-02 satisfied-but-violated | `…F7-02-satisfied-but-violated.sysml:34-35` `massActual = 2500.0` against `massRequired = 2000.0`, with `satisfy … by vehicle` | **Yes** | Inventing plausible numbers that violate the stated bound is *the* characteristic LLM failure. But note the construct: the numbers are bound on the requirement usage, so the model is checkable — which is why the instrument can decide it (§5 O1). |
| F7-03 missing flow | base `KG-09-actions.sysml:27` (`flow focus.image to shoot.image;`) deleted; the mutant's `shoot` therefore has no supplier for `in image` | **Yes — and my corpus is full of its shape** | I checked the base (`KG-09-actions.sysml:27`): it has the flow, the mutant removes it, one defect. By this criterion **10 of my 18 models** have action sequencing with parameters and **no `bind` and no `flow` at all** — a materially important finding *against my own pilot* (§7). |
| F7-04 contradictory assertions | `…F7-04-contradictory-assertions.sysml:9-10` `assert constraint { computedMass >= 0.0 }` / `< 0.0` | **Yes, within a construct my corpus never emits** | Two contradictory assertions is plausible; 0/18 of my models contain any `assert constraint` or `require constraint`, so the empirical frequency of this construct is unknown and probably low for simple prompts. |
| F8-02 metadata body typo | `…F8-02-body-feature-typo.sysml:18` `@SafetyRelevant { levle = 3; }` | **Yes, inside metadata** | A one-character typo is plausible; but metadata annotations are absent from my corpus, so the class is untested empirically. |

**Verdict on realism.** No mutant is adversarial or artificial in the sense of "no generator could
emit this". Two are weakly representative because the *construct* is spec-flavoured rather than
generation-flavoured (F1-04 short names; F7-04 asserts), and several depend on constructs absent
from my corpus (F4 `connection def`, F6 units, F8 metadata). The realism problem is therefore not
per-mutant implausibility but **construct-surface selection**: B's material lives largely on the
specification's demonstration surface (quantities, asserts, metadata, conjunction), while the models
my generator produced live almost entirely on declaration + requirement-usage + connection surface.

---

## 4. Ground truth independence (mandate item 3) and omissions (item 4)

### 4.1 Hashes and timeline — verified

| Artefact | Recorded | Recomputed by me | Verdict |
|---|---|---|---|
| `METHODOLOGY-FROZEN.md` | `2c80d63e…6f00b` | matches | ✓ |
| `mutants/MANIFEST.csv` | `a9f47974…57be7` | matches | ✓ content |
| `harness/author_manifest.py` | `40c75cef…84432` | matches | ✓ |
| `mutants/expectations.sha256` | — | contains the MANIFEST hash | ✓ |

Timeline (local mtimes, UTC+1): `author_manifest.py` 15:12:52 → `expectations.sha256` 15:13:00 →
`FREEZE.md` 15:13:02 → first validator run `run1` **15:13:03**. The expectations file is older than
the run and its recorded hash equals the file's current content. **I could not find evidence that an
expectation was changed after the run.** One blemish: `MANIFEST.csv`'s mtime is 15:15:56, i.e. *after*
the run, although its content hash equals the pre-run value; `author_manifest.py` rewrites the file
idempotently (its tail writes `MANIFEST.csv`), so an identical-content regeneration explains it. Not
evidence of fitting — but it should have been logged (§5 O11).

### 4.2 The `-explain` disclosure — consequence assessed

B read the instrument's diagnostic inventory before authoring expectations (disclosed in the report
§4.1 and methodology §12.6). Consequence, measured against B's own audit:

- The **detection numbers do not depend on the expectations at all**: 23/32 is computed from raw
  diagnostics. Anchoring cannot move the headline.
- The **expectation audit is softened**: 24/24 of the "expected detectable" bucket produced some
  diagnostic, and the only two expectation errors are in the "expected not detectable" bucket, in
  the direction of *under*-predicting the tool (F4-01 inverted bounds, F6-02 missing unit, both
  reported as errors). That is the signature of expectations written with the tool's vocabulary in
  view, even if unconsciously. The pre-registration still bound the *report* (H9 failed and is
  reported as failed), so this is not fatal — but "expectations were authored from the
  specification alone" is not a claim the artefacts can support, and B does not make it.
- Practical consequence for a reader: treat B's `expected_layer` labels as the *tool's* layer names,
  not independent ones. `expected_layer` for F2 is `names`, F3/F6 `typing`, F4 partly `typing` and
  `constraints` — that is the instrument's own taxonomy.

### 4.3 Classes my corpus shows that B's fault model omits

| My class (records) | In B's model? | Consequence for B's figures |
|---|---|---|
| **S1 subset: reserved keyword as an unquoted name** (6 of 9 S1 records; 5 models) | **No** | Adds an F1 sub-class the tool reports as `error[reserved-keyword-name]` **with exit code 0** in default mode (`-strict` makes it exit 2 — probe in §8). B's F1 mutants all exit 2. So F1's 4/4 and B's exit-status discussion do not transfer to the empirical notation class. |
| **N2 missing standard-library prelude** (1 model, 10 occurrences) | **No** | The exact confound `TOOLING.md` warns about. B's bases all import `ScalarValues` (verified: 10/10), so B cannot report whether an "unresolved" diagnostic distinguishes a forgotten import from a dangling name. My data shows the message does ("did you mean `ScalarValues::Real`"), but B's corpus never tests it. |
| **S2 satisfy with no satisfying feature** (1) | **No** | A named, class-A, SHOULD constraint silently missed. F5 → 3/5 = 0.60. |
| **R1 connector end over a multi-valued usage** (2) | **No** (F4-02 is a different condition) | Silent under every mode I tried; corroborates F7's blindness but adds a *structural* class B does not sample. |
| **I1 documentation/value contradiction** (1) | **No** (F7-04 is assert-vs-assert) | Silent; second independent structural/semantic class B does not sample. |
| *(candidate, not coded by me)* **duplicate member names / `name-conflict`** | **No** | The tool diagnoses `name-conflict` in **10 of 24** independent single-shot artefacts from an external corpus I sampled (140 diagnostics: 119 `name-conflict`). I did not hand-verify those 10, so this is a candidate class, not a codebook record — but it is a class that occurs at a visible rate in generated text and is absent from B's model, and the tool *does* report it (as a warning, exit 0). |

**Effect on the headline if my observed distribution replaced B's sampling frame.** Mapping my
records to B's measure ("relevant error-severity detection") and using my own detection results
(`research/issue-007/detection/table.md`):

| Population | n | detected | rate |
|---|---|---|---|
| B's mutants | 32 | 23 | **0.72** |
| My frozen error population | 14 | 9 | **0.64** |
| My population incl. post-inspection verified records | 21 | 15 | **0.71** |

So the **aggregate is coincidentally stable** (0.64–0.72 across three frames), and I will not claim
B's headline is inflated. What is not stable is the per-class picture: with the empirical records
added, **F5 falls from 0.75 to 0.60** (a named SHOULD constraint silently missed on the satisfying
feature), **F1 becomes 12/13 but with a sub-class that exits 0**, and **F7 gains one detection under
`-instantiate` (1/4) plus one "undecided" (F7-04)**, which B's binary measure cannot express. The
honest reading is: *B's overall sensitivity is a reasonable central estimate; its per-class claims
and its severity/exit-code story need the empirical classes added.*

---

## 5. Objections, with severity and what would settle each

### O1 — **BLOCKING** — F7-02 is detectable by the pinned instrument; "invisible to the only available instrument" is not supported

**Evidence.** On B's own mutant, with the same pinned binary:

```
$ .tools/sysml -instantiate vehicle -validate=vehicle \
    research/issue-008/mutants/M31-F7-02-satisfied-but-violated.sysml
✓ Created instance of KG07Requirements::vehicle
✗ satisfy vehicleMaximumMass by vehicle fails (on KG07Requirements::vehicle ID: 1)
  Required condition evaluated to false: massActual <= massRequired
✗ KG07Requirements::vehicle is not valid: 1 of 1 assertion fails
[exit 1]

$ .tools/sysml -instantiate vehicle -validate=vehicle research/issue-008/known-good/KG-07-requirements.sysml
✓ satisfy vehicleMaximumMass by vehicle holds … [exit 0]
```

The positive control on the known-good base holds, so this is not a spurious complaint: the
invocation discriminates the mutant from its base. `sysml -help` documents
`-validate[=<object>] … checks instead every assertion about that object`, and B's report §12.5
names this mode as an unexercised "plausible bridge". So the class is *not* invisible to the
instrument; it is invisible to the **default `-validate` invocation**, which is the only one B ran.

**Why it matters.** Report §1 says "it is **no evidence at all** about whether the model's structure
means what it claims", and P3 says "at least one class of plausible model defect is invisible to the
only available instrument". Both outrun the measurement: for requirement-satisfaction defects
encoded with a `require constraint`, the instrument *does* establish a violates/holds verdict.
**What would settle:** re-run the F7 arm with `-instantiate <object> -validate=<object>` (and
`-self-check`) per mutant, report a per-mode table, and restate P3 as a claim about the default
path. If the mode is judged out of scope, say so and say why — the current wording cannot stand
either way.

### O2 — **MATERIAL** — the instrument's assertion verdict is three-valued; B's binary measure has no category for "checked and undecided"

**Evidence.** `-instantiate testObject -validate=testObject` on B's F7-04 returns

```
? assert constraint could not be evaluated … no value for feature computedMass
? KG10Asserts::testObject is not shown valid: 2 of 2 assertions undecided
  standing: not covered (2 undecided)
[exit 2]
```

The instrument distinguishes *holds / violated / undecided / no assertion to validate*, and the
verdict schema is `checks[]` with a `standing`, not `diagnostics[]` with error codes
(`{"status": "fails", "checks": [{"subject": …, "standing": "violated (witnessed…)"}]}`). B's
`detected / not detected` measure is typed on error-severity diagnostics, so it collapses "checked
and undecided" into "not detected" and cannot represent "checked and violated" either; its
"wrong severity" category covers only warnings. For a semantic-checking instrument, "undecided" is
arguably the most informative outcome, and it is invisible in B's tables.
**What would settle:** add an outcome category for `undecided`/`not covered` and re-report the F7
arm; state the tri-state in the measurement definitions (§3.1).

### O3 — **MATERIAL** — the notation class is under-represented, and its exit-code behaviour differs from every F1 mutant

**Evidence.** 7 of my 9 notation records (in 7 models) are reserved keywords used as names (`port in;`, `port out;`,
`port return;`, `attribute state : …`, `action def assign;`), verified against the specification's
reserved-keyword list (SysML 2.0 §8.2.2.1.2). Default invocation reports
`error[reserved-keyword-name]` and **exits 0** ("no error that stops a check; the notation reported
above does not conform"); `-validate -strict` on the same file exits 2. B's four F1 mutants exit 2 in
default mode, so F1's 4/4 does not cover the empirical notation class, and B's discussion of
exit-status gating (§3.3, §11.3) covers only the *warning* case, not error-with-exit-0.
**What would settle:** one mutant of this form (I will supply it in the frozen empirical subset) run
in default and `-strict` modes, with the exit codes reported.

### O4 — **MATERIAL** — F5 tests a satisfy defect the tool catches; the empirical satisfy defect is one it misses

**Evidence.** B's F5-02 (`satisfy Vehicle by vehicle;`) is detected (`relationship-target-kind`).
My S2 record (`T2-C2:33`, `satisfy lowerBeforeArrival;`) violates
`checkSatisfyRequirementUsageBindingConnector` (§8.3.21.10, class A, SHOULD) and is silent — and
under instantiation the tool says "states no assertion to validate", i.e. it does not even form a
check. F5's 3/4 becomes 3/5 = 0.60 with the empirical record added.
**What would settle:** include the no-`by` mutant; if the tool's behaviour is judged correct
because the constraint is a discretionary `check`, then B's P4 ("some named SHOULD constraints are
not enforced") needs a *satisfy* example alongside `validateFeatureValueOverriding`, and the F5 rate
must be reported on the enlarged class.

### O5 — **MATERIAL** — F2's four mutants are all type-position references; detection is site-dependent

**Evidence.** My N1 splits by site: four dangling `satisfy … by <name>` records are **detected**
(`unresolved`), one dangling succession source (`T1-C1:64`, `first start;`) is **silent** — and a
minimal probe (`probe01_first_undefined_source.sysml`) reproduces the silence on a two-line construct
while an undefined name in an expression *is* reported (`probe04`). So resolution coverage is not
uniform across reference sites. B's F2 mutants are a type typo, a parameter typo, a redefinition
typo and an undeclared type — none at the succession or satisfy sites.
**What would settle:** add one mutant per site (succession source, satisfy target, binding end) and
report F2 per site; my corpus supplies the two observed sites.

### O6 — **MATERIAL** — the missing-prelude class is absent, so the documented confound is untested

**Evidence.** 10/10 of B's bases import `ScalarValues::*`; my T3-C1 does not, and produces 10
`unresolved` diagnostics whose message names `ScalarValues::Real`. `TOOLING.md` §1 explicitly warns
that "every mutant in the class 'unresolved reference' will be confounded with a missing stdlib
import". B's corpus is designed *around* the confound rather than measuring it.
**What would settle:** a mutant that deletes the prelude, and a report line on whether the
diagnostic distinguishes the two mechanisms — because a pipeline counting `unresolved` cannot.

### O7 — **MATERIAL** — construct-surface mismatch: B's fault material is built on constructs an 18-model generation corpus never emitted

**Evidence.** In my 18 models: `require constraint` / `assert constraint` / any `constraint { }` —
**0/18**; unit-typed attributes with ISQ/SI libraries — **0/18**; metadata annotations — **0/18**;
`connection def` with explicit `end` features — **0/18**; short names `<'…'>` — **0/18**. Those
constructs carry all of F5 (constraints), F6 (units), F7-02/F7-04 (assertions) and F8 (metadata), and
part of F3/F4. This is a two-way limitation: my prompts were simple, so my corpus may under-sample
these constructs; but B's claim that its fault model is "specification-derived by design" carries an
unexamined assumption that specification surface ≈ generation surface.
**What would settle:** a construct-frequency census over ≥200 generated models (issue #7's own
requirement), and either B's fault model reweighted by it or an explicit statement that the pilot
measures spec-surface defects, not generation-surface defects.

### O8 — **MATERIAL** — the `-explain` disclosure bounds what the expectation audit can claim

Assessed in §4.2. **What would settle:** expectations authored by an agent that has not read
`-explain`, or a second coder on the expectations; and a sentence in §3.1 that the `expected_layer`
vocabulary is the instrument's.

### O9 — **MINOR** — F1-04 (unquoted short name) is a spec-idiom construct

`requirement def <1.1> MaximumMass` — a generator that never writes short names cannot produce this
error; 0/18 of my models used a short name. Keep it as a notation probe, but do not count it toward
"notation defects generators make".
**What would settle:** state the construct-frequency assumption per mutant, or replace it with a
reserved-keyword mutant (O3).

### O10 — **MINOR** — F4-02's condition is not the empirical multiplicity/connection defect

`end part hub : Hub[2];` is a named-constraint violation (warning) on an explicit end feature. My R1
is a *chain through a multi-valued usage* in a `connect`, with no named constraint and no diagnostic.
Both are worth having; they are not the same class, and reporting F4 as coverage of "multiplicity"
overstates the connection surface.
**What would settle:** classify R1 explicitly (as F7-shaped structural), and say F4 covers declared
multiplicity, not connection-end structure.

### O11 — **MINOR** — provenance blemish: `MANIFEST.csv` mtime is after the first run

Content hash equals the pre-run recording, and `author_manifest.py` rewrites the file idempotently,
so I do not believe expectations were fitted; but an artefact whose mtime post-dates the run it
pre-registers should carry a one-line log entry saying what rewrote it.
**What would settle:** a line in `FREEZE.md` or the run log recording the regeneration.

### O12 — **MINOR** — "every emitted error was about the injected defect" measures the design, not the tool's specificity

Single-defect mutants guarantee relevance; cascades nevertheless produce 3 (`F1-03`) and 5 (`F1-04`)
error diagnostics for one defect. The equality any-error = relevant-error is a property of
one-substitution corpora; it should not be read as evidence that the tool does not over-report.
**What would settle:** report diagnostics-per-defect, and say the claim is about relevance, not
precision.

### O13 — **MINOR** — a candidate class with visible frequency is missing: duplicate member names

`name-conflict` appears in 10 of 24 independently generated artefacts I sampled (119 of 140
diagnostics). I did not hand-verify them, so I am not asserting it as a coded class — but a fault
model for generated SysML v2 that has no duplicate-name class is missing a condition that appears at
double-digit rates in generated text, and that the tool reports (as a warning, exit 0).
**What would settle:** hand-code the 10 artefacts (my external sample is on disk with hashes), then
add a class if confirmed.

---

## 6. Objection register

| ID | Objection | Severity | Settled by |
|---|---|---|---|
| O1 | F7-02 is detectable under `-instantiate … -validate`; P3/§1 overstate silence | **blocking** | re-run F7 with instantiation + assertion validation, per-mode table |
| O2 | tri-state verdict (holds/violated/undecided) not representable in B's measure | material | add outcome category, re-report F7 |
| O3 | reserved-keyword notation class absent; error-severity + exit 0 not covered | material | one mutant, default vs `-strict` |
| O4 | empirical satisfy defect (no satisfying feature) absent; F5 3/5 not 3/4 | material | include mutant; restate F5 |
| O5 | F2 all type-position; resolution is site-dependent (succession source silent) | material | one mutant per reference site |
| O6 | missing stdlib prelude absent; the documented confound is untested | material | prelude-deletion mutant |
| O7 | fault material lives on constructs 0/18 generated models emitted | material | construct census over ≥200 models, or scope the claim |
| O8 | `-explain` anchoring softens the expectation audit (numbers insulated) | material | independent expectation author; vocabulary note |
| O9 | F1-04 short-name construct rarely generated | minor | per-mutant construct-frequency note |
| O10 | F4-02 is not the empirical connection/multiplicity defect | minor | classify R1 explicitly |
| O11 | MANIFEST mtime post-dates the run (content unchanged) | minor | log the rewrite |
| O12 | any-error = relevant-error reflects design, not specificity | minor | diagnostics-per-defect |
| O13 | duplicate-name class missing (candidate, 10/24 external) | minor | hand-code the external sample |

---

## 7. Where B's work changes my view

Three places, and I state them against my own report:

1. **My corpus contains F7-03-shaped defects that I did not code.** B's F7-03 tests "a subaction's
   input is not supplied". By that criterion **10 of my 18 models** (`T1-C1, T1-C2, T1-C3, T2-C3,
   T4-C1, T4-C2, T4-C3, T5-C1, T5-C2, T5-C3`) contain action sequencing whose parameters are never
   bound or flowed. My codebook deliberately excluded them (semantic layer required *internal
   incoherence*, §4.1 of my codebook). The consequence is that my statement "almost no structural or
   semantic defects" is a statement about my codebook's conservatism, not about the models. If the
   codebook were extended with B's F7-03 criterion, my semantic layer would grow from 1 record to
   ~11 and my class distribution would look much more like B's fault model. B's cross-review of me
   will presumably say this; B is right to.
2. **My "exit 0 with an error diagnostic" finding is mode-dependent.** I reported it for the default
   invocation, which is what my detection column used. `-validate -strict` makes the same model exit
   2. My report should say "default mode", and my detection table is a default-mode measurement.
3. **My detection column understates the instrument's surface.** I ran only `-validate` (text and
   json). B's `-instantiate … -validate=<object>` probe shows a verdict facility I never exercised,
   and on my own T4-C3 it returns `satisfy … holds` (vacuously — see the caveat in §5 O1: a
   requirement whose only content is documentation and attributes has no assertion to falsify; 0/18
   of my models encode a checkable constraint, which is exactly why my corpus cannot show the
   facility's reach).

I also record one point **in B's favour** that the report does not make enough of: B's F3-02
(`attribute` typed by a `part def`) is the same defect I recorded independently as T2, from a
generator rather than from mutation. That is a small but genuine two-source convergence on a class,
and it is the strongest representativeness evidence in B's corpus.

---

## 8. Reproduce my probes

All commands below are read-only; verbatim output in
`research/issue-007/detection/cross-review-probes/PROBES.md`.

```bash
M=research/issue-008/mutants
.tools/sysml -instantiate vehicle -validate=vehicle $M/M31-F7-02-satisfied-but-violated.sysml   # exit 1, "fails"
.tools/sysml -instantiate vehicle -validate=vehicle research/issue-008/known-good/KG-07-requirements.sysml  # exit 0, "holds"
.tools/sysml -instantiate testObject -validate=testObject $M/M31-F7-04-contradictory-assertions.sysml       # "undecided"
.tools/sysml -self-check $M/M31-F7-01-unreachable-state.sysml    # 0 violations, exit 0
.tools/sysml -self-check $M/M31-F7-03-missing-flow.sysml         # 0 violations, exit 0
.tools/sysml -validate research/issue-007/corpus/normalized/T6-C1.sysml          # error[reserved-keyword-name], exit 0
.tools/sysml -validate -strict research/issue-007/corpus/normalized/T6-C1.sysml  # same diagnostic, exit 2
.tools/sysml -instantiate levelCrossing -validate=levelCrossing research/issue-007/corpus/normalized/T2-C2.sysml  # "states no assertion"
.tools/sysml -instantiate fleet -validate=fleet research/issue-007/corpus/normalized/T4-C3.sysml                 # "holds" (vacuous)
```

Hashes I recomputed: `METHODOLOGY-FROZEN.md` `2c80d63e…6f00b`; `MANIFEST.csv`
`a9f47974…57be7`; `author_manifest.py` `40c75cef…84432` — all match B's report.

---

## 9. What I did not assess

I did not audit B's harness code beyond the manifest writer, did not recompute the Wilson intervals
or the triage of the known-good warnings, did not test `make_mutants.py` for hidden second
substitutions beyond the single-substitution assertion and my own before/after reading of the five
mutants whose bases I opened, and did not assess B's known-good provenance arguments clause by
clause. Those belong to the independent reviewer and are outside my mandate as the researcher whose
corpus supplies the challenge set. My fatal-error-rate assessment is therefore about
representativeness, not about arithmetic.

---

## 10. Status of this review

**Frozen at 2026-11-13T14:22Z.** I will not revise it in place. My response to B's review of my work
(Gate 2 close) will be a separate dated record, and if any finding here is refuted I will say so
there rather than editing this file.
