// Clause 7.20.3 (SysML 2.0 Part 1, formal/2026-03-02, p.128), examples verbatim,
// with MassValue replaced by Real (deviation recorded in the provenance file).
// Provenance: KG-10-asserts.PROVENANCE.md
package KG10Asserts {
    private import ScalarValues::*;

    part testObject {
        attribute computedMass : Real;
        assert constraint { computedMass >= 0.0 }
    }

    constraint negativeMass {
        attribute mass : Real;
        mass < 0.0
    }

    part alienObject {
        attribute antiMass : Real;
        assert negativeMass {
            :>> mass = antiMass;
        }
    }
}
