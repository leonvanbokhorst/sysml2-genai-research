// P04 — a requirement stated in prose only: no `require constraint`, no bound attribute.
// Property under test: requirement satisfaction with prose only.
// The model is *semantically* the same claim as P03b and is in fact false of the declared values
// (totalMass 2500 against a documented 2000 kg limit), so a checker that decided requirement
// satisfaction would have to return "violated". Whether it can depends only on the encoding.
package P04 {
    private import ScalarValues::*;

    part def Vehicle { attribute totalMass : Real; }

    part vehicle : Vehicle { attribute :>> totalMass = 2500.0; }

    requirement def MaxMass {
        doc
        /*
         * The total mass of a Vehicle shall be no greater than 2000 kg.
         */
        subject v : Vehicle;
    }

    requirement maxMass : MaxMass { subject v = vehicle; }

    satisfy maxMass by vehicle;
}
