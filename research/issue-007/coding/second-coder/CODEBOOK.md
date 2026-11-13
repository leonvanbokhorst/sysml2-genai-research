# CODEBOOK — error classes in GenAI-generated SysML v2 models (issue #7 pilot)

**Version 1.0 — FROZEN at 2026-11-13T15:2xZ (sha256 quoted in the report and in
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
| **S1** | Construct written in a non-conforming textual form | syntax/parse | blocking | `checkSatisfyRequirementUsageBindingConnector` (8.3.21.10); `TransitionUsage` textual notation (8.3.18.9) |
| **S2** | Mandatory clause of a construct omitted | syntax/parse | blocking | `checkSatisfyRequirementUsageBindingConnector` (8.3.21.10) |
| **N1** | Reference to a model element that is not declared or not in scope | name resolution | blocking | no single named OCL constraint — name resolution is a precondition of every constraint (7.5, 8.3.2.4) |
| **N2** | Standard-library prelude omitted, so scalar type names do not resolve | name resolution | blocking | — (normative model libraries; no constraint names the import) |
| **T1** | Kind mismatch: a *definition* referenced where a *usage* is required | type/typing | major | — (no constraint by name; usage/definition distinction is structural in KerML §8.3.3/8.3.6) |
| **R1** | Connector whose ends are not individual features (they traverse a multi-valued usage) | structural/architectural | major | related: `validateFeatureEndMultiplicity` (8.3.3.3.4), `checkConnectorTypeFeaturing` (8.3.4.5.3) |
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
**Worked example:** Example E12 — preamble sentence, then a ```` ```sysml ```` fence, then
trailing prose after the closing fence. Normalised body: Example E1.

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
- Example E2 — `satisfy greenhouse to moistureControl;` — `to` is not
  part of the satisfy notation, and the operands are reversed (requirement first, satisfying
  feature after `by`).
- Example E3 — `transition from idle to lowering on
  detection.approaching;` — `from … to … on …` is SysML v1/UML activity/state-machine notation.
  Four transitions share the mechanism → one record, 4 occurrences.
- Example E4 — `port in;` / `… to line.in;` — `in` is a reserved
  direction keyword; using it as a declared feature name is not accepted as a name in this
  position.

### S2 — Mandatory clause omitted

**Definition (include):** the construct is named correctly but a clause the notation requires is
absent, so the construct cannot mean anything as written. The only corpus instance is a `satisfy`
usage with no satisfying feature (`by` clause), which therefore has no subject binding.
**Exclude:** a construct that leaves an *optional* part out (e.g. an untyped port, an action
usage with no body); a construct that is complete but resolves to nothing (N1).
**Worked example:** Example E5 — `satisfy lowerBeforeArrival;` —
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
- Example E6 — `first start;` — no action usage `start` is declared;
  the succession's source is a dangling name (the model declares `sense`, `compare`,
  `openValve`, `runPump`, `closeValve`).
- Example E7 — `subject pump : InfusionPump;` is declared inside
  `requirement def AlarmTiming`, and the package-level `satisfy alarmTiming by pump;` references
  it from outside. No part usage `pump` exists in the package. Same mechanism in
  `Example`, `Example`, `Example`.

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
**Worked example:** Example E8 — no import at all; `Real` at lines 4, 9,
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
**Worked example:** Example E9 with declarations at `:<lines>` —
`first checkCharge; then checkAvailability; then assign;` against `action def checkCharge;`
etc. Three occurrences, one record.

### R1 — Connector ends that are not individual features

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
**Worked examples:** Example E10 —
`connection powerLink connect controller.fleet.battery.power to controller.fleet.dock.power;`
(`fleet : Agv[10]`); `Example.sysml:56` — `connect fleet.vehicles.battery.power to
fleet.stations.power;` (`vehicles : Agv[10]`, `stations : DockingStation[4]`).

### I1 — Internal contradiction

**Definition (include):** the model text asserts two incompatible things about its own content, in
a way no reading reconciles — here, a requirement's documentation states one numeric bound while
the requirement's own attribute declares another.
**Exclude:** a deviation from the *task prompt* (fidelity — out of scope, issue #9 territory); a
value that is merely unused; a documentation sentence that is vague rather than contradictory.
**Worked example:** Example E11 — `doc /* … between 35% and 75% … */`
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
4. **Connecting value properties** (`Example`, `connect pump.sensor.measuredPressure to
   pump.flowRate;`). Similarly not established as ill-formed from the text; the mismatch of
   quantities is semantic and belongs to fidelity/adequacy.
5. **Flow over an attribute definition** (`Example`, `flow of Temperature …`). Not established
   as ill-formed; a value type as flow payload is questionable modelling, not a text defect.
6. **`entry action lowerArms;` with a package-level `action def lowerArms`** (`Example`). The
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
| 0.1 | 2026-11-13T~14:45 | open pass notes, no classes | start of coding |
| 0.2 | 2026-11-13T~15:05 | clustered observations into W1/S1/S2/N1/N2/T1/R1/I1 | 14 observed defects across 18 models; each cluster had ≥1 span |
| 0.3 | 2026-11-13T~15:15 | split N2 out of N1; added precedence rules 2–4 and exclusion list §5 | the four "satisfy by subject parameter" cases and the one "missing import" case have different mechanisms; exclusions were being re-litigated per model |
| **1.0** | **2026-11-13T15:2xZ** | **frozen** — classes, precedence, exclusions fixed before second coding | methodology §5.5 |
