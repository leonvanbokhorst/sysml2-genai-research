# Implementation evidence: what the SysML v2 / KerML pilot validator actually enforces

**Scope.** Independent-implementation evidence only: which well-formedness constraints the pilot validator enforces, which are declared but not enforced, where the implementation documents divergence from the normative metamodel, and what third parties report. This note does **not** build the version-pinned constraint catalogue and does not characterise the specification's normative set; it supplies the implementation side and the constraint names as the implementation itself spells them.

**Retrieval date for every source below: 2026-11-13 (UTC).** Every claim names its retrieved source. No claim rests on a search snippet, and no quote, URL or line number is reconstructed from memory.

**Reading conventions.** **[INFERENCE]** marks my own reasoning, not a source assertion. **[VENDOR]** marks a commercial third party's characterisation of the pilot. **[THIRD-PARTY]** marks an independent open-source implementation's characterisation, which is also self-interested. Line numbers refer to the exact files hashed in §1; where another party cites different line numbers for the same code, that is noted rather than reconciled silently.

---

## 1. Source table

| # | Source | URL | What it is | Retrieved (UTC) | HTTP | Bytes | sha256 | Class |
|---|---|---|---|---|---|---|---|---|
| S1 | `SysMLValidator.xtend` | `https://raw.githubusercontent.com/Systems-Modeling/SysML-v2-Pilot-Implementation/master/org.omg.sysml.xtext/src/org/omg/sysml/xtext/validation/SysMLValidator.xtend` | SysML validation checks, Xtend source, branch `master` | 10:34:00 | 200 | 78,434 | `7d4a29e220dfd6032f6ccffe7a513cecf8d7dd3953deff3eebaae58c9b7069ab` | primary (source code) |
| S2 | `KerMLValidator.xtend` | `https://raw.githubusercontent.com/Systems-Modeling/SysML-v2-Pilot-Implementation/master/org.omg.kerml.xtext/src/org/omg/kerml/xtext/validation/KerMLValidator.xtend` | KerML validation checks, Xtend source, branch `master` | 10:34:00 | 200 | 77,545 | `82f0495daf28f4da437155207d135b3fedf3b68de914645ae37d78f08978e219` | primary (source code) |
| S3 | Releases API | `https://api.github.com/repos/Systems-Modeling/SysML-v2-Pilot-Implementation/releases?per_page=100` | JSON for 90 releases incl. full release-note bodies | 10:34:01 | 200 | 978,813 | `bb40656576f031995f7615c345669d879e7f75d202d7286008427fcba84b2adb` | primary (first-party release notes) |
| S4 | SYSML21-185 | `https://issues.omg.org/issues/SYSML21-185` | OMG RTF issue record, public (anonymous) view | 10:34:34 | 200 | 11,057 | `eb9817bf430f1875722c4558ad285c0b89000771b9a3e5b51ff7c66ad9cde0cf` | primary (OMG issue tracker) |
| S5 | SYSML21-185 `browse` URL | `https://issues.omg.org/browse/SYSML21-185` | Jira `browse` view of the same issue | 10:34:28 | **302 → login** | — | — | access boundary, not bypassed |
| S6 | Syside "Differences to the Pilot Implementation" | `https://docs.sensmetry.com/1.0.1/about/differences/` | Vendor divergence documentation, Syside 1.0.1 | 10:34:38 | 200 | 68,269 | `debb430ca782a5115e6c14f204ff568b96484c31f664d904bd9aed0fb4f5304a` | **vendor** |
| S7 | OpenSysML README | `https://raw.githubusercontent.com/Open-MBEE/OpenSysML/develop/README.md` | Independent Go implementation, branch `develop` | 10:34:39 | 200 | 58,785 | `e6a7c0df6d392c35159cc9f786d5b229f5117bc6153372efec2e8558f794e55b` | **third-party** |
| S8 | OpenSysML pilot differential | `https://raw.githubusercontent.com/Open-MBEE/OpenSysML/develop/docs/project/pilot-differential.md` | Diagnostic-by-diagnostic comparison against pilot `2026-09` | 10:34:47 | 200 | 327,213 | `a00543f64e59804384ac0b0d460704be52aa5d5132d4eeb03bcfeb163fec1359` | **third-party** |
| S9 | OpenSysML OMG-issues registry | `https://raw.githubusercontent.com/Open-MBEE/OpenSysML/develop/docs/project/omg-issues.md` | Registry of claimed defects in OMG-published material | 10:34:48 | 200 | 167,098 | `431385a2441ad937d034b687176ba96ede1fb387b837bf9053be523e80b42d30` | **third-party** |
| S10 | Errata overlay (registry code) | `https://raw.githubusercontent.com/Open-MBEE/OpenSysML/develop/tools/oracle/errata/errata.go` | The executable errata registry (`Registry()`) | 10:34:59 | 200 | 5,519 | `5c3ba3ddc3cb0097a375c83cca51536c2195016602a12cfb005c43274b993d4c` | **third-party** |
| S11 | Errata overlay (library entries) | `https://raw.githubusercontent.com/Open-MBEE/OpenSysML/develop/internal/workspace/libs/errata/errata.go` | `LibraryEntries()` — the 10 standard-library entries | 10:35:10 | 200 | 16,809 | `8306bb6a026ede95b7d6442ff7179ca7f8ad1b22a516ccf3233f37a7f3b121ae` | **third-party** |
| S12 | `tools/oracle/errata` (bare path) | `https://raw.githubusercontent.com/Open-MBEE/OpenSysML/develop/tools/oracle/errata` | Attempted as a file | 10:34:47 | **404** | 14 | — | not a file — `tools/oracle/errata/` is a directory (S10, S11 are its contents) |

Grounding file read first, not cited as evidence: [`evidence/spec-tooling.md`](../evidence/spec-tooling.md) §3.3, §4, §6.

