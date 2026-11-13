package P {
    private import ScalarValues::*;
    state def S {
        state idle;
        state run;
        transition from idle to run on trigger;
    }
}
