# Reviewer A — independent review of the issue #7 pilot (methods, evidence, interpretation)

**Reviewer:** Reviewer A (independent; did not produce the work under review).
**Subject:** issue #7 pilot — `reports/issue-007-error-taxonomy-pilot.md` and the artefacts under
`research/issue-007/`, plus the Gate-2 record (`B-reviews-A.md`, `A-response-to-B-review.md`).
**Review completed:** 2026-11-13T14:40Z. **No git command was run. No researcher artefact was edited.**
This file is my only write.

**Pinned snapshot.** The tree changed while I reviewed it (see §7, P-1). Every citation below is to
the following bytes, verified by `shasum -a 256` at 14:37–14:40Z:

| Artefact | sha256 (reviewed) |
|---|---|
| `reports/issue-007-error-taxonomy-pilot.md` (810 lines) | `edf02fc6173da7f563aa2fad82ee8946a70498932ed28b27813ed3ea152cc2fd` |
| `research/issue-007/METHODOLOGY-FROZEN.md` | `269d8dbe7228db83d20ca2be39991172f20fd23458ac1e5e6755ff7269564f76` |
| `research/issue-007/AMENDMENTS.md` | `34855cdfde7c71ce826b7db06ca667cfc5c828b8a038001b274d89e1d39fe559` |
| `coding/CODEBOOK.md` (v1.3) | `106e620d6c6808f980f2f58d6e79f574bcd350dcf41978a4083df0cdd9063314` |
| `coding/errors.csv` (frozen, 14 rows) | `30265ff57bdd1f4036304c6acbc1026678d36f0b3604c925a7b538455fc815f6` |
| `coding/errors-post-inspection.csv` (7 rows) | `285d70ea816eb3d73da9a954faba5f54d05292103da3c740abb9763da7851f74` |
| `coding/errors-corrections.csv` (C01–C13) | `c551040564049eee7e358dfba63b0584c42a2807aca9986c2a417576566489ec` |
| `coding/errors-combined.csv` (19 rows) | `56f4467a755f9764e1651a99c48b0f4bd5d097434699708ee0b9027d78b750fe` |
| `coding/models.csv` | `c3ccec8e88ace00dd68be8869c01f0d134daed9362f7a600686b7f718cbd243e` |
| `coding/agreement.md` / `agreement.json` | `f67ba9db…4ea1c` / `ce603cb0…27e80` |
| `coding/second-coder/CODEBOOK.md` (coder-facing, v1.0) | `341c0ca89362c6aa837ef44bb8b0b98c24691db0236f95abd10aa15d5f6c471f` |
| `coding/second-coder/INSTRUCTIONS.md` | (not separately hashed by A; cited by line) |
| `coding/coder-b.csv` | `336c8fce423d9f8ed74d94a4ddafb54e5d51dce49506bc1c8e88ad9e3f206123` |
| `detection/summary.csv` | `556c7afd6e2c7a179ee0a4e3d85d1ef23a8ecacda19c2c8c213e542ffad3adee` |
| `detection/diagnostics.csv` | `6c7ab6ef5a9018d78faabf15fe17ce2fef85b3b771ec386e1471d6ae186100a8` |
| `research/relational/cross-reviews/B-reviews-A.md` | `de2d99cea17587a9603e9602303873556db9b00f93d8101451c0db57be9af0b1` |
| `research/relational/cross-reviews/A-response-to-B-review.md` | `965924fe8e2bce7a1387aef44060bfe7292219461f6cdaaf353c9d61151ebd45` |
| `.tools/sysml` (OpenSysML v0.12.1) | `ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0` |

---

## 0. Summary verdict

The **empirical substrate of the pilot reproduces**. I re-ran the agreement, corrections and
detection scripts and obtained byte-identical outputs (apart from an absolute-path column in
`diagnostics.csv`); the frozen 14 records, the 12/6 model split, the 9/14 detection table, the
external-arm counts and the 8/11 answer-key count all re-derive from the stored evidence. The
corrections pipeline is deterministic and genuinely derives the corrected population from the
preserved raw fields. A's response is candid: B was right on O1 (phantom) and O12
(warning-vs-error) and A accepted both; A's 8/11 answer-key count is more accurate than B's 7/11;
and A's treatment of I1 (keep, mark contested, report both denominators) is better reasoned than
B's implied withdrawal.

**But the report's interpretative claims are weaker than its numbers, and A's own later corrections
have not been integrated into the summary sections.** Two findings carry most of the damage:

1. **The 9/14 “validator blind spot” is composed entirely of records whose defect status is
   contested, discretionary, or not established.** Of the five silent records in the published
   table, one (`first start;`) is now withdrawn as legal SysML (C12) and the other four are S2 (a
   MAY-report constraint), R1 ×2 (no normative basis), and I1 (contested). After C12 the table is
   9/13, and on the records that are established defects and mandatory-to-report the instrument
   detects **9/9**. The report's “silent on 5 of 14 … neither method is an oracle” is arithmetically
   right and interpretatively unsupported.
2. **The V1/V2 wrapper split (6/12) is gate-dependent and A applies two different gates.** Three of
   the twelve “invalid after normalisation” models are exit-0, warning-only `reserved-keyword-name`
   reports (T2-C2, T6-C1, T6-C3). Under the error-level gate A himself applied to the external arm
   (O12), V1 = 9 and V2 = 9, not 6/12. The headline (report §1, §7) never states the gate.

Neither is a fabrication and neither destroys the pilot's qualitative claims — the wrapper is
universal and not sufficient; inspection did miss mechanical notation defects; the taxonomy is
countable. But a reader of the report as filed would over-read the detection and wrapper results.

