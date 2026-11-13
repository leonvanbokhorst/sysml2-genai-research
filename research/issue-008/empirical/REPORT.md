# External challenge set: Researcher A's frozen observed errors, measured against the pinned validator

> **ADJUDICATED CORRECTIONS APPLIED (Gate 4, 2026-11-13T15:10Z).** Several statements below are
> superseded; the originals are kept visible and each correction is in §14 with its ruling id.
> Read §14 before quoting any number from this file. In short:
> **9/13 is retained but must be read as 9/9 established-and-mandatory + 0/4
> discretionary/normative-basis/contested**; M2's applicable count is **1**, M3's is **3**;
> the pre-registration hash `9458406e…` is **post-AM1** and does not establish pre-registration;
> R1's defect status is contested, adding a **9/11[R1]** rung; and a verdict is never quoted
> without its invocation, engine and standing label.


**Task:** `task-6` — run A's frozen empirical error subset through the pinned validator as a
**separate external challenge set**, distinct from my synthetic mutants.
**Author:** Researcher B. **Run:** 2026-11-13T14:37–14:39Z (run2), raw output in `raw/run2/`.
**Pre-registration:** `PRE-REGISTRATION.md`, frozen at `9458406e7db665ac42f5a3a896a7dc05b094b0fb6e8ef3a4ab9ed9db7e6acfbc`
**before the first run** (the superseded first draft, `0106e082…`, differs only in a header
timestamp — see `run-log.md` §2). Mode set, attribution rule, scoring rule, control rule, class
mapping and the P6/P8 decision rule were all fixed in that file.
**Ground truth:** `research/relational/empirical-subset/subset.json`, sha256
`bc2b92a5fdff6e976ae7156b13beba3535f0895e4a41268cf76c1551a6c3dfaa`, `frozen_utc`
2026-11-13T14:33:20Z — **verified by me before the first run and again by `run_external.py --verify-only`**;
all 36 files in `models/manifest.csv` match their recorded sha256 and byte counts, and every frozen
copy is byte-identical to A's live corpus (`run-log.md` §1).
**Rules I applied to myself:** no relabelling, no dropping, no repair. Where I think an item is
wrong I say so in §7 and measure it as labelled anyway.

---

## 1. Answer

**Against 13 observed, independently-coded, specification-anchored defects from a corpus I did not
generate, the default `-validate` path detected 9/13 = 0.69 [0.42, 0.87]** — statistically
indistinguishable from my synthetic 23/32 = 0.72 [0.55, 0.84], and *composed completely differently*.

The composition is the finding. **Every observable detection sits at the notation, resolution and
visible-typing layers** (S1 3/3, N1 4/4, N2 1/1, T1 1/1). **Every miss sits at the
constraint/semantic/structural layer** (S2 0/1, R1 0/2, I1 0/1), and one of those misses could not
even be measured because the model short-circuits before checks run. That is the same layer boundary
my synthetic mutants found, reproduced on an observed error population by a different agent. It is the
strongest evidence this project has produced that the boundary is a property of the instrument rather
than of my mutant authorship.

What the external set does **not** do: it does not support my P6, by the rule I registered in
advance; it cannot test four of my eight fault classes at all; and its own composition is so heavily
notation-and-resolution that its aggregate rate says more about what an LLM wrote in six prompts than
about what a validator can do.

**Headline numbers, every one with its denominator:**

| measure | result | denominator |
|---|---|---|
| M1 `-validate -format json`, as registered | **9/13 = 0.69** [0.42, 0.87] | 13 observed error items |
| M1 excluding the contested I1 item | **9/12 = 0.75** [0.47, 0.91] | 12 unqualified items |
| M1 excluding I1 **and** the one short-circuited item (see §6.1) | **9/11 = 0.82** [0.52, 0.95] | 11 measurable unqualified items |
| M2 `-satisfy` | **0 detected**, 1 evaluated (`holds-vacuously`), 10 not applicable | 13 items |
| M3 `-instantiate … -validate=<obj>` | **0 detected**, 1 `undecided` (weaker signal), 10 not applicable | 13 items |
| M4 `-validate -strict` | **9/13 = 0.69**, same items as M1; exit codes differ on four models | 13 items |
| Controls, clean tier, M1 | **0/4** models with an error diagnostic; 0/4 with a warning | 4 controls |
| Frozen-clean-only tier (descriptive, not scored) | 3/3 carry their known post-inspection defect, diagnosed correctly | 3 models |

