# METHODOLOGY-ADDENDUM-1 — dated addendum to `METHODOLOGY-FROZEN.md`

**Written:** Gate 4, per `research/relational/adjudication/CORRECTIONS.md` **B-14** (ruling RB-03,
ACCEPTED). **`METHODOLOGY-FROZEN.md` is NOT edited** — it stays byte-identical
(`2c80d63e8800be9ca67a051aaffdbc4b6c56c1b576002fc4446fe82862e6f00b`) per `PROTOCOL.md`
Amendment A1. This file records what that frozen document under-described, and supersedes it on one
point only.

## What the frozen file says (§12.6, quoted)

> **6. The author had read the instrument's `-explain` code list** before writing expectations
> (logged in `results/calibration/PRE-FREEZE-CALIBRATION.md`). This biases expectations *towards*
> the instrument's advertised capability. It cannot be undone; it is disclosed. The expectation is
> nonetheless anchored to a specification constraint, and H5/H9 predict silence despite the author
> having seen the code list.

## What it should have said (adjudication RB-03)

The disclosure is **too narrow**: `-explain` was not the only pre-freeze source of expectation
knowledge. The calibration log also recorded **construct-level detection observations**, made by
running the instrument on probe models before the expectations were authored:

| probe (in `results/calibration/probes/`) | observation recorded pre-freeze | expectation it pre-determines |
|---|---|---|
| `q1.sysml` | `error[incommensurable-binding]`: "cannot bind kg (dimension M) to a feature typed by SpeedValue" | **F6's `expected_detectable = yes`** — the dimensional mechanism was already observed firing |
| `m1.sysml` | `error[metadata-metaclass]` on an annotation typed by a `part def` | **F8-01's `yes`** |
| `m2.sysml` | `error[metadata-owning-type-feature]` on a misspelt metadata body feature | **F8-02's `yes`** |
| `t1.sysml` | `warning[bound-feature-types]` on a non-conforming bound value | the severity expectation for the whole F6 arm |
| `t2.sysml` | `error[syntax]: missing ';'` | F1's trivial-detectability prior |
| `bad.sysml` | `error[unresolved]` with a "did you mean" hint | F2's trivial-detectability prior |

**Consequence, stated plainly.** For F6 and F8, "expected detectable" was written *after* the same
mechanism had been watched firing. That part of the expectation audit is **near-tautological** and
must be labelled **informed, not blind, and weak by construction** wherever the audit is quoted. The
detection counts themselves are unaffected: 23/32 is computed from raw diagnostics and does not
depend on any expectation. What loses weight is the audit's claim to have anticipated the instrument.

**What does not change.** The frozen hypotheses, the fault model, the measurement definitions, the
metrics, the exclusions and every other threat in §12. H5 and H9 were falsified/mixed *despite* the
anchoring, which remains the strongest available sign that the pre-registration bound the report.

**Applies to:** report §4.1 and Addendum A8, and `research/relationa/../results/analysis.md` wherever
the audit is described. `research/relational/gate-log.md` Gate 1 is corrected by the Lead (L-1).
