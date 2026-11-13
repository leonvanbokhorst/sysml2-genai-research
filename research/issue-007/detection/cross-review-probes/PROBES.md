# Cross-review probes run by Researcher A against B's published mutants (read-only)
# date -u: 2026-11-13T14:20:30Z  instrument: .tools/sysml v0.12.1 (sha256 ddfc2962…1598f0)

## F7-02-instantiate
$ .tools/sysml -instantiate vehicle -validate=vehicle research/issue-008/mutants/M31-F7-02-satisfied-but-violated.sysml
✓ package KG07Requirements
✓ Created instance of KG07Requirements::vehicle
  ID: 1
  Use %features vehicle to inspect
✗ satisfy vehicleMaximumMass by vehicle fails (on KG07Requirements::vehicle ID: 1)
  Required condition evaluated to false: massActual <= massRequired
✗ KG07Requirements::vehicle is not valid: 1 of 1 assertion fails
  standing: violated (witnessed: 1 run under reverse)
[exit 1]

## F7-02-known-good-control
$ .tools/sysml -instantiate vehicle -validate=vehicle research/issue-008/known-good/KG-07-requirements.sysml
✓ package KG07Requirements
✓ Created instance of KG07Requirements::vehicle
  ID: 1
  Use %features vehicle to inspect
✓ satisfy vehicleMaximumMass by vehicle holds (on KG07Requirements::vehicle ID: 1)
✓ KG07Requirements::vehicle is valid: its 1 assertion holds
  standing: holds (observed: 1 run under reverse)
[exit 0]

## F7-04-instantiate
$ .tools/sysml -instantiate testObject -validate=testObject research/issue-008/mutants/M31-F7-04-contradictory-assertions.sysml
✓ package KG10Asserts
✓ Created instance of KG10Asserts::testObject
  ID: 1
  Use %features testObject to inspect
? assert constraint could not be evaluated (on KG10Asserts::testObject ID: 1)
  Error: constraint : assertion evaluation failed: no value for feature computedMass
? assert constraint could not be evaluated (on KG10Asserts::testObject ID: 1)
  Error: constraint : assertion evaluation failed: no value for feature computedMass
? KG10Asserts::testObject is not shown valid: 2 of 2 assertions undecided
  standing: not covered (2 undecided)
[exit 2]

## F7-04-alien-instantiate
$ .tools/sysml -instantiate alienObject -validate=alienObject research/issue-008/mutants/M31-F7-04-contradictory-assertions.sysml
✓ package KG10Asserts
✓ Created instance of KG10Asserts::alienObject
  ID: 1
  Use %features alienObject to inspect
? assert could not be evaluated (on KG10Asserts::alienObject ID: 1)
  Error: constraint : assertion evaluation failed: no value for feature mass
? KG10Asserts::alienObject is not shown valid: 1 of 1 assertion undecided
  standing: not covered (1 undecided)
[exit 2]

## F7-01-self-check
$ .tools/sysml -self-check research/issue-008/mutants/M31-F7-01-unreachable-state.sysml
✓ package KG05States
Self-model check: 11 elements, 127 checks, 0 violations, 0 unevaluated
[exit 0]

## F7-03-self-check
$ .tools/sysml -self-check research/issue-008/mutants/M31-F7-03-missing-flow.sysml
✓ package KG09Actions
Self-model check: 45 elements, 490 checks, 0 violations, 0 unevaluated
[exit 0]

## A-S2-instantiate
$ .tools/sysml -instantiate levelCrossing -validate=levelCrossing research/issue-007/corpus/normalized/T2-C2.sysml
research/issue-007/corpus/normalized/T2-C2.sysml:17:19: error[reserved-keyword-name]: "state" is a reserved keyword, not a name the ID terminal admits; write 'state' to use it as a name
        attribute state : String;
                  ^~~~~
✓ package LevelCrossingProtection
✓ Created instance of LevelCrossingProtection::levelCrossing
  ID: 1
  Use %features levelCrossing to inspect
? LevelCrossingProtection::levelCrossing states no assertion to validate
  standing: not covered (states no assertion to validate)
[exit 2]

## A-R1-instantiate
$ .tools/sysml -instantiate fleet -validate=fleet research/issue-007/corpus/normalized/T4-C3.sysml
✓ package WarehouseAgvFleetSystem
✓ Created instance of WarehouseAgvFleetSystem::fleet
  ID: 1
  Use %features fleet to inspect
✓ satisfy returnBeforeLowCharge by fleet holds (on WarehouseAgvFleetSystem::fleet ID: 1)
✓ WarehouseAgvFleetSystem::fleet is valid: its 1 assertion holds
  standing: holds (observed: 1 run under reverse)
[exit 0]

## A-I1-instantiate
$ .tools/sysml -instantiate greenhouse -validate=greenhouse research/issue-007/corpus/normalized/T1-C3.sysml
✓ package GreenhouseIrrigationSystem
✓ Created instance of GreenhouseIrrigationSystem::greenhouse
  ID: 1
  Use %features greenhouse to inspect
✓ satisfy moistureBand by greenhouse holds (on GreenhouseIrrigationSystem::greenhouse ID: 1)
✓ GreenhouseIrrigationSystem::greenhouse is valid: its 1 assertion holds
  standing: holds (observed: 1 run under reverse)
[exit 0]

## A-S1-default-vs-strict-default
$ .tools/sysml -validate research/issue-007/corpus/normalized/T6-C1.sysml
research/issue-007/corpus/normalized/T6-C1.sysml:26:14: error[reserved-keyword-name]: "return" is a reserved keyword, not a name the ID terminal admits; write 'return' to use it as a name
        port return;
             ^~~~~~
✓ package HeatPumpHeating
✓ research/issue-007/corpus/normalized/T6-C1.sysml: no error that stops a check; the notation reported above does not conform
[exit 0]

## A-S1-default-vs-strict-strict
$ .tools/sysml -validate -strict research/issue-007/corpus/normalized/T6-C1.sysml
research/issue-007/corpus/normalized/T6-C1.sysml:26:14: error[reserved-keyword-name]: "return" is a reserved keyword, not a name the ID terminal admits; write 'return' to use it as a name
        port return;
             ^~~~~~
sysml: research/issue-007/corpus/normalized/T6-C1.sysml did not analyse cleanly; no check was made
[exit 2]


## F7-02 JSON shape of the assertion verdict (added 2026-11-13T14:21Z)
$ .tools/sysml -instantiate vehicle -validate=vehicle -format json research/issue-008/mutants/M31-F7-02-satisfied-but-violated.sysml
{
  "status": "fails",
  "exit": 1,
  "checks": [
    {
      "subject": "satisfy vehicleMaximumMass by vehicle on KG07Requirements::vehicle",
      "status": "fails",
      "values": null,
      "lines": [
        "✗ satisfy vehicleMaximumMass by vehicle fails (on KG07Requirements::vehicle ID: 1)",
        "  Required condition evaluated to false: massActual \u003c= massRequired"
      ],
      "rows": null
    },
    {
      "subject": "KG07Requirements::vehicle",
      "status": "fails",
      "values": null,
      "lines": [
        "✗ KG07Requirements::vehicle is not valid: 1 of 1 assertion fails",
        "  standing: violated (witnessed: 1 run under reverse)"
      ],
      "rows": null,
      "plan": {
        "engine": "auto",
