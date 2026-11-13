# External challenge-set run log — `run2`

Written by `empirical/run_external.py` at 2026-11-13T14:36:06Z.

## 1. Frozen artefact verification

| artefact | recorded | recomputed | verdict |
|---|---|---|---|
| `subset.json` | `bc2b92a5fdff6e976ae7156b13beba3535f0895e4a41268cf76c1551a6c3dfaa` | `bc2b92a5fdff6e976ae7156b13beba3535f0895e4a41268cf76c1551a6c3dfaa` | **OK** |
| `models/manifest.csv` | `a968ff34079a35cdab943dd72415853a4f05617eb353b8deb5665f93ae26b0cb` | `a968ff34079a35cdab943dd72415853a4f05617eb353b8deb5665f93ae26b0cb` | **OK** |
| 36 files in `models/manifest.csv` | per-row sha256 + bytes | all match | **OK** |

`frozen_utc` recorded by A: 2026-11-13T14:33:20Z.

**Result:** all hashes verified; run proceeded.

## 2. Pre-registration hashes

| version | sha256 | note |
|---|---|---|
| first draft | `0106e08276103e9afbfa6d37015f04f57d2f1a5fc0a4976feb22c2555254f6f2` | header carried a forward-dated written-time; **superseded before any run** (this hash was taken at 14:35:15Z, before run1) — see §7 |
| **frozen** | `9458406e7db665ac42f5a3a896a7dc05b094b0fb6e8ef3a4ab9ed9db7e6acfbc` | the version this run implements |

**CORRECTED 2026-11-13T15:08Z under adjudication B-12 / RB-01.** The sentence that stood here
claimed that no rule differed between the two versions and that the change was confined to a header
timestamp. That was wrong about the hash: `9458406e…` is the hash **after** AM1 (it contains the
amendment section), so it cannot have existed before the first run, and the pre-run value in
`PRE-REGISTRATION.sha256` was overwritten when the amendment was appended. See §7 for the full
disclosure and what the pre-registration actually rests on.

## 3. Instrument

- path: `/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml`
- binary sha256: `ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0` (MATCH against TOOLING.md)
- `-version`:

```
sysml v0.12.1
  Commit:     b2f0e9b802a334369da94312c35cefbd8726d3bf
  Build time: 2026-11-06_03:25:57
  Go version: go1.27.3
```

## 4. Exact argv, every invocation

