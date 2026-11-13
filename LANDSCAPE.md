# Research landscape — candidate questions

**Main question:** see [QUESTION.md](QUESTION.md).
**Status:** exploration only. Nothing here is selected, scheduled, ranked or started. Selection is the
human's, marked with the `selected` / `parked` labels on the issues. No dependency graph is implied;
where one brief's output would be useful input to another, that is noted as convenient ordering, not
as a blocker.

**Grounding:** three evidence notes gathered 2026-11-13, every claim URL-cited — [spec-tooling.md](evidence/spec-tooling.md)
(specifications, versions, validators, interchange), [literature.md](evidence/literature.md) (prior work,
evaluation designs, gaps), [industrial-practice.md](evidence/industrial-practice.md) (workflow, traceability,
expert judgement). The briefs cite these rather than restating received wisdom.

---

## The map

| # | Question | Dimension | Opens |
|---|---|---|---|
| [1](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/1) | Which well-formedness constraints are actually normative, and which are left to tool discretion? | A | Where "correct" comes from, and where it stops being specified |
| [2](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/2) | Do tools agree, and does validator acceptance predict downstream usability? | A / D | Whether "validates" is a property of the model, the tool, or the revision |
| [3](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/3) | What can a non-GenAI baseline achieve? | B | Whether GenAI is necessary at all |
| [4](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/4) | Does repair beat independent resampling at equal compute? | B | Whether iterative repair is architecture or expense |
| [5](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/5) | Is retrieval's benefit the content, or just the prompt? | B | Which part of "RAG helps" is real |
| [6](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/6) | Do structure-imposing strategies beat free-text generation? | B | The validity-versus-fidelity trade |
| [7](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/7) | What error populations do generated models contain? | B / C | The missing dependent variable for everything else |
| [8](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/8) | How reliable are validators as measuring instruments? | C | Whether validator pass rates mean anything |
| [9](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/9) | Can fidelity be scored automatically, and does it agree with experts? | C / E | The circularity, broken |
| [10](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/10) | What can semantic checking establish — where is the ceiling? | C | The structural limit of automated validation |
| [11](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/11) | Does a generated model survive requirement change? | D | File generation versus industrial integration |
| [12](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/12) | Are generated traceability links trustworthy? | D | Invention, and whether it can be detected |
| [13](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/13) | What would a defensible benchmark require — including abstention? | E | Comparability, and the right behaviour on bad requirements |
| [14](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/14) | How do systems engineers actually review a generated model? | D / E | Usability as a measured quantity; the judgement boundary |

Five dimension-A/B questions, four on validation, three on industrial integration, three on evaluation.
Deliberately not a taxonomy: each brief is a question someone could investigate, not a category.

---

## 1. What is already known

Established, and **not** contributions this project can claim:

- **The specifications are formal and pinned.** SysML 2.0, KerML 1.0 and the Systems Modeling API 1.0 are
  OMG-adopted (September 2025); documents `formal/26-03-02`, `formal/26-03-01`, `formal/26-03-04`. KerML
  supplies the semantic foundation. Note the date conflict: catalogue pages say September 2025, the PDFs
  say March 2026.
- **The reference tooling does not implement the formal documents.** Since its 2026-07 release the pilot
  targets *SysML 2.1 Beta 2 / KerML 1.1 Beta 2*, and `omg.org/spec/SysML/2.1` returns 404. Metamodel
  identity is frozen at `20250201`, so a serialised model carries no readable statement of which semantics
  it was written for.
- **Validation is three layers deep and no deeper.** Parse, name resolution, and OCL constraints — one
  Xtext validator file. No standalone validator binary in any release. No type checking or inference by
  design. No execution of actions or state machines. No OMG conformance suite.
- **GenAI can produce SysML v2 that parses, given help.** Cibrián et al. (2025): 0% to 55% syntactic
  validity from RAG alone, 100% with an ANTLR-validated repair loop. The MDPI study (2026): requirements
  F1 of 0.80 under RAG upload. Both peer-reviewed, both real results.
- **Those results have specific, documented weaknesses.** Neither used independent ground truth, held-out
  tasks, or a human expert panel with inter-rater agreement; both ran the repair loop inside the
  measurement; both generate once per configuration; neither reports failure rates after repair; neither
  releases artefacts.
- **Semantic correctness is where it breaks.** The one study separating grammar accuracy from semantic
  accuracy reports >90% grammar accuracy but semantic F1 of 95% for activity diagrams and **50% for
  sequence diagrams**.
- **Nothing in this field is comparable.** Three mutually incompatible validity gates (ANTLR grammar,
  commercial-tool import, dataset-specific semantic F1) and no shared protocol.
- **Industrial practice asks for more than a file.** Quality is company-, role- and phase-specific; experts
  "cannot use existing standards and norms, because these are too general"; and model version control
  fails on identity loss when models are restructured.

## 2. What remains uncertain

- Whether a non-GenAI pipeline covers most of the task, making the GenAI contribution the residue. No
  baseline exists anywhere in this literature.
