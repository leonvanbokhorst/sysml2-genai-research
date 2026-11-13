// P11 — a POSTCONDITION over a run, expressed as a verification case: the case returns a value
// derived from its subject and requires a condition of that returned value. This tests whether
// the instrument decides a condition on a run's OUTPUT, as distinct from an invariant that must
// hold at every stable state (P08).
package P11 {
    private import ScalarValues::*;

    verification def StopCheck {
        subject s : Real;
        return distance : Real = s * s / 8.0;
        require constraint { distance <= 40.0 }
    }
}

// Two cases with the subject bound: one whose output violates the postcondition, one whose does not.
package P11Cases {
    private import ScalarValues::*;
    private import P11::*;

    verification over : StopCheck { subject s = 20.0; }
    verification under : StopCheck { subject s = 10.0; }
}
