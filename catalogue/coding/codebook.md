# Coding frame — SysML v2 / KerML well-formedness constraints

**Version 1.0, frozen 2026-11-13 before any coding began.**
**Coding unit:** one *named constraint* (`validateXxx`, `checkXxx`, `deriveXxx`) as
defined in the normative machine-readable abstract syntax of SysML 2.0
(`formal/2026-03-02`, MOF XMI `ptc/25-02-15`) or KerML 1.0 (`formal/2026-03-01`,
MOF XMI `ptc/25-04-04`).

**Terminology clarification (added 2026-11-13 after review; rule, sample and
labels unchanged).** The codes A/B/U are **dependency classes**: they record what
a checker must have under this frame. "A" means *no external library or
semantic-layer dependency* — it is **not** a claim that the published OCL executes
as written. Twenty-seven class-A rows carry a high-confidence defect in their
published body (see [`../ocl-defects.csv`](../ocl-defects.csv)); executability is
reported separately in `classified.csv` as `executable_ocl_status`. The frozen
decision rule and the counts are unchanged by this wording.

## The question each coder answers

Given the constraint's published prose and OCL body, **what must a checker have
in order to decide the constraint?** Code exactly one class:

| Code | Class label | Definition |
|---|---|---|
| **A** | No external library/semantic dependency (model-local; intended decidable from the abstract syntax) | The OCL body can be evaluated against an instance graph of the metamodel plus definitions that are *inside the metamodel itself* (metaclasses, properties, derived properties, operations, enumerations, enumeration literals). No element of the normative Kernel Semantic Library or Systems Model Library is needed, and no resolution against an external namespace. |
| **B** | Requires semantics beyond the abstract syntax (library/semantic dependency) | The body names an element of the normative model libraries through a quoted `'Package::Element'` path, **or** calls a helper whose meaning is defined in terms of those libraries (`specializesFromLibrary`, `redefinesFromLibrary`, `resolveGlobal` with a library path, `libraryNamespace`, `isLibraryElement`), **or** otherwise depends on the semantic layer / implied relationships declared in the specification (Clause 8.4). |
| **U** | Undecidable as published | The published body is not a usable decision criterion: a placeholder (e.g. `TBD`), a malformed expression, or otherwise not evaluable as written. |

Class C (mentioned only in informative text or examples) and Class D (absent,
left to tool discretion) are **not** coded on this sample. They are established at
document level in the catalogue: C from names that appear in a specification PDF
but are defined in neither normative XMI; D from the specification-silence
register.

## Rules of application

1. **Kind is not the criterion.** The constraint's name prefix (`validate…`,
   `check…`, `derive…`) records the specification's own taxonomy, not the answer.
   A `check…` constraint whose body is pure model OCL is **A**. A `validate…`
   constraint that calls a library helper is **B**.
2. **Metamodel enumerations are not library elements.** A literal such as
   `VisibilityKind::protected` or `FeatureDirectionKind::_'in'` is part of the
   abstract syntax and does **not** make a constraint B.
3. **Library literals make a constraint B**, whatever the kind. A quoted
   `'Actions::Action'`, `'Base::dataValues'`, `'ScalarValues::Boolean'` is a
   reference to an element of a normative model library (a separate OMG
   artefact), not to the metamodel.
4. **Name resolution is not library dependency.** Use of `qualifiedName` or
   resolution within the submitted model (imports, namespaces) does not by
   itself make a constraint B; code A and note the resolution requirement.
5. **Implication of an external semantic layer makes a constraint B**, even when
   no quoted literal appears, if the body can only be evaluated after the
   specification's implied relationships (Clause 8.4) have been materialised or
   the semantic library consulted.
6. **When in doubt, A is the default** unless you can point to the specific
   library element or helper that makes it B. Record any doubt in `note`.
7. **Do not correct the specification.** If the body contains a name that cannot
   exist in the metamodel (a typo), code the class the *intended* expression
   would have, and record the defect in `note`. Code **U** only where no
   intended expression can be inferred (e.g. `TBD`).
8. **Independence.** Do not consult the other coder's file, the principal
   researcher's notes, or any pre-computed classification. Code from the prose,
   the OCL body and this frame only.

## Confidence

For every row record `confidence` ∈ {`high`, `medium`, `low`}:
- **high** — the body contains an unambiguous signal (a library literal/helper, or
  no external reference at all).
- **medium** — the signal requires interpretation (e.g. an unqualified name that
  may be a library element; resolution that may cross models).
- **low** — the body is defective or genuinely ambiguous.

`note` is required for every medium or low row: one sentence saying what is
uncertain.

## Worked examples (from outside the sample)

| Constraint | Class | Why |
|---|---|---|
| `validateAttributeUsageFeatures` — `feature->forAll(not isComposite)` | **A** | Only metamodel properties and standard OCL. |
| `checkAttributeUsageSpecialization` — `specializesFromLibrary('Base::dataValues')` | **B** | Helper + library element `Base::dataValues`. |
| `validateTransitionFeatureMembershipEffectAction` — `kind = TransitionFeatureKind::effect implies transitionFeature.oclIsKindOf(ActionUsage)` | **A** | `TransitionFeatureKind` is a metamodel enumeration; the rest is model structure. |
| `validateTriggerInvocationExpressionAtArgument` — `argument->at(1).result.specializesFromLibrary('Time::TimeInstantValue')` | **B** | A `validate…` constraint, but it needs the `Time` library and the `specializesFromLibrary` helper. |
| `checkTransitionUsageSourceBindingConnector` — `ownedMember->selectByKind(BindingConnector)->exists(b | ...)` | **A** | A `check…` constraint, but the body is pure model structure: binding connectors are metamodel elements, and no library element is named. |
| `checkConstructorExpressionResultDefaultValueBindingConnector` — body `TBD` | **U** | Published body is a placeholder. |

## What agreement means

Two coders classify the same 60-row stratified sample independently. Report
Cohen's κ per class (A/B/U) and the raw agreement, plus a table of every
disagreement with both coders' notes. A disagreement is not resolved by
averaging: it is reported, and the rule that produced it is revised in a later
version of this frame, not retrospectively applied to the frozen sample.
