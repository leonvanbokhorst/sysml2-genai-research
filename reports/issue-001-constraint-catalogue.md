# Which SysML v2 well-formedness constraints are actually normative, and which are left to tool discretion?

**Issue:** [#1](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/1)
**Report status:** primary report; catalogue and registers in [`catalogue/`](../catalogue/)
**Pinned specification versions:** SysML 2.0 `formal/2026-03-02`; KerML 1.0 `formal/2026-03-01`; normative MOF XMI `ptc/25-02-15` and `ptc/25-04-04`
**Retrieval date:** 2026-11-13
**Lens:** none supplied; the issue's four-way classification is the frame.

---

## Summary answer

The question has an answer, and it is countable. The pinned 1.0/2.0 normative
metamodels contain **623 named well-formedness constraints** — SysML 365, KerML
258 — and the specification itself grades them into three obligations before any
tool sees them:

- **235 `derive…` derivation constraints** — "shall always enforce";
- **208 `check…` semantic constraints** — a tool "may satisfy the constraints by
  introducing implied relationships into the model, it may simply report their
  violation, or it **may ignore** the violations";
- **180 `validate…` validation constraints** — "should report violations".

By what a checker actually needs under the frozen **dependency-class** rule,
**437 have no external library or semantic dependency** (class A — model-local;
intended decidable from the abstract syntax), **184 need the normative
Kernel/Semantic Library or the semantic layer** (class B), and **2 are
placeholders** whose published body is the literal string `TBD` (class U). This
is a classification of dependency, **not** a claim that the published OCL
executes as written: 27 class-A rows and 14 class-B rows carry a high-confidence
defect in their published body (§3.3). The 437 class-A constraints are not all
obligations: 35 of them are `check…` constraints whose reporting is discretionary.

Three further findings change what "well-formed" can mean:

1. **The published OCL is not always executable as written.** 48 named
   constraints contain at least one published-body defect; 43 are high
   confidence and 5 medium: 2 bodies are `TBD`, 34 have misspelled metamodel
   identifiers, 7 have malformed or misspelled library paths, and 5 more are
   suspected. Nine constraints are additionally
   mislabelled `language="English"` on an OCL body. A tool that implements the
   text literally will fail on some of the normatively specified rules.
2. **The prose names constraints the metamodel does not define.** 39
   constraint-name occurrences in the two PDFs (38 distinct names) have no
   definition in either XMI. Thirty-one of them state conditions in **normative
   Clause 8.4 (Semantics)** with no formal counterpart: 12 are plausible
   renamings, 11 have no counterpart at all, 6 are typos, and 2 are subsumed by a
   generic constraint. This is not "informative text"; it is normative prose
   asserting conditions with no formal definition.
3. **The engineering-interesting properties are largely outside the constraint
   surface.** Ten areas are registered: four are genuinely absent (default
   multiplicities — OMG issue SYSML21-185, open since 2024-06 — general type
   conformance and inference, dimensional consistency of units and quantities,
   and diagnostic severity/identity); two are explicit discretion or delegation
   (implied-relationship materialisation; method-level constraints); one is an
   unresolved ambiguity (membership selection); one lies outside the
   well-formedness surface (execution behaviour); and two are oracle/provenance
   gaps (no conformance suite; frozen metamodel URI). The register distinguishes
   these kinds rather than calling all ten "silence":
   [`silence-register.md`](../catalogue/silence-register.md).

On the implementation side, the reference pilot's validator names **200 distinct
identifiers**, of which **156 match a catalogue constraint name exactly**:
**identifier coverage only**, not implementation, enforcement or conformance
coverage. Of those 156, **149** occur in non-TODO `@Check` methods and **7** only
in TODO-only methods; none was runtime-tested. Eight model-local, SHOULD-report
control-node constraints are `// TODO` comments in empty `@Check` methods; an
independent implementation (OpenSysML) also adjudicates each as a "pilot gap" at
the source level; and the pilot's 2026-01 release admits that 13 named
constraints "were previously **not being checked**". These are hypotheses for a
runtime false-negative study (issue #8), not measured false negatives. The pilot
that most third parties benchmark against is therefore not a conformance oracle
for the pinned 1.0/2.0 documents, and it cannot be one: since 2026-07 it targets
an unpublished **2.1 Beta 2** revision.

**The direct answer.** "Correct with respect to what?" has four different answers,
and they are not nested:

| Sense of "correct" | Size | Who decides |
|---|---|---|
| Satisfies the 180 validation constraints | 169 dependency class A + 11 class B | specification, SHOULD report |
| Satisfies the 208 semantic constraints | 35 dependency class A + 171 class B + 2 U | tool may imply, report or ignore |
| Derives the 235 derived properties | 233 dependency class A + 2 class B | specification, SHALL, but not "well-formedness" |
| Type-correct, dimensionally consistent, method-adequate, behaviourally executable | **0 specified** | nobody |

A validator pass is evidence for the first sense and, at best, weak evidence for
the second. It is not evidence for the fourth, which is where systems engineers
locate most of the correctness they care about.

---

## 1. Question, scope and exclusions

**Question (from the issue).** Which well-formedness rules does SysML v2 — and the
KerML it is built on — actually impose on a model, and how are they specified?
Separate rules stated normatively and checkable mechanically, from rules stated
normatively but not mechanically checkable, from rules not specified at all,
leaving each implementation to invent its own answer.

**Authorised scope, as executed.**

- Systematic extraction of constraints from the pinned SysML 2.0 and KerML 1.0
  normative artefacts: clause, constraint name, kind, context metaclass, OCL
  body, and what a checker needs to decide it.
- A four-way classification aligned to the issue's classes.
- A deep-traced subset: 15 constraints followed to two independent implementations, 18 more to one implementation plus the normative text, and four contested release-note claims.
- An explicit silence-and-discretion register with kind labels and the
  corresponding implementation choices.

**Explicitly out of scope (from the issue).** A validator implementation; full
spec coverage as if exhaustive; a conformance verdict on any tool; adjudication
of ambiguous OMG text on OMG's behalf.

**What "version-pinned" means here.** Every row is traceable to one of four
artefacts by name and file hash (see [`catalogue/README.md`](../catalogue/README.md)).
The catalogue does **not** claim to cover SysML 2.1 Beta 2 / KerML 1.1 Beta 2,
which the pilot targets and which has no published normative document.

---

## 2. Status of propositions

**Established on retrieved evidence.**

- The pinned metamodels contain 623 named constraints: 365 SysML (145 derive,
  128 check, 92 validate) and 258 KerML (90 derive, 80 check, 88 validate). All
  623 appear as definition-style headings in the corresponding PDF at the clause
  recorded in each row; all 623 have an `uml:OpaqueExpression` body.
- The specification's §8.3.1 taxonomy and its modal verbs are as quoted
  (SHALL/SHOULD/MAY). This is the specification's own classification, retrieved
  from both documents.
- 437 constraints are **dependency class A** (model-local: no external library or
  semantic-layer dependency under the frozen rule), 184 are class B, and 2 are
  placeholders, under the decision procedure in
  [`coding/codebook.md`](../catalogue/coding/codebook.md). Dependency class does
  not imply executability: 27 class-A and 14 class-B rows carry a
  high-confidence defect in their published OCL.
- 48 named constraints have at least one defect in their published OCL; 43 of
  the 48 are high confidence, 5 medium. Examples: two
  KerML `check…` bodies are `TBD`; `validateAssertConstraintUsageReference`
  calls `referencedFeaureTarget()` (sic); `checkFeatureChainExpressionTargetRedefinition`
  contains the malformed path `'ControlFunctions::\'.\'::source::target'`.
- 38 distinct constraint names are used in the PDFs and defined in neither XMI;
  31 are normative conditions asserted in Clause 8.4 (34 Clause-8.4 names minus
  1 non-constraint name and 2 worked examples).
- Ten areas are recorded in the silence-and-discretion register, each with its
  specification text and implementation evidence: four genuine absences (D1–D4),
  two explicit discretion/delegation cases (D5, D8), one unresolved ambiguity
  (D6), one area outside the well-formedness surface (D7), and two
  oracle/provenance gaps (D9–D10). Only the first four are class D in the strict
  sense.
- The pilot's validator contains 114 active `@Check` methods (72 SysML, 42
  KerML), mapping to 200 distinct identifiers. Zero `derive…` identifiers and two
  `check…` identifiers are named. **156/623 is identifier coverage only**: 149
  occur in non-TODO methods and 7 only in TODO-only methods; no check was run.
  Eight control-node `validate…` constraints are TODO-only, and OpenSysML
  independently reports the same source-level gap. The false-negative rate is
  not measured.
- OMG issue SYSML21-185 is publicly readable and states the specification has no
  formal default-multiplicity rule in Clause 8; status open, reported 2024-06-15.
- The 2026-01 pilot release states 13 named constraints "were previously not
  being checked"; the 2026-03 release admits that a suppression "was not
  conformant with the normative metamodel".
- Two coders classified a 60-row stratified sample with 60/60 raw agreement
  (Cohen's κ = 1.000).

**Contested.**

- Whether the Syside diamond example is a genuine pilot false negative for
  `validateFeatureValueOverriding`. It is a vendor worked example; OpenSysML
  implements the rule but does not adjudicate that case; the pilot has a check.
- Whether the four `check…` constraints named in the 2026-07 release notes
  (`checkConstraintUsageCheckedConstraintSpecialization`,
  `checkIncludeUseCaseSpecialization`,
  `checkRequirementUsageObjectiveRedefinition`,
  `checkRequirementUsageSubrequirementSpecialization`) are implemented under
  other identifiers. None occurs in the validator source at 2026-11-13.
- Whether the 44 pilot identifiers with no 1.0/2.0 counterpart are
  implementation-specific checks or constraints from the unpublished 2.1 Beta 2
  metamodel. The pilot's target revision cannot be retrieved.
- For each prose-only name, whether it is a rename, a deletion, or a condition
  the metamodel never captured. The nearest-name mapping in
  [`prose-only-names.csv`](../catalogue/prose-only-names.csv) is explicitly
  marked as a plausible counterpart, not as OMG's intent.
- The severity the specification requires for a violation. §8.3.1 says "should
  report"; it does not say error or warning. The pilot emits at least four
  constraints as warnings.

**Provisional.**

- The dependency-class A/B rule as a proxy for "intended decidability". It operationalises
  the dependency boundary as "names a model-library element or library helper".
  It does not assert that the published OCL executes as written: a class-A OCL
  expression can still be defective (27 rows are), intractable to evaluate, or
  require an interpretation. A class-B helper can
  in principle be inlined. The rule is reproducible, not ontological.
- The claim that the 437 model-local (class-A) constraints are "the syntactic surface". Many
  are structural conditions on specialisation and redefinition that would
  ordinarily be called semantic. The label is about *what the checker needs*, not
  about linguistic depth.

**Not established.**

- The behaviour of the released 2026-09.1 validator JAR. All source claims are
  about `master` at 2026-11-13; no JAR was built or decompiled.
- The false-negative rate of any validator on a representative model corpus.
  This study counts specified and named constraints; it does not run anything.
- Whether any tool implements all 437 class-A constraints.
- Whether the 2.1 Beta 2 text resolves the registered absences and ambiguities.

---

## 3. Evidence

### 3.1 The normative set and its own obligation taxonomy

The extraction is from the normative MOF XMI, not the PDF, because SysML Clause 2
states: "The specification comprises this document together with the content of
the machine-readable files listed on the cover page. **If there are any conflicts
between this document and the machine-readable files, the machine-readable files
take precedence.**" The XMI gives each constraint its constrained metaclass, its
prose comment and its OCL body in a machine-readable form; the PDF is the
human-readable rendering, used as a cross-check (all 623 names found, at the
clause recorded).

Both specifications classify their own constraints in §8.3.1. The SysML text is:

> "1. **Derivation constraints.** … A tool conformant to the SysML abstract
> syntax **shall always enforce** derivation constraints. …
> 2. **Semantic constraints.** … These constraints may be violated by a model as
> entered by a user or as interchanged. In this case, a tool **may** satisfy the
> constraints by introducing implied relationships into the model, it **may**
> simply report their violation, or it **may ignore** the violations. …
> 3. **Validation constraints.** … A valid model is a model that satisfies all
> validation constraints. A tool conformant to the SysML abstract syntax
> **should report** violations of validation constraints."

This is the first substantive answer to the issue's question: the specification
does not merely distinguish "normative" from "not"; it distinguishes three
normative kinds with three different forces, and the largest kind is explicitly
discretionary in reporting. The catalogue records this as the `obligation`
column and does not re-derive it.

The three kinds also have structural signatures in the OCL. `derive…` bodies are
equalities defining a derived property (`ownedFeature = ownedFeatureMembership.ownedMemberFeature`).
`validate…` bodies are predicates over the constrained element and its
metamodel-derived features (`feature->forAll(not isComposite)`). `check…` bodies
either call `specializesFromLibrary('Actions::acceptActions')` or require
redefinition/type-featuring/binding-connector relationships that the semantic
layer is permitted to insert. That is why dependency class B is dominated by
`check…` constraints: 171 of 208 `check…` constraints name a library element or
helper.

### 3.2 Dependency class A / B: what a checker needs

**Terminology revision (2026-11-13, after review).** The labels A/B/U are
**dependency classes**. This changes wording, not the frozen decision rule, the
sample, the labels assigned by either coder, or any count. "Mechanically
checkable" in the issue is operationalised as "no external library or
semantic-layer dependency"; executability is reported separately in
`executable_ocl_status`.

| | A: model-local (no external library/semantic dependency) | B: library / semantic layer | U | total |
|---|---:|---:|---:|---:|
| `derive…` (SHALL) | 233 | 2 | 0 | 235 |
| `check…` (MAY) | 35 | 171 | 2 | 208 |
| `validate…` (SHOULD) | 169 | 11 | 0 | 180 |
| **total** | **437** | **184** | **2** | **623** |

**Read A as a dependency class, not as a claim that the published OCL runs.**
27 of the 437 class-A rows and 14 of the 184 class-B rows carry a high-confidence
defect in their published body; `executable_ocl_status` records that separately.
The boundary says only that a checker needs no external library or semantic-layer
element under the frozen rule.

The 11 class-B `validate…` constraints are the sharpest illustration of why the
two dimensions must be separated. They are SHOULD-report, but a checker must load
normative library content and resolve it globally. Four are SysML
(`validateTriggerInvocationExpressionAtArgument`, `…AfterArgument`, `…WhenArgument`
and one other trigger condition, which call `specializesFromLibrary('Time::TimeInstantValue')`
etc.); seven are KerML, including `validateElementFilterMembershipConditionIsBoolean`
and `validateMetadataFeatureAnnotatedElement` (`resolveGlobal('Metaobjects::Metaobject::annotatedElement')`).
Conversely, 35 `check…` constraints are model-local and class A — decidable in
principle, but with no reporting obligation: the tool may ignore them.

Two independent coders applied the decision procedure to a 60-row stratified
sample (10 per specification × kind). Raw agreement was 60/60, Cohen's κ = 1.000;
all 60 rows were classified high confidence by the first coder, with three
medium by the second for reasons recorded in
[`coding/coder-b.csv`](../catalogue/coding/coder-b.csv). This establishes that
the rule can be applied without drift to ordinary rows. It does **not** establish
human-expert agreement, and it does not test the hardest cases: the sample was
drawn at random within strata, not adversarially.

### 3.3 The published OCL is not always executable

[`ocl-defects.csv`](../catalogue/ocl-defects.csv) records 48 named constraints with
a high-confidence or medium-confidence defect in the published body. The types:

| Defect | Count | Example |
|---|---:|---|
| placeholder body | 2 | `checkConstructorExpressionResultDefaultValueBindingConnector` body is `TBD`; same for `checkInvocationExpressionDefaultValueBindingConnector` |
| misspelled metamodel identifier | 34 | `relatedFeatures` for `relatedFeature`; `specializesFromLibary`; `refrencedFeature`; `exits` for `exists`; `implied` for `implies`; `allSuperTypes` for `allSupertypes` |
| malformed / misspelled library path | 7 | `'AssigmentAction::target::startingAt::accessedFeature'`; `'Occurrence::Occurrence::suboccurrences'` (package is `Occurrences`); `'ControlFunctions::\'.\'::source::target'` |
| suspected typo (distance 2) | 5 | `AStakholderMembership` for `StakeholderMembership`; `superType` for `supertypes` |

Each row records the clause, the context metaclass, the defective token, the
nearest metamodel identifier, a confidence, and a verification note. The method
is a shallow identifier audit against the vocabulary of both XMIs
([`audit_ocl.py`](../catalogue/audit_ocl.py)); it is **not** an OCL parser, and the
register is curated rather than machine-verdicted. The two `TBD` bodies and the
malformed literals are unambiguous; the misspellings are checked for absence from
both XMIs and for the existence of the intended identifier.

Two further mechanisation problems were found:

- **Language labels lie.** Nine constraints (1 SysML, 8 KerML) carry
  `language="English"` on a body that is ordinary OCL. An automated pipeline that
  filters on the language attribute would discard nine valid constraints.
- **The release notes do not use exact identifiers.** The 2026-01 note names
  `validateEndFeatureMembership` and `validateParameterMembership`; the metamodel
  defines `validateEndFeatureMembershipIsEnd`,
  `validateParameterMembershipOwningType` and
  `validateParameterMembershipParameterDirection`. Name-based audits undercount.

**What this does and does not establish.** It establishes that the specification
publishes formal bodies that cannot be implemented literally without
interpretation, and that the number of such cases is small but non-zero. It does
not establish that the OCL is *wrong* in each case: a reader can usually infer the
intended expression. The issue's class B ("normative but requiring semantics
beyond the abstract syntax") is therefore not the only way a rule escapes
mechanical checking; a defective formalisation does too.

### 3.4 Names in normative prose with no metamodel definition

The PDF ↔ XMI cross-check found 38 distinct constraint names in the PDFs that are
defined in neither XMI. They are **not** in the 623. Their distribution:

| Category | Count | Examples | Where |
|---|---:|---|---|
| renamed in the metamodel (plausible counterpart) | 12 | `checkFlowUsageFlowSpecification` → `checkFlowUsageFlowSpecialization`; `checkEventOccurrenceSpecialization` → `checkEventOccurrenceUsageSpecialization` | Clause 8.4 |
| missing from the metamodel | 11 | `checkClassifierSpecialization`, `checkFlowBinarySpecialization`, `validateForkNodeOutgoingSuccessions`, `validateJoinNodeIncomingSuccessions`, `validatePortDefinitionNestedUsagesNotComposite`, `validateDefinitionVariationMembership`, `validateUsageVariationMembership` | Clause 8.4 |
| typo of a metamodel name | 7 | `checkConstructorExpressionResultFeatureRedefnition`, `checkFeatureParameterRefinition`, `checkPartUsageSupartSpecialization` | Clause 8.4 |
| not a constraint name (operation, library feature, example action) | 3 | `checkCondition` (OCL operation), `checkConstraints` (library feature), `checkLevel` (action in an example) | 8.3.x / 7.17 |
| example only | 3 | `validateUsageOwningType` (the naming-convention example), `checkConnectorEndRedefinition`, `checkFeatureValueExpressionTypeFeaturing` | 8.3.1 / 8.4.2 |
| subsumed by a generic constraint | 2 | `validateForkNodeOutgoingSuccessions` → `validateControlNodeOutgoingSuccessions`; `validateJoinNodeIncomingSuccessions` → `validateControlNodeIncomingSuccessions` | Clause 8.4 |

**The important subset is the 31 names that state normative conditions in Clause 8.4.** Clause 8.4 is
the Semantics clause. A sentence there that says "the `checkFlowBinarySpecialization`
constraint further requires…" is a normative assertion. But the metamodel defines
no such constraint, and a conformant abstract-syntax tool is only required to
validate "the constraints defined in the SysML metamodel" (Clause 2). The result
is a class of requirements that are stated, normative, and formally uncatchable.

Two examples make the consequence concrete:

- `validateForkNodeOutgoingSuccessions` and `validateJoinNodeIncomingSuccessions`
  state 1..1 multiplicity conditions for fork/join successions. The metamodel has
  generic `validateControlNodeOutgoingSuccessions` / `…IncomingSuccessions`
  instead. Whether the generic rule subsumes the specific one is an
  interpretation; the prose does not say.
- `checkClassifierSpecialization` is asserted in Clause 8.4.2 to be automatically
  satisfied by `checkStructureSpecialization`. No `checkClassifierSpecialization`
  constraint exists in the KerML XMI. A reader who trusts the sentence will look
  for a rule that is not there.

### 3.5 The silence-and-discretion register

[`silence-register.md`](../catalogue/silence-register.md) records ten areas and
labels each with a **kind**. Only four are silence in the strict sense — no
normative rule at all (D1–D4). The others are explicit discretion (D5), explicit
delegation (D8), unresolved ambiguity (D6), an area outside the well-formedness
surface (D7), or an oracle/provenance gap (D9–D10); they have the same practical
effect on a checker but are not "the specification says nothing". The three
`absent` entries with the largest consequences are:

**Default multiplicities.** SysML Clause 8 contains no default-multiplicity rule;
the `1..1` default lives in the non-normative Language Description (§7.6.3). OMG
issue SYSML21-185, filed by the constraint's author, states: "In the SysML
Specification, in non-normative Language Description subclause 7.6.3 Usages, it
describes several conditions that, if met, require a usage to have default
multiplicity 1..1. However, there is no formal specification of this in the
normative Clause 8 Metamodel." The pilot invented a default and changed it in
2026-09, a declared backward incompatibility: "may result in multiplicity
violations in the interpretation of some models." A multiplicity diagnostic is
therefore not attributable to the model alone.

**Type checking and inference.** There are six local conformance constraints in
the catalogue, but no general rule that an assigned value conforms to the
feature's type, and none that infers a type. Syside states: "the specification
itself completely omits type checking and type inference"; its example
`attribute num : ScalarValues::Positive = 5.0;` "is fine according to the Pilot
Implementation" and is a type error in Syside. This is the single largest gap
between what the specification checks and what "the model is correct" normally
means.

**Units and dimensions.** Zero constraints mention dimensional consistency. The
Systems Model Library defines quantity dimensions; the metamodel does not require
a checker to compare them. Syside cannot yet infer dimensions, so it "cannot
currently catch such errors as assigning length quantity to a mass quantity."
Assigning a length to a mass is a conformity question with no normative answer.

The remaining entries are recorded with their evidence and implementation
choices, and are not all silence: severity/identity is under-specified (D4);
implied-relationship materialisation is explicit discretion (§8.3.1's MAY, D5);
membership resolution is ambiguous (D6); execution lies outside the
well-formedness surface (D7); method-level adequacy is explicitly delegated
(§1: "the specific methods and practices may impose additional constraints on
how the language is used", D8); and the conformance-oracle and version-identity
entries (D9–D10) are institutional/artefact gaps, not missing language rules.

### 3.6 Specified versus enforced versus reported

The pilot inventory ([`validator-inventory.csv`](../catalogue/validator-inventory.csv))
is a source-code inventory of 116 `@Check` methods. Cross-checked exactly by name
against the catalogue ([`validator-coverage.json`](../catalogue/validator-coverage.json)).
(The inventory's narrative reports 202 distinct constraint names; recomputation
from the CSV gives 200. The difference of two does not affect the coverage
conclusion and is recorded rather than reconciled.)

| Catalogue slice | Catalogue count | Matched in a non-TODO `@Check` | Matched only in a TODO method | Identifier coverage |
|---|---:|---:|---:|---:|
| SysML `derive…` | 145 | 0 | 0 | 0 (0%) |
| SysML `check…` | 128 | 0 | 0 | 0 (0%) |
| SysML `validate…` | 92 | 70 | 7 | 77 (84%) |
| KerML `derive…` | 90 | 0 | 0 | 0 (0%) |
| KerML `check…` | 80 | 2 | 0 | 2 (2%) |
| KerML `validate…` | 88 | 77 | 0 | 77 (88%) |
| **total** | **623** | **149** | **7** | **156 (25.0%)** |

**This is identifier coverage, not implementation or conformance coverage.** A
name in a `@Check` method's comment or diagnostic-code constant does not
demonstrate that the method executes, that it fires on a violating model, or that
it enforces the constraint correctly. Seven of the 156 appear only in TODO-only
methods; the 149 in non-TODO methods are still source-level attributions. No
validator was built or run, and the 2.0/2.1 revision skew remains decisive. The
25.0% figure should not be read as "the pilot implements a quarter of the
specification".

These identifier-match rates are **lower bounds**, for three reasons that are
themselves findings:

1. **The pilot uses different identifiers.** `validateReferenceUsageIsReferential`
   in the pilot corresponds to `validateReferenceUsageIsReference` in the
   catalogue; `validateDifferencingTypesNotSelf` to
   `validateTypeDifferencingTypesNotSelf`; `validateElementFilterMembershipIsBoolean`
   to `validateElementFilterMembershipConditionIsBoolean`. 44 pilot identifiers
   have no exact catalogue match.
2. **Some checks are named after the condition, not the constraint.** `checkSuccession`
   and `checkTransitionUsage` are methods, not constraints.
3. **The pilot targets 2.1 Beta 2.** Since 2026-07, a pilot check may implement a
   constraint that does not exist in 1.0/2.0. The catalogue cannot adjudicate
   those. This is the largest single limit on the comparison.

Even with those caveats, the pattern is not ambiguous. The pilot's validator is a
**validator for `validate…` constraints**: it carries identifiers for 154 of
180, and almost none for `check…` or `derive…` constraints. That is consistent with the architecture: the
`check…` constraints are largely handled by the adapter/implied-relationship
layer, not by diagnostics, and the `derive…` constraints are computed by getters.
The specification's own MAY licenses exactly this. But it has a consequence for
the research question: **the 208 `check…` constraints are not "checked" in any
sense a validator pass could report.** They are either materialised, or ignored.

The first-party admissions are independent of the name matching:

- **2026-01:** "The following validation constraints were previously **not being
  checked**, since they were automatically satisfied due to getter overrides.
  Since these getter overrides have now been removed, checks have been
  implemented for all the constraints." Thirteen names follow (7 KerML, 6 SysML).
- **2026-03:** "The Pilot Implementation was not reporting this as an error,
  **which was not conformant with the normative metamodel for KerML** (and, so,
  SysML, too)." The release removes code that suppressed `checkConnectorTypeFeaturing`.
- **2026-09:** the default-multiplicity change, a declared backward incompatibility.

The 2026-07 release notes go the other way and name four `check…` constraints as
resolved, none of which appears in either validator source at 2026-11-13. I do
not adjudicate that; it is recorded as contested.

### 3.7 The deep trace

[`deep-trace.md`](../catalogue/deep-trace.md) follows 15 constraints from clause
to two independent implementations, and 18 more to one implementation plus the
normative text. Four further release-note claims could not be traced. The strongest case is the control-node family: eight SysML
`validate…` constraints, each a short model-local (dependency class A) OCL
predicate, each SHOULD-report,
each a TODO in an empty or near-empty `@Check` method, each independently
reported by OpenSysML as a "pilot gap". This meets the issue's "at least two
implementations" bar at the **source level** (pilot source and OpenSysML
differential), and the constraints are not ambiguous or library-dependent.
Neither source runs the check on a violating model: this is a hypothesis for
runtime confirmation (issue #8), not a measured false-negative rate.

Other traced cases:

- `validateFeatureValueOverriding` — Syside's diamond example asserts a pilot
  false negative; OpenSysML implements the rule but does not adjudicate the
  case. **Contested.**
- `validateAttributeUsageFeatures` / `validateAttributeDefinitionFeatures` — both
  enforced, but Syside reports that the **normative standard library itself**
  contained non-conforming attributes. Enforcement does not imply corpus
  conformance.
- `checkFeatureValueBindingConnector` — class B; the pilot does not construct
  implicit binding connectors, so the predicate cannot be evaluated without
  materialising implied elements the specification says a tool MAY insert.
- `validateRedefinitionDirectionConformance` — Syside records two KerML clauses
  that point in opposite directions on implicit flow directions. The verdict on
  the same model depends on which clause is read. This is a specification
  ambiguity, not a tool defect.
- `checkMetadataFeatureSemanticSpecialization` — Syside: the pilot "silently
  ignores" a library `CauseAndEffect` defect, so `CauseMetadata` and
  `EffectMetadata` can annotate any element.
- `validateMultiplicityRangeBounds` — the pilot's own comment says the published
  OCL should be corrected from OMG issue KERML-199.

### 3.8 What the coding agreement does and does not show

60/60 and κ = 1.000 is a strong reproducibility result for the rule but a weak
reliability result for the construct. The sample was stratified to cover all six
specification × kind cells, but the ordinary rows are easy: the presence of a
quoted library path or a `specializesFromLibrary` call settles most. The hard
cases — is an unqualified `Action` a library element or a typo? is
`multiplicityHasBounds` itself library-dependent? — are rare and were not
oversampled. The honest claim is: **the decision procedure is stable across two
independent appliers on a representative sample**; it is not "two experts agree
on the boundary".

---

## 4. Counter-evidence and tensions

**Tension 1: Clause 2 requires validation; §8.3.1 permits ignoring the largest
class.** Clause 2: an Abstract-Syntax-Conformant tool "must also provide a way to
validate the well-formedness of models that corresponds to the constraints
defined in the SysML metamodel." §8.3.1: for semantic constraints, a tool "may
ignore the violations." Both are in the same normative document. A tool can
therefore provide "a way to validate" that reports nothing for 208 constraints,
and be conformant on a plain reading. This is not a tool defect; it is a tension
in the specification, and it is the strongest counter-argument to treating
validator acceptance as a correctness signal.

**Tension 2: "The specification is complete; the tools lag" is supported, but
only for part of the surface.** The control-node family is exactly the tools-lag
story: eight model-local rules, no source-level enforcement, independently
reported. But the
same trace shows constraints the specification cannot express without
interpretation (KERML-199), constraints whose verdict depends on which KerML
clause you read (`validateRedefinitionDirectionConformance`), and requirements in
Clause 8.4 with no metamodel definition. Tools lag *and* the text is uneven; the
two are not alternatives.

**Tension 3: "Under-specified where it matters" is also supported, but "under-specified"
is the wrong word for some of it.** The specification is not silent about
derivation or validation; it publishes OCL for all 623 named constraints. The
silence is in specific *kinds* of property — type conformance, units, behaviour,
method adequacy. And some of the "silence" is deliberate delegation (§1, §8.3.1),
not oversight. The useful formulation is: the specification formalises structure
and local well-formedness, and delegates semantics, typing, units, behaviour and
method to the semantic layer, the libraries, or the adopter.

**Tension 4: the third reading — the specified constraints are mostly the
uninteresting ones — is the one the counts most support.** Of 437 dependency
class-A constraints, 233 are derivations (not well-formedness checks at all), and 169 are
validation predicates over structural properties (cardinalities, owning types,
specialisation shape). The engineering-interesting properties — is this the right
decomposition, is the value type-correct, are the units consistent, does the
state machine terminate — have zero or near-zero formal coverage. If that reading
holds, automated validation has a ceiling that is a property of the language, not
of the tools. This study cannot prove the reading, but it supplies the counts
that make it testable.

**Counter-evidence to my own dependency-class boundary.** OpenSysML's
control-node adjudication found that a literal reading of the four multiplicity
OCL constraints rejects `first a then f;`, a form the specification's own
examples use. So a model-local class-A constraint can still be *wrong* as
written, or require an interpretation. Dependency class A means "no external
library semantics are needed under the frozen rule", not "the OCL is executable
or uncontested". The OCL-defect register is the same
point in a different form.

**Counter-evidence to "the pilot is permissive".** The pilot enforces 154
`validate…` constraints and has added checks over time; the 2026-03 release
removed a suppression and accepted the resulting backward incompatibility. It is
not a tool that ignores validation. The finding is narrower and more useful: its
validation surface is the `validate…` layer, plus very little else, and that
layer is 180 of 623 constraints.

---

## 5. Investigation and access log

All retrievals 2026-11-13 (UTC). Nothing was bypassed.

| Resource | Result | Notes |
|---|---|---|
| SysML 2.0 Language PDF (`formal/2026-03-02`) | 200, 3,804,140 bytes, sha256 `46e6c047…` | 691 pages; text extracted with `pdftotext -layout` (1,721,431 chars) |
| KerML 1.0 PDF (`formal/2026-03-01`) | 200, 1,821,407 bytes, sha256 `3bcc96f9…` | 1,144,341 chars extracted |
| SysML XMI (`ptc/25-02-15`) | 200, 1,135,635 bytes, sha256 `caa65d54…` | primary extraction source |
| KerML XMI (`ptc/25-04-04`) | 200, 962,254 bytes, sha256 `45b18775…` | primary extraction source |
| SysML JSON schema, KerML JSON schema | 200 | fetched for provenance, not used in extraction |
| `omg.org/spec/SysML/2.1` | **404** | missing / never published; no 2.1 normative text exists to pin |
| `omg.org/spec/SysML/2.0/PDF` | **404** | the correct route is `/Language/PDF`; recovered from the catalogue page |
| GitHub raw validator sources | 200 | SysML 78,434 bytes; KerML 77,545 bytes; hashed |
| GitHub releases API | 200, 90 releases | used instead of scraping the rendered releases page; full bodies, attributable |
| `issues.omg.org/browse/SYSML21-185` | **302 → login** | access boundary; not bypassed |
| `issues.omg.org/issues/SYSML21-185` | 200 | authorised public record; recovered the full issue text |
| `tools/oracle/errata` (raw file) | **404** | it is a directory; contents recovered via the two `errata.go` files |
| Syside differences page | 200, 68,269 bytes | signed retrieval; no challenge |
| OpenSysML differential | 200, 327,213 bytes | third-party; read the control-node and feature-value sections directly |
| INCOSE certification paper (prior note) | **403 Cloudflare challenge** (`cf-ray a59d07b0…-AMS`) | recorded in `evidence/spec-tooling.md` §6.5; not revisited, not bypassed |

**robots.txt.** Not consulted for any URL used here. All sources are OMG
published files, GitHub raw endpoints, the GitHub public API, or public vendor
documentation. No retrieval relied on the robots.txt exception; no access control
was challenged.

**Text extraction.** The PDF text has layout artefacts. Constraint names in
tables can be split across lines (`checkAssociation` + `Specialization`); the
extraction excludes any candidate that is a proper prefix of an XMI name and
records 86 such fragments separately. Page headers/footers are interleaved; the
parser skips table-of-contents lines and tracks the nearest numbered heading.

**A date conflict, recorded not resolved.** OMG catalogue pages say September
2025; the PDFs say March 2026 and the file IDs are `formal/26-03-*`. The Systems
Modeling release README explains the later date as an editorial update for ISO.
The catalogue cites the PDF cover date and document number.

---

## 6. Delegation and verification

Two teammates were used, for independent lines of work.

**`tooling-evidence`** gathered implementation behaviour: the two pilot validator
sources and their release notes, OpenSysML's differential and defect registry,
Syside's divergence page, and the SYSML21-185 record. Deliverables:
[`impl-evidence.md`](../catalogue/impl-evidence.md) and
[`validator-inventory.csv`](../catalogue/validator-inventory.csv).

I verified the claims used in this report against the primary sources where they
were pivotal:

- Re-read the Syside differences page directly (signed retrieval, 200) for the
  type-checking, diamond, implicit-binding-connector, unit, `CauseAndEffect`,
  name-resolution and multiplicity statements quoted here.
- Re-read the OpenSysML control-node table directly (raw `develop` file) for the
  eight "pilot gap" verdicts and the "nine constraints / eight TODOs" wording.
- Re-fetched the pilot releases API and confirmed the 2026-01 "not being
  checked", 2026-03 "not conformant", and 2026-09 default-multiplicity quotes.
- Fetched the SYSML21-185 public record and confirmed its status and summary.
- Re-ran the validator inventory cross-check from the CSV rather than accepting
  the summary counts; the 156/623 identifier-coverage figure (149 non-TODO, 7
  TODO-only) is my computation from the teammate's inventory.

I did **not** independently re-fetch every release note from 2026-02 to 2026-09.1;
the chronology in `impl-evidence.md` is the teammate's, and I quote only the
releases I verified above.

**`coder-b`** independently classified the 60-row sample using the frozen codebook,
without access to my labels. It read only the codebook and the sample. Its counts
(A 42, B 17, U 1) match the first coder exactly; 60/60 raw agreement. I verified
the file's 60 rows, columns and sample order. The limitation is stated in §3.8:
both coders are LLM-based, so this is reproducibility across independent appliers,
not human-expert reliability.

No subagent was asked to classify the specification text, and no subagent output
was treated as a second witness for a source it read in the same way as me.

---

## 7. Important uncertainties and limits

1. **The catalogue is pinned to 1.0/2.0; the pilot targets unpublished 2.1 Beta 2.**
   This is the largest limit. The specified–enforced comparison is cross-revision
   by necessity. A 2.1 catalogue cannot be built from published OMG artefacts
   today.
2. **Dependency class A/B is operationalised, not proved.** The rule is
   reproducible and auditable, but it classifies *what a checker needs*, not
   whether the published OCL executes. 27 class-A rows carry a high-confidence
   defect, and a class-A expression can still require an interpretation (see the
   control-node multiplicities) or be intractable to evaluate.
3. **The OCL audit is shallow.** It finds identifier-level problems, not type
   errors or semantic inconsistencies in the OCL. The 48-row register is a
   curated sample of a larger possible defect surface.
4. **No tool was run.** Every implementation claim is source- or document-level.
   The false-negative rate of the pilot, Syside or OpenSysML is not measured.
5. **The coding study is small and easy.** 60 rows, two LLM coders, one sample,
   no adjudication round after disagreement (there were none to adjudicate).
6. **The silence-and-discretion register is an argument, not a proof of absence.**
   Ten areas were searched by name, OCL body and specification text; an unusual
   constraint that encodes a type or unit rule under a name that does not contain
   the term could have been missed. Only four of the ten entries are genuine
   absence; two are explicit discretion/delegation, one is ambiguity, one is
   outside the well-formedness surface, and two are oracle/provenance gaps. The
   register names the search terms and the counts, so the claim is auditable.
7. **The prose-only categorisation is inferential.** "Renamed" and "missing" are
   my reading of context and nearest name, not OMG's intent. The CSV marks each
   row's status and nearest name so a reader can disagree with a specific row.

---

## 8. What would change the answer

- **Publishing SysML 2.1 Beta 2 / KerML 1.1 Beta 2.** The pilot's target set would
  become auditable, the 44 unmatched pilot identifiers could be classified, and
  the cross-revision caveat would disappear.
- **An OMG conformance suite.** It would replace this catalogue's denominator with
  an authoritative one, and turn identifier coverage into a measured enforcement
  rate on a violating-model corpus.
- **A runtime differential.** Running the pilot, Syside and OpenSysML on a
  purpose-built corpus of one violating model per class-A constraint would
  convert the source-level gap into a measured false-negative rate. This is the
  natural next study, and the catalogue is its input.
- **Resolution of SYSML21-185, KERML-199 and the flow-direction ambiguity.** Each
  would move a specific register entry from "silent/defective/contested" to
  "specified".
- **A human-expert coding round.** If two systems engineers disagreed materially
  with the dependency-class calls on the hardest 20 constraints, the classification
  would need revision. The current agreement result does not test that.

---

## 9. Dead ends and things that did not work

- **`omg.org/spec/SysML/2.1` is 404.** There is no published 2.1 document, so the
  pilot's target cannot be pinned. This is a finding, not a retrieval failure.
- **The INCOSE certification paper** remains behind a Cloudflare challenge (403,
  `cf-ray a59d07b0…`). It was not revisited. Its existence suggests an OMG
  certification programme, but no claim about its content is made.
- **A literal OCL parse was not attempted.** Writing or adopting an OCL parser was
  out of scope; the shallow identifier audit plus manual curation was the
  proportionate method. A full parse would produce a better defect count and is
  the obvious extension.
- **The pilot's XML/XMI interchange JSON schemas** were fetched but not used. The
  constraint set is in the MOF XMI; the JSON schema describes instances, not
  constraints. Recorded so the choice is auditable.
- **The 39 PDF-only names cannot be resolved to OMG intent** without the RTF
  issue record for each. The nearest-name mapping is a reading aid, not a
  resolution.
- **The Syside diamond example was not reproduced.** No commercial licence, and
  the vendor's example is a worked illustration, not a test fixture.

---

## 10. Implications for the main question

**For "reliably validated".** A validator pass is a claim about a specific,
enumerated subset of constraints. Under the pinned 1.0/2.0 text, that subset is at
most the 180 `validate…` constraints, and the pilot names 154 of them. It says
nothing about the 208 `check…` constraints (discretionary), the 235 `derive…`
constraints (computed, not checked), or the silent areas (type, units, behaviour,
method). Any experiment that uses validator acceptance as the dependent variable
should say which of these it means, and report the constraint-set version. The
catalogue gives it a denominator.

**For "correct models".** The four senses of correctness in the summary are not
nested, and the largest engineering sense is unformalised. A generated SysML model
that passes every available validator can still assign a length to a mass, give a
`Positive` the value `5.0`, use an undefined symbol in an ambiguous namespace, or
describe a state machine that cannot execute. This is not a tooling deficiency
that a better LLM or a longer repair loop fixes; it is a property of what the
standard specifies.

**For validator reliability (issue #8).** The false-negative rate is not a
single number. It is at least: eight control-node constraints (reported at source
level by two implementations; runtime confirmation is the first experiment this
suggests), 13 constraints unchecked before 2026-01 (first-party), four
constraints emitted as warnings, seven constraints whose diagnostic identity is
lost, and 208 constraints whose reporting is discretionary. A reliability study
that samples "constraints" uniformly will be dominated by easy structural rules;
one that samples by engineering consequence will find the absences and the
discretion.

**For benchmark design (issue #13).** A benchmark needs a pinned catalogue, a
pinned validator build, and a per-constraint expected verdict. This catalogue is a
first version of the first artefact. It is not a benchmark: it has no violating
models and no measured behaviour. That is the next step.

**For the rival readings.** The counts support a composite: tools lag on the
specified structural rules (control nodes), the specification is silent or
defective where the engineering interest is (type, units, defaults, behaviour),
and the specified constraints are dominated by derivations and structural
predicates. The third reading is the one that most changes the programme: if the
checkable surface is mostly uninteresting, automated validation has a ceiling
that no amount of GenAI or repair-loop engineering removes.

---

## 11. Adjacent questions noticed, not researched

- **Issue #2** (do tools agree?) — the pilot/Syside/OpenSysML divergence in this
  report is qualitative; a systematic same-model comparison is issue #2.
- **Issue #7** (error populations) — the defect and silence/discretion registers suggest a
  taxonomy of model errors that validators cannot see; not built here.
- **Issue #8** (validator reliability) — the 8 control-node gaps and the 17
  declared-but-unimplemented constraints are a ready-made test set; not executed.
- **Issue #10** (semantic ceiling) — the silence-and-discretion register is its evidence base.
- **The 2.1 Beta 2 constraint set** — outside published OMG artefacts; not
  researched.
- **The OMG RTF issue records behind the 39 prose-only names** — not retrieved;
  would resolve rename vs missing for each.
- **A full OCL semantic parse** — out of scope; would improve the defect count.

---

## 12. Sources

**Normative artefacts (pinned, hashed).** SysML 2.0 Language Specification,
`formal/2026-03-02`, <https://www.omg.org/spec/SysML/2.0/Language/PDF>; KerML 1.0,
`formal/2026-03-01`, <https://www.omg.org/spec/KerML/1.0/PDF>; SysML MOF XMI,
`ptc/25-02-15`, <https://www.omg.org/spec/SysML/20250201/SysML.xmi>; KerML MOF
XMI, `ptc/25-04-04`, <https://www.omg.org/spec/KerML/20250201/KerML.xmi>.

**Implementation.** SysML-v2-Pilot-Implementation `master`, validator sources
<https://raw.githubusercontent.com/Systems-Modeling/SysML-v2-Pilot-Implementation/master/org.omg.sysml.xtext/src/org/omg/sysml/xtext/validation/SysMLValidator.xtend>
and <https://raw.githubusercontent.com/Systems-Modeling/SysML-v2-Pilot-Implementation/master/org.omg.kerml.xtext/src/org/omg/kerml/xtext/validation/KerMLValidator.xtend>;
releases API <https://api.github.com/repos/Systems-Modeling/SysML-v2-Pilot-Implementation/releases?per_page=100>;
OpenSysML <https://github.com/Open-MBEE/OpenSysML> and
<https://raw.githubusercontent.com/Open-MBEE/OpenSysML/develop/docs/project/pilot-differential.md>;
Syside 1.0.1 differences <https://docs.sensmetry.com/1.0.1/about/differences/>.

**OMG issue.** SYSML21-185, <https://issues.omg.org/issues/SYSML21-185>
(anonymous public record; the `/browse/` route requires login and was not
bypassed).

**Project evidence notes.** [`evidence/spec-tooling.md`](../evidence/spec-tooling.md),
[`evidence/literature.md`](../evidence/literature.md),
[`evidence/industrial-practice.md`](../evidence/industrial-practice.md) — used for
orientation and for the implementation pointers verified here.

**Generated artefacts.** [`catalogue/constraints.csv`](../catalogue/constraints.csv),
[`classified.csv`](../catalogue/classified.csv),
[`ocl-defects.csv`](../catalogue/ocl-defects.csv),
[`prose-only-names.csv`](../catalogue/prose-only-names.csv),
[`silence-register.md`](../catalogue/silence-register.md),
[`deep-trace.md`](../catalogue/deep-trace.md),
[`impl-evidence.md`](../catalogue/impl-evidence.md),
[`validator-inventory.csv`](../catalogue/validator-inventory.csv),
[`validator-coverage.json`](../catalogue/validator-coverage.json),
[`coding/codebook.md`](../catalogue/coding/codebook.md),
[`coding/coder-a.csv`](../catalogue/coding/coder-a.csv),
[`coding/coder-b.csv`](../catalogue/coding/coder-b.csv).
