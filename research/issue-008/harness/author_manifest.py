#!/usr/bin/env python3
"""Authoring script for mutants/MANIFEST.csv — the PRE-REGISTERED expectations.

The expectations in this file were authored from the specification, the 623-row
constraint catalogue and the model text, BEFORE the validator was run over any
mutant. They are not derived from any validator output. The script is kept for
regenerability; `mutants/MANIFEST.csv` is the frozen artefact and its sha256 is
recorded in `mutants/expectations.sha256` before the first run.

Fields
  mutant_id                  stable id, also the file stem
  base_model                 known-good model the mutant was derived from
  fault_class                F1..F8
  spec_constraint_or_defect  the condition the mutant instantiates, with clause
  expected_layer             syntax | names | typing | constraints | none
  expected_detectable        yes | no | uncertain  (spec-side reasoning only)
  rationale                  why that expectation
  plausibility               why a generator could produce this defect
  surface_tell               yes | no — is the defect lexically conspicuous?
  sha256                     hash of the mutant file
"""
import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MUT = ROOT / "mutants"

ROWS = [
    # ---- F1 syntax / textual notation -------------------------------------
    ("M31-F1-01-missing-semicolon", "KG-01-parts.sysml", "F1-syntax",
     "SysML 2.0 §8.2 textual notation: a usage declaration is terminated by ';' (notation condition, not an OCL constraint)",
     "syntax", "yes",
     "The text does not parse as the notation the specification defines; this is the instrument's first advertised layer.",
     "A generator emitting a member list often drops the terminator on the last member of a block, or on a member written without a body.",
     "yes"),
    ("M31-F1-02-extra-brace", "KG-05-states.sysml", "F1-syntax",
     "SysML 2.0 §8.2 textual notation: a namespace/definition body is a balanced '{' … '}' block",
     "syntax", "yes",
     "Unbalanced braces cannot be parsed; nothing about the model's meaning can be checked.",
     "A generator writing nested state bodies emits one closing brace too many when it closes both the last substate and the enclosing definition.",
     "yes"),
    ("M31-F1-03-keyword-typo", "KG-02-ports.sysml", "F1-syntax",
     "SysML 2.0 §7.12.2 / §8.2: the kind keyword of a port definition is 'port'",
     "syntax", "yes",
     "An unknown keyword is a notation error at the parse layer.",
     "Character-level slips in a kind keyword are a common generation artefact when many similar keywords (port/part/action) are in play.",
     "yes"),
    ("M31-F1-04-unquoted-shortname", "KG-07-requirements.sysml", "F1-syntax",
     "SysML 2.0 §7.2.2 / §8.2: a short name is '<' name '>', and a name beginning with a digit must be quoted ('1.1')",
     "syntax", "yes",
     "An unquoted digit-leading name is not admitted by the notation.",
     "A generator asked to preserve requirement identifiers such as '1.1' naturally emits <1.1> rather than <'1.1'>; the identifier is real, the quoting rule is not modelled.",
     "no"),
    # ---- F2 unresolved reference ------------------------------------------
    ("M31-F2-01-type-typo", "KG-01-parts.sysml", "F2-unresolved",
     "KerML 1.0 §8.3.3 namespace/membership resolution: a type reference must resolve to a visible element. No constraint in the 623-row catalogue names resolution.",
     "names", "yes",
     "The name resolves to nothing; the reference has no referent, so no constraint about the reference can be evaluated.",
     "Dropping a character from a name it has just used is a textbook generation defect; the name is still locally plausible.",
     "no"),
    ("M31-F2-02-parameter-typo", "KG-09-actions.sysml", "F2-unresolved",
     "KerML 1.0 §8.3.3 resolution: a feature reference in a binding must resolve (here a parameter name)",
     "names", "yes",
     "As F2-01, at a feature-reference site rather than a type site: a different resolver path is exercised.",
     "Parameter names are short and repeated across actions; a generator copying a parameter list can alter one letter.",
     "no"),
    ("M31-F2-03-redefinition-typo", "KG-07-requirements.sysml", "F2-unresolved",
     "KerML 1.0 §8.3.3.3.4: the target of a redefinition (' :>> ') must be a feature inherited by the owning element; a typo'd target resolves to nothing",
     "names", "yes",
     "The redefinition names no inherited feature, so the relationship is dangling. Third distinct resolution site (redefinition target).",
     "The redefined name is long ('massActual') and the generator writes it twice (declaration and redefinition); one of the two is altered.",
     "no"),
    ("M31-F2-04-missing-declaration", "KG-01-parts.sysml", "F2-unresolved",
     "KerML 1.0 §8.3.3 resolution: a type used by a feature must be declared somewhere in the model",
     "names", "yes",
     "The declaration is simply absent, so the reference cannot resolve. This is the omission form, not the typo form.",
     "A generator that summarises a design can use a type ('Wheel') it never declares, especially when the type only appears in a multiplicity-sized collection.",
     "no"),
    # ---- F3 kind / type mismatch ------------------------------------------
    ("M31-F3-01-part-typed-by-portdef", "KG-02-ports.sysml", "F3-kind-mismatch",
     "SysML 2.0 §7.11.2 prose: 'a part usage must only be defined by item definitions (including part definitions) or KerML structures'; a port definition is neither. No constraint of this shape exists in the 623-row catalogue.",
     "typing", "yes",
     "The metaclass pairing is wrong (PartUsage ↔ PortDefinition). A conformant tool must reject it; whether any tool checks it is the measurement.",
     "Ports and parts are both occurrence usages with similar notation; a generator relabelling a connection point as a component produces exactly this.",
     "no"),
    ("M31-F3-02-attribute-typed-by-partdef", "KG-08-quantities.sysml", "F3-kind-mismatch",
     "SysML 2.0 §7.7.1/§7.7.2: an attribute usage is typed by a data type (a quantity definition is one; a part definition is not)",
     "typing", "yes",
     "A part definition is not a data type, so the usage is typed by an element of the wrong kind.",
     "Vehicle and its attributes are the two things a generator writes most; conflating the thing with its property is a plausible slip.",
     "no"),
    ("M31-F3-03-state-replaced-by-action", "KG-06-transitions.sysml", "F3-kind-mismatch",
     "SysML 2.0 §7.18.3: a transition relates a source state usage to a target state usage; §8.3.18.9 validateTransitionUsageSuccession requires an ActionUsage target for the succession (MAY/SHOULD as catalogued)",
     "typing", "yes",
     "The succession now targets an action usage where the transition semantics require a state vertex; a kind mismatch at a reference site rather than at a typing site.",
     "State subactions and nested actions are both 'state X;'/'action X;' lines in the same body; a generator that models behaviour as actions emits `action` inside a state definition.",
     "no"),
    ("M31-F3-04-subject-typed-by-requirement", "KG-07-requirements.sysml", "F3-kind-mismatch",
     "SysML 2.0 §7.21.2 prose: 'The subject of a requirement definition or usage is modeled as its first parameter… a subject parameter' (a part/occurrence); a RequirementDefinition is not an occurrence type",
     "typing", "yes",
     "The subject parameter is typed by a requirement definition, i.e. by the wrong family of classifier.",
     "Generators routinely reuse the nearest available name; 'MaximumMass' is the only definition in scope besides Vehicle.",
     "no"),
    # ---- F4 multiplicity ---------------------------------------------------
    ("M31-F4-01-inverted-bounds", "KG-01-parts.sysml", "F4-multiplicity",
     "No catalogue constraint. KerML 1.0 §8.3.4.11.2 derives the lower and upper bounds of a MultiplicityRange; the specification nowhere states that lower <= upper, and a range with lower > upper denotes the empty range rather than an ill-formed element.",
     "none", "no",
     "If the specification does not forbid it, a conformant tool is not obliged to report it. This mutant measures whether the instrument enforces a rule the specification does not state.",
     "Writing a range in the wrong order is a plausible slip when a generator is interpolating a min/max pair into a template.",
     "no"),
    ("M31-F4-02-end-feature-multiplicity", "KG-03-connections.sysml", "F4-multiplicity",
     "KerML 1.0 validateFeatureEndMultiplicity §8.3.3.3.4 (SHOULD report, dependency class A): 'If a Feature has isEnd = true, then it must have multiplicity 1..1'; SysML 2.0 §7.13.2 states the same for connection ends",
     "constraints", "yes",
     "A named validate… constraint with a published OCL body that is decidable from the abstract syntax alone.",
     "A generator that thinks of a hub as plural writes a collection multiplicity on every 'part' line, including the ones it placed after 'end'.",
     "no"),
    ("M31-F4-03-non-natural-bound", "KG-01-parts.sysml", "F4-multiplicity",
     "KerML 1.0 validateMultiplicityRangeBoundResultTypes §8.3.4.11.2 (SHOULD report, dependency class B): bounds must be typed by ScalarValues::Integer and, if evaluable, non-negative",
     "typing", "yes",
     "A named constraint, though one whose dependency class B means it needs the Kernel Data Types library.",
     "A generator reasoning in 'number of wheels' may emit a fraction when it is computing an average or a ratio and reuses the slot.",
     "no"),
    ("M31-F4-04-feature-value-count", "KG-04-featurevalues.sysml", "F4-multiplicity",
     "No catalogue constraint names the relationship between a feature value's element count and the feature's multiplicity; only generic type conformance and the derive… rules on FeatureValue are available",
     "typing", "uncertain",
     "The model is defective in the intended reading (one score, two values), but the specification's own constraints may not name it, so an implementation might legitimately only flag the type mismatch of the sequence.",
     "A generator asked for 'the score' and given a pair of results emits a single-valued attribute and then a literal list.",
     "no"),
    # ---- F5 named constraints ---------------------------------------------
    ("M31-F5-01-feature-value-overriding", "KG-04-featurevalues.sysml", "F5-named-constraint",
     "KerML 1.0 validateFeatureValueOverriding §8.3.4.10.2 (SHOULD report, class A): 'All Features directly or indirectly redefined by the featureWithValue of a FeatureValue must have only default FeatureValues'",
     "constraints", "yes",
     "The redefined feature now carries a fixed (bound) FeatureValue while the redefining feature supplies a default; the constraint's antecedent is satisfied and its consequent violated.",
     "`=` and `default =` differ by one keyword; a generator writing feature values from a table emits the shorter form. This is also the exact construct Sensmetry documents the reference implementation mishandling.",
     "no"),
    ("M31-F5-02-satisfy-reference", "KG-07-requirements.sysml", "F5-named-constraint",
     "SysML 2.0 validateSatisfyRequirementUsageReference §8.3.21.10 (SHOULD report, class A): the referenced feature of a SatisfyRequirementUsage must be a RequirementUsage",
     "constraints", "yes",
     "The reference names a part definition; the constraint names exactly this condition and is model-local (class A).",
     "Requirement IDs are long and the surrounding definitions are not; a generator reaching for 'the thing being satisfied' can pick the part definition it just declared.",
     "no"),
    ("M31-F5-03-decision-node-incoming", "KG-09-actions.sysml", "F5-named-constraint",
     "SysML 2.0 validateDecisionNodeIncomingSuccessions §8.3.17.7 (SHOULD report, class A): 'A DecisionNode may have at most one incoming Succession'. Note: in the reference implementation this constraint is named only in [TODO] methods (catalogue/validator-coverage.json).",
     "constraints", "yes",
     "A decision node with two incoming successions violates a named, model-local constraint. The construct is also the one the reference implementation is documented not to enforce, so it separates this instrument from the reference.",
     "Routing two branches into a decision instead of a merge is the single most plausible control-flow confusion: 'decide' and 'merge' are near-synonyms in prose.",
     "no"),
    ("M31-F5-04-composite-port-feature", "KG-02-ports.sysml", "F5-named-constraint",
     "SysML 2.0 §8.4.8.1 prose-only condition validatePortDefinitionNestedUsagesNotComposite: 'All the features of a port definition or port usage, other than any nested port usages, must be referential (non-composite)'. The name occurs in the PDF but is MISSING from the metamodel (catalogue/prose-only-names.csv).",
     "constraints", "uncertain",
     "The condition is normative prose with no published OCL body, so a tool may implement it, partially implement it, or not at all. An expectation of 'yes' would be a guess about the tool, not about the specification.",
     "A generator drawing a port as a small part with owned internal items writes 'part' inside the port body; that is how ports look in SysML v1 and in informal diagrams.",
     "no"),
    # ---- F6 quantity / unit ----------------------------------------------
    ("M31-F6-01-wrong-dimension-unit", "KG-08-quantities.sysml", "F6-quantity",
     "No catalogue constraint names dimension conformance (0 rows match Quantity/Dimension). Basis: the normative ISQ/SI model libraries (SysML 2.0 §9) and generic conformance of a bound value to its feature's type",
     "typing", "yes",
     "Mass is not a speed; the quantity literal's dimension contradicts the declared quantity type. A conformant tool needs library semantics, so this tests dependency class B territory.",
     "Unit symbols are one- or two-character tokens; a generator filling a template from a table of units mis-picks.",
     "no"),
    ("M31-F6-02-missing-unit", "KG-08-quantities.sysml", "F6-quantity",
     "Same basis as F6-01. The specification does not state that a quantity value must carry a unit; a unitless magnitude is a number, and whether binding it to a quantity type is ill-formed is not settled by a named constraint",
     "typing", "no",
     "If the specification does not require a unit, an implementation is not obliged to report its absence. This mutant measures whether silence here is specification-faithful or merely unchecked.",
     "Omitting the unit bracket is the commonest quantity-generation error: the number is right, the unit is assumed.",
     "no"),
    ("M31-F6-03-incommensurable-sum", "KG-08-quantities.sysml", "F6-quantity",
     "Same basis as F6-01: operator application to quantities of different dimensions is only constrainable through ISQ/SI semantics",
     "typing", "yes",
     "The expression adds a mass to a speed; the resulting dimension is undefined, so the declared EnergyValue cannot be bound.",
     "A generator that knows the formula only by its operands can put '+' where '*' was meant; the expression still looks like physics.",
     "no"),
    ("M31-F6-04-wrong-product-dimension", "KG-08-quantities.sysml", "F6-quantity",
     "Same basis as F6-01: a product of mass and speed has the dimension of momentum, not energy",
     "typing", "yes",
     "The dimensional arithmetic does not reach M·L²·T⁻², so the declared type is contradicted. This is the hardest of the four: it requires multiplying dimensions, not matching a unit symbol to a type.",
     "A generator writing kinetic energy from memory drops the squared velocity term; 'm*v' is a plausible half-remembered formula.",
     "no"),
    # ---- F7 structural / architectural ------------------------------------
    ("M31-F7-01-unreachable-state", "KG-05-states.sysml", "F7-structural",
     "No constraint names reachability. The 623-row catalogue and the 38-row prose-only register contain no condition requiring a state usage to be entered",
     "none", "no",
     "Nothing in the specification's well-formedness surface mentions reachability, so this is expected to be an oracle gap, not a tooling gap.",
     "A generator that renames or drops a transition while keeping the state produces exactly this; the state itself looks perfectly ordinary.",
     "no"),
    ("M31-F7-02-satisfied-but-violated", "KG-07-requirements.sysml", "F7-structural",
     "No constraint ties a SatisfyRequirementUsage to the truth of the requirement's required constraint. A requirement usage is a claim; §7.21.2 defines its semantics as an implication, not as an assertion about the satisfying feature",
     "none", "no",
     "For a checker to catch this it would have to evaluate the required constraint against the satisfying feature's values and treat the satisfy link as an assertion. No catalogue constraint asks for that.",
     "A generator that fills satisfying values from a different document, or invents a plausible number, produces a satisfied-but-false requirement.",
     "no"),
    ("M31-F7-03-missing-flow", "KG-09-actions.sysml", "F7-structural",
     "No constraint requires a subaction's input to be supplied. §7.16/§7.17 define how flows are written, not that a flow must exist",
     "none", "no",
     "An unbound input parameter is not ill-formed; at most an implementation-specific lint could mention it, which is not a specification constraint.",
     "A generator that emits the action sequence but omits the data dependency is the characteristic 'structure right, meaning thin' failure of generated behaviour models.",
     "no"),
    ("M31-F7-04-contradictory-assertions", "KG-10-asserts.sysml", "F7-structural",
     "No constraint names consistency between two assert constraint usages. §7.20.3 defines what an assertion means; nothing forbids two assertions that cannot both hold",
     "none", "no",
     "Detecting this needs reasoning across assertions (or execution), which no validation layer in the specification's surface performs.",
     "A generator assembling a model from two requirements can assert both without noticing the contradiction; each line is locally correct.",
     "no"),
    # ---- F8 metadata ------------------------------------------------------
    ("M31-F8-01-annotation-not-metadata", "KG-01-parts.sysml", "F8-metadata",
     "KerML 1.0 validateMetadataFeatureMetaclass §8.3.4.12.3 (SHOULD report, class A): 'A MetadataFeature must have exactly one type that is a Metaclass'",
     "constraints", "yes",
     "A part definition is not a metaclass, so the annotation has no metaclass at all. Named, model-local, SHOULD-report.",
     "Annotation syntax '@X' accepts any name; a generator using an existing definition to express 'this element is safety-relevant' writes '@SafetyCase' without declaring a metadata def.",
     "no"),
    ("M31-F8-02-body-feature-typo", "KG-01-parts.sysml", "F8-metadata",
     "KerML 1.0 §8.3.4.12.3 with SysML 2.0 §8.3.27.3: a feature in a metadata usage body must redefine a feature of the metaclass",
     "constraints", "yes",
     "The body member redefines nothing, which is the constraint's subject. Whether it is reported as a typo hint or as a violation is a message-quality question, not a detection question.",
     "Metadata feature names are declared once and used once; a generator reproducing them from a prompt alters a letter.",
     "no"),
    ("M31-F8-03-value-kind", "KG-01-parts.sysml", "F8-metadata",
     "KerML 1.0 §8.3.4.12.3 plus generic conformance of a feature value to the feature's type: 'level : Integer' bound to a String literal",
     "typing", "yes",
     "The literal does not conform to the declared type. This is the case the reference implementation is documented to handle *without* strict type checking, so it separates the two implementations' reported behaviour.",
     "Assigning a severity label ('high') to a field declared as a number is a routine generator slip when the surrounding prose uses words.",
     "no"),
    ("M31-F8-04-abstract-metaclass", "KG-01-parts.sysml", "F8-metadata",
     "KerML 1.0 validateMetadataFeatureMetaclassNotAbstract §8.3.4.12.3 (SHOULD report, class A): 'The metaclass of a MetadataFeature must not be abstract'",
     "constraints", "yes",
     "A named, model-local validate constraint whose antecedent is satisfied: the annotated type is abstract.",
     "Declaring metadata definitions abstract is what a generator does when it models a metadata *taxonomy* (SafetyRelevant, SafetyCritical :> SafetyRelevant) and then applies the root.",
     "no"),
]


def main() -> int:
    out = MUT / "MANIFEST.csv"
    rows = []
    for (mid, base, cls, spec, layer, det, rat, plaus, tell) in ROWS:
        path = MUT / f"{mid}.sysml"
        if not path.exists():
            raise SystemExit(f"missing mutant file: {path}")
        rows.append({
            "mutant_id": mid,
            "base_model": base,
            "fault_class": cls,
            "spec_constraint_or_defect": spec,
            "expected_layer": layer,
            "expected_detectable": det,
            "rationale": rat,
            "plausibility": plaus,
            "surface_tell": tell,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        })
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} expectation rows to {out}")
    from collections import Counter
    print("by class:", dict(Counter(r["fault_class"] for r in rows)))
    print("expected_detectable:", dict(Counter(r["expected_detectable"] for r in rows)))
    print("surface_tell:", dict(Counter(r["surface_tell"] for r in rows)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
