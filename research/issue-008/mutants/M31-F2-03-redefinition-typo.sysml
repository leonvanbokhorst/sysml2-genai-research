// Clause 7.21.2 (SysML 2.0 Part 1, formal/2026-03-02, p.133), examples adapted:
// the specification types the masses with ISQ::MassValue and writes 0[kg]; this
// model uses Real with a unitless bound so that KG-07 is independent of the unit
// libraries (deviation recorded in the provenance file).
// Provenance: KG-07-requirements.PROVENANCE.md
package KG07Requirements {
    private import ScalarValues::*;

    part def Vehicle {
        attribute totalMass : Real;
    }

    requirement def <'1.1'> MaximumMass {
        doc
        /*
         * Assuming the required mass is greater than 0,
         * the actual mass shall be less than or equal to
         * the required mass.
         */
        attribute massActual : Real;
        attribute massRequired : Real;
        assume constraint { massRequired > 0.0 }
        require constraint { massActual <= massRequired }
    }

    part vehicle : Vehicle {
        attribute :>> totalMass = 1500.0;
    }

    requirement <'v1.1'> vehicleMaximumMass : MaximumMass {
        doc
        /* The total mass of a Vehicle shall be no greater than its required mass. */
        subject v : Vehicle;
        attribute :>> massActul = 1500.0;
        attribute :>> massRequired = 2000.0;
    }

    satisfy vehicleMaximumMass by vehicle;
}
