# KG-09-actions — provenance and validity argument

**Independence type:** S (specification example), with one one-token deviation that is itself a finding.
**Source:** SysML 2.0 Part 1, `formal/2026-03-02`, §7.17.2, p.99.

**Quoted verbatim.**
```
action def TakePicture {
    in scene : Scene;
    out picture : Picture;
    bind focus.scene = scene;
    action focus : Focus { in scene; out image; }
    first focus then shoot;
    flow focus.image to shoot.image;
    action shoot : Shoot { in image; out picture; }
    bind picture = focus.picture;
}
```
**Supplied by the author.** `item def Scene;`, `item def Picture;`, `action def Focus { in scene :
Scene; out image : Picture; }`, `action def Shoot { in image : Picture; out picture : Picture; }`.
The fragment names all four types and declares none of them.

**Deviation, recorded as a finding.** The last line of the source excerpt reads
`bind picture = focus.picture;`, but `focus` is declared in the line above as
`action focus : Focus { in scene; out image; }` — **`focus` has no feature `picture`**, so the
specification's own example does not resolve against its own declarations. Substituting `image` for
`picture` is the only reading under which the example is coherent (`picture` is `TakePicture`'s out
parameter, and the intent is plainly to bind it to `focus`'s output). The model therefore reads
`bind picture = focus.image;` and the deviation is one token. **This is a defect in the specification
text, not in the model**, and it is reported in the pilot report as an incidental observation about
the source material. Triage record: category (i) at first run — a genuine unresolved reference in the
source excerpt.

**Why the repaired model is believed valid.**
1. §7.17.2: "Any directed features declared in the body of an action definition or usage are
   considered to be owned parameters." `in scene`, `out picture` are the parameters; the subactions'
   `in scene`, `out image` etc. likewise. Satisfied.
2. §7.17.2: "If an action definition has a single superclassification … may declare fewer owned
   parameters". No superclassification is declared, so no parameter-redefinition obligation arises.
3. `bind focus.scene = scene;` binds an input parameter of a subaction to an input parameter of the
   enclosing action — both are features of the enclosing action's featuring type. KerML
   `checkConnectorTypeFeaturing` satisfiable.
4. `first focus then shoot;` — a succession between two action nodes (§7.17.4); both ends are
   `ActionUsage`s, so the control-node and `endpoint-not-a-node` conditions do not apply.
5. `flow focus.image to shoot.image;` — both ends name features of the two subactions and are
   compatible item types (`Picture`). §7.16 flow end subsetting is satisfied because the flow's ends
   are the named features themselves.

**Author's uncertainty.** `bind focus.scene = scene` refers to a feature of `focus` before `focus` is
declared; SysML's namespace rules make this legal in principle (members are visible throughout the
body), and both `bind` lines are in the specification as printed. The ordering is preserved verbatim.

## Author-supplied addition: the control-node example of §7.17.3

`action def ConcurrencyExample { … }` is quoted **verbatim** from §7.17.3, Table 16 commentary
(p.101) — fork / join / decide / merge with the specification's own successions. It was added as the
base for the control-node mutant (F5-03) and it exercises rules 1–4 of §7.17.3, which the
specification says "shall be enforced in the abstract syntax".

**Why it is believed well-formed.** `fork1` has one incoming (none — a fork with no incoming
succession is not constrained) and two outgoing, which rule 4 permits ("Outgoing successions from a
fork node must have target multiplicity 1..1"). `join1` has two incoming and one outgoing (rule 3 is
about *source* multiplicity, satisfied). `decision1` has exactly one incoming (the catalogue's
`validateDecisionNodeIncomingSuccessions`, §8.3.17.7: "A DecisionNode may have at most one incoming
Succession") and two outgoing with target multiplicity 0..1 (rule 2). `merge1` has two incoming with
source multiplicity 0..1 (rule 1). Control nodes are only declared inside an action body (§7.17.3),
which they are.
