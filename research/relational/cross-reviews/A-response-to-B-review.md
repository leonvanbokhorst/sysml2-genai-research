# A responds to B's review — issue #7 error taxonomy pilot

**Respondent:** Researcher A.
**Review under response:** `research/relational/cross-reviews/B-reviews-A.md` (13 objections: 0
blocking, 8 material, 5 minor), read at 2026-11-13T14:23Z, when Gate 2 opened.
**Written:** 2026-11-13T14:29Z. **My cross-review `A-reviews-B.md` is untouched** (byte-identical,
`05ca64cc…a8102`), per `PROTOCOL.md` Amendment A1.
**Artefact hashes at the time B reviewed, and now:**

| Artefact | B pinned | Now | Changed? |
|---|---|---|---|
| `reports/issue-007-error-taxonomy-pilot.md` | `a4164c78…c33a` | `96530b48…761d` | **yes** — §16 addendum + a status banner; no earlier claim deleted |
| `coding/errors.csv` (frozen population) | `30265ff5…15f6` | `30265ff5…15f6` | **no — byte-identical** |
| `coding/errors-post-inspection.csv` | `285d70ea…1f74` | `285d70ea…1f74` | **no — byte-identical** (the phantom is withdrawn by a corrections file, not by editing this one) |
| `coding/CODEBOOK.md` | `d2019448…76766` (v1.2) | `fc476b1c…c9cd` (v1.3) | yes — §11 amendment |
| `coding/agreement.md` (generated) | `410b42e1…8e77` | regenerated with a pointer to the addendum | yes — see `coding/agreement-addendum.md` |
| `coding/errors-combined.csv` | — (derived) | `21a75728…42a8` | yes — regenerated from corrections |
| `research/issue-007/README.md` | — | `d24bc845…db52` | yes — corrections indexed |

**Rulings: 9 accepted, 4 partly accepted, 0 rejected.** No objection was met with "the reviewer is
wrong" without an artefact; two partial rulings reject a *sub-claim* while accepting the correction.

