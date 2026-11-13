# Deep trace: 15 constraints to two implementations, 18 further to one

**Version-pinned sources.** SysML 2.0 `formal/2026-03-02` (PDF sha256
`46e6c047…a84a83a`), KerML 1.0 `formal/2026-03-01` (PDF sha256
`3bcc96f9…96373697`), and the normative MOF XMI files
(`SysML.xmi` sha256 `caa65d54…11cf8c6f`, `KerML.xmi` sha256 `45b18775…7a193354`).
Implementation evidence: pilot `master` at 2026-11-13 (validator sources and
release notes), OpenSysML `develop` at 2026-11-13 (`docs/project/pilot-differential.md`),
Syside 1.0.1 vendor documentation at 2026-11-13.

**Scope.** Section 1 follows 15 constraints to evidence from at least two
independent implementations (the pilot plus OpenSysML or Syside). Sections 2–3
extend the trace to 18 further constraints where only one implementation could
be evidenced. Section 4 records four release-note claims that could not be
traced to any implementation. The issue asked for 10–20 deep traces; 15 meet
that bar with two implementations, and the wider tables are included because the
one-implementation cases are where the release-note evidence lives.

**Read this first.** The pilot has targeted **KerML 1.1 Beta 2 / SysML 2.1 Beta 2**
since its 2026-07 release. Those documents are not published. The catalogue is
pinned to 1.0/2.0. Therefore a pilot check that has no counterpart here is not
thereby "implementation-specific": it may be a constraint from the unpublished
2.1 metamodel. This trace only makes claims where the 1.0/2.0 text and the
implementation evidence can be joined by name or by quoted behaviour.

**Status vocabulary.** *Not enforced* — the implementation declares the
constraint and enforces nothing (empty body or TODO). *Partial* — an
approximation is enforced (e.g. at warning severity). *Enforced* — a check is
present. *Deliberate non-check* — the implementation states it believes the
constraint is satisfied by construction or is not worth checking. *Contested* —
implementations or sources disagree and the evidence does not adjudicate.

---

## 1. Constraints with evidence from two independent implementations

### 1.1 The control-node succession family (8 constraints)

All eight are SysML 2.0 `validate…` constraints on metaclasses in §8.3.17.
Each is **class A** in the catalogue (OCL over metamodel properties, no library
element) and carries the specification's **SHOULD report** obligation
(§8.3.1). The pilot's own source leaves each as a `// TODO: Check validate… (?)`
comment in an otherwise empty `@Check` method; OpenSysML's differential
independently adjudicates each as a "pilot gap" and reports that its own checker
enforces all nine control-node constraints.

| Constraint (clause) | OCL (gist) | Pilot, `master` 2026-11-13 | OpenSysML differential | Status |
|---|---|---|---|---|
| `validateControlNodeIncomingSuccessions` (8.3.17.6) | incoming Successions have target multiplicity 1..1 | TODO in `checkControlNode`, `SysMLValidator.xtend:871`; only `validateControlNodeOwningType` checked | "pilot gap — `checkControlNode` checks the owning type only" | **Not enforced** |
| `validateControlNodeOutgoingSuccessions` (8.3.17.6) | outgoing Successions have source multiplicity 1..1 | same TODO | "pilot gap — as above" | **Not enforced** |
| `validateDecisionNodeIncomingSuccessions` (8.3.17.7) | at most one incoming Succession | `checkDecisionNode`, `:883`, two TODOs, no executable body | "pilot gap — `checkDecisionNode` is empty" | **Not enforced** |
| `validateDecisionNodeOutgoingSuccessions` (8.3.17.7) | outgoing target multiplicity 0..1 | same empty method | "pilot gap — `checkDecisionNode` is empty" | **Not enforced** |
| `validateForkNodeIncomingSuccessions` (8.3.17.8) | at most one incoming Succession | `checkForkNode`, `:889`, TODO only | "pilot gap — `checkForkNode` is empty" | **Not enforced** |
| `validateJoinNodeOutgoingSuccessions` (8.3.17.11) | at most one outgoing Succession | `checkJoinNode`, `:894`, TODO only | "pilot gap — `checkJoinNode` is empty" | **Not enforced** |
| `validateMergeNodeIncomingSuccessions` (8.3.17.13) | incoming source multiplicity 0..1 | `checkMergeNode`, `:899`, two TODOs | "pilot gap — `checkMergeNode` is empty" | **Not enforced** |
| `validateMergeNodeOutgoingSuccessions` (8.3.17.13) | at most one outgoing Succession | the TODO is misspelled `validateMergeNodeOutgoingSucessions`; no diagnostic constant at all | "pilot gap — `checkMergeNode` is empty" | **Not enforced** |

