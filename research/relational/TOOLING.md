# Pinned tooling and access log (demonstration run)

Recorded by the Team Lead on 2026-11-13, before researcher work began. These are the only
tool versions the pilot's results are valid for. A tool change requires a re-run or an explicit
"results not valid for this version" statement.

## 1. Primary validator — OpenSysML CLI (open source, Apache-2.0)

| Field | Value |
|---|---|
| Project | <https://github.com/Open-MBEE/OpenSysML> |
| Release | `v0.12.1`, published 2026-11-06T02:46:10Z |
| Asset | `opensysml-darwin-arm64.tar.gz` (33,743,961 bytes) |
| Asset sha256 | `0f16d282ec50bfda916e74ef102e5b257bf2c9964f6e44df9db495db4fc96210` |
| `sysml` binary sha256 | `ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0` |
| Build identity | `sysml v0.12.1`, commit `b2f0e9b802a334369da94312c35cefbd8726d3bf`, build time 2026-11-06_03:25:57, go1.27.3 |
| Local path (git-ignored) | `.tools/sysml` |
| Licence basis | project states Apache-2.0 |

Re-create with:

```bash
mkdir -p .tools && cd .tools
curl -sSLO https://github.com/Open-MBEE/OpenSysML/releases/download/v0.12.1/opensysml-darwin-arm64.tar.gz
shasum -a 256 opensysml-darwin-arm64.tar.gz     # expect 0f16d282...c96210
tar xzf opensysml-darwin-arm64.tar.gz && ./sysml -version
```

### Behaviour confirmed by the Lead before the pilot (smoke test, not evidence)

- `sysml -validate <file>` reports `file:line:col: severity[code]: message` and exits nonzero on
  error; `-format json|sarif|junit` gives machine-readable output; `-explain <code>` documents each
  diagnostic code and the clause/constraint behind it.
- Diagnostics are layered in the tool's own taxonomy: **Syntax**, **Name resolution**, **Typing**,
  then constraint/other groups — usable for a detection-layer column, but see
  [`PROTOCOL.md`](PROTOCOL.md) §3 (validator verdicts are not ground truth).
- On a model with no `private import ScalarValues::*;`, a bare `Real`/`Integer` is reported as
  `unresolved` with a "did you mean ScalarValues::Real" hint. **Mutant authors must therefore use
  fully resolved preludes, or every mutant in the class "unresolved reference" will be confounded
  with a missing stdlib import.**
- A cache warning (`record cache unavailable: mkdir ~/Library/Caches/sysml-ls: operation not
  permitted`) appears under the sandbox and is harmless: the tool falls back to holding files
  loaded. Recorded so later runs do not mistake it for a model diagnostic.

## 2. Second validator — OMG SysML v2 Pilot Implementation

Not usable in this environment unless a JVM is obtained: no Java runtime is installed
(`/usr/libexec/java_home` reports none), and the project publishes **no standalone validator CLI**
asset (see `evidence/spec-tooling.md` §3.1: release assets are the Jupyter kernel zip, JupyterLab
extension, `.kpar` libraries and source archives). Status: **bounded attempt**, with the exact
failure to be logged if it fails. Researchers may substitute a second *independent* open
instrument only if found and pinned; otherwise the pilot reports one-instrument results.

## 3. Commercial validator — Syside (Sensmetry)

`pip install syside==0.11.0` installs the Syside Automator library but the runtime refuses to
start without a licence:

```
Please provide a license key as an argument, set the SYSIDE_LICENSE_KEY environment variable,
or provide a path to a file containing the license key.
```

This is a **licence/access boundary, not a technical failure**. It is not to be bypassed, and
Syside results are out of scope for this pilot. Recorded as an access limitation of the
"available open validators" question: one prominent validator is not openly runnable.

## 4. Specification and catalogue inputs (already pinned by issue #1)

- SysML 2.0 Part 1 `formal/2026-03-02`; KerML 1.0 `formal/2026-03-01`; XMI `ptc/25-02-15`,
  `ptc/25-04-04` — hashes in [`../../catalogue/README.md`](../../catalogue/README.md) §1.
- `catalogue/classified.csv` — 623 constraints with kind, obligation, dependency class and
  published-OCL executability. Use this for mutant provenance (constraint name + clause), not
  as a claim that the constraint executes.
