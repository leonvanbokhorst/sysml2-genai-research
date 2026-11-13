# Researcher B responds to Researcher A's review — Gate 2 close

**Author:** Researcher B (issue #8 pilot).
**Reviewed artefact:** `research/relational/cross-reviews/A-reviews-B.md`, frozen by A at
2026-11-13T14:22Z, sha256 `05ca64ccaa4ceae4032ca36aa22f2090c5565449d021764a9da480bbbb1a8102`
(computed by me on the file I reviewed; recorded in `results/run-log-run2-modes.md`).
**Response written:** 2026-11-13T14:40Z.
**Task:** test each of A's 13 objections against the pinned instrument and record what changes.
Not to defend the report.
**Files I touched:** this file; `research/issue-008/harness/run_modes.py` (new);
`research/issue-008/results/raw/run2-modes/**` (new, 35 probe records);
`research/issue-008/results/probes-gate2/**` (new, 5 probe models);
`research/issue-008/results/modes-summary-run2-modes.csv`,
`results/probes-gate2-summary.csv`, `results/run-log-run2-modes.md` (new);
and **dated addenda A2–A9 appended to** `reports/issue-008-validator-reliability-pilot.md`.
**Nothing was deleted.** `METHODOLOGY-FROZEN.md`, `mutants/MANIFEST.csv`, `mutants/*.sysml` and every
result in `results/results.csv` are byte-identical to their frozen versions. `B-reviews-A.md` is
untouched.
My own review (`B-reviews-A.md`) is byte-identical to its Gate-2 version, sha256
`de2d99cea17587a9603e9602303873556db9b00f93d8101451c0db57be9af0b1`; the report was
`524beb75…` before the addenda below and is a different file after them, by design.

---

## 1. Rulings at a glance

| A's objection | Severity A gave it | My ruling | Effect on a published number |
|---|---|---|---|
| O1 F7-02 detectable via `-instantiate … -validate=` | blocking | **ACCEPT** | F7 0/4 → **1/4 violated, 1/4 undecided, 2/4 silent**; overall 23/32 → **24/32 = 0.75** mode-aware |
| O2 tri-state verdict not representable | material | **ACCEPT** | new outcome category; F7-04 reclassified silent → **undecided** |
| O3 reserved-keyword notation class absent | material | **ACCEPT** | F1 4/4 retained for my mutants + **new observed sub-class** with exit 0 / `-strict` exit 2 |
| O4 F5 tests a satisfy defect the tool catches | material | **ACCEPT** | F5 3/4 → **3/5 = 0.60** on the cross-corpus union (both reported) |
| O5 F2 detection is site-dependent | material | **ACCEPT** | F2 4/4 holds **only at the sites tested**; 0/1 at succession sources |
| O6 missing-prelude class absent | material | **ACCEPT, with a refinement** | new probe; the confound is real *and* the message distinguishes it |
| O7 construct-surface mismatch | material | **ACCEPT as scope** | new limits paragraph; one of A's own counts corrected (3/18 import SI/ISQ) |
| O8 `-explain` anchoring | material | **ACCEPT** | expectation-audit wording corrected; detection numbers unaffected |
| O9 F1-04 is a spec-idiom construct | minor | **ACCEPT** | per-mutant construct-frequency assumption stated |
| O10 F4-02 ≠ the empirical connection defect | minor | **ACCEPT** | F4 relabelled as declared multiplicity, not connection surface |
| O11 MANIFEST mtime post-dates the run | minor | **ACCEPT** | cause identified and logged |
| O12 any-error = relevant-error reflects design | minor | **ACCEPT** | diagnostics-per-defect reported (24/28 exactly one) |
| O13 duplicate-name class missing | minor | **PARTLY ACCEPT** | confirmed as a missing class; my known-good arm shows the diagnostic is also unreliable |

**12 accept, 1 partly accept, 0 reject.** A found one thing that was simply wrong in my report
(O1), and it was wrong in the way that matters most: I claimed a class was invisible to the only
available instrument when the instrument decides it under an invocation I had read about, named in
my own report as an unexercised bridge, and did not run.

**Verification of A's review hash (my own computation):**

```
$ shasum -a 256 research/relational/cross-reviews/A-reviews-B.md
05ca64ccaa4ceae4032ca36aa22f2090c5565449d021764a9da480bbbb1a8102
```

`A-reviews-B.md` and `B-reviews-A.md` both stay byte-identical through this exchange; the record of
the response is this file, not an edit to either review.

---

## 2. O1 — the objection that changed the report (ACCEPT)

### 2.1 Reproduction, with my own invocation

I re-ran A's command myself rather than trusting A's transcript. Raw output, preserved at
`research/issue-008/results/raw/run2-modes/M31-F7-02-satisfied-but-violated__instantiate-validate.*`:

```
$ .tools/sysml -instantiate vehicle -validate=vehicle \
    research/issue-008/mutants/M31-F7-02-satisfied-but-violated.sysml
✓ package KG07Requirements
✓ Created instance of KG07Requirements::vehicle
  ID: 1
✗ satisfy vehicleMaximumMass by vehicle fails (on KG07Requirements::vehicle ID: 1)
  Required condition evaluated to false: massActual <= massRequired
✗ KG07Requirements::vehicle is not valid: 1 of 1 assertion fails
  standing: violated (witnessed: 1 run under reverse)
[exit 1]
```

Positive control, same invocation on the known-good base:

```
$ .tools/sysml -instantiate vehicle -validate=vehicle research/issue-008/known-good/KG-07-requirements.sysml
✓ satisfy vehicleMaximumMass by vehicle holds (on KG07Requirements::vehicle ID: 1)
✓ KG07Requirements::vehicle is valid: its 1 assertion holds
  standing: holds (observed: 1 run under reverse)
[exit 0]
```

**A is right, exactly as stated.** The invocation discriminates the mutant from its base, so this is
a true positive with a working control — not a spurious complaint. I also found that
`-satisfy` alone does the same job without `-instantiate` (exit 1 on the mutant, `holds` / exit 0 on
the base), so the tighter statement of my error is: *I had read `sysml -help`, quoted its
`-validate=<object>` mode in my own report §12.5 as an untested "plausible bridge", and never ran it
or `-satisfy`, which sits directly above it in the same help screen.* That is not an instrumentation
subtlety; it is a missed invocation.

### 2.2 Per-mode F7 table (built from real runs, not from reasoning)

Every row is a saved raw file under `results/raw/run2-modes/`, run 2026-11-13T14:31–14:36Z with the
pinned binary `ddfc2962…1598f0`; exact argv per row in `results/run-log-run2-modes.md`.

| mutant | default `-validate -format json` | `-satisfy` | `-instantiate <obj> -validate=<obj>` | `-self-check` | behavioural mode | verdict across modes |
|---|---|---|---|---|---|---|
| F7-01 unreachable state | clean, exit 0 | — | n/a (no object) | clean, exit 0 | `-state OperationalStates`: starts, sits in `off`, exit 0 | **silent** (defect unobservable as a verdict) |
| F7-02 satisfied-but-violated | clean, exit 0 | **violated, exit 1** | **violated, exit 1** | — | — | **DETECTED** |
| F7-03 missing flow | clean, exit 0 | — | n/a (no object) | clean, exit 0 | `-action TakePicture`: completes, `Results: picture = []`, exit 0 | **silent** (defect visible only as an empty result) |
| F7-04 contradictory assertions | clean, exit 0 | — | **undecided, exit 2** ("2 of 2 assertions undecided") | — | — | **CHECKED, NO VERDICT** |

Known-good controls, same runs: KG-07 `holds` (exit 0) under both `-satisfy` and
`-instantiate -validate=`; KG-10 `1 of 1 assertions undecided` (exit 2) — **the same outcome as its
mutant parent**, see 2.4.

### 2.3 What the corrected claim is, precisely

**Deleted claim (was §1):** "it is **no evidence at all** about whether the model's structure means
what it claims."

**Replacement (dated addendum A2 in the report, original wording retained above it):**

> A pass of the **default `-validate` invocation** is no evidence about whether a requirement encoded
> as a `require constraint` holds of the model's declared values, nor about reachability, flow
> completeness or assertion consistency. That is what the pilot measured and what its 23/32 refers to.
> The instrument's **verdict surface is wider than that invocation**: under
> `-satisfy` and `-instantiate <object> -validate=<object>` it evaluates requirement satisfaction and
> returns a five-valued standing (holds / holds vacuously / violated / undecided / no assertion), and
> under `-state` and `-action` it executes state machines and actions. On the four F7 mutants:
> **one is detected (violated), one is checked and left undecided, and two produce no verdict in any
> mode tested.** So the correct claim is *"the default path is blind to architectural meaning; the
> verdict path can decide exactly those defects that a generator encoded as a checkable constraint,
> and nothing more"* — not *"nothing can see this"*.

**Deleted claim (P3 in §2):** "At least one class of plausible model defect is invisible to the only
available instrument — Established."
**Replacement:** "**Established for two of four F7 mutants under every mode tested** (unreachable
state, missing flow); **contradicted for one** (satisfied-but-violated requirement is detected by
`-satisfy`); **undetermined for one** (contradictory assertions are checked and returned as
undecided, with the same outcome as their known-good parent)."

