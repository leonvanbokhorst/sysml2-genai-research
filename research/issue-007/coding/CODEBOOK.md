# CODEBOOK — error classes in GenAI-generated SysML v2 models (issue #7 pilot)

**Version 1.0 — FROZEN at 2026-11-13T14:12Z (sha256 quoted in the report and in
`../README.md`).** Built bottom-up from the 18-model pilot corpus
(`../corpus/normalized/*.sysml`); not derived from a validator, from the specification's
constraint list, or from Researcher B's work.

**Coding unit.** One *error record* = one defect mechanism in one model. A model may carry several
records; each record carries exactly one class. Where the same mechanism recurs within a model
(e.g. the same unresolvable identifier used five times, or four badly written transitions), the
record is **counted once** and the occurrence count and lines are recorded in `notes` /
`line_range`. This convention is fixed here so that counts measure *distinct defects*, not text
repetition.

**Denominator.** The error population is counted over the **18 normalised models**. The wrapper
class `W1` is a property of the **18 raw outputs** and is counted separately (see §6), so that
packaging defects and modelling defects are never summed into one misleading total.

**How the classes were produced.** Open pass over all 18 normalised models writing free-text
observations (no categories); the observations were then clustered into mechanisms; every cluster
had to account for at least one observed span, and every observed span had to go into exactly one
cluster or into the explicit exclusion list in §5. Nothing in this file was chosen to match a
validator diagnostic — the validator had not been run on these files when this version was
written.

---

## 1. Classes

| ID | Class | Layer | Default severity | Named constraint (catalogue) |
|---|---|---|---|---|
| **W1** | Wrapper/formatting defect (raw output is not a SysML file) | wrapper/formatting | blocking (for a raw-text consumer) | — (textual-notation grammar, clause 8.2.2) |
| **S1** | Construct written in a non-conforming textual form | syntax/parse | blocking | notation productions: `SatisfyRequirementUsage` (8.2.2.21.2); states/transition notation (8.2.2.18); reserved-keyword list (8.2.2.1.2). *Superseded 2026-11-13T15:06Z (A-12): the pre-correction row cited `checkSatisfyRequirementUsageBindingConnector` (a MAY `check`) and `TransitionUsage` at 8.3.18.9 (abstract syntax); C08/C09 corrected the records, this row lagged.* |
| **S2** | Required semantic binding absent where the notation's clause is optional (satisfy with no satisfying feature) | constraint/OCL | minor | `checkSatisfyRequirementUsageBindingConnector` (8.3.21.10) |
| **N1** | Reference to a model element that is not declared or not in scope | name resolution | blocking | no single named OCL constraint — name resolution is a precondition of every constraint (7.5, 8.3.2.4) |
| **N2** | Standard-library prelude omitted, so scalar type names do not resolve | name resolution | blocking | — (normative model libraries; no constraint names the import) |
| **T1** | Kind mismatch: a *definition* referenced where a *usage* is required | type/typing | major | — (no constraint by name; usage/definition distinction is structural in KerML §8.3.3/8.3.6) |
| **T2** | Typing mismatch: an attribute (value) usage typed by a non-value definition | type/typing | major | `checkAttributeUsageSpecialization` (8.3.7.3) |
| **R1** | A connection end whose feature chain traverses a multi-valued usage, so the end does not denote a single feature of the connector's domain | type/typing | major | no decisive constraint; nearest named rule `validateFeatureEndMultiplicity` (8.3.3.3.4). **Defect status CONTESTED** (C14/C15; adjudication RA-03/X-03). *Superseded 2026-11-13T15:06Z (A-12): the pre-correction row placed R1 at structural/architectural and treated the constraint basis as merely adjacent.* |
| **I1** | Model contradicts its own declared content (documentation/decimal values) | semantic/behavioural | minor | — (documentation is derived, `deriveElementDocumentation` 8.3.2.1.2; no constraint relates documentation to values) |

### W1 — Wrapper/formatting defect

