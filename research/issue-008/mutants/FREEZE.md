# Mutant corpus and expectation freeze

Frozen at **2026-11-13T14:13Z** (see `expectations.sha256` mtime and the run log), **before the
first validator run over `mutants/`**.

| Artefact | Role | Hash |
|---|---|---|
| `MANIFEST.csv` | the pre-registered expectations: per-mutant fault class, specification condition, expected layer, expected detectability, rationale, plausibility, surface-tell flag | see `expectations.sha256` |
| `*.sysml` (32) | the mutant corpus, one injected defect each, regenerable with `harness/make_mutants.py` | see `mutants.sha256` |
| `harness/make_mutants.py` | generator; asserts each substitution matches exactly once | see `expectations.sha256` |
| `harness/author_manifest.py` | the authored expectation table (this file is the source of MANIFEST.csv) | see `expectations.sha256` |
| `../METHODOLOGY-FROZEN.md` | methodology and pre-registered hypotheses, frozen earlier | see `../methodology.sha256` |

**Rules that apply from here.** No expectation in `MANIFEST.csv` is edited after the first run. If a
revision is genuinely needed it is appended to `MANIFEST-REVISIONS.md` as a dated row with the old
and new value and the reason, and both are reported. A validator's silence does not reclassify a
mutant as valid, and a validator's firing does not make it defective.

Corpus summary at freeze: 32 mutants, 8 fault classes × 4; `expected_detectable` = 24 yes / 2
uncertain / 6 no; `surface_tell` = 3 yes / 29 no.