**What this establishes.** These are not ambiguous or library-dependent rules:
the specification gives a short OCL predicate over abstract-syntax properties,
states that a conformant tool *should report* violations, and two independent
implementations agree the pilot does not. This is the cleanest evidence in the
study that the specified–enforced gap is real and countable, not a matter of
interpretation.

**A caveat that cuts the other way.** OpenSysML's own adjudication records a
readability problem: a literal evaluation of the four multiplicity constraints
would reject `first a then f;`, because an unwritten connector end has no
multiplicity and `multiplicityHasBounds` requires a non-null multiplicity.
OpenSysML adopts the "specification's intent" reading. So even this family
requires an interpretation the OCL alone does not supply — evidence for the
label `A` being about decidability, not about being trouble-free.

### 1.2 `validateFeatureValueOverriding` (KerML 8.3.4.10.2) — class A, SHOULD report

OCL: `featureWithValue.redefinition.redefinedFeature->closure(redefinition.redefinedFeature).valuation->forAll(isDefault)`.

- **Syside (vendor).** Worked diamond example: `A` owns `attribute a`; `B0 :> A`
  redefines it; `B1 :> A` redefines it with `= 42`; `C :> B0, B1` redefines it
  with `= 7`. "Pilot Implementation does not detect any issues, but the example
  above is semantically inconsistent… upholding `validateFeatureValueOverriding`,
  the expected values should be `b0 == b1 == 42` and a semantic error of
  overriding feature value in `C::a`." Syside reports the pilot resolves
  `b0 == 7`, `b1 == 42`.
- **OpenSysML (third party).** Implements the constraint as a constraint-tier
  rule (`passes/feature_value_overriding.go`) and reports corpus movement:
  overall agreeing cases 334 → 337 after adding it. It does **not** adjudicate
  the diamond example, so it corroborates that the rule is implementable, not
  that the pilot is wrong.
- **Pilot source.** `checkFeatureValue` exists (`KerMLValidator.xtend:1318`), so
  the relevant check is present; the disagreement is about the closure over
  redefinitions, not about absence.

**Status: contested.** A vendor with a commercial interest asserts a specific
false negative; an independent open-source implementation treats the rule as
real; neither the pilot nor the specification supplies the diamond case as a
test. The catalogue records the constraint as class A and the *behaviour* as not
established.

### 1.3 `validateAttributeUsageFeatures` and `validateAttributeDefinitionFeatures` (SysML 8.3.7.2–3) — class A, SHOULD report

OCL: `feature->forAll(not isComposite)`, on `AttributeUsage` and `AttributeDefinition`.

- **Pilot.** `checkAttributeDefinition` calls `checkAllNotComposite`
  (`SysMLValidator.xtend:557`); `checkAttributeUsage` calls the same helper
  (`:565`, though its in-code note also carries a TODO for a different
  constraint). Both checks exist.
- **Syside (vendor).** "There were a few places in the standard library and
  accompanying examples where Attributes contained owned non-referential
  ItemUsages." Syside's own standard-library diff fixes them. That is a report
  that the **normative artefact set is internally inconsistent**: the model
  library, which is normative, violates a normative constraint.