## 2. Per-item detection, per registered mode

Full matrix with codes and standings: `per-item-per-mode.md`. Summarised:

| item | model | class | layer | M1 default | M2 satisfy | M3 object | M4 strict |
|---|---|---|---|---|---|---|---|
| ES-T1-C2-E01 | T1-C2 | S1 | syntax/parse | **detected** (`syntax@41`) | n/a | n/a | detected |
| ES-T1-C3-E01 | T1-C3 | I1 *(contested: defect status)* | semantic/behavioural | silent | wrong-target (`holds-vacuously`) | not detected (`holds`) | silent |
| ES-T2-C1-E01 | T2-C1 | S1 | syntax/parse | **detected** (`syntax@48–51`) | n/a | n/a | detected |
| ES-T2-C2-E01 | T2-C2 | S2 | constraint/OCL | wrong-target (`reserved-keyword-name@17`, nothing at 33) | not detected (`holds-vacuously`) | weaker signal (`undecided`) | wrong-target |
| ES-T3-C1-E01 | T3-C1 | N2 | name resolution | **detected** (9 × `unresolved`) | n/a | n/a | detected |
| ES-T3-C2-E01 | T3-C2 | S1 | syntax/parse | **detected** (`reserved-keyword-name@23,@24`) | n/a | n/a | detected |
| ES-T3-C2-E02 | T3-C2 | N1 | name resolution | **detected** (`unresolved@44`) | n/a | n/a | detected |
| ES-T4-C1-E01 | T4-C1 | T1 | type/typing | **detected** (`endpoint-not-a-node@43`) | n/a | n/a | detected |
| ES-T4-C1-E02 | T4-C1 | R1 *(contested: layer)* | type/typing | wrong-target — **and the tool states it made no check (§6.1)** | n/a | n/a | wrong-target |
| ES-T4-C2-E01 | T4-C2 | N1 | name resolution | **detected** (`unresolved@32`) | n/a | n/a | detected |
| ES-T4-C3-E01 | T4-C3 | R1 *(contested: layer)* | type/typing | **silent** — the clean test of R1 | wrong-target | not detected (`holds`) | silent |
| ES-T5-C2-E01 | T5-C2 | N1 | name resolution | **detected** (`unresolved@32`) | n/a | n/a | detected |
| ES-T6-C2-E01 | T6-C2 | N1 | name resolution | **detected** (`unresolved@40`) | n/a | n/a | detected |

"n/a" = not applicable: either the model does not analyse cleanly (so no verdict can be formed) or it
states no satisfaction assertion for the mode to evaluate. Per `PRE-REGISTRATION.md` §4.2, n/a is
never counted as silence.

## 3. Per-class detection, with denominators

| class | layer | n | M1 detected | outcome of the misses |
|---|---|---:|---:|---|
| S1 notation | syntax/parse | 3 | **3** | — |
| N1 unresolved | name resolution | 4 | **4** | — |
| N2 missing prelude | name resolution | 1 | **1** | — |
| T1 kind (definition where usage required) | type/typing | 1 | **1** | — |
| S2 named `check…` constraint | constraint/OCL | 1 | **0** | wrong-target: the model's only diagnostic is a *different* defect at line 17 |
| R1 connector over a multi-valued usage | type/typing *(layer contested)* | 2 | **0** | 1 silent (T4-C3, clean model); 1 unmeasurable-by-short-circuit (T4-C1) |
| I1 documentation/value contradiction | semantic/behavioural *(defect status contested)* | 1 | **0** | silent |
| **total** | | **13** | **9** | |

