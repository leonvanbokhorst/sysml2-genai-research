# Main research question

**Project:** GenAI-assisted SysML v2 Model Generation and Validation
**Context:** Master's research project, Fontys ICT
**Status:** exploration — candidate questions only; nothing selected, scheduled or started

> How can a GenAI-based system generate SysML v2 system models that are correct, consistent, and aligned with industrial Model-Based Development workflows, and how can such models be reliably validated using automated evaluation techniques?

This file records the question only. It is not a queue. The research landscape lives in the
repository's GitHub issues; selection and prioritisation are the human's, marked with the
`selected` / `parked` labels.

## Structure of the question

The question bundles three claims that have to be separated before any of them can be tested:

1. **Generation** — that a GenAI system can produce SysML v2 models at all, and better than
   available alternatives.
2. **Validation** — that automated techniques can establish the models are correct, consistent
   and faithful to their sources, and that the validators themselves can be trusted.
3. **Usability** — that the results are usable by systems engineers inside real Model-Based
   Development workflows.

The candidate briefs deliberately do not treat (1) as the centre of gravity. A syntactically
valid SysML v2 model is not necessarily a correct system model, and an automated check is not
evidence until the check has been shown to be reliable.

## Guiding constraint

Do not assume an agentic architecture, RAG, fine-tuning, or iterative repair is the right
solution. Each is a hypothesis with a competing baseline, and several have published evidence
against them (see `evidence/literature.md`).

## Grounding

`evidence/` holds three evidence notes gathered 2026-11-13, each claim URL-cited:
what the formal specifications and tooling actually do, what the prior literature
established and where its evaluation designs are weak, and what industrial MBSE practice
requires of a model. Briefs cite these rather than restating received wisdom.