**Definition (include):** the raw model output, as emitted, is not a SysML v2 text file: it is
markdown (a fenced code block), or it contains preamble/trailing prose, or both. Coding unit is
the raw output, not the normalised model.
**Exclude:** a fenced block whose *content* is defective (that is an S/N/T/R/I defect on the
normalised model); a model with no fence at all (absence of a wrapper is not a wrapper defect —
record `wrapper_status = no_fence`).
**Why it is an error at all:** a consumer that feeds model output straight to a parser or an
import gate (the design of the anchor's validation engine, and of any pipeline that does not
extract code first) receives a file that is not SysML. It is *not* evidence that the modelling is
wrong, which is exactly why it is kept separate.
**Worked example:** `../raw/T1-C1.md` — preamble sentence, then a ```` ```sysml ```` fence, then
trailing prose after the closing fence. Normalised body: `../corpus/normalized/T1-C1.sysml`.

### S1 — Non-conforming textual form

**Definition (include):** a construct is written in a form that is not the SysML v2 textual
notation, even though the author's intent is recognisable — a construct borrowed from SysML
v1/UML, a wrong keyword, or a reserved word used as an identifier in a declaration position.
**Exclude:** a construct that is syntactically well-formed but wrong in meaning (that is I1 or
R1); a missing mandatory clause (S2); a construct whose *names* do not resolve but whose form is
conforming (N1).
**Rule of precedence:** if the span cannot be parsed at all, code S1/S2 and do **not** also code
the names inside that span as N1 — an unparsed span is not a resolution failure.
**Worked examples**
- `../corpus/normalized/T1-C2.sysml:41` — `satisfy greenhouse to moistureControl;` — `to` is not
  part of the satisfy notation, and the operands are reversed (requirement first, satisfying
  feature after `by`).
- `../corpus/normalized/T2-C1.sysml:48-51` — `transition from idle to lowering on
  detection.approaching;` — `from … to … on …` is SysML v1/UML activity/state-machine notation.
  Four transitions share the mechanism → one record, 4 occurrences.
- `../corpus/normalized/T3-C2.sysml:23,33` — `port in;` / `… to line.in;` — `in` is a reserved
  direction keyword; using it as a declared feature name is not accepted as a name in this
  position.

### S2 — Required semantic binding absent (was: "Mandatory clause omitted"; corrected 2026-11-13T15:06Z, A-12)

**Superseded body.** The text below asserted that a mandatory clause was omitted. The `by` clause is
optional in the notation (8.2.2.21.2), so the obligation is the discretionary `check…` constraint,
not the grammar; the class table above is authoritative and the text below is retained for the
record.

**Definition (include):** the construct is named correctly but a clause the notation requires is
absent, so the construct cannot mean anything as written. The only corpus instance is a `satisfy`
usage with no satisfying feature (`by` clause), which therefore has no subject binding.
**Exclude:** a construct that leaves an *optional* part out (e.g. an untyped port, an action
usage with no body); a construct that is complete but resolves to nothing (N1).
**Worked example:** `../corpus/normalized/T2-C2.sysml:33` — `satisfy lowerBeforeArrival;` —
nothing is satisfied *by* anything. The requirement usage exists, but the satisfying feature that
`checkSatisfyRequirementUsageBindingConnector` requires is missing.

### N1 — Unresolved model-local reference

**Definition (include):** an identifier used in a construct (satisfy `by`, succession source, flow
or connection end, expression) names something that is declared nowhere visible in the model at
that point. Two observed sub-mechanisms, coded the same way because the failure mode is identical:
(a) a dangling reference to a name that was intended but never declared; (b) a reference to a
*requirement definition's subject parameter* from outside that definition — the parameter is a
feature of the definition, not of the package, so it is not in scope where the `satisfy` sits.
**Exclude:** unresolved *standard-library* type names where no import exists (N2 — different
mechanism: the model is internally consistent, the prelude is missing); a name that resolves to a
definition where a usage is required (T1); a name inside a span that does not parse (S1).
**Worked examples**
- `../corpus/normalized/T1-C1.sysml:64` — `first start;` — no action usage `start` is declared;
  the succession's source is a dangling name (the model declares `sense`, `compare`,
  `openValve`, `runPump`, `closeValve`).
- `../corpus/normalized/T3-C2.sysml:37,44` — `subject pump : InfusionPump;` is declared inside
  `requirement def AlarmTiming`, and the package-level `satisfy alarmTiming by pump;` references
  it from outside. No part usage `pump` exists in the package. Same mechanism in
  `T4-C2:32`, `T5-C2:32`, `T6-C2:40`.

### N2 — Missing standard-library prelude

**Definition (include):** the model uses SysML/KerML standard-library names — in this corpus, the
scalar types `Real`, `Boolean`, `Integer`, `String` — without importing the library package that
declares them (`ScalarValues`), and without qualifying them.
**Exclude:** a model that imports `ScalarValues::*` (then a bare `Real` resolves); a single
misspelled model-local name (N1); an unresolved name inside a non-parsing span (S1).
**Why a separate class:** the mechanism and the fix are different from N1 — nothing is dangling;
the model is complete in its own terms but is not self-contained with respect to the normative
libraries. Folding it into N1 would make "the model forgot one import line" indistinguishable
from "the model refers to something it never defines", and the two have different implications for
a generation pipeline.
**Known confound (recorded in advance):** a validator that does not load the standard library
reports the same unresolved-reference diagnostic for both classes. The detection table therefore
separates "prelude absent" from other unresolved references per model.
**Worked example:** `../corpus/normalized/T3-C1.sysml` — no import at all; `Real` at lines 4, 9,
10, 19, 32 and `Boolean` at lines 5, 14, 15, 20 are all unresolved (6 + 4 occurrences → one
record).

### T1 — Kind mismatch (definition where usage required)

**Definition (include):** a construct that requires a *usage* is given a *definition*. The corpus
instance is an action succession: `first checkCharge;` / `then assign;` inside an action
definition, where `checkCharge` and `assign` are declared at package level as `action def`.
A definition is a type, not an occurrence, so it cannot be the source/target of a succession.
**Exclude:** `entry action lowerArms;` where a same-named `action def` exists — the notation
declares a *usage* with that name, so no mismatch is established (see §5, exclusion 6); a
correctly typed usage that resolves to nothing (N1).
**Worked example:** `../corpus/normalized/T4-C1.sysml:42-44` with declarations at `:47-49` —
`first checkCharge; then checkAvailability; then assign;` against `action def checkCharge;`
etc. Three occurrences, one record.

### R1 — Connector ends that are not individual features (status: CONTESTED as to defect status)

**Contested status, added 2026-11-13T15:06Z (A-6, adjudication RA-03/X-03).** The *layer* was already
contested between `type/typing` (recorded) and `structural/architectural` (rival). The adjudicator
went further: the *defect status itself* is contested, because the criterion conflates a feature with
its instances and no constraint decides the case. Operational criterion, restated to expose where the
contested step is:

> A connection end is defective iff, after resolving its feature chain, the end does not denote a
> single feature of the connector's domain. **Contested step:** whether a chain through a usage whose
> multiplicity admits more than one instance violates that requirement, or merely denotes a
> many-valued feature that the language permits.

Records are marked `frozen_contested` (C14/C15). The class is retained — not withdrawn — so a reader
can report with and without it.

**Definition (include):** a `connection` whose end is a feature chain that traverses a
multi-valued usage (e.g. `fleet : Agv[10]`, `stations : DockingStation[4]`), so the connector as
written relates *collections*, not the individual parts it names. The end does not identify one
feature at each side, and the connection therefore cannot hold between the parts the model text
asserts it connects.
**Exclude:** a chain through single-valued usages, even when it mixes a port end with a part end
(§5, exclusion 3 — no normative basis found to call that an error); a connection whose ends name
a definition (T1); a connection whose end name is undeclared (N1).
**Basis and honesty note:** the end-feature rules are adjacent (`validateFeatureEndMultiplicity`
requires an end feature to be 1..1; `checkConnectorTypeFeaturing` requires featuring-type
compatibility), but I did not find a named constraint that decides *feature chains over
multi-valued usages*. This class is coded as a **structural defect established from the model
text**, not as a named OCL violation; the report says so and the detection column shows whether
the pinned tool notices.
**Worked examples:** `../corpus/normalized/T4-C1.sysml:51` —
`connection powerLink connect controller.fleet.battery.power to controller.fleet.dock.power;`
(`fleet : Agv[10]`); `T4-C3.sysml:56` — `connect fleet.vehicles.battery.power to
fleet.stations.power;` (`vehicles : Agv[10]`, `stations : DockingStation[4]`).

### I1 — Internal contradiction (status: CONTESTED)

**Contested status, added 2026-11-13T15:06Z (A-7, A-9).** A model record carries `status ∈ {frozen,
frozen_contested, post_inspection}`. `frozen_contested` means the label may be right but a rival
reading is live, and a reader must be able to report with and without it. I1 is such a class: a
documentation band of 35–75 % *contains* a declared 35–55 % bound, so calling this a contradiction is
an authored reading that the text does not compel. The body below is the original, unqualified
criterion, retained as the superseded form.

**Definition (include):** the model text asserts two incompatible things about its own content, in
a way no reading reconciles — here, a requirement's documentation states one numeric bound while
the requirement's own attribute declares another.
**Exclude:** a deviation from the *task prompt* (fidelity — out of scope, issue #9 territory); a
value that is merely unused; a documentation sentence that is vague rather than contradictory.
**Worked example:** `../corpus/normalized/T1-C3.sysml:37,39` — `doc /* … between 35% and 75% … */`
with `attribute upperBound : Real = 55.0;`. Both cannot be the model's upper bound. Note that the
prompt said 35–55, so the 75 is also a fidelity defect; **only the internal contradiction is
coded**, and the fidelity deviation is deliberately not counted (exclusion 1).

---

## 2. Precedence rules (applied to every record)

1. **Mechanism, not symptom.** Code the mechanism that produces the defect; a symptom that is a
   consequence of an already-coded defect is recorded in `notes`, not as a second record.
2. **Parse before resolve.** If a span is not in the textual notation, it is S1/S2; names inside
   it are not additionally coded.
3. **Prelude before dangling name.** Unresolved stdlib scalar types with no library import are
   N2, never N1.
4. **Definition/usage mismatch is T1, not N1**, when the name *does* resolve but to the wrong kind
   of element.
5. **Structure over semantics for connectors.** A connector defect that is visible in the model's
   own structure (ends not individual) is R1 even if it also looks semantically odd.
6. **No double-coding the wrapper.** W1 is never coded on a normalised model.
7. **Uncertainty is recorded, not resolved by fiat.** A record may carry `confidence` in `notes`
   (`high`/`medium`/`low`); a low-confidence record is still counted, and the report states how
   many there are.

## 3. Severity scale (as frozen in the methodology)

`blocking` — the model cannot be loaded/parsed at all, or the defect prevents the construct from
resolving (W1, S1, S2, N1, N2). `major` — the construct resolves but is wrong as a construct
(T1, R1). `minor` — a localised defect that is real but does not stop the model being interpreted
(I1).

## 4. What the layer labels mean here

`wrapper/formatting` = the artefact's packaging; `syntax/parse` = textual notation;
`name resolution` = scope/imports; `type/typing` = definition/usage and typing distinctions;
`constraint/OCL` = a named well-formedness constraint violation; `semantic/behavioural` =
meaning of a construct that parses and resolves; `structural/architectural` = whole-model
structure (connectors, decomposition). The detection table maps each class to whether the pinned
validator reports anything at that layer — that is a measurement of the instrument, not evidence
for the class.

## 5. Explicit exclusions — things this codebook deliberately does **not** count as errors

These were all observed in the corpus and rejected, with the reason, so that the taxonomy is not
inflated by taste:

1. **Deviation from the task prompt** (e.g. a bound that differs from the paragraph). Fidelity is
   issue #9's question, not a well-formedness property.
2. **Untyped port usages** (`port inlet;` in 12 models). The textual notation permits a port usage
   with no type; the implicit specialisation is derived, not written. Not an error.
3. **Part-to-part and port-to-part connection ends** where both are single-valued
   (e.g. `connect house.tank to house.circuit.supply;`). I found no normative basis for calling
   this ill-formed; it is a modelling choice with a semantic smell, and the smell is an adequacy
   judgement.
4. **Connecting value properties** (`T3-C1:39`, `connect pump.sensor.measuredPressure to
   pump.flowRate;`). Similarly not established as ill-formed from the text; the mismatch of
   quantities is semantic and belongs to fidelity/adequacy.
5. **Flow over an attribute definition** (`T6-C1:48-50`, `flow of Temperature …`). Not established
   as ill-formed; a value type as flow payload is questionable modelling, not a text defect.
6. **`entry action lowerArms;` with a package-level `action def lowerArms`** (`T2-C3:53`). The
   notation declares a usage named `lowerArms`; that the name matches a definition is not a
   kind mismatch.
7. **Unused declarations, unused imports, missing `doc`, absent behaviour, decomposition and
   naming choices** — inclusion/coverage properties, recorded separately (see `models.csv`
   columns), never errors.
8. **Anything a validator reports that is not also a defect of the model text.** The validator
   column may add diagnostics; it may not add errors.

## 6. Wrapper counting (separate denominator)

For each **raw** output record: `wrapper_status` ∈ {`fenced`, `no_fence`, `multi_block`},
`preamble_present` (bool), `trailing_prose_present` (bool), and later `parses_as_is` (bool, from
the detection run). W1 is counted over raw outputs; the error population is counted over
normalised models. The two counts are never added together.

## 7. Agreement procedure (fixed before the second coder ran)

The second coder receives this file, the 12 selected normalised models and their raw wrappers, and
labels independently in the same CSV schema. Agreement is computed by `agreement.py`:
model-level agreement on "any error present / none"; record-level agreement on class for records
that both coders placed in the same model (paired by error id after sorting by line); percent
agreement; Cohen's κ for the class label and for the presence call, with the prevalence caveat
stated; Krippendorff's α (nominal) as a cross-check. Disagreements are listed with both coders'
classes and excerpts, and are **not** resolved by majority.

## 8. Revision table

| Version | Date (UTC) | Change | Why |
|---|---|---|---|
| 0.1 | 2026-11-13T14:08Z | open pass notes, no classes | start of coding |
| 0.2 | 2026-11-13T14:10Z | clustered observations into W1/S1/S2/N1/N2/T1/R1/I1 | 14 observed defects across 18 models; each cluster had ≥1 span |
| 0.3 | 2026-11-13T14:11Z | split N2 out of N1; added precedence rules 2–4 and exclusion list §5 | the four "satisfy by subject parameter" cases and the one "missing import" case have different mechanisms; exclusions were being re-litigated per model |
| **1.0** | **2026-11-13T14:12Z** | **frozen** — classes, precedence, exclusions fixed before second coding | methodology §5.5 |

---

## 9. Amendment v1.1 — 2026-11-13T14:14Z — S2 corrected against the normative BNF

**What happened.** While the coding was being checked against the specification (before the
detection run was used for anything), the SysML 2.0 Language Specification `formal/2026-03-02`
was retrieved and its textual-notation BNF read
(`https://www.omg.org/spec/SysML/2.0/Language/PDF`, 691 pages, sha256
`46e6c0476a6f1f34f367d57e039d56659bff75e41d2e4b3d37ca4cadea84a83a`). §8.2.2.21.2 gives:

