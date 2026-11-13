// P05b — the same declarations with non-conforming values, including the exact class Sensmetry's
// divergence register says the OMG *reference implementation* accepts (a Real bound to an
// Integer-typed feature: `attribute num : ScalarValues::Positive = 5.0;`).
// Property under test: type conformance of an attribute value.
package P05B {
    private import ScalarValues::*;

    part device {
        attribute count : Integer = 2.5;
        attribute num : Positive = 5.0;
        attribute flag : Boolean = 1;
    }
}