---

## 2. Constraint-level evidence table

Each row is one constraint-level statement I can attribute to a retrieved source. "Establishes" is deliberately narrow.

| Constraint / subject | Kind | Implementation | Statement (verbatim) | Source | Class | What it establishes |
|---|---|---|---|---|---|---|
| default multiplicity (SYSML21-185) | derive/validation policy | Pilot | "For the specification, it is expected that this situation will be handled as part of the resolution to [SYSML21-185](https://issues.omg.org/issues/SYSML21-185) (\"Default multiplicities are not formally specified\")." | S3, release `2026-09` and `2026-09.1` | primary | The pilot states, first-party, that it chose default-multiplicity behaviour the specification does not formally fix |
| default multiplicity | — | Pilot | "Previously, default multiplicities were not applied if a usage had explicit owned subsettings, including owned redefinitions, largely consistent with the SysML specification." … "This has now been changed so that a usage with an explicit, non-redefinition owned subsetting _does_ get the SysML `1..1` default multiplicity." | S3, `2026-09` | primary | Behaviour changed in a way the pilot itself calls only "largely consistent" before the change |
| default multiplicity | — | Pilot | "it may result in multiplicity violations in the interpretation of some models" | S3, `2026-09`, Backward Incompatibilities | primary | A validation-semantics change with an admitted backward incompatibility |
| SYSML21-185 issue record | — | OMG | Status "open"; Source "Model Driven Solutions ( Mr. Ed Seidewitz )"; Summary "In the SysML Specification, in non-normative Language Description subclause 7.6.3 Usages, it describes several conditions that, if met, require a usage to have default multiplicity 1..1. However, there is no formal specification of this in the normative Clause 8 Metamodel."; Reported "SysML 2.0b2 — Sat, 15 Jun 2024 17:52 GMT"; Updated "Fri, 20 Jun 2025 22:40 GMT" | S4 | primary | The **specification itself** is recorded as silent on default multiplicity, by the constraint author, and the issue was still open ~17 months later |
| `checkConnectorTypeFeaturing` | check | Pilot | "the `checkConnectorTypeFeaturing` constraint is impossible to satisfy for the binding connectors implied by these feature references. The Pilot Implementation was not reporting this as an error, which was not conformant with the normative metamodel for KerML (and, so, SysML, too)." | S3, `2026-03` | primary | A first-party admission of a deliberate *suppression* of a normative constraint |
| `checkConnectorTypeFeaturing` | check | Pilot | "Removed code that suppressed violations of `checkConnectorTypeFeaturing` within feature references in filter expressions." | S3, `2026-03`, Bug Fixes | primary | The suppression existed as code and was removed — i.e. it was an implementation choice, not a parse artefact |
| `checkConnectorTypeFeaturing` | check | Pilot | `// TODO: Be able to remove these special cases` — guarding the `location instanceof FeatureReferenceExpression \|\| location instanceof FeatureChainExpression` branch inside `checkConnector` | S2 `:1023` | primary | The 2026-03 fix removed the *filter-expression* suppression; a related special case **remains** in `master` at 2026-11-13 |
| 13 constraints previously unchecked | validate | Pilot | "The following validation constraints were previously **not being checked**, since they were automatically satisfied due to getter overrides. Since these getter overrides have now been removed, checks have been implemented for all the constraints." — KerML: `validateEndFeatureMembership`, `validateParameterMembership`, `validateCollectExpressionOperator`, `validateFeatureChainExpressionOperator`, `validateIndexExpressionOperator`, `validateSelectExpressionOperator`, `validateFlowEndIsEnd`; SysML: `validateUsageIsReferential`, `validateReferenceUsageIsReferential`, `validateAttributeUsageIsReferential`, `validateEnumerationDefinitionIsVariation`, `validateEventOccurrenceUsageIsReference`, `validatePortUsageIsReference` | S3, `2026-01` | primary | 13 named constraints had **no effective check** before 2026-01; the text says explicitly they were "not being checked" |
| `validateEndFeatureMembershipIsEnd` | validate | Pilot | "the `isEnd` property of the `ownedMemberFeature` of an `EndFeatureMembership` will no longer be automatically be `true`, but must be explicitly set to `true` to meet the `validateEndFeatureMembershipIsEnd` constraint" | S3, `2026-01` | primary | Enforcement was previously achieved by a getter default, not by a check |
| `validateAttributeUsageIsReferential` | validate | Pilot | "it is possible to use the `setIsComposite` method to set this to `true`, even though this would violate the `validateAttributeUsageIsReferential` constraint" | S3, `2026-01` | primary | The constraint is enforceable but the in-memory API can construct violating models |
| control-node succession constraints (8) | validate | Pilot | `// TODO: Check validateControlNodeIncomingSuccessions (?)`, `// TODO: Check validateControlNodeOutgoingSuccessions (?)`, `// TODO: Check validateDecisionNodeIncomingSuccessions (?)`, `// TODO: Check validateDecisionNodeOutgoingSuccessions (?)`, `// TODO: Check validateForkNodeIncomingSuccessions (?)`, `// TODO: Check validateJoinNodeOutgoingSuccessions (?)`, `// TODO: Check validateMergeNodeIncomingSuccessions (?)`, `// TODO: Check validateMergeNodeOutgoingSucessions (?)` | S1 `:873–902` | primary | Eight named normative constraints are present as TODO comments in otherwise empty `@Check` methods |
| same 8 constraints | validate | Pilot | Each has a declared diagnostic code bound to its constraint name, e.g. `public static val INVALID_CONTROL_NODE_INCOMING_SUCCESSIONS = "validateControlNodeIncomingSuccessions"` … `INVALID_MERGE_NODE_OUTGOING_SUCCESSIONS = "validateMergeNodeOutgoingSuccessions"` | S1 `:283–304` | primary | The authors intended to implement them; the identifiers exist and are unused |
| same 8 constraints | validate | Pilot | None of the 8 code constants is referenced by **any** executable line in either validator; `checkDecisionNode`, `checkForkNode`, `checkJoinNode` and `checkMergeNode` have **no executable body at all**; `checkControlNode` checks only `validateControlNodeOwningType` | S1, S2 (own analysis of S1/S2) | primary | Independently confirms non-enforcement; corroborates S8's claim |
| same 8 constraints | validate | OpenSysML | "The pinned pilot implements only `validateControlNodeOwningType`; the other eight are `// TODO: Check validate… (?)` comments in the `@Check` methods of `SysMLValidator.xtend` (`:857–888` at `c7fc737`), so a model the specification rejects on any of them validates clean there." | S8, "Control-node successions the pilot does not validate" | **third-party** | An independent party reached the same conclusion from a **different commit**; the two agree on substance, differ on line numbers (§5.4) |
| `validateBindingConnectorArgumentTypeConformance` | validate | Pilot | `// Note: This check is not currently implemented.` | S2 `:262` | primary | Self-declared non-implementation, first-party |
| `validateBindingConnectorArgumentTypeConformance` | validate | Pilot | The only code reference is inside a commented-out block: `// if (outConformsToIn.filter[!empty].length != inTypes.length)` / `// error(INVALID_BINDING_CONNECTOR_ARGUMENT_TYPE_CONFORMANCE_MSG, …)` | S2 `:950–957` | primary | Confirms the note at `:262` — the implementation was written and then disabled |
| `validateAssociationStructureIntersection` | validate | Pilot | `// validateAssociationStructureIntersection is automatically satisfied` | S2 `:919` | primary | A deliberate non-check with a stated reason (believed unreachable) — a different class from "forgotten" |
| `validateRedefinitionMultiplicityConformance`, `validateSubsettingMultiplicityConformance` | validate | Pilot | `// TODO: Add validateRedefinitionMultiplicityConformance` and `// TODO: Add validateSubsettingMultiplicityConformance`, immediately above bound-comparison code that *does* emit `warning(...)` under those codes | S2 `:795`, `:806` | primary | **Partial** implementation: an approximation is enforced, at `warning` severity, and the authors record that the real constraint is not implemented |
| `validateBindingConnectorTypeConformance` | validate | Pilot | `// TODO: Add validateBindingConnectorTypeConformance` above code that emits `warning(INVALID_BINDING_CONNECTOR_TYPE_CONFORMANCE_MSG, …)` | S2 `:959–973` | primary | Enforced as a **warning**, with a TODO — severity differs from the metamodel's presumed error |
| `validateOperatorExpressionCastConformance` | validate | Pilot | `// TODO: Add validateOperatorExpressionCastConformance` above `warning(INVALID_OPERATOR_EXPRESSION_CAST_CONFORMANCE_MSG, …)` | S2 `:1250–1259` | primary | Enforced as a warning, with a TODO |
| `validateAttributeUsageEnumerationDefinition` | validate | Pilot | `// TODO: Add validateAttributeUsageEnumerationDefinition?` | S1 `:570` | primary | The pilot is unsure whether the constraint should exist; an adjacent enumeration-type check is implemented under its own code |
| `validateFlowEndSubsetting`, `validateFlowEndImplicitSubsetting` | validate | Pilot | `// TODO: Add validateFlowEndSubsetting? validateFlowEndImplicitSubsetting?` above code emitting an `error` for the first and a `warning` for the second | S2 `:1307–1314` | primary | Both partially implemented; the TODO marks uncertainty about the constraint's intent |
| `validateMultiplicityRangeBoundResultTypes` | validate | Pilot | `// TODO: Correct validateMultiplicityBoundResults OCL from KERML-199.` | S2 `:1337` | primary | The pilot asserts the **specification's OCL** is wrong; names OMG issue KERML-199 |
| `validateMetadataFeatureMetaclass` | validate | Pilot | `// TODO: Submit new issue to revise this to actually fix the problem KERML-90 was trying to address.` | S2 `:1358` | primary | The pilot implements a workaround for OMG issue KERML-90 and states the underlying problem is unfixed |
| `validateExposeOwningNamespace` | validate | Pilot | Comment `// validateExposeOwningNamespace` precedes `error(INVALID_VARIANT_MEMBERSHIP_OWNING_NAMESPACE_MSG, exp, null, INVALID_VARIANT_MEMBERSHIP_OWNING_NAMESPACE)` | S1 `:1267–1269` | primary | Enforced, but reported under a **different constraint's name** — a code-name-based search would record it as unimplemented |
| `validateOccurrenceUsageIsPortion`, `validateOccurrenceUsagePortionKind`, `validateOccurrenceUsageIndividualDefinition`, `validateSendActionUsagePayloadArgument`, `validateStateDefinitionParallelSubactions`, `validateStateUsageParallelSubactions` | validate | Pilot | Each branch calls `error(<…>_MSG, elem, feature, <…>_MSG)` — the **message constant** is passed where the constraint-code constant belongs | S1 `:636, :646, :651, :929, :1038, :1041` | primary | Enforced, but the emitted diagnostic code is a message string, so constraint identity is lost in the diagnostic stream |
| `validateOccurrenceUsagePortionKind` | validate | Pilot | `public static val INVALID_OCCURRENCE_USAGE_PORTION_KIND = "validateOccurrenceUsageIsPortion"` — the same payload as the preceding constant | S1 `:205`, `:207` | primary | The constraint has **no unique code string anywhere** in the validator |
| `validateFunctionResultExpressionMembership` | validate | Pilot | `checkFunction` reports the function-case violation under `INVALID_EXPRESSION_RESULT_EXPRESSION_MEMBERSHIP` (`"validateExpressionResultExpressionMembership"`), the Expression constraint's code | S2 `:1084–1100` | primary | The Function variant is enforced but attributed to the Expression constraint |
| `checkConstraintUsageCheckedConstraintSpecialization`, `checkRequirementUsageSubrequirementSpecialization`, `checkIncludeUseCaseSpecialization`, `checkRequirementUsageObjectiveRedefinition` | check | Pilot | Named as resolved issues in the `2026-07` notes (respectively `[SYSML21-4]`, `[SYSML21-300]`, `[SYSML21-299]`, `[SYSML21-309]`) | S3, `2026-07` | primary | Four normative **`check…`-named** constraints are cited by the release notes — but none of the four names, nor the fragments `Subrequirement` / `CheckedConstraint` / `IncludeUseCaseSpecialization` / `ObjectiveRedefinition`, occurs anywhere in S1 or S2 at 2026-11-13 |
| implementation-specific checks | check | Pilot | `// Note: validateClassifierDefaultSupertype is not in the spec, but it is implied by semantic constraints on classifiers.`; `// Note: validateFeatureHasType is not in the spec, but it is implied by semantic constraints on features.`; `// Note: This validation is not in the spec.` (→ `validateOperatorExpressionBracketOperator_`); `// Note: This validation is not formalized in the spec.` (→ `validateLibraryPackageNotStandard_`); `// Note: This check is not in the spec as a single constraint.` | S2 `:163`, `:173`, `:329`, `:384`, `:569` | primary | The pilot adds checks the specification does not contain, and says so; a spec-to-implementation diff is therefore not a subset relation in either direction |
| implicit construction / validation scope | — | Pilot | `// NOTE: Need to allow parameters and objectives because they are currently physically inserted by transform implementation.` / `// TODO: Add allowance of parameters and objectives in variations to spec? Or remove when possible?` | S1 `:528–529` | primary | The implementation's own transform inserts elements that then violate a constraint it enforces; it relaxes the check and proposes changing the **specification** |
| redundancy shortcuts | validate | Pilot | `// NOTE: Only check owned features, for efficiency and to avoid redundancy.` / `// (This should be sufficient, unless a composite feature is inherited from a KerML data type.)` | S1 `:560–561`, `:583–584` | primary | Two checks are knowingly incomplete in an inherited-feature corner the author flags |
| `validateNamespaceDistinguishability` | validate | Pilot | `// Do not check distinguishability for automatically constructed expressions and binding connectors (to improve performance).` and `// NOTE: Does not check distinguishibility for imported Memberships.` | S2 `:423`, `:426` | primary | Scope of a normative constraint is deliberately narrowed for performance; the imported-membership gap is flagged |
| `validateClassifierDefaultSupertype_`, `validateFeatureHasType_`, `validateLibraryPackageNotStandard_`, `validateOperatorExpressionBracketOperator_` | validate | Pilot | These are the only **four** names in either validator ending in `_`; all four carry an explicit "not in the spec" note (above); 29 further SysML names end in `_` with no note | S1, S2 | primary | A naming convention correlates with implementation-specific provenance in KerML; the SysML extension is **[INFERENCE]** |