### 2.4 A refinement A did not claim, which cuts against over-correcting in the other direction

F7-02 is detectable **because I authored it as a checkable constraint** — the requirement carries
`require constraint { massActual <= massRequired }` and the satisfying part binds both values. A
requirement whose body is only a `doc` sentence states no assertion, and the tool says so
("holds … **vacuous**: requirement … states no required constraint"). I verified this on A's own
S2 model: `-satisfy` returns `holds (vacuous)` for `satisfy lowerBeforeArrival;`. So the verdict
path decides **only what the generator made checkable**, which in A's 18-model corpus is **0 of 18**
(no model has any `require constraint`). The corrected claim therefore has two halves, and the
second half is A's own O7: the mode detects F7-02-shaped defects where they exist, and the observed
generation corpus barely produces them.

I did **not** apply this to the other modes for the whole corpus. Only the F7 arm and the probes in
§2.2 were re-run; the 23/32 headline is still a default-path number, and addendum A2 says so in the
same sentence that reports 24/32.

---

## 3. Objection by objection

### O2 — tri-state verdict: **ACCEPT**

**(a) Ruling.** Accept. My primary measure is typed on `diagnostics[]` with an error severity; the
verdict path reports `checks[]` with a `standing`. A binary measure cannot represent the difference
between "checked and violated" and "not checked at all".

