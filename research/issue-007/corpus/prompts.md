# Corpus prompts (written before generation)

**Authored:** 2026-11-13T14:2xZ, before any generation in this pilot. Six tasks, three
configurations, one generation per cell → **18 model outputs**.
**Generator:** DeepSeek-family model served through DSH; exact checkpoint not exposed to the
researcher. Generation performed as inline model output by Researcher A in this session (see
`METHODOLOGY-FROZEN.md` §2.2 and §11.1 for the circularity that creates).

## Design rationale

Each task is a short system-engineering requirement paragraph: a named system, some structure,
at least one obligation that maps naturally onto a `requirement` + `satisfy`, and at least one
element that invites a behaviour (action/state) or a connection/flow. Domains are deliberately
generic and spread across five sectors so that no single SysML idiom dominates. No task shows
SysML text, names a constraint, or hints at an error class. The tasks do not state which
language constructs to use — that choice is the generator's, which is where many coding
decisions will come from.

`C1` = the paragraph alone. `C2` = paragraph + demand for a fenced ```` ```sysml ```` block and
nothing else. `C3` = paragraph + an ordered checklist of inclusion obligations (it says *what to
include*, never *how to be correct*).

Task-to-configuration cells are independent: each was produced in one pass without seeing the
other outputs, with no repair round and no validator in the loop.

---

## T1 — Greenhouse irrigation controller

> A small greenhouse uses an irrigation controller that operates a pump and a solenoid valve.
> The controller receives soil-moisture readings from two moisture probes placed in different
> beds and must keep soil moisture between 35% and 55% for each bed. When moisture in a bed
> falls below 35% the controller opens that bed's valve and runs the pump until the reading
> reaches 50%. If a probe reports no reading for more than 10 minutes, the controller must stop
> all irrigation and raise a fault. Model the greenhouse irrigation system: its structure, the
> moisture-control obligation with an explicit requirement and a satisfy link, and the
> irrigation cycle as a behaviour.

## T2 — Railway level-crossing protection

> A level crossing protects a single-track railway line where it crosses a public road. The
> installation has two barrier arms driven by one motor, a pair of red flashing lights, and a
> train-detection unit that reports approaching, on-crossing and clear states. The barrier must
> be fully lowered before a train reaches the crossing, and must rise again only after the train
> has cleared it. Model the crossing protection system: the physical and control structure, the
> lowering-before-arrival obligation as a requirement with a satisfy link, and the operating
> sequence as a state machine.

## T3 — Infusion pump occlusion alarm

> A volumetric infusion pump delivers fluid through a disposable line. A downstream pressure
> sensor detects occlusion of the line. The pump must raise an audible and visible alarm within
> 2 seconds of an occlusion being detected, and must stop delivery at the same time. The
> occlusion threshold is configured per drug library entry. Model the infusion pump: the pump,
> line, sensor and alarm structure, the alarm-timing obligation with a requirement and a satisfy
> link, and the relationship between the sensor, the pump's delivery and the alarm.

## T4 — Warehouse AGV fleet

> An automated warehouse runs a fleet of battery-powered automated guided vehicles (AGVs). Each
> AGV docks at a charging station when its state of charge falls below 15% and must not accept a
> new transport job while charging. A fleet controller assigns transport jobs to available AGVs
> and monitors their state of charge. Model the AGV fleet: the AGV, battery, docking station and
> controller structure, the return-to-dock obligation with a requirement and a satisfy link, and
> the job-assignment behaviour or the power connection between battery and dock.

## T5 — Ground-station pass scheduler

> A ground station with one steerable antenna and one S-band transceiver schedules contacts with
> Earth-observation satellites. A contact may only be scheduled inside a satellite's visibility
> window, and the antenna must be pointed before the window opens. The station can support only
> one contact at a time. Model the ground-station scheduling system: the antenna, transceiver and
> satellite structure, the visibility-window obligation with a requirement and a satisfy link,
> and the scheduling activity or the signal connection from antenna to transceiver.

## T6 — Heat pump with buffer tank

> A domestic heat pump charges a buffer tank that supplies an underfloor heating circuit. A
> thermostat reports the indoor temperature. The heat pump must maintain the indoor temperature
> at or above 20 °C whenever the outside temperature is below 15 °C, using the buffer tank to
> avoid short cycling. Model the heating system: the heat pump, buffer tank, thermostat and
> heating circuit structure, the indoor-temperature obligation with a requirement and a satisfy
> link, and the thermal energy flow between heat pump, tank and circuit.

---

## Exact prompts sent, per configuration

Identifier convention for cells: `T<task>-<config>`, e.g. `T3-C2`. Raw outputs are stored at
`research/issue-007/raw/<cell>.md`; the manifest records hashes.

### C1 — single-shot free text

Prompt text = the task paragraph, verbatim, with no other instruction.

### C2 — fenced block demanded

Prompt text = the task paragraph, verbatim, followed by:

> Return the complete SysML v2 model in a single ```sysml fenced code block and nothing else.

### C3 — structured / checklist-guided

Prompt text = the task paragraph, verbatim, followed by:

> Produce one self-contained SysML v2 textual-notation model for this system. Your output must:
> 1. be a single `package` with a name that reflects the system;
> 2. define the system's main parts as part definitions, and include part usages where a whole
>    contains other parts;
> 3. declare at least one `requirement def`, at least one `requirement` usage that states the
>    obligation above, and at least one `satisfy` link connecting a model element to that
>    requirement;
> 4. include at least one behaviour (an `action` or a `state`) OR at least one `connection`
>    between parts — whichever the paragraph asks for;
> 5. give every attribute an explicit type using SysML v2 scalar types where a quantity or text
>    value is meant;
> 6. be a single model in SysML v2 textual notation, with no explanatory prose outside the model.

Note (recorded at authoring time, not after seeing results): item 5 of C3 deliberately mentions
"scalar types" without naming them, so that the configuration is a realistic instruction and not
a disguised correctness hint. Item 4 offers a choice, so that the checklist does not force one
modelling idiom.
