// P07b — two assertions about the same BOUND feature that cannot both hold, with `reading` given
// a concrete value (1.0). This is B's F7-04 shape with the value bound; F7-04 left `computedMass`
// unbound, which is why the instrument returned "undecided" there.
// Property under test: contradictory assertions.
package P07B {
    private import ScalarValues::*;

    part gauge {
        attribute reading : Real = 1.0;
        assert constraint { reading > 0.0 }
        assert constraint { reading < 0.0 }
    }
}
