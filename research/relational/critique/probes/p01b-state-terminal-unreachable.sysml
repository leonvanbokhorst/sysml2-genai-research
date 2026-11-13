// P01b — the same machine with one succession removed, so `done` is never entered.
// Property under test: an unreachable state (here: an unreachable terminal state).
package P01B {
    state def Mission {
        entry action initial;
        then idle;

        state idle;
        state running;
        state done;

        first idle then running;
    }
}
