# Gate log — relational demonstration (#7 × #8, #10 lens)

Recorded by the Team Lead. Each gate lists what was required, the artifact that satisfies it, and
the evidence a reader can check. Times are the artifact timestamps in UTC where recorded by the
author, as found on disk by the Lead.

## Gate 0 — Setup (Lead)

- Protocol written and frozen before researchers began: [`PROTOCOL.md`](PROTOCOL.md).
- Tool pinned before researchers began: [`TOOLING.md`](TOOLING.md) — OpenSysML CLI `v0.12.1`
  (asset sha256 `0f16d282…c96210`, binary sha256 `ddfc2962…1598f0`).
- Directory layout created; write scopes disjoint ([`PROTOCOL.md`](PROTOCOL.md) §5).
- Task board opened (11 tasks, dependency-ordered). Researchers claim their own tasks.

## Gate 1 — Independent methodology freeze

**Required:** both researchers write and hash their methodology before seeing the other's results.

| Researcher | Artifact | sha256 | Author's freeze time (UTC) |
|---|---|---|---|
| A (issue #7) | [`../issue-007/METHODOLOGY-FROZEN.md`](../issue-007/METHODOLOGY-FROZEN.md) | `269d8dbe7228db83d20ca2be39991172f20fd23458ac1e5e6755ff7269564f76` | 2026-11-13T14:05:30Z |
| B (issue #8) | [`../issue-008/METHODOLOGY-FROZEN.md`](../issue-008/METHODOLOGY-FROZEN.md) | `2c80d63e8800be9ca67a051aaffdbc4b6c56c1b576002fc4446fe82862e6f00b` | 2026-11-13T14:08Z |

**Status: passed.** Both files contain an explicit independence statement (neither had read the
other's directory, and no results were relayed by the Lead). A's freeze precedes B's, so neither
can have been fitted to the other's findings; each hash is quoted in that researcher's own report.

**Disclosed pre-freeze activity, not a breach.** Researcher B ran tool-invocation probes before
writing the freeze and logged them separately as
[`../issue-008/results/calibration/PRE-FREEZE-CALIBRATION.md`](../issue-008/results/calibration/PRE-FREEZE-CALIBRATION.md).
Two kinds of pre-freeze knowledge must be named, not one (correction L-1, from ruling RB-03):

1. **Interface knowledge** — output shape, JSON envelope, exit codes, the fact that an early-layer
   error short-circuits later checks. The frozen measurement definition has to name these in
   advance, and they are excluded from every denominator.
2. **Construct-level detection knowledge** — the probes also showed the binary firing
   `incommensurable-binding` (F6), `metadata-metaclass` and `metadata-owning-type-feature` (F8),
   and `bound-feature-types` as a warning. F6's and F8's "expected detectable = yes" flags were
   therefore written after the same mechanisms had been observed firing. That is a material threat
   to the expectation audit, and the report now states it (addendum B-7): the audit is *informed,
   not blind*, and weak by construction. It is also why the audit's 24/24 "expected detectable →
   produced a diagnostic" result cannot be read as predictive accuracy.

The mutant author had additionally seen the tool's advertised diagnostic codes (`-explain`). B
disclosed this at freeze time; the consequence was under-described until the adjudicator ruled on
it. The probes are excluded from every denominator.

## Gate 2 — Cross-review

**Required:** each researcher challenges the other on evidence, and each writes a dated response to
the review of their own work. Neither reads the review of themselves before filing their own.

| Artifact | Author | sha256 | Objections |
|---|---|---|---|
| [`cross-reviews/A-reviews-B.md`](cross-reviews/A-reviews-B.md) | Researcher A | `05ca64ccaa4ceae4032ca36aa22f2090c5565449d021764a9da480bbbb1a8102` | 13 — 1 blocking, 7 material, 5 minor |
| [`cross-reviews/B-reviews-A.md`](cross-reviews/B-reviews-A.md) | Researcher B | `de2d99cea17587a9603e9602303873556db9b00f93d8101451c0db57be9af0b1` | 13 — 0 blocking, 8 material, 5 minor |

**What the reviews found, in one line each** (the Lead's summary of the filed reviews; the reviews
themselves are authoritative):

- A's blocking objection: B's strongest claim — that structural defects are invisible to the
  instrument — is true of the default `-validate` path only. On B's own F7-02 mutant the pinned
  binary reports the failing `satisfy` assertion under `-instantiate … -validate=<object>`, with a
  passing positive control on B's known-good base. B had disclosed the mode as unexercised but had
  not run it.
- A's material objections: the fault model is specifications-flavoured rather than
  generation-flavoured (no reserved-keyword or missing-prelude class; all F2 mutants in
  type-position; F5 tests a satisfy defect the tool catches while A's observed named-SHOULD defect
  is silent; the F5/F6/F7/F8 constructs appear in 0/18 of A's models); substituting A's observed
  class distribution barely changes the aggregate (0.64–0.71 vs 0.72), so A explicitly does *not*
  claim B's headline is inflated.
- B's material objections: one post-inspection record cites a `port` that the model does not
  contain (phantom record), one real notation defect is uncounted, the "hashed before detection"
  claim has no hash behind it, 7 of 11 double-coded excerpts are verbatim in the codebook the
  second coder received (so κ = 1.0 is weaker than the headline implies), and R1/I1 carry the
  structural/semantic claims while resting on readings that are not defended against the obvious
  rival. B verified and cleared the frozen population's 14 excerpts, the 9/14 detection result,
  the κ arithmetic and the external-arm counts.

**Independence caveat, recorded rather than hidden.** A's artefact tree was not frozen at Gate 1:
A added detection cross-review probes under its own directory while B was writing its review. B
stated it read only the heading of that probe file, and pinned sha256 of all eleven artefacts it
reviewed so the adjudicator knows exactly what was reviewed. Gate 1 froze *methodology*, not the
artefact tree; this is a limit of what procedural independence can establish, not a breach of the
protocol as written.

**Status: response turn in progress.** Each researcher now writes a dated response
(`A-response-to-B-review.md`, `B-response-to-A-review.md`) applying corrections as addenda that
preserve the original claims, per [`PROTOCOL.md`](PROTOCOL.md) Amendment A1.

## Gate 3 — Independent review and semantic-ceiling critique

**Required:** each pilot is reviewed by an agent with no stake in it, and a critic applies the #10
semantic-ceiling perspective adversarially to both.

| Artifact | Author | Objections | Status |
|---|---|---|---|
| [`reviews/reviewer-a-issue-007.md`](reviews/reviewer-a-issue-007.md) | Reviewer A | 0 blocking · 7 material · 6 minor | filed |
| [`reviews/reviewer-b-issue-008.md`](reviews/reviewer-b-issue-008.md) | Reviewer B | 0 blocking · 7 material · 5 minor (43 claim verdicts) | filed |
| [`critique/semantic-ceiling-critique.md`](critique/semantic-ceiling-critique.md) | Semantic-ceiling critic | 20 claim rulings, 8 flagged as overstated | filed |

**Reviewer A's two material findings, as filed:** (1) the 9/14 "validator blind spot" is composed
entirely of records that are withdrawn, discretionary or contested — after A's own correction it is
9/13, and on records that are established defects and mandatory-to-report the tool detects 9/9;
(2) the V1/V2 wrapper split is gate-dependent — three of the twelve "invalid after normalisation"
models are exit-0, warning-only, so under the error-level gate A applied elsewhere the split is
9/9, not 6/12. Reviewer A also found the report's summary sections stale after A's own later
corrections (material), and recorded the artefact instability during review with pinned hashes
(process finding). Reviewer A re-ran the agreement, corrections and detection scripts and
reproduced the published numbers byte-identically.

## Gate 4 — Adjudication

**Required:** every challenge reconciled on documented evidence; accepted / rejected / unresolved;
no majority vote, no deference to model authority, no self-judging; unresolved visible.

| Artifact | Rulings |
|---|---|
| [`adjudication/ADJUDICATION.md`](adjudication/ADJUDICATION.md) | 81 consolidated rulings: **64 accepted · 3 rejected · 4 unresolved**, plus 10 critic status propositions upheld |
| [`adjudication/rulings.json`](adjudication/rulings.json) | one machine record per ruling (id, sources, claim, ruling, evidence, reasoning, residual uncertainty, correction) |
| [`adjudication/CORRECTIONS.md`](adjudication/CORRECTIONS.md) | 63 numbered edits by owner (A: 24, B: 35, Lead: 4); none performed by the adjudicator |

**Independence and method.** The adjudicator re-ran the pinned binary 11 times and recounted every
disputed figure from raw CSVs; no validator verdict was used as ground truth. It pinned 34 artefact
hashes, re-verified byte-identical before filing, and rejected three challenges — including two
sub-claims made by reviewers and the inference that the 9/9 "established + mandatory" subset proves
the validator reliable (it is post-hoc and covers only the layers the tool reaches).

**Consequential rulings.** (1) A's 9/14 "blind spot" is a composition artefact — one withdrawn
record, one MAY-obligation constraint, two with no normative basis, one contested — so the honest
statement is 9/9 on established mandatory records plus four discretionary/contested misses; the
numerator stays 9 and the denominator ladder is printed. (2) A's V1/V2 wrapper split is
gate-dependent: 6/12 on any diagnostic, 9/9 on exit status. (3) B's F4-01 `[4..2]` is an empty range
and therefore a real defect: **23/32 stands**, and the "tool is stricter than the spec" sentence is
what goes; 22/32 is stated as the named-constraint-only alternative. (4) B's external 9/13 is
composed of 9/9 established-mandatory plus 0/4 discretionary/contested — the same composition
problem the adjudicator found in A's population and nobody else noticed. (5) The two pilots' `name
conflict` findings are one mechanism, not two local curiosities.

**Status: passed.** Corrections were routed to their owners (Amendment A2 governs the form: dated
addenda, no rewrites, no re-freezing); the four unresolved questions are carried into the synthesis
with named settle criteria. **The human review gate is the next and final stop: no merge, no issue
closure, no new questions.**

**Reviewer B's two material findings, as filed:** (1) the external pre-registration's "frozen"
hash `9458406e…` is not a pre-run hash — the file contains amendment AM1, written after external
run1, and `PRE-REGISTRATION.sha256` was regenerated at the same instant, so the pre-run value was
overwritten and the run log's "differ only in a header timestamp" claim is contradicted by the
file's contents; the rules are visibly pre-run in content and AM1 is conservative, but the hash
chain offered as proof does not show it. (2) F4-01 (`[4..2]`) is counted as a detection in the
23/32 numerator while the report cites the same error as the instrument being "stricter than the
specification": either the model is legal and that is a spurious error (F4 2/4, headline 22/32),
or it is a defect and the over-reach framing is wrong — the report adopts neither. Reviewer B also
found reader-facing overreach surviving the addenda (§1 "no evidence at all", "perfect on the
layers", §11.1 "four out of four … means nothing at all", README "nothing here was informed by
Researcher A's work") with no pointer from the front matter to the addenda, and specific count
errors (A8's "24 of 28" recomputes to 23; "5 silent" contradicts B's own frozen definition;
the external M2/M3 applicability row does not sum to its denominator). It reproduced every
headline number by re-running the binary and recomputing the intervals.

**Semantic-ceiling critic's core finding, as filed:** both pilots measured one invocation and then
named *the instrument*, *the language* or *the ceiling*. Six of the nine properties the #10 premise
treats as unreachable are decided by the same pinned binary under some invocation, and every
decided case depends on the model's *encoding* and the values being bound. The sharpest evidence is
probe P08b: for an action whose invariant is violated at the final state, `-engine check` returns
`no violation … standing: holds` (exit 0) while `-engine smt` witnesses `violated at step 2`
(exit 1), and only `-engine all` names the disagreement. A validator's *verdict* is therefore no
more self-certifying than its *detection* — an axis neither pilot measured. The critic also found
A mis-attributes the OMG reference implementation's "executes neither actions nor state machines"
to the tool it measured, and that B's §4.2/§11.5 ceiling statements survive in text its own
addenda contradict.
