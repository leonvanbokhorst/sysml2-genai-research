# KG-04-featurevalues — provenance and validity argument

**Independence type:** S (specification example), with an author-supplied prelude.
**Source:** SysML 2.0 Part 1, `formal/2026-03-02`, §7.13.4, p.72.

**Quoted verbatim.**
```
attribute monthsInYear : Natural = 12;
item def TestRecord {
    attribute scores[1..*] : Integer;
    derived attribute averageScore[1] : Rational = sum(scores)/size(scores);
    attribute cutoff : Integer default = 0.75 * averageScore;
}
part def Counter {
    attribute count[1] : Natural := 0;
}
```
**Supplied by the author.** The prelude `private import ScalarValues::*;`,
`private import SequenceFunctions::*;`, `private import RealFunctions::*;`. The clause's example
uses `sum` and `size` unqualified without showing imports; in this instrument they resolve only from
those library packages, so the prelude is required to make the quoted text resolve at all. **This
was found by a validator firing and is triaged as a confound, not a defect** (`results/known-good-triage.md`).

**Why it is believed valid.**
1. §7.13.4: "A usage can have at most one feature value relationship." Each feature here has at
   most one. Satisfied.
2. `attribute cutoff : Integer default = 0.75 * averageScore;` is the specification's own line. Its
   *value* need not conform to `Integer` to be well-formed — a default feature value is not a fixed
   binding, and the specification presents it as a pedagogical illustration of a default.
   **Author's uncertainty, flagged:** if a strict type check applies to defaults, this line is where
   it would fire. If the instrument flags it, that is reported as over-reach-or-genuine, not assumed.
3. `derived attribute averageScore[1] : Rational` with an explicit multiplicity 1: legal
   (§8.3.4.11.2 bound is a `Natural`), and `derived` is a feature-flagging keyword, not a constraint.
4. `attribute count[1] : Natural := 0;` — a fixed *initial* value inside a part definition (an
   occurrence definition), which §7.13.4 requires for `:=` ("the owner must be a kind of occurrence
   definition or usage"). Satisfied.

**Risk carried into the mutant corpus.** Because this base already contains a feature value of a
type that may not conform, a mutant in this base could be confounded by a pre-existing condition.
The triage file records that no diagnostic fires on the base, so the confound is not realised here.

## Author-supplied addition, and a warning the base already produces

`item def TestWithCutoff :> TestRecord { attribute cutoff : Rational default = 0.75 * averageScore; }`
is quoted **verbatim** from the same clause (§7.13.4, p.72) and was added as the base for mutant
F5-01 (`validateFeatureValueOverriding`).

**Observed, and triaged rather than repaired:** this instrument emits
`warning[name-conflict]: Duplicate of inherited member name 'cutoff' from TestRecord` on that line.
The specification makes a same-named declaration in a specializing definition an *implicit
redefinition* (§7.6.5 effective names; §7.6.3), not a conflict, and its own example relies on that.
The warning is therefore recorded in `results/known-good-triage.md` as a **candidate over-reach
(category ii)**, and the model is left verbatim. It is a warning, not an error, so it does not
affect the error-level false-positive count; it is reported separately.