**Verdict counts (13 propositions):** 1 supported · 8 partly supported · 2 not supported ·
2 unverifiable. **Objection register:** **0 blocking · 7 material · 6 minor** (plus one adjacent
finding for B's arm).

---

## 1. Claim-by-claim verdicts

Verdicts are mine; the evidence column is the artefact a third party can check. “Partly” means the
arithmetic is right but the stated scope, denominator, population or gate is not.

| # | Claim (report location) | Verdict | Evidence |
|---|---|---|---|
| 1 | **Headline error population: 14 coded errors in 12/18 models, 6 clean; mean 0.78, median 1** (§1 table, report:36–50) | **Partly supported** | `coding/errors.csv` has 14 data rows over 12 models; `models.csv` re-sums to 14/12/6, mean 0.778, median 1, range 0–2. The *effective* population after A's own C12 is **13 records / 11 models / 7 clean** (report:784–790; `errors-combined.csv` 19 rows; `errors-corrections.csv` C12). The §1 table still says 14 and the banner says the 14 “survives” (report:8). |
| 2 | **Class distribution: N1 5, S1 3, R1 2, N2 1, S2 1, T1 1, I1 1** (§1, report:52–63) | **Partly supported** | Exact from `errors.csv`. After C12, **N1 = 4**; after C05/C06, R1's layer is `type/typing` in the corrected population, not `structural/architectural`. The §1 table and README headline still show N1 = 5 and R1 = structural. |
| 3 | **The pinned validator detects 9/14 (64 %)** (§1:50, §5.1:238–253) | **Partly supported** | Re-ran `run_detection.py`: `detection/table.md` is byte-identical; per class S1 3/3, N1 4/5, N2 1/1, T1 1/1, R1 0/2, S2 0/1, I1 0/1 = 9/14. After C12 it is **9/13 = 69 %** (report:787). The *interpretation* — “the instrument misses a quarter of the defects” — is not established: every silent record is withdrawn, discretionary or contested (see §5, item 1, and objection M-1). |
| 4 | **Inspection missed a third of the defects: 7 further notation defects, 7 of 21** (§1 finding 2:78–85; §5.4:289–308) | **Partly supported** | The six live post-inspection rows are real and tool-flagged: `port return;` at T6-C1:26, T6-C2:22, T6-C3:26; `attribute state : String;` at T2-C2:17; `action def assign;`/`then assign;` at T4-C1:44,49; `attribute window : VisibilityWindow;` at T5-C3:11 (verified in the models; diagnostics at those lines). The seventh (`T5-C3-P01`) is the phantom A withdrew. “7 of 21” is stale: 6 live post-inspection defects against 20 combined records before C12, 19 after. The rate is also selection-biased (A's own subset excludes these six as “non-independent for a detection measurement” — `research/relational/empirical-subset/subset.json`, `excluded`). |
| 5 | **Wrapper/V1-V2: 18/18 raw outputs fail, 6/18 invalid only because of the wrapper, 12/18 still invalid after normalisation** (§1:43–47; §7:410–422) | **Partly supported** | 18/18 raw outputs exit 2 with diagnostics; 6/18 normalised models have zero diagnostics. But of the 12 “invalid” normalised models, **3 are exit-0 warning-only** `reserved-keyword-name` (`summary.csv` rows T2-C2, T6-C1, T6-C3: `exit_code=0`, `n_error=1`, `nonblocking_notation_only=yes`). Under the any-diagnostic gate V1 = 6, V2 = 12; under the error-level gate A applied to the external arm, **V1 = 9, V2 = 9**. The headline does not state the gate. |
| 6 | **External-corpus check (LaVoie et al.): 7/24 clean, 10/24 `name-conflict`, 6/6 negative fail; `name-conflict` absent from the 18-model corpus** (§5.5:310–337; §16.6:735–742) | **Supported (corrected form)** | Recounted from `summary.csv` + `external/manifest.json`: 24 files = 18 positive + 6 negative; positive = 2 error-level, 9 warning-only, 7 clean; negative = 6/6 error-level; 119 of 140 external diagnostics are `name-conflict` warnings, present in 10/24. No `name-conflict` in the primary corpus. Local files match the manifest hashes and contain no fences. The “only public corpus located” search-completeness claim is not independently verified (see §8). |
| 7 | **“The frozen 14-record population survives / did not change”** (banner report:8; §16.8:758–765) | **Not supported as stated** | `errors.csv` is byte-identical (`30265ff5…`), but C12 **withdraws** `T1-C1-E01` from the effective population; A's own §17.1 table says 13 records / 11 models / 7 clean (report:784–790), and `errors-combined.csv` has 19 rows. The file-preservation sense is true; the evidentiary sense (“no frozen record was withdrawn”) is false. |
| 8 | **C2 configuration pattern: all six C2 models carry ≥1 error; four share the dangling-`satisfy` mechanism** (§1 finding 3:86–90; §2 Prop. 8:105) | **Partly supported** | From `errors.csv`: C2 models T1-C2 (S1), T2-C2 (S2), T3-C2 (S1+N1), T4-C2 (N1), T5-C2 (N1), T6-C2 (N1) = 6/6; the subject-parameter N1 occurs in T3-C2, T4-C2, T5-C2, T6-C2 = 4/6. The descriptive observation holds. The causal wording (“causes”) is explicitly provisional at n = 1 per cell; it is a hypothesis, not an effect (A says so). |
| 9 | **Second-coder agreement: 12/12 presence, 11/11 class, κ = 1.0, α = 1.0; layer 10/11, severity 10/11** (§6:341–372) | **Partly supported** | Re-ran `agreement.py`: identical `agreement.md`/`agreement.json`; the statistics are exact (κ class 1.0, pₑ 0.3058; layer 10/11 κ 0.8659; severity 10/11 κ 0.7556). The *reliability* claim is not supported: I reproduced **8/11** paired excerpts verbatim in the coder-facing codebook (11/11 exemplar-covered), and `INSTRUCTIONS.md:61–64` additionally states the S2/T1/N2/R1 criteria as “SysML v2 facts you may rely on”, including the false “requires `satisfy <requirement> by <feature>`”. A's §16.5 downgrade is substantially right; its “W1 dissent” item is not. |
| 10 | **Structural and semantic defects are present and invisible to the instrument** (§13:551–555; implied §1:78–85) | **Not supported as stated** | After C05/C06, R1 is `type/typing` in the corrected population and the report's own §16.4 says “the frozen population contains no record the report can defend as architectural” (report:713–721). I1 is `frozen_contested` (C07). Structural = 0; semantic = 1 contested. What survives is the narrower, true instrument claim: the tool reported nothing on the two connector records and on I1. |
| 11 | **The codebook is applicable without drift by an independent second reader** (§2 Prop. 4:101; §6.1) | **Partly supported** | The second reader's rows are line-accurate and verbatim-substring-verified, and it produced coherent labels. But 8/11 excerpts are verbatim in the codebook it was given, 11/11 exemplar-covered; the instruction sheet asserts the class criteria; and the current codebook v1.3 remains internally inconsistent (see §4.3). “Applicable without drift” is not established; “the labels can be reproduced from the codebook” is. |
| 12 | **The error population was frozen before detection** (§2 Prop. 1:98; §16.2) | **Unverifiable** | No hash of `errors.csv` exists (A concedes: report:666–701; `A-response-to-B-review.md` O4). The composition argument is the only support, and C12 removes one of its three “silent” records. mtimes have been reset by re-runs/copies and cannot establish order. See §3. |
| 13 | **The corpus is one generation per cell by the same DeepSeek-family model** (§3.2:148–151; §11.1) | **Unverifiable** | The 18 raw files are present and hash-consistent, but `generation_timestamp_utc` in `corpus/manifest.csv` is the raw file's mtime (`extract.py:106–107`); all 18 were written 14:07:24–14:07:56Z. There is no generation log or per-turn record. The generator = coder circularity is disclosed; the “one turn per cell” claim is A's word. |

---

## 2. Independent re-derivation

All scripts were run on a copy under `/tmp/revA` (with `.tools` symlinked read-only), not in the
repository. **No researcher artefact was modified.** The repository files were compared by `diff`
and `shasum`.

### 2.1 Agreement

```bash
cp -R research/issue-007 /tmp/revA/research/issue-007
cd /tmp/revA && python3 research/issue-007/coding/agreement.py
```

Output: `presence 12/12; class 11/11; kappa=1.0; alpha=1.0; layer 10/11; sev 10/11`.
`agreement.md` and `agreement.json` were **byte-identical** to the committed files.
This confirms the κ arithmetic independently: pₒ = 1.0, pₑ = 37/121 = 0.3058 (N1 5, S1 3, S2 1,
T1 1, R1 1), κ = 1.0.

### 2.2 Corrections pipeline

```bash
cd /tmp/revA && python3 research/issue-007/coding/apply_corrections.py
```

Output: `excerpt verification: 19 records, all excerpt parts found in their models`; `frozen 14 |
post 7 (1 withdrawn) | combined 19`; combined classes `S1 8, I1 1, S2 1, N2 1, N1 4, T1 1, R1 2,
T2 1`; contested `T1-C3-E01`. `errors-combined.csv`, `models.csv` and `reconciliation.md` were
**byte-identical** to the committed files (`56f4467a…`, `c3ccec8e…`, `c99c1b07…`).

So the pipeline does derive the corrected counts from the preserved raw fields, and the frozen
`errors.csv` is genuinely untouched by it. Two caveats:
- The excerpt-substring contract (`apply_corrections.py:64–82`) is what caught the phantom; it is
  applied only to the *combined* set, after C01 has already dropped `T5-C3-P01`. It would not catch
  a bad row in `errors-post-inspection.csv` unless the row survives into the combined set.
- `models.csv`'s `n_errors_post_inspection` column is overwritten with the *combined* count
  (`apply_corrections.py:105`), so the column name misdescribes its content. Minor (m-5).

### 2.3 Detection

```bash
cd /tmp/revA && python3 research/issue-007/detection/run_detection.py
```

- `detection/summary.csv` and `detection/table.md`: **byte-identical**.
- `detection/diagnostics.csv`: all 260 rows identical on every field except the absolute `path`
  column (a copy-path artefact); no content difference.
- Counts: normalised 33, raw 81, external 140, probe 6; codes `syntax` 101,
  `reserved-keyword-name` 17, `unresolved` 17, `endpoint-not-a-node` 1, `usage-typing` 5,
  `name-conflict` 119.
- Per-class: S1 3/3, N1 4/5, N2 1/1, T1 1/1, R1 0/2, S2 0/1, I1 0/1 = **9/14**.

**One numeric slip found:** raw diagnostics are **72 `syntax` + 9 `reserved-keyword-name` = 81
total**. The report says “81 `syntax` diagnostics” (report:44, 251). B had it right (“81 raw
diagnostics”, `B-reviews-A.md:63`); A's label is wrong. It changes no conclusion (m-6).

### 2.4 Manual recounts

- Frozen: 14 rows, 12 models, 6 clean; mean 14/18 = 0.778, median 1, range 0–2; configs C1 5,
  C2 7, C3 2. All match `errors.csv`/`models.csv`.
- Combined (C01 + C12): 19 rows, 14 models affected, 4 clean; S1 8, N1 4, R1 2, others 1.
- External: 18 positive + 6 negative; positive 2 error / 9 warning / 7 clean; negative 6/6 error;
  119/140 `name-conflict` warnings; 10/24 artefacts with `name-conflict`. All match report §16.6.
- Answer-key: 8/11 paired excerpts whitespace-normalised-verbatim in
  `coding/second-coder/CODEBOOK.md`; the other 3 are the `subject pump : InfusionPump;` exemplar's
  sub-mechanism. Matches A's §16.5 (and improves on B's 7/11).
- Extraction: all 18 normalised bodies are verbatim substrings of their raw files; manifest hashes
  match; all 18 have exactly one `sysml` fence; preamble 4, trailing prose 6, union 7.

### 2.5 C12's normative basis

A cites `sysml.library/Systems Library/Actions.sysml` line 43, sha256 `ac36c940…5693`. I retrieved
the file from the Open-MBEE release repository: **sha256 `ac36c9404cac347a2c12d4a0cb067b1a9cebcba6a1a1853eaa1f5b3fdeb15693`**, and it contains
`action start: Action :>> startShot {` inside `abstract action def Action`. C12's factual premise
is verified. (The file is not stored in the repository, so a reader cannot check it offline; that is
a source-availability gap, not a correctness problem.)

---

## 3. Anti-circularity audit

### 3.1 What is established

- The frozen labels are a static list in `labels.py`; `errors.csv` is re-derivable from it.
- The detection run edits no label (`run_detection.py` writes only detection files and the two
  detection columns of `models.csv`; the table it prints is built from `errors.csv`).
- The frozen set's **composition** is not what a validator-copying pass would produce: it omits
  exactly the cheap, tool-flagged notation defects (`port out;` T3-C2:24, `attribute state : String;`
  T2-C2:17, `action def assign;` T4-C1:49) and includes records the tool does not report (R1 ×2,
  I1). This is the strongest available evidence, and it is inferential, as A says.

### 3.2 What is not established

- **No hash of `errors.csv` at freeze.** `FREEZE-HASH.txt` and `CODEBOOK-HASH.txt` hold other files;
  `detection/manifest.json` hashes the artefacts the detection run touched, not the coding files.
  A's reconstruction (report:666–701; response O4) is candid but is reconstruction.
- **No synchronised clock.** The raw files' mtimes are the only “generation” times; `errors.csv`,
  `errors-post-inspection.csv` and the detection outputs all share a late re-run mtime (my snapshot:
  14:28:49Z). `post_inspection.py` (mtime 14:14:54Z) precedes the current `run_detection.py` mtime
  (14:26:45Z) and the detection outputs (14:28:49Z), so the claim “the post-inspection arm was
  written after the detection run” cannot be verified from artefacts; it is author-asserted. The
  file may have been edited after the run (the combined-table block was added later), but the
  ordering is not evidenced.
- **The post-inspection arm is validator-surfaced by construction.** A's rule (discover by any
  route, enter only on a spec basis) is defensible and disclosed, but it means the six live
  post-inspection records are not an independent sample of “what inspection missed”; they are the
  defects the tool happened to find. A's own empirical subset excludes them for exactly this reason
  (`subset.json`, `excluded`: “their discovery route makes them non-independent for a detection
  measurement”). That is the right call for B's arm — but it also means the report's **15/19
  combined detection rate is not a detection measurement** (m-1).

