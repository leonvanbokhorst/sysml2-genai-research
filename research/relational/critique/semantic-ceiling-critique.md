# Semantic-ceiling critique: what the two pilots may and may not claim

**Role.** Semantic-ceiling critic for the relational demonstration. Issue
[#10](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/10) is used **only as an
adversarial lens** here; no #10 deliverable is claimed and #10 is not launched as a study. What
follows is one bounded critique of two pilots
([#7](../reports/issue-007-error-taxonomy-pilot.md), [#8](../reports/issue-008-validator-reliability-pilot.md)).

**Instrument for every probe:** OpenSysML CLI `sysml v0.12.1`, commit
`b2f0e9b802a334369da94312c35cefbd8726d3bf`, binary sha256
`ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0` — the same pinned binary both
pilots used (`../TOOLING.md` §1). Hash re-verified in every raw file.

**Artifacts.** 25 probe models in [`probes/`](probes/), 122 invocations in
[`raw/`](raw/) with the exact argv, timestamp, tool hash and exit status of each; run log
[`raw/RUNLOG.tsv`](raw/RUNLOG.tsv); machine-readable claim rulings in
[`CLAIMS.csv`](CLAIMS.csv) (20 rows).

---

## 1. Answer

**In one paragraph.** Both pilots understate what automated checking can establish, and they do it
in the same way: each measured *one invocation* of one tool and then named *the instrument*, *the
language*, or *the ceiling* in its conclusion. Probing the same pinned binary across its documented
modes, I found that six of the nine semantic properties the #10 premise treats as unreachable are
in fact **decided** by this tool under some invocation: requirement satisfaction, a
property-checkable invariant across schedules, contradictory assertions, type conformance of an
attribute value, unit dimensional consistency, and — as a bonus case outside the nine — a
postcondition on a run's output. A seventh (missing flow between actions) is decided as a run-time
failure when the model actually reads the missing input, and is silent otherwise. Every one of these
depends on the model *encoding* the condition as a checkable constraint or assertion with the values
it mentions bound. The binding constraint is therefore not the
language, and not "SysML v2 tooling": it is the **encoding**, the **invocation**, the **engine**, and
above all **how the verdict is read**. The sharpest instance is my own probe P08b: the same binary
returned `no violation, exhaustive … standing: holds` for an invariant its own SMT engine witnesses
as `violated at step 2`, and only `-engine all` names the disagreement. A pilot that reports
"automated validation cannot see X" is therefore usually reporting what one invocation returned; a
pilot that reports "automated validation *says* X holds" may be reporting a false verdict. #8 sets
out to establish whether a validator can serve as a measurement instrument, and on this evidence the
same scepticism has to be applied to the instrument's *verdicts* as to its *detections* — which
neither pilot did, because neither ran more than one mode.

---

## 2. Status of the propositions

| # | Proposition | Status on the evidence I gathered |
|---|---|---|
| S1 | The pinned instrument executes actions and state machines | **Established** (p01a–c, p02a–d; `-state … -advance`, `-action`; `-schedule explore` reports failing linearizations) |
| S2 | The instrument decides requirement satisfaction when the requirement carries a `require constraint` | **Established** (p03a holds / p03b violated, exit 0/1, under `-satisfy`, `-requirement`, and `-instantiate … -validate=`) |
| S3 | A prose-only requirement is reported as **holding vacuously** | **Established** (p04) — stronger than "not checked": it reads as a pass |
| S4 | A contradictory assertion pair is decided when its feature is bound, and undecided when it is not | **Established** (p07b violated exit 1; p07c `2 of 2 assertions undecided` exit 2) |
| S5 | A property-checkable invariant over an execution is decidable | **Established for the SMT engine** (p08b `violated (witnessed)`, exit 1); **the bounded `check` engine returns a false `holds`** on the same model |
| S6 | Unreachability of a state is reported as a defect | **Not established and contradicted in every mode I ran** (p01b): it is *observable* in the visited-state set but never a verdict |
| S7 | "The semantic ceiling" is a property of the language | **Not established; and the premise it rests on is misattributed** — the "executes neither actions nor state machines" sentence describes the OMG *reference implementation*, not this instrument |
| S8 | The ceiling is a property of "SysML v2 tooling" | **Not established** — one instrument, one version, and its own document set is far wider than the default path either pilot ran |
| S9 | The ceiling is a property of **the model's encoding × the invocation × the engine × the reading** | **Established for the seven properties some invocation decides, and for the two it never decides** (§4): the two undecided ones stay undecided because no property of the reachability/liveness kind is expressible, which is a fourth, separate reason. The only framing the probe evidence supports |
| S10 | B's mutants and A's codings are the ground truth for their own sensitivity figures | **Partly** — the *defect* ground truth is authored and defensible; the *detectability* ground truth is not authored, it is measured, and it moves with the encoding (§5) |

---

## 3. Capability table

Each cell names the probe file and the raw output behind it. Raw outputs are the verbatim tool
output plus the exit status; the recorded status is the tool's own, never a pipeline's.
**a** = decided (a verdict distinguishing pass from fail), **b** = checked but undecided (or decided
and reported wrongly), **c** = silently passed, **d** = not expressible in any mode I found.

| semantic property | default `-validate` | behavioural / object / property mode | class | probe → raw evidence |
|---|---|---|---|---|
| **reachability of a terminal state** | silent (c) | `-state Mission -advance 100 -engine check` prints `outcome: finalState done; visits idle, running, done`. The fact is *observable*, there is no verdict, and I found no flag that states "eventually" — the check vocabulary (`-check-property`, `-check-diverge`, `-check-assume`) is over safety conditions and values. | **c**, then **b** (observed, no verdict); reachability as a property **d** | `p01a` → `raw/p01a-state-terminal-reachable__state-advance-check.txt` |
| **an unreachable state** | silent (c) | same invocation prints `finalState running; visits idle, running` — `done` absent. Base and mutant differ **only** in that string; neither is a violation and both exit 0. | **c**; observable (**b**, no verdict), never decided | `p01b` → `…p01b…__state-advance-check.txt`, `…__state-advance-100.txt` |
| *bonus:* **no terminal state / non-termination** | silent (c) | `-schedule explore` reports `1 outcome … 1 of 1 linearization failing`, `error: … possible infinite loop`, **exit 1**. `-engine check` instead reports bounded-and-exhausted, **exit 2**. | **a** under `-schedule explore` (as an observed failure), **b** under `-engine check` | `p01c` → `…__state-advance-explore.txt`, `…__state-advance-check.txt` |
| **requirement satisfaction with a constraint** | silent (c) | `-satisfy`: `holds` (exit 0, p03a) / `fails … Required condition evaluated to false` (exit 1, p03b). `-instantiate vehicle -validate=vehicle` and `-requirement vehicleMaximumMass` agree. | **a** | `p03a`/`p03b` → `raw/p03b…__satisfy-all.txt`, `…__satisfy-json.txt`, `…__instantiate-check.txt`, `…__requirement.txt` |
| **requirement satisfaction with prose only** | silent (c) | `-satisfy`: `holds … (vacuous: requirement maxMass states no required constraint, so it holds vacuously)`, **exit 0**. The model is *false* of its own declared values (2500 against a documented 2000). | **b** — and the failure mode is worse than undecided: a passing verdict with no content | `p04` → `raw/p04-req-prose-only__satisfy-all.txt`, `…__satisfy-json.txt` |
| **missing flow between actions** | silent (c) | `-action` on the base and on the mutant both print `Results: picture = []` — **indistinguishable** (my p02a base is not a working positive control; see §8). But when the sink *reads* the missing input, execution fails: `execution failed: action Pipe: assignment to observed: multiplicity violation: 0 value(s) bound to a feature with multiplicity lower bound 1`, **exit 2**. | **c** in general; **a** (as a run-time failure) when the model's own bindings force the read | `p02a`/`p02b` → `…__action-run.txt`, `…__action-check.txt`; `p02d` → `raw/p02d-flow-unwired__action-run.txt` |
| **type conformance of an attribute value** | **error** `binding-connector-type-conformance` on all three of `Integer = 2.5`, `Positive = 5.0`, `Boolean = 1`, **exit 2** | same | **a** at the typing layer, in the default path | `p05b` → `raw/p05b-types-nonconformant__default-validate.txt` |
| **unit dimensional consistency** | **warning** `incommensurable-operands` ("MassValue (dimension M) and LengthValue (dimension L)"), **exit 0** — a gate on exit status passes it | object check emits `error: feature value vehicle.total: incommensurable units: cannot express m (metre) in kg` | **b** at the default gate, **a** under object check | `p06b` → `raw/p06b-units-incommensurable__default-validate.txt`, `…__instantiate-check.txt` |
| **contradictory assertions** | silent (c) | `-instantiate gauge -validate=gauge`: one holds, one fails — `1 of 2 assertions fails`, `standing: violated (witnessed)`, **exit 1**. With the feature **unbound**: `2 of 2 assertions undecided`, `standing: not covered`, **exit 2**. | **a** when bound; **b** when unbound | `p07b` → `…__instantiate-check.txt`, `…__instantiate-all.txt`; `p07c` → `raw/p07c-assertions-unbound__instantiate-check.txt` |
| **a property-checkable invariant** | silent (c) | `-engine smt -check-property within15`: `at step 2: constraint within15: assertion evaluated to false: x <= 15.0`, `standing: violated (witnessed)`, **exit 1**. `-engine check` on the *same model*: `no violation, exhaustive (3 states, 2 moves, depth 2)`, **`standing: holds`**, **exit 0**. `-engine all` names the conflict: `check not covered (check claimed holds (bounded) but smt witnessed violated; the interpreter's witness stands)`. | **a** under `smt`; **b, reported as a** under the default `check` engine — a false pass | `p08b` → `raw/p08b-invariant-violated__engine-smt-prop.txt`, `…__engine-check-prop.txt`, `…__engine-all-prop.txt`; base `p08a` for contrast |
| *bonus:* **a postcondition over a run's output** | silent (c) | `-analysis over`: `distance = [50.0]`, `assertion distance <= 40.0: not satisfied` — decided **per assertion** — but the case verdict is `inconclusive — the case body bound no VerdictKind value`, exit 2. | **a** per assertion; **b** at the verdict level, *because the standard requires the model to state its own verdict* | `p11` → `raw/p11-verification-case__analysis-over.txt`, `…__analysis-under.txt` |
| *bonus:* **named-constraint evaluation** | n/a | `-constraint "Fits(150.0, 100.0)"`: `Constraint … failed … violated (witnessed)`, exit 1. `-instantiate tank -constraint Fits` without arguments: `unbound parameter … not covered`, exit 2. | **a** with arguments bound; **b** without | `p10` → `raw/p10…__constraint-args.txt`, `…__constraint-on-object.txt` |

**What the table is not.** It is not a conformance statement, not a claim about the reference
implementation, and not a claim that these properties are decidable *for a generator's model*. Every
"a" cell depends on an encoding I authored. That dependence is the finding, not a caveat to it.

### 3.1 The two capability premises the pilots inherit, tested

| premise (as stated in the issue texts and `evidence/spec-tooling.md`) | true of the measured instrument? | evidence |
|---|---|---|
| "evaluates expressions but executes neither actions nor state machines" | **No.** This is true of the OMG reference implementation, which `evidence/spec-tooling.md` §3.3(f)/§5.5 correctly attributes. OpenSysML runs both. | `p01a–c`, `p02a–d`; `sysml -help` "Running behaviors: `-action`, `-state`, `-advance`" |
| "no type checking or type inference at all — so `attribute num : ScalarValues::Positive = 5.0;` is accepted" | **No** for this instrument: it is rejected at error severity. The Sensmetry sentence is about the *pilot* implementation. | `raw/p05b-types-nonconformant__default-validate.txt` (three such errors, exit 2) |
| "control-node succession rules unimplemented" (pilot) | not tested here; the reference implementation is not runnable in this environment | — (out of scope; `../TOOLING.md` §2) |

The transfer is the mechanism of both pilots' most consequential overreach: a limitation documented
of *the reference implementation* is read as a limitation of *the tool in hand*, and then of
*automated validation*.

---

## 4. The encoding-dependence finding

**The claim.** There is no single "semantic ceiling" for SysML v2. For the properties tested, what
automated validation can establish is a function of four variables, and the first dominates:

1. **Encoding.** The same intended condition yields a verdict only when the model states it as a
   `require constraint`, an `assert constraint`, a `constraint` usage, or a verification-case
   assertion — and only when the features it mentions are bound to declared values.
2. **Invocation.** `-validate` is a *diagnostics* verb. `-satisfy`, `-requirement`, `-constraint`,
   `-validate=<object>`, `-self-check`, `-state`, `-action`, `-analysis`, `-check-property` are
   *verdict* verbs. The pilots measured the first and generalised to the instrument.
3. **Engine.** `check` (bounded search), `explore`, `smt` (z3, "proved"), `solve`, `sweep`, `run`.
   Their **strength labels** — `observed`, `bounded`, `proved`, `witnessed`, `not covered` — are the
   epistemic content of the output, and they are not interchangeable.
4. **Reading.** A human or pipeline that stops at `✓ … no violation, exhaustive` and exit 0 has
   been told something false (P08b). The same output read with the `standing:` line is a bounded
   claim; read with `-engine all`, it is a *contradiction between two engines*.

**Three probes that isolate the encoding variable alone.** In each pair the models differ by one
line, and the tool's answer changes from "no information" to a decided verdict:

| pair | one-line difference | without | with |
|---|---|---|---|
| `p03a` / `p03b` | `massActual = 1500.0` → `2500.0` against `massRequired = 2000.0`, both with `require constraint` | `holds` exit 0 | `fails` exit 1 |
| `p07c` / `p07b` | `attribute reading : Real;` → `attribute reading : Real = 1.0;` | `2 of 2 assertions undecided` exit 2 | `1 of 2 assertions fails` exit 1 |
| `p02b` / `p02d` | the sink's input is *read by an assignment* rather than left as a dangling pin | `Results: picture = []`, exit 0 | `execution failed … multiplicity violation`, exit 2 |

B reached the first of these at Gate 2 and stated it well
(`reports/issue-008-validator-reliability-pilot.md:511-516`): the verdict path's reach is bounded by
what the model encodes. My probes show the same structure governs two further defect classes B
reports as undetectable, so the correct general statement is not "the ceiling is where the tool stops
looking" but **"the ceiling is where the model stops asserting"**.

### 4.1 The engine problem, which the pilots did not see because they ran one mode

Probe `p08b` is one `constraint within15 { x <= 15.0 }` inside an action with two assignments that
leave `x = 20.0`. The invariant holds initially (0 ≤ 15) and is violated at the final stable state.

```
$ sysml -action Seq -engine check -check-property within15 p08b-invariant-violated.sysml
✓ Action Seq: no violation, exhaustive (3 states, 2 moves, depth 2)
  outcome: x = 20.0
  standing: holds (bounded over schedules: 3 states, 2 moves searched)
[exit 0]

$ sysml -action Seq -engine smt -check-property within15 p08b-invariant-violated.sysml
✗ Action Seq: at step 2: constraint within15: assertion evaluated to false: x <= 15.0
  standing: violated (witnessed: inputs as written)
[exit 1]

$ sysml -action Seq -engine all -check-property within15 p08b-invariant-violated.sysml
✗ Action Seq: at step 2: constraint within15: assertion evaluated to false: x <= 15.0
  standing: violated (witnessed: inputs as written); all: check not covered
  (check claimed holds (bounded) but smt witnessed violated; the interpreter's witness stands)
[exit 1]
```

I report this as an **instrument behaviour I observed**, not as a defect report and not as a bug
claim: I have not read the source, and the output is internally inconsistent in a way I cannot
adjudicate (`exhaustive` in the prose, `bounded` in the `standing:` line). What it establishes for
this critique is enough and is independent of the cause: **a validator's negative verdict is not
self-certifying either.** #8's mandate is to establish validator reliability before validators are
used as ground truth; on this evidence the same scepticism that #8 applies to *detection* must be
applied to *verdicts*, and no pilot here did that because no pilot ran more than one mode.

---

## 5. The oracle problem

Both pilots' ground truth is authored, and it is worth separating exactly what is authored in each.

**A (issue #7).** The ground truth is A's inspection against specification constraints, with a
second coder on 12 of 18 models. What is authored is *whether a defect exists and which class it
is*. That is a defensible authored oracle for **model text**: the records cite excerpts, the codebook
carries definitions, and the corrections (16.x, 17.x) show the oracle being audited and one record
being withdrawn on the library text. So A's frequencies are claims about *A's reading of 18 model
texts*, and A says so.

But A's *detection* column is a different object. "9/14 detected" is not an authored fact about a
defect; it is a measurement of one invocation. When A writes "invisible to the instrument" it
converts a measurement into a property of the instrument. My probes show the measurement would have
been different under `-instantiate … -validate=` for at least two of the five misses' *classes*
(not the same records — I did not re-encode A's records, and I do not claim I would have). So:

- A's error **population** is an authored-oracle claim about model text, and it is the honest kind.
- A's error **detectability** is a measurement of the default path, and any word stronger than
  "the default `-validate` invocation returned nothing" outruns it.

**B (issue #8).** B's ground truth has two layers, and only the first is authored:

1. *The defect exists* — authored (`MANIFEST.csv`, pre-registered, hashed before the run). B is
   scrupulous here and refuses to let validator silence reclassify a mutant.
2. *The defect is (un)detectable* — **not** authored. B pre-registered an *expectation*, and the
   audit shows B's expectations were wrong twice (in the tool's favour). Detectability is measured.
   And the measurement is a function of the invocation set, which B fixed as `-validate` only and
   then widened, by A's objection, only for the F7 arm (A2).

So the sentence "F7 is 0/4" is true of *B's mutants under `-validate`* and false as a statement about
the defect classes, because the class label was assigned to a *shape*, and the shape's detectability
depends on how the shape is written. My P07b/P07c pair makes this concrete for the very class that
carries B's "undetermined" verdict: the instrument returns `undecided` for the F7-04 shape because
`computedMass` has no value, not because contradiction is undecidable.

**The consequence for both headlines.**

| headline | what it is actually about |
|---|---|
| A: "9/14 detected (64 %)" | *A's 14 authored records, read as text, under one invocation of one binary.* Not a property of validators, not a property of the error classes. |
| B: "23/32 = 0.72 sensitivity" | *B's 32 authored mutants, under one invocation of one binary.* Not a sensitivity of "the instrument" — the instrument decides at least 4 additional classes at other modes, and one class at another encoding. |
| B: "a pass means X, and does not mean Y" | This is the one headline that survives intact, because it is phrased about the **pass**, and a pass is exactly what the default invocation produces. |

**Where a claim depends on an oracle that does not exist.** Highest-value: the I1 record
(documentation/value contradiction). There is no automated check for "a `doc` sentence contradicts a
declared attribute value" in any mode I could find, and there is no specification constraint that
names it. Deciding it requires reading prose against numbers — an oracle that is not authored *in the
model* and cannot be authored *by the tool*. That is a genuine instance of the negative inventory the
#10 brief asks for. The connector records (R1) are *not* such an instance: they are a multiplicity
condition, A re-recorded them as `type/typing` (16.4), and the layer question is live for
adjudication.

---

## 6. Claims under test — verdicts

Every row is in [`CLAIMS.csv`](CLAIMS.csv) with source locator, evidence and residual uncertainty;
the table below is the ruling summary. `overstated` means: as printed in the report's current live
text, the claim asserts more than the retrieved evidence licenses.

| id | claim (abridged) | source | verdict |
|---|---|---|---|
| C01 | the undetected records are "outside its stated scope" because the tool "executes neither actions nor state machines" | #7 §5.3 | **overstated** — mis-attributed reference-implementation limitation |
| C02 | structural/semantic defects are "*invisible to the instrument*" | #7 §13.2 | **overstated** — true of the default path on those records only |
| C03 | the instrument "cannot" check state-machine reachability | #7 §14 | **partly supported / overstated on "cannot"** — no verdict, but observable |
| C04 | silent on 5/14 frozen records | #7 §5.1 | **supported** (reproduced) |
| C05 | "reliable detector … contradicted as a general claim" | #7 §2 P9 | **appropriately cautious** |
| C06 | "exit status is not a validity verdict" | #7 §5.2 | **supported** (independently reproduced, p07 externals) |
| C07 | a clean validation is "no evidence at all about whether the model's structure means what it claims" | #8 §1 | **overstated** — already corrected on the record by A2 |
| C08 | default path blind; verdict path decides "exactly … and **nothing more**" | #8 A2 | **supported except the "nothing more" clause** |
| C09 | P3 restated (2 of 4 F7 established) | #8 A2 | **appropriately cautious as worded** |
| C10 | `validateFeatureValueOverriding` "not enforced" | #8 §2 P4, §3.4 | **supported literally; class-level reading overstated** (site-dependent, p12) |
| C11 | "the ceiling of automated SysML v2 validation here is typing plus per-constraint well-formedness" | #8 §4.2 | **overstated** — execution, SMT invariants and verification postconditions also decide |
| C12 | "Four defect classes … are invisible" | #8 §11.5 | **overstated and internally inconsistent** with the report's own A2/A3 |
| C13 | tool gap and language gap separable only "through the specification-oracle table" | #8 §8.1 | **overstated** — a third separator exists: invocation and encoding |
| C14 | P5, conditions the specification does not name | #8 §2 P5 | **supported** (reproduced, with severity refinement) |
| C15 | "a pass means … it means nothing at all" (structural) | #8 §11.1 | **supported as a default-path claim**; ambiguous wording |
| C16 | P7, numbers not a property of "SysML v2 validators" | #8 §2 P7 | **appropriately cautious** |
| C17 | verdict path reach bounded by what generation wrote | #8 A10.5 | **supported** (reproduced) |
| C18 | both reports defer the class-level ceiling claim to #10 | both | **appropriately cautious** — credit |
| C19 | A2: a doc-only requirement returns "holds (vacuous)" | #8 A2 | **verified**, and it generalises |
| C20 | original P3: "at least one class … is invisible … Established" | #8 §2 P3 | **overstated, corrected on the record** by A2/A3 |

**Count: 8 overstated claims that need action** — C01, C02, C03, C07, C08 (the "nothing more"
clause), C11, C12, C13. **Plus 1 overstated but already corrected on the record** — C20 (the original
P3), superseded by A2/A3; it is not counted in the 8 because the correction already exists in the
same document, but it is listed so the adjudicator can rule on whether retaining it visibly is
enough.

**A note on why the "already corrected" claims still matter.** Three of the twenty sit in text a
dated addendum has superseded but not amended in place (C07 in §1, C20 in the P-table, and §11.5's
"four classes are invisible" which A2 contradicts). `PROTOCOL.md` Amendment A1 requires the original
text to stay visible, which is right; the consequence is that the report now contains both the
corrected and the uncorrected form of the same claim, and the uncorrected form is the one in the
headline position. That is a presentation defect with an evidentiary consequence, and it is the
single easiest thing for the Lead to fix without touching any researcher's evidence.

### 6.1 Credit where it is due

These are not rhetorical concessions; they are the parts of both pilots that the probe evidence
strengthens:

- **#8's severity-as-a-measurable-property result** (§11.3) and the exit-status finding are the most
  useful results in either pilot. My external re-runs reproduce both (`a-probe07` exit 0 with an
  error-severity diagnostic; exit 2 under `-strict`).
- **#7's "exit status is not a validity verdict"** and its separation of wrapper / notation /
  resolution / semantics survive every probe I ran.
- **#8's P6 refusal** — declining to make the literature claim its own design cannot support — is
  exemplary, and its A10.3 report that the external set *does not* support P6 is the kind of
  self-defeating disclosure that makes the rest of the report credible.
- **#7's §17.1 withdrawal** of a record on the normative library text, against its own interest in
  the rate, is the strongest single act of discipline in the run.
- Both reports' `P`-tables already say most of what I say here about scope; the overreach is
  concentrated in the prose *implications* sections, which is where readers and citations go.

---

## 7. What a generation-evaluation study may claim today

> A generation-evaluation study may today claim, honestly, that a generated SysML v2 model is
> *expressible* (it parses and resolves under a named tool version), *well-formed* against the
> constraints that tool implements, and — where the model itself states a machine-checkable
> condition and binds the values it mentions — *true or false of its own declarations*, as decided by
> a named invocation of a named engine at a named strength. It may claim per-condition verdicts with
> their strength labels (`observed`, `bounded`, `proved`, `witnessed`, `not covered`, or
> `vacuous`), and it must report the encoding it relied on, because the same intended condition
> that is `violated` under `-satisfy` is invisible to `-validate` and *vacuously true* if written as
> prose. It may **not** claim that a validated model is adequate, complete, behaviourally correct, or
> that a clean run is a semantic pass; it may **not** claim that a condition is beyond automated
> checking, because for that condition some invocation of the same pinned binary reaches a verdict
> — and it may **not** treat the tool's own verdict as self-certifying
> either, because on probe P08b the bounded engine asserted `holds` for an invariant the SMT engine
> witnessed as violated, and only a third invocation revealed the disagreement. The defensible
> headline for this project is therefore not a validity percentage and not a ceiling, but a
> **conditional**: *"under invocation I and engine E, with condition C authored into the model and
> values bound, N of M generated models were decided, and K were decided against"* — with the
> construct census showing how rarely C appears in generated text at all (0 of 18 in A's corpus for
> `require constraint`). Two caveats belong in the same sentence: three of the nine properties are
> **not** decided by any invocation I found (terminal reachability and unreachability: no expressible
> property, only an observable trace; a prose-only requirement: reported as `holds … vacuous`), and
> the construct census above is the number that decides whether the rest is reachable in practice.
> Everything stronger than that conditional is currently a claim about the invocation, the engine or
> the reading, not about the model.

---

## 8. What I could not establish, and why

1. **Whether reachability/liveness is expressible at all.** I found no flag that states an
   *eventual* property; `-check-property` evaluates a condition at every stable state. `-check-property
   Mission::done` is refused as `unresolved reference`. This is "not established", not "not
   expressible": I read `-help` and the man page, not the source.
2. **Why the bounded `check` engine reports `holds` on P08b.** The output contradicts itself
   (`exhaustive` in prose, `bounded` in `standing:`). I did not read the implementation, so I claim
   the observation, not a cause. It is not a bug report and should not be filed as one.
3. **Whether my p02a "base" is a valid positive control.** It is not: with `scene` unbound, both
   base and mutant yield `Results: picture = []`, so the pair does not discriminate and I do not use
   it to claim the tool is blind to missing flow. P02d replaces the pair with a case where the
   consequence is forced, and that one does discriminate (`execution failed … multiplicity
   violation`). I record the failed control rather than dropping it.
4. **Whether the encoding dependence holds on the reference implementation or Syside.** The pilot is
   not runnable here (no JVM, no CLI artefact) and Syside requires a licence — both are access
   boundaries, not obstacles to route around (`../TOOLING.md` §2, §3). So every statement about
   "SysML v2 tooling" in this critique is really "this instrument".
5. **Whether B's F5-01 mutant violates the constraint at all.** My p12 shows the binary *has* a
   `feature-value-overriding` diagnostic that fires where the redefined feature carries a fixed
   binding. Whether that makes B's case "site-dependent enforcement" or "a mutant that does not
   violate the constraint" is a mutant-validity question that belongs to reviewer-b and adjudication.
   I state both readings and choose neither.
6. **A verification-case *verdict*.** P11 decides the postcondition per assertion but the case verdict
   is `inconclusive — the case body bound no VerdictKind value`. Whether a `VerdictKind` binding
   would make the case decide is a one-line experiment I did not run; it is the natural follow-up and
   the honest status is "not established".
7. **`-strict` beyond one probe.** I ran it only on A's `probe07` (exit 0 → exit 2). Whether
   `-strict` converts any of my "b"/"c" cells into "a" is untested.
8. **Construct frequencies.** I did not census how often generated models contain the encodings that
   make these verdicts reachable; B measured 0/18 for `require constraint` in A's corpus and I did
   not independently verify that count. That census, not another capability probe, is what decides
   whether the encoding-dependence finding matters *in practice*.

---

## 9. Dead ends and things that did not work

All but the last of these are preserved as raw output rather than described from memory.

- **`-check-property` naming a state** (i.e. trying to make reachability a property): refused.
  `-state Mission -advance 10 -engine check -check-property Mission::done` → `sysml: unresolved
  reference: Mission::done`, exit 2 — `raw/p13-dead-ends__check-property-on-a-state.txt`. Without
  `-engine` selected the flags are refused outright: `… are the check and smt engines'; select one`,
  exit 2 — `raw/p13-dead-ends__check-property-no-engine.txt`.
- **`-observe` without `-runs`**: `sysml: -observe names what -runs reports; ask for the runs, as
  -runs <number>`, exit 2 — `raw/p13-dead-ends__observe-without-runs.txt`. Not pursued.
- **`-instantiate tank -constraint Fits`** without arguments for the `in` parameters: `unbound
  parameter: constraint Fits parameter "level" has no argument and no default`, `standing: not
  covered`, exit 2 — `raw/p13-dead-ends__constraint-without-args.txt` and
  `raw/p10-constraint-and-invariant__constraint-on-object.txt`. A subject does not bind `in`
  parameters; only arguments do.
- **`-analysis "StopCheck(20.0)"`** (subject passed as an argument): `calc argument count mismatch:
  verification P11::StopCheck takes 0 argument(s), got 1`, exit 2 —
  `raw/p11-verification-case__analysis-arg-form.txt`. The subject is bound by an object, not an
  argument; the working form is `-analysis over`.
- **Binding a constraint's `in` parameters to a running action's features** so that
  `-check-property` could evaluate it. Four exploratory models were tried before the working form;
  **their transcripts were not preserved** (they were superseded during probe design and deleted, a
  real degradation of this critique's own audit trail). What they exhibited is preserved indirectly:
  the "unbound parameter" refusal is in the two constraint raw files above, and the working form —
  a `constraint` usage lexically inside the action — is `p08`.

---

## 10. Implications for the main question

1. **"Validate the generated model" is an under-specified instruction**, and the pilot evidence
   shows the spread is not marginal: the same 18 models in A's corpus sit at 0/18, 6/18 or 12/18
   valid depending on extraction and gate (A §13, item 1), and the same defect class in my probes flips
   between silent and decided depending on encoding and mode. An evaluation framework must fix the
   invocation and the encoding, not just the tool version.
2. **The negative inventory is real but it is not where the pilots put it.** The instance that
   survives is *prose against numbers* (I1) — an oracle that cannot be authored inside the model and
   that no mode decides. Unreachability survives as "no verdict, but observable". Missing flow,
   contradictory assertions, dimensionally-impossible sums and violated requirements do **not**
   survive: they are decided under some encoding.
3. **#8's central framing needs one more axis.** A validator's reliability is not a single
   sensitivity number; it is a *verdict-surface* profile — which invocation, which engine, which
   strength label, and whether its `holds` is trustworthy. My P08b is a one-model demonstration that
   the last question is open, and it is the question that matters most for anyone who plans to gate
   on a validator.
4. **The literature's "semantic F1" numbers and this project's validator passes are measured on
   different objects.** A parse-or-validate rate is not a weaker measure of the same thing as a
   semantic score; on this evidence it is a measure of a different property. That is a sharper and
   more defensible claim than "the ceiling is low", because it does not require knowing where the
   ceiling is.

---

## 11. Adjacent questions noticed and not researched

1. **A tool-by-tool mode register** (reference implementation / OpenSysML / Syside): which verdict
   verbs exist in each, and whether the same encoding dependence holds. This is #2's and #10's
   territory; Syside is licence-blocked and the pilot is not runnable here.
2. **Whether the `-engine check` false-`holds` is systematic.** One probe is not a rate. A small
   mutant family over invariants would measure it — that is a #8-shaped study of a *verdict* engine
   rather than a diagnostics engine.
3. **The construct census that decides practical relevance**: how often generated models contain a
   `require constraint`, an `assert constraint`, a bound value, or a readable flow. B measured 0/18
   once; a ≥200-model census is #7's stated requirement and would convert my "encoding matters" into
   a number.
4. **Whether a `VerdictKind` binding makes verification cases decide** (§8.6). One line, separate
   bounded study.
5. **Human review of `-check` vs `-smt` disagreements** by a systems engineer: does a reviewer given
   `standing: holds (bounded …)` and exit 0 accept it? That is #14's warning-presentation question
   with a much stronger stimulus than B's F3-01.
6. **A second implementation** for any of these nine cells. Nothing here replicates; that is the
   limitation and #8 already names it.

---

## 12. Sources

**Instrument.** OpenSysML CLI `sysml v0.12.1`, commit `b2f0e9b8…`, binary sha256 `ddfc2962…1598f0`,
`.tools/sysml`; `-help` and `-man` read in full for the capability inventory; `-engines` run to list
engine authority/status (`check`, `explore`, `run`, `smt`, `solve`, `sweep`, `tool:fmi`; z3 at
`/opt/homebrew/bin/z3`).

**This critique's own evidence (primary).**
- `research/relational/critique/probes/*.sysml` — 25 probe models (p00 pre-flight, p01–p13).
- `research/relational/critique/probes/run-probes.sh` — the runner; records argv, UTC timestamp,
  tool version, tool hash, model hash, verbatim output and the tool's own exit status per invocation.
- `research/relational/critique/raw/*.txt` — 122 raw outputs, unedited.
- `research/relational/critique/raw/RUNLOG.tsv` — 122 rows, one per invocation.
- `research/relational/critique/CLAIMS.csv` — 20 claim rulings.

**Others' artifacts, read only (never edited).**
- `reports/issue-007-error-taxonomy-pilot.md` (§1, §2, §5, §13, §14, §16, §17);
  `research/issue-007/detection/probes/probe01…`, `probe07…` (re-run);
  `research/issue-007/METHODOLOGY-FROZEN.md`.
- `reports/issue-008-validator-reliability-pilot.md` (all, esp. §1, §2, §3.4, §4.2, §8, §11, §12,
  A1–A10); `research/issue-008/mutants/M31-F5-01…` and `known-good/KG-04-featurevalues.sysml`
  (re-run read-only); `research/issue-008/empirical/REPORT.md`.
- `research/relational/cross-reviews/{A-reviews-B,B-reviews-A,A-response-to-B-review,B-response-to-A-review}.md`.
- `research/relational/PROTOCOL.md`, `gate-log.md`, `TOOLING.md`;
  `research/relational/empirical-subset/FROZEN-SUBSET.md`.
- `evidence/spec-tooling.md` §3.3, §5.5, §6.
- Issues #7, #8, #10 (retrieved with `gh issue view`).

**Nothing in this critique is cited from memory.** Where a claim rests on a file, the file and
section are named; where it rests on a run, the raw file is named.
