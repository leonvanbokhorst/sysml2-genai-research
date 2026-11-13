# research/issue-008 — mutation-based evaluation of an open SysML v2 validator (pilot)

Pilot artefacts for research issue
[#8](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/8), *How reliable are SysML v2
validators as measuring instruments?*

**This is a preliminary pilot. It cannot close #8.** It measures **one** instrument
(OpenSysML CLI `sysml v0.12.1`) against 32 synthetic, specification-derived mutants derived from 10
small known-good models. There is no second instrument, no second coder, and no representativeness
study against observed generation errors. Read
[`../../reports/issue-008-validator-reliability-pilot.md`](../../reports/issue-008-validator-reliability-pilot.md)
for the answer and the limitations; this file indexes the evidence.

## Headline

| measure | result |
|---|---|
| relevant error-severity detection, 32 mutants | **23/32 = 0.72** (95% Wilson [0.55, 0.84]) |
| any signal (error or warning) | 28/32 = 0.88 [0.72, 0.95] |
| error-level false positives on 10 known-good models | **0/10** (1 warning, triaged as over-reach) |
| classes detected at 0/4 | **structural/architectural (F7)** — all four silent |
| named SHOULD constraint silently missed | KerML `validateFeatureValueOverriding` §8.3.4.10.2 |

## Artefacts

| Path | What it is |
|---|---|
| `METHODOLOGY-FROZEN.md` | Research question, fault model and its derivation, mutant-construction and plausibility rules, known-good corpus basis, pinned instruments, **pre-registered hypotheses H1–H9**, measurement definitions, metrics with denominators, exclusions, threats to validity. Frozen at 2026-11-13T14:08Z; hash `2c80d63e…6f00b` in `methodology.sha256`. |
| `methodology.sha256` | sha256 of the frozen methodology. |
| `known-good/*.sysml` (10) | Known-good corpus, 10–40 lines each: nine quoting the pinned SysML 2.0 PDF (§7.11.2, §7.12.2, §7.13.2, §7.13.4, §7.17.2, §7.17.3, §7.18.2, §7.18.3, §7.20.3, §7.21.2), one authored quantity pattern labelled as authored. |
| `known-good/*.PROVENANCE.md` (10) | Per model: source and clause, which declarations are quoted and which I supplied, the **constraint-level** validity argument, and my own uncertainties. |
| `mutants/*.sysml` (32) | Mutant corpus: 8 fault classes × 4, one injected defect each. |
| `mutants/MANIFEST.csv` | The **pre-registered expectations** — fault class, specification condition with clause, expected layer, expected detectability, rationale, plausibility note, surface-tell flag, file hash. Frozen: `a9f47974…57be7`. |
| `mutants/expectations.sha256`, `mutants/mutants.sha256` | Freeze hashes for the expectations and the 32 mutant files. |
| `mutants/FREEZE.md` | What was frozen, when, and the rules that apply afterwards. |
| `harness/run_validators.py` | Runs the pinned validator over both corpora, writes **unedited** raw JSON + stderr per case, a tidy `results.csv`, per-diagnostic `diagnostics.csv` and a run log with tool identity, hashes, argv, exit codes. Refuses to overwrite raw output (per-run directories, exclusive file creation). |
| `harness/make_mutants.py` | Regenerates `mutants/*.sysml` from `known-good/` by exact literal substitution; asserts each match occurs exactly once. |
| `harness/author_manifest.py` | The authored expectation table (source of `MANIFEST.csv`). |
| `harness/analysis.py` | Applies the post-hoc relevance triage, computes every rate with Wilson intervals, and writes `triage.csv`, `analysis.json`, `analysis.md`. |
| `results/raw/run1/{known-good,mutants}/*.json` | **42 unedited validator outputs** (plus `.stderr.txt`). Primary evidence; never edited. |
| `results/raw-run1.json` | The full machine record of the run (argv, timestamps, exit codes, parsed diagnostics). |
| `results/results.csv` | One row per case: expectations joined to observed diagnostics. |
| `results/diagnostics.csv` | One row per emitted diagnostic (severity, code, layer, line, message). |
| `results/run-log-run1.md` | Instrument identity and hash check, exact argv per case, corpus hashes at run time, per-case outcome. |
| `results/triage.csv` | Per mutant: judged outcome (`detected` / `wrong_severity` / `misleading` / `incidental` / `silent`), specification-oracle status, codes, and the note justifying the judgement. |
| `results/analysis.md`, `results/analysis.json` | Per-class sensitivity with denominators and CIs, layer-confusion view, specification-oracle table, expectation audit, surface-tell stratum, known-good arm, per-mutant record. |
| `results/known-good-triage.md` | Every firing on a known-good model, triaged (i) genuine defect / (ii) over-reach / (iii) confound — including the two **pre-freeze** corrections and one unresolved reference in the **specification's own example text**. |
| `results/calibration/PRE-FREEZE-CALIBRATION.md` | The 10 tool-invocation probes run before the methodology was frozen, why they were needed, and what they do **not** show. Probe models preserved in `results/calibration/probes/`. |
| `harness/run_modes.py` | **Gate-2 addition.** Re-runs the F7 arm and specific probes through every invocation of the pinned binary that bears on a verdict — default `-validate`, `-satisfy`, `-instantiate <obj> -validate=<obj>`, `-self-check`, `-validate -strict`, `-state`, `-action` — and preserves raw output. It exists because the original harness ran exactly one invocation, which is the substance of Researcher A's blocking objection O1. |
| `results/raw/run2-modes/**` (78 files) | Unedited raw output of the 34 per-mode probes, with `results/modes-summary-run2-modes.csv` and `results/run-log-run2-modes.md` (tool hash, exact argv, exit codes, timestamps). |
| `results/probes-gate2/**` (5 models) | Gate-2 probe models: reserved keyword as a name, dangling succession source (and its declared control), missing stdlib prelude, dangling satisfy target. **Not** frozen mutants; they exist to measure classes the frozen 32 did not sample. |
| `../relational/cross-reviews/B-response-to-A-review.md` | The Gate-2 response: ruling, evidence, change and number delta for each of Researcher A's 13 objections (12 accept, 1 partly accept, 0 reject). |
| `empirical/PRE-REGISTRATION.md` (+ `.sha256`) | **Task-6.** The invocation set, line-attribution rule, five-valued standing map, control rule, class mapping and the P6/P8 decision rule, frozen at `9458406e…6acfbc` **before the first run** — the remedy for the mode-selection degree of freedom I flagged after Gate 2. |
| `empirical/run_external.py` | Harness: verifies A's recorded hashes, runs the four registered modes over the frozen subset, scores strictly per the pre-registration, writes raw output and tidy tables. Exits non-zero and refuses to run if any hash mismatches. |
| `empirical/results.csv` | 80 rows = 20 items (13 errors + 7 controls) × 4 modes, with outcome, detail, standing, exit code and exact argv. |
| `empirical/per-item-per-mode.md` | The readable matrix with per-cell codes and standings. |
| `empirical/raw/run1`, `raw/run2` | Unedited validator output. `run1` is superseded (a harness JSON-parsing bug in M4); `run2` is the run the numbers come from. The run log proves no detection outcome changed between them. |
| `empirical/run-log.md` | Frozen-artefact verification, pre-registration hashes, tool identity, every argv, exit codes, M3 object selection, run1→run2 comparison. |
| `empirical/REPORT.md` | Findings: 9/13 = 0.69 on the default path, per-class and per-layer comparison with the synthetic frame, controls, the two measurement subtleties, flagged observations, P6/P8 assessment, and "what changed because of the external set". |
| `METHODOLOGY-ADDENDUM-1.md` | **Gate-4 addition (B-14 / RB-03).** Dated addendum to the frozen methodology: the pre-freeze *calibration probes* (not only `-explain`) supplied construct-level detection knowledge that pre-determined F6's and F8's expectation flags. `METHODOLOGY-FROZEN.md` stays byte-identical. |
| `empirical/rescore_addendum.py`, `empirical/results-addendum.csv`, `empirical/SCORING-ADDENDUM.md` | **Gate-4 addition (B-16, B-17, B-32, B-34).** Re-derives the external arm's M2/M3 accounting under the registered rule, adds the obligation split (9/9 established+mandatory + 0/4 discretionary/contested) and the uniquely-labelled denominator ladder including the 9/11[R1] rung. Raw output and `results.csv` untouched. |
| `ADJUDICATION-RESPONSE.md` | **Gate-4 addition.** Every adjudicated B-item with status APPLIED / APPLIED-PARTLY / DISSENTED, the corrected headline numbers, and the new hashes. |
| `second-validator-attempt.md` | The bounded (20-minute) attempt at a second instrument: exact failures, the release asset list proving no CLI artefact exists, why it stopped, and what the one-instrument limitation costs. |

## Reproduce (offline; needs only the pinned binary and Python 3)

```bash
cd research/issue-008

# 1. regenerate the mutant corpus from the known-good bases (asserts one defect each)
python3 harness/make_mutants.py

# 2. regenerate the pre-registered expectations table
python3 harness/author_manifest.py

# 3. confirm the frozen hashes are unchanged
shasum -a 256 -c methodology.sha256
shasum -a 256 -c mutants/mutants.sha256
shasum -a 256 -c mutants/expectations.sha256

# 4. run the pinned validator over both corpora into a NEW run directory
#    (raw output is never overwritten; run1 already exists)
python3 harness/run_validators.py --run-id run2

# 5. analyse (reads results/results.csv + results/diagnostics.csv)
python3 harness/analysis.py
```

The validator is `.tools/sysml` at the repository root, git-ignored; recreate it with the commands in
[`../relational/TOOLING.md`](../relational/TOOLING.md) §1. `run_validators.py --binary <path>` takes an
alternative binary — that is the intended hook for the second instrument this pilot could not obtain
— and it warns loudly if the binary hash differs from the pinned value.

## What is *not* here

- **No second validator.** Syside requires a licence (access boundary, not bypassed); the OMG pilot
  implementation has no CLI release asset and no JVM is installed. See `second-validator-attempt.md`.
- **No second coder** on whether each mutant instantiates the fault class it claims (issue #8 asks for
  one).
- **No conformance claim, no bug report.** Diagnostics are recorded as observations.

## What *is* here, and was not when this pilot began (corrected after adjudication B-23 / RB-12)

- **An empirical challenge set does exist** — `empirical/` runs Researcher A's frozen observed errors
  (13 items, 7 controls) as a *separate* external arm, with its own pre-registration, raw output and
  report. The earlier version of this section said the opposite and that "nothing here was informed by
  Researcher A's work"; both statements were false once Gate 2 opened.
- **Researcher A's work did change these artefacts.** The influence is recorded in
  `reports/issue-008-validator-reliability-pilot.md` addenda **A1** (F2 over-generalised; F7
  corroborated), **A2–A9** (Gate-2 corrections, including the one blocking error A found), and
  **A10–A11** (the external arm, and the adjudicated corrections). The frozen methodology and the
  mutant expectations were fixed before any contact with A; everything after Gate 1 was not.
- **The pilot's claims are addendum-corrected, not as-frozen.** Read the front matter of the report
  before quoting any sentence from §1, §2 P3, §3.5 or §11.
