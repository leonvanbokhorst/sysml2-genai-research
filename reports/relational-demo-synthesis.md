# Relational research synthesis — what changed because agents challenged one another

**Run:** demonstration pilot, 2026-11-13. **Questions:** issue
[#7](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/7) (observed error population,
Researcher A) and issue [#8](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/8)
(validator reliability, Researcher B), with issue [#10](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/10)
(semantic ceiling) used only as an adversarial critique.
**Status: stopped at the human review gate.** No merge, no issue closure, no expansion to further
questions. This pilot does not complete either issue; both reports say so in their first paragraph.
**Author:** Team Lead, writing only after the adjudicator filed Gate 4 — this document synthesises
the research record, it does not create evidence.

The authoritative record of what was ruled is
[`research/relational/adjudication/ADJUDICATION.md`](../research/relational/adjudication/ADJUDICATION.md)
and its 81 machine-readable rulings. Where this synthesis and a report disagree, the adjudication
wins; where the adjudication leaves a question open, this synthesis says so rather than closing it.

---

## 1. The short answer

**The demonstration worked, and the work is better for it — but not in the way a success story
would predict.** No headline numerator moved: A's detection numerator stayed 9, B's stayed 23, B's
external rate stayed 9/13. What changed is what each number is *allowed to say*.

Three claims did not survive contact:

1. **B's central negative claim was false as stated.** B reported that all four structural defects
   it built were invisible to the only available validator, and concluded that a clean validation is
   "no evidence at all" about a model's structure. Researcher A ran one command B had read about but
   never executed — `-instantiate <object> -validate=<object>` — and the validator reported the
   failing requirement, exit 1, with a passing control on the known-good base. B reproduced it,
   accepted it, and replaced the claim with a mode-specific one. The corrected finding is *sharper*
   than the original: the default path is blind to architectural meaning; the verdict path decides
   exactly those defects the generator encoded as a checkable constraint, and nothing more.
2. **A's "validator blind spot" was a composition artefact.** The four-to-five "silent" records that
   carried the claim were one record withdrawn as legal (the library declares `action start`), one
   constraint whose obligation is MAY ("a tool … may ignore the violations"), two with no normative
   basis, and one contested. On records that are established defects and mandatory to report, the
   pinned validator detected 9 of 9. The 9/14 figure is arithmetically right and interpretatively
   unsupported.
3. **Both pilots measured one invocation and named "the instrument", "the language", or "the
   ceiling".** The #10 critic built 25 probe models and ran 122 invocations of the same pinned
   binary: six of the nine semantic properties the #10 premise treats as unreachable are decided
   under *some* invocation, and every decided case depends on the model's encoding, not on SysML v2.
   The sharpest case is the critic's own: `-engine check` returned `no violation … standing: holds`
   for an invariant the same binary's SMT engine witnessed as `violated at step 2`. A validator's
   verdict is no more self-certifying than its detection — an axis neither pilot had measured.

What survived is not nothing: the wrapper study (every raw output was markdown; normalising it
fixes only half the failures), the finding that inspection missed real mechanical notation defects,
the exit-status-is-not-validity finding, the direction of B's fault-class boundary, and B's refusal
to claim representativeness it could not establish. Those survived because reviewers re-ran the
numbers and found them right, not because anyone agreed with them.

---

## 2. The challenge record, in the order it happened

Every row is a separately inspectable artifact. "Effect" is what the challenged researcher changed,
not what a reviewer asserted.

| # | Challenge | Challenger | Evidence used | Response | Effect on the work |
|---|---|---|---|---|---|
| 1 | B's structural defects are invisible to the instrument | A | One command on B's own F7-02 mutant and its known-good control; exit 1 vs 0 | **Accepted** after independent reproduction (12 accept / 1 partly / 0 reject of A's 13) | B added 34 mode probes, a per-mode F7 table, and replaced "no evidence at all" with the encoding-dependent claim; frozen method and expectations untouched |
| 2 | A has a post-inspection record whose excerpt is not in its model | B | Text search of `T5-C3.sysml`; line 26 is `part antenna : Antenna;` | **Accepted**; record withdrawn | Combined arm 21→20, S1 9→8; the substring check that would have caught it is now a hard contract in `apply_corrections.py` |
| 3 | A claims `errors.csv` was "frozen and hashed before detection", but no hash exists | B | Absence of any hash artefact; mtime coincidence traced to A's own determinism re-run | **Accepted**; claim **withdrawn**, not defended | Report now labels the ordering argument inferential; protocol amendment A2 makes hash-at-freeze mandatory |
| 4 | A's κ = 1.0 is mostly answer-key matching | B | 7–8 of 11 paired excerpts appear verbatim in the copy of the codebook the second coder received | **Accepted** | κ demoted from reliability evidence to a reproduction check; narrower independent residue named (three clean-model calls, reserved-keyword spotting, W1 recording difference) |
| 5 | A's "inspection missed a third" rate treats validator-surfaced records as recall | Reviewer A | The post-inspection arm was surfaced by the tool's own diagnostics | **Accepted** | Restated as 6 further verified defects, descriptive not recall |
| 6 | A's 9/14 blind-spot reading is a composition artefact; on established mandatory records it is 9/9 | Reviewer A | Catalogue obligation column; the withdrawn T1-C1 record; spec text for S2 | **Accepted** (adjudicator recounted it) | 9/14 kept as registered; the interpretative claim narrowed to the 9/14→9/13→9/12→9/10→9/9 ladder with its composition named |
| 7 | A's wrapper split is gate-dependent: 6/12 any-diagnostic vs 9/9 exit-status | Reviewer A | Three normalised models are error-severity with exit 0 | **Accepted** | Both gates reported; the headline must name its gate |
| 8 | A's technical report pages are stale relative to its own corrections | Reviewer A | §1 vs §16/§17; README hash mismatch | **Accepted** | Front-matter "current numbers" table; superseded sections marked |
| 9 | B's external pre-registration hash is post-AM1, so the hash chain does not prove pre-run status | Reviewer B | File contents contain AM1; `.sha256` mtime equals the post-run regeneration instant | **Accepted** | Disclosure corrected; pre-registration now rests on content + AM1 disclosure + run1/run2 identity, not on the hash |
| 10 | B counts F4-01 as a detection while citing the same error as tool over-reach | Reviewer B | KerML §8.3.4.11.2 / §8.4.4.12.2 read directly | **Accepted on the factual question**, with the ruling that `[4..2]` is an *empty range* and therefore a real defect: **23/32 stands**; the "over-reach" sentence goes, and 22/32 is stated as the named-constraint-only alternative | Report must present both readings; P5 rewritten |
| 11 | B's overreach survives in reader-facing text after the addenda | Reviewer B + critic | §1, §11.1, README "nothing here was informed by Researcher A's work" | **Accepted** | Front-matter pointers required; README false statement removed |
| 12 | Both pilots understate what automated checking can establish and mis-attribute the #10 premise | #10 critic | 25 probe models, 122 invocations; p08b check-vs-SMT disagreement; execution flags | **8 claims accepted as overstated**, the rest upheld as cautious | A's "the pilot implementation executes neither actions nor state machines" corrected: that sentence is the OMG reference implementation's, not this tool's; B's ceiling is the *default path's* ceiling |
| 13 | Challenge: the 9/9 subset (established + mandatory) carries evidential weight | Adjudicator, rejecting an inference | 9/9 is post-hoc and spans only the layers the tool is known to cover | **Rejected as an inference**; retained only as a composition statement | Prevents the correction becoming a new overclaim in the other direction |
| 14 | Challenge: A's line 42 is legal because a definition can stand where a usage is required | B | Grammar text | **Rejected** | The record stands; B's sub-claim was wrong |

**What the relational structure added that no single researcher found:**

- **A and B were describing the same `name-conflict` mechanism.** A's external corpus produced 119
  `name-conflict` diagnostics in 10 of 24 artefacts; B's only known-good-arm diagnostic was a
  `name-conflict` warning (later reclassified as unresolved/specification-ambiguous). The adjudicator checked all 119: every one is "Duplicate of inherited
  member name 'X' from Y". KerML's distinguishability constraint forbids it on the letter; SysML
  §7.13.4's own example uses it. Neither pilot could see this alone; it is now one unresolved
  question, not two local curiosities.
- **B's external challenge set had the same composition problem as A's population** — the
  adjudicator noticed that B's four external misses are one discretionary constraint, two without a
  normative basis, one contested, so 9/13 is really 9/9 established + 0/4. That symmetry was
  invisible to both researchers because each was looking at the other's numbers.
- **"Detection tracks the layer" and "detection tracks what the specification names and mandates"
  are perfectly confounded** in both corpora: every miss is discretionary, unnamed or contested.
  B's H9 conclusion ("layer, not specification silence") therefore rests on six mutants with two
  counterexamples, and the adjudicator ruled it unresolved rather than preferring the more
  interesting explanation.

---

## 3. What did not change, and why that matters

| Claim | Status after challenge | Reason |
|---|---|---|
| Wrapper is universal and insufficient: 18/18 raw outputs are markdown; only part of the failure is formatting | Holds | Reviewer A re-derived the counts; the gate question changed the labels, not the phenomenon |
| Inspection missed real mechanical notation defects (reserved-keyword names, attribute-as-state, etc.) | Holds | Independently verified against the notation productions; survived even after the post-inspection arm was relabelled descriptive |
| Exit status is not a validity verdict (error-severity diagnostics with exit 0) | Holds | Reproduced on A's corpus, B's probes, and the critic's invocations; `-strict` changes it |
| B's 23/32 default-path detection | Holds | Reviewer B re-ran the binary over all 42 models and recomputed every interval |
| B's 0/10 known-good error-level diagnostics | Holds as a **calibration probe, not a false-positive rate** | The bases were quoted from the specification but iterated to tool-silence before the freeze (B-22); a clean run on a corpus tuned to pass cannot estimate specificity |
| B's external 9/13 default-path rate | Holds | Re-scored from raw by two reviewers; composition caveat added |
| The direction of B's fault-class boundary (notation/resolution/typing detected; constraint/semantic/structural missed) | Holds as direction, not as a law | Replicated on A's independently generated corpus; confounded with obligation status (unresolved) |
| B's refusal to claim representativeness | Holds, and is vindicated | The external set showed the construct gap: 0/18 of A's models contain a checkable constraint, unit literal, metadata or connection def, which carry four of B's eight classes |

**No report was rewritten to look better.** Corrections are dated addenda that keep the original
claim visible; the frozen method files and expectation manifests are byte-identical to their
pre-challenge bytes, and the adjudicator pinned them.

---

## 4. Unresolved disagreements (kept visible, not averaged)

The adjudicator ruled four questions genuinely unresolved. They are not softened here.

1. **Is a `name-conflict` / same-named member inside a specializing definition a defect?**
   Both pilots met it and labelled it differently. KerML's `validateNamespaceDistinguishibility`
   with the default `isDistinguishableFrom` forbids it as written; SysML §7.13.4's own example uses
   it. *Settled by:* an OMG SysML/KerML RTF or SysML-expert ruling, or running the OMG reference
   implementation on the 10 external artefacts plus B's KG-04. A PI can obtain either.
2. **Does detection track the semantic layer, or the specification's obligation structure?**
   Perfectly confounded in both corpora; B's H9 had two counterexamples. *Settled by:* a crossed
   mutant design — named-mandatory vs unnamed at each layer, invocation fixed — using B's existing
   harness. Days, no access boundary.
3. **Is a connector end resolved through a multi-valued feature usage defective?** A says yes
   (structural), the adjudicator notes no named constraint decides it, and it is contested as to
   *defect status*, not only layer. It carries A's structural claim and moves B's external
   denominator (9/11 if R1 falls). *Settled by:* the same RTF/expert route as (1).
4. **Is the bounded engine's false `holds` systematic?** The critic's p08b showed `-engine check`
   claiming `holds` on an invariant `-engine smt` witnessed as violated. One model is not a rate.
   *Settled by:* a small invariant-mutant family run under check/smt/all — an afternoon for a PI.

Three further limitations are not disagreements but boundaries of this run: one generator family
(the research agents themselves), no human expert coder, one validator, N = 18 models and
N = 32 mutants, and one adjudicator. Every lettered rubric for #7 (≥200 models) and #8 (second
coder on mutant validity, second instrument) remains unmet. **Both pilots are preliminary and
neither issue can close on this evidence.**

---

## 5. What the workflow itself learned

This is the part a student should take away: the process failures are as instructive as the
research findings, and they were found by the people whose job was to attack the work.

1. **A hash of the method is not evidence about the data.** B's method hash was exemplary and B
   still regenerated its pre-registration hash after the first run; A never hashed its coded
   population at freeze. The fix is mechanical (`PROTOCOL.md` Amendment A2): hash the ground-truth
   file at the moment it is frozen, never regenerate a `.sha256`, and give a corrected artefact a
   new dated name.
2. **Frozen artefacts drift unless the ledger is append-only.** Files moved under reviewers who had
   pinned hashes — report, codebook, a response file. The adjudicator pinned 34 hashes and
   re-verified them; one reviewer caught a "frozen at 14:29Z" label on a file containing 14:31Z
   corrections. Nothing false was published, but the mechanism, not the argument, is what should
   carry the weight.
3. **An invocation is a methodological choice and must be pre-registered.** B found its own worst
   bug by noticing it had quoted `-validate=<object>` in its report and never run it; the critic
   then found that *engine choice* can flip a verdict from `violated` to a false `holds`. Any future
   validator study must freeze the invocation set and the engine, exactly as it freezes mutants.
4. **A second coder is not independent if the codebook contains the answers.** A's copy of the
   codebook reproduced 8 of 11 paired excerpts verbatim. κ = 1.0 was reported, then correctly
   demoted. The lesson is not "don't use a second coder" but "don't bake the sample into the
   instrument".
5. **Adjudication is not consensus.** Reviewers filed 28 objections and the critic 20 claim
   rulings; the adjudicator rejected 3 challenges outright (including two *reviewers'* sub-claims
   and the inference that the 9/9 subset proves the validator reliable), corrected two challengers
   on their own evidence, and left 4 questions unresolved. A majority of reviewers agreeing would
   have settled nothing.

---

## 6. What a reader should take to the main question

The main question asks how GenAI-generated SysML v2 models can be reliably validated. This pilot's
evidence supports a narrower, more useful statement than either original report:

> On this evidence, validator pass rates measure notation, name resolution, typing and
> per-constraint well-formedness. They do not measure whether a model means what it claims, and
> they do not even reliably measure the encoded part unless the invocation is stated: the same
> pinned binary reports a requirement as holding vacuously when the requirement has no checkable
> constraint, decides it when it does, and can return a false `holds` from its bounded engine while
> its SMT engine witnesses a violation.

That is a calibration statement about one instrument at one version against two small corpora,
and it is exactly the kind of statement issue #8 was created to make possible. It is not a claim
about "SysML v2 validators", and both pilots now say so.

---

## 7. Where the record lives

| Question | Primary report | Evidence |
|---|---|---|
| #7 pilot | [`reports/issue-007-error-taxonomy-pilot.md`](issue-007-error-taxonomy-pilot.md) | [`research/issue-007/`](../research/issue-007/) |
| #8 pilot | [`reports/issue-008-validator-reliability-pilot.md`](issue-008-validator-reliability-pilot.md) | [`research/issue-008/`](../research/issue-008/) |
| Process | [`research/relational/`](../research/relational/) | protocol, gate log, cross-reviews, reviews, critique, adjudication |
| Rulings | [`ADJUDICATION.md`](../research/relational/adjudication/ADJUDICATION.md) — 81 entries: 64 accepted challenges + 10 upheld status propositions + 3 rejected + 4 unresolved (the JSON groups the ten upheld under `ACCEPTED`, so its counters read 74/3/4) | [`rulings.json`](../research/relational/adjudication/rulings.json) |
| Corrections | [`CORRECTIONS.md`](../research/relational/adjudication/CORRECTIONS.md) | dated responses in each researcher's tree |

**Stop.** Nothing here is merged or closed. The next move is a human's: accept, reject, or redirect.
