// P07c — the same contradictory pair, but `reading` has NO value in the model.
// This isolates whether "undecided" is caused by the contradiction or by the absence of a value:
// B's F7-04 returned "undecided" and this variant is the mechanism hypothesis.
// Property under test: contradictory assertions (unbound-value variant).
package P07C {
    private import ScalarValues::*;

    part gauge {
        attribute reading : Real;
        assert constraint { reading > 0.0 }
        assert constraint { reading < 0.0 }
    }
}
