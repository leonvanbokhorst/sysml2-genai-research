# Issue #7 pilot — observed error population in GenAI-generated SysML v2 models

**Status:** pilot, preliminary, **N = 18** models. Issue #7 asks for ≥ 200; this cannot close it.
**Report:** [`reports/issue-007-error-taxonomy-pilot.md`](../../reports/issue-007-error-taxonomy-pilot.md)
**Owner:** Researcher A. No git operations were performed by the researcher (protocol §6).

## Headline (with denominators)

- 18 models = 6 self-authored tasks × 3 prompting configurations, one generation per cell.
- Population accounting, because the corrections moved it: **14 records in 12/18 models, 6 clean**
  in the frozen file (untouched, `30265ff5…`); **13 in 11 models, 7 clean** after the C12
  withdrawal (`first start;` is legal — `Actions::Action` declares an inherited `start`); **19
  records in 14 models, 4 clean** in the corrected combined arm (C01 phantom + C12 applied).
  Report §16 (Gate-2 corrections) and §17 (post-closure corrections) carry every old→new value.
- Largest classes (frozen population): **N1 unresolved model-local reference (5; 4 after C12)**, **S1
  non-conforming textual form (3)**, **R1 connector over multi-valued usages (2, contested as to defect
  status)**.
- **18/18 raw outputs are markdown**, **6/18 are invalid only because of the wrapper** (V1),
  **12/18 still fail after normalisation** (V2).
- Second coder (independent context, same model family): 12/12 model-level agreement and 11/11
  class agreement, **but** κ = 1.0 is not reliability evidence — 8/11 paired excerpts were verbatim
  in the coder-facing codebook (11/11 exemplar-covered). Only the three clean-model calls are
  independent. Corrected in the report §16.5 and `coding/agreement.md`.
- Pinned validator detects **9/14** coded errors (**9/13[C12]** = 69 % after C12; **9/12[−I1]** = 75 % excluding the contested I1; **9/10[−R1]**; **9/9[−S2]**); silent
  on both connector records (R1), the constraint-layer record (S2) and the contested
  documentation/value record (I1). Record-level counts are upper bounds for two records: the tool
  flagged 2/3 occurrences of T3-C2's S1 and 1/2 of T4-C1's T1 (`detection/occurrence_detection.csv`).

## Freeze hashes

| Artefact | sha256 |
|---|---|
| `METHODOLOGY-FROZEN.md` (frozen before any data existed) | `269d8dbe7228db83d20ca2be39991172f20fd23458ac1e5e6755ff7269564f76` |
| `coding/CODEBOOK.md` v1.4 (current, after Gate-4 adjudication A-6/A-7/A-12) | `91f963bffb980924f4969da4200cb2a35231e23ca80a8afa4497435f886094b9` |
| `coding/CODEBOOK.md` v1.3 (after Gate-2 corrections) | `106e620d6c6808f980f2f58d6e79f574bcd350dcf41978a4083df0cdd9063314` |
| `coding/CODEBOOK.md` v1.2 (as reviewed by B) | `d2019448c6840ced7b1aab077c40fbdf5afd89747426370ca80007b07ff76766` |
| `coding/CODEBOOK.md` v1.0 (classes as first frozen) | `9d3e5e0522debccaf68fc3987f1e8efe161ae225b6204aa4525df34523f10a03` |

Methods changed only through dated amendments: `AMENDMENTS.md` A1–A6 (selection rule ambiguity,
coder-facing codebook copy, S2 correction from the normative BNF, external corpus use, detection
scope). The freeze file itself is byte-identical, so its hash remains checkable.

## Layout

