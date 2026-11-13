# Pre-freeze tool-invocation calibration (NOT evidence about mutants)

**Timestamps:** 2026-11-13, 14:06–14:08 UTC (before `METHODOLOGY-FROZEN.md` was written).
**Status:** logged because the protocol requires every accessed source and every attempt to be
recorded. These probes test **how the pinned binary is invoked and what its output looks like**.
They are *not* part of the mutant corpus, *not* part of the known-good corpus, and none of them
is counted in any denominator.

Probe files are preserved in `probes/` exactly as written. The validator was
`.tools/sysml` (sysml v0.12.1, `ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0`).
Every invocation printed the harmless stderr line
`sysml: record cache unavailable, holding every file loaded: mkdir ~/Library/Caches/sysml-ls: operation not permitted`
(documented in `research/relational/TOOLING.md` §1 and not a model diagnostic).

## Why this was done before the freeze

The frozen methodology has to state the *measurement* (what counts as detected, at which
severity, in which layer). That requires knowing the output shape and the exit-code convention.
Guessing it, or discovering it after the mutants existed, would have made the pre-registration
partly retrospective.

## What was learned (each item is a fact about the instrument's interface, not about any mutant)

| Probe | Observation | Consequence for the methodology |
|---|---|---|
| `hello.sysml` | `-validate` prints `✓ …: no errors`, exit 0. `-validate -format json` prints a JSON envelope `{status, exit, checks, diagnostics, output, errors}`. On a clean model `diagnostics` is `null`. | The harness parses `diagnostics[]` (`severity`, `code`, `pass`, `line`, `column`, `message`) and records the JSON `exit` field. |
| `bad.sysml` | An `unresolved` error produces exit 2 **and** the stderr line `did not analyse cleanly; no check was made`. | **Short-circuit.** A defect at an early layer can suppress later layers. Recorded as a measured property of this instrument (H-layers), not as a nuisance to be hidden. |
| `t1.sysml` (`attribute :>> mass = "heavy";` on a `Real` feature) | Reported as `warning[bound-feature-types]`, exit 0. | "Detected at the wrong severity" is a real, measurable outcome. Severity must be recorded, not collapsed into a boolean. |
| `t2.sysml` (missing `;`) | `error[syntax]: missing ';' at end of declaration`, exit 2, no further checks. | F1 mutants will be visible to layer 1; nothing else about them is measurable (short-circuit). |
| `t3.sysml` (`part engine : Engine[2];`) | No diagnostic. Legal. | Explicit multiplicity alone is not a defect; F4 mutants need an actual violation (bound order, non-Natural bound, redefinition widening, end-feature multiplicity). |
| `q1.sysml` | `ISQ::*` and `SI::*` resolve. `incommensurable-binding` fires as **error**; `quantity-unit` fires as **warning**, and fired on `4.5 [m]` only because a local `attribute m` shadowed the metre unit. | F6 mutants work, but feature names must not collide with library unit symbols. Recorded as a design constraint. |
| `en.sysml`, `meta.sysml`, `req.sysml`, `m3.sysml` | Enumeration definitions, `metadata def` + `@X { … }` annotations, requirement defs with `require constraint`, and `satisfy … by …` all parse and validate cleanly. | The constructs the fault model needs are available. |
| `m1.sysml` (`@SafetyCase` where `SafetyCase` is a `part def`) | `error[metadata-metaclass]`. | F8 has at least one construct that this instrument *does* catch — the Sensmetry-documented "silently ignored" case is not automatically a gap here. |
| `m2.sysml` (typo `levl` inside a metadata body) | `error[metadata-owning-type-feature]`. | F8 typo case is catchable. |
| `m4.sysml` (`metadata def abstract X`) | Does not parse (`reserved-keyword-name`, `syntax`). | `metadata def abstract …` is not admitted by this notation; not used in the corpus. |

## Access notes

- No network request was needed for the probes. The validator's model library is embedded in the
  binary; `.tools/share` contains only man pages.
- `-explain` (bare) was run to enumerate the tool's own diagnostic codes. **This is a
  documented capability list, not a result**, and it is a threat to validity for the
  pre-registered expectations: the mutant author could see which conditions the tool advertises a
  code for. It is recorded in the frozen methodology and revisited in the report.
- No Syside attempt, no licence check bypassed, no client spoofed.
