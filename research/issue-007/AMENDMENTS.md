# Dated amendments to the frozen methodology

The freeze file `METHODOLOGY-FROZEN.md` (sha256
`269d8dbe7228db83d20ca2be39991172f20fd23458ac1e5e6755ff7269564f76`, frozen 2026-11-13T14:05:30Z)
is deliberately left **byte-identical** so that its hash stays checkable. Amendments are recorded
here instead of in an appended §14 table; that is the one deviation from the freeze file's own
wording, and it is made to protect the evidentiary value of the hash rather than to revise the
plan.

---

## A1 — 2026-11-13T14:10Z — Selection rule for the 12 double-coded models (ambiguity resolved)

**Freeze text (§6) was internally inconsistent:** "for each task, take C1 and C2, plus two tasks'
C3 — i.e. 12 of 18" describes 6×2 + 2 = 14 models, not 12, and cannot satisfy "all 6 tasks
represented, all 3 configurations represented" at n = 12 by that construction.

**Operationalisation applied.** 12 = C2 for all six tasks (6) + C1 for the four tasks with the
lowest `sha256(task)` + C3 for the two remaining tasks. Result:
`T1-C1, T1-C2, T2-C1, T2-C2, T3-C2, T3-C3, T4-C1, T4-C2, T5-C1, T5-C2, T6-C2, T6-C3`.
This keeps every task represented, keeps all three configurations represented, keeps a stratified
mix, and includes three of the six models coder A judged clean. It was computed and recorded
(`coding/second-coder/BRIEF.md`) before the second coder started.

**Disclosure:** the choice was made after coder A's labels existed, so it is not a blind design
choice. The rule is mechanical (hash order) precisely to limit that freedom; a reviewer should
still treat it as a post hoc operationalisation of an ambiguous frozen sentence.

## A2 — 2026-11-13T14:11Z — Coder-facing codebook copy

The second coder received the frozen codebook with model identifiers and line numbers in the
worked examples replaced by placeholders, so that labels could not be copied by file identity. No
definition, criterion, precedence rule, exclusion or class was changed. Reasons and residual
contamination are in `coding/second-coder/BRIEF.md`. This is a presentation change to one
artifact, disclosed; the canonical codebook is unchanged.

## A3 — 2026-11-13T14:12Z — Codebook timestamp correction before the freeze hash was published

The codebook's revision table initially carried estimated clock times that were ahead of the
actual session clock. They were corrected to the real times (14:08/14:10/14:11/14:12Z) and the
codebook was hashed **after** the correction. No class, rule or label changed. The coder-facing
copy (A2) still shows the earlier timestamp strings; that difference is textual only.

## A4 — 2026-11-13T14:09Z — An external public corpus was found and is used as a bounded secondary check

The bounded corpus search (freeze §2.1) found a public, openly downloadable corpus of
LLM-generated SysML v2: LaVoie, Andujar Lugo, Topcu & Kara (2026), *Natural-Language to SysMLv2
Translation via Conformance-Driven Iterative Refinement* (arXiv:2607.14162, IDETC/CIE 2026), whose
companion repository `cmuchancel/NL-to-SysMLv2-via-Conformance-Driven-Refinement` releases 151
SysMBench prompts, 604 prompt–model cases and 1,043 iteration artefacts across four model
backends.

It **fails one of the freeze's own selection criteria**: the released artefacts are stored as
`.sysml` files, i.e. the markdown wrapper has already been stripped by the authors' harness, so
raw outputs *including* fences/preamble — criterion (b) — are not available. It therefore cannot
replace the primary corpus for the wrapper question. It satisfies (a) LLM-generated SysML v2
textual notation, (c) open download without bypassing an access control, and (d) per-output prompt
and generator identity.

