// P05a — type-conformant attribute values (the positive control for P05b).
// Property under test: type conformance of an attribute value.
package P05A {
    private import ScalarValues::*;

    part device {
        attribute count : Integer = 5;
        attribute num : Positive = 5;
        attribute flag : Boolean = true;
    }
}
