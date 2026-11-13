# Specification-silence and discretion register

**What this is.** The register records ten areas in which the normative
specification does not supply a well-formedness rule a checker can enforce. For
each area it records what the specification does say, what is missing or left
open, the implementation choices observed, and what that costs a checker. It
does not adjudicate whether the gap is a defect; it records it as the finding.

**Not every entry is "silence" in the strict sense.** The `Kind` field
distinguishes:
- **absent** — no normative rule at all; genuine class D (D1–D4);
- **explicit discretion** — the specification permits the tool to choose (D5);
- **explicit delegation** — the specification says another practice or the
  adopter supplies the rule (D8);
- **ambiguous / partial** — a rule exists but does not determine the answer (D6);
- **outside the well-formedness surface** — semantics are defined, but no
  well-formedness constraint enforces them (D7);
- **no oracle** (D9) and **provenance gap** (D10) — institutional/artefact gaps,
  not missing language rules.

Only the four `absent` entries are class D in the strict sense. The others are
recorded because they have the same practical effect on what a validator can
establish, but they should not be counted as "the specification says nothing".

**Pinned sources.** SysML 2.0 `formal/2026-03-02`; KerML 1.0 `formal/2026-03-01`;
both MOF XMI files as in `README.md`. Implementation evidence is the same as
`deep-trace.md`; every claim names its source.

**Scope note.** Strict silence means *no named constraint and no OCL in the
normative metamodel*; the four `absent` entries meet that test. All ten entries
are distinct from (a) a constraint that is named but defective
(`ocl-defects.csv`), (b) a condition stated only in Clause 7/8.4 prose
(`prose-only-names.csv`), and (c) a constraint that is specified but whose
reporting is discretionary (dependency class B). Those are counted separately
and must not be added to this register.

---

## D1. Default multiplicities

**Kind:** absent.

**Silence.** The specification describes default `1..1` multiplicity in the
*non-normative* Language Description (§7.6.3 and the attribute/item/port
clauses), but the normative Clause 8 metamodel contains no constraint that
derives it. This is recorded by the constraint's author in OMG issue
**SYSML21-185**: "In the SysML Specification, in non-normative Language
Description subclause 7.6.3 Usages, it describes several conditions that, if
met, require a usage to have default multiplicity 1..1. However, there is no
formal specification of this in the normative Clause 8 Metamodel." Status
**open**; reported 2024-06-15, last updated 2025-06-20.

**Implementation choice.** The pilot applied a default, then changed it in
2026-09: "Previously, default multiplicities were not applied if a usage had
explicit owned subsettings… This has now been changed so that a usage with an
explicit, non-redefinition owned subsetting *does* get the SysML `1..1` default
multiplicity." The release lists this as a **Backward Incompatibility** that
"may result in multiplicity violations in the interpretation of some models",
and says the situation "is expected to be handled as part of the resolution to
SYSML21-185".

**Consequence.** A model can be valid under one pilot release and invalid under
the next, with no change to the model or to the normative text. A multiplicity
violation reported by any tool is therefore not attributable to the model alone:
it depends on a default the specification does not fix.

**Catalogue effect.** Zero constraints; the register entry is the finding.
Related but different: `validateMultiplicityRangeBounds`,
`validateFeatureEndMultiplicity`, `validateTypeOwnedMultiplicity` constrain
explicit multiplicities, not defaults.

---

## D2. General type conformance and type inference

**Kind:** absent.

**Silence.** The catalogue contains **six** type-related *conformance*
constraints, all local: `validateFeatureChainingFeatureConformance`,
`validateFeatureChainExpressionConformance`,
`validateRedefinitionDirectionConformance`,
`validateRedefinitionEndConformance`,
`validateSubsettingConstantConformance`,
`validateSubsettingUniquenessConformance`. It contains **no** general rule that
the type of an assigned value conforms to the declared type of the feature, and
no rule for inferring a feature's type from an expression.

Syside states the absence directly: "the specification itself completely omits
type checking and type inference which are, in our opinion, crucial for
determining model correctness and name resolution." Its worked example:
`attribute num : ScalarValues::Positive = 5.0;` — "This is fine according to the
Pilot Implementation. The example above gives a type error in Syside because
assigning a rational to a positive is not guaranteed to satisfy type
constraints."

