#!/usr/bin/env python3
"""Regenerate the mutant corpus from the known-good models.

Every mutant is ONE injected defect, applied to a known-good base by an exact
literal substitution (or deletion). The script asserts that each substitution
matched exactly once, so a silent drift in a base model fails loudly instead of
producing a mutant that is not the mutant it claims to be.

It writes research/issue-008/mutants/<mutant_id>.sysml and prints a diff-like
record. MANIFEST.csv is authored separately (it is the frozen expectations
table); this script only produces the model text.

Usage:  python3 harness/make_mutants.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
KNOWN = ROOT / "known-good"
OUT = ROOT / "mutants"

# (mutant_id, base_file, old, new, note)
MUTATIONS = [
    # ---------------- F1  syntax / textual notation ----------------
    ("M31-F1-01-missing-semicolon", "KG-01-parts.sysml",
     "        part engine : Engine;\n",
     "        part engine : Engine\n",
     "delete the terminator after the part declaration"),
    ("M31-F1-02-extra-brace", "KG-05-states.sysml",
     "    }\n}\n",
     "    }\n}\n}\n",
     "one extra closing brace at the end of the file"),
    ("M31-F1-03-keyword-typo", "KG-02-ports.sysml",
     "    port def FuelingPort {",
     "    prot def FuelingPort {",
     "misspell the kind keyword `port`"),
    ("M31-F1-04-unquoted-shortname", "KG-07-requirements.sysml",
     "requirement def <'1.1'> MaximumMass {",
     "requirement def <1.1> MaximumMass {",
     "drop the quotes around a digit-leading short name"),

    # ---------------- F2  unresolved reference ----------------
    ("M31-F2-01-type-typo", "KG-01-parts.sysml",
     "part engine : Engine;",
     "part engine : Engin;",
     "drop one character from a type name"),
    ("M31-F2-02-parameter-typo", "KG-09-actions.sysml",
     "bind focus.scene = scene;",
     "bind focus.scene = scne;",
     "drop one character from a parameter name in a binding"),
    ("M31-F2-03-redefinition-typo", "KG-07-requirements.sysml",
     "attribute :>> massActual = 1500.0;",
     "attribute :>> massActul = 1500.0;",
     "drop one character from the target of a redefinition"),
    ("M31-F2-04-missing-declaration", "KG-01-parts.sysml",
     "    part def Wheel;\n",
     "",
     "omit the declaration of a referenced type"),

    # ---------------- F3  kind / type mismatch ----------------
    ("M31-F3-01-part-typed-by-portdef", "KG-02-ports.sysml",
     "        port fuelOutPort : FuelingPort;",
     "        part fuelOutPort : FuelingPort;",
     "declare a part usage typed by a port definition"),
    ("M31-F3-02-attribute-typed-by-partdef", "KG-08-quantities.sysml",
     "attribute unladenMass : MassValue = 1200.0 [kg];",
     "attribute unladenMass : Vehicle = 1200.0 [kg];",
     "type an attribute usage by a part definition"),
    ("M31-F3-03-state-replaced-by-action", "KG-06-transitions.sysml",
     "        state on;",
     "        action on;",
     "supply an action where the transitions require a state vertex"),
    ("M31-F3-04-subject-typed-by-requirement", "KG-07-requirements.sysml",
     "        subject v : Vehicle;",
     "        subject v : MaximumMass;",
     "type a requirement subject by a requirement definition"),

    # ---------------- F4  multiplicity / cardinality ----------------
    ("M31-F4-01-inverted-bounds", "KG-01-parts.sysml",
     "part wheels[4] : Wheel;",
     "part wheels[4..2] : Wheel;",
     "swap the order of a bounded multiplicity"),
    ("M31-F4-02-end-feature-multiplicity", "KG-03-connections.sysml",
     "        end part hub : Hub;",
     "        end part hub : Hub[2];",
     "give a connection end feature a multiplicity other than 1..1"),
    ("M31-F4-03-non-natural-bound", "KG-01-parts.sysml",
     "part wheels[4] : Wheel;",
     "part wheels[0.5] : Wheel;",
     "write a fractional multiplicity bound"),
    ("M31-F4-04-feature-value-count", "KG-04-featurevalues.sysml",
     "        attribute scores[1..*] : Integer;",
     "        attribute scores[1] : Integer = (1, 2);",
     "assert a single-valued feature and give it two values"),

    # ---------------- F5  named constraint violation ----------------
    ("M31-F5-01-feature-value-overriding", "KG-04-featurevalues.sysml",
     "        attribute cutoff : Integer default = 0.75 * averageScore;",
     "        attribute cutoff : Integer = 0.75 * averageScore;",
     "write a fixed feature value (`=`) where a default (`default =`) was meant, "
     "so the redefinition in TestWithCutoff overrides a bound value"),
    ("M31-F5-02-satisfy-reference", "KG-07-requirements.sysml",
     "    satisfy vehicleMaximumMass by vehicle;",
     "    satisfy Vehicle by vehicle;",
     "name a part definition instead of the requirement usage in a satisfy link"),
    ("M31-F5-03-decision-node-incoming", "KG-09-actions.sysml",
     "        first action2 then join1;",
     "        first action2 then join1;\n        first action2 then decision1;",
     "route a second succession into the decision node instead of the merge"),
    ("M31-F5-04-composite-port-feature", "KG-02-ports.sysml",
     "        in fuelReturn : Fuel;\n",
     "        in fuelReturn : Fuel;\n        part fuelLine : Fuel;\n",
     "declare a composite feature inside a port definition"),

    # ---------------- F6  quantity / unit dimensionality ----------------
    ("M31-F6-01-wrong-dimension-unit", "KG-08-quantities.sysml",
     "attribute ratedSpeed : SpeedValue = 55.0 [m/s];",
     "attribute ratedSpeed : SpeedValue = 55.0 [kg];",
     "give a speed quantity a mass unit"),
    ("M31-F6-02-missing-unit", "KG-08-quantities.sysml",
     "attribute unladenMass : MassValue = 1200.0 [kg];",
     "attribute unladenMass : MassValue = 1200.0;",
     "omit the unit from a quantity value"),
    ("M31-F6-03-incommensurable-sum", "KG-08-quantities.sysml",
     "        attribute kineticEnergyAtRatedSpeed : EnergyValue =\n"
     "            0.5 * unladenMass * ratedSpeed * ratedSpeed;",
     "        attribute kineticEnergyAtRatedSpeed : EnergyValue =\n"
     "            unladenMass + ratedSpeed;",
     "add a mass to a speed in a quantity expression"),
    ("M31-F6-04-wrong-product-dimension", "KG-08-quantities.sysml",
     "        attribute kineticEnergyAtRatedSpeed : EnergyValue =\n"
     "            0.5 * unladenMass * ratedSpeed * ratedSpeed;",
     "        attribute kineticEnergyAtRatedSpeed : EnergyValue =\n"
     "            unladenMass * ratedSpeed;",
     "supply a momentum product where an energy is declared"),

    # ---------------- F7  structural / architectural ----------------
    ("M31-F7-01-unreachable-state", "KG-05-states.sysml",
     "        first off then starting;\n",
     "",
     "remove the only succession into a state"),
    ("M31-F7-02-satisfied-but-violated", "KG-07-requirements.sysml",
     "attribute :>> massActual = 1500.0;",
     "attribute :>> massActual = 2500.0;",
     "give the satisfying part a value that violates the requirement it satisfies"),
    ("M31-F7-03-missing-flow", "KG-09-actions.sysml",
     "        flow focus.image to shoot.image;\n",
     "",
     "remove the flow that supplies a subaction input"),
    ("M31-F7-04-contradictory-assertions", "KG-10-asserts.sysml",
     "        assert constraint { computedMass >= 0.0 }",
     "        assert constraint { computedMass >= 0.0 }\n"
     "        assert constraint { computedMass < 0.0 }",
     "assert two constraints that cannot both hold"),

    # ---------------- F8  metadata / annotation mis-typing ----------------
    ("M31-F8-01-annotation-not-metadata", "KG-01-parts.sysml",
     "        @SafetyRelevant { level = 3; }",
     "        @Engine { }",
     "annotate with a part definition instead of a metadata definition"),
    ("M31-F8-02-body-feature-typo", "KG-01-parts.sysml",
     "        @SafetyRelevant { level = 3; }",
     "        @SafetyRelevant { levle = 3; }",
     "misspell the metadata feature name in the annotation body"),
    ("M31-F8-03-value-kind", "KG-01-parts.sysml",
     "        @SafetyRelevant { level = 3; }",
     "        @SafetyRelevant { level = \"high\"; }",
     "give an Integer metadata feature a String value"),
    ("M31-F8-04-abstract-metaclass", "KG-01-parts.sysml",
     "    metadata def SafetyRelevant {",
     "    abstract metadata def SafetyRelevant {",
     "annotate with an abstract metadata definition"),
]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    bases = {}
    for mid, base, old, new, note in MUTATIONS:
        if base not in bases:
            bases[base] = (KNOWN / base).read_text()
        text = bases[base]
        count = text.count(old)
        if count != 1:
            raise SystemExit(
                f"{mid}: substitution matched {count} times in {base}, expected exactly 1\n"
                f"  old={old!r}"
            )
        mutated = text.replace(old, new, 1)
        assert mutated != text, mid
        target = OUT / f"{mid}.sysml"
        target.write_text(mutated)
        removed = [l for l in old.splitlines() if l not in new.splitlines()]
        added = [l for l in new.splitlines() if l not in old.splitlines()]
        print(f"{mid}: {base}")
        for line in removed:
            print(f"  - {line.strip()}")
        for line in added:
            print(f"  + {line.strip()}")
        print(f"    ({note})")
    print(f"\nwrote {len(MUTATIONS)} mutants to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
