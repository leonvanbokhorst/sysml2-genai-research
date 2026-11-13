// P06b — a dimensionally impossible sum: a length added to a mass.
// Property under test: unit dimensional consistency.
package P06B {
    private import ScalarValues::*;
    private import ISQ::*;
    private import SI::*;

    part vehicle {
        attribute mass : MassValue = 1500.0 [kg];
        attribute length : LengthValue = 4.0 [m];
        attribute total : MassValue = mass + length;
    }
}