**Implementation choice.** The pilot performs a symmetric bound-type comparison
(Syside: "tries to perform type checking by looking at bound feature types
symmetrically"), which cannot enforce the asymmetry of assignment. Syside
implements full type checking and inference. OpenSysML's tiered passes include
"types" as a validation tier.

**Consequence.** The single most important correctness property for generated
models — that a value is of the right type — is outside the normative
well-formedness surface. Any claim that a model "validates" is silent on it.

**Catalogue effect.** Class-D entry. The six local conformance constraints are
class A but do not compose into a type system.

---

## D3. Units, quantities and dimensional consistency

**Kind:** absent.

**Silence.** Zero named constraints contain `Unit`, `Quantity` or `Dimension`;
zero OCL bodies mention dimensional consistency (the one hit for "quantity" is
`validateTriggerInvocationExpressionAfterArgument`, a trigger-argument type
check). The Systems Model Library §9.8 defines quantity dimensions and units,
but the metamodel imposes no well-formedness rule that an expression's
dimensions are consistent.

**Implementation choice.** Syside: "At the moment, Syside cannot infer the
dimensions from expressions so every unit and quantity result type is up-casted
to respective tensor types from the standard library. As a result, Syside cannot
currently catch such errors as assigning length quantity to a mass quantity nor
evaluate such expressions." The pilot evaluates expressions but does not expose
a dimensional check.

**Consequence.** Assigning a length to a mass is a class-A engineering error that
no conformant tool is required to reject. A generated model can be perfectly
well formed and dimensionally nonsensical.

---

## D4. Severity and diagnostic identity

**Kind:** absent (under-specified).

**Silence.** §8.3.1 says a tool "should report violations of validation
constraints", and the compliance clause says an Abstract-Syntax-Conformant tool
"must also provide a way to validate the well-formedness of models that
corresponds to the constraints defined in the SysML metamodel". Neither states a
severity, a diagnostic code, a message, a location, or a machine-readable
identity for a violation. The only severity language in the specification is
local library guidance ("should raise a warning or error", §9.8.2) and is not a
constraint-level rule.

**Implementation choice.** The pilot emits at least four constraints as
`warning` where an error is the natural reading
(`validateBindingConnectorTypeConformance`,
`validateOperatorExpressionCastConformance`,
`validateRedefinitionMultiplicityConformance`,
`validateSubsettingMultiplicityConformance`), and it loses constraint identity in
at least seven places: six pass a `_MSG` constant where the diagnostic code
belongs, and `validateExposeOwningNamespace` reports under
`validateVariationMembershipOwningNamespace`. One constraint
(`validateOccurrenceUsagePortionKind`) has no unique code string at all.

**Consequence.** A validation report is not a set of constraint identifiers. Two
tools can agree on the verdict and disagree on the code, severity and location;
a machine reader cannot reliably map a diagnostic back to a catalogue row. This
is a measurable limit on "validator acceptance" as an outcome variable.

---

## D5. Whether implied relationships are materialised

**Kind:** explicit discretion.

**Not silence, but an explicit degree of freedom.** KerML §8.4.2: "a tool may
insert certain implied Relationships into the model in order to meet the
semantic constraints"; the tables "define what implied Relationships **should**
be included to satisfy each semantic constraint when it would otherwise be
violated." §8.3.1 adds that a tool "may satisfy the constraints by introducing
implied relationships into the model, it may simply report their violation, or
it may ignore the violations."

**Implementation choice.** The pilot does not construct implicit binding
connectors (Syside); OpenSysML implements implied relationships selectively.
Syside says its own type checking is disabled in places where the pilot would
construct implicit binding connectors.

**Consequence.** The abstract-syntax instance graph a validator sees is not
determined by the specification. Class-B constraints (§CATALOGUE `class = B`)
can be true, false or undecided depending on this choice, and the specification
licenses all three.

---

## D6. Name and membership resolution in ambiguous cases

**Kind:** ambiguous / partial.

**Silence (partial).** `validateNamespaceDistinguishibility` exists in KerML, so
distinctness is not wholly absent. But Syside records a case the constraint does
not settle: "Named members in the root namespace are checked to be unique in the
global namespace… The specification does not determine which membership is
chosen in such cases, (see note in clause 8.2.3.5.4 Full Resolution of Kernel
Modeling Language, Release 2024-12). This may lead to silent breakages even in
the same tool, e.g. if the order of documents changes between tool invocations."

**Implementation choice.** Syside emits a warning for duplicate root-namespace
names, "to match namespace distinguishability rule"; the pilot's resolution
order is an implementation detail.

**Consequence.** The meaning of an unqualified name can be implementation- and
document-order-dependent, and no well-formedness constraint forbids the model
that triggers it.

---

## D7. Execution and behavioural semantics

**Kind:** outside the well-formedness surface.

**Silence in the well-formedness surface.** The specification gives a
mathematical semantics for behaviour (§8.4) and the Systems Model Library
defines actions and states, but there is no constraint that a model's behaviour
is executable, deterministic, deadlock-free, or that a state machine has a
reachable initial state. The pilot "evaluates expressions but executes neither
actions nor state machines" (evidence note, corroborated by the architecture of
its `execution` layer); OpenSysML notes "no external referee executes behavior"
and self-assesses its own action/state-machine coverage.