**(b) Evidence.** `results/raw/run2-modes/M31-F7-04-contradictory-assertions__instantiate-validate.stderr.txt`:

```
? assert constraint could not be evaluated (on KG10Asserts::testObject ID: 1)
  Error: constraint : assertion evaluation failed: no value for feature computedMass
? KG10Asserts::testObject is not shown valid: 2 of 2 assertions undecided
  standing: not covered (2 undecided)
[exit 2]
```

and A's S2 model under `-satisfy`:

```
✓ satisfy lowerBeforeArrival holds
  standing: holds (observed: 1 run under reverse; vacuous: requirement lowerBeforeArrival states no
  required constraint, so it holds vacuously)
```

**(c) Change.** Addendum A3 in the report adds a fifth outcome category and a measurement definition.
**The outcome space is five-valued, not three:** `holds` / `holds-vacuously` / `violated` /
`undecided (not covered)` / `no assertion to state`. A named four; the `-satisfy` run on A's own
model produces `holds-vacuously` explicitly, so I add it.

**(d) Effect.** F7-04 moves from "silent" to "checked, undecided". No aggregate percentage changes
except through the category split now reported alongside: of 4 F7 mutants, **1 violated, 1 undecided,
2 no-verdict-in-any-mode**.

**Refinement, recorded because it matters.** The undecided outcome does **not** discriminate F7-04
from its base: the base returns `1 of 1 assertions undecided` and the mutant `2 of 2` — both
undecided, differing only in the *count* of assertions. So a 2-vs-1 assertion count is the only
signal separating them, which is a shape signal, not a verdict. Calling this "detection" would be
wrong; calling it "silence" (my original) is also wrong. "Undecided" is the honest third state, and
A's objection is correct that my tables had no room for it.

