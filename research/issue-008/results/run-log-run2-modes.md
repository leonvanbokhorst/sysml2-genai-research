# Per-mode probe run log — `run2-modes`

Written by `harness/run_modes.py` at 2026-11-13T14:24:51Z. This run exists because the original
pilot ran one invocation only (`-validate -format json`); see the Gate-2 response to
Researcher A's objection O1.

## Instrument

- path: `/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml`
- binary sha256: `ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0` (MATCH against TOOLING.md)
- `-version`:

```
sysml v0.12.1
  Commit:     b2f0e9b802a334369da94312c35cefbd8726d3bf
  Build time: 2026-11-06_03:25:57
  Go version: go1.27.3
```

## Exact argv (every probe is read-only over the model files)

```
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/mutants/M31-F7-01-unreachable-state.sysml   # exit=0   -> raw/run2-modes/M31-F7-01-unreachable-state__default-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -self-check /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/mutants/M31-F7-01-unreachable-state.sysml   # exit=0   -> raw/run2-modes/M31-F7-01-unreachable-state__self-check.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/known-good/KG-05-states.sysml   # exit=0   -> raw/run2-modes/KG-05-states(base of F7-01)__default-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -self-check /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/known-good/KG-05-states.sysml   # exit=0   -> raw/run2-modes/KG-05-states(base of F7-01)__self-check.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/mutants/M31-F7-02-satisfied-but-violated.sysml   # exit=0   -> raw/run2-modes/M31-F7-02-satisfied-but-violated__default-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/mutants/M31-F7-02-satisfied-but-violated.sysml   # exit=1   -> raw/run2-modes/M31-F7-02-satisfied-but-violated__satisfy.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate vehicle -validate=vehicle /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/mutants/M31-F7-02-satisfied-but-violated.sysml   # exit=1   -> raw/run2-modes/M31-F7-02-satisfied-but-violated__instantiate-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/known-good/KG-07-requirements.sysml   # exit=0   -> raw/run2-modes/KG-07-requirements(base of F7-02)__default-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/known-good/KG-07-requirements.sysml   # exit=0   -> raw/run2-modes/KG-07-requirements(base of F7-02)__satisfy.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate vehicle -validate=vehicle /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/known-good/KG-07-requirements.sysml   # exit=0   -> raw/run2-modes/KG-07-requirements(base of F7-02)__instantiate-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/mutants/M31-F7-03-missing-flow.sysml   # exit=0   -> raw/run2-modes/M31-F7-03-missing-flow__default-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -self-check /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/mutants/M31-F7-03-missing-flow.sysml   # exit=0   -> raw/run2-modes/M31-F7-03-missing-flow__self-check.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/known-good/KG-09-actions.sysml   # exit=0   -> raw/run2-modes/KG-09-actions(base of F7-03)__default-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -self-check /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/known-good/KG-09-actions.sysml   # exit=0   -> raw/run2-modes/KG-09-actions(base of F7-03)__self-check.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/mutants/M31-F7-04-contradictory-assertions.sysml   # exit=0   -> raw/run2-modes/M31-F7-04-contradictory-assertions__default-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate testObject -validate=testObject /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/mutants/M31-F7-04-contradictory-assertions.sysml   # exit=2   -> raw/run2-modes/M31-F7-04-contradictory-assertions__instantiate-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/known-good/KG-10-asserts.sysml   # exit=0   -> raw/run2-modes/KG-10-asserts(base of F7-04)__default-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate testObject -validate=testObject /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/known-good/KG-10-asserts.sysml   # exit=2   -> raw/run2-modes/KG-10-asserts(base of F7-04)__instantiate-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/mutants/M31-F1-03-keyword-typo.sysml   # exit=2   -> raw/run2-modes/M31-F1-03-keyword-typo__default-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/mutants/M31-F1-03-keyword-typo.sysml   # exit=2   -> raw/run2-modes/M31-F1-03-keyword-typo__strict.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/../issue-007/corpus/normalized/T6-C1.sysml   # exit=0   -> raw/run2-modes/A-T6-C1(reserved-keyword)__default-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/../issue-007/corpus/normalized/T6-C1.sysml   # exit=2   -> raw/run2-modes/A-T6-C1(reserved-keyword)__strict.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/../issue-007/corpus/normalized/T2-C2.sysml   # exit=0   -> raw/run2-modes/A-T2-C2(satisfy-no-by)__default-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/../issue-007/corpus/normalized/T2-C2.sysml   # exit=0   -> raw/run2-modes/A-T2-C2(satisfy-no-by)__satisfy.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate levelCrossing -validate=levelCrossing /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/../issue-007/corpus/normalized/T2-C2.sysml   # exit=2   -> raw/run2-modes/A-T2-C2(satisfy-no-by)__instantiate-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -strict /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/../issue-007/corpus/normalized/T2-C2.sysml   # exit=2   -> raw/run2-modes/A-T2-C2(satisfy-no-by)__strict.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/../issue-007/corpus/normalized/T1-C1.sysml   # exit=0   -> raw/run2-modes/A-T1-C1(dangling-succession)__default-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/../issue-007/corpus/normalized/T1-C1.sysml   # exit=0   -> raw/run2-modes/A-T1-C1(dangling-succession)__satisfy.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -instantiate greenhouse -validate=greenhouse /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/../issue-007/corpus/normalized/T1-C1.sysml   # exit=0   -> raw/run2-modes/A-T1-C1(dangling-succession)__instantiate-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -validate -format json /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/../issue-007/corpus/normalized/T3-C2.sysml   # exit=2   -> raw/run2-modes/A-T3-C2(dangling-satisfy)__default-validate.*.txt
/Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/.tools/sysml -satisfy /Users/leonvanbokhorst/repos/sysml2-to-do-with-research-i-dont-know/research/issue-008/../issue-007/corpus/normalized/T3-C2.sysml   # exit=2   -> raw/run2-modes/A-T3-C2(dangling-satisfy)__satisfy.*.txt
```

