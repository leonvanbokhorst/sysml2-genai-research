# KG-07-requirements — provenance and validity argument

**Independence type:** S (specification example), adapted; deviations listed.
**Source:** SysML 2.0 Part 1, `formal/2026-03-02`, §7.21.2, p.133.

**Quoted verbatim** (structure, documentation text, `assume`/`require` form, `subject`,
`attribute :>>` redefinitions, short names `<'1.1'>`, `<'v1.1'>`).

**Deviations introduced by the author, and why.**
| Deviation | Reason |
|---|---|
| `MassValue` → `Real` for `massActual`, `massRequired`; `0[kg]` → `0.0` and `<=` on unitless reals | Keeps this base independent of the ISQ/SI libraries so that F6 (quantity/unit) mutants are not derived from, and confounded by, a base that already exercises units. |
| `subject v : Vehicle` added to the usage; `part vehicle : Vehicle` added | The clause's usage names `Vehicle` and requires a subject; without both, the `satisfy … by …` link of §7.21.2/§8.3.21.10 has no referent. |
| `satisfy vehicleMaximumMass by vehicle;` added at package level | Needed as the base for mutant F5-02 (`validateSatisfyRequirementUsageReference`) and F7-02 (satisfied-but-violated requirement). The form is the specification's `satisfy` shorthand (§8.3.21.10, §7.21.1). |

**Why it is believed valid.**
1. §7.21.2: "A requirement usage must be defined by a single requirement definition."
   `vehicleMaximumMass : MaximumMass` — one definition. Satisfied.
2. §8.3.21.8 `validateRequirementDefinitionOnlyOneSubject`: "at most one featureMembership that is a
   SubjectMembership". The definition has none; the usage has exactly one. `validateRequirementUsageOnlyOneSubject`
   satisfied. `validateRequirement{Definition,Usage}SubjectParameterPosition`: "the subjectParameter
   must be its first input" — it is the only parameter and is declared first. Satisfied.
3. §7.21.2: a requirement constraint is the implication "if all assumption constraints are true,
   all required constraints must be true". `assume constraint { massRequired > 0.0 }` and
   `require constraint { massActual <= massRequired }` are that form. Satisfied structurally — note
   that *well-formedness does not require the implication to hold for any particular values*, which
   is exactly the oracle gap that F7-02 exercises.
4. §8.3.21.10 `validateSatisfyRequirementUsageReference`: "the featureTarget of its
   referencedFeature must be a RequirementUsage". `vehicleMaximumMass` is a RequirementUsage.
   Satisfied. §8.3.21.10 `checkSatisfyRequirementUsageBindingConnector` (MAY) concerns the implied
   BindingConnector between `subjectParameter` and the satisfying feature; per
   `evidence/spec-tooling.md` §3.3(f) an implementation may not construct it, and the constraint's
   obligation is MAY, so its absence is not a well-formedness defect of the model.
5. `attribute :>> massActual = 1500.0;` — a redefinition with a feature value. KerML
   `validateFeatureValueOverriding` (§8.3.4.10.2) forbids this only if the redefined feature already
   has a **non-default** FeatureValue. The definition's `massActual` has none — it is declared with
   no value. Satisfied; this is exactly the difference F5-01 exploits.
6. The numeric bound `1500.0 <= 2000.0` makes the requirement *true* for the modelled vehicle, so
   the `satisfy` claim is also semantically honest here (unlike F7-02).

**Author's uncertainty.** Whether `satisfy x by y;` at package level is admitted without an owning
occurrence is not stated in the clause I read; it validates in this instrument and the notation is
in §7.21.1's representative-notation table as I read it.