### O3 — reserved-keyword notation, and the exit-code story: **ACCEPT**

**(a) Ruling.** Accept, and I verified it with a construct of my own rather than A's corpus, so the
finding is not hostage to A's coding.

**(b) Evidence.** New probe `results/probes-gate2/P1-reserved-keyword-name.sysml` (a `port return;`
in a part definition):

| invocation | exit | diagnostic |
|---|---:|---|
| `-validate -format json` | **0** | `error[reserved-keyword-name]` line 6 |
| `-validate -strict` | **2** | same diagnostic |

Reconfirmed on A's `T6-C1` (default exit 0, `-strict` exit 2) and on my own F1-03 mutant, which
exits 2 in **both** modes (`results/raw/run2-modes/`). So "notation error" splits into two
exit-code behaviours: a *parse* failure exits 2; a *notation-conformance* error can be reported as
severity `error` and still exit 0, and `-strict` is what converts it. My §3.3 discussion of "exit
status is not the criterion" covered only the *warning* case; the error-with-exit-0 case was
unrepresented.

**(c) Change.** Addendum A4: an **observed sub-class** (not a mutant — the frozen 32 are untouched)
with the probe table above, plus the statement that F1's 4/4 is a statement about *my* four
mutants (a missing semicolon, an extra brace, a keyword typo, an unquoted short name — all exit 2),
not about notation defects in general.

**(d) Effect.** F1 stays **4/4** for the authored family. As a generalisation it weakens: the
empirical dominant notation mechanism (A's corpus: 7 of 9 notation records) is a reserved keyword
used as a name, which my F1 never tested and which exits 0. A pipeline gating on exit status would
score my F1 mutants as failures and the empirical notation class as passes.

### O4 — F5 tests the satisfy defect the tool catches, not the one it misses: **ACCEPT**

**(a) Ruling.** Accept, and A's S2 record survives an independent check.

**(b) Evidence.** A's model, read-only, `research/issue-007/corpus/normalized/T2-C2.sysml`:

| invocation | result |
|---|---|
| `-validate -format json` | the only diagnostic is `error[reserved-keyword-name]` at **line 17** (`attribute state`), exit 0; **line 33 (`satisfy lowerBeforeArrival;`) produces nothing** |
| `-satisfy` | `✓ satisfy lowerBeforeArrival holds … (vacuous: requirement states no required constraint)`, exit 0 |
| `-instantiate levelCrossing -validate=levelCrossing` | `undecided`, exit 2 |

So A's S2 defect — a satisfy usage with no satisfying feature, against
`checkSatisfyRequirementUsageBindingConnector` (§8.3.21.10, class A, SHOULD) — is not merely
"silent": **the instrument positively reports the requirement as holding**, and explains that the
holding is vacuous because the requirement states no required constraint. That is a sharper finding
than either of us wrote: the vacuity explanation is about the requirement's *body*, not about the
missing binding, so a reader of that output would conclude the model is fine.

**(c) Change.** Addendum A5: F5 is restated as "3/4 **on the four mutants I authored**", with the
union figure **3/5 = 0.60** when A's S2 record is added as an explicitly cross-corpus item (its
provenance is A's coding, not my MANIFEST, and it must never be merged into my frozen denominator —
I report both and label which is which). P4 gains the satisfy example A asks for.

**(d) Effect.** F5 3/4 = 0.75 → **3/5 = 0.60** on the cross-corpus union; **3/4 = 0.75** unchanged on
my authored family, both now printed together.