---

## 2.1 Third-party disagreement taxonomy (OpenSysML)

Relevant because it is the only published scheme for classifying *where* two SysML v2 implementations disagree at constraint level. Verbatim from S8, "What is compared":

> "Each diagnostic is normalized to a tuple: `(file, line, severity, coarse category)`. Message wording will never match between two implementations, so **message text is never compared** … Categories are coarse and deliberately few:"

| Category | Meaning (verbatim) |
|---|---|
| `syntax` | "the file did not parse as written" |
| `unresolved-reference` | "a name did not resolve" |
| `kind-mismatch` | "a declaration used where its metaclass is not allowed" |
| `multiplicity` | "bounds, cardinality, subsetting caps" |
| `units` | "quantity/unit incompatibility" |
| `unmapped` | "**no rule claimed this message**" |

Its own caveat on `unmapped`: "a message that does not fit a category stays in its bucket and is also listed in a table of its own, rather than being mapped to something adjacent to make the report look tidy." This matters for interpreting the numbers: at the `spec-examples` root the pilot's largest bucket is 1359 `unmapped` diagnostics (S8 Results table), i.e. the majority of reported disagreement is not attributed to any rule by the third party's own scheme. **[INFERENCE]** A taxonomy of this kind classifies *diagnostics*, not *constraints*, so it cannot be used directly to enumerate which normative constraints differ — the constraint-level mapping in §2 and the CSV has to carry that.