### 3.3 Is A's withdrawal sufficient, and does any claim still lean on it?

A's withdrawal of “frozen and hashed before detection” is **substantively sufficient** (it states
no hash exists, labels the ordering inferential, and asks the adjudicator to treat Proposition 1 as
argued, not hashed). It is **not sufficient presentationally**: the §2 status table still reads
“`coding/errors.csv`, frozen and hashed before detection” (report:98), and the banner points readers
to §16 but not §17 and still says the 14-record population survives (report:8). Claims that still
lean on the withdrawn mechanism:
- the detection table's own intro (“frozen **before** this run”, `run_detection.py:162–165`, emitted
  into `table.md`);
- the “primary vs post-inspection” separation that makes 9/14 the primary rate;
- the 15/19 combined rate;
- Proposition 1's “Established”.
The C12 withdrawal also weakens the composition argument: one of the three “silent” records A used
as proof the labels were not tool-driven (`first start;`) is now shown not to be a defect at all.

**Audit verdict: no evidence that validator output set a frozen label; the ordering is not
verifiable; the post-inspection arm is validly labelled but not independent; A's disclosure is
honest but incomplete in the summary sections.**

---

## 4. Codebook and agreement

### 4.1 Mutual exclusivity in practice

The 19 combined records each carry exactly one class; I found no double-coded record. The
boundaries that could have collided are handled defensibly:
- **S1/N1** in T3-C2: `port in;`/`port out;` (S1) and `satisfy alarmTiming by pump;` (N1) are
  different spans; `line.in` is an occurrence of the S1 mechanism, not a separate N1, under
  precedence 2 (unparsed span → no name coding). Defensible.