```
SatisfyRequirementUsage =
    OccurrenceUsagePrefix 'assert' ( isNegated ?= 'not' ) 'satisfy'
    ( ownedRelationship += OwnedReferenceSubsetting FeatureSpecializationPart?
    | 'requirement' UsageDeclaration )
    ValuePart?
    ( 'by' ownedRelationship += SatisfactionSubjectMember )?
    RequirementBody
```

The `'by'` clause is **optional**. The original S2 class ("mandatory clause omitted",
syntax/parse, blocking) therefore rested on a false premise, and the one record coded under it is
not a parse defect at all. The pinned validator's silence on that construct was correct.

**Change.** S2 is retained as a class ID but redefined: the defect is that a `satisfy` usage has
*no satisfying feature*, so the requirement is asserted satisfied with nothing bound to its
subject. The obligation that makes this a defect is the (discretionary, `check…`)
constraint `checkSatisfyRequirementUsageBindingConnector` — "A SatisfyRequirementUsage must have
exactly one ownedMember that is a BindingConnector between its subjectParameter and some Feature
other than the subjectParameter" (§8.3.21.10). Layer therefore moves from `syntax/parse` to
`constraint/OCL`, and the default severity from `blocking` to `minor`, because reporting is
discretionary for `check…` constraints (catalogue `obligation` column: "MAY report, satisfy by
implied relationships, or ignore").

**Effect on labels.** One record changes layer/severity (the `satisfy` with no `by`); the error
*count* is unchanged. No other record was touched. The change is recorded here, in
`../../AMENDMENTS.md` A6, and in `errors.csv` (`notes` of that record), rather than being applied
silently.

**What this does not change.** The classes, their mutual exclusivity, the precedence rules, the
exclusion list and every other label stand as frozen at v1.0. The classes were *not* adjusted to
fit validator output; this correction came from the normative grammar, which is the authority the
methodology names.

| Version | Date (UTC) | Change | Why |
|---|---|---|---|
| 1.1 | 2026-11-13T14:14Z | S2 redefined (layer `constraint/OCL`, severity `minor`); 1 record relabelled | BNF shows `'by'` is optional; the obligation is `checkSatisfyRequirementUsageBindingConnector`, not the grammar |

---

## 10. Amendment v1.2 — 2026-11-13T14:15Z — new class T2, S1 keyword scope, and the discovery-route rule

**Context.** The detection run (post-freeze) drew attention to defects the inspection pass had
missed. Protocol §7.2 forbids a validator verdict becoming the criterion for an error, so none of
these was added on the tool's authority. Each was verified against the normative text and kept in
a separate file (`errors-post-inspection.csv`), leaving the frozen population in `errors.csv`
untouched. This section records the taxonomy consequence.

1. **S1 is broader than the first pass recorded.** SysML 2.0 §8.2.2.1.2 lists the reserved
   keywords explicitly: `… in inout … out … return … state … assign … first then …` (the list is
   reproduced in the specification clause). The first inspection pass caught `port in;` but
   missed `port out;`, `port return;`, `attribute state : String;` and `action def assign;`.
   Consequence: S1's *definition* is unchanged, but the corpus contains 9 S1 records, not 3, and
   the frozen count of 3 is an inspection under-count, not a different class. Codebook note added:
   **when checking S1, test every declared name against the §8.2.2.1.2 list.**
2. **New class T2 — typing mismatch (attribute typed by a non-value definition).** Observed once
   (`attribute window : VisibilityWindow;` where `VisibilityWindow` is a `part def`). Obligation:
   `checkAttributeUsageSpecialization` (8.3.7.3) — an AttributeUsage must specialise
   `Base::dataValues`. Distinct from T1 (definition-where-usage-required) and from N1 (name does
   not resolve): here the name resolves and the usage/definition distinction is respected, but the
   *kind of definition* is wrong. Layer: type/typing. Severity: major.
3. **Discovery-route rule (new, general).** A record may be discovered by any route, but it may
   only enter the taxonomy if the *basis* recorded for it is a specification clause, a named
   constraint or the model text itself. The `discovery_route` and `verification` columns exist for
   this: "detection run surfaced" is acceptable as a route of attention; "the tool said so" is not
   an admissible basis. Records so added are reported separately from the pre-detection population,
   and every frequency table states which population it uses.
4. **One record corrected in place, not reclassified:** the S1 record for the `in`/`out` pair now
   records 2 occurrences; the T1 record's span is narrowed to lines 42-43 because `assign` is a
   reserved keyword (own S1 record), not a kind mismatch.

| Version | Date (UTC) | Change | Why |
|---|---|---|---|
| 1.2 | 2026-11-13T14:15Z | added T2; S1 occurrence scope corrected; discovery-route rule | post-freeze verification of defects the detection run surfaced, each grounded in §8.2.2.1.2 / §8.3.7.3 |

---

## 11. Amendment v1.3 — 2026-11-13T14:27Z — corrections after Reviewer B's Gate-2 review

Reviewer B audited this codebook against the artefacts and found three places where it describes
the labels inaccurately. Each is corrected here; none changes a class definition.

1. **§10.4 claimed a change that was not in `errors.csv`.** It said "the S1 record for the `in`/`out`
   pair now records 2 occurrences". The frozen row `T3-C2-E01` actually read `line_range = 23,33`
   and excerpt `port in;`, so the second declaration (`port out;`, line 24) was *not* recorded, and
   the claim was wrong. The record is now corrected **outside** the frozen file
   (`errors-corrections.csv` C02/C03 → `errors-combined.csv`), because `errors.csv` is the
   pre-detection freeze and is never edited. Convention, now explicit: **`errors.csv` is
   immutable; corrections are written to `coding/errors-corrections.csv` and applied to
   `coding/errors-combined.csv` by `coding/apply_corrections.py`.**
2. **The T1 record's span.** §10.4 said the span was narrowed to lines 42-43; it was narrowed only
   in `post_inspection.py`'s working list, not in any CSV. The frozen row still says 42-44. Same
   convention applies: the narrowing is C04 in the corrections file.
3. **R1's layer label is an authored placement.** The class table placed R1 at
   `structural/architectural`. Reviewer B is right that its operative condition is end-feature
   multiplicity conformance ("after resolving the chain, the end denotes more than one feature"),
   which is a typing/multiplicity statement, not an architectural one. The placement is re-recorded
   as `type/typing` in the corrections file (C05/C06); the rival reading (architectural) remains
   visible in the report's addendum. The class definition itself is unchanged.

Also recorded, not changed: the S1 citation basis. Two S1 records cited a `check…` OCL constraint
that is a MAY obligation about implied bindings; a notation defect must cite the textual-notation
production that does not admit the text (§8.2.2.21.2 for `satisfy`, §8.2.2.18 for transitions).
Corrected in C08/C09. For T2, the citation `checkAttributeUsageSpecialization` is kept but its MAY
obligation is now stated in the record (C10), with §7.7.1 prose as the decisive basis.

| Version | Date (UTC) | Change | Why |
|---|---|---|---|
| 1.3 | 2026-11-13T14:27Z | correction convention (frozen file immutable, corrections in a dated file); R1 layer re-recorded; citation bases corrected | Reviewer B's O2, O3, O8, O9, O10, verified against the models and the pinned specification |

---

## 12. Amendment v1.4 — 2026-11-13T15:06Z — adjudicated corrections to the class table and bodies

Applied after Gate-4 adjudication (`research/relational/adjudication/CORRECTIONS.md` A-6, A-7, A-12):

1. **S1 row** cites the notation productions (8.2.2.21.2, 8.2.2.18, 8.2.2.1.2) rather than a MAY
   `check…` constraint and the abstract-syntax clause; the superseded wording is retained in the row.
2. **R1 row** places the class at `type/typing` and marks **defect status contested**, with the
   operational criterion restated so the contested step is visible.
3. **S2 body** no longer asserts that a mandatory clause was omitted; the class table's wording
   ("required semantic binding absent where the notation's clause is optional") is authoritative.
4. **Contested status is part of the per-class record schema** (`status ∈ {frozen,
   frozen_contested, post_inspection}`), so a future coder sees it in the codebook, not only in a CSV.
5. **Agreement cannot be re-established from the artefacts that exist.** The v1.0 copy the second
   coder used carried the pre-correction S1/S2/R1 text, and the coder-facing codebook was an answer
   key for 8 of 11 paired excerpts; κ = 1.0 is a reproduction check. A held-out set with no exemplar
   in this codebook is required — the 24 external artefacts are the cheapest candidate
   (`coding/agreement-addendum.md`).

| Version | Date (UTC) | Change | Why |
|---|---|---|---|
| 1.4 | 2026-11-13T15:06Z | class table/bodies corrected with superseded markers; contested status in the schema; no-re-establishment statement | adjudication A-6, A-7, A-12 |
