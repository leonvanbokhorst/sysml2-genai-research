// P06a — dimensionally consistent quantities (the positive control for P06b).
// Property under test: unit dimensional consistency.
package P06A {
    private import ScalarValues::*;
    private import ISQ::*;
    private import SI::*;

    part vehicle {
        attribute mass : MassValue = 1500.0 [kg];
        attribute load : MassValue = 4.0 [kg];
        attribute total : MassValue = mass + load;
    }
}