## Outcome table

| case | mode | exit | outcome | note |
|---|---|---:|---|---|
| M31-F7-01-unreachable-state | default-validate | 0 | clean | state machine: no part usage to instantiate |
| M31-F7-01-unreachable-state | self-check | 0 | clean | state machine: no part usage to instantiate |
| KG-05-states(base of F7-01) | default-validate | 0 | clean | base machine is complete: every state reachable |
| KG-05-states(base of F7-01) | self-check | 0 | clean | base machine is complete: every state reachable |
| M31-F7-02-satisfied-but-violated | default-validate | 0 | clean | part usage `vehicle` carries a false require constraint |
| M31-F7-02-satisfied-but-violated | satisfy | 1 | violated | part usage `vehicle` carries a false require constraint |
| M31-F7-02-satisfied-but-violated | instantiate-validate | 1 | violated | part usage `vehicle` carries a false require constraint |
| KG-07-requirements(base of F7-02) | default-validate | 0 | clean | same construct, requirement is true (positive control) |
| KG-07-requirements(base of F7-02) | satisfy | 0 | holds | same construct, requirement is true (positive control) |
| KG-07-requirements(base of F7-02) | instantiate-validate | 0 | holds | same construct, requirement is true (positive control) |
| M31-F7-03-missing-flow | default-validate | 0 | clean | action definition: no object to instantiate |
| M31-F7-03-missing-flow | self-check | 0 | clean | action definition: no object to instantiate |
| KG-09-actions(base of F7-03) | default-validate | 0 | clean | base has the flow |
| KG-09-actions(base of F7-03) | self-check | 0 | clean | base has the flow |
| M31-F7-04-contradictory-assertions | default-validate | 0 | clean | part `testObject` carries two contradictory assert constraints |
| M31-F7-04-contradictory-assertions | instantiate-validate | 2 | undecided (no verdict) | part `testObject` carries two contradictory assert constraints |
| KG-10-asserts(base of F7-04) | default-validate | 0 | clean | one assert, no value for the feature it names |
| KG-10-asserts(base of F7-04) | instantiate-validate | 2 | undecided (no verdict) | one assert, no value for the feature it names |
| M31-F1-03-keyword-typo | default-validate | 2 | error-diagnostic (exit 2) | F1 notation mutant, baseline exit 2 in default mode |
| M31-F1-03-keyword-typo | strict | 2 | error-diagnostic (exit 2) | F1 notation mutant, baseline exit 2 in default mode |
| A-T6-C1(reserved-keyword) | default-validate | 0 | error-diagnostic (exit 0) | A's reserved-keyword-as-name model (O3) |
| A-T6-C1(reserved-keyword) | strict | 2 | error-diagnostic (exit 2) | A's reserved-keyword-as-name model (O3) |
| A-T2-C2(satisfy-no-by) | default-validate | 0 | error-diagnostic (exit 0) | A's S2 record: satisfy with no satisfying feature (O4) |
| A-T2-C2(satisfy-no-by) | satisfy | 0 | holds | A's S2 record: satisfy with no satisfying feature (O4) |
| A-T2-C2(satisfy-no-by) | instantiate-validate | 2 | undecided (no verdict) | A's S2 record: satisfy with no satisfying feature (O4) |
| A-T2-C2(satisfy-no-by) | strict | 2 | error-diagnostic (exit 2) | A's S2 record: satisfy with no satisfying feature (O4) |
| A-T1-C1(dangling-succession) | default-validate | 0 | clean | A's N1 record at a succession source (O5) |
| A-T1-C1(dangling-succession) | satisfy | 0 | holds | A's N1 record at a succession source (O5) |
| A-T1-C1(dangling-succession) | instantiate-validate | 0 | holds | A's N1 record at a succession source (O5) |
| A-T3-C2(dangling-satisfy) | default-validate | 2 | error-diagnostic (exit 2) | A's N1 record at a satisfy target: detected in default mode (O5 contrast) |
| A-T3-C2(dangling-satisfy) | satisfy | 2 | error-diagnostic (exit 2) | A's N1 record at a satisfy target: detected in default mode (O5 contrast) |

## hash of the reviewed artefact

The Gate-2 review this probe run responds to:

```
$ shasum -a 256 research/relational/cross-reviews/A-reviews-B.md
05ca64ccaa4ceae4032ca36aa22f2090c5565449d021764a9da480bbbb1a8102  research/relational/cross-reviews/A-reviews-B.md
```

(computed 2026-11-13T14:38Z on the file I read; the file was frozen by its author at 14:22Z).

Recorded here so the response document can cite a value that was actually computed rather than
transcribed. The response itself carries this hash.
