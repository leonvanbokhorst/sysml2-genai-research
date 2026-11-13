// P03a — requirement satisfaction encoded as a machine-checkable `require constraint`, holding.
// Property under test: requirement satisfaction with a constraint (the positive control for P03b).
package P03A {
    private import ScalarValues::*;

    part def Vehicle { attribute totalMass : Real; }

    requirement def MaximumMass {
        subject v : Vehicle;
        attribute massActual : Real;
        attribute massRequired : Real;
        require constraint { massActual <= massRequired }
    }

    part vehicle : Vehicle { attribute :>> totalMass = 1500.0; }

    requirement vehicleMaximumMass : MaximumMass {
        subject v = vehicle;
        attribute :>> massActual = 1500.0;
        attribute :>> massRequired = 2000.0;
    }

    satisfy vehicleMaximumMass by vehicle;
}
