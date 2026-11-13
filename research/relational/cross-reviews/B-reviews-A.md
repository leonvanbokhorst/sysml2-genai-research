# Researcher B reviews Researcher A — issue #7 error taxonomy pilot

**Reviewer:** Researcher B (issue #8 pilot: mutation-based validator evaluation).
**Subject:** `reports/issue-007-error-taxonomy-pilot.md` and the artefacts under
`research/issue-007/` (`coding/`, `corpus/`, `detection/`).
**Written:** 2026-11-13, after Gate 1 closed. **Independence:** I formed this review without
seeing `research/relational/cross-reviews/A-reviews-B.md` (it does not exist at the time of
writing), and I have not discussed A's findings with A or with the Lead. My own frozen
methodology (`2c80d63e…`, 14:08Z) and mutant expectations (`a9f47974…`) were fixed before I read
any of A's work; nothing below revises them.
**Method:** I re-derived A's numbers from the raw artefacts rather than reading the report's
tables, re-ran the pinned validator myself on the seven models that carry the contested records,
and wrote throwaway scripts (in `/tmp`, not committed) to test each claim. Where I could not
settle something, I say so. **I have not edited any of A's artefacts; this file is my only write.**

**Artefacts pinned to the bytes I reviewed** (sha256, so A and the adjudicator know exactly what
was reviewed and what changed afterwards):

| artefact | sha256 |
|---|---|
| `reports/issue-007-error-taxonomy-pilot.md` | `a4164c787f40e7a4ef36eaf009cda9ea6ded9b08dd7cb1bc91182a24bc62c33a` |
| `research/issue-007/METHODOLOGY-FROZEN.md` | `269d8dbe7228db83d20ca2be39991172f20fd23458ac1e5e6755ff7269564f76` |
| `research/issue-007/AMENDMENTS.md` | `b6ea551af2a051a3afc38e77aeac0e9e763ceb208dd8a91fae3d23f87d60110b` |
| `coding/CODEBOOK.md` | `d2019448c6840ced7b1aab077c40fbdf5afd89747426370ca80007b07ff76766` |
| `coding/errors.csv` | `30265ff57bdd1f4036304c6acbc1026678d36f0b3604c925a7b538455fc815f6` |
| `coding/errors-post-inspection.csv` | `285d70ea816eb3d73da9a954faba5f54d05292103da3c740abb9763da7851f74` |
| `coding/models.csv` | `87aa3e7d255fd657d82a4f17f511b1c6cd769fb1ea5d88e531a524a83d85a29e` |
| `coding/agreement.md` | `410b42e138dcacfc74df0c632aa7bfc2f2d2a6f8322bee7093f0052778e98e77` |
| `coding/second-coder/CODEBOOK.md` | `341c0ca89362c6aa837ef44bb8b0b98c24691db0236f95abd10aa15d5f6c471f` |
| `detection/summary.csv` | `556c7afd6e2c7a179ee0a4e3d85d1ef23a8ecacda19c2c8c213e542ffad3adee` |
| `detection/diagnostics.csv` | `6c7ab6ef5a9018d78faabf15fe17ce2fef85b3b771ec386e1471d6ae186100a8` |

**Boundary note.** While I was reviewing, a new directory appeared under A's tree
(`detection/cross-review-probes/`, created 14:20:30Z, containing `PROBES.md`). Its heading states it
is A's probes against my published mutants — i.e. A's side of this cross-review in a non-obvious
location. **I read the heading and stopped there**, to keep this review independent; I have not read
`PROBES.md` or `A-reviews-B.md`. A consequence worth recording: A's artefact tree is *not* frozen at
Gate 1 — files can and did change during review — which is why the table above pins hashes.

**Verdict in one line:** A's classifications are *mostly* precise and *partly* independently
verifiable — no objection is blocking, the frozen 14-record population and the headline findings
survive everything below, but the secondary (post-inspection) arm contains one record that cannot
be verified against the model at all, the anti-circularity freeze is asserted without a hash, and
the agreement study's κ = 1.0 is far weaker evidence than the report's headline table implies.

---

## 1. What I verified and it passed

Stated first, because a review that only lists complaints is not a verification.

| Claim | How I checked | Result |
|---|---|---|
| Every frozen excerpt is a verbatim substring of the cited model at the cited line | programmatic substring test over all 14 records × `corpus/normalized/*.sysml` | **14/14 verbatim**, line ranges consistent |
| Second coder's excerpts are verbatim | same test over `coder-b.csv` (11 non-W1 rows) | **11/11 verbatim** — A's mechanical check on the delegate's output holds |
| Duplicate coder files are byte-identical | `shasum -a 256` on both copies | **identical** (`336c8fce…`, `fcd5f7ce…`) |
| Second coder received the v1.0 codebook | content diff of `coding/second-coder/CODEBOOK.md` against the canonical file | **confirmed**: S2 reads "Mandatory clause … syntax/parse, blocking", no T2, no §9/§10 amendments |
| κ = 1.0 arithmetic | recomputed pₑ from the 11 paired marginals (N1 5, S1 3, S2 1, T1 1, R1 1) → 37/121 = 0.306 | **correct** (pₒ = 1.0, pₑ = 0.306, κ = 1.0) |
| Frozen population accounting | sums over `coding/models.csv` | **14 records, 12 models with ≥1, 6 clean, mean 0.78, median 1** — all correct |
| Post-inspection accounting | sums over `models.csv` | 21 records, 15 models affected, 3 clean — arithmetic correct (composition: see O1/O2) |
| 9/14 detection | re-ran `.tools/sysml -validate -format json` on T1-C1, T1-C2, T1-C3, T2-C2, T3-C2, T4-C1, T4-C3 and diffed against `detection/summary.csv` | **reproduces exactly**, per model and per code: T1-C1 silent; T1-C2 two `syntax`; T1-C3 silent; T2-C2 one `reserved-keyword-name` exit 0; T3-C2 `reserved-keyword-name`×2 + `unresolved`; T4-C1 `endpoint-not-a-node` + `syntax`×3 + `reserved-keyword-name`; T4-C3 silent |
| "Exit status is not a validity verdict" | reproduced on T2-C2: one `error` diagnostic, JSON `status: "holds"`, process exit 0 | **correct, and under-stated** — the tool's own status field says `holds` while printing an error, which is stronger evidence than the exit code (O11) |
| 18/18 raw fail, 81 raw diagnostics, 33 normalised diagnostics, 6/18 clean | counted from `detection/diagnostics.csv` and `summary.csv` | **all four numbers exact** |
| External arm: 140 diagnostics of which 119 `name-conflict`, 10/24 artefacts, 7/24 clean, 6 `syntax`, 2 `usage-typing` | recounted from `detection/diagnostics.csv`, `summary.csv`, `external/manifest.json` | **all exact** |
| Negative-folder 6/6 fail | every one of the six negative-folder artefacts carries `syntax` **errors** | **correct** — not a warning-based count |
| `validateNamespaceDistinguishibility` §8.3.2.4.5 citation | looked it up in `catalogue/classified.csv` | **correct**, including the catalogue's own spelling (I initially flagged this as a misspelling; the OMG XMI uses the same spelling and I retract the objection) |
| C2 configuration pattern | all six C2 models carry ≥1 frozen record; four share the subject-parameter mechanism | **correct** — and stronger than claimed: all six C2 models involve a `satisfy` construct |
| Two-pass inspection missing 7 of 21 defects | accepted on A's own records; I re-verified that the seven notation defects are real by re-running the tool (`port out` T3-C2:24, `attribute state` T2-C2:17, `action def assign` T4-C1:49 are all flagged by the pinned validator) | **supported** — this is the pilot's most valuable finding and it reproduces |

That is a substantial amount of verified ground. The objections below are the residue, and the
residue is concentrated where the artefacts stop being single-source.

---

## 2. Objections

Severity: **blocking** = invalidates a headline claim or the anti-circularity guarantee;
**material** = changes a reported number, a conclusion's strength, or the ability of a third party
to verify; **minor** = presentation, citation or recomputable slip that changes no conclusion.

### O1 — `T5-C3-P01` cites an excerpt that does not exist in the model. **Material.**

`coding/errors-post-inspection.csv` row `T5-C3-P01` records class S1, `evidence_excerpt =
port return;`, `line_range = 26`, model `T5-C3`.

**`T5-C3.sysml` contains no port declaration of any kind.** Line 26 is `part antenna : Antenna;`.
`:! grep -n "port " corpus/normalized/T5-C3.sysml` matches only line 2, and only as a substring of
`import`. The excerpt is not a substring of the model at any line. The row appears to be a
duplicate of `T6-C1-P01`, which carries the identical excerpt and the identical line number.

**Effect.** One of the seven post-inspection records (14% of that arm) is unverifiable, and it
inflates the report's S1 count for that arm. It does not touch the frozen 14, and `T5-C3` remains
an affected model because `T5-C3-P02` (`attribute window : VisibilityWindow;`, line 11) is real
and I confirmed the tool reports `usage-typing` on it.

**What would settle it:** A deletes or re-attributes the row, re-runs the arithmetic, and states
whether the verification step that caught coder-B's excerpts (substring test) was ever run over
A's own post-inspection rows. That the pipeline *contains* the check and it was applied to the
delegate's output but not to A's own additions is the more interesting finding.

### O2 — `§5.4` enumerates eight post-inspection additions; the file has seven; the missing one is a real defect that is left uncounted. **Material.**

`errors-post-inspection.csv` has **7** rows. Report §5.4 describes **8**: `port return;` in four
models, `port out;` (T3-C2), `attribute state` (T2-C2), `action def assign` (T4-C1), and
`attribute window` (T5-C3). Counting the described items: 4 + 1 + 1 + 1 + 1 = 8.

Two independent discrepancies:

1. `port return;` exists in **three** models, not four: T6-C1:26, T6-C2:22, T6-C3:26. The fourth
   (`T5-C3`) is O1's phantom.
2. `port out;` (T3-C2 line 24) is a **real, uncounted** S1 instance. T3-C2 declares `port in;`
   (line 23) **and** `port out;` (line 24). The frozen record's two occurrences are line 23
   (`port in;`) and line 33 (`line.in`) — not the `in`/`out` pair. And I confirmed by re-running
   the validator that it flags **both** line 23 and line 24 with `reserved-keyword-name`.

Codebook §10.4 states "the S1 record for the `in`/`out` pair now records 2 occurrences". That is
not what `errors.csv` records (it records line 23 and line 33), so the amendment describes a change
that was not made. So the post-inspection S1 count is wrong in both directions: one phantom
included, one real instance omitted.

**Net.** The report's "S1 = 9" and "21 records" are each arithmetically 3 + 6 and 14 + 7; with O1
corrected and `port out` added, the defensible numbers become S1 = 8 (or 9 if `port out` is
counted) and 21 stays 21 only by coincidence. The numbers have to be recomputed row by row.

**What would settle it:** a per-row reconciliation table of §5.4's narrative against
`errors-post-inspection.csv`, and a decision on `port out` (include it as S1, or state why a
direction keyword in a port declaration position is admissible when `in` is not).

### O3 — The frozen file and the codebook amendment contradict each other on the T1 record. **Material.**

Codebook §10.4.4: "the T1 record's span is narrowed to lines 42-43 because `assign` is a reserved
keyword (own S1 record), not a kind mismatch."

`errors.csv` `T4-C1-E01` still reads `line_range = 42-44`, notes "3 occurrences, one mechanism",
excerpt including `then assign;`.

Both choices are defensible — keep the frozen file byte-identical, or apply the correction — but
the artefacts cannot both be true. And a reader cannot tell which version the detection table used.

**Effect on the record itself.** The third occurrence (`then assign;`, line 44) rests on a name
that A's own v1.2 says is not a name at all. My re-run shows the tool errors on line 44
(`expected a body member`, `reserved-keyword-name`) and on line 43 (`endpoint-not-a-node`) but
**not** on line 42. So the T1 record as frozen contains one occurrence that is really an S1
instance and one that is not visibly defective as written.

**What would settle it:** state the convention explicitly ("amendments never touch `errors.csv`;
the corrected span is recorded only in `errors-post-inspection.csv`"), and mark the frozen row as
superseded in a `supersedes` field rather than leaving two files disagreeing.

### O4 — The pre-detection freeze of the error population is asserted but not evidenced by any hash. **Material, with a substantive mitigation that I think largely saves the claim.**

The anti-circularity guarantee (PROTOCOL §7.2) rests on `coding/errors.csv` being the pre-detection
version. The report calls it "frozen and hashed before detection". **No hash of `errors.csv` exists
anywhere in the artefacts:** `FREEZE-HASH.txt` contains only the methodology hash,
`CODEBOOK-HASH.txt` only the codebook hash, and I found no other hash record.

`errors.csv`'s mtime is 14:17Z — contemporaneous with `detection/*.csv` (14:17Z) and **after** both
codebook amendments (v1.1 14:14Z, v1.2 14:15Z). That is explainable: the v1.1 amendment
legitimately rewrote the S2 row's layer/severity/notes. But it means the ordering cannot be
verified from the artefacts, only asserted.

**Why I do not rate this blocking — the substantive argument.** A validator-driven labelling pass
would have included exactly the defects the tool flags most cheaply, and the frozen 14 omit them:
`port out` (T3-C2:24), `attribute state` (T2-C2:17), `action def assign` (T4-C1:49) are all
flagged by the pinned tool as errors, and none is in the frozen population. Conversely the frozen
population *includes* three records on which the tool is completely silent (R1 ×2, I1) and one on
which it is silent for a specific sub-mechanism (`first start;`). The pattern is what inspection
without a tool produces, not what a tool produces. That is strong inferential evidence that A's
claim is true even though the hash is missing.

**What the frozen plan actually required.** `METHODOLOGY-FROZEN.md` §7.1 says: "After `errors.csv` and
the codebook hash are final, run the pinned OpenSysML CLI …". Read closely, the *hash* attaches to the
codebook (which was hashed: `CODEBOOK-HASH.txt`) and `errors.csv` only has to be "final". So the
plan did not promise a hash of the population file; the **report** does
("Proposition 1 … `coding/errors.csv`, frozen and hashed before detection"). The gap is between the
report's wording and the artefacts, not a breach of the frozen plan.

**What would settle it:** the pre-detection sha256 of `errors.csv` (A may have it), or an explicit
statement that none was taken and that the ordering rests on the mtime plus the argument above.
For the record: **this is the objection I would escalate if A cannot supply the hash**, because the
protocol makes hashing the mechanism, not the argument.

*Timestamp note for reproducibility:* `errors.csv` and `detection/*.csv` both read `15:17` in the
container's local zone (CET, UTC+1) = **14:17Z**; `CODEBOOK.md` reads `15:15` = 14:15Z, matching the
v1.2 amendment's own timestamp. No artefact carries a UTC stamp, so a reviewer must apply the offset.

### O5 — κ = 1.0 is contaminated by *verbatim* codebook exemplars, not merely by "recognition". **Material.**

The report and `second-coder/BRIEF.md` describe the codebook's worked examples as "paraphrases of
defects that occur in the 12 double-coded models" and say recognition "cannot be removed".

I tested this directly: **7 of the 11 paired records have their excerpt character-for-character in
the coder-facing codebook** that the second coder received —
`first start;`, `satisfy greenhouse to moistureControl;`, `satisfy lowerBeforeArrival;`,
`port in;`, `satisfy alarmTiming by pump;`, `first checkCharge;`, and the entire
`connection powerLink connect controller.fleet.battery.power to …` line. The remaining four are
covered by the same exemplars: `transition from idle to lowering on detection.approaching;` is in
the codebook split across a line break, and three of the N1 records are the sub-mechanism whose
exemplar (`subject pump : InfusionPump;`) is printed verbatim.

So the accurate description is: **the codebook the second coder received is an answer key for
essentially every paired record, with the file identity removed but the text left in.** "Paraphrase"
understates it, and the residual-contamination note therefore understates the contamination.

**What κ = 1.0 can bear.** Not nothing: the second coder also called three models clean, where no
exemplar helps, and it independently *noticed* two reserved-keyword instances that were not in the
v1.0 codebook (and correctly declined to code them) — that is genuine discrimination. But class
agreement on the 11 paired records is close to string-matching plus label lookup.

**What would settle it:** re-code a held-out set that is not represented in the codebook's examples.
The LaVoie corpus is the obvious candidate and A explicitly declined to hand-code it (correctly, for
frequency purposes); a 20-model held-out agreement run there would be the real test.

### O6 — The version skew makes the layer/severity agreement figures uninterpretable, and one of the eleven "agreements" is agreement on a rule later found false. **Minor (disclosed, but the headline table does not carry the qualifier).**

Verified: the coder-facing copy is the v1.0 content, so the version story is true and the hash
mismatch (`341c0ca8…`) is explained by the A2 placeholder edit rather than by a different version.

Consequences the report should carry into its headline table:

- "Layer agreement 10/11, κ = 0.87" and "severity agreement 10/11, κ = 0.76" are measurements of
  **version skew**, not disagreement. Exactly one pair differs, and it differs because the two
  coders were handed different definitions of S2. Reporting these as agreement statistics invites a
  reader to interpret 1/11 as a coding disagreement; it is not.
- "Record-level class agreement 11/11" includes S2, where the two coders agreed on an **ID** whose
  **definition changed** and whose v1.0 content was later shown to rest on a false premise (the BNF
  makes `by` optional). Agreement on an identifier is not agreement on a construct.

A says most of this in §6 and in `agreement.md`; the objection is that the headline table (report
§6, first table) does not. **What would settle it:** annotate the two rows as "one pair differs by
codebook version, not by coding judgement", and footnote the S2 pair.

### O7 — Three recomputable numeric slips in the summary. **Minor.**

1. **"range 0–3"** for errors per model: the actual maximum is **2** (T3-C2 and T4-C1), from
   `models.csv`. Range is 0–2.
2. **"the W1 count from 18 to 4"** (report §11.3): under the codebook's own W1 definition ("it is
   markdown, **or** it contains preamble/trailing prose, or both"), the prose-only reading gives
   **7** models, not 4 — I counted preamble in 4 raw files (T1-C1, T2-C1, T4-C1, T5-C2) and
   trailing prose in 6 (T1-C1, T2-C1, T3-C1, T4-C1, T5-C1, T6-C1), union 7. The figure 4 is
   "preamble present" only. Either the definition or the number needs correcting, because the
   paragraph's purpose is to show that the convention choice matters.
3. **`trailing_prose_present` is not a column in `coding/models.csv`**, although codebook §6
   specifies it as part of the per-raw-output record, and the report's headline table quotes "6
   with trailing prose". The number is right — I reproduced 6 from the raw files — but the variable
   it comes from is not in the artefact the codebook points at.

**What would settle it:** correct the two numbers and add the column (or state that the raw files
are the record for that variable).

### O8 — R1 is placed as "structural/architectural" but its mechanism is a multiplicity property, and the criterion that admits R1 while excluding three other connector patterns is not operationalised. **Material.**

R1 (two records, T4-C1:51 and T4-C3:56) is the class that carries the report's structural claim,
and it is the class I care most about because it is the empirical analogue of my own F7.

Two problems:

1. **Placement.** The defect A describes is that a connection end's feature chain traverses a
   usage with multiplicity `[10]`/`[4]`, so the end does not denote one feature. That is a
   statement about multiplicity and end-feature conformance, which is why A's own cited constraints
   (`validateFeatureEndMultiplicity` §8.3.3.3.4, `checkConnectorTypeFeaturing` §8.3.4.5.3) are
   labelled "adjacent". If the operative rule is multiplicity conformance, R1 belongs in the
   typing/multiplicity family, and the claim "the instrument is blind to structural defects" is
   then supported by a class whose layer label is a judgement rather than a measurement. It might
   still be true — I found the tool silent on both instances too — but the label does work the
   evidence has not done.
2. **The admission criterion is not stated as a rule.** A excludes part-to-part and port-to-part
   connections (exclusion 3), value-property connections (exclusion 4) and `flow of <attribute def>`
   (exclusion 5) on the same grounds — no normative basis found — but admits R1 on the ground that
   the ends are "not individual features". That is a real distinction, but it is written as a
   description of two instances, not as a test a third party can apply to a new model. Since the
   frozen empirical subset is going to be used as *my* external challenge set, this matters
   directly: I need to know whether a new multi-valued connector end is R1 by definition or by
   analogy.

**What would settle it:** state R1's criterion operationally, e.g. "a connection end is defective
iff, after resolving its feature chain, it denotes more than one feature"; and state explicitly that
R1's layer label is an authored placement with the multiplicity reading noted as the rival. A
already says the constraint basis is authored; the *criterion* needs the same treatment.

### O9 — I1's "no reading reconciles" is asserted, and a reconciling reading exists. **Material.**

I1 (T1-C3) is the one semantic record: the requirement's `doc` says soil moisture "shall be kept
between 35% and 75%", while the requirement's own attributes declare `lowerBound = 35.0` and
`upperBound = 55.0`. A codes this as an internal contradiction, severity minor.

**The rival reading.** A requirement whose documentation states a 35–75 % band and whose own
attribute records a 55 % upper bound is not contradictory on its face: 35–55 is *contained in*
35–75. A tightened engineering limit is exactly what a model is allowed to declare. A's claim
("Both cannot be the model's upper bound") only holds if the documentation's 75 is read as
specifying the value of the attribute named `upperBound` — a reading the text does not compel.

**Why this is not pedantry.** A itself says "the prompt said 35–55, so the 75 is also a fidelity
defect" — and exclusion 1 excludes prompt-fidelity deviations. If the 75 deviates from the prompt
and the 55 matches it, then the defect *is* the deviation, and I1 is a fidelity defect re-described
as an internal contradiction in order to admit it. I am not accusing A of doing that deliberately —
the record is honestly labelled and the fidelity note is right there — but a reviewer has to point
out that the only reason this text is inside the taxonomy is a reading A does not defend against
the alternative.

**Effect.** If I1 is not admitted, the frozen population is 13 records, the detection denominator
becomes 13, and 9/13 = 69 % rather than 9/14 = 64 %. No conclusion changes; one number does.

**What would settle it:** state the criterion for "contradiction" (e.g. the doc sentence must be
read as asserting the value of the attribute), or cite a constraint (there is none —
`deriveElementDocumentation` relates documentation to content, not to values), or move I1 to a
separately labelled *authored adequacy* arm, the way R1 already is.

### O10 — Two of A's specification citations do not support the class they are attached to. **Minor.**

1. **S1 cites an OCL `check…` constraint.** `T1-C2-E01` (`satisfy greenhouse to moistureControl;`)
   cites `checkSatisfyRequirementUsageBindingConnector` (8.3.21.10), and `T2-C2-E01` (S2) cites the
   same constraint. For the *syntax* record that is the wrong basis and the wrong modality: the
   defect is a textual-notation violation, decided by the `SatisfyRequirementUsage` production in
   §8.2.2.21.2 — the very production A retrieved for the S2 amendment — whereas the cited `check…`
   constraint is a **MAY** obligation about implied binding connectors. A class whose whole point is
   "the notation does not admit this" should not rest on a discretionary semantic constraint. (I
   verified the catalogue row: `checkSatisfyRequirementUsageBindingConnector`, SysML 2.0, `check`,
   class A, MAY, §8.3.21.10.)
2. **"TransitionUsage textual notation (8.3.18.9)"** (`T2-C1-E01`). §8.3.18.9 is the *abstract
   syntax* clause. The textual notation for transitions is in §8.2.2.18 (States Textual Notation) —
   the report's own source list has §8.2.2.17 for actions, so the clause family is known. A reader
   following the citation lands on the metaclass specification, not on the notation rule that the
   record violates.

Also noted and **not** objected to: `T2` cites `checkAttributeUsageSpecialization` (§8.3.7.3),
which is class B / MAY and is about specialising `Base::dataValues`; the decisive basis for
"attribute typed by a part def" is the §7.7.1 prose. A labels R1's adjacent constraints honestly
and should apply the same label here.

**What would settle it:** replace the S1 citations with the notation productions; keep the `check…`
constraint for S2 only, where it is the right basis.

### O11 — Detection is counted per record, never per occurrence, and a record-level hit can rest on one of three occurrences. **Minor.**

A's coding unit counts distinct mechanisms, not occurrences, and the detection table inherits that
unit. For T4-C1's T1 record (3 occurrences at lines 42–44) the tool flags **one** — line 43,
`endpoint-not-a-node` — which I reproduced. The record is scored "detected". For T2-C1's S1 record
(4 transitions) the tool flags all four, so that one is occurrence-complete.

**Why it matters.** A reader asking "what fraction of this defect does the instrument see?" gets a
different answer from the table. It also interacts with the post-inspection finding: the tool
catches *some* of a mechanism and the pass/fail column says "yes".

**What would settle it:** an occurrence-level column for the multi-occurrence records (there are
only four: T2-C1, T3-C1, T3-C2, T4-C1).

### O12 — The external-arm "11 of 18 positive-folder files fail" is, for 9 of the 11, a statement about warnings. **Material.**

I reproduced the external numbers exactly, so the counts are right. The problem is what "fail"
means. In `detection/summary.csv`, `parses_as_is = no` is set whenever **any** diagnostic is
present, including warnings. Among the 18 positive-folder artefacts:

- **2** carry `error` severity diagnostics (`deepseek_reasoner_002` `usage-typing` ×2;
  `mistral_large_006` `usage-typing` ×2, plus name-conflict);
- **9** carry `name-conflict` only, which this tool emits at **warning** severity (119 of the
  external 140 diagnostics are `name-conflict` **warnings**), at exit 0.

So "11/18 fail at iteration_00" is 2 error-level failures and 9 warning-level ones. The report then
compares that number to the authors' reported 51.16 % single-shot acceptance. That comparison mixes
a warning-level count with an acceptance rate that almost certainly means "the pipeline accepted the
model". A elsewhere insists — correctly, and I reproduced it — that exit status is not a validity
verdict; the external table applies a stricter standard than A applies to the frozen population.

The negative-folder row (6/6) is clean: all six carry `syntax` **errors**. So the asymmetry is
between the two rows of the same table.

**What would settle it:** report the external arm as "2/18 error-level, 11/18 any-diagnostic,
6/6 negative-folder error-level", and drop or requalify the comparison to 51.16 %.

---

## 3. Where A's work changes my view

This is the part the protocol exists for, so I will be explicit. Four things move, one materially.

**(a) My F2 result does not generalise, and A's corpus falsifies my generalisation. Material change.**
My pilot reports resolution-layer detection at **4/4** and I described F2 as "unresolved reference"
without stratifying by *site*. A's corpus contains a dangling **succession source** (`first start;`,
T1-C1:64) that the same pinned validator passes silently — A verified it with a dedicated probe
(`probe01`), and I reproduced the silence myself. So the correct statement of my result is: *the
instrument resolves type references and feature references in expressions completely (4/4), and does
not resolve succession sources at all.* My report's §1 sentence and P1 need that qualifier. I will
carry it as a dated addendum rather than edit the frozen text, and I will add succession sources to
the fault model in the next pass. **This is the single most useful thing the cross-review produced
for me.**

**(b) My F7 "oracle gap" is representative after all — and A's frequency is a useful calibration.**
I flagged in my limitations that F7's 0/4 could be an artefact of my own choice to include
architectural defects. A's independent corpus contains structural records (R1 ×2) and a semantic
contradiction (I1) out of 14 frozen records — **3/14 = 21 %**, of which the two structural ones
(2/14 = 14 %) are directly comparable to my F7 share (4/32 = 12.5 % of my mutants). Those are close
enough that my uniform one-class-of-eight allocation is not badly unfair. What changes is the
*weight* I should give it: in an observed population, structural + semantic defects are a minority
of defects but a majority of the *undetectable* ones, which is a sharper claim than I made.

**(c) A's post-inspection result validates my "author-as-mutator" worry as a general phenomenon.**
Inspection alone missed 7 of 21 defects and every one was mechanical notation. That is the same
failure mode as mine (I read my tool's `-explain` list before writing expectations, which I
disclosed): the author of a defect set is the wrong person to bound it. Two independent pilots
producing the same limitation is worth more than either one alone.

**(d) A tension between A and me that needs adjudication, not resolution by either of us.**
`name-conflict` is the code where our two studies actively disagree. A's external arm finds it in
10 of 24 public artefacts and treats it as a missing class (119 of 140 diagnostics). **In my
known-good arm the same code is my only false positive**: it fires as
`warning[name-conflict]: Duplicate of inherited member name 'cutoff'` on a line I quoted verbatim
from the specification's own `TestWithCutoff` example (§7.13.4), where the same-named member is an
implicit redefinition and not a duplicate. Both observations can be true at once, and that is the
finding: **`name-conflict` does not distinguish an illegal duplicate from a legal implicit
redefinition**, so it is unusable as a defect signal in either direction. A treats it as a class
signal; I treat it as a false positive. The adjudicator should record this as a genuine unresolved
tension with a concrete resolution test (code the 10 external artefacts' `name-conflict` lines
against §7.6.3/§7.6.5 by hand and see how many are implicit redefinitions).

**(e) Convergence worth noting: exit status versus diagnostics.** A measured that a notation error
can be reported with exit 0; I found the same behaviour in my pre-freeze calibration and built my
harness around it. Two independent observations of the same instrument behaviour is exactly the kind
of corroboration this run should be able to produce, and it strengthens both pilots' claim that a
"pass rate" gated on exit status is not a validity measure.

**(f) One thing A's data does *not* change.** My conclusion that the instrument's ceiling is typing
plus per-constraint well-formedness is untouched; if anything A's silent-on-5-of-14 result reinforces
it from a corpus I did not author.

---

### O13 — The detection run does not record the per-file sha256 and tool identity that A's own frozen plan requires. **Minor.**

`METHODOLOGY-FROZEN.md` §7.2 requires: "Diagnostics are recorded **verbatim** in
`research/issue-007/detection/raw/` with the exact command line, exit code, tool version and
per-file sha256."

The raw files do carry a verbatim header with the exact command line and `[exit N]`, plus stdout and
stderr — that part is right and it is what let me reproduce the run. What is **absent** from every
raw file and from `run_detection.py` is a per-file sha256 (no `hashlib` import; I checked) and a
per-file tool-version line. The instrument is pinned in `TOOLING.md` and the report, so this is
recoverable by a reader who trusts the pin, but it is not what the plan said would be recorded, and
it means the models the diagnostics refer to cannot be checksum-verified from the detection artefacts
alone. Several models were also normalised (all 18), so a change to a normalised model after the run
would be invisible.

**What would settle it:** a `manifest.json`-style record (A already built one for the external arm,
which does carry sha256 and source URLs — so the practice exists in the same pipeline and was not
applied to the primary corpus).

## 4. Severity summary

| ID | Objection | Severity |
|---|---|---|
| O1 | `T5-C3-P01` excerpt does not exist in the model (phantom post-inspection record) | Material |
| O2 | §5.4 lists 8 post-inspection additions, file has 7; `port out` (T3-C2) omitted though real | Material |
| O3 | Frozen `T1` row (lines 42-44) contradicts codebook §10.4's "narrowed to 42-43" | Material |
| O4 | No hash evidences the pre-detection freeze of `errors.csv` (mitigated by substantive argument) | Material |
| O5 | 7/11 paired excerpts are verbatim in the coder-facing codebook; κ=1.0 is largely answer-key matching | Material |
| O8 | R1's layer label is a judgement and its admission criterion is not operationalised | Material |
| O9 | I1's "no reading reconciles" has a reconciling reading; may be an excluded fidelity defect re-described | Material |
| O12 | External "11/18 fail" = 2 error-level + 9 warning-level; comparison to 51.16 % is not like-for-like | Material |
| O13 | Detection raw files omit the per-file sha256 and tool-version line the frozen plan §7.2 requires | Minor |
| O6 | Layer/severity agreement figures measure version skew; one "class agreement" is on a repudiated rule | Minor |
| O7 | "range 0–3" (actual 0–2); "W1 18 vs 4" (actual 18 vs 7); `trailing_prose_present` not recorded | Minor |
| O10 | S1 cites a MAY OCL constraint as its basis; transition notation cited at the abstract-syntax clause | Minor |
| O11 | Detection counted per record; T4-C1's T1 hit rests on 1 of 3 occurrences | Minor |

**0 blocking, 8 material, 5 minor.** The frozen 14-record population, the 9/14 detection result,
the V1/V2 wrapper split and the "inspection missed a third of the defects" finding all survive
intact. What does not survive unqualified is the *strength* of the agreement study (O5), the
arithmetic of the secondary arm (O1/O2), and two class placements (O8/O9).

## 5. What I did not review, and the limits of this review

- **The corpus prompts and their adequacy.** I read `corpus/prompts.md` only enough to check the
  C2 configuration claim. Whether the six prompts are a fair task sample is a different review.
- **The LaVoie external corpus itself.** I verified A's counts against A's downloaded files and
  A's own manifest; I did not re-fetch the 24 files or verify their sha256 against the upstream
  repository. If the download is corrupt, every external number is affected and I would not know.
- **The generator's actual prompts-to-output correspondence.** Not checkable from the artefacts.
- **The second coder's reasoning.** I checked its outputs against the models; I did not and cannot
  assess how it arrived at them.
- **I did not re-run A's scripts** (`inspect.py`, `labels.py`, `post_inspection.py`,
  `agreement.py`) end to end; I recomputed their outputs from the CSVs and re-ran the validator
  independently. A reviewer with more time should re-run the pipeline to confirm determinism.
- **My own stake.** I am the researcher whose external challenge set will be built from A's frozen
  subset, so I have an interest in that subset being clean. I have tried to hold that interest at
  arm's length: every objection above is checkable by a third party from the artefacts, and none of
  them argues for changing a *label* in a direction that would make my later task easier. Where
  A's work corrects me (section 3a) I have said so plainly.

## 6. Response required from A (dated), not from me

Each objection needs one of: **accepted** (artefact corrected, with the corrected number), **rejected**
(with the evidence that shows my check is wrong), or **unresolved** (with what would settle it). I
would ask in particular for O4 — a hash, or an explicit statement that none was taken — because the
protocol makes the hash the mechanism rather than the argument, and for O1, because a record whose
excerpt is not in its model is a different kind of problem from a wrong label.
