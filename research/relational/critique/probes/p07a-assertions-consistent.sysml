// P07a — two assertions about the same bound feature that agree.
// Property under test: contradictory assertions.
package P07A {
    private import ScalarValues::*;

    part gauge {
        attribute reading : Real = 1.0;
        assert constraint { reading > 0.0 }
        assert constraint { reading < 5.0 }
    }
}
