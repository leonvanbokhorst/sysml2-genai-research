# METHODOLOGY — FROZEN BEFORE DATA COLLECTION (issue #7 pilot)

**Author:** Researcher A (independent research agent, issue #7 pilot)
**Frozen at:** 2026-11-13T14:05:30Z (UTC), by `date -u` in this workspace.
**Status:** frozen. This file is not revised. Corrections and changes of plan are appended as
dated amendments at the bottom (§15), with the reason and the time of the change.

**Freeze statement.** This document was written **before** any model was generated, before any
corpus text was inspected, before any codebook existed, and **before** Researcher B's results,
artefacts or review were seen. I have not read `research/issue-008/**` or
`research/relational/cross-reviews/**` at the time of writing, and I will not read them until the
Lead opens the Gate-2 cross-review. The sha256 of this file is quoted in
`reports/issue-007-error-taxonomy-pilot.md`; that hash is the evidence that the plan preceded the
data.

---

## 1. Research question and scope (as authorised)

**Question (issue #7, pilot subset):** *What error population does a corpus of GenAI-generated
SysML v2 models actually contain?* Concretely: build the error population bottom-up from model
text, code it twice, and report frequencies with stated denominators and a detection-layer map.

**Not the whole of issue #7.** Issue #7 requires ≥200 models across several tasks, models and
prompting strategies. This pilot targets **N = 18 models**. It is a complete demonstration of the
process at small scale, **not** a completion of #7. No claim in the report is a claim about
"LLM-generated SysML v2" in general; every frequency is a property of this corpus.

**Unit of analysis:** one *model output* = one (task, configuration) cell. Errors are coded
inside a model output; a model output may carry several errors, or none.

**In scope**

- Corpus construction and its provenance (prompts, configurations, generation conditions).
- Raw-output preservation including wrappers (markdown fences, preamble, trailing prose).
- Normalisation of raw output to intended SysML text, with every extraction decision logged.
- A bottom-up error codebook with mutually exclusive classes, inclusion/exclusion criteria,
  worked examples, and a layer + specification-constraint mapping.
- Double coding of a subset by an independent second coder; agreement statistics.
- A separate **detection measurement**: which coded errors the pinned validator notices.
- A bounded mechanism test of the "wrapper vs modelling" question suggested by the anchor's
  0 %-vs-100 % anomaly.

**Out of scope (explicit exclusions)**

- Whether a model is *right for the system* it describes (fidelity / adequacy) — issue #9/#12/#14
  territory. I code defects in the model **text as SysML v2**, not disagreements with the
  requirement paragraph, except where the model text is internally incoherent or contradicts
  itself, which is a model-text property.
- Model-vs-model quality comparison as an object of study. Configuration identity is a
  stratifying variable only.
- Any re-run of issue #10 (semantic ceiling) or #8 (validator reliability). The detection column
  is a measurement of one instrument on this corpus, nothing more.
- A validator verdict is **never** the criterion for an error (§7).

---

## 2. Corpus construction plan

### 2.1 Step 1 — bounded search for an existing public corpus (≤15 minutes)

Before generating anything, search for a publicly available corpus of LLM-generated SysML v2
model text: GitHub code/repository search, dataset registries (Zenodo, Hugging Face, figshare),
papers with released artefacts. Log every query, URL and outcome in
`research/issue-007/corpus/PROVENANCE.md` and in the report's investigation log.

Prior expectation, recorded now so that it cannot be presented as a discovery later: the anchor
study (Cibrián et al. 2025) states "data available on request" and its threats-to-validity
analysis in `evidence/literature.md` §4.12 records that neither anchor releases prompts,
reference models or per-output artefacts. Wang et al. 2025 reports a *SysML behaviour-model*
dataset (107 models) that is human/curated reference material rather than LLM outputs.
**Selection criterion if something is found:** it must (a) be LLM-generated SysML **v2 textual
notation**, (b) include raw outputs with wrappers, (c) be openly downloadable without bypassing
an access control, (d) carry traceable per-output prompt and generator identity. A corpus that
fails (a)–(d) is logged as unusable rather than stretched. If nothing qualifies, the search is
recorded as a failed-access/dead-end entry and I fall back to §2.2.

### 2.2 Step 2 — own corpus (the planned primary route)

**Task prompts:** 6 prompts of my own design, written before generation, stored verbatim in
`research/issue-007/corpus/prompts.md` with a stated design rationale. Each is a
system-engineering-style requirement paragraph modelled on the *shape* of published prompt sets
(a short paragraph naming a system, some structure, and at least one obligation), and each asks
for **structure plus at least one requirement/`satisfy` and one behaviour or connection**, so
that the corpus exercises more than one language area. Domains are varied and deliberately
generic (no SysML tutorial clichés reused verbatim). Constraints on prompt design:
no example SysML text, no constraint names, no hints about the codebook — prompts must not
encode the error taxonomy.

**Configurations:** 3 prompting configurations, applied to every task:

| ID | Configuration | Exact instruction |
|---|---|---|
| **C1** | Single-shot free text | The task paragraph only; model answers however it likes. |
| **C2** | Fenced block demanded | The task paragraph plus an explicit instruction to return the model inside a ```` ```sysml ```` fenced code block and nothing else. |
| **C3** | Structured / checklist-guided | The task paragraph plus a short ordered checklist of modelling obligations (name the package, define the parts, declare at least one requirement and one `satisfy`, give one behaviour or connection, state that the output must be a single SysML v2 model). The checklist states *what to include*, not *how to be correct*. |

**Design size:** 6 tasks × 3 configurations = **18 model outputs**, one generation per cell.
One generation per cell means **no variance estimate and no repeatability claim**; this is stated
as a limitation, not repaired with a second run (§14).

**Generator identity (honest record):** every output is produced by the same DeepSeek-family
model served through DSH, the agent runtime this session runs on. The **exact checkpoint is not
exposed** to me and I do not claim one. I am therefore both the generator and coder A — a
circularity that is a stated limitation (§14.1), mitigated procedurally, not eliminated.

### 2.3 Generation discipline

1. All 6 prompts are finalised and stored before the first generation.
2. Generations are produced **in one pass**, cell by cell, each written immediately to
   `research/issue-007/raw/<model_id>.md` as a verbatim record of what the "model turn" produced,
   including fences, preamble, trailing prose, apologies and refusal text. Nothing is trimmed,
   repaired or re-generated. If a cell produces something unusable, that is data.
3. Configuration text is not varied between tasks. Temperature/decoding parameters are not
   available to me as a knob; this is recorded rather than pretended.
4. No feedback loop, no repair pass, no validator in the loop: first output only. This is a
   deliberate difference from both anchors, whose repair loops sit inside their measurement.
5. `research/issue-007/corpus/manifest.csv` records per model: `model_id, task, configuration,
   generator, generation_timestamp_utc, char_count, sha256_raw, raw_path`. Character counts and
   hashes are computed from the files on disk, not typed by hand.

---

## 3. Normalisation plan

`research/issue-007/corpus/extract.py` converts each raw output to
`research/issue-007/corpus/normalized/<model_id>.sysml` by **removing wrapper material only**:

- If the raw output contains one or more fenced code blocks, the intended model is the block
  whose content is SysML v2 (language tag `sysml`/`sysmlv2`/none/`text`), chosen by a stated
  rule; the block is extracted **verbatim**, fences removed, content otherwise untouched.
- Preamble and trailing prose are removed and recorded verbatim in the extraction log.
- **No semantic repair.** No token is added, renamed, reordered or deleted inside the extracted
  model body. No missing import is added. No typo is fixed. Indentation is preserved as-is.
- If no fence exists, the whole raw text is the candidate model; leading/trailing prose is NOT
  stripped, because deciding where prose ends and the model starts is itself a judgement that
  would destroy the wrapper/formatting signal. It is flagged `no_fence` and the model is coded
  as-is.
- Multiple fenced blocks: the first block containing a SysML keyword (`package`, `part`,
  `requirement`, `action`, `state`, `connection`, `attribute`, `port`, `import`) is taken as the
  intended model; other blocks are logged as `extra_blocks` with their hashes, and are not coded.
- Every decision is written to `research/issue-007/corpus/extraction-log.json` with the rule ID
  that fired. The script must be deterministic and re-runnable with no network.

Wrapper status is therefore recorded **independently of** the model's SysML quality, so that
"invalid only because of the wrapper" is computable (§9).

---

## 4. What counts as an error — operational definition (frozen)

> **An error is a property of the model text**: a construct in the normalised model that
> (E1) cannot be parsed under the SysML v2 textual-notation grammar, **or** (E2) refers to
> something the model does not provide (unresolved name, missing end, dangling reference),
> **or** (E3) violates a named well-formedness constraint of SysML 2.0 / KerML 1.0 as
> catalogued in `catalogue/classified.csv` (constraint name + clause recorded), **or**
> (E4) is internally incoherent such that no reading of the model text makes the construct mean
> what its own syntax says it means (e.g. a `satisfy` whose subject is not a requirement usage;
> a behaviour declared but connected to nothing while the model claims the connection).

Coding is **by inspection against the constraint catalogue and the model text**, at the level of
the smallest text span that carries the defect (one error record = one defect, one excerpt).

**Error is not:**
- a stylistic choice (ordering, naming, comments, formatting inside the model body);
- a granularity or decomposition choice, or a legitimate alternative modelling of the same
  requirement (part vs attribute, one action vs three);
- content the prompt did not ask for, unless it makes the model internally inconsistent;
- anything established only by a validator. A validator diagnostic is never sufficient to code
  an error, and the validator not complaining never removes one (§7).

**Severity (frozen scale, used as a coding property, not a quality judgement):**
- `blocking` — the model cannot be loaded/parsed at all (E1), or the defect prevents the
  construct from resolving (E2);
- `major` — the construct resolves but violates a normative constraint (E3) or is incoherent (E4);
- `minor` — a localised defect that is real but does not stop the model from being interpreted
  (e.g. a redundant or unused declaration that the constraint set flags).

---

## 5. Coding procedure and codebook development (plan)

1. **Open pass (no codebook).** Read all 18 normalised models in task order, writing free-text
   observations per model. No categories fixed in advance.
2. **Cluster.** Group observations into candidate classes; write inclusion/exclusion criteria and
   one worked example per class from the corpus. Classes must be **mutually exclusive at the
   error-record level**: each record gets exactly one class; when a defect could fit two, the
   rule is "the class of the *mechanism* that produces the defect, not of its surface symptom",
   and the tie-break is recorded in the codebook as an explicit precedence rule.
3. **Layer mapping.** Every class maps to exactly one detection layer:
   `wrapper/formatting`, `syntax/parse`, `name resolution`, `constraint/OCL`, `type/typing`,
   `semantic/behavioural`, `structural/architectural`. Class → layer is part of the codebook.
4. **Constraint mapping.** Where a catalogue constraint names the violation, cite the
   constraint name and clause from `catalogue/classified.csv`; leave empty when no named
   constraint covers it (and say so — those are the classes the specification does not name).
5. **Frozen codebook.** Final version written to `research/issue-007/coding/CODEBOOK.md` with a
   revision table (date, change, why), then hashed. Coding of coder A's labels is completed
   **before** the codebook is frozen? — No: the frozen codebook is the one both coders use. Order
   is: open pass → draft codebook → coder A codes all 18 with the draft → codebook revised once
   if a model forces a class split/merge (each revision dated and reasoned) → **freeze + hash** →
   second coder labels 12 models using only the frozen codebook. Coder A's labels are re-checked
   against the frozen codebook after freeze; any label that the frozen text no longer supports is
   corrected **and the correction logged** (not silently).
6. **Error records.** `research/issue-007/coding/errors.csv`, one row per error:
   `model_id, error_id, class, layer, severity, evidence_excerpt, line_range, spec_constraint, notes`.
   Models with zero errors are recorded explicitly in a separate `models.csv` (one row per model,
   `n_errors`, `wrapper_status`, `parses_as_is`) so that the denominator is auditable.

---

## 6. Second coder and agreement (plan)

- Exactly **one** `subagent`, fresh context, used only as second coder (the single delegation
  permitted by `PROTOCOL.md` §6).
- It receives **only**: the frozen codebook text, 12 selected normalised models with their raw
  wrappers, a blank CSV schema, and instructions to label independently. It does **not** receive
  coder A's labels, the error counts, the taxonomy rationale, or any hint of expected classes.
- Selection of the 12: **stratified by task and configuration** (all 6 tasks represented, all 3
  configurations represented), chosen by a rule fixed now: for each task, take C1 and C2, plus
  two tasks' C3 — i.e. 12 of 18 — so that both wrapper variants and the checklist variant appear.
  (Which two C3 cells is decided by a deterministic rule at the time: lowest model_id hashes;
  recorded in the selection file.)
- Models are presented to the subagent **in the same form coder A saw** (normalised text plus
  the raw wrapper, labelled separately), because the codebook requires distinguishing wrapper
  from modelling defects.
- **Independence is limited and is stated as such:** the second coder is the same model family,
  served through the same runtime; it has no memory of this session but no epistemic independence
  from the generator. This is the procedural independence the protocol anticipates, not human
  independence.
- **Agreement metrics:** percent agreement (primary, reported with raw counts), Cohen's κ
  overall on the model-level "error present/absent" and on the class label per coded error;
  Krippendorff's α (nominal) if class marginals make κ unstable; a disagreement table listing
  every disputed record with both coders' class and excerpt. κ is reported with its known
  prevalence sensitivity stated (Feinstein–Cicchetti), never as a bare number. Disagreements are
  **not** smoothed: they are reported and, where the codebook is at fault, appended as a dated
  amendment rather than retro-applied.
- Agreement is computed by `research/issue-007/coding/agreement.py` (self-contained, no network),
  emitting `agreement.json` and `agreement.md`. The script asserts the id sets match.

---

## 7. Detection layer measurement (plan; runs only after coding is frozen)

1. After `errors.csv` and the codebook hash are final, run the pinned OpenSysML CLI v0.12.1
   (`.tools/sysml`, sha256 `ddfc2962…1598f0`, per `TOOLING.md`) on **each normalised model**
   (`-validate`, plus `-format json` for machine-readable diagnostics) and on **each raw output**
   that is not syntactically valid SysML as-is.
2. Diagnostics are recorded **verbatim** in `research/issue-007/detection/raw/` with the exact
   command line, exit code, tool version and per-file sha256.
3. Build a table: for each coded class, how many coded errors did the tool report (detected /
   silent), at which severity, and which diagnostics fired. Recall per class is
   `detected errors / coded errors in that class`, with the denominator printed.
4. **The tool cannot change a label.** Where a diagnostic seems to contradict a coded error, the
   contradiction is recorded and investigated against the specification; the error is not
   reclassified on the tool's authority. Where the tool's silence is explained by a known
   capability gap, that is recorded as an instrument property.
5. **Known confound, recorded in advance:** without `private import ScalarValues::*;` (or a
   library prelude), a bare `Real`/`Integer`/`String` is reported as unresolved. Wrapper
   omission of an import therefore shows up as a name-resolution diagnostic. I will report how
   many models have the prelude and how many diagnostics are of that form, so that this is
   visible rather than absorbed into a "name resolution" count.

---

## 8. Reproduction arm (plan; honest and bounded)

The anchor's design **cannot be re-run**: Cibrián et al. publish the 20 prompt texts but release
no reference models, no prompts file, no code, and no per-output artefacts
(`evidence/literature.md` §4.12), and Anchor B releases nothing either. Neither their generator
versions nor their parser is available to me. **I will not claim to have reproduced or refuted
any anchor number.**

What is testable within this corpus is the *mechanism hypothesis* their 0 %-versus-100 % pattern
suggests: that the dominant failure is **wrapper/formatting** (markdown fences, preamble prose,
refusal text) rather than SysML modelling. Two counts will be reported over the 18 models:

- **V1 — invalid only because of the wrapper:** raw output fails when fed to the validator as-is
  *and* the normalised model validates clean;
- **V2 — invalid after normalisation:** the normalised model still produces diagnostics.

with the class distribution behind each count. This is a mechanism test on *my* corpus, at
n = 18, reported as such. It cannot confirm or refute the anchor's numbers; it can only say
whether the wrapper explanation is *available* in this corpus and how large it is here.

---

## 9. Metrics (all with denominators)

1. `N_models` = 18; `N_models_coded`; `N_models_with_zero_errors`.
2. Errors per model: total, mean, median, min, max; per configuration (C1/C2/C3); per task (T1–T6).
3. Class frequency: count per class, **denominator = all coded errors** (and separately,
   denominator = models, as "models containing ≥1 error of class X").
4. Layer frequency with the same two denominators.
5. Wrapper status: fenced / unfenced / prose-embedded / multiple blocks; and V1/V2 counts (§8).
6. Detection: recall per class, plus total diagnostics by severity and by the tool's own layer
   labels, plus diagnostic count per model.
7. Agreement: percent agreement, κ (overall and per class where defined), α if warranted,
   disagreement count and table.
8. All frequency tables are per-corpus descriptions. No inferential test is applied to n = 18
   counts, and no confidence interval is reported as if the corpus were a probability sample.

---

## 10. Exclusions restated as coding rules

- An error is never "the model is not what I would have modelled".
- A missing element that the prompt did not request is not an error.
- A modelling *choice* that is legal SysML v2 but unusual is not an error.
- A `satisfy` link is not an error merely because its justification is thin; it is an error when
  the link's own syntax/semantics does not hold (e.g. subject is not a requirement).
- Absence of behaviour where behaviour was requested is recorded as a **coverage/omission**
  observation, in a separate table from the error population, because omission is a
  prompt-compliance property, not a well-formedness defect. This separation is fixed now so that
  omissions cannot inflate the error counts.

---

## 11. Threats to validity (pre-registered)

1. **Generator = coder A (same model family, same session).** The corpus is produced by the model
   that inspects it. Mitigations: generation precedes codebook; second coder is a fresh context;
   raw outputs preserved and hashed; codebook frozen and hashed before second coding; labels
   re-checkable by a third party from the raw files. This is a *procedural* independence only
   (`PROTOCOL.md` §8) and any claim beyond "this corpus contains these errors" is unsupported.
2. **n = 18, one generation per cell.** No sampling frame, no repeats, no variance. Frequencies
   are descriptions of these 18 outputs.
3. **Task authorship.** The 6 prompts are mine; prompt design shapes the error population. Task
   effects cannot be separated from prompt-author effects at this n.
4. **Single generator family, three configurations.** Configuration is confounded with prompt
   length and instruction content (C3 is longer and more directive), so C1–C3 differences are not
   clean causal estimates of "structure-imposing strategies".
5. **Specification version skew.** The catalogue is SysML 2.0 `formal/2026-03-02` / KerML 1.0;
   the pinned validator tracks 2.1 Beta material (`evidence/spec-tooling.md` §4.1). A defect
   coded against 2.0 may be treated differently by the 2.1-era tool; both directions are recorded.
6. **Normalisation is a judgement.** Fence selection and prose non-stripping are rules, but their
   application is mine; the log makes every case auditable.
7. **No human expert.** Agreement between two instances of one model family is not expert
   agreement and does not establish that the classes are the *right* ones.
8. **A single-instrument detection column.** One open validator; the second is unavailable
   (no JVM) and the commercial one is licence-blocked (`TOOLING.md` §2–3). Detection results are
   instrument calibration, not ground truth about error prevalence.

---

## 12. Deliverables and reproduction

Artifacts under `research/issue-007/` (raw/, corpus/, coding/, detection/) and the report
`reports/issue-007-error-taxonomy-pilot.md`. All scripts (`corpus/extract.py`,
`coding/agreement.py`, detection summary) run offline and rebuild the tables from the stored raw
files; the exact commands are in `research/issue-007/README.md`.

## 13. Statement on the pilot's status

**N = 18 < 200. This pilot is preliminary and cannot close issue #7.** Its value, if any, is
that the process — provenance-preserving corpus, bottom-up codebook, double coding, separate
detection measurement — is complete and re-runnable, and that its numbers are honest about
their denominator.

---

## 14. Amendments

(none at freeze; dated entries appended below if the plan changes)

| # | Date (UTC) | Amendment | Reason |
|---|---|---|---|
| — | 2026-11-13T14:05:30Z | none — this is the frozen original | — |
