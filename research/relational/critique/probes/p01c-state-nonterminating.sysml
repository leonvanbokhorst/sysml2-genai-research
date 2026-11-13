// P01c — a machine with no terminal state: `running` re-enters itself forever.
// Property under test: does the instrument distinguish "no terminal state" from "terminal state
// present but unreachable", and does it report either as a defect?
package P01C {
    state def Mission {
        entry action initial;
        then idle;

        state idle;
        state running;

        first idle then running;
        first running then running;
    }
}
