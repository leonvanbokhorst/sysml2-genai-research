// P13 — a container for the invocation forms the critique reports as dead ends, so that their
// raw output is preserved rather than described from memory:
//   * -check-property naming a STATE (reachability is not a property name)
//   * -observe without -runs
//   * -constraint on an object without arguments for its `in` parameters
package P13 {
    private import ScalarValues::*;

    state def Mission {
        entry action initial;
        then idle;
        state idle;
        state done;
        first idle then done;
    }

    action def Fill {
        attribute level : Real = 0.0;
        action add { assign level := 5.0; }
    }

    part tank {
        attribute level : Real = 150.0;
        attribute capacity : Real = 100.0;
    }

    constraint Fits {
        in level : Real;
        in capacity : Real;
        level <= capacity
    }
}