- **T1/S1** in T4-C1: the kind mismatch is confined to lines 42–43 after C04; `then assign;`/
  `action def assign;` (44,49) is the reserved-keyword/S1 mechanism. The split is a judgement, but
  it follows “mechanism, not symptom” and the tool's own line-level diagnostics. Defensible.
- **N1/R1** in T6-C2: the unresolved `heating` at the connection (line 42) is an N1 occurrence, not
  R1; A records it as N1 at line 40 only — an occurrence-count omission (m-3), not a class overlap.
- **I1/fidelity**: the only genuine status contest (below).

So the taxonomy is **countable**; that part of issue #7's “convincing evidence” is met at pilot
scale.

### 4.2 R1 and I1: are A's rulings defensible?

**R1 — partly defensible; the re-layering is an improvement, but it does not establish that R1 is
an error.** A accepted B's point that the operative property is multiplicity/typing and re-recorded
the layer as `type/typing` (C05/C06; response O8). That is the right layer call. But:
- The nearest named rule, `validateFeatureEndMultiplicity` (catalogue row, §8.3.3.3.4), says “If a
  Feature has `isEnd = true`, then it must have multiplicity 1..1.” It constrains the connector's
  **end features**, not the multiplicity of a usage traversed by a feature chain. A's own note says
  the constraint is “adjacent, not decisive” (`errors.csv` T4-C1-E02), and the codebook says “I did
  not find a named constraint that decides feature chains over multi-valued usages”
  (`CODEBOOK.md:151–156`).
- A's operational criterion — “after resolving its feature chain, it denotes more than one feature”
  — conflates a feature with its instances. `controller.fleet.battery.power` denotes **one** feature
  (`power`) whose featuring instances number 10 through `fleet : Agv[10]`; it does not denote ten
  features. The intended test (“the chain traverses a usage with multiplicity >1”) is a modelling
  property, not by itself a well-formedness violation. The subset freezes this wording for B
  (`subset.json`, `operational_criterion_R1`), so the ambiguity propagates into B's challenge set.
- The defensible status is therefore **contested as a defect**, like I1, not merely contested as a
  layer. Keeping the two records in the primary denominator is A's call, but the report should not
  count them as established structural/typing defects.

