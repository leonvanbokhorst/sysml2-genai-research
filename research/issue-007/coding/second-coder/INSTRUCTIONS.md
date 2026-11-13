# Second-coder instructions (independent labelling task)

You are the independent second coder for a small error taxonomy study of GenAI-generated SysML v2
models. Your job is to label defects in 12 model files using the frozen codebook in this
directory, and to write your labels to a CSV. You are *not* asked to improve the codebook, to
check anyone else's labels, or to judge the models' engineering adequacy.

## What you may read

- `CODEBOOK.md` — the frozen codebook (definitions, inclusion/exclusion, precedence, severity,
  layer mapping, worked examples).
- `models/*.sysml` — the intended SysML v2 model text for each of the 12 models.
- `raw/*.md` — the raw model output as it was emitted, including any markdown fence, preamble or
  trailing prose.

Do **not** read anything outside this directory. Do not search the repository for other coders'
outputs. There are no other coders' outputs in this directory.

## What to produce

Write `coder-b.csv` in this directory with exactly these columns, one row per **distinct defect
mechanism per model** (the codebook's coding unit — a repeated occurrence of the same mechanism is
one row, with the occurrences and lines noted):

```
model_id,error_id,class,layer,severity,evidence_excerpt,line_range,spec_constraint,notes
```

- `model_id` — the file stem, e.g. `T3-C2`.
- `error_id` — `T3-C2-E01`, `T3-C2-E02`, … in line order.
- `class` — one of `W1, S1, S2, N1, N2, T1, R1, I1` (see codebook §1). Use `W1` only for a
  wrapper/formatting defect of the **raw** output; do not code `W1` on normalised model text.
- `layer` — the codebook layer for that class.
- `severity` — `blocking`, `major` or `minor` per codebook §3.
- `evidence_excerpt` — the shortest text span from the model that carries the defect (verbatim,
  one line or a short multi-line quote).
- `line_range` — line number(s) in the **normalised** model file (`models/<model_id>.sysml`), e.g.
  `41` or `48-51`.
- `spec_constraint` — the catalogue constraint name from the codebook's class table if one applies,
  otherwise empty.
- `notes` — one sentence: why this class, and your confidence (`high`/`medium`/`low`).

Models with **no** defect get **no row**; instead list them in a separate file `coder-b-models.csv`
with columns `model_id,n_errors` (use `0`) so the denominator is visible. Include all 12 models in
`coder-b-models.csv`.

## Rules

1. **Label from the model text and the codebook only.** Do not run a SysML validator, parser or
   language server. A defect exists because the text deviates from the SysML v2 notation /
   well-formedness rules or from the codebook's structural criteria, not because a tool says so.
2. **One class per row**, using the codebook's precedence rules (parse before resolve; prelude
   before dangling name; mechanism not symptom; no double-coding an unparsed span's names).
3. **Do not code**: deviations from the task prompt (there is no task prompt here on purpose),
   naming/decomposition/style choices, unused declarations, untyped ports, or anything in
   codebook §5's exclusion list. Omissions are not errors; do not invent them.
4. **Apply the codebook as written.** If you believe a rule is wrong, record the objection in
   `notes` and still apply it. Do not silently amend the codebook.
5. **Do it in one pass per model**, in the order `T1-C1, T1-C2, T2-C1, T2-C2, T3-C2, T3-C3, T4-C1,
   T4-C2, T5-C1, T5-C2, T6-C2, T6-C3`.
6. SysML v2 facts you may rely on: the textual notation requires `satisfy <requirement> by
   <feature>`; a feature chain through a multi-valued usage is not a single feature; `Real`,
   `Integer`, `Boolean`, `String` are standard-library scalar types that must be imported or
   qualified; a definition is a type, not an occurrence. If you are unsure whether a construct is
   legal SysML v2, say so in `notes` with `confidence=low` rather than leaving the row out.

When you are finished, report back: the number of rows, the class counts, the models you found
clean, and any codebook rule you found hard to apply.