**Use decided:** the primary corpus and all hand coding remain the 18 self-generated models. The
external corpus is used **only** as a bounded secondary check with its own denominator: a
deterministic 24-artefact sample (single-shot `iteration_00` for prompts 001–006 × four backends),
run through the *same* normaliser and the *same* pinned validator, with the same wrapper-status
variables. It is **not hand-coded**, so it contributes to the formatting-mechanism arm and to the
detection measurement only — never to the taxonomy frequencies. Its generator families (Anthropic,
OpenAI, DeepSeek, Mistral, per the repository's folder names) are independent of this session's
generator for three of the four backends.

## A5 — 2026-11-13T14:13Z — Detection runs on raw outputs of models that are valid SysML as-is

Freeze §7 said to run the validator on (i) every normalised model and (ii) raw outputs that are not
syntactically valid SysML as-is. In practice **all 18** raw outputs are markdown, so the raw set is
all 18, not a subset. No change of principle; recorded so the numbers can be read correctly.

## A6 — 2026-11-13T14:14Z — One label corrected after retrieving the normative grammar

The SysML 2.0 Language specification PDF (`formal/2026-03-02`, sha256 `46e6c047…4a83a`) was
retrieved because two labels depended on the textual-notation grammar: the `by` clause of
`satisfy`, and the `first <QualifiedName>` succession reference. The BNF shows the `by` clause is
**optional**, so the one record coded as "mandatory clause omitted / syntax / blocking" was wrong
as a syntax defect. It was relabelled to the constraint layer (violation of the discretionary
`checkSatisfyRequirementUsageBindingConnector`) with severity `minor`; the error count did not
change. Codebook v1.1 records the change (§9) and the codebook was rehashed
(`d42a2ad0…943617`). This is a specification-grounded correction, not a validator-driven one: the
validator had been silent on that construct, and its silence was correct.

The same retrieval confirmed the second label: `InitialNodeMember = MemberPrefix 'first'
memberFeature = [QualifiedName]` is a cross-reference, so `first start;` in the corpus requires
`start` to resolve. The pinned validator reports nothing for it (a detection gap, recorded in the
detection table), which does not remove the defect.

## A7 — 2026-11-13T14:31Z — Two post-closure evidence corrections from Reviewer B, adjudicated

Reviewer B sent two minor corrections after Gate 2 closed. Both are accepted, and one changes a
label; neither edits a frozen file (`errors.csv`, `errors-post-inspection.csv`, `A-reviews-B.md` are
untouched). They are registered as C12/C13 in `coding/errors-corrections.csv`.

**A7.1 — `first start;` is legal; the T1-C1 record is withdrawn (C12).** B's probe suggested that
`Action` has an inherited member `start`, so `first start;` may resolve. I checked the source rather
than the probe: the normative Systems Library declares, at line 43 of
`sysml.library/Systems Library/Actions.sysml` (sha256
`ac36c9404cac347a2c12d4a0cb067b1a9cebcba6a1a1853eaa1f5b3fdeb15693`),

```
action start: Action :>> startShot
```

so every Action inherits a `start` action and `first start;` inside an action definition is not a
dangling reference. My record `T1-C1-E01` said the opposite ("no action usage named `start` is
declared … the succession source is a dangling reference"), so **its basis is false and it is
withdrawn**. B explicitly declined to relitigate this; the withdrawal is mine, on the library text.

Consequences, stated because they are awkward: the frozen population falls from 14 to **13
records** (12 → 11 affected models; the clean set grows from 6 to 7 because `T1-C1` had no other
record), and the frozen detection rate rises from 9/14 = 64 % to **9/13 = 69 %** because the
withdrawn record was one the instrument did not detect. Every post-closure correction in this pilot
has moved the rate upward; that is a reason to distrust small-n rates that have been corrected after
the fact, and it is why the report now shows the original and corrected denominators side by side.

This is deliberately **not** the same treatment as I1 (kept, marked contested): I1 has two defensible
readings, so withdrawal would be my choice among readings; T1-C1's record rests on a factual claim
about the language that the normative library contradicts, so keeping it would be wrong regardless of
which way the rate moved.

**A7.2 — the construct census said 0/18 for ISQ/SI; it is 3/18 for SI (C13).** `grep -l "import SI::*"`
matches `T3-C2`, `T3-C3`, `T5-C1` — three models import SI, none imports ISQ, and **none writes a
unit literal** (`[kg]`, `[m]`, …: no match). My cross-review of B (O7) and the report's
construct-surface claim said "unit-typed attributes with ISQ/SI libraries — 0/18", which overstates
the absence. Corrected statement: *3/18 import SI, 0/18 import ISQ, 0/18 write a unit literal*. The
substance of the objection to B (that F6's unit/quantity faults are built on a construct generated
models in this corpus do not exercise) survives: importing SI without writing a unit-typed quantity
does not make the model unit-checkable.

**A7.3 — the frozen plan is unchanged.** No methodology change; these are evidence corrections
inside the existing coding frame.