| Path | What it is |
|---|---|
| `METHODOLOGY-FROZEN.md` | the plan, written before generation, hashed |
| `AMENDMENTS.md` | dated amendments, with reasons |
| `FREEZE-HASH.txt`, `coding/CODEBOOK-HASH.txt` | recorded hashes |
| `corpus/prompts.md` | the 6 task prompts, 3 configurations, design rationale (written before generation) |
| `raw/*.md` | 18 raw outputs, verbatim, fences and prose intact |
| `corpus/manifest.csv` | model_id, task, configuration, generator, timestamp, chars, sha256 raw |
| `corpus/extract.py` | wrapper-only extraction (no semantic repair) |
| `corpus/extraction-log.json` | every extraction decision, per model |
| `corpus/normalized/*.sysml` | 18 normalised models |
| `coding/CODEBOOK.md` | frozen error classes, criteria, exclusions, precedence, layer + constraint map |
| `coding/inspect.py`, `coding/indicators.json`, `coding/_audit-view.txt` | mechanical pointers for the inspection pass (not verdicts) |
| `coding/labels.py` | coder A's frozen labels as data |
| `coding/errors.csv` | **the frozen error population** (14 records) |
| `coding/models.csv` | all 18 models, incl. zero-error models and detection columns |
| `coding/omissions.csv` | coverage/omission observations kept out of the error counts |
| `coding/post_inspection.py`, `coding/errors-post-inspection.csv` | the post-inspection, BNF-verified additions, kept separate (7 rows; one withdrawn on review) |
| `coding/errors-corrections.csv` | dated corrections from the Gate-2 response: the withdrawn phantom, corrected spans/occurrences, R1 re-layering, contested I1, corrected citations |
| `coding/apply_corrections.py`, `coding/errors-combined.csv`, `coding/reconciliation.md` | applies the corrections to the derived population and prints the per-row reconciliation Reviewer B asked for; the frozen `errors.csv` is never edited |
| `coding/coder-b.csv`, `coding/coder-b-models.csv` | the second coder's labels (canonical copy; identical to the files it wrote in `second-coder/`) |
| `coding/second-coder/` | the subagent's brief, the coder-facing codebook copy, and its 12 models + raws |
| `coding/agreement.py`, `agreement.json`, `agreement.md` | agreement statistics and the disagreement/ convention notes (generated) |
| `coding/agreement-addendum.md` | dated Gate-2 correction: what κ = 1.0 can and cannot support (answer-key contamination) |
| `ADJUDICATION-RESPONSE.md` | Gate-4 adjudication: every A-item with APPLIED/DISSENTED status and the corrected numbers |
| `CROSS-REVIEW-HASH.txt` | append-only hash ledger, one row per write (A-15) |
| `detection/run_detection.py` | the instrument measurement (runs after coding, edits no label) |
| `detection/raw/*.txt` | verbatim validator output per artefact (18 normalised, 18 raw, 24 external, 10 probes) |
| `detection/diagnostics.csv`, `summary.csv`, `table.md` | parsed diagnostics; per-artefact and per-class tables |
| `detection/probes/*.sysml` | 10 minimal probes characterising the instrument's scope |
| `detection/external/` | 24 single-shot artefacts from the LaVoie et al. release + hashes (secondary check only) |
| `detection/manifest.json`, `detection/make_manifest.py` | per-file sha256, tool sha256/version and argv for every artefact the detection run touched |
| `detection/occurrence_detection.csv` | occurrence-level detection for the four multi-occurrence records |

## Reproduce

Everything below is offline except the two fetches marked *(network, run once)*; the committed
outputs are the result of these commands.

```bash
cd <repo root>

# 0. (network, run once) the only external data: 24 external artefacts + the spec PDF
#    hashes are in detection/external/manifest.json and the report §9

# 1. wrapper-only extraction: raw/*.md -> corpus/normalized/*.sysml + manifest + extraction log
python3 research/issue-007/corpus/extract.py

# 2. mechanical indicators used during the inspection pass
python3 research/issue-007/coding/inspect.py

# 3. coder A's frozen labels -> errors.csv, models.csv, omissions.csv
python3 research/issue-007/coding/labels.py

# 4. post-inspection, BNF-verified additions -> errors-post-inspection.csv
python3 research/issue-007/coding/post_inspection.py

# 5. apply the dated corrections -> errors-combined.csv, reconciliation.md, refreshed models.csv
python3 research/issue-007/coding/apply_corrections.py

# 6. instrument measurement (needs .tools/sysml v0.12.1; edits no label)
python3 research/issue-007/detection/run_detection.py

# 7. detection provenance + occurrence-level table
python3 research/issue-007/detection/make_manifest.py

# 8. re-apply corrections (keeps derived columns consistent with the fresh detection columns)
python3 research/issue-007/coding/apply_corrections.py

# 9. agreement with the second coder -> agreement.json, agreement.md
python3 research/issue-007/coding/agreement.py

# 10. verify the freeze and codebook hashes
shasum -a 256 research/issue-007/METHODOLOGY-FROZEN.md research/issue-007/coding/CODEBOOK.md
```

The second coder's files (`coding/second-coder/coder-b.csv`, `coder-b-models.csv`) are inputs to
step 6, not outputs of it; step 6 must not be run before they exist.

## What this pilot does not do

It does not close issue #7 (N = 18 < 200), does not reproduce or refute either anchor, does not
judge model fidelity to the prompts, does not establish human agreement, and does not evaluate
validator reliability (that is #8). It is a complete, re-runnable demonstration of the process at
small scale, with its limits stated in the report.

## Gate-2 corrections (added 2026-11-13T14:31Z)

Reviewer B raised 13 objections (0 blocking, 8 material, 5 minor). All were tested against the
artefacts; the rulings are in
[`research/relational/cross-reviews/A-response-to-B-review.md`](../../research/relational/cross-reviews/A-response-to-B-review.md)
and every changed number is listed in the report's **§16** with old and new values. The frozen
14-record population is intact; one post-inspection record was withdrawn as a phantom (its excerpt
did not exist in the model), one frozen record is marked contested (I1), the agreement study's κ is
downgraded to non-evidential because the coder-facing codebook was an answer key for 8 of 11 paired
excerpts, and the external comparison to the authors' 51.16 % is withdrawn as not like-for-like.