```
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T1-C2.sysml   # exit=2   -> raw/run2/ES-T1-C2-E01__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T1-C2.sysml   # exit=2   -> raw/run2/ES-T1-C2-E01__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate greenhouse -validate=greenhouse /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T1-C2.sysml   # exit=2   -> raw/run2/ES-T1-C2-E01__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T1-C2.sysml   # exit=2   -> raw/run2/ES-T1-C2-E01__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T1-C3.sysml   # exit=0   -> raw/run2/ES-T1-C3-E01__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T1-C3.sysml   # exit=0   -> raw/run2/ES-T1-C3-E01__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate greenhouse -validate=greenhouse /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T1-C3.sysml   # exit=0   -> raw/run2/ES-T1-C3-E01__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T1-C3.sysml   # exit=0   -> raw/run2/ES-T1-C3-E01__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T2-C1.sysml   # exit=2   -> raw/run2/ES-T2-C1-E01__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T2-C1.sysml   # exit=2   -> raw/run2/ES-T2-C1-E01__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate crossing -validate=crossing /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T2-C1.sysml   # exit=2   -> raw/run2/ES-T2-C1-E01__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T2-C1.sysml   # exit=2   -> raw/run2/ES-T2-C1-E01__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T2-C2.sysml   # exit=0   -> raw/run2/ES-T2-C2-E01__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T2-C2.sysml   # exit=0   -> raw/run2/ES-T2-C2-E01__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate levelCrossing -validate=levelCrossing /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T2-C2.sysml   # exit=2   -> raw/run2/ES-T2-C2-E01__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T2-C2.sysml   # exit=2   -> raw/run2/ES-T2-C2-E01__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T3-C1.sysml   # exit=2   -> raw/run2/ES-T3-C1-E01__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T3-C1.sysml   # exit=2   -> raw/run2/ES-T3-C1-E01__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate pump -validate=pump /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T3-C1.sysml   # exit=2   -> raw/run2/ES-T3-C1-E01__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T3-C1.sysml   # exit=2   -> raw/run2/ES-T3-C1-E01__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T3-C2.sysml   # exit=2   -> raw/run2/ES-T3-C2-E01__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T3-C2.sysml   # exit=2   -> raw/run2/ES-T3-C2-E01__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T3-C2.sysml   # exit=2   -> raw/run2/ES-T3-C2-E01__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T3-C2.sysml   # exit=2   -> raw/run2/ES-T3-C2-E02__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T3-C2.sysml   # exit=2   -> raw/run2/ES-T3-C2-E02__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T3-C2.sysml   # exit=2   -> raw/run2/ES-T3-C2-E02__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C1.sysml   # exit=2   -> raw/run2/ES-T4-C1-E01__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C1.sysml   # exit=2   -> raw/run2/ES-T4-C1-E01__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate controller -validate=controller /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C1.sysml   # exit=2   -> raw/run2/ES-T4-C1-E01__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C1.sysml   # exit=2   -> raw/run2/ES-T4-C1-E01__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C1.sysml   # exit=2   -> raw/run2/ES-T4-C1-E02__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C1.sysml   # exit=2   -> raw/run2/ES-T4-C1-E02__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate controller -validate=controller /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C1.sysml   # exit=2   -> raw/run2/ES-T4-C1-E02__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C1.sysml   # exit=2   -> raw/run2/ES-T4-C1-E02__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C2.sysml   # exit=2   -> raw/run2/ES-T4-C2-E01__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C2.sysml   # exit=2   -> raw/run2/ES-T4-C2-E01__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C2.sysml   # exit=2   -> raw/run2/ES-T4-C2-E01__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C3.sysml   # exit=0   -> raw/run2/ES-T4-C3-E01__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C3.sysml   # exit=0   -> raw/run2/ES-T4-C3-E01__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate fleet -validate=fleet /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C3.sysml   # exit=0   -> raw/run2/ES-T4-C3-E01__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T4-C3.sysml   # exit=0   -> raw/run2/ES-T4-C3-E01__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T5-C2.sysml   # exit=2   -> raw/run2/ES-T5-C2-E01__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T5-C2.sysml   # exit=2   -> raw/run2/ES-T5-C2-E01__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate gs -validate=gs /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T5-C2.sysml   # exit=2   -> raw/run2/ES-T5-C2-E01__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T5-C2.sysml   # exit=2   -> raw/run2/ES-T5-C2-E01__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T6-C2.sysml   # exit=2   -> raw/run2/ES-T6-C2-E01__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T6-C2.sysml   # exit=2   -> raw/run2/ES-T6-C2-E01__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T6-C2.sysml   # exit=2   -> raw/run2/ES-T6-C2-E01__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T1-C1.sysml   # exit=0   -> raw/run2/CTRL-T1-C1__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T1-C1.sysml   # exit=0   -> raw/run2/CTRL-T1-C1__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate greenhouse -validate=greenhouse /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T1-C1.sysml   # exit=0   -> raw/run2/CTRL-T1-C1__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T1-C1.sysml   # exit=0   -> raw/run2/CTRL-T1-C1__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T2-C3.sysml   # exit=0   -> raw/run2/CTRL-T2-C3__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T2-C3.sysml   # exit=0   -> raw/run2/CTRL-T2-C3__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate crossing -validate=crossing /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T2-C3.sysml   # exit=0   -> raw/run2/CTRL-T2-C3__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T2-C3.sysml   # exit=0   -> raw/run2/CTRL-T2-C3__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T3-C3.sysml   # exit=0   -> raw/run2/CTRL-T3-C3__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T3-C3.sysml   # exit=0   -> raw/run2/CTRL-T3-C3__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate pump -validate=pump /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T3-C3.sysml   # exit=0   -> raw/run2/CTRL-T3-C3__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T3-C3.sysml   # exit=0   -> raw/run2/CTRL-T3-C3__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T5-C1.sysml   # exit=0   -> raw/run2/CTRL-T5-C1__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T5-C1.sysml   # exit=0   -> raw/run2/CTRL-T5-C1__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate station -validate=station /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T5-C1.sysml   # exit=0   -> raw/run2/CTRL-T5-C1__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T5-C1.sysml   # exit=0   -> raw/run2/CTRL-T5-C1__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T5-C3.sysml   # exit=2   -> raw/run2/CTRL-T5-C3__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T5-C3.sysml   # exit=2   -> raw/run2/CTRL-T5-C3__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate station -validate=station /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T5-C3.sysml   # exit=2   -> raw/run2/CTRL-T5-C3__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T5-C3.sysml   # exit=2   -> raw/run2/CTRL-T5-C3__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T6-C1.sysml   # exit=0   -> raw/run2/CTRL-T6-C1__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T6-C1.sysml   # exit=0   -> raw/run2/CTRL-T6-C1__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate dwelling -validate=dwelling /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T6-C1.sysml   # exit=0   -> raw/run2/CTRL-T6-C1__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T6-C1.sysml   # exit=2   -> raw/run2/CTRL-T6-C1__M4.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T6-C3.sysml   # exit=0   -> raw/run2/CTRL-T6-C3__M1.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T6-C3.sysml   # exit=0   -> raw/run2/CTRL-T6-C3__M2.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate house -validate=house /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T6-C3.sysml   # exit=0   -> raw/run2/CTRL-T6-C3__M3.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/relational/empirical-subset/models/T6-C3.sysml   # exit=2   -> raw/run2/CTRL-T6-C3__M4.*.txt
```