**Consequence.** For a project whose dependent variable is "correct model", the
behavioural half of correctness has no normative checker at all. Validation can
establish structure and typing (where specified), not that the system does what
the model says.

---

## D8. Method-level and organisational constraints

**Kind:** explicit delegation.

**Silence by design.** SysML §1 Scope: "The language is intended to support
multiple systems engineering methods and practices. The specific methods and
practices may impose additional constraints on how the language is used." The
standard does not name a method, a review process, a naming convention, a
decomposition rule, or an adequacy criterion.

**Implementation choice.** OpenSysML ships non-normative extension libraries
(`OOSEM.sysml`, `MOSA.sysml`, `SysMLValidation.sysml`, …) explicitly described
as "**non-normative** OpenSysML extensions". Industrial practice evidence says
experts "cannot use existing standards and norms, because these are too
general".

**Consequence.** This is where the industrial "correctness" requirements live,
and the language deliberately does not speak to them. Any automated validation
ceiling is a property of the language, not only of the tools — the third rival
reading in the brief.

---

## D9. A conformance oracle

**Kind:** no oracle (institutional).

**Silence.** The compliance clause makes conformance claims conditional on
testing suites "in the event that testing suites are implemented or approved by
Object Management Group". No such suite exists in any artefact read. OpenSysML:
"the OMG corpora are demonstrations rather than an official conformance suite";
"no conformance certification is claimed"; "none of these is a percentage of the
specification — no global compliance figure is claimed anywhere."

**Consequence.** There is no normative answer to "how many constraints does this
tool implement?" other than the one this catalogue constructs. That is the
methodological justification for the catalogue, and also its main limit: the
denominator is our extraction from the pinned artefacts, not an OMG-published
list.

---

## D10. Version identity of the semantics

**Kind:** provenance gap.

**Silence in the artefacts.** The SysML metamodel URI is frozen at version date
`20250201` across 2.0 and the 2.1 Beta line (pilot release 2026-05: "To promote
compatibility, the metamodel URI is being kept the same as for 1.0/2.0 (version
date 20250201)"). The abstract syntax of the 2.1 Beta model is "structurally the
same" as 2.0, but the constraints can differ, and there is no published 2.1
document.

**Consequence.** A serialised model does not state which constraint set it was
written against, and the pilot that validates it targets a revision the public
cannot read. A version-pinned catalogue is therefore necessary but not
sufficient: the *validator's* target revision must be pinned separately, and for
the pilot it cannot be, publicly.

---

## Summary table

| # | Area | Kind | Normative text | Count in catalogue | Observed implementation divergence |
|---|---|---|---|---:|---|
| D1 | Default multiplicities | absent | §7.6.3 only (non-normative); SYSML21-185 open | 0 | pilot default changed 2026-09; backward incompatibility |
| D2 | General type conformance / inference | absent | none | 0 general (6 local) | pilot symmetric comparison; Syside full checking; `Positive = 5.0` accepted by pilot |
| D3 | Unit / quantity dimensions | absent | library §9.8 only | 0 | Syside cannot infer dimensions; pilot has no dimensional check |
| D4 | Severity / diagnostic identity | absent (under-specified) | "should report violations" only | 0 | pilot warnings; 7 constraints lose their identity |
| D5 | Implied-relationship materialisation | explicit discretion | explicit MAY in §8.3.1 / §8.4.2 | — | pilot omits implicit binding connectors; Syside/OpenSysML differ |
| D6 | Ambiguous membership resolution | ambiguous / partial | partial (`validateNamespaceDistinguishibility`) | 1 | Syside warns on duplicates; selection order unspecified |
| D7 | Execution / behaviour | outside well-formedness | semantics §8.4, no constraint | 0 | pilot executes no actions/state machines |
| D8 | Method / adequacy | explicit delegation | explicitly deferred (§1) | 0 | non-normative extension libraries |
| D9 | Conformance oracle | no oracle | conditional on absent testing suites | — | no official suite; third-party self-assessments |
| D10 | Version identity | provenance gap | metamodel URI frozen | — | pilot targets unpublished 2.1 Beta 2 |

**What would change this register.** A published SysML 2.1 / KerML 1.1 normative
document with the constraint set the pilot now targets; an OMG conformance suite;
or a normative statement of default multiplicity (SYSML21-185 resolved). None
was available at the retrieval date.
