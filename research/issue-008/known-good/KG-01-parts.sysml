// Clause 7.11.2 (SysML 2.0 Part 1, formal/2026-03-02, p.60), example verbatim;
// Engine and Wheel declarations supplied by the author (the fragment references
// them without declaring them). Provenance: KG-01-parts.PROVENANCE.md
package KG01Parts {
    private import ScalarValues::*;

    item def Person;
    part def Engine;
    part def Wheel;

    // Author-added (not in the clause example): a metadata definition and one
    // annotation, giving the metadata fault class (F8) a base to mutate.
    metadata def SafetyRelevant {
        attribute level : Integer;
    }

    part def Vehicle {
        @SafetyRelevant { level = 3; }
        ref part driver[0..1] : Person;
        part engine : Engine;
        part wheels[4] : Wheel;
    }
}
