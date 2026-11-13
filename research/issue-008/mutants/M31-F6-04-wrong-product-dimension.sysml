// Authored pattern (Type A): quantity and unit usage over the normative ISQ and SI
// libraries. Labelled authored, not quoted from the specification.
// Provenance: KG-08-quantities.PROVENANCE.md
package KG08Quantities {
    private import ScalarValues::*;
    private import ISQ::*;
    private import SI::*;

    part def Vehicle {
        attribute unladenMass : MassValue = 1200.0 [kg];
        attribute overallLength : LengthValue = 4.5 [m];
        attribute ratedSpeed : SpeedValue = 55.0 [m/s];
        attribute kineticEnergyAtRatedSpeed : EnergyValue =
            unladenMass * ratedSpeed;
    }
}