**I1 — A's ruling is defensible, and better than B's implied withdrawal.** The rival reading (a
documentation band of 35–75 % containing a declared 35–55 % bound is a tightened engineering limit,
not a contradiction) is live; A's original “both cannot be the upper bound” is not established. The
protocol reason for not withdrawing it on review (the correction would improve the rate) is sound,
and reporting 9/14 and 9/13 side by side is the honest treatment. Two residual problems:
- The codebook has no “contested” status; C07 introduces one in the corrections file only. The
  codebook definition of I1 (“no reading reconciles”, `CODEBOOK.md:162–172`) is **not met** on the
  rival reading, so under the frozen text the record should be withdrawn or reclassified. Marking
  it contested is a pragmatic, disclosed exception; it should be a codebook amendment, not only a
  CSV field.
- After C12 the “9/13 = 69 %” figure appears twice with **different 13s**: §16.3's 13 = 14 − I1
  (uncontested), §17.1's 13 = 14 − T1-C1 (C12). Both happen to yield 9/13 because both removed
  records were undetected, but a reader cannot tell them apart. Unique labels are needed (m-5).

### 4.3 The codebook is not internally consistent (material)

The corrections were applied to individual records and to §11 prose, but **not to the class table or
the S2 body**, which are the parts a new coder would use:
- **S2 table** (`CODEBOOK.md:34`) correctly says “Required semantic binding absent where the
  notation's clause is optional”. **S2 body** (`CODEBOOK.md:78–87`) still says “**Mandatory clause
  omitted** … a clause the notation requires is absent” — the false v1.0 premise A corrected in §9
  after reading the BNF. A third party applying the body would code S2 as syntax/blocking, exactly
  as the second coder did.
- **R1 table** (`CODEBOOK.md:39`) still places R1 at `structural/architectural`, while C05/C06 and
  §11.3 re-record it as `type/typing`. The table is the authoritative class→layer mapping.
- **S1 table** (`CODEBOOK.md:33`) still cites `checkSatisfyRequirementUsageBindingConnector`
  (8.3.21.10) and `TransitionUsage` textual notation (8.3.18.9) — the two citations C08/C09 replace
  because they do not support a notation defect.
This is not a numbers error, but the codebook is issue #7's stated reusable deliverable; as filed,
v1.3 would reproduce the pre-correction labels. It should be fixed with dated “superseded” markers
and re-hashed, and the agreement should be re-run against the corrected codebook.

### 4.4 The 8/11 answer key and A's revised wording

What the 8/11 leaves as independent evidence:
- **Three clean-model calls** (T3-C3, T5-C1, T6-C3): no exemplar exists for “no defect”; genuine
  discrimination. (T6-C3's clean call is accompanied by a recorded `port return;` objection, so it
  is a codebook-clean call, not an unqualified “no defect” judgement.)
- **Three reserved-keyword notices** (`attribute state`, `port return` ×2) that the coder left
  uncoded for lack of a rule: genuine discrimination, and the same blind spot A had.
- **Verbatim-substring/line verification** of the coder's excerpts: a mechanical check that it used
  the models, not evidence of class reliability.
- **No class-level independence**: all 11 paired labels are verbatim or exemplar-covered, and
  `INSTRUCTIONS.md:61–64` additionally supplies the S2/T1/N2/R1 criteria as facts. The S2 pair
  (A `constraint/OCL, minor`; B `syntax/parse, blocking`) is not a codebook-version accident: the
  instruction sheet told the coder that `by` is required, a rule A's own v1.1 shows is false.
- **No W1 “dissent”**: both coders treat a bare fence as W1 (A counts 18/18 raw outputs; B codes W1
  for 12/12, including bare fences). The disagreement is about where W1 is *recorded*, not whether
  it applies. A's §16.5 list should drop “its dissent on the W1 convention” (m-2).

A's revised wording is therefore **substantially accurate and appropriately deflationary** on the
8/11 count and on κ; it **over-claims** the W1 dissent and **under-describes** the instruction
sheet. “Only the three clean-model calls are independent” (README) is accurate for class/presence
agreement, but the reserved-keyword notices are also independent and should be named.

---

## 5. Interpretation overreach

1. **The detection gap is composed of the disputed records (M-1).** Report §1 finding 2 and §5.3 say
   the validator is silent on 5 of 14: `first start;`, S2, R1 ×2, I1. After C12 the first is
   withdrawn, leaving S2 (a MAY-report constraint; the catalogue row says “MAY report, satisfy by
   implied relationships, or ignore”), R1 ×2 (no normative basis), I1 (contested). The established,
   mandatory-report records are S1 ×3, N1 ×4, N2 ×1, T1 ×1 — and the tool detects **9/9** of them.
   The ladder is 9/14 → 9/13 (C12) → 9/12 (exclude I1) → 9/10 (exclude R1) → **9/9** (exclude S2's
   discretionary reporting). The report presents 9/14 as a blind-spot measurement; it is a
   disagreement with the disputed records.
2. **The V1/V2 gate is unstated (M-2).** See claim 5. The report elsewhere (probe07, §5.2) insists
   exit status is not a validity verdict, then counts three exit-0 warning-only models as “invalid”.
   A corrected exactly this conflation for the external arm (O12) but not for the primary headline.
3. **“All 18 raw outputs fail as SysML *because they are markdown*”** (§2 Prop. 6:103) is
   contradicted by the report's own 6/18 clean result: only 6 fail *because of* the wrapper; 12
   fail for other reasons (9 error-level, 3 warning-only). The corrected sentence is “18/18 fail
   as-is; 6 are rescued by extraction”.
4. **“0/18 to 6/18 to 12/18”** (§13:547) mixes a valid count (0, 6) with an invalid count (12), so
   it reads as a third validity figure. It should be “0/18 valid raw, 6/18 valid normalised, 12/18
   still produce diagnostics (9 of them error-level)”.
5. **“Structural and semantic defects are present and invisible”** (claim 10) is not supported after
   A's own C05/C06/C07; the narrow instrument-silence claim is.
6. **The “inspection missed a third” framing** (claim 4) is selection-biased: the denominator
   includes the six records the tool surfaced, and A's subset excludes them as non-independent for
   detection. The factual finding (A missed them) is solid; the rate is not a miss-rate for
   inspection.