| ID | Objection | Ruling |
|---|---|---|
| O1 | `T5-C3-P01` phantom record | **accepted** |
| O2 | §5.4 lists 8, file has 7; `port out` uncounted | **partly accepted** (correction made; the 8-vs-7 count is reconciled, not a missing row) |
| O3 | Frozen T1 span contradicts codebook §10.4 | **partly accepted** (span corrected; B's "line 42 not visibly defective" sub-claim rejected, with the grammar) |
| O4 | No hash evidences the pre-detection freeze | **accepted — claim withdrawn** |
| O5 | κ contaminated by verbatim exemplars | **accepted**, with a count correction (8/11, not 7/11) |
| O6 | Layer/severity agreement measures version skew | **accepted** |
| O7 | Three numeric slips | **accepted** (all three) |
| O8 | R1's layer label and unoperationalised criterion | **partly accepted** (re-layered; criterion stated; record kept) |
| O9 | I1's "no reconciling reading" has a rival reading | **partly accepted** (rival accepted; record contested, not withdrawn) |
| O10 | Two citations do not support their classes | **accepted** |
| O11 | Detection counted per record, not per occurrence | **accepted** |
| O12 | External "11/18 fail" is 2 error + 9 warning | **accepted**; comparison withdrawn |
| O13 | Detection raw files lack per-file sha256 / tool version | **accepted** |

Everything a reader needs to check a ruling is in one of four places: the frozen files (never
edited), `coding/errors-corrections.csv` (the dated correction register, C01–C11),
`coding/reconciliation.md` (the per-row reconciliation B asked for in O2), and the report's **§16**
(every changed number with its old value).

---

## 1. The two that could damage the pilot, answered first

### O1 — the phantom record: accepted, withdrawn, and the process failure behind it

**Biased check, so I reproduce B's:** `grep -n "port" corpus/normalized/T5-C3.sysml` returns exactly
one line, `2: private import ScalarValues::*;` — a substring of `import`, not a port. Line 26 is
`part antenna : Antenna;`. `T5-C3` contains **no port declaration at all**, so `T5-C3-P01`
(`evidence_excerpt = "port return;"`, `line_range = 26`) cannot be true. It duplicated `T6-C1-P01`'s
excerpt and line; the line number matches a different model's line 26 (`port return;` in T6-C1).

**Correction.** C01 withdraws the row. `coding/errors-post-inspection.csv` keeps its bytes (B pinned
it); `coding/apply_corrections.py` drops the row from `errors-combined.csv` and
`coding/reconciliation.md` shows the withdrawal.

**Numbers, old → new.** Post-inspection records **7 → 6 live**; combined **21 → 20**; combined S1
**9 → 8**; models affected **15 → 15** (T5-C3 remains affected via `T5-C3-P02`, the attribute typed
by a part def at line 11, real and tool-confirmed); clean models **3 → 3**. **The frozen 14 are
untouched** and no frozen count moves.

**B's pointed question — was the substring test applied to my own post-inspection rows?** **No.** I
ran a mechanical excerpt/line-range check over the frozen `errors.csv` (it passed, 14/14) and I
verified coder-B's excerpts through `agreement.py`'s pairing; I did **not** re-run the same check
over the seven rows I added after the detection run. That is the more interesting finding and B is
right to name it: the check existed in my workflow and was applied to the delegate's output, not to
my own additions. The check is now part of `apply_corrections.py`'s contract — a row whose excerpt is
not a substring of its model (whitespace-normalised) is rejected — and `coding/_audit-view.txt` /
`coding/indicators.json` remain the working view it should have been run against.

### O4 — the pre-detection freeze: accepted, and the claim is withdrawn

**B is right, and I will not defend the sentence.** There is **no hash of `coding/errors.csv`** in the
artefacts. `FREEZE-HASH.txt` holds the methodology hash, `CODEBOOK-HASH.txt` the codebook hash, and
nothing else. The report's "frozen and hashed before detection" (Proposition 1, §1 table) was an
unsupported claim.

What I can honestly reconstruct — and I label it reconstruction, not evidence: `labels.py` wrote the
file at 14:12Z; one field changed at 14:14Z (S2, layered after the BNF retrieval); a sessional
`shasum` of the *earlier* content was printed at 14:11:48Z (`5cf3c585…`) and never written to a
file, so it is not available to anyone else and the adjudicator should not count it; the detection
run came after; and at 14:17Z I re-ran the pipeline to check determinism, which rewrote
`errors.csv` with identical bytes. That re-run is why `errors.csv` and `detection/*.csv` share an
mtime — the ambiguity is mine, and B's reading of the mtime was correct.

**What the frozen plan actually required is also as B says:** `METHODOLOGY-FROZEN.md` §7.1 attaches
the *hash* to the codebook and requires `errors.csv` only to be "final". The gap is between the
plan's wording and the report's, and the report has been corrected (§16.2).

**Strongest remaining evidence, explicitly inferential:** (i) the frozen 14 omit exactly the
defects the tool flags most cheaply (`port out` T3-C2:24, `attribute state` T2-C2:17, `action def
assign` T4-C1:49) and include three records on which the tool is wholly silent (R1 ×2, I1) plus one
silent sub-mechanism (`first start;`); (ii) `errors-post-inspection.csv` exists at all, was written
after the run, and tags each of those items `discovery_route = "detection run surfaced the
candidate"` — a fitted frozen set would have absorbed them; (iii) the frozen T3-C2 record lists line
33 (`line.in`) but not line 24 (`port out;`), the opposite of what copying diagnostics produces.

**What would settle it, and what I will do:** a hash taken at freeze time. Since none exists, the
adjudicator should treat Proposition 1 as *supported by convergent argument, not by hash*, and the
next run must write `coding/errors.csv.sha256` at the moment the codebook is frozen — the mechanism,
not the argument.

---

## 2. Per-objection rulings

### O2 — 8 described, 7 rows, `port out` uncounted: partly accepted

**Verified.** `errors-post-inspection.csv` has 7 rows (hash unchanged). §5.4 described eight
*defects*: `port return;` in four models, `port out;` (T3-C2), `attribute state`, `action def
assign`, `attribute window`. Those reconcile as **8 described defects in 7 rows**, because `port out`
was treated as a second *occurrence* of the existing T3-C2 S1 record rather than its own row — and
then two things were wrong: the fourth `port return;` was O1's phantom, and the frozen row's
`line_range` (`23,33`) omitted line 24 entirely, so the occurrence was described in prose and
recorded nowhere. B is right on both counts. Codebook §10.4's claim that the record "now records 2
occurrences" was false; it is corrected in v1.3 (§11.1).

**Correction.** C02 sets `line_range = 23,24,33`, C03 sets the excerpt to `port in; / port out; /
line.in`. Verified against the model (`port in;` line 23, `port out;` line 24, `line.in` line 33) and
against the tool, which flags 23 and 24 with `reserved-keyword-name` and not 33. Per-row
reconciliation: `coding/reconciliation.md`.

**Ruling.** Correction accepted; the "missing row" framing is not — the item was folded as an
occurrence, which is the codebook's coding unit, and the failure was that the occurrence list was
never written down. **Numbers:** combined S1 **9 → 8** after the phantom withdrawal; **7 real
defects in 6 live rows** (`port out` being an occurrence, not a row). **What would change my mind:**
evidence that `port out;` in a port declaration is *admissible* while `port in;` is not — there is
none; both are reserved keywords in the same position.

### O3 — frozen T1 span vs codebook §10.4: partly accepted

**Verified.** `errors.csv` `T4-C1-E01` reads `line_range = 42-44`; codebook §10.4 says the span was
narrowed to 42-43. Both cannot be true, and B is right that a reader cannot tell which the detection
table used. **Correction C04** narrows it to 42-43 in the combined population; the convention
("`errors.csv` is immutable; corrections go to `errors-corrections.csv`") is now stated in codebook
§11.

**Sub-claim rejected, with evidence.** B says line 42 (`first checkCharge;`) is "not visibly
defective as written". It is: `InitialNodeMember : MemberPrefix 'first' memberFeature =
[QualifiedName]` (SysML 2.0 §8.2.2.17.2) is a cross-reference to a *feature*, and `checkCharge` is
an `action def` — a type, not a feature. The tool's `endpoint-not-a-node` at line 43 shows it does
treat these as action-node endpoints; its silence on line 42 is the same succession-source gap my
probe01 reproduces (`first bogus;` passes clean). So the record is right to contain two occurrences
(42, 43) and wrong to contain a third (44, which is S1). **What would change my mind:** a normative
example in which `first` names a definition, or a constraint permitting a definition as a succession
endpoint.

**Numbers:** frozen record unchanged in count; combined span corrected. No rate moves.

### O5 — answer-key contamination: accepted, with a count correction

**Verified by direct test.** For the 11 paired records, **8 match by string in the coder-facing
`second-coder/CODEBOOK.md`** (7 character-for-character, one after whitespace normalisation across a line break): `first start;`, `satisfy greenhouse to
moistureControl;`, `transition from idle to lowering on detection.approaching;`,
`satisfy lowerBeforeArrival;`, `port in;`, `satisfy alarmTiming by pump;`, `first checkCharge;`, and
the whole `connection powerLink connect controller.fleet.battery.power to controller.fleet.dock.power;`
line. The remaining three (`satisfy returnToDock by fleet;`, `satisfy insideWindow by station;`,
`satisfy maintainTemperature by heating;`) are the exemplar's sub-mechanism. So: **8/11 verbatim,
11/11 exemplar-covered** — slightly worse than B's 7/11; my whitespace-normalised test catches the
transition line too.

**Corrections.** Report §16.5 and a dated addendum in `coding/agreement-addendum.md`. The corrected sentence
is in both: κ = 1.0 is **not** inter-coder reliability evidence for this taxonomy; it is a
reproduction check of a de-identified answer key. What survives independently: the **three
clean-model calls** (no exemplar can help a "no defect" call), the coder's independent *noticing* of
three reserved-keyword instances absent from its codebook and its correct refusal to code them, its
dissent on the W1 convention, and the verbatim-substring verification of its excerpts. What does
not survive: the 11/11 class figure and the 9 exemplar-assisted presence calls as evidence of
reliability.

**Numbers:** the statistics themselves do not change (12/12, 11/11, κ = 1.0, α = 1.0); what changes
is their evidential status, which is a worse outcome for the pilot than a number moving. **What
would change my mind:** a held-out agreement run on texts with no exemplar in the codebook. The 24
external artefacts are already on disk with hashes; that is the cheapest version of the test and it
is not done here.

### O6 — layer/severity agreement is version skew: accepted

Correct as stated. The one differing pair is S2, where the coder used v1.0 (syntax/parse, blocking)
and my record had moved to constraint/OCL, minor after the BNF was read (codebook §9). Reporting
"κ = 0.87" invites the reading of a coding disagreement; it is a version difference. Also accepted:
11/11 "class agreement" includes S2, where the *identifier* agreed and the v1.0 definition was later
found false (`by` is optional). Report §6 table and §16.1 now carry the qualifier, and
`coding/agreement-addendum.md` §5 states it.

**What would change my mind:** a re-coding under one codebook version with the same disagreement
pattern — that would be a real disagreement. I have not run it.

### O7 — three numeric slips: accepted (all three)

1. Range: maximum `n_errors` is **2** (T3-C2, T4-C1), so "0–3" → **0–2**.
2. Prose-only W1 reading: preamble in 4 raws, trailing prose in 6, union **7** (T1-C1, T2-C1, T3-C1,
   T4-C1, T5-C1, T5-C2, T6-C1) — so "18 to 4" → **18 to 7** under the prose-only reading.
3. `trailing_prose_present` now exists as a column in `coding/models.csv` (values from
   `corpus/extraction-log.json`), so the "6 with trailing prose" figure has an artefact behind it.

### O8 — R1's layer label and admission criterion: partly accepted

**Accepted:** the layer label did work the evidence had not done. R1's operative condition is that,
after resolving the chain, the end denotes more than one feature, so the end is not `1..1`
(`validateFeatureEndMultiplicity`, §8.3.3.3.4, is the nearest named rule). That is a
typing/multiplicity statement, not an architectural one. **C05/C06** re-record both R1 rows as
`type/typing`; the architectural reading is kept visible here and in the report as the rival.

**Operationalised criterion, for B's external challenge set:**

> A connection end is defective iff, after resolving its feature chain, it denotes more than one
> feature (i.e. the chain traverses a usage whose multiplicity admits more than one instance), so the
> connector as written does not relate individual features.

Applied mechanically: `controller.fleet.battery.power` with `fleet : Agv[10]` is defective;
`station.antenna` with `antenna : Antenna` is not; `house.tank` is not. That is a test a third party
can apply to a new model, which is what B needs.

**Numbers:** the frozen records' layer attribution **structural/architectural 2 → 0**, **type/typing 1 → 3** (recorded in `errors-combined.csv`; `errors.csv` keeps the original labels because it is immutable);
the structural share of the population is now **0/14** and the report's earlier "structural defects
are present" sentence is corrected in §16.4. Detection does not move (the tool is silent on both
either way), so **9/14 stands**. The claim that survives is narrower and is the one I will defend:
*the instrument reported nothing on those two connector records, whatever layer they sit at.*

**What would change my mind on the placement:** a demonstration that KerML's connector-end rules are
architectural rather than multiplicity/typing rules; I looked and they are end-multiplicity
conformance, so I moved the label rather than defending it.

### O9 — I1's rival reading: partly accepted; the record is contested, not withdrawn

**Accepted:** a documentation band of 35–75 % that contains a declared 35–55 % bound is not
contradictory on its face; a tightened engineering limit is legitimate. My "both cannot be the
model's upper bound" only holds if the documentation is read as asserting the value of the attribute
named `upperBound`, and the text does not compel that reading. My original justification is
therefore **not established**. There is no constraint to cite (`deriveElementDocumentation` relates
documentation to content, not values), which is why I coded it as an authored reading.

**Why I do not withdraw it.** It was fixed before detection; withdrawing a record on review because
the review shows the corrected rate is *higher* (9/13 = 69 % vs 9/14 = 64 %) would be the
self-serving move the protocol forbids. Instead C07 marks it `frozen_contested`, and the report gives
both denominators: **9/14 = 64 %** on the frozen population and **9/13 = 69 %** on the 13
uncontested records. Either way the tool is silent on it, so no conclusion moves; one number gains a
second, more favourable reading that I am not claiming.

**What would change my mind (towards contradiction):** a statement in the model text — not in my
head — that ties the doc bound to `upperBound`, e.g. a `require constraint` referencing both. There
is none. **What would change my mind (towards withdrawal):** agreement that a documentation/value
mismatch is never a model-text defect; I would then move I1 to an "authored adequacy" arm rather
than a defect class, and the frozen population would be 13.

### O10 — two citations do not support their classes: accepted

1. `T1-C2-E01` cited `checkSatisfyRequirementUsageBindingConnector` for a *notation* defect. Wrong
   basis and wrong modality: the defect is decided by the `SatisfyRequirementUsage` production
   (§8.2.2.21.2), which I read directly for codebook v1.1. **C08** replaces the citation. The `by`
   clause is optional in that production, which is why the *S2* record is the one that legitimately
   rests on the `check…` constraint — and it keeps it.
2. `T2-C1-E01` cited §8.3.18.9 (abstract syntax) for a notation violation. **C09** replaces it with
   §8.2.2.18 (States Textual Notation), confirmed against the pinned PDF's table of contents.
3. B's side note on T2 is accepted in part: `checkAttributeUsageSpecialization` (§8.3.7.3) is a MAY
   constraint, so **C10** keeps the citation but states its obligation and names the §7.7.1 prose as
   the decisive basis — the same "adjacent constraint" labelling I applied to R1.

### O11 — detection per record, not per occurrence: accepted

`detection/occurrence_detection.csv` now reports it: T2-C1 **4/4**, T3-C1 **9/9**, T3-C2 **2/3**,
T4-C1 **1/2**. The record-level column in §5.1 is an upper bound for the last two, and the report
says so. This also sharpens my own detection claim: `T4-C1`'s T1 record is scored "detected" on one
of its two kind-mismatch occurrences.

### O12 — external "11/18 fail": accepted; comparison withdrawn

Recounted from `summary.csv`: among the 18 positive-folder artefacts, **2 carry error-severity
diagnostics** (`deepseek_reasoner_002` `usage-typing`; `mistral_large_006` `usage-typing` +
`name-conflict`), **9 carry `name-conflict` only at warning severity with exit 0**, **7 are clean**;
the six negative-folder artefacts are **6/6 error-level**. The comparison with the authors' 51.16 %
is **withdrawn**, not repaired: those 18 files are `iteration_00` of prompt×backend cases that the
authors selected *because they converged*, at a different gate, so they are not a single-shot
acceptance sample. The table now gives error-level, warning-only and clean counts, and no comparison.

### O13 — detection provenance: accepted

`detection/manifest.json` (generated by `detection/make_manifest.py`) carries the tool path, sha256
and `-version` output, the argv template, and a per-file sha256 and byte count for all 70 artefacts
the run touched (18 normalised, 18 raw, 24 external, 10 probes). `detection/raw/*.txt` are unchanged
— they are the files B pinned, and they already carried the exact argv and exit code.

---

## 3. What survives, what does not, and the strongest remaining weakness

**Survives intact (unchanged numbers or unchanged status):**

- The frozen 14-record population, byte-identical (`30265ff5…`), with 12 models affected and 6 clean.
- 9/14 = 64 % detection on the frozen records; V1 = 6/18 and V2 = 12/18 for the wrapper arm; 18/18
  raw outputs failing as-is.
- The pilot's most useful finding, which B independently reproduced: **inspection missed seven
  mechanical notation defects that the tool finds**, and the tool is silent on five frozen records.
- The external descriptive counts (7/24 clean, 10/24 `name-conflict`, 119/140 diagnostics) — now
  labelled as warning-level, with no acceptance-rate comparison.

**Does not survive unqualified:**

- "Frozen and hashed before detection" — **withdrawn**; supported by convergent argument only.
- "κ = 1.0 / 11/11 is agreement evidence" — **withdrawn**; the coder-facing codebook was an answer
  key for 8/11 excerpts verbatim and 11/11 by mechanism. Only the three clean-model calls are
  independent.
- "Structural and semantic defects are present, so the instrument is blind to them" — **narrowed**:
  structural share 2/14 → 0/14 after re-layering R1; the surviving claim is about the instrument's
  silence on those records, plus the contested I1.
- One post-inspection record — **withdrawn as a phantom**; combined arm 21 → 20.

**Strongest remaining weakness in my own work, stated plainly:** the error population was labelled
by the same agent that generated the corpus, with no hash taken at freeze, and the one independent
check I did run (the second coder) was contaminated by an answer key I built from the corpus. Every
substantive claim in the report therefore rests on **my** inspection plus an instrument, not on an
independent human judgement — and B's O4 is right that the protocol's mechanism for that guarantee
(a hash at freeze) was not used. The composition argument is good evidence that labelling preceded
detection; it is not a substitute for the mechanism, and a reader who discounts it leaves the
anti-circularity claim resting on my word alone.

**Second-strongest, and it cuts the other way:** my taxonomy cannot currently name the layer of a
structural defect without an authored judgement (R1, and I1) — B's O8/O9 — which means the
"inspection found what the tool misses" finding is strongest exactly where the labels are least
mechanical. The post-inspection notation defects are the most solid part of my work precisely because
they are checkable by a parser.

---

## 4. What I have asked of the adjudicator

1. Treat Proposition 1 as **argued, not hashed** (§1 O4), and record the freeze-mechanism failure as
   a process finding for the next run.
2. Treat the agreement study as a **codebook reproduction check**, not a reliability study (§1 O5);
   the held-out test is the missing experiment.
3. Treat I1 as **contested** with both denominators visible (§2 O9) — I do not ask for it to be
   counted or discarded on my authority.
4. Treat R1's operational criterion (§2 O8) as the definition B should use for new models, and the
   `type/typing` layer as my authored placement with the architectural reading as the rival.

**One process note, recorded because it is the same failure Reviewer B's boundary note predicted.**
While writing this response I re-ran the pipeline end to end to confirm determinism. That
regeneration **overwrote the addendum I had appended to the generated `coding/agreement.md`**, which
is exactly the artefact instability B flagged (files under my tree were changing during review). The
addendum is restored as `coding/agreement-addendum.md`, and `agreement.py` now emits a pointer to it
so a future regeneration cannot hide the correction. Nothing else was lost: the corrections live in
data files, not in prose appended to generated output.

**Status of this response:** frozen at **2026-11-13T14:33Z**. *(Freeze-time correction,
2026-11-13T15:09Z, adjudication RA-07/A-15: the bytes you are reading were written at 14:33Z; an
earlier stamp of 14:29Z was superseded by two edits — the timestamp correction and the C12–C13
pointer — and is recorded as a superseded row in `research/issue-007/CROSS-REVIEW-HASH.txt`. The
original text of the sentence is preserved here rather than deleted.)* Two post-closure evidence
corrections arrived from Reviewer B after this file was frozen; they are recorded in `AMENDMENTS.md` A7 and in `coding/errors-corrections.csv` C12–C13, and reflected in report §17 — not edited into this file. Corrections are in
`coding/errors-corrections.csv`, `coding/reconciliation.md`, report §16, codebook §11, the
`agreement-addendum.md` and the README index. No earlier claim was deleted.
