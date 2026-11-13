// P12 — the same KerML constraint class as Researcher B's F5-01 mutant
// (`validateFeatureValueOverriding`, KerML 1.0 §8.3.4.10.2), at a different site: a feature whose
// value is a FIXED binding (`=`) is redefined by a feature that also binds (`=`), where B's mutant
// pairs a `default =` in the base with a `=` in the redefining feature.
// Purpose: test whether the instrument's silence on F5-01 is a property of the *constraint* or of
// the *site*.
package P12 {
    private import ScalarValues::*;

    part def Base {
        attribute x : Real = 1.0;
    }

    part def Derived :> Base {
        attribute :>> x = 2.0;
    }
}
