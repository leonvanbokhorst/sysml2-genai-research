# Relational research demonstration — issues #7, #8, with #10 as critique

This directory is the **process record** of a bounded pilot in which two research agents worked
on separate questions, challenged each other, were independently reviewed, and had their
disagreements adjudicated. The research artifacts live in
[`../issue-007/`](../issue-007/) and [`../issue-008/`](../issue-008/); this directory holds the
material that only exists *because* the work was relational.

**Status: pilot, preliminary, stopped at the human review gate.** Nothing here closes issue #7 or
issue #8, and #10 was used as a critical lens, not launched as a study.

## Artifact map

| Path | What it is | Author |
|---|---|---|
| [`PROTOCOL.md`](PROTOCOL.md) | Frozen operating protocol written before the researchers started: roles, phases, gates, evidence rules, anti-circularity rules, write scopes | Team Lead |
| [`TOOLING.md`](TOOLING.md) | Pinned tool versions, hashes, and the access log (what could and could not be lawfully run) | Team Lead |
| [`METHODOLOGY-FROZEN.md`](../issue-007/METHODOLOGY-FROZEN.md) (A) / [`METHODOLOGY-FROZEN.md`](../issue-008/METHODOLOGY-FROZEN.md) (B) | Each researcher's methodology, frozen and hashed before seeing the other's results | Researcher A / B |
| [`cross-reviews/`](cross-reviews/) | A's challenge to B's mutants; B's challenge to A's classifications, with each researcher's dated response | Researcher A, Researcher B |
| [`empirical-subset/`](empirical-subset/) | A's frozen subset of observed errors, handed to B as an external challenge set | Researcher A |
| [`reviews/`](reviews/) | Independent reviews of each pilot (methods, evidence, interpretation) | Reviewer A, Reviewer B |
| [`critique/`](critique/) | Adversarial critique grounded in #10: are the conclusions claiming more than automated checking can establish? | Semantic-ceiling critic |
| [`adjudication/`](adjudication/) | Accepted / rejected / unresolved rulings on every challenge, with evidence | Independent adjudicator |
| [`demo-map.md`](demo-map.md) | Student-facing map of the sequence of decisions, gates and evidence dependencies | Team Lead |
| [`synthesis`](../../reports/relational-demo-synthesis.md) | What changed because agents challenged one another | Team Lead |

## The gate sequence

1. **Gate 1 — Freeze.** Both researchers wrote and hashed their methodology before any
   cross-review contact: neither could fit its method to the other's results.
2. **Gate 2 — Cross-review.** Each researcher read the other's *artifacts* (not their reasoning)
   and wrote specific objections, then responded to the objections against themselves.
3. **Freeze of A's empirical subset.** A's observed errors became B's external challenge set,
   so B's synthetic fault model could be tested against errors that actually occurred.
4. **Gate 3 — Independent review.** Two reviewers, each with a fresh context and no stake in the
   pilot, plus a #10-grounded critic.
5. **Gate 4 — Adjudication.** An independent adjudicator ruled on every challenge on documented
   evidence. Majority vote and model authority were not admissible.

## What the protocol forbids

- Validator verdicts as ground truth (they are the object of measurement in #8, and a detection
  measurement in #7).
- Hindsight-fitted methodology, silent substitution of a secondary source, or invented evidence.
- Resolving disagreements by consensus, by asking the same model to judge its own work, or by
  editing a researcher's conclusion in place — corrections are recorded as adjudicated rulings,
  and unresolved disagreements stay on the record.
- Merging, closing issues, or expanding to further research questions: this run stops at the
  human review gate.

## Reproduce

```bash
# Validator (pinned, open source) — see TOOLING.md for hashes
mkdir -p .tools && cd .tools
curl -sSLO https://github.com/Open-MBEE/OpenSysML/releases/download/v0.12.1/opensysml-darwin-arm64.tar.gz
shasum -a 256 opensysml-darwin-arm64.tar.gz    # 0f16d282...c96210
tar xzf opensysml-darwin-arm64.tar.gz
cd .. && .tools/sysml -version                 # v0.12.1, commit b2f0e9b

# Researcher scripts (offline, self-contained)
python3 research/issue-007/coding/agreement.py
python3 research/issue-008/harness/run_validators.py
```

The raw corpus, raw validator outputs and every intermediate table are preserved beside the
derived ones, so a reviewer can re-derive the published numbers rather than trust them.