Constraint-level disagreements the third party names explicitly, with its verdict (all **[THIRD-PARTY]**):

| Constraint / rule | Third party's statement | Where |
|---|---|---|
| 8 control-node succession constraints | "the other eight are `// TODO: Check validate… (?)` comments … so a model the specification rejects on any of them validates clean there" | S8 |
| specialization cycles (no constraint name — nothing in the spec) | "The pilot has no specialization-cycle check at `2026-05`: `KerMLValidator.checkSpecialization` implements only `validateSpecializationSpecificNotConjugated`" | S8 "Specialization cycles (F4)" |
| value-level uniqueness | "the pilot has no value-level uniqueness constraint, so all 5 [diagnostics] are one-sided by construction" | S8 Results |
| dimensional analysis | "the pinned pilot does no dimensional analysis" | S8 "The declared errata overlay" |
| `validateSubsettingUniquenessConformance` | the pilot "refuses to redefine either `nonunique` (`validateSubsettingUniquenessConformance`)" | S9 |
| invocation argument count | "KerML 1.0 §8.3.4.8.8 lists no `InvocationExpression` constraint on the count of arguments" — adjudicated as *the specification's* reading, not a pilot defect | S9 |

The last row is the clearest example of an implementation reporting a gap that it concludes is **specification silence rather than implementation error**.

---

