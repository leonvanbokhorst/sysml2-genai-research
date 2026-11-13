# PRE-REGISTRATION — external challenge set (A's frozen observed errors)

**Author:** Researcher B (issue #8 pilot). **Written:** 2026-11-13T14:30–14:35Z. **Frozen:**
2026-11-13T14:35:15Z, **before the first validator run over the frozen subset**. **Frozen by hash before that run**; quoted in `REPORT.md`.
**Task:** `task-6` — run Researcher A's frozen empirical subset through the pinned validator as a
**separate external challenge set**, distinct from my synthetic mutants.

**Why this file exists.** After Gate 2 I wrote that mode-selection is "a degree of freedom that could
be fitted to an outcome" and asked that it be fixed in advance in any future run. This is that
fixing. Every invocation, every attribution rule and every scoring rule below is decided before the
tool runs. If I later want a different mode or rule, it goes in `REPORT.md` as a dated addendum with
the original text visible.

---

## 1. Frozen artefact: identity verified before anything else

I verified every hash myself before writing this file. Verification is recorded in
`run-log.md` §1 and reproduced by `run_external.py --verify-only`.

| artefact | recorded | recomputed | verdict |
|---|---|---|---|
| `subset.json` | `bc2b92a5fdff6e976ae7156b13beba3535f0895e4a41268cf76c1551a6c3dfaa` | same | **OK** |
| `models/manifest.csv` | `a968ff34079a35cdab943dd72415853a4f05617eb353b8deb5665f93ae26b0cb` | same | **OK** |
| 36 files in `models/manifest.csv` (18 normalised + 18 raw) | per-row sha256 + bytes | all 36 match | **OK** |
| frozen copies vs A's live corpus (`research/issue-007/...`) | — | all 36 byte-identical | **OK** |
| `frozen_utc` | `2026-11-13T14:33:20Z` | — | recorded |

No file mismatched, so the run proceeded. The subset contains **no validator-derived field** (I
checked for `detect*`, `diagnos*`, `opensysml`, `validator` keys and prose: the only occurrences are
in the `excluded` list, where they explain why six records were kept *out* — a selection reason, not a
result).

## 2. Ground-truth rule

**`subset.json` is ground truth. I do not relabel, drop, repair or re-score an item because my run
disagrees with it.** If I believe an item is mislabelled, the measurement stands as labelled and the
disagreement is recorded as a **flagged observation** in `REPORT.md` §"Flagged observations for the
adjudicator", with my evidence, for someone else to adjudicate.

**Contested items are measured as labelled and also reported with and without**, per A's instruction:
`ES-T1-C3-E01` (I1) has a live rival reading of its *defect status*; `ES-T4-C1-E02` and
`ES-T4-C3-E01` (R1) are not disputed as defects but their *layer* is contested. Layer contest cannot
change a detection outcome, so R1's contest affects the layer table only. I1's contest affects the
headline rate, so **two rates are pre-registered** for the primary mode: with I1 (`n = 13`) and
without (`n = 12`).

## 3. Registered invocation set (fixed now, four modes)

| id | mode | exact argv | role | applies to |
|---|---|---|---|---|
| **M1** | default validate | `sysml -validate -format json <model>` | **primary**, comparable to the synthetic 23/32 | all 13 items + 4 clean-tier controls |
| **M2** | satisfaction verdict | `sysml -satisfy <model>` | verdict path for the `satisfy` construct family | all 13 items (a model with no satisfy usage returns no verdict ⇒ `not applicable` for that item) |
| **M3** | object verdict | `sysml -instantiate <object> -validate=<object> <model>` | verdict path for assertions about an object | items whose model supplies an instantiable package-level object (rule in §3.1) |
| **M4** | strict notation | `sysml -validate -strict <model>` | secondary; tests Gate-2's exit-code finding | all 13 items |

`<object>` is chosen by a **mechanical rule**, never per item.

### 3.1 Object-selection rule for M3 (mechanical)

> Scan the normalised model top to bottom. Take the **first** line that (a) has **exactly four
> leading spaces** (i.e. a package-level member in these files, not a member of a nested definition),
> (b) matches `^(part|item|occurrence)\s+(?!def\b)([A-Za-z_][A-Za-z0-9_]*)\s*(?::|;|=)`, and (c) is
> not preceded by `ref` or `private`. The captured identifier is `<object>`. If no line matches,
> **M3 is `not applicable` for every item in that model** — recorded as `n/a`, never as `silent`.

I implement this in the harness and let it decide; I do not look at the models and pick. (I *have*
already read 15 of the 18 models during the Gate-2 cross-review, which is disclosed in §7; the rule is
mechanical regardless.)

## 4. Scoring rule (fixed now, per item per mode)

### 4.1 Attribution — the line-range rule (M1, M4)

An item carries a `line_range` from `subset.json` (e.g. `41`, `48-51`, `4,5,9,10,…`). I parse it into
an integer set / inclusive span and use it as the item's location.

| outcome | definition (M1 and M4) |
|---|---|
| **detected** | ≥1 diagnostic with `severity == "error"` whose `line` **falls inside the item's line range** |
| **weaker signal** | no error in range, but ≥1 `warning` in range |
| **wrong-target** | the model produced ≥1 error diagnostic, **none** of them inside the item's line range (the tool reacted to something else — a different defect, or a cascade from another item in the same model) |
| **silent** | the model produced **zero** diagnostics of any severity |
| **not applicable** | the mode cannot address this item at all (see §3.1 and §4.2) |

`wrong-target` matters here in a way it did not for synthetic mutants: some models carry two items
(`T3-C2` has S1 at 23/24/33 and N1 at 44; `T4-C1` has T1 at 42-43 and R1 at 51), so a diagnostic
anywhere is *not* evidence for a specific item. The rule is applied per item.

### 4.2 Verdict modes (M2, M3) — five-valued standing

The verdict path reports a **standing**, not diagnostics. Registered categories:

| standing | meaning |
|---|---|
| `violated` | the instrument evaluated the assertion and it fails — **counts as detected** |
| `holds` | evaluated and true |
| `holds-vacuously` | evaluated as true because the requirement states no required constraint |
| `undecided` | checked and **not decidable** ("not covered", "no value for feature …") — **weaker signal**, not detection |
| `no-assertion` | the model states no assertion of the kind the mode evaluates — **not applicable**, not silence |

**M2 (`-satisfy`)**: record the standing of each satisfaction assertion the model states. For a
**satisfy-family item** (classes `S2`, or an `N1` whose excerpt is a `satisfy … by` line), the item is
`detected` if its own satisfying assertion is reported `violated`. For any other item class, M2 cannot
address the defect and the item is `not applicable` — a `-satisfy` standing is about satisfaction,
not about notation, typing or resolution. Where a satisfy-family item's model states **no** assertion
(`no-assertion`), the item is `not applicable` rather than `silent`.

**M3 (`-instantiate … -validate=` )**: record the standing reported for `<object>`.
`violated` = detected; `undecided` = weaker signal; `holds` / `holds-vacuously` / `no-assertion` =
not detected for that item (the object's assertions do not encode the item's defect). Where the model
declares no instantiable object, `not applicable`.

### 4.3 What "the item's defect" means in the verdict modes

A verdict is about the **object's assertions**, which are a modelling choice, not about the item's
class. So a `violated` standing on an item whose class is `S1` would be a violation *unrelated to the
notation defect* and would be recorded as `wrong-target`, not as detection. This asymmetry is stated
so that the verdict modes cannot inflate the detection rate.

## 5. Controls (false-positive arm)

**Scored:** the four `clean`-tier controls (`T1-C1`, `T2-C3`, `T3-C3`, `T5-C1`) under **M1**
(primary). False-positive measure = controls with ≥1 **error**-severity diagnostic. Warnings reported
separately (they are not errors).

**Not scored:** the three `frozen-clean-only` models (`T5-C3`, `T6-C1`, `T6-C3`). Each carries a
verified post-inspection defect, so a diagnostic on them is **not** a false positive. They are run
anyway (the run is uniform) and their diagnostics are reported **descriptively only**, clearly marked
as not part of the false-positive arm.

**Triage rule** for any diagnostic on a clean-tier control, into exactly one of:
**(i) genuine defect A's coding missed** — the diagnostic names a condition I can substantiate from
the specification or model text; **(ii) validator over-reach / legal-but-flagged** — the construct is
admissible and the tool objects; **(iii) confound** — missing import, library resolution, feature-name
shadowing, or harness artefact. Only (ii) counts as a false positive; (i) changes the control's
status and is reported as such.

## 6. Class mapping — synthetic frame ↔ observed frame (names are NOT identical)

The two frames were coded independently, by different agents, under different codebooks. No class
name may be carried across without a stated mapping, and the mapping is **many-to-many and partial**.

| my synthetic class | A's observed class(es) | mapping quality | rationale |
|---|---|---|---|
| F1 syntax/notation | `S1` | **close** | both are textual-notation violations; but A's S1 is dominated by *reserved-keyword-as-name* (which my F1 never sampled) and my F1 is dominated by *parse breakage* (missing `;`, extra brace), so the sub-mechanisms differ |
| F2 unresolved reference | `N1`, `N2` | **close** | same mechanism at the level of what is wrong; A splits the stdlib-prelude case (N2) out, I do not have it at all |
| F3 kind/type mismatch | `T1` (`T2` is outside this subset) | **partial** | T1 is "definition where a usage is required"; my F3 is "usage typed by a definition of the wrong kind" — adjacent, not identical |
| F4 multiplicity | *(none)* | **absent in observed** | no observed record has a multiplicity defect; A's `R1` was formerly placed here but is now labelled `type/typing`, contested |
| F5 named-constraint violation | `S2` | **partial** | one named `check…` constraint each, different constraints (`validateFeatureValueOverriding` vs `checkSatisfyRequirementUsageBindingConnector`) |
| F6 quantity / unit | *(none)* | **absent in observed** | 0 of A's 18 models write a unit literal |
| F7 structural / architectural | `R1`, `I1` | **weak / contested** | R1 is now labelled `type/typing` by A with `structural/architectural` as the rival layer; I1 is a documentation/value contradiction. Neither is the same condition as any of my four F7 mutants |
| F8 metadata / annotation | *(none)* | **absent in observed** | 0 of A's 18 models contain a metadata annotation |

**Consequence, stated in advance:** per-class comparison is possible for **F1↔S1, F2↔{N1,N2},
F3↔T1, F5↔S2**; it is **not** possible for F4, F6, F7 or F8, because the observed frame contains no
record of those conditions. Any comparison table in `REPORT.md` will show the unmapped classes as
unmapped rather than forcing a correspondence.

## 7. Independence and what I already know (disclosed)

- I have **not** read A's detection results for the purpose of this task and will not use them; A's
  report's detection table is not consulted while the run is designed or scored.
- **Disclosure:** during the Gate-2 cross-review I ran the pinned validator on 15 of these 18 models
  and reproduced some of A's detection claims. My expectations below are therefore **informed, not
  blind**, and their evidential weight is correspondingly low. This is recorded rather than hidden,
  and it is the reason the pre-registration's value here is in the *rules*, not in the predictions.

## 8. Pre-registered expectations (directional, low weight — see §7)

| mode | prediction | basis |
|---|---|---|
| M1 primary, all 13 | **9/13 = 0.69** (with I1); **9/12 = 0.75** (without I1) | S1 3/3, N1 4/4, N2 1/1, T1 1/1 detected; S2 0/1, R1 0/2, I1 0/1 not |
| M2 `-satisfy` | **0/13 `violated`**; the satisfy-family items return `holds` or `holds-vacuously` | Gate-2 probe on `T2-C2` returned `holds (vacuous …)` |
| M3 object verdict | **0/13 `violated`**, some `undecided`, several `n/a` (models with no package-level usage) | no observed model encodes a checkable `require constraint` (0/18) |
| M4 `-strict` | **same detection as M1** for items whose defect is a parse failure; may *add* detection for reserved-keyword items, since `-strict` turns exit 0 into exit 2 — but my criterion is the diagnostic, not the exit code, so M4 is expected to equal M1 | Gate-2 probe P1 |
| controls M1 | **0/4** clean-tier controls with error diagnostics | four short models written by a competent generator |
| contested I1 | no change to any class-level conclusion; the headline moves by at most 1/13 | it is 1 item |

**Registered decision rule for P6/P8** (stated now so the conclusion cannot be fitted):

- **P6** ("validator pass rates measure less than the literature claims") is **supported** if observed
  detection is materially below synthetic detection *for the classes that map*, i.e. the mapped
  classes' observed rate is ≥ 0.15 lower than the synthetic rate.
- **P8** ("the fault model is representative of real generation errors") is **weakened but not
  settled** if the observed set contains classes my fault model does not sample (F4, F6, F7, F8 have
  no observed counterpart) — because that is a statement about *the corpus*, not about generation in
  general; it is **supported** only if the observed class distribution and per-class detection both
  resemble the synthetic frame.
- If the two frames disagree in *direction* (e.g. observed detection higher), the honest outcome is
  "the external set cannot bear the weight", recorded as such.

## 9. Exclusions

- No attempt to re-code, extend or repair A's subset.
- No use of the 24-file external LaVoie corpus (that is A's secondary arm, not my challenge set).
- No new validator, no licence-gated tool, no network retrieval: this run uses the pinned binary
  already in `.tools/` and files already on disk.
- No change to the synthetic corpus, expectations or report numbers; the external set is reported in
  its own section and its own addendum.

## 10. Deliverables (fixed now)

```
research/issue-008/empirical/
  PRE-REGISTRATION.md     this file (+ .sha256)
  run_external.py         harness: verify, run the four modes, write raw + tidy tables
  results.csv             one row per item × mode
  per-item-per-mode.md    the readable matrix
  raw/**                  unedited validator output per item per mode
  run-log.md              verification, tool identity, argv, timestamps, exit codes
  REPORT.md               findings, comparisons, controls, flagged observations, what changed
```

## 11. Amendments

None at freeze. A later amendment is appended here with UTC date, reason, superseded text quoted, and
is reported in `REPORT.md`.

*Pre-freeze correction, 2026-11-13T14:35Z:* the first draft's header carried a forward-dated
"written" time (14:52Z) taken from a shell clock before the file was finished. It was corrected to
the actual writing window and freeze time **before the file was hashed and before any run**, and both
hashes are recorded in `run-log.md` §2. No rule, mode, expectation or scoring definition was changed.

---

## 11. Amendment AM1 — 2026-11-13T14:39Z — three derivation fixes, made after a first run and before any result was scored

**What happened.** The first execution of `run_external.py` (`raw/run1/`) completed, and its output
revealed three defects **in my harness, not in the instrument**:

1. **M4 was parsed as JSON but invoked as text.** The registered argv `-validate -strict <model>`
   prints text; the harness tried `json.loads` on it, got nothing, and recorded `silent` for every
   item. Fixed by adding `-format json` to M4's argv — a *serialization* change, not a mode change.
2. **A verdict mode recorded "not detected" where no verdict was possible.** When a model does not
   analyse cleanly (error diagnostics from M1), `-satisfy`/`-instantiate` cannot form a standing and
   print the resolution errors instead. That was being scored `not detected`, which overstates
   silence. Fixed: such items are `not applicable — model does not analyse cleanly`.
3. **Controls were labelled with the item-attribution vocabulary.** A control has no item location,
   so "wrong-target" is meaningless for it. Fixed: controls are labelled `clean model`,
   `diagnostic (warning only)` or `diagnostic (error)`.

**Nothing else changed.** No mode was added or removed; no attribution rule (§4.1), no standing
mapping (§4.2), no expectation (§8) and no class mapping (§6) was altered. The two changes to
outcomes move items from `not detected` to `not applicable`, i.e. they *reduce* what can be claimed,
and neither touches a detection count.

**What run1 is.** Preserved unedited in `raw/run1/` and reported here as superseded by `raw/run2/`.
The reported numbers come from run2. I diffs M1/M2/M3 outcomes between the runs and report any
difference in `run-log.md` §6; if any M1/M2/M3 outcome had changed, that would be a bug I did not
intend and would be reported rather than smoothed.
