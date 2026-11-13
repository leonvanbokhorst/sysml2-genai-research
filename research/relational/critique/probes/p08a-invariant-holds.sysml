// P08a — an action invariant that holds at every stable state. `x` ends at 5.0, limit is 15.0.
// Property under test: a property-checkable invariant over an execution.
package P08A {
    private import ScalarValues::*;

    action def Seq {
        attribute x : Real = 0.0;
        constraint within15 { x <= 15.0 }

        action set1 { assign x := 5.0; }

        first set1 then set2;
        action set2 { assign x := 5.0; }
    }
}