## 3. Validator inventory summary

Deliverable: [`validator-inventory.csv`](validator-inventory.csv) — 116 rows, one per `@Check` method (114 active + 2 commented out). Every constraint name in it was machine-verified to appear verbatim in the hashed source file, and every method/line pair to match.

### 3.1 Counts

| Measure | SysML (S1) | KerML (S2) | Total |
|---|---:|---:|---:|
| File lines / bytes | 1,501 / 78,434 | 1,531 / 77,545 | — |
| `@Check` occurrences | 74 | 42 | 116 |
| **Active** `@Check` methods | **72** | **42** | **114** |
| Commented-out `@Check` methods | 2 | 0 | 2 |
| Active methods whose constraints are named in an in-code comment | 54 | 40 | 94 |
| Active methods whose constraints come only from the diagnostic code constant passed | 16 | 1 | 17 |
| Active methods that name no constraint (`none_named_in_source`) | 2 | 1 | 3 |
| Methods with **no executable body** | 5 | 0 | 5 |
| Distinct constraint names mapped to a check | 108 | 94 | **202** |

Method name vs constraint name, as requested:

- **Method name equal or near-equal to a `validate…` constraint**: 0. Every method is named `check…`. The constraint names appear in the method *body* (comments) or in the diagnostic code constants.
- **Method name matching a `check…`-named constraint**: 2 in KerML — `checkFeatureCrossingSpecialization` (`:187`) and `checkConstructorExpressionResultFeatureRedefinition` (`:297`) are the only two diagnostic payloads in either file that are `check…` rather than `validate…`.
- **Neither** (implementation-specific method naming): 22 rows have no constraint name in an in-code comment — 20 active methods (17 naming a diagnostic-code constant only, of which 16 are `_`-suffixed and one, `checkOperatorExpression` → `validateOperatorExpressionQuantity`, is not; 2 delegating to a helper; 1 empty) plus the 2 commented-out methods. Listed in §3.3.
- **`derive…` constraints: zero.** Neither validator contains a single `derive…`-named diagnostic or check (the only occurrence of the string "derive" in either file is inside the message `"End feature cannot be derived, abstract, composite or portion"`, KerML `:196`). Derivation constraints are not validator concerns in this implementation; they live in the adapter/logic layer.

Declared-but-unreferenced diagnostic codes (executable lines only, comments excluded from the test):

| | SysML | KerML |
|---|---:|---:|
| Constraint-named code constants | 123 | 101 |
| Never referenced by any executable line | **21** | **5** |
| …of which: no implementation at all | **14** | **3** |
| …of which: enforced but the `_MSG` constant is passed as the code | **6** | 0 |
| …of which: enforced but under another constraint's code | **1** | **1** |
| …of which: deliberate non-check ("automatically satisfied") | 0 | **1** |

The 17 with no implementation: `validateDefinitionVariationIsAbstract`, `validateItemUsageType_`, `validatePartUsageType_`, `validatePartUsagePartDefinition`, `validateAssignmentActionUsageArguments`, `validateUseCaseUsageReference`, and the 8 control-node succession constraints (all SysML: 14); `validateFeatureEndIsConstant`, `validateSubsettingPortionConformance`, `validateBindingConnectorArgumentTypeConformance` (KerML: 3).

### 3.2 Empty or TODO-only `@Check` methods — registered checks that enforce nothing

SysML (5; KerML has none):

| Line | Method | Body |
|---|---|---|
| `:623` | `checkOccurrenceDefinition` | **completely empty** — no logic, no comment |
| `:883` | `checkDecisionNode` | 2 TODO comments only |
| `:889` | `checkForkNode` | 1 TODO comment only |
| `:894` | `checkJoinNode` | 1 TODO comment only |
| `:899` | `checkMergeNode` | 2 TODO comments only |

`checkOccurrenceDefinition` is the notable one: it registers a validator for the metaclass and does nothing, with no comment saying why. Whether a normative constraint is thereby unenforced is **not established** from the file alone — it depends on the normative set, which is the main catalogue's business.

### 3.3 Implementation-specific checks (no `validate…`/`check…` mapping in source)

Methods named after the metaclass rather than a constraint, with their basis:

- **`delegates_to_helper`** (2): `checkConstraintUsage` (SysML `:1093`; its diagnostic payload is the message string `"Invalid Constraint Usage - invalid type"`, not a constraint name); `checkImplicitBindingConnectors` (KerML `:932`; delegates to `doCheckConnector` / `doCheckBindingConnector`).
- **`diagnostic_code_constant`** (17): constraint identity comes only from a diagnostic-code constant, 16 of them `_`-suffixed (e.g. `checkEnumerationUsage` → `validateEnumerationUsageType_`) and one not (`checkOperatorExpression` → `validateOperatorExpressionQuantity`). The mapping is real but the constraint is pilot-named.
- **`commented_out`** (2): `checkItemUsage` (`:657`), `checkPartUsage` (`:661`) — whole method bodies commented out.
- **`empty_body_no_logic`** (1): `checkOccurrenceDefinition` (`:623`).
- **`override_of_kerml_check`** (3): `checkDataType`, `checkClass`, `checkOperatorExpression` in SysML override the KerML methods; `checkOperatorExpression` additionally adds a SysML-only quantity check.

Naming-anomaly diagnostics, recorded because they defeat name-based matching:

