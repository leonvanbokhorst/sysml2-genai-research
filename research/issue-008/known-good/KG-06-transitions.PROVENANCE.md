# KG-06-transitions — provenance and validity argument

**Independence type:** S (specification example).
**Source:** SysML 2.0 Part 1, `formal/2026-03-02`, §7.18.3, p.118.

**Quoted verbatim.**
```
state def OnOff1 {
    entry;
    then off;
    state off;
    state on;
    transition off_on first off then on;
    transition on_off first on then off;
}
```
**Supplied by the author.** Package wrapper and inert scalar-values import.

**Why it is believed valid.**
1. §7.18.3: a transition usage relates "a source state usage to a target state usage"; both
   transitions name declared states in the same body. Satisfied.
2. `entry;` is the "empty entry action" shorthand of §7.18.2; `then off;` follows it. Satisfied.
3. §7.18.3 and `validateTransitionUsageTriggerActions` (SysML §8.3.21.10 context —
   catalogue row `validateTransitionUsageTriggerActions`, §8.3.18.9): a transition whose source is a
   state usage may have trigger actions; these have none, which is trivially compliant.
4. Transitions here are between the direct substates of a *non-parallel* state, so
   `parallel-state-transition` is not engaged.
5. No guard expressions, so `validateTransitionFeatureMembershipGuardExpression` does not apply.
