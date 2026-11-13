// P08b — the same action with one assignment changed, so the invariant `x <= 15.0` holds at the
// initial state (x = 0.0) and is violated at the final stable state (x = 20.0).
// Property under test: a property-checkable invariant over an execution.
// This is the probe behind the critique's central capability finding: the invariant is DECIDABLE,
// but the bounded `check` engine reports it as holding while the `smt` engine witnesses the
// violation, and only `-engine all` reports the disagreement.
package P08B {
    private import ScalarValues::*;

    action def Seq {
        attribute x : Real = 0.0;
        constraint within15 { x <= 15.0 }

        action set1 { assign x := 5.0; }

        first set1 then set2;
        action set2 { assign x := 20.0; }
    }
}