| Constant | Payload | Where |
|---|---|---|
| `INVALID_CONSTRAINT_USAGE_TYPE` | `"Invalid Constraint Usage - invalid type"` | S1 `:374` |
| `INVALID_METADATA_FEATURE_BODY` | `"invalidateMetadataFeatureBody"` (typo for `validate…`) | S2 `:371` |
| `INVALID_OCCURRENCE_USAGE_PORTION_KIND` | `"validateOccurrenceUsageIsPortion"` (duplicate of the previous constraint's name) | S1 `:207` |
| `INVALID_TRIGGER_INVOCATION_EXPRESSION_*` | payloads say `…Action…` rather than the EMF feature name `…Expression…` | S1 `:276–280` |

### 3.4 TODO and gap evidence — complete list

Every `// TODO` comment found in either file — **18 in total: 10 in SysML (`:529`, `:570`, `:873`, `:874`, `:885`, `:886`, `:891`, `:896`, `:901`, `:902`) and 8 in KerML (`:795`, `:806`, `:959`, `:1023`, `:1250`, `:1307`, `:1337`, `:1358`)** — plus two KerML non-TODO gap notes (`:262`, `:919`). 20 rows:

| File:line | Text |
|---|---|
| S1 `:529` | `// TODO: Add allowance of parameters and objectives in variations to spec? Or remove when possible?` |
| S1 `:570` | `// TODO: Add validateAttributeUsageEnumerationDefinition?` |
| S1 `:873`, `:874` | `// TODO: Check validateControlNodeIncomingSuccessions (?)`, `// TODO: Check validateControlNodeOutgoingSuccessions (?)` |
| S1 `:885`, `:886` | `// TODO: Check validateDecisionNodeIncomingSuccessions (?)`, `// TODO: Check validateDecisionNodeOutgoingSuccessions (?)` |
| S1 `:891` | `// TODO: Check validateForkNodeIncomingSuccessions (?)` |
| S1 `:896` | `// TODO: Check validateJoinNodeOutgoingSuccessions (?)` |
| S1 `:901`, `:902` | `// TODO: Check validateMergeNodeIncomingSuccessions (?)`, `// TODO: Check validateMergeNodeOutgoingSucessions (?)` |
| S2 `:262` | `// Note: This check is not currently implemented.` (→ `validateBindingConnectorArgumentTypeConformance`) |
| S2 `:795` | `// TODO: Add validateRedefinitionMultiplicityConformance` |
| S2 `:806` | `// TODO: Add validateSubsettingMultiplicityConformance` |
| S2 `:919` | `// validateAssociationStructureIntersection is automatically satisfied` |
| S2 `:959` | `// TODO: Add validateBindingConnectorTypeConformance` |
| S2 `:1023` | `// TODO: Be able to remove these special cases` (→ `checkConnectorTypeFeaturing`) |
| S2 `:1250` | `// TODO: Add validateOperatorExpressionCastConformance` |
| S2 `:1307` | `// TODO: Add validateFlowEndSubsetting? validateFlowEndImplicitSubsetting?` |
| S2 `:1337` | `// TODO: Correct validateMultiplicityBoundResults OCL from KERML-199.` |
| S2 `:1358` | `// TODO: Submit new issue to revise this to actually fix the problem KERML-90 was trying to address.` |

Two OMG issue keys appear in the source: **KERML-199** and **KERML-90**. No `SYSML21-*` key appears in either validator.

---

## 4. Release-note chronology, `2026-01` → `2026-09.1`

All quotes verbatim from S3 (`published_at` given). Note: **there is no `2026-06` release** — the `2026-07` notes state "there was no 2026-06 release".

**`2026-01`** — published 2026-02-10. Plugin 0.56.0.
- "The following validation constraints were previously **not being checked**, since they were automatically satisfied due to getter overrides. Since these getter overrides have now been removed, checks have been implemented for all the constraints." (13 constraints listed: 7 KerML, 6 SysML — see §2.)
- "it is now the responsibility of the constructor of a model to ensure that the corresponding abstract syntax properties have values consistent with various validation constraints"
- "when an `AttributeUsage` is created, the default value for `isComposite` is `false`, but it is possible to use the `setIsComposite` method to set this to `true`, even though this would violate the `validateAttributeUsageIsReferential` constraint"

**`2026-02`** — 2026-03-07. Plugin 0.57.0. No constraint-level content. Removed the metamodel-altering `isNonunique` property: "This alteration of the metamodel has now been removed."

**`2026-03`** — 2026-04-08. Plugin 0.58.0.
- "the `checkConnectorTypeFeaturing` constraint is impossible to satisfy for the binding connectors implied by these feature references. The Pilot Implementation was not reporting this as an error, which was not conformant with the normative metamodel for KerML (and, so, SysML, too)."
- "Now that this nonconformity has been corrected, the above feature references will cause \"Must be accessible feature\" errors."
- "Removed code that suppressed violations of `checkConnectorTypeFeaturing` within feature references in filter expressions."
- Backward incompatibility: yes — models using qualified names in filter expressions now error.

**`2026-04`** — 2026-05-13. Plugin 0.59.0. No validation content (licence LGPL → EPL; `org.omg.sysml.model` split out).

**`2026-05`** — 2026-07-02. Plugin 0.60.1.
- "Updated/implemented a few constraints that were corrected or added for SysML 2.1 Beta 1"
- "Added a validation check that the referent of an assign action usage is time varying. Previously a non-time-varying feature was accepted." → backward incompatibility (matches `validateAssignmentActionUsageReferentIsTimeVarying`, present in S1 `:794–805`)
- "Revised the derivation of the properties `Definition::ownedMetadata` and `Usage::nestedMetadata` to work properly. Previously they were always empty (due to a specification error)." — a first-party assertion of a **specification** error
- Issue resolutions naming constraints: `validateAssignmentActionUsageReferent` (`SYSML21-15` "Error in constraint validateAssignmentActionUsageReferent"), `validateAssignmentActionUsage` (`SYSML21-17` "Error in constraint validateAssignmentActionUsage"), `checkConstraintUsageCheckedConstraintSpecialization` (`SYSML21-4` "Error in constraint checkConstraintUsageCheckedConstraintSpecialization"), `checkIncludeUseCaseSpecialization` (`SYSML21-299` "Constraint checkIncludeUseCaseSpecialization is misnamed"), `checkRequirementUsageObjectiveRedefinition` (`SYSML21-309`), plus `SYSML21-301` "Viewpoint specialization constraints are incorrect"
- "the metamodel URI is being kept the same as for 1.0/2.0 (version date `20250201`)"

**`2026-07`** — 2026-08-20. Plugin 0.61.0.
- "This release brings the implementation into conformance with the KerML 1.1 Beta 2 and SysML 2.1 Beta 2 metamodels."
- "Corrects textual notation BNF non-conformities between the implementation and the KerML and SysML specifications."
- Issue resolutions naming constraints: `SYSML21-300` "Constraint checkRequirementUsageSubrequirementSpecialization needs to exclude assumed requirements" ("Revised previous implementation from [PR #87]"), `KERML11-191` "Problem with deriveTypeFeatureMembership" (`[PR #749]`), `SYSML21-302` "Override namingFeature for a view", `SYSML21-318` "Diamond inheritance problem with TradeStudy", `SYSML21-368` "Abstract syntax changes from resolution of SYSML2_-159 were not made"
- No stated backward incompatibility.

**`2026-08`** — 2026-09-11. Plugin 0.62.0. No validation-semantics change. Technical: parse post-processing moved out of adapters because of "limitations in the KerML and SysML grammars, as specific to using the Xtext grammar language"; bug fixes incl. "Fixes a bug which caused the `KerMLValidator` to throw an exception when checking invalid cross-subsettings."

**`2026-09`** — 2026-10-22. Plugin 0.63.0.
- Default multiplicity change (quoted in §2), attributed to `SYSML21-185` ("Default multiplicities are not formally specified").
- "Adds validation checks that the end features of connection definitions and flow definitions are usages." (matches `checkConnectionDefinition` / `checkFlowDefinition` in S1 `:710–746`)
- "Fixes the derivation computation for the property `Type::multiplicity` and the implementation of th[e] constraint `validateTypeOwnedMultiplicity`."
- Backward incompatibility: yes, default multiplicity — "may result in multiplicity violations in the interpretation of some models".

**`2026-09.1`** — 2026-10-28. Plugin 0.63.1. "This release is the same as the [2026-09] release, except for one additional bug fix (to correct a bug introduced in the 2026-09 release)." Notes repeated; plus "Reference Linking. Fixes bugs related to the resolution of reference links that were hidden in previous releases but uncovered by changes made in the 2026-09 release."

**Chronology summary.** Three releases in this window changed what is *enforced* (2026-01: 13 constraints added; 2026-03: one suppression removed; 2026-09: one check family added), and two carried admitted backward incompatibilities caused by validation behaviour (2026-03, 2026-09). Two releases cite a **specification** defect as the reason for a change (2026-05 `ownedMetadata`; 2026-09/`SYSML21-185`).

---

## 5. Established / contested / not established, and access log

### 5.1 Established (retrieved evidence, primary unless marked)

1. The pilot's constraint checks are 114 active `@Check` methods in two Xtend files (72 SysML, 42 KerML), mapping to **202 distinct constraint names** as the implementation spells them. No `derive…` constraint appears in either file.
2. **17 constraints have a declared diagnostic code and no implementation**, listed in §3.1. Eight of them (control-node successions) are TODO comments in empty methods; `validateBindingConnectorArgumentTypeConformance` has its logic commented out beside a `// Note: This check is not currently implemented.`
3. **5 `@Check` methods in SysML enforce nothing** (§3.2), one of them completely empty with no explanatory comment.
4. **7 constraints are enforced but attributed to the wrong diagnostic code** — 6 pass a `_MSG` constant, 1 (`validateExposeOwningNamespace`) passes another constraint's code entirely.
5. **1 constraint is deliberately not checked as "automatically satisfied"** (`validateAssociationStructureIntersection`), and 2 more have knowingly narrowed scope for performance/duplication reasons (§3.3, S1 `:560–561`, S2 `:423–426`).
6. The pilot implements checks **not in the specification** and says so — 4 in KerML, all `_`-suffixed (§2). A spec↔implementation diff is not a subset relation in either direction.
7. The pilot's own source names **two OMG issues** (KERML-199, KERML-90) as defects in the specification or in the resolution of it.
8. SYSML21-185 **is publicly readable** (S4) and states that the specification has no normative formalisation of default multiplicity; status open; reported 2024-06-15, updated 2025-06-20.
9. Thirteen named constraints were "not being checked" before `2026-01` (13 names enumerated), and one suppression was removed in `2026-03` after being called "not conformant with the normative metamodel".
10. Three OpenSysML claims I could test against source code are **independently confirmed** by S1/S2: (a) that eight control-node succession constraints are TODO comments in otherwise empty `@Check` methods; (b) that "`SysMLValidator.xtend` declares an error code for each" — I verified all eight code constants exist and bound to the constraint names; (c) that `checkSpecialization` "implements exactly one constraint, `validateSpecializationSpecificNotConjugated`" — confirmed, and no cycle check exists anywhere in either file.

### 5.2 Contested / conflicting

1. **Line numbers for the control-node TODOs.** S8 cites `SysMLValidator.xtend:857–888` at commit `c7fc737`; my S1 (`master`, 2026-11-13) has them at `:872–902`. Substance agrees, positions differ by ~15 lines. This is version drift between the commit S8 analysed and `master`, not a disagreement about fact. **Do not mix line numbers from the two.**
2. **Whether the SysML `_` suffix means "not in the spec".** In KerML the convention is directly evidenced (all 4 `_` names carry a "not in the spec" note). For the 29 SysML `_` names there is no such comment, so the generalisation is **[INFERENCE]**, not established.
3. **Pilot severity vs normative severity.** At least 4 constraints are emitted as `warning` (`validateBindingConnectorTypeConformance`, `validateOperatorExpressionCastConformance`, `validateRedefinitionMultiplicityConformance`, `validateSubsettingMultiplicityConformance`). I have **not** established what severity the normative text requires — that needs the clause-8 OCL, which is outside my scope.
4. **Whether the 14 SysML + 3 KerML no-implementation constraints are real permissiveness.** A code constant with no logic strongly indicates no check, but a supertype `@Check` could in principle cover the same condition under a different diagnostic code. Not established without probing the built validator.
5. **The 4 `check…`-named normative constraints absent from the validator** (§2). The `2026-07` notes describe them as resolved issues "already implemented previously" (`SYSML21-4`, `-299`, `-309`) or revised (`SYSML21-300`), yet no such name or name-fragment occurs in either validator file at 2026-11-13. Either they were implemented under different names, or they are no longer implemented. **Contested, not resolved.**
6. **OpenSysML's self-reported defect count.** S7 says the registry declares "13 defect(s) in the published reference material — 6 with a specification-derived correction, 7 documented without one". I verified the arithmetic against S10/S11: 3 corpus entries (`F82`, `F83`, `F84`) plus 10 library entries (`SI-137`, `SI-149`, `SI-163`, `SI-233`, `SI-239`, `SI-247`, `SI-286`, `SI-299`, `SI-303`, `USCustomaryUnits-255`) = **13**, of which 6 carry a non-empty `Corrected` field (`F82`, `SI-137`, `SI-233`, `SI-247`, `SI-303`, `USCustomaryUnits-255`) and 7 do not. The count is **confirmed**. But the framing needs care: these are defects in the **OMG example corpora and the vendored standard library**, not in the specification document. `evidence/spec-tooling.md` §4.5 characterises the claim as "about the OMG corpus/spec"; the registry is precise, and it is corpora + library.
7. **OpenSysML's internal count inconsistency** flagged in the grounding note is repeated in S7/S8 as retrieved: S7 says the differential gives "524 of 924 files agree"; S8's Results table also gives 524/924 total with `Only pilot 2462` and `Only ours 122`, while a separate paragraph in S7 says "0 the pinned pilot rejects and we accept". At `spec-examples` the pilot's single largest bucket is 1359 `unmapped` — messages no rule claimed — so most of the "disagreement" is unclassified by the third party's own taxonomy. Treat all its counts as self-reported indicators.

### 5.3 Not established

1. **What severity the normative metamodel requires** for the constraints the pilot emits as warnings (clause-8 OCL not read).
2. **The size of the normative constraint set**, and therefore the true denominator: how many normative constraints have *no* corresponding check at all. My 202 figure is what the implementation names, not what the specification requires. This is the main catalogue's job; §3.1's 17-code list is the handover set for that cross-check.
3. Whether the Syside divergences (S6) reproduce. Its examples are concrete and checkable but I did not build or run any validator.
4. Behaviour of the *built* validator. Everything here is source-level or documentary. No JAR was built or run; OpenSysML's behavioural probes (S8) are the only runtime evidence, and they are third-party.

### 5.4 Access log — failures and recovery

| Resource | Failure | Class | Recovery attempted | Outcome |
|---|---|---|---|---|
| `https://issues.omg.org/browse/SYSML21-185` | HTTP 302 → `login.jsp?permissionViolation=true&os_destination=%2Fbrowse%2FSYSML21-185` | **access-restricted** (authentication boundary) | Tried the tracker's alternate public route `https://issues.omg.org/issues/SYSML21-185`, which the pilot's own release notes use as the canonical link | **Recovered**: HTTP 200, full record read anonymously. The `browse` route was **not** bypassed |
| `tools/oracle/errata` (as a raw file) | HTTP 404, 14-byte body | moved / not-a-file | Listed the containing directory via the GitHub contents API, which showed `tools/oracle/errata/` is a directory | **Recovered**: fetched `errata/errata.go` (S10) and `internal/workspace/libs/errata/errata.go` (S11) |
| GitHub releases HTML page | Not attempted | — | Used the public releases API (S3) instead of scraping the rendered page, because the API returns the release bodies verbatim and unambiguously attributable | **Preferred route**, not a recovery |
| `2026-06` release tag | Absent from the 90-release list | **never published** | Read the `2026-07` body, which states "there was no 2026-06 release" | Confirmed never published, not a retrieval failure |

No source in this note required bypassing a login, paywall, CAPTCHA or Cloudflare control, and none was attempted. `robots.txt` was not consulted for any of these URLs and no retrieval here relied on the robots.txt exception — all sources retrieved are either raw-file endpoints, a public JSON API, or public documentation pages. The INCOSE PDF access failure recorded in `evidence/spec-tooling.md` §6.5 was **not** revisited, per instruction.

### 5.5 What would change the answer

- **Building the validator and probing** the 17 no-implementation constraints with minimal violating models. That would convert "no code path" into "observed permissiveness" and would settle §5.2 item 4.
- **Retrieving clause 8.3's OCL** for SysML 2.0 (or the 2.1 Beta 2 metamodel the pilot targets) to fix severities and to compute the true gap denominator (§5.3 item 2).
- **Inspecting the commit S8 pinned** (`c7fc737`) to reconcile line numbers and confirm whether the control-node TODOs predate the pinned release, as S9 asserts for `2026-07`.
- **Decompiling the shipped `SysMLValidator.class` / `KerMLValidator.class`** from a release JAR to test whether the source on `master` corresponds to the released 0.63.1 validator. I did not do this, so **every claim here is about `master` at 2026-11-13, not about the 2026-09.1 release artefact.**

---

## 6. Sources cited

S1–S12 in §1. Prior note consulted for orientation only: [`evidence/spec-tooling.md`](../evidence/spec-tooling.md). Companion deliverable: [`validator-inventory.csv`](validator-inventory.csv).