- **Status: enforced; the library is non-conforming.**

**What this establishes.** Enforcement of a class-A rule does not imply that the
normative corpus satisfies it. A catalogue entry can be checkable, implemented,
and still fail on the specification's own library.

### 1.4 `checkFeatureValueBindingConnector` (KerML 8.3.4.10.2) — class B, MAY ignore

OCL: `not isDefault implies featureWithValue.ownedMember->selectByKind(BindingConnector)->exists(...)`.

- **Pilot.** Not named anywhere in either validator. `checkFeatureValue` exists
  but the binding-connector condition is not among its diagnostic payloads.
- **Syside (vendor).** "Some implicit model elements are not constructed, e.g.
  implicit binding connectors. This is done for performance reasons… According
  to the specification, implicit binding connectors are constructed between
  every feature with value and value… As a result, strict type checking is not
  working for all cases yet."
- **Specification.** §8.3.1 says a tool "may satisfy the constraints by
  introducing implied relationships into the model, it may simply report their
  violation, or it may ignore the violations."

**Status: not enforced and not reportable without materialising implied elements.**
This is the archetype of class B: the predicate is expressible, but its truth
depends on an implementation choice the specification explicitly leaves open.
A validator that does not construct implicit binding connectors will report
either nothing or a false violation; both are licensed.

### 1.5 `checkMetadataFeatureSemanticSpecialization` (KerML 8.3.4.12.3) — class B, MAY ignore

- **Pilot.** Not named in either validator.
- **Syside (vendor).** Of the standard library's `CauseAndEffect` package using
  `operator as` to compute `baseType`: "Syside diagnoses this during semantic
  resolution phase, while Pilot implementation silently ignores this unintended
  behavior. The result of this is that `CauseMetadata` and `EffectMetadata` can
  be applied to any element type without triggering diagnostics."
- **Status: not enforced.** The condition depends on the semantic metatype and
  library resolution; the pilot neither materialises the check nor reports.

### 1.6 `validateInvocationExpressionParameterRedefinition` (KerML 8.3.4.8.8) — class A, SHOULD report

- **Pilot.** `checkInvocationExpression` (`KerMLValidator.xtend:1198`) calls
  `checkInstantiationExpressionFeatures`; a check exists.
- **Syside (vendor).** On `CollectionFunctions::'array#'::index`, whose second
  and third parameters lack an `in` direction: "Pilot Implementation diagnoses
  nothing. `validateInvocationExpressionParameterRedefinition` requires that all
  InvocationExpression parameters redefine exactly one feature of the invoked
  type, but implicit Expression owned feature redefinitions only work on
  parameters, that is - directed features."
- **Status: partial / contested.** The check exists but a specific case is
  missed; the vendor's explanation is a mechanism (undirected features excluded
  from implicit redefinition), not a mere assertion.

### 1.7 `validateRedefinitionDirectionConformance` (KerML 8.3.3.3.8) — class A, SHOULD report

- **Pilot.** `checkFeature` and `checkRedefinition` both call
  `checkRedefinitionDirection` (`KerMLValidator.xtend:592`, `:705`).
- **Syside (vendor).** Syside gives item-flow source/target features implicit
  `out`/`in` directions and therefore diagnoses incompatible flow directions
  through this constraint. It then records a **specification conflict**: KerML
  §7.4.10.3 "seems to heavily imply" the directions, while KerML §8.2.5.9.2
  Note 1 "seems to contradict this by specifying that directions should instead
  be set to the directions of the redefined features… which would make
  `validateRedefinitionDirectionConformance` pass unconditionally. A
  clarification on this is needed."
- **Status: contested at the specification level.** Two readings of the
  normative text produce opposite verdicts on the same model. This is recorded
  as ambiguity, not as a tool defect.

---

## 2. Constraints traced to one implementation, with first-party release-note evidence