- Whether iterative repair causes the validity gains, or merely samples more expensively.
- How much of retrieval's benefit is retrieved content as opposed to prompt length or format.
- Whether validator acceptance predicts usability in any tool.
- The false-negative rate of validators — never measured, against a suspicious documented history of
  unchecked constraints and an admitted suppression.
- Whether automated fidelity scores track expert judgement — no calibration study exists.
- What proportion of generated traceability is invented but plausible — never measured.
- Whether a generated model survives a requirement change with reviewable diffs — asserted, not measured.
- Whether validation reports help or harm a reviewing engineer — no study of systems engineers consuming
  LLM-generated SysML exists at all.
- Whether SysML v2's claimed formal semantics are usable for checking, given that accessible documentation
  was reported unavailable.

## 3. What can be investigated empirically

All fourteen, though not at equal cost. Roughly by shape:

- **Cheap and immediately actionable:** 4 (repair versus resampling), 7 (error taxonomy), 3 (non-GenAI
  baseline), 5 (retrieval decomposition) — these need a corpus and a validator, nothing more.
- **Instrument-building, high reuse:** 8 (validator reliability), 9 (fidelity metric), 1 (constraint
  catalogue), 13 (benchmark design).
- **Needs infrastructure or access:** 2 (multiple toolchains), 11 (change sequences), 12 (OSLC surface).
- **Needs human participants, and is therefore the binding constraint:** 9 and 14, and partly 13. These
  should be scoped only once a recruitment route through Fontys ICT / industry partners is confirmed.

**Project constraints applied:** no paid or enterprise licences — which removes the commercial modelling
tool used as a validity gate in one anchor, and requires the alternative routes proposed in 2, 11 and 12;
one semester, one or two students — which rules out 13 at full scale (design plus pilot only) and makes 9
and 14 dependent on an existing partner relationship; reusable artefacts — 1, 7, 8, 9 and 13 all produce
assets a partner could keep running; publishability — every brief above has a reportable outcome under
either polarity, which matters most for 3, 4 and 5 where the negative result is the likely and valuable one.

## 4. What would constitute convincing evidence

Shared requirements, applied per brief in its own section:

- An **oracle that is not the system under test.** Validator-as-oracle is not acceptable until brief 8
  shows the validator is a reliable instrument.
- **Ground truth whose independence is argued**, not assumed — including who authored references and what
  they had seen.
- **More than one run per configuration**, with variance reported. Single-generation cells with two-decimal
  means are the specific weakness that makes the existing literature's cross-configuration claims
  unfalsifiable.
- **Compute- and sample-matched comparisons** where a budget is a confound.
- **Both error rates.** False positives matter as much as false negatives: the adjacent evidence says
  false alarms and warning presentation, not detection gaps, are what stop practitioners using analyzers.
- **Published artefacts** — prompts, models, codebooks, mutants, references — since neither anchor releases
  anything, and that is the cheapest available improvement on the state of the art.
- **Negative results reported as results.** The literature has none, and their absence is not neutral.

## 5. Where human engineering expertise remains indispensable

This is the part the landscape should protect, not minimise:

- **Deciding what the model should say.** Whether something is an item, a part or an attribute; how
  structure and behaviour connect; whether a decomposition suits its audience. These are adequacy
  questions, and no constraint names them.
- **Judging fidelity and elaboration.** Distinguishing legitimate engineering elaboration from invention
  is the crux of brief 12, and it is not obviously mechanisable.
- **Being the criterion for measurement.** Briefs 9 and 14 need experts as the external standard. There is
  no substitute, and using students or the project team would reproduce exactly the flaw the anchors are
  criticised for.
- **Deciding what a validation report means.** A passing validator licenses a claim about syntax, not about
  the system.
- **Setting method-level constraints.** The standard itself defers these to adopters, and in current
  tooling each organisation authors its own validation rules.

---

## Judgement on the set

**Strongest, most defensible:** 8 (validator reliability) and 7 (error taxonomy). Both are cheap, both
produce reusable artefacts, both can report a clean negative result, and both are prerequisites for
believing anything else. 10 is close behind as the honest counterweight to the parse-success metric.

**Highest novelty and highest risk:** 13's abstention rubric — scoring a system on correctly *not* producing
a model on a contradictory requirement is the most original idea here and the least proven; if experienced
engineers cannot agree on what a correct ambiguity response is, the construct collapses.

**Most likely to be low-yield, and worth saying so:** 6 (structure-imposing strategies). Constrained
decoding against a specification grammar may simply not be tractable within a semester with open tooling,
and the audit-objective cost is high. 2 is the most infrastructure-heavy for a result that may reduce to
"the tools are immature".

**Most likely to change the programme's direction:** 3. If a competent non-GenAI baseline covers most
requirements, the framing of the whole project shifts — and that would be a finding, not a setback.

**Genuine soft ordering** (convenience, not dependency): 7 supplies the fault catalogue for 8; 9 calibrates
whatever judge 13 and 14 rely on; 1 defines the constraints that 8 measures against. None of these blocks
another, and none should be used to defer a question the human actually wants answered.