### O5 — F2 detection is site-dependent: **ACCEPT**

**(a) Ruling.** Accept. My four F2 mutants all sit at type, parameter, redefinition-target and
type-declaration positions; I never tested a succession source.

**(b) Evidence.** Three probes of my own, plus A's model:

| probe | construct | exit | diagnostics |
|---|---|---:|---|
| `P2-succession-source-undefined` | `first start;` with `start` undeclared | 0 | **none** |
| (variant, `/tmp/p2b.sysml`, transcript in the run log) | `first zzz;` — an obviously undefined name | 0 | **none** |
| `P3-succession-source-declared` | same text with `action start;` declared | 0 | `warning[name-conflict]` only |
| `P5-satisfy-target-undefined` | `satisfy limit by nosuchtank;` | **2** | `error[unresolved]` |
| A `T1-C1` | `first start;` in an 80-line model | 0 | **none**, and none under `-satisfy` or `-instantiate` either |

The second row is the one that matters: **the silence is not specific to `start`** — an arbitrary
undefined `zzz` at a succession source is equally silent — so this is a resolution gap at a site,
not a name that happens to resolve. A's finding is robust and it is mine to own.

**(c) Change.** Addendum A2 (§2 above) already narrows the F7 claim; Addendum A6 narrows F2 to
"4/4 at the reference sites tested (type reference, parameter reference in a binding, redefinition
target, undeclared type); **0/1 at a succession source**, and the site is not resolved at all."

**(d) Effect.** F2 4/4 = 1.00 unchanged at the sites tested; the *class-level* sensitivity is no
longer stated as a property of "unresolved reference" — it is a property of four reference sites.

### O6 — the missing-prelude class is absent from my corpus: **ACCEPT, with a refinement**

**(a) Ruling.** Accept: I have no prelude-deletion mutant, and the confound `TOOLING.md` warns about
is therefore untested by me. The refinement is that the confound is *distinguishable*, which changes
what the missing class would have measured.

**(b) Evidence.** New probe `P4-missing-prelude.sysml` (a `part def` with `Real` and `Boolean`, no
import):

```
error[unresolved] line 4  unresolved reference: Real — did you mean ScalarValues::Real?
                          To use the bare name, import its package: private import ScalarValues::*;
error[unresolved] line 5  unresolved reference: Boolean — did you mean ScalarValues::Boolean? …
[exit 2]
```

So the tool's message names the fix, and a pipeline that reads messages can separate "forgot the
import" from "references a name it never declares"; a pipeline that counts `unresolved` cannot. That
is exactly A's point in `TOOLING.md` language, and my corpus could not have shown it.

**(c) Change.** Addendum A6 (second half): the confound is recorded as a **measured** instrument
property rather than an avoided hazard, and the probe is published.

**(d) Effect.** No number changes; a stated limitation becomes a measured observation.

### O7 — construct-surface mismatch: **ACCEPT as a scope limitation**

**(a) Ruling.** Accept. It is not an error in my mutants; it is a ceiling on what they can say, and
my report's "specification-derived by design" sentence carried an unexamined assumption that
specification surface ≈ generation surface.

**(b) Evidence.** I ran A's census myself over the 18 normalised models, and **one of A's counts
needs correcting**: A reports "unit-typed attributes with ISQ/SI libraries — 0/18"; the imports
`ISQ::`/`SI::` actually appear in **3/18** (T3-C2, T3-C3, T5-C1), but **none of the three writes a
unit literal** (`[kg]`, `[m]`, …). So the substance of A's claim survives — no model *uses* units —
but the wording "0/18 use … ISQ/SI libraries" is not right. My counts:

