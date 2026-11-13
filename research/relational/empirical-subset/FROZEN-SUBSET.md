# FROZEN SUBSET — A's empirical SysML v2 errors, for B's external challenge set

**Frozen at (UTC):** 2026-11-13T14:33:20Z
**subset.json sha256:** `bc2b92a5fdff6e976ae7156b13beba3535f0895e4a41268cf76c1551a6c3dfaa`
**models/manifest.csv sha256:** `a968ff34079a35cdab943dd72415853a4f05617eb353b8deb5665f93ae26b0cb`
**Owner:** Researcher A (issue #7 pilot). **Consumer:** Researcher B (issue #8), as the *external*
challenge set — separate from B's synthetic mutants.

> **ADDENDUM (2026-11-13T15:14Z, Gate-4 adjudication A-6/A-11/A-21): read this with
> [`FROZEN-SUBSET-ADDENDUM.md`](FROZEN-SUBSET-ADDENDUM.md).** Two R1 items (`ES-T4-C1-E02`, `ES-T4-C3-E01`)
> are contested **as to defect status**, not only as to layer; the item set is therefore 10 unqualified
> + 3 contested, and B's primary denominator is 10. The summary line below said "7 controls"; the correct
> reading is **4 controls + 3 descriptive models**. `subset.json` is unchanged (B's run is pinned to it).

## What this is

13 error items from the corrected frozen error population of A's 18-model corpus, plus
7 control models. Each item is one defect mechanism, with the verbatim model excerpt,
the line range, the class and layer A assigned, the specification or model-text basis, A's
confidence, and its corroboration status. The normalised model and the raw output are copied into
`models/` and `raws/` and hashed in `models/manifest.csv`, so this is a frozen artefact: B runs the
files here, not the live corpus.

## Selection rule (stated before freezing)

> Include every record from the frozen population that **survived the corrections**: supported by a
> verbatim excerpt in its own model, with a citable basis, and not withdrawn. Include contested
> records and mark them contested with the rival reading named. Exclude withdrawn records and any
> record whose discovery was instrument-surfaced without independent verification. Add the models
> with no coded defect as controls, in two tiers, clearly labelled.

The rule produced: **13 error items** (10 unqualified, 3 contested), **0 withdrawn**, **4 controls +
3 descriptive models** (the original line said "7 controls"; relabelled 2026-11-13T15:14Z, A-11/A-21 —
the three `frozen-clean-only` models are not controls), across all 18 models. No item was selected for its detection
outcome; this file contains **no detection results and no validator-derived fields** (rule 1 of the
freeze instruction). A's detection results stay in A's own report; B must measure independently.

## Items

| item_id | model | class | layer | contested | confidence | excerpt | lines |
|---|---|---|---|---|---|---|---|
| ES-T1-C2-E01 | T1-C2 | S1 | syntax/parse | no | high | `satisfy greenhouse to moistureControl;` | 41 |
| ES-T1-C3-E01 | T1-C3 | I1 | semantic/behavioural | yes (defect status) | low | `doc /* Soil moisture shall be kept between 35% and 75% ...` | 37-39 |
| ES-T2-C1-E01 | T2-C1 | S1 | syntax/parse | no | high | `transition from idle to lowering on detection.approaching;` | 48-51 |
| ES-T2-C2-E01 | T2-C2 | S2 | constraint/OCL | no | medium | `satisfy lowerBeforeArrival;` | 33 |
| ES-T3-C1-E01 | T3-C1 | N2 | name resolution | no | high | `attribute innerDiameter : Real;` | 4,5,9,10,14,15,19,20,32 |
| ES-T3-C2-E01 | T3-C2 | S1 | syntax/parse | no | high | `port in; / port out; / line.in` | 23,24,33 |
| ES-T3-C2-E02 | T3-C2 | N1 | name resolution | no | high | `satisfy alarmTiming by pump;` | 44 |
| ES-T4-C1-E01 | T4-C1 | T1 | type/typing | no | medium | `first checkCharge; / then checkAvailability; / then assign` | 42-43 |
| ES-T4-C1-E02 | T4-C1 | R1 | type/typing | yes (layer) | medium | `connection powerLink connect controller.fleet.battery.powe` | 51 |
| ES-T4-C2-E01 | T4-C2 | N1 | name resolution | no | high | `satisfy returnToDock by fleet;` | 32 |
| ES-T4-C3-E01 | T4-C3 | R1 | type/typing | yes (layer) | medium | `connection batteryToDock connect fleet.vehicles.battery.po` | 56 |
| ES-T5-C2-E01 | T5-C2 | N1 | name resolution | no | high | `satisfy insideWindow by station;` | 32 |
| ES-T6-C2-E01 | T6-C2 | N1 | name resolution | no | high | `satisfy maintainTemperature by heating;` | 40 |

| control_id | model | tier | second coder covered | note |
|---|---|---|---|---|
| CTRL-T1-C1 | T1-C1 | clean | yes | No coded defect in any population after C12 (the 'first start;' record was withdrawn: Acti |
| CTRL-T2-C3 | T2-C3 | clean | no | No coded defect in any population. |
| CTRL-T3-C3 | T3-C3 | clean | yes | No coded defect in any population; imports SI without writing a unit literal. |
| CTRL-T5-C1 | T5-C1 | clean | yes | No coded defect in any population; imports SI without writing a unit literal. |
| CTRL-T5-C3 | T5-C3 | frozen-clean-only | no | NOT A CONTROL: carries a verified post-inspection defect (attribute window : VisibilityWin |
| CTRL-T6-C1 | T6-C1 | frozen-clean-only | no | NOT A CONTROL: carries a verified post-inspection defect (port return; line 26, reserved k |
| CTRL-T6-C3 | T6-C3 | frozen-clean-only | yes | NOT A CONTROL: carries a verified post-inspection defect (port return; line 26). A diagnos |


## Per-item notes that matter for B's measurement

- **Contested records.** `T1-C3-E01` (I1) has a live rival reading (a tightened limit is not a
  contradiction); report the rate with and without it. `T4-C1-E02` and `T4-C3-E01` (R1) are not
  disputed as defects, but their *layer* is contested between `type/typing` (recorded) and
  `structural/architectural` (rival).
- **R1's operational criterion** (so a new model can be judged without asking me): *a connection end
  is defective iff, after resolving its feature chain, it denotes more than one feature.*
- **Corroboration.** 10 of the 13 items sit in models the second coder also coded, but its
  corroboration is weak: the coder-facing codebook contained those excerpts verbatim or their
  exemplars (`research/issue-007/coding/agreement-addendum.md`). 3 items (`T1-C3-E01`, `T3-C1-E01`,
  `T4-C3-E01`) have **no** independent corroboration. No item is corroborated by the external corpus.
- **Confidence** is A's own: 8 high, 4 medium, 1 low (the contested I1).

## Controls — read the tiers before using them as a false-positive arm

- **`clean` tier (4 models: T1-C1, T2-C3, T3-C3, T5-C1):** no coded defect in any population. They
  are *clean as far as A's coding goes* — **not** known-good by construction and **not**
  independently certified. A false-positive rate computed on four short models is a falsification of
  a gross over-reach, not an estimate.
- **`frozen-clean-only` tier (3 models: T5-C3, T6-C1, T6-C3):** clean in the *frozen* population but
  each carries a **verified post-inspection defect** (a reserved keyword used as a name; an attribute
  typed by a part definition). **Do not use these as controls**: a diagnostic on them is not a false
  positive. They are included so the record is complete, not so they can be scored.

## What this subset is NOT

1. **Not a representative sample of generation errors.** 13 records from 18 models, one generator
   family, six prompts authored by the same agent that coded the models. Any rate computed on it is
   a property of this corpus.
2. **Not independently labelled.** The generator, coder and selector are the same agent. The second
   coder's agreement is weak evidence (see above), and there is no human expert.
3. **Not a validator's fault model, and not validator-derived.** Nothing here was chosen because a
   tool caught it or missed it. The six records *excluded* for that reason are listed in
   `subset.json` under `excluded`.
4. **Not a benchmark.** It is a challenge set for one instrument on one corpus, with a stated
   criterion per item.
5. **Not stable against further evidence.** Two records from the original 14 have already left the
   population on evidence (a phantom excerpt; a legal construct). If an item is shown wrong, the
   honest outcome is a dated correction and a new frozen hash, not an edit here.

## Provenance

- Frozen population: `research/issue-007/coding/errors.csv` (sha256 `30265ff5…15f6`, untouched),
  corrected by `research/issue-007/coding/errors-corrections.csv` (C01–C12) into
  `errors-combined.csv`; corrections documented in report §16–§17 and `AMENDMENTS.md` A6–A7.
- Codebook: `research/issue-007/coding/CODEBOOK.md` v1.3 (`fc476b1c…c9cd`).
- Model files: `models/` and `raws/` copies, hashed in `models/manifest.csv`.
- Post-inspection verification basis: SysML 2.0 §8.2.2.1.2 (reserved keywords), §7.7.1 (attribute
  typing), and the normative `Actions.sysml` library for the C12 withdrawal.

## Freeze record

`FROZEN-SUBSET-HASH.txt` contains both hashes and the UTC freeze time. B should verify them before
running, and should not regenerate `subset.json` (that would change the hash).
