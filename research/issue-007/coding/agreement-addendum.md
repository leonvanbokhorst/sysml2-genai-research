# Agreement — interpretation addendum (Gate-2 response)

**Added:** 2026-11-13T14:29Z, after Reviewer B's review (`B-reviews-A.md`, O5/O6). The statistics in
`agreement.json` / `agreement.md` are unchanged; this file corrects what they may be cited as
evidence for. It is a separate file because `agreement.md` is **generated** by `agreement.py` and is
regenerated on every pipeline run — appending to a generated file is how a correction silently
disappears (it happened once during this response; the text below is the restored copy).

## 1. The coder-facing codebook was closer to an answer key than "paraphrase" implied

Reviewer B tested this directly; I reproduce the test. For the 11 paired records, **8 match by
string** in `second-coder/CODEBOOK.md` — 7 character-for-character, 1 after whitespace
normalisation across a line break — and the remaining 3 (`satisfy returnToDock by fleet;`,
`satisfy insideWindow by station;`, `satisfy maintainTemperature by heating;`) are the sub-mechanism
of the printed exemplar (`satisfy alarmTiming by pump;`). So: **8/11 verbatim, 11/11
exemplar-covered.** (Reviewer B counted 7/11; the substance is the same and marginally worse.)

## 2. What the 12/12 model-level presence agreement is worth

Nine of the twelve models carry a record whose exemplar is in the codebook, so nine presence calls
are answer-key-assisted. The three **clean** calls (T3-C3, T5-C1, T6-C3) have no exemplar — nothing
in the codebook shows a model with no defects — so those three are genuine discrimination: a coder
working from the codebook still had to conclude "none" for those models. That is the part of the
presence result that survives on its own.

## 3. What the 11/11 class agreement is worth: not reliability evidence

With 8 verbatim and 3 exemplar-covered pairs, class agreement is largely string matching plus label
lookup. It shows the classes are *applicable* to the texts they were built from (no ambiguity
prevented copying), **not** that two readers independently converge. κ = 1.0 must not be quoted as
inter-coder reliability for this taxonomy.

## 4. What survives independently of the contamination

1. The three clean-model calls above.
2. The second coder independently *noticed* three reserved-keyword instances that were not in the
   v1.0 codebook (`attribute state : String;`, `port return;` in two models) and correctly declined
   to code them under the frozen text — a discrimination test the answer key does not explain, and
   the same blind spot coder A had.
3. *(withdrawn 2026-11-13T15:15Z, A-17: the "W1 dissent" was a recording-scope difference, not a
   judgement the key could not supply — both coders treat a bare fence as W1 and differ only on
   where it is recorded. This item no longer counts as independent evidence.)*
4. Its excerpts are verbatim substrings at the cited lines (verified here and by Reviewer B), so the
   labelling was done against the models rather than invented from the codebook.

## 4a. The instruction channel (added 2026-11-13T15:15Z, A-13)

The coder also received `coding/second-coder/INSTRUCTIONS.md`. Its §6 supplied four class criteria as
facts — that `satisfy` requires `by`, that a definition where a usage is required is a kind
mismatch, that bare scalar types need an import, and that a chain through a multi-valued usage is not
a single feature — and one of those rules is **false as stated** (the `by` clause is optional,
§8.2.2.21.2: `( 'by' … )?`). For S1, S2, T1 and R1 the agreement therefore measures
instruction-following as well as coding judgement, independently of the answer-key problem. What
survives as independent discrimination is only the reserved-keyword noticing (item 2 above) and the
verbatim-substring verification.

## 5. Layer/severity agreement 10/11 is version skew, not disagreement

The single differing pair is S2, where the coder applied the v1.0 definition (syntax/parse,
blocking) and coder A's record had been moved to constraint/OCL, minor after the normative BNF was
read (codebook §9). Reporting "κ = 0.87" invites the reading of a coding disagreement; the coders
were handed different definitions. Likewise the 11/11 class figure includes S2, where the
*identifier* agreed while the v1.0 definition was later found to rest on a false premise (the `by`
clause is optional in §8.2.2.21.2).

## 6. The reliability test that remains unrun

Re-code a held-out set with **no exemplar** in this codebook — the LaVoie release is the obvious
candidate (24 artefacts already on disk, hashes in `detection/external/manifest.json`) — with the
codebook's worked examples removed entirely. Until that exists, no agreement figure in this pilot
should be quoted as evidence that the taxonomy is reliable.
