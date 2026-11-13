# KG-10-asserts — provenance and validity argument

**Independence type:** S (specification example), adapted.
**Source:** SysML 2.0 Part 1, `formal/2026-03-02`, §7.20.3, p.128.

**Quoted verbatim.** The `assert constraint`, `assert not constraint`, named-constraint `assert`
forms, the `negativeMass` constraint definition, and the `:>>` redefinitions in the assertion body.
**Deviations.** `MassValue` → `Real` (keeps this base independent of ISQ/SI, same reason as KG-07);
`0.0` instead of `0[kg]`. The `part alienObject` example is retained in full.

**Why it is believed valid.**
1. §7.20.3: an `assert constraint` usage asserts the constraint evaluates true at all times;
   `assert negativeMass { :>> mass = antiMass; }` relates the assertion to the named constraint via
   reference subsetting and redefines its parameter. The specification gives this exact form.
2. §8.3.20.2 `checkAssertConstraintUsageSpecialization` (MAY): a non-negated assert must specialize
   `Constraints::constraintChecks`; derivable and satisfied by the library's own implicit
   specialization for a conformant implementation. Its obligation is MAY, so an implementation that
   does not construct it is not reporting a model defect.
3. `constraint negativeMass { attribute mass : Real; mass < 0.0 }` — a constraint definition whose
   body ends in a Boolean expression (§7.20.2). One result expression. Satisfied.
4. `assert constraint { computedMass >= 0.0 }` in `testObject`: the constraint expression references
   a feature of the owning part, which is in scope. Satisfied.
5. The two assertions in `alienObject` and the negated-form comment are not contradictory in the
   model: only the named-constraint form is instantiated.

**Note carried into the mutant corpus.** This base is the intended home of an F7 "contradictory
guards/assertions" mutant: the specification requires only that the assertion be *declared*, not
that it be *satisfiable* for any value, which is again the oracle gap.
