# Relational research protocol — demonstration run (issues #7, #8, #10)

**Status:** operating protocol for this demonstration. Authored by the Team Lead before any
researcher produced evidence, on 2026-11-13. Frozen: later edits require a dated
amendment section at the bottom; earlier text is not rewritten.

## 1. What this run is

A small, complete **pilot of the research process**, not a completion of issues
[#7](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/7) or
[#8](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/8).
Issue #10 is used only as an adversarial critical lens; it is **not** launched as its own
research project here, and no #10 deliverable is claimed.

Success is defined as: independent challenges materially test the evidence and produce a
traceable outcome — even if every original conclusion survives, or the empirical results are
negative.

## 2. Roles

| Role | Mandate | Must not |
|---|---|---|
| Researcher A | Issue #7 pilot: observed GenAI-generated SysML v2 error population, independently coded | Treat a validator verdict as ground truth; see B's results before freezing methodology |
| Researcher B | Issue #8 pilot: mutation-based validator evaluation + A's frozen findings as external challenge set | Let validator output define mutant ground truth; see A's results before freezing methodology |
| Reviewer A | Independent challenge to A's methods, evidence, interpretation | Edit A's artifacts |
| Reviewer B | Independent challenge to B's methods, evidence, interpretation | Edit B's artifacts |
| Semantic-ceiling critic | Adversarial critique grounded in #10: do either researcher's conclusions claim more than automated checking can establish? | Re-run #10 as a standalone study |
| Adjudicator | Reconcile challenges on documented evidence | Decide by majority vote or by authority |
| Team Lead | Orchestration, synthesis after adjudication, branches and draft PRs | Judge the researchers' evidence in place of reviewers/adjudicator |

A and B are separate agents with separate contexts. Neither reads the other's working
directory before the freeze gate (§4). The Lead does not relay in-progress findings between them.

## 3. Evidence rules (apply to every artifact in this run)

1. **SOURCE → EVIDENCE → INTERPRETATION → INFERENCE → DECISION** are separate and labelled.
2. Every substantive claim names the retrieved source, file and line, or the model excerpt.
   Training knowledge is not a source. No invented citations, URLs, page numbers or figures.
3. **Validator verdicts are never ground truth.** A model's defect status is established by
   the specification constraint, the observable model text, or an explicit authored expectation —
   recorded *before* a validator is run. Detection results are a separate measurement.
4. Denominators are stated for every frequency. Repeated publication is not corroboration.
5. Counter-evidence and dead ends are recorded, not omitted. "Not established" is a valid return.
6. Corpus/mutant provenance is recorded: who generated what, with which prompt/configuration,
   and what was modified. Raw artefacts are preserved unedited next to derived ones.
7. Anything unreachable (paywall, licence, missing release asset) is logged with the exact
   failure and what was tried; it is never silently replaced by a secondary source.
8. Pilot scale is stated plainly. A <200-model corpus makes #7 **preliminary** and it cannot be
   closed. #8's full evaluation criteria likewise are not met by this pilot.

## 4. Phases and gates

```
P0  Lead: protocol, tooling pinning, directory layout            [done before researchers start]
P1  Researchers A and B work independently.
    GATE 1 — both write METHODOLOGY-FROZEN.md (with sha256) before either sees the other's results.
P2  Cross-review, in both directions.
    GATE 2 — both cross-review records exist; each researcher writes a dated response.
P3  Researcher A freezes an empirical error subset (evidence-preserving, no validator input).
    Researcher B runs that subset as an *external* challenge set, separate from synthetic mutants.
P4  Independent reviewers (Reviewer A, Reviewer B) + semantic-ceiling critic.  [GATE 3]
P5  Adjudicator reconciles every challenge: accepted / rejected / unresolved.
    Unresolved stays visible; no majority vote; no self-judging.                  [GATE 4]
P6  Lead synthesis + student-facing demonstration map + core README updates.
    Branches and draft PRs; STOP at the human review gate. No merge, no issue closure.
```

Gate 1 exists to prevent hindsight-fitted methodology: each freeze file records what was decided
before any cross-review contact, and its sha256 is quoted in the researcher's own report.

## 5. Write scopes (disjoint; advisory, not locks)

| Owner | Paths |
|---|---|
| Researcher A | `research/issue-007/**`, `reports/issue-007-*.md`, `research/relational/cross-reviews/A-reviews-B.md`, `research/relational/empirical-subset/**` |
| Researcher B | `research/issue-008/**`, `reports/issue-008-*.md`, `research/relational/cross-reviews/B-reviews-A.md` |
| Reviewer A | `research/relational/reviews/reviewer-a-issue-007.md` |
| Reviewer B | `research/relational/reviews/reviewer-b-issue-008.md` |
| Semantic-ceiling critic | `research/relational/critique/**` |
| Adjudicator | `research/relational/adjudication/**` |
| Team Lead | `README.md`, `.gitignore`, `research/relational/PROTOCOL.md`, `research/relational/TOOLING.md`, `research/relational/README.md`, `research/relational/demo-map.md`, `reports/relational-demo-synthesis.md`, `catalogue/README.md` (cross-link only) |

Nobody edits another owner's files. Findings are communicated by message and by their own
review/critique artifacts.

## 6. Environment and tooling discipline

- Pinned tools and their hashes are in [`TOOLING.md`](TOOLING.md). Same binary for both
  researchers; a tool version change invalidates comparisons and must be re-run or reported.
- Validators that cannot be lawfully used here (e.g. a commercial tool requiring a licence key)
  are recorded as an access boundary, not worked around and not silently dropped.
- No git operations by researchers, reviewers, critic or adjudicator. The Lead owns branches,
  commits, pushes and pull requests, after Gate 4.
- No spawning of further agents, with one exception: Researcher A may use exactly one subagent
  as the independent second coder (see the assignment brief), and must record that subagent's
  brief and its independence limits.

## 7. Anti-circularity rules (specific)

1. B's mutant ground truth ("this model is defective, by constraint X at layer Y") is fixed and
   hashed before any validator runs. A validator's silence never reclassifies a mutant as valid.
2. A's error taxonomy is developed from the corpus by inspection against specification
   constraints. Validator diagnostics may be *recorded afterwards* as a detection column and as a
   cross-check on the *codebook's naming*, never as the criterion for what counts as an error.
3. The empirical challenge set in P3 is frozen from A's findings before B's validators see it, and
   is reported in a separate table from B's synthetic mutants.
4. Reviewers verify claims against raw evidence; they may re-run scripts but may not rewrite
   results. Adjudication cites artifacts, not personalities or model authority.

## 8. Known limits, stated up front

- Corpus and mutants come from the same model family that codes and inspects them (the research
  agents). Independence is procedural (separate contexts, frozen codebook, second coder), not
  human. This is a reported limitation, not a hidden one.
- Generator diversity in this pilot is low (one model family, a handful of configurations), so any
  frequency table is a property of *this* corpus, not of "LLM-generated SysML v2" in general.
- One open validator (OpenSysML v0.12.1) is the primary instrument; the second (OMG Pilot
  Implementation) is Java-dependent and may be unavailable. A one-instrument result is a
  calibration of that instrument, and the report must say so.

---

## Amendment A1 — 2026-11-13T14:35Z (Gate 2 response artifacts)

The Gate-2 responses are **separate files**, not edits to the reviewed cross-review:
`research/relational/cross-reviews/A-response-to-B-review.md` and
`research/relational/cross-reviews/B-response-to-A-review.md`. This keeps each cross-review
file byte-identical and hash-stable for the adjudicator.

Corrections to a researcher's own artifacts are made as **dated addenda** that preserve the
original claim text and state what changed, why, and on whose objection. No original claim is
deleted. If a correction changes a number, both the old and the new number remain visible with the
date of the change. Frozen methodology and pre-registered expectation files are never edited:
a change of method is an amendment, a change of expectation is an addendum with the original
expectation still visible.

---

## Amendment A2 — 2026-11-13T15:20Z (two process failures this run exposed)

Both failures recurred across researchers and are cheap to prevent. They are amendments to the
process, not corrections to any researcher's evidence.

**(i) Hash at freeze must cover the ground-truth artefact, not only the method.** Researcher B
froze a method hash before any mutant existed, which was exemplary; but the *external*
pre-registration hash was regenerated after the first run (ruling RB-01), and Researcher A's
frozen `errors.csv` was never hashed before the detection run (ruling B2A-05, withdrawn claim).
A hash of the protocol is not evidence that the measurements preceded the results. From the next
run onward: write `errors.csv.sha256` (or the corpus equivalent) **at the same time as** the
codebook freeze, before any instrument is run over it, and never regenerate a `.sha256` file —
a corrected artefact gets a new dated filename and a new hash.

**(ii) The artefact ledger is append-only.** The frozen 14-record file was correct and unchanged,
but its directory, the report and the response file all moved while reviewers held pinned hashes;
one reviewer's snapshot and the final bytes disagreed, and a "frozen at 14:29Z" label sat on a
file containing corrections dated 14:31Z. From the next run onward: every phase writes a new dated
file; the ledger records one row per write (`path, sha256, utc, author, supersedes`); and a file
declared frozen is never edited — a correction is a new file that names the superseded hash.

Neither amendment changes the evidence in this run. They are recorded because the demonstration's
value depends on the mechanism being real, not on the argument being persuasive afterwards.