7. **The stale summary sections** (M-6): the banner, §1 table, §2 propositions 1/6/9, §5.3, §5.4,
   §12 and §16.8 all assert superseded values. Amendment A1 permits the original text to remain,
   but the reader-facing summary must carry a “superseded by §17” marker; at present the first
   screen says the 14-record population survives and the status table says “hashed before
   detection”.
8. **Minor numeric/label slips:** “81 `syntax` diagnostics” is 72 syntax + 9 reserved (m-6); “two
   pass human-style inspection” is not evidenced as two passes (the artefacts show an open pass,
   mechanical indicators and a coding pass); “three-way separation” lists four layers (§13:557).
9. **What is *not* overreach:** A explicitly refuses to claim a replication of the anchor, refuses to
   generalise beyond the corpus, states the generator = coder circularity, states the single-
   instrument limit, and reports the external arm descriptively without the 51.16 % comparison.
   Those are exemplary and should be preserved.

---

## 6. Process compliance

| Rule | Finding |
|---|---|
| **Gate 1 freeze** | `METHODOLOGY-FROZEN.md` hash `269d8dbe…` verified; prompts written 14:07:11Z, first raw 14:07:24Z, freeze claimed 14:05:30Z. Freeze precedes generation. Independence from B is asserted, not evidenced (no artefact can show it). **Pass on the record.** |
| **Write scopes** | A wrote only under `research/issue-007/**`, `reports/issue-007-*`, `research/relational/cross-reviews/A-reviews-B.md` and `research/relational/empirical-subset/**`. `A-reviews-B.md` remains `05ca64cc…`; no B artefact was edited. **Pass.** |
| **Validator not ground truth** | The post-inspection arm is validator-*surfaced* but spec-*verified*; the codebook rule (v1.2 §10.3) states the distinction and the records carry `discovery_route`. This is a disclosed near-miss, not a breach, but the arm is not an independent sample (m-1). The class T2 was added after the detection run (codebook v1.2) — disclosed in §11.3. **Pass with disclosed bias.** |
| **Second-coder independence** | One subagent, fresh context, no A labels, no validator; brief and file list recorded; model/raw copies byte-identical to canonical; coder CSVs byte-identical in both locations. **But** the codebook was an answer key (8/11) and the instruction sheet asserted the class criteria, including a false `by` rule. Procedural independence is not epistemic independence (A says so); the instruction channel is not disclosed. **Pass with a material qualification (M-5).** |
| **No git** | A says none; I cannot verify without running git (forbidden). **Not checkable.** |
| **Artefact stability** | B's Gate-2 boundary note stands: A's tree was not frozen at Gate 1, and the probes appeared during B's review. It recurred during Gate 3: while I was reviewing, `A-response-to-B-review.md` changed (its declared read/written times moved from 14:42/14:56Z to 14:23/14:29Z and a post-closure sentence was added), `CROSS-REVIEW-HASH.txt` was rewritten (A-response hash `c0528b36…` → `965924fe…`), the report changed (`3f0a8cfe…` → `f507ed49…` → `edf02fc6…`), the codebook was re-hashed (`fc476b1c…` → `106e620d…`), and `errors-combined.csv` moved from `21a75728…` (20 rows) to `56f4467a…` (19 rows) with C12. At my snapshot all self-recorded hashes match (I verified `CROSS-REVIEW-HASH.txt` and `CODEBOOK-HASH.txt`), so the final record is internally consistent. But a response declared “frozen” was edited, and a reviewer following an earlier hash would be reviewing different bytes. **Material process finding (P-1).** |
| **P3 empirical subset** | Created 14:33Z, after C12; `subset.json` correctly excludes `T1-C1-E01`, `T5-C3-P01` and the post-inspection batch; 13 error items (10 unqualified, 3 contested: I1, R1 ×2), 7 “controls”. Two risks for B: the 7 “controls” include **three models A's own note says are “NOT A CONTROL”** (T5-C3, T6-C1, T6-C3, all carrying post-inspection defects); and R1 is contested only as to **layer**, not as to **defect status**. If B scores these as negatives, specificity is understated. **Adjacent material finding for B, not for the #7 report.** |

**Verdict on process:** the protocol's investigative rules were followed in substance; the freeze,
write-scope and no-validator-as-truth rules are met or met-with-disclosure. The **hash-at-freeze**
mechanism was not used for `errors.csv`, and the **artefact-freeze** mechanism was not used for the
response/tree during Gate 3. Those are the two process failures the adjudicator should record.

---

## 7. Objection register (severity and what would settle each)

Severity: **blocking** = invalidates a headline claim or the anti-circularity guarantee; **material**
= changes a reported number, a conclusion's strength, or a third party's ability to verify; **minor**
= presentation/recomputable slip that changes no conclusion.