## 5. Object used for M3 (mechanical rule, PRE-REGISTRATION §3.1)

| item | object | object source |
|---|---|---|
| ES-T1-C2-E01 | greenhouse | T1-C2 |
| ES-T1-C3-E01 | greenhouse | T1-C3 |
| ES-T2-C1-E01 | crossing | T2-C1 |
| ES-T2-C2-E01 | levelCrossing | T2-C2 |
| ES-T3-C1-E01 | pump | T3-C1 |
| ES-T3-C2-E01 | *(none — n/a)* | T3-C2 |
| ES-T4-C1-E01 | controller | T4-C1 |
| ES-T4-C2-E01 | *(none — n/a)* | T4-C2 |
| ES-T4-C3-E01 | fleet | T4-C3 |
| ES-T5-C2-E01 | gs | T5-C2 |
| ES-T6-C2-E01 | *(none — n/a)* | T6-C2 |
| CTRL-T1-C1 | greenhouse | T1-C1 |
| CTRL-T2-C3 | crossing | T2-C3 |
| CTRL-T3-C3 | pump | T3-C3 |
| CTRL-T5-C1 | station | T5-C1 |
| CTRL-T5-C3 | station | T5-C3 |
| CTRL-T6-C1 | dwelling | T6-C1 |
| CTRL-T6-C3 | house | T6-C3 |

## 6. run1 → run2 comparison (what the AM1 fixes changed, and what they did not)

The fixes in AM1 were to *derivation*, so the question that matters is whether any **detection**
outcome moved.

| check | run1 | run2 | verdict |
|---|---|---|---|
| M1 items `detected` | 9: ES-T1-C2-E01, ES-T2-C1-E01, ES-T3-C1-E01, ES-T3-C2-E01, ES-T3-C2-E02, ES-T4-C1-E01, ES-T4-C2-E01, ES-T5-C2-E01, ES-T6-C2-E01 | **identical set of 9** | **no change** |
| M2/M3 items `detected` (standing `violated`) | 0 — no raw file in either run contains `standing: violated` | **0** | **no change** |
| M4 | broken in run1 (JSON parsed from a text invocation → `silent` everywhere) | 9 detected, exit codes differ from M1 on four models | fixed by AM1; M4 is reported from run2 only |
| other label changes | `none`/`silent`/`wrong-target` on controls and non-applicable items | `not applicable` / `clean model` / `diagnostic (...)` | **labelling only**, no detection moved |

So the run1 → run2 difference is: M4 becomes measurable, and roughly twenty rows are relabelled with
the more precise vocabulary AM1 introduced. **No item changed from detected to not-detected or the
reverse.** The reported numbers use run2; run1 stays in `raw/run1/` as the superseded set.

## 7. Correction under adjudication B-12 / RB-01 — the pre-registration hash cannot establish pre-registration

**What I wrote (quoted so it stays visible):** *"frozen at `9458406e7db665ac42f5a3a896a7dc05b094b0fb6e8ef3a4ab9ed9db7e6acfbc`
**before the first run** (the superseded first draft, `0106e082…`, differs only in a header
timestamp)"*, and in §2, *"No rule, mode, expectation or scoring definition differs between the two
versions; only the header timestamp and a note were changed, before the first run."*

**What is wrong.** `9458406e…` was computed at **14:36:04Z**, *after* run1 (14:35:38–41Z), and it
contains amendment AM1. It therefore cannot be the hash of a document that existed before the first
run, and the value in `PRE-REGISTRATION.sha256` at run1 is no longer recoverable. The claim that
"only a header timestamp and a note" changed is also wrong: AM1 **added §11** (three derivation
fixes) and is dated after run1.

**What the pre-registration actually rests on, and nothing more:**

1. **Content.** The registered invocation set, the line-attribution rule, the five-valued standing
   map, the control rule, the class mapping and the P6/P8 decision rule are all in the file the run
   implements, and none of them was altered by AM1 — AM1 changed a serialisation flag, introduced
   `not applicable` for models that do not analyse cleanly, and relabelled controls. Each of the
   three is disclosed in AM1 and each moves items from `not detected` toward `not applicable`, i.e.
   it reduces what can be claimed.
2. **AM1's own disclosure.** The amendment states what changed and why, in the same file.
3. **The run1 → run2 identity of the detected set.** `run-log.md` §6 recomputes the M1 detected set
   from the preserved run1 raw files: **identical at n = 9**, and no raw file in either run contains
   `standing: violated`, so M2/M3 had zero detections in both. Whatever AM1 changed, it did not
   change a detection outcome.

**What is lost.** The one-step, hash-based proof that the rules preceded the first run. The honest
status of the pre-registration is therefore **content-evidenced and internally consistent, not
hash-proven**. A future run must hash the pre-registration in a separate `.sha256` file and never
regenerate it (protocol amendment L-2).
