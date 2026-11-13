// P10 — a named constraint def evaluated directly, with an object as subject, and a
// property-style invariant expressed as `assert constraint` on a part.
// Property under test: (a) `-constraint` evaluation as a decided verdict surface;
// (b) whether an invariant on a part is decided by the default path or only by object mode.
package P10 {
    private import ScalarValues::*;

    part tank {
        attribute level : Real = 150.0;
        attribute capacity : Real = 100.0;
    }

    constraint Fits {
        in level : Real;
        in capacity : Real;
        level <= capacity
    }

    part guardedTank {
        attribute level : Real = 150.0;
        attribute capacity : Real = 100.0;
        assert constraint { level <= capacity }
    }
}
