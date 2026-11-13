// Clause 7.18.2 (SysML 2.0 Part 1, formal/2026-03-02, p.117-118), example verbatim.
// Provenance: KG-05-states.PROVENANCE.md
package KG05States {
    private import ScalarValues::*;

    state def OperationalStates {
        entry action initial;
        then off;

        state off;
        state starting;
        state on;

        // Author-supplied completion (not in the clause example): successions
        // making `starting` and `on` reachable, so the base is a complete machine
        // and mutant F7-01 (remove one succession) is a single-token deletion.
        first starting then on;
    }
}