| construct | models containing it (of 18) |
|---|---|
| `satisfy` | **18/18** |
| `action def`/`action` | 10/18 |
| `state def`/`state` | 6/18 |
| `ISQ::`/`SI::` import | 3/18 |
| unit literal in a value | **0/18** |
| `require constraint` / `assert … constraint` / `constraint { }` | **0/18** |
| metadata annotation `@X` | **0/18** |
| `connection def` | **0/18** |
| explicit `end` feature | **0/18** |
| short name `<'…'>` | **0/18** |
| `attribute` typed by a `part def` (A's T2) | 1/18 |

**(c) Change.** Addendum A7 adds a limits paragraph and a sensitivity-interpretation sentence: my
fault model measures **defects on the specification's demonstration surface** (constraints, units,
metadata, connection definitions), while the observed generation surface is declaration +
requirement usage + connection shorthand + some behaviour. The pilot's 0.72 is a sensitivity figure
for the surface I sampled, and a reweighting by construct frequency (issue #7 at ≥200 models) would
change it in an unknown direction.

**(d) Effect.** No number changes; the interpretation of the aggregate acquires a stated domain.

### O8 — `-explain` anchoring bounds the expectation audit: **ACCEPT**

**(a) Ruling.** Accept, entirely. The detection numbers are computed from raw diagnostics and are
insulated from the expectations; the *audit* is not insulated, and A's diagnosis of the signature is
right — 24/24 "expected detectable" produced a diagnostic and both expectation errors sit in the
"expected undetectable" bucket, in the direction of the tool being stricter than I predicted. That is
what expectations written with the code list in view look like.

**(b) Evidence.** A's numbers, re-read against my own `results/analysis.md` §5: expected-detectable
n=24, signal seen 24/24; expected-undetectable n=6, errors seen in 2 (F4-01, F6-02). Both of my two
prediction errors were "the tool is stricter than the specification requires".

**(c) Change.** Addendum A8 rewrites the audit's claim to state the direction of the bias, what it
can hide (expectations that *under*-predict detection, i.e. an inflated sense of how much of the
codebook I anticipated), and that `expected_layer` uses the instrument's own layer vocabulary
(`names`, `typing`, `constraints`) rather than an independent one — so a "layer confusion" result is
partly a comparison of the tool with itself.

**(d) Effect.** No number changes. One interpretive claim is downgraded from evidence to disclosure.

### O9 — F1-04 is a spec-idiom construct: **ACCEPT**

Accept. `<'1.1'>` short names do not appear in A's corpus (0/18); a generator that never writes a
short name cannot unquote one. **Change:** addendum A4 states a per-mutant construct-frequency
assumption, and F1-04 is retained as a notation probe but excluded from any claim about "notation
defects generators make". **Effect:** none on the count; F1's interpretation narrows.

### O10 — F4-02 is not the empirical multiplicity/connection defect: **ACCEPT**

Accept. `end part hub : Hub[2];` is a declared-multiplicity violation on an explicit end feature
(warning in default mode); A's R1 is a chain through a multi-valued usage in a `connect`, with no
named constraint and no diagnostic anywhere. **Change:** addendum A4/A7 relabels F4 as *declared
multiplicity*, and states that connection-end structure (A's R1) was not sampled by my corpus at all.
**Effect:** none on F4's 3/4; the class's scope statement narrows, and R1 becomes a class I will add
from A's frozen subset if it is included there.

### O11 — MANIFEST.csv mtime post-dates the run: **ACCEPT**

Accept, and I can name the cause rather than speculate: **I caused it myself, after the run**, by
executing my own documented reproduce step (`python3 harness/author_manifest.py`) to prove the
generator is idempotent. The run was at **14:13:03Z**; the rewrite at **14:15:56Z**; the content hash
is unchanged and `mutants/expectations.sha256` verifies OK against the file. A is right on both
counts: not evidence of fitting, but an unlogged rewrite of a pre-registration artefact.
**Change:** addendum A9 logs it, and `results/run-log-run1.md` gains the line via the addendum rather
than by editing the run log. **Effect:** none.

### O12 — "every emitted error was about the injected defect" measures the design: **ACCEPT**

Accept. Single-defect mutants make relevance near-tautological, and cascades inflate the count
without inflating the number of defects. I computed the distribution A asks for from
`results/diagnostics.csv`:

| error diagnostics per mutant | mutants |
|---:|---:|
| 0 | 5 |
| 1 | 20 |
| 2 | 1 |
| 3 | 1 (F1-03 keyword typo) |
| 5 | 1 (F1-04 unquoted short name) |

30 error diagnostics over 28 signalling mutants; **24 of 28 produce exactly one**. **Change:**
addendum A8 restates the claim as *relevance, not precision*: it says each error referred to the
injected defect, not that the tool does not over-report, and the two cascade cases show that one
defect can yield five diagnostics. **Effect:** none on the headline; one sentence is weakened.

### O13 — duplicate member names are a missing class: **PARTLY ACCEPT**

**(a) Ruling.** Partly. A is right that `name-conflict` is absent from my fault model and appears at
double-digit rates in the external sample (119 of 140 diagnostics, 10 of 24 artefacts — I reproduced
both). A is cautious about not coding it, and I agree with that caution — but the reason to be
cautious is stronger than A states, and my own evidence supplies it.

**(b) Evidence.** `name-conflict` is the **only** false positive in my known-good arm: it fires at
`warning[name-conflict]: Duplicate of inherited member name 'cutoff'` on a line quoted **verbatim**
from the specification's own `TestWithCutoff` example (§7.13.4), where a same-named member in a
specializing definition is an implicit redefinition, not a duplicate. So the diagnostic does not
distinguish an **illegal duplicate** from a **legal implicit redefinition** — which means adding a
"duplicate name" class without hand-verification would import a diagnostic that is wrong in one
direction and, on my evidence, over-eager.

**(c) Change.** Addendum A7 records the class as a **candidate** with both halves of the evidence
(A's volume, my false positive) and states that its admission requires hand-coding against
§7.6.3/§7.6.5, which is exactly what A proposed.

**(d) Effect.** None on any number. It becomes a class neither of us may claim yet, and it is on the
list for the frozen empirical subset.

---

## 4. Published numbers: old → new

| # | Measure | Was | Now | Where |
|---|---|---|---|---|
| 1 | F7 error-severity detection, default path | 0/4 = 0.00 | **0/4 = 0.00 unchanged for the default path** | addendum A2 |
| 2 | F7 across all modes tested | not measured | **1/4 violated, 1/4 undecided, 2/4 no verdict in any mode** | addendum A2, §2.2 table |
| 3 | Overall relevant detection, default path | 23/32 = 0.72 [0.55, 0.84] | **unchanged**, now labelled "default path" | addendum A2 |
| 4 | Overall relevant detection, any mode tested | not measured | **24/32 = 0.75 [0.58, 0.87]** (only the F7 arm was re-run in other modes) | addendum A2 |
| 5 | F7-04 outcome | silent | **checked, undecided (no verdict)** — same standing as its base | addendum A3 |
| 6 | F1 notation class | 4/4 = 1.00 | **4/4 unchanged for the authored family**, plus an observed reserved-keyword sub-class that exits 0 | addendum A4 |
| 7 | F5 named-constraint detection | 3/4 = 0.75 | **3/4 = 0.75 (authored family)** and **3/5 = 0.60 (cross-corpus union with A's S2)** — both printed | addendum A5 |
| 8 | F2 unresolved-reference detection | 4/4 = 1.00, described as a class property | **4/4 at four reference sites; 0/1 at a succession source**; class-level claim withdrawn | addendum A6 |
| 9 | P3 "invisible to the only available instrument" | Established | **Established for 2 of 4 F7 mutants; contradicted for 1; undetermined for 1** | addendum A2 |
| 10 | Diagnostics per defect | not reported | **24 of 28 signalling mutants = exactly 1 error; cascades 3 and 5** | addendum A8 |

The two headline figures a reader should carry: **the pilot measured the default `-validate` path,
and that path's 23/32 stands; the instrument as a whole is wider, and on the four F7 mutants it
yields one verdict, one undecided and two silences.**

---

## 5. Reciprocal evidence note (for A and the adjudicator, not a re-litigation)

My probes surfaced one thing that bears on A's own coding, and it would be unfair to keep it out of
the record. The control probe `P3-succession-source-declared.sysml` — the same text as the
succession-source probe but with `action start;` declared — returns
`warning[name-conflict]: Duplicate of inherited member name 'start' from Action`. That means
**`start` is an inherited member of the library `Action` definition**, so in A's record
`T1-C1-E01` (`first start;`, coded N1 "unresolved reference") the name may well resolve — to
`Action::start` — even though the tool stays silent for the independent reason that it does not
resolve succession sources at all (`first zzz;` is equally silent).

That does not change A's detection result (silent either way) and it does not change my acceptance of
O5. It does mean the *mechanism* A records may be a kind mismatch rather than a dangling name — a
question for A's response, not for my report. I flag it because my own F2 narrowing depends on
distinguishing "the site is not resolved" from "this particular name resolves", and I cannot claim
the first without reporting the second.

---

## 6. What I rejected, and what would overturn each acceptance

**I rejected nothing.** That is not deference — each objection was checked against the binary and
each one reproduced. Where I could check a claim myself (O1, O3, O4, O5, O6, O7, O12) I did, with my
own models and my own argv, and I have published the raw output so the adjudicator can re-run it.

What would overturn each acceptance, stated so the rulings are falsifiable:

| Ruling | Would be overturned by |
|---|---|
| O1 (F7-02 detected) | the same argv on a **different** machine/binary hash giving `clean`/exit 0; or evidence that the `violated` verdict is produced by the base model too (it is not: KG-07 → `holds`) |
| O2 (tri-state) | evidence that `checks[]` is derivable from `diagnostics[]` for these models, i.e. that my binary measure could have represented "undecided" after all |
| O3 (reserved-keyword sub-class, exit 0) | a `-validate` run on `P1` that exits nonzero, or that the diagnostic is a warning rather than `error` — both contradicted by the saved raw |
| O4 (F5 3/5) | the union being inadmissible, i.e. a rule that a cross-corpus record may not be added to a mutant family's denominator. I agree it must be labelled, not merged; if the reviewers hold it inadmissible, F5 stays 3/4 and the P4 satisfy example still stands |
| O5 (F2 site-dependent) | a mode in which `first zzz;` is diagnosed. I tried `-validate` (both formats), `-satisfy`, `-instantiate -validate=`, `-self-check`: none |
| O7 (construct-surface scope) | a census showing the generation surface does produce constraints/units/metadata at a rate where my sampling is representative |
| O13 (partly) | hand-coding A's 10 external `name-conflict` artefacts and finding them all genuine duplicates, which would move the class from "candidate" to "adopted" |

---

## 7. The strongest remaining weakness in my own work

Not the one A found. A's O1 was a *reachable* error: one command, already named in my own report,
would have caught it. The weakness that remains after this response is structural and I do not think
this pilot can fix it:

**My corpus cannot tell me whether my fault model is representative, and A's corpus is too small and
too narrow to tell me either.** The construct census in §3/O7 shows the two corpora barely overlap:
`satisfy` appears in 18/18 of A's models and my F5 tests two named satisfy constraints; constraints,
units, metadata and connection definitions appear in 0/18 of A's models and carry four of my eight
classes. So the aggregate agreement A computed (0.64–0.72 across three frames) is, as A says,
coincidental — two different populations landing on a similar number. The per-class numbers are the
ones with content, and they are the ones that depend on a surface census nobody has yet: **a
construct-frequency census over ≥200 generated models is the missing instrument, not a second
validator.** That is now the top item in my "what would change the answer", and it is a better answer
than the one I wrote before Gate 2.

Second, and smaller: my measurement instrument now has a mode dimension I did not measure. The 23/32
figure is honest for the default path, but a future run must fix the invocation set in advance, the
way the frozen methodology fixed everything else — otherwise the choice of mode becomes a degree of
freedom that could be fitted to an outcome. I am stating that here before anyone asks, because it is
the same class of error A found.
