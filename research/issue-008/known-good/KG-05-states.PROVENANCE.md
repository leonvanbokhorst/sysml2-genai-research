# KG-05-states — provenance and validity argument

**Independence type:** S (specification example).
**Source:** SysML 2.0 Part 1, `formal/2026-03-02`, §7.18.2, pp.117-118.

**Quoted verbatim.**
```
state def OperationalStates {
    entry action initial;
    then off;
    state off;
    state starting;
    state on;
}
```
**Supplied by the author.** Package wrapper and the (inert) scalar-values import.

**Why it is believed valid.**
1. §7.18.2: "entry, do and exit actions can be declared (at most one of each)". One `entry` action.
   Satisfied.
2. §7.18.2: "A shorthand may also be used for a succession whose source is the entry action,
   consisting of the keyword then followed by a qualified name … placed immediately after the entry
   action declaration". `then off;` is that shorthand; `off` is declared in the same body. Satisfied.
3. Substate usages are exclusive by default (§7.18.2); no transition is declared between them, so
   `validateTransitionUsageTriggerActions` and the control-node constraints do not apply.
4. `state starting;` is legal even though no succession reaches it — **no constraint in the
   623-row catalogue names reachability.** This is deliberate: the same construct is the base for
   mutant F7-01, so the base itself demonstrates that the construct is legal under the
   specification's own constraints. It is a legitimate SysML v2 model and a questionable engineering
   model simultaneously, which is the point of F7.

## Author-supplied addition (added after the corpus was first validated)

The two successions `first off then starting;` and `first starting then on;` are **authored**, not in
the clause example. The clause's fragment leaves `starting` and `on` unreachable, which would make
the base itself instantiate the F7-01 defect. Completing the machine makes the base an ordinary
model and lets F7-01 be a single-line deletion.

**Why the addition is believed well-formed.** §7.17.4/§7.13.5: a succession between two state
usages in the same body; both ends name declared states, so no control-node rule applies.
No constraint in the catalogue is engaged by adding a succession whose endpoints are vertices of the
same state machine.
