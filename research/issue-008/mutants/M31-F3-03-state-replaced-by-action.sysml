// Clause 7.18.3 (SysML 2.0 Part 1, formal/2026-03-02, p.118), example verbatim.
// Provenance: KG-06-transitions.PROVENANCE.md
package KG06Transitions {
    private import ScalarValues::*;

    state def OnOff1 {
        entry;
        then off;

        state off;
        action on;

        transition off_on first off then on;
        transition on_off first on then off;
    }
}
