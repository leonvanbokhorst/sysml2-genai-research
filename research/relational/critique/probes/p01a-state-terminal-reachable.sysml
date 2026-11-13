// P01a — base model: every state reachable; terminal `done` reachable in two moves.
// Property under test: reachability of a terminal state.
package P01A {
    state def Mission {
        entry action initial;
        then idle;

        state idle;
        state running;
        state done;

        first idle then running;
        first running then done;
    }
}
