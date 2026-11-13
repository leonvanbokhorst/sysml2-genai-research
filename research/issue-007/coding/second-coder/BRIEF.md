# Record of the single permitted delegation — second coder (brief and independence limits)

**Delegation:** exactly one `subagent` (fresh context), created 2026-11-13T14:12Z. No other
delegation was used; the subagent was instructed not to spawn agents.
**Role:** independent second coder for 12 of the 18 models.
**Output:** `coder-b.csv`, `coder-b-models.csv` — written in this directory by the subagent and
copied unchanged to the canonical paths `../coder-b.csv` / `../coder-b-models.csv`, which
`../agreement.py` reads. The two copies are byte-identical (sha256 in the report).

## What the second coder received (and nothing else)

1. `INSTRUCTIONS.md` — label 12 models with the frozen codebook; write two CSVs; do not read
   outside the directory; do not run a validator/parser; do not use web search; do not spawn
   agents; apply the codebook as written.
2. `CODEBOOK.md` — **a coder-facing copy of the frozen codebook**. Content: identical classes,
   definitions, inclusion/exclusion criteria, precedence rules, severity scale, layer mapping,
   constraint mapping, exclusions and agreement procedure. The only transformation: in the worked
   examples and the exclusion list, model identifiers and line numbers were replaced by
   placeholder labels (`Example E1`…`E12`, `:<lines>`) so that the coder could not copy a label by
   file identity. No definition, criterion or class was altered. The canonical frozen file is
   `../CODEBOOK.md` (sha256 `9d3e5e05…f10a03`); the timestamp strings in the copy predate a
   metadata correction of that file and differ only in those strings.
3. `models/<id>.sysml` — the 12 normalised models (the same text coder A coded).
4. `raw/<id>.md` — the 12 matching raw outputs (fenced markdown, preamble where present), because
   the codebook requires distinguishing wrapper defects from modelling defects.

## What it did **not** receive

- Coder A's labels (`../errors.csv`, `../models.csv`), the label-generating script
  (`../labels.py`), the counts, the class distribution, or any statement of what coder A expected.
- Any other directory of the repository, including Researcher B's work and the project's
  catalogue/evidence notes.
- The task prompts (deliberately: fidelity to the prompt is out of scope, so the coder should not
  be tempted to code prompt-coverage as error).

## Selection of the 12 (deterministic, fixed before the subagent started)

All six tasks are represented and all three configurations appear:
`T1-C1, T1-C2, T2-C1, T2-C2, T3-C2, T3-C3, T4-C1, T4-C2, T5-C1, T5-C2, T6-C2, T6-C3` —
i.e. C2 for all six tasks, C1 for the four tasks with the lowest `sha256(task)` (T5, T2, T4, T1),
C3 for the remaining two (T3, T6). Three of the twelve are models coder A found clean
(T3-C3, T5-C1, T6-C3), so the presence/absence call is not trivially "always error".

## Independence — what it is, and what it is not

- **Procedural independence:** separate context, no access to A's labels, frozen codebook, no
  sight of A's reasoning. That is what `PROTOCOL.md` §6 and §8 anticipate.
- **Not epistemic independence:** the second coder is served by the **same model family** as the
  generator and as coder A (DeepSeek-family model through DSH; exact checkpoints not exposed). It
  is not a human expert and shares whatever priors produced the corpus. Agreement between two
  instances of one model family is an upper bound on human agreement, not an estimate of it.
- **Residual contamination:** the codebook was built bottom-up from this corpus, so its worked
  examples are paraphrases of defects that occur in the 12 models. Removing model identifiers
  reduces label-copying but cannot remove recognition: a coder who recognises a construct as the
  codebook's example will label it the same way. Agreement is therefore **inflated for exactly the
  classes whose examples are recognisable**, and the report says so. This is a limit of a
  codebook built from a 18-model corpus, not a defect of the second coder.
- **No adjudication by majority, no reconciliation meeting.** Disagreements are reported as found.
