// P03b — the same requirement, with the actual mass exceeding the required mass.
// The only change from P03a is `massActual = 2500.0`.
// Property under test: requirement satisfaction with a constraint (the violated case).
package P03B {
    private import ScalarValues::*;

    part def Vehicle { attribute totalMass : Real; }

    requirement def MaximumMass {
        subject v : Vehicle;
        attribute massActual : Real;
        attribute massRequired : Real;
        require constraint { massActual <= massRequired }
    }

    part vehicle : Vehicle { attribute :>> totalMass = 2500.0; }

    requirement vehicleMaximumMass : MaximumMass {
        subject v = vehicle;
        attribute :>> massActual = 2500.0;
        attribute :>> massRequired = 2000.0;
    }

    satisfy vehicleMaximumMass by vehicle;
}