These are the constraints the pilot's 2026-01 release says were "previously **not
being checked**". The release note and the source agree; no second implementation
was found that reports on the same names, so the trace stops at one implementation
plus the normative OCL.

| Constraint (clause) | Class | Pilot evidence | Status |
|---|---|---|---|
| `validateEndFeatureMembershipIsEnd` (KerML 8.3.3.3.3) | A | 2026-01: `isEnd` "will no longer be automatically `true`, but must be explicitly set to `true` to meet the `validateEndFeatureMembershipIsEnd` constraint"; check now present | **Enforced since 2026-01**; previously satisfied by a getter default, not a check |
| `validateParameterMembershipParameterDirection` (KerML 8.3.4.6.4) | A | 2026-01 lists "`validateParameterMembership`" among constraints "previously not being checked"; the metamodel names the two conditions `…OwningType` and `…ParameterDirection` | **Enforced since 2026-01**; the release note's name is not an exact metamodel identifier |
| `validateCollectExpressionOperator` (KerML 8.3.4.8.2) | A | 2026-01 lists it; `checkCollectExpression` at `KerMLValidator.xtend:1120` | **Enforced since 2026-01** |
| `validateFeatureChainExpressionOperator` (KerML 8.3.4.8.4) | A | 2026-01 lists it; `checkFeatureChainExpression` at `:1128` | **Enforced since 2026-01** |
| `validateIndexExpressionOperator` (KerML 8.3.4.8.6) | A | 2026-01 lists it; `checkIndexExpression` at `:1275` | **Enforced since 2026-01** |
| `validateSelectExpressionOperator` (KerML 8.3.4.8.18) | A | 2026-01 lists it; `checkSelectExpression` at `:1267` | **Enforced since 2026-01** |
| `validateFlowEndIsEnd` (KerML 8.3.4.9.3) | A | 2026-01 lists it; `checkFlowEnd` at `:1290` | **Enforced since 2026-01** (the release note also carries a TODO for it) |
| `validateUsageIsReferential` (SysML 8.3.6.4) | A | 2026-01 lists it; `checkUsage` at `SysMLValidator.xtend:503` | **Enforced since 2026-01** |
| `validateAttributeUsageIsReference` (SysML 8.3.7.3) | A | 2026-01 lists it; `checkAttributeUsage` at `:565`. The same note states a caller "can use the `setIsComposite` method to set this to `true`, even though this would violate the constraint" | **Enforced since 2026-01**, but the API can construct a violating model; validation is not a construction invariant |
| `validateEnumerationDefinitionIsVariation` (SysML 8.3.8.2) | A | 2026-01 lists it; `checkEnumerationDefinition` at `:588` | **Enforced since 2026-01** |
| `validateEventOccurrenceUsageIsReference` (SysML 8.3.9.2) | A | 2026-01 lists it; `checkEventOccurrenceUsage` at `:602` | **Enforced since 2026-01** |
| `validatePortUsageIsReference` (SysML 8.3.12.6) | A | 2026-01 lists it; `checkPortUsage` at `:694` | **Enforced since 2026-01** |

**Name drift in the release note.** The 2026-01 note calls two KerML constraints
`validateEndFeatureMembership` and `validateParameterMembership`; the metamodel
defines `validateEndFeatureMembershipIsEnd` and
`validateParameterMembershipOwningType` / `…ParameterDirection`. A name-based
audit of the release note against the catalogue therefore under-counts by at
least two. This is a small but concrete reason why "constraint identity" needs
a register, not a grep.

## 3. Constraints with a first-party admission but no second-implementation check