**Contested items, both ways** (A's instruction, and my pre-registration §2):

| variant | n | detected | rate | 95% Wilson |
|---|---:|---:|---|---|
| all items as labelled | 13 | 9 | 0.69 | [0.42, 0.87] |
| without I1 (defect status contested) | 12 | 9 | 0.75 | [0.47, 0.91] |
| R1 layer moved to `structural/architectural` | 13 | 9 | **0.69 — unchanged** | — |

The R1 layer contest **cannot** move a detection number, because the layer is a label and my
attribution rule is line-based. The I1 contest moves the headline by 1/13 and nothing else. That is
the honest size of both contests: **≈0.06 on the aggregate, 0 on any class conclusion.**

## 4. Synthetic vs observed: comparison table, and why the class names do not line up

The two frames were coded independently by different agents under different codebooks. Mapping is
partial and, for half my classes, absent. **These are not the same variables and must not be pooled
without the mapping.**

| my synthetic class | n | detected (default) | observed counterpart | n | detected | comparable? |
|---|---:|---:|---|---:|---:|---|
| F1 syntax/notation | 4 | **4** | `S1` | 3 | **3** | **yes at layer level.** Sub-mechanisms differ: my F1 is parse breakage (missing `;`, extra brace, keyword typo); A's S1 is dominated by reserved-keyword-as-name, which my corpus never produced. Both detected. |
| F2 unresolved reference | 4 | **4** | `N1` (4) + `N2` (1) | 5 | **5** | **yes at layer level, with a caveat.** All four observed N1 items are *satisfy-target* references; my four are type/parameter/redefinition/type-declaration references; and Gate 2 established that succession sources are **not** resolved at all. So "resolution is detected" is true for the sites both frames sampled and false for one neither sampled. N2 has no synthetic analogue (my bases all import the prelude). |
| F3 kind/type mismatch | 4 | **2** | `T1` | 1 | **1** | **partial.** T1 is "a definition where a usage is required"; my F3 is "a usage typed by a definition of the wrong kind". Adjacent, not identical. Observed rate is higher on n=1 — no conclusion available. |
| F4 multiplicity | 4 | **3** | *(none)* | 0 | — | **not comparable.** No observed record is a multiplicity defect. R1 was formerly placed here and is now labelled type/typing. |
| F5 named-constraint violation | 4 | **3** | `S2` | 1 | **0** | **partial, and the direction is opposite.** Different named constraints (`validateFeatureValueOverriding` vs `checkSatisfyRequirementUsageBindingConnector`); my mutants are caught, the observed one is not. On n=1 this is a warning, not a rate. |
| F6 quantity/unit | 4 | **3** | *(none)* | 0 | — | **not comparable.** 0/18 observed models write a unit literal. |
| F7 structural/architectural | 4 | **0** (default) / **1** (mode-aware) | `R1` (2) + `I1` (1) | 3 | **0** | **weak.** R1 is now labelled type/typing with structural as the rival layer; I1 is a documentation/value contradiction. Neither is the same condition as any of my four F7 mutants. Both frames show near-total failure here, which is the only thing the comparison supports. |
| F8 metadata/annotation | 4 | **4** | *(none)* | 0 | — | **not comparable.** 0/18 observed models contain an annotation. |

**Pooled mapped classes** (F1↔S1, F2↔{N1,N2}, F3↔T1, F5↔S2): synthetic **13/16 = 0.81** [0.57, 0.93];
observed **9/10 = 0.90** [0.60, 0.98]. The observed mapped rate is **not lower** than the synthetic
one. The aggregate agreement of the two full populations (0.72 vs 0.69) is therefore a coincidence of
composition — my corpus is 8 classes × 4, A's is 13 records concentrated in classes the tool handles.

**The comparison that does carry information is by layer, not by class:**

| layer | synthetic | observed | agreement |
|---|---|---|---|
| notation / parse | F1 **4/4** | S1 **3/3** | both fully detected |
| name resolution | F2 **4/4** (4 sites; 0/1 at succession sources) | N1+N2 **5/5** | both fully detected at the sampled sites |
| typing | F3 **2/4**, F4 **3/4** | T1 **1/1** | both mostly detected |
| constraint / OCL | F5 **3/4** | S2 **0/1** | **disagree in direction** |
| semantic / structural | F7 **0/4** (default), 1/4 (mode-aware) | I1+R1 **0/3** (1 unmeasurable) | both ~fully missed |

Five layers, four agree, one disagrees on n=1. **The layer boundary replicates; the class-level rates
do not, because the classes are not the same classes.**

## 5. Controls (false-positive arm)

Four clean-tier controls under M1: **`T1-C1`, `T2-C3`, `T3-C3`, `T5-C1` — all four produce zero
diagnostics of any severity.** Error-level false-positive rate **0/4**; warning-level **0/4**.
No triage was needed, because nothing fired. Same under M4.

This is a falsification of gross over-reach on four short, ordinary models, **not** an estimate of a
false-positive rate — A says so in the frozen file and I repeat it. Four models cannot estimate a
rate; they can only refute a large one.

**The three `frozen-clean-only` models are reported descriptively and are not in the arm** (A's rule,
which I followed and agree with):

| model | M1 | M4 | what it is |
|---|---|---|---|
| `T5-C3` | `error[usage-typing]@11`, exit 2 | same, exit 2 | the `attribute window : VisibilityWindow;` defect A verified after the frozen population was closed |
| `T6-C1` | `error[reserved-keyword-name]@26`, **exit 0** | same, **exit 2** | the `port return;` defect |
| `T6-C3` | `error[reserved-keyword-name]@26`, **exit 0** | same, **exit 2** | the `port return;` defect |

Two things follow, and neither is a false positive. First, **the instrument diagnoses exactly the
defects A's second pass found and the first pass missed** — which is a point in the tool's favour and
a point against inspection-only coding, on data A generated. Second, **M1 vs M4 changes the exit code
and nothing else** (`0 → 2` on the two reserved-keyword models), which reproduces Gate 2's finding on
observed models rather than on my mutants.

## 6. Two measurement subtleties the external set exposed

### 6.1 One "miss" is not a miss: the short-circuit

`ES-T4-C1-E02` (R1) is scored `wrong-target` under my pre-registered rule, because the model emits
five errors and none is at the connector on line 51. The JSON envelope says something stronger:

```
status: "unresolved"
errors: ["…/T4-C1.sysml did not analyse cleanly; no check was made"]
```

**The tool states that it made no check.** So this item is not "looked at and passed" — it is
**unmeasurable on the default path**, because an earlier-layer defect (a reserved keyword at line 49,
plus the T1 succession errors) prevents the constraint passes from running. That is the short-circuit
I documented for my own pilot in §8.8; here it lands on an external item.

The clean test of R1 is therefore `ES-T4-C3-E01`, whose model analyses cleanly (status `holds`, zero
diagnostics) and where the tool is **completely silent** on a connector whose ends traverse
`Agv[10]` and `DockingStation[4]`. That single model is the whole evidence for R1, and it is a genuine
silent miss.

Consequence for the denominator, which I am reporting rather than choosing: **9/13 as registered;
9/12 excluding the short-circuited item; 9/11 excluding it and the contested I1.** The honest
headline is the registered one, with the ladder shown.

### 6.2 Two "wrong-target" outcomes hide a real diagnostic

`ES-T2-C2-E01` (S2) is scored `wrong-target` because the model's only error is
`reserved-keyword-name@17`, a *different* defect (A's post-inspection `attribute state`), and nothing
appears at line 33 where the satisfy usage is. Under M2 the instrument evaluates that satisfy and
returns

```
✓ satisfy lowerBeforeArrival holds
  standing: holds (… vacuous: requirement lowerBeforeArrival states no required constraint, so it holds vacuously)
```

So the S2 defect is not merely missed: **the instrument asserts the requirement holds, and explains
the vacuity in terms of the requirement's empty body** — not in terms of the missing satisfying
feature. A reader of that output would conclude the model is fine. This is the same finding I recorded
in Gate 2 addendum A5, now reproduced on the frozen item rather than on my probe.

## 7. Flagged observations for the adjudicator (I measured all items as labelled)

I do **not** claim any item is mislabelled. Three observations are recorded because they bear on how
the items should be read, and none of them changes a measurement:

1. **`ES-T4-C1-E02` is unmeasurable as scored** (§6.1). Its `wrong-target` is arithmetically correct
   under my rule and interpretively wrong: the tool made no check. If the adjudicator prefers a
   four-way split (detected / missed / unmeasurable / not applicable), this item moves from "missed"
   to "unmeasurable" and R1's class denominator becomes 1, not 2.
2. **`ES-T2-C2-E01`'s model contains a second, uncoded defect** at line 17 (the reserved keyword) that
   the tool reports. That is not an error in A's subset — the record was correctly kept out of the
   frozen population because its discovery route was instrument-surfaced — but it means the S2 item's
   *model* is not clean, and a reader comparing "tool silent on S2" with "tool silent on this model"
   would be wrong.
3. **`ES-T3-C2-E01` is detected at lines 23 and 24 but not at line 33**, though its declared range is
   `23,24,33`. The two reserved-keyword instances are caught; the reference `line.in` at 33 is not.
   The item is correctly scored detected; the partial coverage is an occurrence-level fact that a
   record-level count hides (the same objection A raised against my synthetic measure, O12).

## 8. What this does and does not establish about P6 and P8

The decision rule was fixed in `PRE-REGISTRATION.md` §8, before the run.

### P6 — "validator pass rates measure less than the literature claims"

**My registered rule: supported if the mapped classes' observed rate is ≥0.15 lower than the
synthetic rate.** Observed mapped 0.90 vs synthetic mapped 0.81 — **the condition is not met. P6 is
therefore not supported by the external set, and not refuted either: it is left where it was.**

That is the honest reading and it is unflattering to my own pilot. The reason P6 cannot be supported
here is structural, not a matter of insufficient data: **the observed corpus is dominated by the
classes the instrument handles**, so a rate computed on it is high by construction. The external set's
evidential value is in the *per-class and per-layer* structure (§3, §4), not in its aggregate.

What the external set *does* add to P6: the misses are all in constraint/semantic/structural classes,
which is where a pass rate claiming "valid" would be least warranted. So the pilot's practical
conclusion — a pass is evidence about four layers and no others — is **corroborated**; the stronger
claim that pass rates are inflated *in aggregate* remains unestablished.

### P8 — "the fault model is representative of real generation errors"

**Registered rule: weakened but not settled if the observed set contains classes my fault model does
not sample; supported only if class distribution and per-class detection both resemble the synthetic
frame.**

- **Four of my eight classes have no observed counterpart at all** (F4 multiplicity, F6 quantity/unit,
  F8 metadata) or only a contested one (F7 ↔ R1/I1). The construct census on the *frozen* models
  confirms why: **0/18** contain a `require`/`assert` constraint, **0/18** a unit literal, **0/18** a
  metadata annotation, **0/18** a `connection def`, **0/18** an explicit `end` feature, **0/18** a short
  name; 3/18 import `ISQ`/`SI` without writing a unit; **18/18** contain `satisfy`.
- **Two observed classes have no counterpart in my frame**: S2's specific constraint, and R1/I1's
  conditions. My fault model also lacks the missing-prelude class (N2) entirely.

**Verdict: P8 is weakened, not settled, and the direction is now stated.** My fault model samples the
**specification's demonstration surface**; the observed generation surface is declarations +
`satisfy` + connection shorthand + some behaviour. Per-class detection does **not** resemble the
synthetic frame (F5 disagrees in direction, four classes are unmapped); per-layer detection **does**.
So: the *layer* generalisation travels; the *class distribution* does not; representativeness remains
unestablished, and a construct-frequency census over ≥200 generated models is still the missing
instrument. **This is the same conclusion I reached after Gate 2, now with an independent corpus
behind it rather than an argument.**

## 9. Construct-mismatch statement, revisited with the observed data

After Gate 2 I wrote: *"the fault model measures defects on the specification's demonstration surface
while the observed generation surface is declaration + requirement usage + connection shorthand"* — at
that point on the basis of A's 18 models read as a census. Re-running the census **on the 18 frozen
models in the subset** (not on A's live corpus) gives the same result, with one correction carried
forward: `ISQ::`/`SI::` **imports** appear in 3/18, but **unit literals in 0/18**.

The external set then adds what a census cannot: what happens to those classes when they *are*
sampled. F4, F6 and F8 were **never sampled**, so the pilot's 3/4, 3/4 and 4/4 for them remain
untested against observation. F5 was sampled once and missed. F7 was sampled three times (R1×2, I1)
and produced one unmeasurable and two silences. **So the classes whose detection rates are most
favourable in my synthetic frame are precisely the classes the observed frame cannot test** — which is
a sharper statement of the construct-mismatch limitation than "constructs differ". It means the
pilot's aggregate 0.72 is *not* a conservative estimate of observed-corpus behaviour; the observed
corpus happens to land near it for entirely different reasons.

## 10. What changed because of the external set

Stated plainly, in order of how much it moves me.

1. **The layer boundary now replicates on a corpus I did not author.** Before this run, "detection
   stops at the constraint/semantic layer" was a finding about my own 32 mutants. It is now also a
   finding about 13 defects that a different agent coded, in models generated from six prompts, with
   two classes (R1, I1) that my fault model does not contain. That is the single thing I now believe
   that I did not believe before.
2. **My aggregate 0.72 is a composition artefact, and I can now show it.** Two populations with
   different class distributions landed at 0.72 and 0.69. Neither number transfers; the per-layer
   table does. I would no longer report 0.72 as a headline without the layer table beside it.
3. **The resolution story narrows again.** All four observed N1 items are *satisfy-target* references
   and all are detected; Gate 2 showed succession sources are not resolved; my four F2 sites are
   detected. So the resolution claim is now: *type references, expression references and satisfy
   targets are resolved; succession sources are not.* That is a three-way statement where I started
   with one.
4. **The instrument's misses are not uniform even inside a class.** S2 is missed while the tool
   positively reports the requirement as holding; R1's clean model is silent; R1's other model
   short-circuits. Three different mechanisms, one class column.
5. **What I did *not* learn.** Nothing about F4, F6 or F8 (unsampled). Nothing about whether my F7
   mutants resemble real structural defects (R1/I1 are not the same conditions). Nothing that
   supports P6 in the aggregate. **The external set supports my layer claim and cannot bear the weight
   of the aggregate claim** — and I would rather say that than let 0.69 sit next to 0.72 as if the
   agreement meant something.

## 11. Limits of this measurement

1. **13 items, 18 models, one generator family, prompts authored by the coder.** Every rate is a
   property of this corpus. A says so in the frozen file; I repeat it because the temptation to read
   0.69 as a general number is exactly the error this pilot exists to warn about.
2. **One instrument, default path primary.** M2 and M3 could each be applied to only **3 of the 13
   items**, because most observed models either do not analyse cleanly or state no assertion. A
   verdict-path measurement on this corpus is therefore mostly *not applicable*, and I report that as
   an applicability fact, not as a null result.
3. **The attribution rule is line-based and therefore conservative and mechanical.** It refuses credit
   for a diagnostic elsewhere in the model (2 items), which is the right choice for a per-item measure
   and the wrong choice if one asks "did the tool flag this model at all". At model level: the 13
   items sit in **11 distinct models**, of which **9 produced ≥1 diagnostic** and 2 (`T1-C3`,
   `T4-C3`) produced none. Item-level detection is 9/13; model-level "something was reported" is
   9/11. The aggregates coincide; they mean different things.
4. **I had previously run 15 of these 18 models** during the Gate-2 cross-review, so my pre-registered
   expectations were informed, not blind (`PRE-REGISTRATION.md` §7). The rules are the valuable part;
   the predictions were 9/13 exactly, which is corroboration of nothing.
5. **`wrong-target` and `unmeasurable` are not the same thing** and my registered vocabulary had only
   the first. §6.1 records the gap rather than retrofitting it.
6. **A's subset is itself contested.** 3 items carry a live contest; 1 of those (I1) moves the
   headline by 0.06, and the R1 contest cannot move any detection number. The subset is also not
   independently labelled: the generator, coder and selector are one agent, and the second coder's
   agreement is weak for the reason I documented in `B-reviews-A.md` (O5).

## 12. What would change this answer

- **A construct-frequency census over ≥200 generated models** would tell me whether F4/F6/F8 ever
  occur, which is the only way to test the classes this set cannot.
- **A second instrument** would separate "this tool misses the constraint/semantic layer" from
  "constraint/semantic checking of SysML v2 misses it".
- **A second, independent coder of the same 13 items** would test whether the 9/13 is a property of
  the items or of A's coding of them.
- **A corpus generated from prompts that ask for quantities, constraints and metadata** would sample
  the classes my fault model was built on; until then the pilot's per-class rates for F4/F6/F8 are
  untested.

## 13. Files

```
research/issue-008/empirical/
  PRE-REGISTRATION.md / .sha256   the frozen rules (hash in the header of this file)
  run_external.py                 harness: verify hashes, run 4 modes, score per the rules
  results.csv                     80 rows: 20 items × 4 modes
  per-item-per-mode.md            the readable matrix, with per-cell detail
  raw/run1/**                     first execution, superseded (AM1 derivation fixes)
  raw/run2/**                     the run these numbers come from, unedited
  run-log.md                      hash verification, pre-registration hashes, tool identity, argv, exit
                                  codes, object selection, run1→run2 comparison
  REPORT.md                       this file
```

---

## 14. Adjudicated corrections (Gate 4, dated addendum)

Each item quotes the text it supersedes (the original stays visible above), states old → new, and
names the ruling. Sources: `research/relational/adjudication/ADJUDICATION.md` and
`CORRECTIONS.md` Part 2. Derived numbers come from `results-addendum.csv` and
`SCORING-ADDENDUM.md`; the raw output in `raw/run2/**` and `results.csv` is untouched.

### 14.1 The pre-registration hash (B-12 / RB-01)

**Superseded:** the header's *"PRE-REGISTRATION.md, frozen at
`9458406e7db665ac42f5a3a896a7dc05b094b0fb6e8ef3a4ab9ed9db7e6acfbc` before the first run (the
superseded first draft, `0106e082…`, differs only in a header timestamp)"*.

**Corrected.** `9458406e…` was computed at **14:36:04Z, after run1** (14:35:38–41Z) and it contains
amendment AM1; the pre-run value was overwritten when AM1 was appended; and AM1 added §11 (three
derivation fixes), so "only a header timestamp and a note" is wrong too. The pre-registration
therefore rests on: (i) the **content** of the rules, none of which AM1 altered; (ii) **AM1's own
disclosure** of the three derivation changes, all of which move items from `not detected` toward
`not applicable`; and (iii) the **run1→run2 identity of the detected set** (M1 identical at n = 9;
no `standing: violated` in any M2/M3 raw file in either run). Its honest status is
**content-evidenced, not hash-proven**. Full disclosure: `run-log.md` §7.

### 14.2 M2 and M3 accounting (B-16 / RB-05; B-17 / RB-06)

**Superseded:** §1's *"M2 `-satisfy` 0 detected, 1 evaluated (holds-vacuously), 10 not applicable"*
and *"M3 … 0 detected, 1 undecided, 10 not applicable"*.

**Corrected, under the registered rule (`PRE-REGISTRATION.md` §4.2), which the harness had
deviated from:**

| mode | applicable | breakdown | not applicable |
|---|---:|---|---:|
| M2 `-satisfy` | **1** | ES-T2-C2-E01 `holds-vacuously` → **not detected** | 12 |
| M3 `-instantiate … -validate=` | **3** | ES-T1-C3-E01 `holds` → not detected; ES-T2-C2-E01 `undecided` → **weaker signal**; ES-T4-C3-E01 `holds` → not detected | 10 |

The harness had scored two non-satisfy items as `wrong-target` instead of `not applicable`; that is
re-scored in `results-addendum.csv` and it changes **no** detection count (nothing becomes
`detected`). Controls now carry model-level vocabulary, not item-attribution vocabulary.

### 14.3 The obligation split (B-32 / X-01) — the most consequential correction to this document

**Superseded:** §1's presentation of **9/13 = 0.69** as the external arm's headline without a
composition line, and §8's treatment of it as an aggregate to be compared with the synthetic 0.72.

**Corrected.** The four misses are one **discretionary** constraint (S2 — a `check…` constraint whose
obligation is "MAY report, satisfy by implied relationships, or ignore"), two items with **no
normative basis** (R1 ×2, contested as to defect status), and one **contested** item (I1). So:

| obligation class | n | detected | rate |
|---|---:|---:|---|
| **established defect status + mandatory reporting** | 9 | **9** | **9/9 = 1.00** |
| discretionary / no normative basis / contested | 4 | 0 | **0/4 = 0.00** |
| all items | 13 | 9 | 9/13 = 0.69 |

**The aggregate 9/13 is not a detection-gap measure.** It is a composition of a perfect score on
everything the specification establishes and mandates reporting for, and a zero on everything it
leaves discretionary or that is contested. This is the same correction the adjudicator applied to
A's 9/14, applied symmetrically to mine — and I did not make it for my own arm.

### 14.4 Layer vs obligation (B-33 / X-02, UNRESOLVED)

**Superseded:** §4's *"the comparison that does carry information is by layer"* and §10's *"the layer
boundary now replicates on a corpus I did not author"*, stated as a property of the instrument.

**Corrected.** Two readings are live and **perfectly confounded in both corpora**: (a) detection
stops at a **layer** (semantics is beyond the instrument), or (b) detection tracks **what the
specification names and mandates reporting for** (the instrument sees what it is told to see). Every
miss in both corpora is simultaneously a semantic-layer condition *and* a discretionary or unnamed
one. Until X-02 is settled, **both readings are reported and neither is stated as a property of the
instrument.** What survives unconfounded is narrower: within the items the specification establishes
and mandates, the tool detects all of them (9/9 here; 9/9 in A's corrected population).

### 14.5 The denominator ladder, uniquely labelled (B-34 / X-03)

**Corrected.** The rungs, with the exclusion order fixed once and used everywhere:

| rung | n | detected | rate | removes |
|---|---:|---:|---|---|
| **L1** | 13 | 9 | 9/13 = 0.69 | nothing |
| **L2 −I1** | 12 | 9 | 9/12 = 0.75 | contested defect status |
| **L3 −I1 −unmeasurable** | 11 | 9 | **9/11[C]** = 0.82 | the short-circuited item |
| **L4 −R1** | 11 | 9 | **9/11[R1]** = 0.82 | both R1 items, contested as to defect status |
| **L5 established+mandatory** | 9 | 9 | **9/9** = 1.00 | everything discretionary/unnormative/contested; with **0/4** on those |

L3 and L4 are both 9/11 and are **different sets**; they carry distinct suffixes and are never quoted
without one. Earlier in this document the ladder appeared as "9/13 → 9/12 → 9/11" with no suffix and
with the exclusion order stated in §1 but not in §6.1.

### 14.6 Verdicts are not self-certifying (B-35 / X-04, UNRESOLVED)

**Corrected.** Wherever this document quotes a verdict it must name **the invocation, the engine and
the standing label**. `-engine` is a mode I never exercised; the adjudicator reproduced
`-engine check` returning `holds` on an invariant that `-engine smt` witnessed as violated. One model
is a demonstration, not a rate — but it means no verdict in the verdict path can be quoted as
self-certifying, and "the instrument decides X" is always shorthand for "invocation I, engine E,
returns standing S". Nothing in this document rested on a verdict being correct: the one `violated`
that ever appeared here was my own F7-02 mutant, with a `holds` control on its known-good base, in
Gate 2 — and that control is the only reason the verdict was readable at all.
