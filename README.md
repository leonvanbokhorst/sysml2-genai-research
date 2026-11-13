# GenAI-assisted SysML v2 model generation and validation — research workspace

**Project:** master's research project, Fontys ICT — *GenAI-assisted SysML v2 model generation and
validation*.
**Status:** exploration. The research landscape exists as GitHub issues; a few have been
researched. Nothing is merged into a thesis claim, and no issue is closed on the strength of a
pilot.

> **Main question.** How can a GenAI-based system generate SysML v2 system models that are
> correct, consistent, and aligned with industrial Model-Based Development workflows, and how can
> such models be reliably validated using automated evaluation techniques?

See [`QUESTION.md`](QUESTION.md) for how that bundles into generation / validation / usability
claims, and [`LANDSCAPE.md`](LANDSCAPE.md) for the map of candidate questions.

## How this repository works

The repository is the lab notebook, not the paper. It is organised so that **a claim is separable
from the evidence under it**, and so that disagreement is visible rather than smoothed away.

```
QUESTION.md ──► LANDSCAPE.md ──► GitHub issues (one bounded research question each)
                                      │
                ┌─────────────────────┴─────────────────────┐
                ▼                                           ▼
        evidence/ (source notes, URL-cited)        catalogue/ (spec-derived instruments)
                │                                           │
                └──────────────► agents research one issue each
                                      │
                     artifacts + report + raw evidence in the repo
                                      │
                     cross-review / independent review / adjudication  ◄── human review gate
                                      │
                              pull request ──► main
```

Working rules the repository holds itself to:

- **Evidence before interpretation.** Claims carry the retrieved source, file and line. Raw
  artefacts are preserved next to derived ones.
- **Validators are instruments, not oracles.** A validator pass is a measurement of a tool, not a
  proof of correct modelling — a distinction that has its own brief ([#8](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/8)).
- **Pilots say they are pilots.** A small corpus makes an issue *preliminary*; it does not close it.
- **Challenges stay on the record.** Review objections, responses, revisions and adjudicated
  rulings are separate, inspectable files. Unresolved disagreements remain visible.

## What exists now

| Area | Artefact | State |
|---|---|---|
| Landscape and question | [`QUESTION.md`](QUESTION.md), [`LANDSCAPE.md`](LANDSCAPE.md), 14 candidate issues [#1](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/1)–[#14](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/14) | exploration; selection is the human's |
| Evidence base | [`evidence/spec-tooling.md`](evidence/spec-tooling.md), [`evidence/literature.md`](evidence/literature.md), [`evidence/industrial-practice.md`](evidence/industrial-practice.md) | three URL-cited notes, gathered 2026-11-13 |
| Issue #1 — constraint catalogue | [`catalogue/`](catalogue/) · [`report`](reports/issue-001-constraint-catalogue.md) | complete: 623 named SysML v2/KerML well-formedness constraints, classified and traced to pinned OMG artefacts |
| Issue #7 pilot — error population | [`research/issue-007/`](research/issue-007/) · [`report`](reports/issue-007-error-taxonomy-pilot.md) | **preliminary pilot** — coded corpus, dual coding, detection map, cross-reviewed and adjudicated; cannot close #7 |
| Issue #8 pilot — validator reliability | [`research/issue-008/`](research/issue-008/) · [`report`](reports/issue-008-validator-reliability-pilot.md) | **preliminary pilot** — mutation study plus an external challenge set, one pinned open instrument; cannot close #8 |
| Relational demonstration (#7 × #8, #10 lens) | [`research/relational/`](research/relational/) · [`demo map`](research/relational/demo-map.md) · [`synthesis`](reports/relational-demo-synthesis.md) · [`adjudication`](research/relational/adjudication/ADJUDICATION.md) | pilot of the review process: cross-reviews, two independent reviews, a #10 critique, 81 adjudicated entries (64 accepted challenges, 3 rejected, 4 unresolved, 10 status propositions upheld); stops at the human review gate |

Each research issue states its own working scope, exclusions, falsification criteria and what
would count as convincing evidence — see the issue text, not a summary here.

## Repository map

```
QUESTION.md  LANDSCAPE.md          the question, and the candidate briefs
evidence/                          source-grounded notes the briefs cite
catalogue/                         issue #1: the constraint instrument (623 constraints, pinned)
research/
  issue-007/                       corpus, codebook, coded errors, agreement, detection mapping
  issue-008/                       known-good models, mutants, harness, validator results
  relational/                      protocol, frozen methods, cross-reviews, reviews, critique,
                                   adjudication, demo map — the process record
reports/                           one report per research run (findings, limits, sources)
```

**New here?** Read [`research/relational/demo-map.md`](research/relational/demo-map.md) — it shows
the sequence of research decisions and the evidence each one rested on, which is the fastest way to
see how a claim in this repository is produced, attacked and either survives or changes.

## Reproduce the main artefacts

Everything is plain Python/CSV/Markdown and offline once pinned inputs are fetched. Full
instructions live beside each artefact; the two entry points worth knowing:

```bash
# Issue #1 — rebuild the constraint catalogue from pinned OMG XMI + PDFs
python3 catalogue/extract_constraints.py --fetch --source-dir /tmp/sysml --out-dir catalogue
python3 catalogue/classify.py --catalogue catalogue/constraints.csv \
    --defects catalogue/ocl-defects.csv --out catalogue/classified.csv \
    --summary catalogue/classification-summary.json

# Issue #8 pilot — re-run the pinned validator over the mutant corpus
python3 research/issue-008/harness/run_validators.py      # see research/relational/TOOLING.md
```

## Pinned artefacts and tooling

Specification inputs are pinned by document number and sha256 in
[`catalogue/README.md`](catalogue/README.md) §1. Research tooling is pinned by release and
sha256 in [`research/relational/TOOLING.md`](research/relational/TOOLING.md), together with the
access log: what could not be used lawfully (e.g. a validator requiring a commercial licence) is
recorded as a boundary rather than worked around.

## Contributing and research workflow

Human selection of a question is authoritative; agents do not choose their own task. A research
contribution is expected to arrive as a branch plus a pull request containing, at minimum, the
artifacts, the raw evidence, a report with stated limits, and the access log. Review is a
gate, not a formality: see [`research/relational/PROTOCOL.md`](research/relational/PROTOCOL.md)
for the version of the process used in the #7/#8 demonstration.

Nothing in this repository is a claim about "LLM-generated SysML v2" in general. Pilot results
are properties of the corpus, tool version and method reported with them.