| Constraint (clause) | Class | First-party evidence | Status |
|---|---|---|---|
| `checkConnectorTypeFeaturing` (KerML 8.3.4.5.3) | A | 2026-03: "The Pilot Implementation was not reporting this as an error, **which was not conformant with the normative metamodel for KerML**… Removed code that suppressed violations". `KerMLValidator.xtend:1023` still carries `// TODO: Be able to remove these special cases` in the related branch | **Enforced since 2026-03**, with a remaining special case |
| `validateAssociationStructureIntersection` (KerML 8.3.4.4.2) | A | Source: `// validateAssociationStructureIntersection is automatically satisfied` (`KerMLValidator.xtend:919`) | **Deliberate non-check**; no second implementation reports on it |
| `validateMultiplicityRangeBounds` (KerML 8.3.4.11.2) | A | Source: `// TODO: Correct validateMultiplicityBoundResults OCL from KERML-199.` (`:1337`); Syside: "Multiplicity bounds are parsed as arbitrary Expressions and are not bound by LL parser limitations. Pilot Implementation has this marked with TODO." | **Partial**; the pilot asserts the published OCL is wrong and names an OMG issue |
| `validateFeatureEndIsConstant` (KerML 8.3.3.3.4) | A | Diagnostic constant declared, never referenced by executable code (inventory `KerML`); SysML prose calls it `checkFeatureEndIsConstaint` (sic) and also `checkFeatureEndIsConstant` | **Not enforced**; name and kind prefix inconsistent between the metamodel and the prose |
| `validateRedefinitionMultiplicityConformance`, `validateSubsettingMultiplicityConformance` | no counterpart in 2.0/1.0 | TODO above code that emits `warning(...)` under those codes (`KerMLValidator.xtend:795`, `:806`) | **Partial, warning severity**; may be a 2.1 Beta 2 constraint, not established |

## 4. Release-note claims with no matching implementation at 2026-11-13 — contested

The 2026-07 release notes name four `check…` constraints as resolved issues.
None of the four names, nor their distinctive fragments, occurs in either
validator source on `master` at 2026-11-13:

- `checkConstraintUsageCheckedConstraintSpecialization` (`SYSML21-4`)
- `checkIncludeUseCaseSpecialization` (`SYSML21-299`)
- `checkRequirementUsageObjectiveRedefinition` (`SYSML21-309`)
- `checkRequirementUsageSubrequirementSpecialization` (`SYSML21-300`; described as revised)

The catalogue defines the first three as class B SysML constraints (the first
two use `specializesFromLibrary`; the third is model-only, class A). Either the
pilot implemented them under different identifiers, or the release note refers
to resolution of the OMG issue rather than to a shipped check. **Not
established**; this is exactly the kind of claim a name-based conformance audit
would wrongly accept.

---

## 5. What the trace establishes, and what it does not

**Established.**
1. At least eight class-A, SHOULD-report constraints are unimplemented in the
   pilot, confirmed by the pilot's own source and an independent implementation.
2. The 2026-01 release added checks for 12–13 named constraints that had been
   satisfied by getter defaults rather than checks; the source corroborates.
3. At least five constraints are *deliberately* not checked, or checked only
   partially or at warning severity, with the implementation's own comment as
   evidence.
4. A constraint can be enforced and still fail on the normative model library
   (Syside's report on `validateAttributeUsageFeatures`).
5. The published OCL is not always executable as written: placeholders, typos
   and malformed library paths exist in the normative metamodel (48 defect rows
   in `ocl-defects.csv`), and one implementation names an OMG issue
   (KERML-199) against a constraint's OCL.
6. At least one constraint's verdict depends on a contested reading of two
   normative KerML clauses (`validateRedefinitionDirectionConformance`).

**Not established.**
- Whether the pilot's targeted 2.1 Beta 2 metamodel contains the 44 pilot
  identifiers that have no 1.0/2.0 counterpart. The 2.1 documents are not
  published.
- Whether the release-note-only constraints are implemented under other names.
- Any behavioural claim about the *released* 2026-09.1 validator: all source
  claims are about `master` at 2026-11-13, and no JAR was built or decompiled.
- Whether the Syside diamond example reproduces; it is a vendor worked example,
  not an executed test in this study.