| ID | Objection | Severity | Evidence | What would settle it |
|---|---|---|---|---|
| **M-1** | The 9/14 detection result is presented as a blind-spot measure, but the five silent records are one withdrawn-as-legal plus four contested/discretionary/unestablished; after C12 it is 9/13, and 9/9 on established mandatory-report records. | **Material** | Report:106, 238–253, 281–287, 787; C12; catalogue rows `checkSatisfyRequirementUsageBindingConnector` (MAY), `validateFeatureEndMultiplicity`; C07. | A normative ruling on S2, R1 and I1 (spec clause, named constraint, or expert); then recompute the detection table on the established, mandatory-report subset. Artefact: codebook ruling + `detection/table.md` on the reduced set. |
| **M-2** | V1/V2 (6/12) is gate-dependent; three of the twelve “invalid” models are exit-0 warning-only; under the error-level gate A applied to the external arm, V1 = 9 and V2 = 9. | **Material** | `detection/summary.csv` T2-C2/T6-C1/T6-C3 (`exit_code=0`, `n_error=1`, `nonblocking_notation_only=yes`); report:46–47, 413–419; O12/§16.6. | Re-issue V1/V2 under both gates in the headline (no new data needed: the columns are in `summary.csv`); state the gate in §1, §7 and §13. |
| **M-3** | R1's re-layering does not establish that R1 is an error; the criterion conflates a feature with its instances and has no decisive constraint; the subset marks it contested only as to layer. | **Material** | `CODEBOOK.md:141–160`; `errors.csv` T4-C1-E02; catalogue `validateFeatureEndMultiplicity` (“if `isEnd`…”); C05/C06; `subset.json` `operational_criterion_R1`; report §16.4. | A normative clause/example showing a connector end through a multi-valued usage is ill-formed, or a SysML expert ruling; until then mark R1 `frozen_contested` (as a defect), and mark it as contested-as-defect in B's subset. |
| **M-4** | Codebook v1.3 is internally inconsistent: S2 body still says “mandatory clause omitted”; R1 table still says `structural/architectural`; S1 table still cites the old constraints. | **Material** | `CODEBOOK.md:33,34,39,78–87` vs §9/§11 and C05–C10; the second coder's S2 label follows the stale body. | Update the class table/body with dated “superseded” markers; re-hash; re-run `agreement.py` against the corrected codebook; diff. |
| **M-5** | The second coder was given an answer key (8/11 verbatim, 11/11 exemplar-covered) **and** an instruction sheet that asserts the S2/T1/N2/R1 criteria, including the false “requires `by`” rule; A's §16.5 omits the instruction channel and over-claims a W1 “dissent”. | **Material** | `coding/second-coder/CODEBOOK.md`; `coding/second-coder/INSTRUCTIONS.md:61–64`; `coder-b.csv` S2 row; A-response O5; report §16.5. | A held-out agreement run on the 24 external artefacts with exemplars removed and a neutral instruction sheet (no rule 6); report class agreement and CI. |
| **M-6** | The report's corrections are not integrated into its summary sections: banner/§1/§2/§5.3/§5.4/§12/§16.8 assert superseded values, and §2 still says “frozen and hashed before detection” and “because they are markdown”. | **Material** | Report:8, 39–50, 65–66, 98, 103, 106, 281–308, 532–540, 758–765 vs §17:769–810; README `coding/CODEBOOK.md v1.3 fc476b1c…` vs actual `106e620d…`. | Add a “current numbers” table and “superseded by §17” markers; update README hashes; use unique denominator labels (14/13/12; 9/14, 9/13, 9/12). |
| **P-1** | Artefact instability during Gate 3: the response, report, codebook, combined CSV and hash ledger changed while review was in progress; the response was edited after declaring itself frozen and its recorded hash changed. | **Material (process)** | Observed hashes: A-response `c0528b36…` → `965924fe…`; report `3f0a8cfe…` → `f507ed49…` → `edf02fc6…`; codebook `fc476b1c…` → `106e620d…`; combined `21a75728…` (20 rows) → `56f4467a…` (19 rows); `CROSS-REVIEW-HASH.txt` rewritten. The current response declares “frozen at 14:29Z” yet its final sentence describes C12–C13, which are dated 14:31Z — so by its own timeline the file was edited after the freeze, and the hash ledger labels the post-edit bytes as the 14:29 freeze. Current ledger is self-consistent otherwise. | Freeze the tree at Gate-2 close; publish an append-only hash ledger; corrections go to a dated addendum, not to a “frozen” response; reviewers pin a snapshot. |
| **m-1** | The “inspection missed a third” rate and the 15/19 combined detection rate are selection-biased: the post-inspection arm is validator-surfaced, and A's own subset excludes it as non-independent for detection. | Minor | Report:304–308, 787; `subset.json` `excluded`; §16.1. | Restate as counts (“inspection coded 14; the tool surfaced 6 further real notation defects”) and label 15/19 descriptive, not recall; or run an independent inspection on a held-out set. |
| **m-2** | The W1 “convention disagreement” is not a disagreement; both coders treat bare fences as W1, and the codebook's include clause is unambiguous. | Minor | `CODEBOOK.md:42–49`; `agreement.md` W1 note; `coder-b.csv` W1 rows; report:366–372; A's §16.5 “dissent”. | Show a bare-fence model A codes as non-W1 (none exists), or correct the “dissent”/“unresolved” wording. |
| **m-3** | `T6-C2-E01` records line 40 only, although the same unresolved `heating` occurs twice at line 42; the occurrence table (O11) omits T6-C2. | Minor | `errors.csv` T6-C2-E01; `diagnostics.csv` T6-C2 lines 40, 42×2; `occurrence_detection.csv` (four records, not T6-C2). | Add line 42 (two occurrences) to the record and to `occurrence_detection.csv`; re-run the detection count (record-level unaffected). |
| **m-4** | `agreement.py` hard-codes presence κ as `None` with the comment “constant marginals (every model has an error on both sides)”, which is false (9 error / 3 clean). | Minor | `agreement.py:141–142`; `agreement.json` `model_level_presence`; `agreement.md` table (3 clean). | Compute presence κ (pₒ = 1, pₑ = 0.625, κ = 1) or state why it is not reported; fix the comment. |
| **m-5** | Denominator labels collide: “9/13 = 69 %” means “14 − I1” in §16.3 and “14 − T1-C1” in §17.1; README still says “13 uncontested” and “N1 5”; `n_errors_post_inspection` holds the combined count. | Minor | Report:655, 710, 787; README headline bullets; `apply_corrections.py:105`. | Unique labels (e.g. 9/13[C12], 9/13[−I1]); rename the models.csv column; update README. |
| **m-6** | “81 `syntax` diagnostics” is wrong: raw diagnostics are 72 `syntax` + 9 `reserved-keyword-name`; “two-pass human-style inspection” is not evidenced as two passes. | Minor | `detection/diagnostics.csv` raw rows; report:44, 251, 304. | Correct the label to “81 raw diagnostics (72 syntax + 9 reserved)” and describe the inspection passes as recorded (open pass + indicators + coding). |
| **Adj-1** | The empirical subset's “7 controls” include three models A's own note calls “NOT A CONTROL”, and R1 is contested only as to layer; B's specificity measurement could be contaminated. | **Material for B's arm** (adjacent to #7) | `research/relational/empirical-subset/FROZEN-SUBSET.md` control table; `subset.json` `counts`/`excluded`. | Relabel the three as “known-defective, not controls” in the count; mark R1 contested-as-defect or exclude it from B's set. |

**Strongest two objections:** **M-1** (the detection gap is composed of the disputed records) and
**M-2** (the V1/V2 gate). Both are material, both are fixable from evidence already on disk, and
both change how a reader should interpret the pilot's two headline findings.

---

## 8. What I could not check, and why

- **The pre-detection hash / exact ordering.** No hash of `errors.csv` exists; mtimes were reset by
  re-runs/copies; the recorded UTC times were revised during my review. The composition argument is
  the only evidence, and it is inferential. (Unverifiable, not false.)
- **The original detection-run time.** The current `detection/raw/*.txt` were regenerated at
  14:28:49Z; no run log records the first run. The claim that `errors-post-inspection.csv` postdates
  it is author-asserted.
- **Generator turns / authorship.** `corpus/manifest.csv`'s `generation_timestamp_utc` is the raw
  file's mtime (`extract.py:106–107`), not a generation log; all 18 files were written within 32
  seconds. Whether each was a separate model turn cannot be checked from artefacts. A discloses the
  generator = coder circularity; it does not claim independent generation.
- **Search completeness for the external corpus.** I verified the 24 local files and their hashes,
  not that no other public corpus exists; “the only public corpus located” is a bounded-search
  claim, not a proven exhaustive one. I did not re-fetch the 24 upstream files (local hashes match
  A's manifest).
- **The second coder's reasoning.** Only its outputs are available; I can test the outputs against
  the models, not how it reached them.
- **The 691-page SysML 2.0 PDF's exact clauses.** I verified the catalogue constraint rows
  (`catalogue/classified.csv`) and independently fetched the `Actions.sysml` library line for C12
  (same sha256 A cites). I did not re-open the PDF to re-read §8.2.2.1.2 / §8.2.2.21.2; A's
  citations are consistent with the catalogue and the library, but the reserved-keyword list itself
  was not re-derived here.
- **The anchor studies' artefacts.** Not available; A correctly does not claim a replication.
- **“No access control was bypassed.”** No network log exists beyond the artefacts; the external
  files are public GitHub raw URLs. I found no contrary evidence, but the claim is not independently
  auditable.
- **The “two-pass” inspection.** No pass log; only `inspect.py` indicators, `_audit-view.txt` and
  `labels.py` exist.
- **Whether A saw B's work before the Gate-1 freeze.** Asserted in the freeze file; no artefact can
  establish it.

---

## 9. Adjacent questions noticed, not researched

- **#8 external arm (B's use of A's subset).** The subset's control labelling and R1's
  contested-as-layer-only status are material for B's specificity measurement (Adj-1). I did not
  evaluate B's mutants or harness; that is Reviewer B's scope.
- **#10 semantic ceiling.** The instrument's silence on S2/R1/I1 is a small, contested data point;
  whether any mechanism can check them is #10's question, not this review's.
- **#6 structure-imposing strategies.** The C2 pattern is a descriptive hypothesis at n = 1/cell; a
  task-stratified, repeated-generation design is needed.
- **#9 fidelity.** The T1-C3 75 % vs 55 % case is kept as an internal contradiction only; whether it
  is a fidelity defect is #9's question.
- **Gate-4 adjudication.** This review supplies verdicts and settle-criteria; it does not decide
  them. The adjudicator should use the pinned snapshot, not the moving tree.

---

## 10. Sources and reproduction commands

**Primary artefacts (pinned hashes in the header):** `reports/issue-007-error-taxonomy-pilot.md`;
`research/issue-007/{METHODOLOGY-FROZEN.md,AMENDMENTS.md,README.md}`;
`research/issue-007/corpus/{prompts.md,manifest.csv,extraction-log.json,extract.py,normalized/*}`;
`research/issue-007/coding/{CODEBOOK.md,errors.csv,errors-post-inspection.csv,errors-corrections.csv,errors-combined.csv,models.csv,omissions.csv,reconciliation.md,agreement.py,agreement.json,agreement.md,agreement-addendum.md,labels.py,apply_corrections.py,inspect.py,indicators.json,_audit-view.txt}`;
`research/issue-007/coding/second-coder/{BRIEF.md,INSTRUCTIONS.md,CODEBOOK.md,coder-b.csv,coder-b-models.csv,models/*,raw/*}`;
`research/issue-007/detection/{run_detection.py,summary.csv,diagnostics.csv,table.md,manifest.json,occurrence_detection.csv,raw/*,probes/*,external/*}`.
**Relational record:** `research/relational/PROTOCOL.md`; `gate-log.md`;
`cross-reviews/B-reviews-A.md`; `cross-reviews/A-response-to-B-review.md`;
`research/relational/empirical-subset/FROZEN-SUBSET.md` and `subset.json`.
**Catalogue / tooling:** `catalogue/classified.csv` rows `checkSatisfyRequirementUsageBindingConnector`
(8.3.21.10), `checkAttributeUsageSpecialization` (8.3.7.3), `validateFeatureEndMultiplicity`
(8.3.3.3.4), `checkConnectorTypeFeaturing` (8.3.4.5.3); `research/relational/TOOLING.md`;
`.tools/sysml -version` = OpenSysML `v0.12.1` (sha256 `ddfc2962…`).
**Independent retrieval for C12:** `https://raw.githubusercontent.com/Systems-Modeling/SysML-v2-Release/master/sysml.library/Systems%20Library/Actions.sysml`
(sha256 `ac36c9404cac347a2c12d4a0cb067b1a9cebcba6a1a1853eaa1f5b3fdeb15693`; contains
`action start: Action :>> startShot`).

**Commands run (on a copy under `/tmp/revA`, not in the repository):**

```bash
python3 research/issue-007/coding/agreement.py
python3 research/issue-007/coding/apply_corrections.py
python3 research/issue-007/detection/run_detection.py
shasum -a 256 <artefacts>                 # freeze, codebook, errors, detection, cross-reviews
diff <copied output> <committed output>   # agreement.md/json, errors-combined, models, reconciliation,
                                          # summary.csv, table.md, diagnostics.csv (path column only)
```

The detection re-run used the pinned `.tools/sysml` v0.12.1. No repository file was written by this
review.
