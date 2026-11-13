# Reviewer B — independent review of the issue #8 pilot (mutation-based evaluation of one validator)

**Reviewer:** Reviewer B (independent; did not produce the work under review).
**Author under review:** Researcher B, issue #8 pilot (`reports/issue-008-validator-reliability-pilot.md`,
`research/issue-008/**`).
**Question under review:** issue #8, *How reliable are SysML v2 validators as measuring instruments?* — the
pilot's answer, its evidence and its pre-registration discipline.
**Review frozen:** 2026-11-13T14:47Z. I will not edit this file after filing; corrections would be a new
dated record.
**Write scope used:** this file only. I edited no researcher artefact, no frozen file, no empirical-subset
file, and no other relational record.
**Status of my verdicts:** `supported` / `partly supported` / `not supported` / `unverifiable`. Only the
adjudicator can convert a verdict into an accepted or rejected challenge.

## 0. Independence, method, and what my verdicts rest on

- I read the protocol, gate log and tooling pin first, then issue #8 and (for framing only) issue #10.
- **No delegation, no subagents, no network retrieval of substantive evidence.** Every check below was run
  by me in this session.
- **The validator was used only to reproduce observations, never as an oracle.** I did not decide whether a
  mutant is defective by asking the tool; mutant validity claims are checked against the mutant text, the
  base text and the pinned specification, and where a specification constraint matters I quote the retrieved
  text (extraction of the hash-verified PDFs at `/tmp/sysml/`, whose sha256 I recomputed and which match
  `catalogue/README.md` §1).
- **I touched one researcher artefact, by re-running B's own documented analysis step** (task E requires
  it): `python3 research/issue-008/harness/analysis.py` rewrote `results/analysis.md`, `analysis.json` and
  `triage.csv` **byte-identically** (`diff` empty against pre-run copies). Content was not changed by this
  review; only mtimes moved. I did **not** run `empirical/run_external.py` (without `--verify-only`) because
  it would overwrite `raw/run2/**` and `results.csv`; see objection RB-07.
- Artefacts reviewed, pinned by sha256 so the adjudicator knows exactly what I read (all recomputed today):

| artefact | sha256 |
|---|---|
| `reports/issue-008-validator-reliability-pilot.md` | `41c743e7eda27fa0de678df67f28cbaefe2a2374bdc2ed105fb31487e2630fcc` |
| `research/issue-008/METHODOLOGY-FROZEN.md` | `2c80d63e8800be9ca67a051aaffdbc4b6c56c1b576002fc4446fe82862e6f00b` (matches `methodology.sha256`) |
| `research/issue-008/mutants/MANIFEST.csv` | `a9f479748aea10c76460421031a384ddda779d4c78ea1cb6a5fe2f208f157be7` (matches `expectations.sha256`) |
| `research/issue-008/results/analysis.md` | `ee630030d23baf07c150aa0a7962c783d7708184ca9c3315c75be0ea43b02d0f` |
| `research/issue-008/results/results.csv` | `6d96175857d4ceec91f38ef2e9928c3b55bdce96f6365fac43bf33adc5aab6c8` |
| `research/issue-008/results/triage.csv` | `e4db5f1a3f4550af8b3d85df5a7920728158f5ff4172156d49f3ce1d2d54815b` |
| `research/issue-008/results/known-good-triage.md` | `3feeb8c85636fb11fb6f9022da3eb5493eadc2ba0a82f309ab18fcc581b08901` |
| `research/issue-008/empirical/PRE-REGISTRATION.md` | `9458406e7db665ac42f5a3a896a7dc05b094b0fb6e8ef3a4ab9ed9db7e6acfbc` |
| `research/issue-008/empirical/REPORT.md` | `21252e16684928b1cb50707bb9f92dad323846f9bcae4288c64c864bf4130e8e` |
| `research/issue-008/empirical/results.csv` | `96e1b0b7272569218946db848ace85e2ebac4a8183a1fa2584dc665fd6c5a875` |
| `research/issue-008/empirical/run-log.md` | `a3fca89887bceb95207dcb4eaee4e3d2c337bd286721b1178a9c6ddc4fd4f1d4` |
| `research/issue-008/empirical/run_external.py` | `0ce7069f5cd4130b8745cbe2ccb121487aa57d37fa05ad3c2adeb949d377f30c` |
| `research/issue-008/README.md` | `ac2319303675d4e198de44a5fadee8f44088f2da2aedc3f83c6503f97cf55751` |
| `research/issue-008/second-validator-attempt.md` | `42734f965f567c2821f5fec200008e6d9202be22d2cadbcad2bfa3c9dedb4a67` |
| `research/issue-008/results/calibration/PRE-FREEZE-CALIBRATION.md` | `f911a42406c20d222424af0418088223b4819740dda95fecdda5a002c623261c` |
| `research/issue-008/results/run-log-run1.md` | `b8976ad7b8b2446d0f0626b3961c3a7051dd3f69b7a3d3643d784e742d4a6a5c` |
| `research/issue-008/results/run-log-run2-modes.md` | `7cd3703e765c73ea91482c378b325a92ae1aaedc7e4ae4274a8ba0b9917eac45` |
| `research/relational/empirical-subset/subset.json` | `bc2b92a5fdff6e976ae7156b13beba3535f0895e4a41268cf76c1551a6c3dfaa` |
| `research/relational/cross-reviews/A-reviews-B.md` | `05ca64ccaa4ceae4032ca36aa22f2090c5565449d021764a9da480bbbb1a8102` |
| `research/relational/cross-reviews/B-response-to-A-review.md` | `3ccbfce43320a870611479bdd127a9d1b5b37cfd3b8be98ff88b62cace2612bb` |

**Clock convention.** Filesystem times on this machine are local (UTC+1); B's scripts stamp UTC. Every
ordering statement below is from **filesystem** order converted by −1 h, which reproduces B's own recorded
UTC times for the artefacts that are self-stamped (e.g. the external `run-log.md` header 14:36:06Z vs its
mtime 15:36:37 local). Where B's *stated* times disagree with the filesystem I say so (RB-09).

## 1. Summary verdict

**The pilot's numbers reproduce, and its most important correction is real.** I re-ran the pinned binary
over all 42 models myself, recomputed every proportion and every Wilson interval, and re-ran B's analysis
script. The headline `23/32 = 0.72 [0.55, 0.84]`, the per-class table, `28/32` any-signal, `0/10` known-good
errors, the external `9/13`, the three denominator ladders, and the addenda that matter most (A2's
`-satisfy` detection of F7-02 **with a working positive control**, A3's `undecided`, A4's error-with-exit-0)
all reproduce exactly from raw artefacts. The pre-registration *ordering* that can be checked from the
filesystem holds for the synthetic arm: methodology hash before any mutant existed, expectation hash before
the first corpus run, and no post-run revision of the frozen expectation file.

**It is a good pilot whose bookkeeping is weaker than its measurements.** My verdicts are **23 supported, 9
partly supported, 10 not supported, 1 unverifiable** across 43 claims (§2). No objection I can substantiate
is *blocking*: nothing I found moves the headline or reverses a conclusion. The material objections are about
record-keeping and about one unresolved conceptual question, not about arithmetic:

1. **The external pre-registration's "frozen" hash is not a pre-run hash** (RB-01). `9458406e…` is the hash
   of the file *after* amendment AM1, which was written following the first external run; the `.sha256`
   file was regenerated at the same moment the amendment was appended, so the pre-run value was overwritten;
   and `run-log.md` §2's sentence that the two recorded versions differ "only in a header timestamp" is
   contradicted by AM1 sitting inside the hashed file. The *rules* were pre-registered; the *hash evidence*
   does not show it, and the log's own description of the difference is wrong.
2. **One headline-adjacent claim is used two ways** (RB-02). F4-01 (`part wheels[4..2]`) is counted as a
   *detection* in the sensitivity numerator while P5 cites the same error as the instrument being "stricter
   than the specification". Both cannot be right: if `[4..2]` is legal, that error is a spurious error on a
   legal model — which contradicts §3.3's "no case of a spurious error on a mutant" — and F4 becomes 2/4,
   `22/32`. The report never states which reading it adopts.
3. **The expectation audit cannot bear the weight put on it** (RB-03). `24/24` "expected-detectable produced
   some diagnostic" is near-tautological for a one-token edit, and B's own pre-freeze calibration log records
   that the validator was already observed to fire (`incommensurable-binding`, `metadata-metaclass`,
   `metadata-owning-type-feature`) on the very constructs that carry F6 and F8's "yes" expectations. The
   report's threat disclosure names only the `-explain` code list (report §4.1, L189–193; methodology §12.6),
   not the behavioural probes.

**What survives the addenda and should not.** A dozen strong sentences in the report body are still asserted
where the addenda have falsified them, and the repository index still says "nothing here was informed by
Researcher A's work" (§7). These are reader-facing, not numeric: a reader who stops at §1 or the README gets
a claim its own addenda retract.

**Where I disagree with the filed cross-review.** Researcher A's O1 was correct and B's acceptance was
correct; I verified both. But A's review did not test the external arm (not available at the time), did not
audit the calibration log against the expectation audit, and accepted the KG-04 over-reach judgement; on
those three points B's evidence is weaker than A assumed (§6, §8, RB-03, RB-04, RB-06). I also record one point
*in B's favour* that A could not test: the P5 strictness claim holds against the retrieved KerML text
(§3.3, C7).

## 2. Claim-by-claim

Verdicts are mine. "Evidence" names the artefact and line I checked, and the check I ran. Line numbers are
to the artefact named, as read today.

| # | Claim (location) | Verdict | Evidence / my check |
|---|---|---|---|
| C1 | Primary measure: relevant error-severity detection **23/32 = 0.72, 95% Wilson [0.55, 0.84]** (report L27–28; analysis.md L9) | **supported** | I re-ran `.tools/sysml -validate -format json` over all 32 mutants: 23 produce ≥1 error, matching `results.csv` row-for-row. Wilson recomputed independently: 23/32 → [0.55, 0.84]. |
| C2 | Per-class rates F1 4/4, F2 4/4, F3 2/4, F4 3/4, F5 3/4, F6 3/4, F7 0/4, F8 4/4 (report L89–96; analysis.md L19–26) | **supported** | Re-running `harness/analysis.py` regenerated `analysis.md/.json/triage.csv` byte-identically; each class count reconciles with `results/diagnostics.csv`. Wilson intervals recomputed for every cell and match to 2 dp. |
| C3 | Any-signal **28/32 = 0.88 [0.72, 0.95]** (report L97) | **supported** | 32 − 4 F7 (no diagnostics at all) = 28; reproduced from raw and from `diagnostics.csv`. |
| C4a | **Default path**: F7 error-severity detection 0/4 = 0.00 [0.00, 0.49] (report L95, A2 L518–519) | **supported** | All four F7 mutants return `status: holds`, zero diagnostics, exit 0 under `-validate`; reproduced. |
| C4b | "It **detected none of the four structural/architectural defects** … all validated cleanly" (report L32–34) and P3 "invisible to the only available instrument — Established" (L65) | **not supported** as written (corrected by A2 L473–521, A3 L525–547, but not in the body) | I reproduced `-satisfy` on F7-02 → `standing: violated`, exit 1; base KG-07 → `holds`, exit 0. F7-04 → `undecided`, exit 2. So one is detected, one checked-undecided, two no verdict in any mode tested. |
| C5 | Known-good arm: **0/10 error-severity false positives**, 1/10 warning (report L172–177) | **supported** | I re-ran all 10 models: 9 clean, KG-04 one `warning[name-conflict]@17`; no errors. Independently reproduces. |
| C6 | KG-04's warning is over-reach on a specification-verbatim example (report L173–177; known-good-triage.md L38–65) | **partly supported** | The line *is* verbatim from §7.13.4 p.72 (verified in the hash-matched PDF text). But "over-reach" requires that a same-named member in a specializing definition is a legal implicit redefinition; the KerML text I retrieved permits the same name only for an *owned* redefinition (`kerml-1.0.txt` 2666–2670, 2686–2698), and SysML §7.6.3 presents `:>>`/`redefines` as how redefinition is declared. The scenario is therefore plausible-but-not-established, and the promised settling retrieval is mis-targeted (§7.6.1 is "Definition and Usage Overview"). B does state the reservation (triage L57–60); §3.6's "does not deserve" is stronger than the triage. |
| C7 | P5: `[4..2]` reported as an error although **no catalogue constraint forbids it** (report L67, L161–168) | **supported** | Retrieved KerML text: `validateMultiplicityRangeBoundResultTypes` constrains bound *typing* (`ScalarValues::Integer`) and non-negativity (14372–14381); `validateMultiplicityRangeBounds` constrains the *owned-member order* (14384–14396). Neither forbids lower > upper. This survives a challenge I expected to succeed against B. |
| C8 | P4: "Some specification-named **SHOULD** constraints are not enforced" (report L66) | **supported for the first example; partly for the second** | `validateFeatureValueOverriding` (KerML 14212–14219) is instantiated by F5-01 and the model validates with only the base's `name-conflict` warning. The second example, `validateFeatureEndMultiplicity`, *was* reported, as a warning — and the tool's own `-explain` documents that code as `warning`. "SHOULD-report" is correctly sourced (KerML §8.3.1 taxonomy: "should report violations of validation constraints"); severity is not graded by the spec, so "not enforced" is the wrong phrase for that one. |
| C9 | Methodology hash computed **before any mutant existed** (report L50/L56; gate log Gate 1) | **supported** | `METHODOLOGY-FROZEN.md` mtime/birth 14:08:59/14:08:53; first `known-good` model 14:09:14; first mutant 14:12:13. `methodology.sha256` verifies OK against the current file. |
| C10 | MANIFEST hash computed **before the first corpus run** (report L51/L56) | **supported** | `expectations.sha256` written 14:13:00; first raw output `results/raw/run1/known-good/KG-01-parts.json` 14:13:02; `raw-run1.json` 14:13:03. Both sha files verify OK today. |
| C11 | "**No expectation was revised**" (report L57) | **partly supported** | The frozen file verifies against the pre-run hash, so **no post-run revision of the frozen content** occurred — that part is supported. But report §10 (L337–341) says a layer expectation was "reorganis[ed]" after the construct "turned out to be caught by the *typing* layer", and the methodology/FREEZE require a `MANIFEST-REVISIONS.md` for any revision; no such file exists. The absolute wording is stronger than the record can support. |
| C12 | Expectation audit: 24/24 expected-detectable produced a diagnostic; 19/24 an error; both expectation errors in the "undetectable" bucket (report L240–245; A8 L694–712) | **partly supported** | Arithmetic reproduces (`analysis.md` §5). As *evidence that the expectations were unfitted* it is weak: "some diagnostic" is near-guaranteed by a one-token edit, and the calibration log shows detection was already observed for F6/F8-type constructs before expectations were authored (§3.6, RB-03). |
| C13 | A8: "30 error diagnostics over 28 signalling mutants; **24 of 28 produce exactly one**" (report L725) | **not supported** | Recomputed from `results/diagnostics.csv`: distribution is 1 diagnostic → **23** mutants, 2 → 3, 3 → 1, 5 → 1 (28 total); 20 of the 23 error-bearing mutants produce exactly one *error*. "24 of 28" is off by one under either reading. No headline depends on it. |
| C14 | "5 **silent**" (analysis.md L12) and F5 "detected:3, **silent:1**" (analysis.md L23; report H3 L224) | **not supported** | F5-01's raw output (`results/raw/run1/mutants/M31-F5-01-feature-value-overriding.json`) contains `warning[name-conflict]` at line 17. Methodology §8 (L209) defines silent as "zero diagnostics of any severity". Correct split: 4 silent + 1 incidental. It is also internally inconsistent with the same page's "any-signal 28/32", which *includes* F5-01. Primary measure unaffected. |
| C15 | "Every emitted **error** was about the injected defect … no case of a spurious error on a mutant" (report L120–122) | **not supported** under the report's own P5 reading | 23/32 any-error = 23/32 relevant-error is arithmetically true, but if `[4..2]` is legal (P5) then `error[multiplicity-range]` on F4-01 is a spurious error on a legal model. The two statements are incompatible; see RB-02. |
| C16 | `spec_status` "was fixed before the run, not chosen to fit the outcome" (report L126–127) | **partly supported** | The MANIFEST *text* was frozen; the six-bucket `spec_status` is a hard-coded post-hoc dict in `harness/analysis.py` (L91+) and is not a column of the frozen MANIFEST. The buckets are transparent and checkable, but the sentence overstates their provenance. |
| C17 | A2: F7-02 is **detected** by `-satisfy` / `-instantiate -validate=`, with a positive control (report L484–495) | **supported** | Reproduced `-satisfy` live with my own argv: mutant → `✗ … fails`, `standing: violated`, exit 1; base KG-07 → `holds`, exit 0. The saved `-instantiate -validate=` raw pair shows the same discrimination (mutant `violated`, base `holds`); I read both. This was the blocking objection and it is properly remedied. |
| C18 | A3: F7-04 is **checked and undecided**, not silent; the five-valued standing (report L525–547) | **supported** | Raw `run2-modes/…F7-04__instantiate-validate.stderr.txt` shows "2 of 2 assertions undecided … standing: not covered"; the base shows 1 of 1 undecided. B's refinement (undecided does not discriminate mutant from base) is correct and is the honest reading. |
| C19 | A4: `error[reserved-keyword-name]` can carry **exit 0**; `-strict` converts to exit 2 (report L551–585) | **supported** | Reproduced on `results/probes-gate2/P1-reserved-keyword-name.sysml`: default exit 0 with `error[reserved-keyword-name]`; `-strict` exit 2. The tool's `-explain` confirms the code exists at error severity. |
| C20 | A9: MANIFEST was rewritten **after** the run by re-running the author's own reproduce step; content unchanged (report L732–750) | **supported**, and one detail is wider than A9 says | MANIFEST mtime 14:15:56 vs run 14:13:03; `shasum -c expectations.sha256` OK today. However **the 32 `mutants/*.sysml` files also carry the 14:15:56 mtime** (birth 14:12:13), so the reproduce step also rewrote the mutant files; `mutants.sha256` verifies OK, so content is unchanged. A9 mentions only `author_manifest.py`. |
| C21a | Synthetic harness: raw output "written once and never rewritten … exclusive file creation" (README L36; `run_validators.py` L101–105) | **supported** | Code uses `open(..., "x")` with per-run directories. |
| C21b | External harness: "Raw output is written once and **refused if it already exists**, so a cited run cannot be edited in place" (`run_external.py` docstring) | **not supported** | The code uses `Path.write_text(...)` with `mkdir(..., exist_ok=True)`; a second run with the same `--run-id` silently overwrites `raw/run2/**`, `results.csv` and `run-log.md`. The anti-tamper property it claims is not implemented. (I did not execute it, for that reason.) |
| C22 | External arm: default path **9/13 = 0.69 [0.42, 0.87]** (empirical REPORT L43; report A10.1 L769) | **supported** | I re-scored all 13 items from `raw/run2/*__M1.stdout.txt` with the pre-registered line-range rule: 9 detected, 2 silent, 2 wrong-target. |
| C23 | Denominator ladder 9/13 → 9/12 (without contested I1) → 9/11 (and the short-circuited item) (report L769–771; empirical REPORT L43–45, L183–185) | **partly supported** | The arithmetic is right and the registered number is retained (honest use of "unmeasurable": the excluding steps are disclosed and the other R1 item remains a clean silent miss). But the two documents label the *first* exclusion differently: empirical REPORT §1 excludes I1 first, §6.1 excludes the short-circuited item first. Same denominators, different provenance — a reader cannot tell which ladder step is which. |
| C24 | External M2/M3 accounting: "**1 item evaluated**, 10 not applicable" (report L784–785; empirical REPORT L46–47) | **not supported** | `empirical/results.csv` has 3 evaluated items in each of M2 and M3 (M2: S2 `not detected`, I1 and T4-C3 `wrong-target`; M3: 2 `not detected`, 1 `weaker signal`), 10 n/a. The count 1+10=11 does not sum to the stated denominator 13, and contradicts the same report's §11.2 / addendum L843 ("applicable to 3 items each"). |
| C25 | External scoring applies pre-registration §4.2 (non-satisfy-family item ⇒ `not applicable`) | **not supported** | `run_external.py` L222–231 returns `wrong-target` for non-satisfy-family M2 items; §4.2 (`PRE-REGISTRATION.md` L102–107) says such an item "is `not applicable`". Two items and six controls carry the item-attribution vocabulary the amendment said controls must not use (AM1 item 3). No detection count changes. |
| C26 | One external "miss" is **unmeasurable** because the tool states it made no check (empirical REPORT §6.1; report A10.5 L845–848) | **supported** | The raw JSON contains `"… did not analyse cleanly; no check was made"` (I printed the full envelope). B quotes it accurately and keeps the registered score. |
| C27 | "The **layer** picture survives but the **class/aggregate** do not": mapped 9/10 vs 13/16; five layers, four agree, one disagrees on n=1 (empirical REPORT §4, L118–134; report A10.2 L789–806) | **supported with the stated caveats** | The numbers are right (I recomputed 9/10, 13/16, and all five layer rows). The word "survives" is defensible as *reproduction of the layer boundary*, not as equality of layer rates: notation and resolution agree by both being fully detected, and the constraint layer's disagreement is n=1. B states both caveats. |
| C28 | P6 not supported by the pre-registered decision rule; P8 weakened not settled (report A10.3 L808–824; empirical REPORT §8) | **supported** | The rule is in `PRE-REGISTRATION.md` §8 (L180–191), the observed mapped rate (0.90) is *higher* than synthetic (0.81), and B reports that as unflattering to its own pilot. This is exactly the discipline the protocol asks for. |
| C29 | External controls: 0/4 error, 0/4 warning on the clean tier; 3 frozen-clean-only reported, not scored (report A10.4 L826–833; empirical REPORT §5) | **supported** | Raw M1 for the four controls: zero diagnostics. The three frozen-clean-only models carry the verified post-inspection defects (`usage-typing@11`, `reserved-keyword-name@26` twice). |
| C30 | External pre-registration "frozen at `9458406e…` **before the first run**" (report L761; empirical REPORT L6–7; PRE-REGISTRATION L4) | **not supported as a statement about that hash** | See §3.4. The hashed file contains AM1, written after run1; the `.sha256` was rewritten at the amendment (mtime = the amended file's mtime, both after run1). The pre-run hash was not preserved. |
| C31 | "No item changed from detected to not-detected or the reverse" between external run1 and run2 (run-log §6; README L57) | **supported** | I re-scored `raw/run1` and `raw/run2` M1 independently: identical 9-item detected set, zero differences. `grep -r "violated" raw/` returns nothing in either run, so the M2/M3 claim "no raw file contains `standing: violated`" is also true. |
| C32 | Second-validator attempt: no JVM, no build tool, **no CLI release asset**; the Jupyter kernel is the only executable surface (second-validator-attempt.md) | **supported** | Reproduced locally: `java -version` and `/usr/libexec/java_home` fail, no `mvn`/`gradle`. Re-queried the GitHub releases API read-only: tag `2026-09.1`, published `2026-10-28T18:20:13Z`, **12 assets, same names and byte counts, no CLI/jar bundle**. |
| C33 | Frozen files byte-identical today (all four sha files) and the empirical subset untouched | **supported** | `shasum -a 256 -c` OK for `methodology.sha256`, `mutants/mutants.sha256`, `mutants/expectations.sha256`, `empirical/PRE-REGISTRATION.sha256`; `subset.json`, `models/manifest.csv` and all 36 frozen model copies match their recorded hashes **and** are byte-identical to A's live corpus (verified per file). |
| C34 | README: "**No empirical challenge set** … deliberately absent; **nothing here was informed by Researcher A's work**" (README L97–98) | **not supported** | `research/issue-008/empirical/**` exists, is listed in the same README (L53–59), and addenda A1–A10 record A's influence. The file was last written *after* A10 (mtime 14:38:19 vs report 14:38:04) and still carries the stale section. |
| C35 | One-instrument framing: "the one-instrument limitation is not a caveat, it is the boundary of what this pilot measured" (report L16–21, §8 L279–281, §9) | **supported** | The framing is adequate and repeated in the methodology, the second-validator log and the external report. Residual: §11.1's bold sentence ("A validator pass is evidence about four layers and no others") is phrased generally before the qualifier "For this instrument". |
| C36 | A2's runs happened "2026-11-13T14:31–14:36Z" (report L484; B-response §2.2) | **not supported** | Raw `run2-modes/**` mtimes are 14:24:50–14:26:00Z and B's own `run-log-run2-modes.md` header says "Written … at 2026-11-13T14:24:51Z". The stated window is 6–11 minutes late. No consequence for the results. |
| C37 | Known-good corpus "independent of the mutant generator and of the tool's own tests" (issue #8 criterion; methodology §5) | **partly supported** | 9/10 are Type S quotations from the hash-verified PDF (I verified KG-04's block and KG-09's block verbatim) and 1 is labelled Type A; the four cited clauses I spot-checked are accurate. But the 10 models are **also the mutant parents** (KG-01 alone is the base of 9/32 mutants), the same agent authored bases and expectations, and the corpus was iterated to tool-silence before the freeze (two pre-freeze firings, both tool-correct). Independence from the tool's own test suite is not checkable here (no test suite on disk). |
| C38 | KG-09: the specification's own §7.17.2 example contains an unresolved reference (`bind picture = focus.picture;` while `focus` declares `out image`) (report L178–183; KG-09 PROVENANCE L28–38) | **supported** | Retrieved PDF text at the cited clause: the example reads exactly that, and the `action focus` line declares `out image`. B repaired it by one token and reported it as an observation about the source material, not as a tool finding. |
| C39 | "No delegation. No subagents were spawned" (report §7 L265–269) | **unverifiable** | Nothing in the artefact tree can prove or disprove agent provenance; the single-context style is consistent with the claim. I record it as unverifiable rather than accepted. |
| C40 | Methodology §4: expectations "authored from the specification and the model text only"; the reason "never instrument-side-observed" (L113–121) | **partly supported** | The MANIFEST *rationales* I read (F4–F8) are spec-side, as required. But the pre-freeze calibration log (14:06–14:08Z, before the methodology freeze) records construct-level detection results — `q1`: `incommensurable-binding` error; `m1`: `metadata-metaclass`; `m2`: `metadata-owning-type-feature`; `t1`: `bound-feature-types` warning — that directly pre-determine the F6 and F8 "yes" expectations. Formally compliant, substantively informed. |
| C41 | `-explain` disclosure: the report states the author had seen the code inventory and treats the audit as softer evidence (report §4.1 L189–193; §8.6; A8 L694–712) | **supported as a disclosure, incomplete as a description** | The disclosure exists and is candid about direction. It names only `-explain`; the calibration log's behavioural probes are the larger source of prior knowledge and are not named in the report (§3.6). |

**Tally (43 rows):** supported 23 (C1, C2, C3, C4a, C5, C7, C9, C10, C17, C18, C19, C20, C21a, C22, C26,
C27, C28, C29, C31, C32, C33, C35, C38); partly 9 (C6, C8, C11, C12, C16, C23, C37, C40, C41); not supported
10 (C4b, C13, C14, C15, C21b, C24, C25, C30, C34, C36); unverifiable 1 (C39). Four rows carry two verdict
shades in their wording (C8, C23, C40, C41) and are counted at the stronger failing verdict.

## 3. Pre-registration audit

### 3.1 Verified hashes (all recomputed today, all OK)

| artefact | hash | relation to the run |
|---|---|---|
| `METHODOLOGY-FROZEN.md` | `2c80d63e…6f00b` | written/frozen 14:08:53–59; **before** first known-good model (14:09:14) and first mutant (14:12:13) |
| `mutants/MANIFEST.csv` | `a9f47974…57be7` | content hashed 14:13:00; first raw output 14:13:02 |
| `mutants/*.sysml` (32) | `mutants.sha256` | written 14:13:00; first raw output 14:13:02 |
| `harness/author_manifest.py` | `40c75cef…84432` | in `expectations.sha256`, pre-run |
| `empirical/PRE-REGISTRATION.md` | `9458406e…6acfbc` | **amended after run1** (AM1); see §3.4 |
| `empirical/PRE-REGISTRATION.sha256` | contains `9458406e…` | **rewritten at 14:36:04**, i.e. after run1 (14:35:38–41) |
| `relational/empirical-subset/subset.json` | `bc2b92a5…c3dfaa` | frozen 14:33:20; first external run 14:35:38 |
| `relational/empirical-subset/models/**` (36) | per-row | all match, and byte-identical to A's live corpus |

### 3.2 Timeline (filesystem, converted −1 h)

```
14:06–14:08  PRE-FREEZE-CALIBRATION probes (10 instrument probes; -explain read)
14:08:53/59  METHODOLOGY-FROZEN.md written and hashed
14:09:14     first known-good model
14:12:13     first mutant
14:12:54     MANIFEST.csv created
14:13:00     expectations.sha256 + mutants.sha256 written
14:13:02-03  first validator run over the corpus (raw/run1, raw-run1.json)
14:15:56     MANIFEST.csv and mutants/*.sysml rewritten (idempotent reproduce step; content unchanged)
14:22:13     A-reviews-B.md filed
14:23:19     B-reviews-A.md filed
14:24:47-14:26:00  Gate-2 per-mode probes (run2-modes, probes-gate2)
14:33:13     A-response-to-B-review.md filed
14:33:20     empirical subset frozen (A)
14:35:13/15  external PRE-REGISTRATION.md written and hashed
14:35:38-41  external run1
14:36:04     PRE-REGISTRATION.md **amended (AM1)** and .sha256 **rewritten**
14:36:04-06  external run2 (the run the numbers come from)
14:37:43     empirical/REPORT.md written
14:38:04     pilot report last written (A10); 14:38:19 README last written
```

Two orderings the gate depends on hold: **methodology before mutants** and **MANIFEST before the corpus
run**. The external arm's ordering holds for the *rules as amended* but **not for the recorded hash** (§3.4).

### 3.3 AM1 — legitimate pre-scoring correction, or a fitted degree of freedom?

AM1 (`PRE-REGISTRATION.md` L227–251) makes three changes after run1 and before any result was scored:
(1) M4's argv gains `-format json`; (2) verdict modes become `not applicable` instead of `not detected`
where the model does not analyse cleanly; (3) controls get model-level labels instead of item-attribution
labels.

Assessment:
- **None of the three can inflate detection.** (1) is serialisation; (2) moves items *out of* "not
  detected" into "not applicable", i.e. it reduces the claimed applicable denominator; (3) is labelling.
  Verified consequence: run1 → run2 changed **no** M1 detection outcome (my independent re-score of both
  runs gives the identical 9-item set) and no M2/M3 standing reaches `violated` in either run.
- **(1) is nevertheless a change to a registered invocation.** §3 of the pre-registration fixes M4's argv
  as `sysml -validate -strict <model>`; adding `-format json` is a deviation from a frozen rule, recorded
  as an amendment rather than a new run under the old rule. Because the detection *criterion* is the
  diagnostic and not the exit code, the practical effect is nil — but the amendment is a post-hoc edit to
  the registered design, and M4's run1 record is therefore not a run of the registered procedure.
- **(2) is not neutral in one respect**: it makes the M2/M3 arms look *less* like a failure. The
  conservative direction is real, but an adjudicator should note that the amendment runs in the tool's
  favour and was made by the same agent who then reports "0 detected".
- **The real defect is evidential, not substantive**: AM1 was appended *inside* the frozen file, and the
  `.sha256` was regenerated in the same instant (both mtimes 14:36:04). The pre-AM1 hash is therefore lost,
  so "no rule changed" is an assertion, not a checkable claim. A separate AM1 file, with the pre-run hash
  left in place, would have cost nothing and preserved the chain.

**Ruling: legitimate in direction, defective in record.** Not a fitted degree of freedom in effect; a
process failure in evidence.

### 3.4 The two pre-registration hashes

Two hashes are recorded in `empirical/run-log.md` §2:
`0106e08276103e9afbfa6d37015f04f57d2f1a5fc0a4976feb22c2555254f6f2` ("first draft") and
`9458406e…6acfbc` ("**frozen**, the version this run implements"). What can be checked:

- The draft file **does not exist**; the draft hash is asserted in a **script-generated** log (the hash is a
  literal in `run_external.py` L273), so the claim that the draft differs "only in a header timestamp" and
  that "no rule, mode, expectation or scoring definition differs between the two versions" is
  **unverifiable**.
- The "frozen" hash `9458406e…` is the hash of the file **containing AM1** (`PRE-REGISTRATION.md` L227–251),
  which was written *after* run1 ("The first execution … completed, and its output revealed three
  defects"). So `9458406e…` cannot have existed before the first run.
- The `.sha256` file's **birth** is 14:35:15 (before run1) but its **mtime** is 14:36:04 — the same instant
  as the amendment — so whatever value it recorded at freeze was overwritten.
- Consequently `run-log.md` §2's sentence ("No rule … differs between the two versions; only the header
  timestamp and a note were changed, **before the first run**") is **contradicted by the hashed file's own
  contents**: between the draft and `9458406e…` there is an amendment that changed three derivation rules
  after the first run.

**Verdict:** the external pre-registration's *content* is credible (the amendments are disclosed, dated,
conservative, and the M1/M2/M3 outcomes are identical between runs), but the *hash chain that is offered as
proof of pre-registration does not establish it*, and the log's description of the difference between the
two recorded versions is wrong. This is material and remediable: publish the pre-AM1 file or its hash.

### 3.5 "Run1 and run2 detected sets are identical" and "no raw file contains `standing: violated`"

Both claims are **true**, verified independently:
- I re-scored `raw/run1/*__M1.stdout.txt` and `raw/run2/*__M1.stdout.txt` against the frozen line ranges:
  9 detected in each, **zero items differ**.
- `grep -rn "violated" empirical/raw/` returns **nothing** in either run, so the M2/M3 claim is literally
  true (though note that "not violated" is a weak statement given that 10 of 13 items were not applicable —
  see C24/C25).

The run-log's own claim that the differences are "M4 becomes measurable, and roughly twenty rows are
relabelled" is consistent with the CSVs. This is the strongest part of B's external-arm bookkeeping.

### 3.6 Pre-freeze calibration — the disclosure that matters

`results/calibration/PRE-FREEZE-CALIBRATION.md` (14:06–14:08Z, before the methodology freeze) records
**ten validator probes**, and four of them are construct-level detection observations, not interface
observations:

| probe | observation recorded | what it pre-determines |
|---|---|---|
| `q1.sysml` | `incommensurable-binding` fires as **error**; `quantity-unit` as warning | F6's `expected_detectable = yes` |
| `m1.sysml` (`@SafetyCase` on a `part def`) | `error[metadata-metaclass]` | F8-01's `yes` |
| `m2.sysml` (`levl` typo in metadata body) | `error[metadata-owning-type-feature]` | F8-02's `yes` |
| `t1.sysml` | `warning[bound-feature-types]` | the "wrong severity" outcome and F3/F8 expectations |
| `t3.sysml` (`Engine[2]`) | no diagnostic; "explicit multiplicity alone is not a defect" | the shape of all four F4 mutants |

The calibration file says explicitly that this "is a threat to validity for the pre-registered
expectations". The **report** (L189–193), the **methodology** (§12.6) and the **gate log** name only the
`-explain` code list; the gate log characterises the probes as establishing "output shape, exit codes and
short-circuit behaviour". That is narrower than what the file records.

**Consequence for the audit, not for the numbers.** The detection counts (23/32) are computed from raw
diagnostics and are insulated. But `24/24` is close to a re-run of the probes for the classes the probes
touched. The honest reading is B's own sentence in A8, *plus* "and several of the 'yes' predictions were
made after seeing the same mechanism fire on a probe". What is genuinely unpredicted is the two errors
(F4-01, F6-02) — and both err in the "tool stricter than predicted" direction, which is the direction a
spec-anchored forecast should err. So the audit is weak evidence, not fitted evidence.

## 4. Mutant audit

I diffed **all 32** mutants against their bases (`diff -u`), not a sample, and read the eight classes. Table
below records every mutant; the "single defect" column is my reading of the diff, not B's rationale.

| mutant | base | diff | one deliberate defect? | instantiates claimed class? |
|---|---|---|---|---|
| F1-01 missing-semicolon | KG-01 | `part engine : Engine` (semicolon deleted) | yes | yes — parse break |
| F1-02 extra-brace | KG-05 | one `}` appended | yes | yes — parse break |
| F1-03 keyword-typo | KG-02 | `port` → `prot` | yes | yes — parse break |
| F1-04 unquoted-shortname | KG-07 | `<'1.1'>` → `<1.1>` | yes | yes — notation conformance (5 cascade syntax errors) |
| F2-01 type-typo | KG-01 | `Engine` → `Engin` | yes | yes — unresolved type |
| F2-02 parameter-typo | KG-09 | `scene` → `scne` in a binding | yes | yes — unresolved expression reference |
| F2-03 redefinition-typo | KG-07 | `massActual` → `massActul` at `:>>` | yes | yes — unresolved redefinition target |
| F2-04 missing-declaration | KG-01 | `part def Wheel;` deleted | yes | yes — undeclared type |
| F3-01 part-typed-by-portdef | KG-02 | `port fuelOutPort` → `part fuelOutPort` | yes | yes — part typed by a port definition |
| F3-02 attribute-typed-by-partdef | KG-08 | `MassValue` → `Vehicle` | yes | yes — attribute typed by a part definition (same condition A recorded independently as T2) |
| F3-03 state-replaced-by-action | KG-06 | `state on` → `action on` | yes | **adjacent, not identical**: the *declaration kind* changes, and the reported condition is "transition endpoint is not an action node"; the class says "usage typed by a definition of the wrong kind", which this is not literally |
| F3-04 subject-typed-by-requirement | KG-07 | `Vehicle` → `MaximumMass` | yes | yes — subject typed by a requirement definition |
| F4-01 inverted-bounds | KG-01 | `[4]` → `[4..2]` | yes | **contested** — instantiates a *range inconsistency*, not any named constraint; whether it is a defect at all is exactly RB-02 |
| F4-02 end-feature-multiplicity | KG-03 | `Hub` → `Hub[2]` on an `end part` | yes | yes — verified against KerML 10955–10961 ("must have multiplicity 1..1") |
| F4-03 non-natural-bound | KG-01 | `[4]` → `[0.5]` | yes | yes — verified against KerML 14372–14381 |
| F4-04 feature-value-count | KG-04 | **one line, two changes**: `[1..*]` → `[1]` and a 2-element value appended | **no, strictly**: the multiplicity change is a second semantic change, needed to construct the count violation | yes for the intended condition; the manifest rationale does not flag the composite edit |
| F5-01 feature-value-overriding | KG-04 | `default` deleted on the supertype's `cutoff` | yes | yes — verified against KerML 14212–14219; the subtype's `default =` now overrides a bound value |
| F5-02 satisfy-reference | KG-07 | `vehicleMaximumMass` → `Vehicle` | yes | yes — satisfy target is a definition |
| F5-03 decision-node-incoming | KG-09 | one succession added into `decision1` | yes | yes — verified against `validateDecisionNodeIncomingSuccessions` (catalogue row, SHOULD) |
| F5-04 composite-port-feature | KG-02 | `part fuelLine : Fuel;` added inside a `port def` | yes | yes for the prose-only §8.4.8.1 condition (B's 'uncertain' was well placed) |
| F6-01 wrong-dimension-unit | KG-08 | `[m/s]` → `[kg]` | yes | yes |
| F6-02 missing-unit | KG-08 | `[kg]` deleted | yes | yes (the tool's Rational-vs-MassValue error is a genuine type-conformance failure) |
| F6-03 incommensurable-sum | KG-08 | `0.5*mass*speed*speed` → `mass + speed` | yes | yes |
| F6-04 wrong-product-dimension | KG-08 | … → `mass * speed` | yes | yes |
| F7-01 unreachable-state | KG-05 | `first off then starting;` deleted | yes | yes — reachability |
| F7-02 satisfied-but-violated | KG-07 | `1500.0` → `2500.0` | yes | yes — and it is checkable, which is why the instrument can decide it |
| F7-03 missing-flow | KG-09 | `flow focus.image to shoot.image;` deleted | yes | yes — supplier missing for `shoot.in image` |
| F7-04 contradictory-assertions | KG-10 | `assert constraint { computedMass < 0.0 }` added | yes | yes — contradiction with the existing `>= 0.0` |
| F8-01 annotation-not-metadata | KG-01 | `@SafetyRelevant { level = 3; }` → `@Engine { }` | **one line, two changes** (name and body) | yes — a part definition is not a metaclass |
| F8-02 body-feature-typo | KG-01 | `level` → `levle` | yes | yes |
| F8-03 value-kind | KG-01 | `level = 3` → `level = "high"` | yes | yes — value-kind conformance inside metadata |
| F8-04 abstract-metaclass | KG-01 | `metadata def` → `abstract metadata def` | yes | yes — verified against `validateMetadataFeatureMetaclassNotAbstract` |

**Structural findings a reviewer should carry.**

1. **Base concentration.** 9 of 32 mutants (28%) are edits of one 23-line model (KG-01): the whole of F8,
   plus F1-01, F2-01, F2-04, F4-01, F4-03. KG-07 5, KG-08 5, KG-02 3, KG-09 3, KG-04 2, KG-05 2, KG-03 1,
   KG-06 1, KG-10 1. The top three bases carry 19/32. The methodology says mutants "are not independent of
   each other" (§4.5) but does not quantify it; the per-class table therefore inherits a cluster structure
   that the Wilson intervals do not represent.
2. **Class diversity is uneven.** F3 and F7 sample four genuinely different constructions each; F1 and F2
   are 3–4 *sites/instances of one mechanism* (parse break; undeclared/typo'd name) — so "F2 4/4" is one
   mechanism at four sites, which A6 later says explicitly; F8 is **one annotation on one model** with four
   different defect types, so "F8 4/4" is closer to "this instrument checks the metadata surface at four
   points" than to a class-level rate in a population. That is a real limitation on four `n = 4` cells, and
   it is not quantified anywhere in the report.
3. **Single-defect discipline is met in 30/32 cases and is a matter of interpretation in two.** F4-04 and
   F8-01 change two things on one line. Both are constructible as "one defect" if the second change is part
   of the construction, but the methodology's rule ("exactly one deliberate defect; no incidental changes")
   is stated more strongly than the artefacts show, and neither rationale flags the composite edit.
4. **Surface-tell flags are defensible except F1-04.** `<1.1>` in a name position is lexically conspicuous
   to a reader who knows the short-name syntax; flagged `no`. Reclassifying it changes the stratum from
   `3/3 vs 20/29` to `4/4 vs 19/28` — direction unchanged, so no conclusion moves.
5. **Class-instantiation is exact for 30/32; F3-03 and F4-01 are the exceptions** (declaration-kind change
   posing as a typing relation; range inconsistency with no named constraint). Neither is a fatal
   mislabelling, but the F4 row's meaning depends on how RB-02 is resolved.
6. **The corpus contains no adversarial-input mutants**, which issue #8's exclusion requires; I saw none.

## 5. Re-derivation (commands and results)

Everything below was run by me in this workspace. Where a command re-ran B's own script, the output was
byte-identical to the committed derived artefact.

```bash
# instrument identity
shasum -a 256 .tools/sysml
#  ddfc2962...1598f0  (matches TOOLING.md and every run log)
.tools/sysml -version      # sysml v0.12.1, commit b2f0e9b8..., build 2026-11-06_03:25:57

# frozen hashes
cd research/issue-008
shasum -a 256 -c methodology.sha256        # OK
shasum -a 256 -c mutants/mutants.sha256    # 32 × OK
shasum -a 256 -c mutants/expectations.sha256  # OK, OK
shasum -a 256 -c empirical/PRE-REGISTRATION.sha256 # OK

# independent reproduction of the mutant arm (my own loop over the binary)
#   32 mutants -> 23 with >=1 error, 28 with >=1 diagnostic
# independent reproduction of the known-good arm
#   10 models -> 0 errors, 1 warning (KG-04 name-conflict@17)

# re-derivation of every reported rate
python3 harness/analysis.py
#  primary: 23/32 = 0.72 [0.55, 0.84]; outcomes detected 23 / wrong_severity 2 /
#  misleading 1 / incidental 1 / silent 5; per-class 4,4,2,3,3,3,0,4
#  (the "silent 5" is the artefact's own output; see C14 for why that label is wrong)
#  diff against pre-run copies of analysis.md/.json/triage.csv: EMPTY (byte-identical)

# Wilson intervals, recomputed from scratch for every proportion in the report
#  23/32 [0.55,0.84]; 0/4 [0.00,0.49]; 3/4 [0.30,0.95]; 4/4 [0.51,1.00];
#  2/4 [0.15,0.85]; 28/32 [0.72,0.95]; 3/3 [0.44,1.00]; 20/29 [0.51,0.83];
#  13/16 [0.57,0.93]; 9/10 [0.60,0.98]; 9/13 [0.42,0.87]; 9/12 [0.47,0.91];
#  9/11 [0.52,0.95]; 24/32 [0.58,0.87]   -> all match the report to 2 dp

# external arm, from raw
python3 - <<'PY' ... re-score raw/run1 and raw/run2 M1 by line range ...
#  run1 9 detected; run2 9 detected; zero differences; 4 controls clean; 3 frozen-clean-only with errors
PY
python3 empirical/run_external.py --verify-only
#  subset.json OK, models/manifest.csv OK, 36 files OK
```

**Triage spot-checks (at least one per category).**
- `detected`: F3-02 raw → `error[usage-typing]` at L10, "An attribute must be typed by attribute
  definitions" — the injected defect, correctly labelled.
- `detected but un-named`: F4-01 raw → `error[multiplicity-range]` at L21, "multiplicity lower bound exceeds
  upper bound on wheels" — correct line, real condition, spec-silent (C7), but see RB-02 for what it means.
- `wrong_severity`: F4-02 raw → `warning[end-feature-multiplicity]` only; the tool's `-explain` documents that
  code at warning severity. So "wrong severity" is a CI-gate judgement, not a spec violation.
- `misleading`: F3-01 raw → `warning[name-conflict]` at the right line, "Duplicate of inherited member name
  'self' from Part, Port"; the injected kind mismatch is not named. I agree with the label as a *message
  quality* judgement and note that it applies to a warning, whereas methodology §8 reserves "misleading" for
  an emitted *error*. The report acknowledges at L120–122 that the misleading cases are warning-severity, but
  the category label stays "misleading" — a definitional drift, not a wrong number.
- `incidental`: F3-04 raw → `warning[bound-feature-types]` on the `satisfy` line below the defect; correctly
  incidental.
- `silent` (true): F7-01..04 raw → `diagnostics: null`, exit 0.
- `"silent"` (wrong): F5-01 raw → one `warning[name-conflict]` (the base's own warning). See C14.

**Denominator ladders.** 9/13 (registered) → 9/12 (drop contested I1) → 9/11 (also drop the
short-circuited item). The arithmetic is right, the registered number is retained as the headline, and the
ladder is shown rather than chosen between. "Unmeasurable" is used honestly here: the excluded item's raw
envelope really does say no check was made, and the class is not rescued (the other R1 item is a clean
silent miss). My only reservation is presentational (C23) and that the 0.82 rung is quoted in the same
sentence as the synthetic 0.72.

## 6. External-set assessment

**What is solid.** The frozen subset is untouched and byte-identical to A's live corpus (I verified all 36
files). B did not relabel, drop or repair any item; I re-scored 9/13 independently. The invocation set,
attribution rule, standing map, control rule and P6/P8 decision rule are in the file before the run (with
the AM1 caveat in §3.4). The run1→run2 identity claim is true. The short-circuit quotation is accurate. The
denominator ladder is disclosed. P6 is reported as *not supported by its own pre-registered rule* — the
single most credible thing in the whole submission, because it costs B its strongest narrative.

**What needs correction.**
1. **The M2/M3 accounting is wrong** (C24): 3 items evaluated in each mode, not 1. The report's own §11.2 and
   addendum L843 say 3; the headline table (empirical REPORT L46–47) and A10.1 (report L784–785) say 1 and
   then list 10 n/a against a denominator of 13. This is a simple column-sum error that an adjudicator should
   require fixed, because "applicability" is the honest form of the M2/M3 null result.
2. **The scoring deviates from the registered rule for non-satisfy-family items** (C25): `not applicable` was
   registered; the harness emits `wrong-target` (2 items, 6 controls). Detection counts are unaffected, but
   "applicable to 3 items" is only true under the harness's reading, not the registered one — under §4.2 the
   M2 applicable count is 1 (S2) and M3's is 3.
3. **The external harness's immutability claim is false** (C21b). The synthetic harness does what it says;
   the external one overwrites. A future run must fix this before any citation-by-hash is safe.
4. **The "external set was frozen before B saw it" story is weaker than it reads.** B had run the validator
   on 15 of the 18 models during Gate 2 and says so (`PRE-REGISTRATION.md` §7); A had seen B's report before
   freezing; and the two agents exchanged reviews before the subset was frozen (14:22/14:23, subset frozen
   14:33). The *items* are A's and predate B's run, which is the substantive independence; the *predictions*
   are informed. B states this; a reader should not upgrade "different agent" into "blind".
5. **"The layer picture survives but class/aggregate do not" is supported** (C27), with the caveats B himself
   supplies: agreement on notation and resolution is agreement-by-full-detection; the constraint layer
   disagrees in direction on n = 1; four synthetic classes have no observed counterpart at all (0/18
   construct frequency), so the most favourable synthetic cells are exactly the untestable ones.

**What the external arm does to the main question.** It strengthens the *practical* claim (a pass is
evidence about a few layers) and leaves the *aggregate* claim unestablished. B says exactly that. I agree,
and I note that the coincidence of 0.69 and 0.72 is correctly labelled a composition artefact rather than
corroboration — that is the most important interpretive move in the submission.

## 7. Overreach that survived the addenda

The addenda are real corrections, not decorations, and the protocol requires the original text to remain.
The consequence is that the *front* of the report still asserts claims its own addenda retract, with no
forward pointer. Specific sentences, still present today:

1. **"it is no evidence at all about whether the model's structure means what it claims"** (§1, L42) — A2
   retracts this in terms ("That is what this pilot measured…"; "not 'nothing can see this'"). No pointer
   from §1 to A2.
2. **"it detected none of the four structural/architectural defects"** (§1, L32–34) — false after A2/A3.
3. **P3 "invisible to the only available instrument — Established — F7 0/4, all four silent"** (§2, L65) —
   contradicted by A2's "P3 restated" (L507–510); the table cell itself is never qualified.
4. **"for four out of four structural defects tested it means nothing at all"** (§11.1, L352–353) — the
   report's own "calibrated sentence" is the most-quoted sentence in the document, and it is the one the
   addenda falsify.
5. **"it was perfect on the two layers it advertises first"** (§1 L30–31; quoted again in A4 L554) — A4
   withdraws the notation generalisation (reserved-keyword errors can exit 0) and A6 withdraws the
   resolution generalisation (succession sources are not resolved). "Perfect on the layers" survives only
   for the authored families.
6. **§3.4's heading "which conditions no available checker catches"** (L124) and **"the ceiling of automated
   SysML v2 validation here is typing plus per-constraint well-formedness"** — after A2 the same instrument
   decides one F7 condition, so "no available checker" is wrong even for the four mutants in that table.
7. **"one warning that a specification-verbatim example does not deserve"** (§1 L38) — a judgement (C6)
   stated as a fact; the triage file's hedged version ("not evidence of a wrong verdict") is the accurate
   one.
8. **"Four defect classes that any systems engineer would call wrong are invisible"** (§11.5, L367–368) —
   now one of four is visible to `-satisfy`; and "any systems engineer would call wrong" is a normative
   assertion, not a finding.
9. **"§12.5 … `-validate=<object>` mode … which I did not exercise"** (§12.5) — exercised in A2; the
   adjacent-question list was not annotated.
10. **README headline "F7 — all four silent"** (L21) and **"named SHOULD constraint silently missed:
    `validateFeatureValueOverriding`"** (L22, now at least two) — stale for the same reason.
11. **README "No empirical challenge set … nothing here was informed by Researcher A's work"** (L97–98) —
    contradicted by `empirical/**` and by A1–A10; this is the most concrete internal contradiction in the
    repository index.
12. **Generalisation in §11's bold sentences** ("A validator pass is evidence about four layers and no
    others"; "Both error rates matter and both are now bounded") — one binary, one version, 32 authored
    mutants; the qualifier follows, but the bolded claim travels further than the evidence.

None of these changes a number. All of them are the kind of sentence a downstream reader copies into a
review without reading the addenda, which is why the protocol's addendum mechanism needs a front-page
pointer as well as a dated correction.

## 8. Objection register

Severity: **blocking** (invalidates a headline or a load-bearing conclusion) / **material** (changes the
weight a claim can bear, or must be fixed before publication) / **minor** (record-keeping or wording; no
effect on a number).

| ID | Objection | Severity | What would settle it |
|---|---|---|---|
| **RB-01** | **The external pre-registration's "frozen" hash is post-AM1, the pre-run hash was overwritten, and `run-log.md` §2 mis-describes the difference between the two recorded versions as "only a header timestamp".** The file whose hash is offered as proof contains an amendment written after the first run; the `.sha256` mtime equals the amended file's mtime. | **material** | Publish the pre-AM1 `PRE-REGISTRATION.md` (or its hash) from before 14:35:38Z, or state in the report that the pre-run hash is unrecoverable and that the pre-registration is evidenced by content + AM1's disclosure, not by hash. Correct the run-log sentence. |
| **RB-02** | **F4-01 is used as both a true detection and as evidence of over-reach.** If `[4..2]` is legal (P5's reading), `error[multiplicity-range]` is a spurious error on a legal model, contradicting "no case of a spurious error on a mutant", and F4 is 2/4, not 3/4 (headline 22/32, not 23/32). If it is a defect, the instrument is not "stricter than the specification" in the P5 sense. The report adopts neither reading explicitly. | **material** | A ruling on whether a lower bound exceeding an upper bound is a specification-named/semantically-required condition (retrieve the MultiplicityRange semantics, not only the validate constraints), then one recomputation of F4 and the headline under the chosen reading, with the other reading stated. |
| **RB-03** | **The expectation audit overstates its independence.** `24/24` is near-tautological, and the pre-freeze calibration log records construct-level detections (`incommensurable-binding`, `metadata-metaclass`, `metadata-owning-type-feature`) that pre-determine F6/F8 "yes" flags. The report and methodology name only the `-explain` list; the gate log characterises the probes as interface calibration. | **material** | Amend report §4.1 / methodology §12.6 / gate-log Gate 1 to name the behavioural probes as a source of expectation knowledge; keep the audit but relabel it "informed, not blind, and weak by construction". |
| **RB-04** | **KG-04's over-reach classification is a contestable judgement, not a spec-verbatim finding**, and the "what would settle it" pointer (§7.6.1) is mis-targeted: in SysML 2.0 Part 1, §7.6.1 is "Definition and Usage Overview". KerML permits the same name for a redefined feature only where there is an owned redefinition. | **material** | Retrieve the naming/redefinition rules (§7.6.3, KerML §7.3.5/8.3.3) and decide whether a same-named member in a specializing definition is an implicit redefinition; if it is not, reclassify KG-04's warning as category (i) or as unresolved rather than (ii), and re-state A10.3's name-conflict argument accordingly. |
| **RB-05** | **The M2/M3 accounting in the external arm is arithmetically wrong and internally contradictory**: "1 item evaluated, 10 not applicable" vs "applicable to 3 items each" vs `results.csv` (3 evaluated, 10 n/a). | **material** (publication-blocking for that table) | Correct both documents to 3 evaluated / 10 n/a, with the per-item breakdown (M2: S2 not detected, I1 and T4-C3 wrong-target; M3: 2 not detected, 1 weaker signal). |
| **RB-06** | **The external scoring does not follow the registered rule for non-satisfy-family items** (registered `not applicable`; emitted `wrong-target`), and controls are labelled with the vocabulary AM1 said must not be used for controls. | **material** | Re-label under §4.2 and report M2 applicable = 1 (S2 only), or amend the pre-registration with a dated addendum explaining why a non-satisfy item can be "wrong-target". |
| **RB-07** | **The external harness's immutability claim is false** (`write_text`, no existence check, `exist_ok=True`). A cited raw run can be overwritten by re-running the documented command. | **material** (evidence-integrity claim) | Implement `open(..., "x")`/refuse-if-exists as the synthetic harness does, or delete the claim. Log the change. |
| **RB-08** | **Three internal arithmetic/label errors**: A8's "24 of 28" (recomputation: 23 of 28); "5 silent" (F5-01 carries a warning, so 4 silent + 1 incidental under the frozen definition); the ladder's exclusion order differs between empirical REPORT §1 and §6.1. | **minor** | Recompute from `diagnostics.csv`; correct the counts and the ladder wording. No headline changes. |
| **RB-09** | **B's stated UTC times are unreliable and several are forward-dated**: A2's run window 14:31–14:36Z vs raw/run-log 14:24:50–14:26:00Z; addenda A2–A9 dated 14:40Z in a file last written 14:38:04Z; A10 dated 14:56Z in the same file; the Gate-2 response dated 14:40Z but written 14:27:06Z. (B has twice before corrected forward-dated timestamps.) | **minor** | Stop quoting stated times for ordering; use filesystem order or a timestamped append-only log. The *ordering* the protocol cares about is independently established and unaffected. |
| **RB-10** | **`spec_status` is post-hoc**, not a frozen field, though the report says it "was fixed before the run". The deliverable table's category column is a single-coder reading. | **minor** | Add the six-bucket assignment to a dated pre-run file, or say "assigned post hoc from the frozen text by a mechanical rule, single-coder". |
| **RB-11** | **The known-good arm is not independent of the mutant arm** (same 10 models are the parents of all 32 mutants; 9/32 from one base; corpus iterated to tool-silence before the freeze) and its independence from the tool's own tests is unverifiable. | **minor** | State the base concentration and the iterate-to-silence history in §3.1/§8; the 0/10 claim itself is unaffected and reproduces. |
| **RB-12** | **The README index contradicts the artefacts** ("No empirical challenge set… nothing here was informed by Researcher A's work"), and the report/README carry no pointer from their summaries to the addenda that retract §1/P3/§11.1. | **minor** (reader-facing) | Update the README's "not here" section and add a one-line pointer at the top of the report: "the F7/P3/§11.1 claim is corrected in A2–A3". |

**No blocking objection.** I looked for one: I tried to break the headline by re-running the arm
independently, by recomputing every interval, by re-scoring the external raw outputs, and by checking the
one correction that could reverse a conclusion (A2). It held. A's O1 was the blocking objection and B's
remedy is verified. **7 material, 5 minor.** RB-01's severity could reasonably be argued up by an
adjudicator who treats hash-based pre-registration as load-bearing for the external arm; I keep it at
material because the rules are visibly pre-run in content and the only post-run changes are conservative.

## 9. Process compliance

| Requirement (PROTOCOL §3/§5/§7, Amendment A1) | Verdict |
|---|---|
| Write scopes respected | **yes as far as the artefacts show**: everything B wrote is under `research/issue-008/**`, `reports/issue-008-*.md`, and the two Gate-2 files the amendment authorises. |
| No validator-as-truth in the mutant arm | **yes**: no expectation or classification was changed by validator output; the frozen MANIFEST verifies against its pre-run hash; the one place a validator influenced a *layer label* (F4-03) is confessed in §10 (C11), and no `MANIFEST-REVISIONS.md` exists to test it. |
| No silent edits: addenda preserve originals | **yes**: original claims are visible (A2 quotes the deleted wording; A3/A5/A6/A8 name the original claim), and no post-run edit to the frozen files is detectable by hash. The failure is the reverse: the front of the report was *not* updated and the README was not reconciled (RB-12). |
| Frozen files byte-identical | **yes**: all four sha files verify today, and the empirical subset is untouched and byte-identical to A's live corpus. |
| "No expectation was revised" | **partly**: true of the frozen content (hash), over-stated as a statement about the authoring process (C11). |
| One-instrument limitation stated | **yes**, repeatedly and adequately (C35). |
| Access boundaries | **yes**: Syside's licence check was not attempted; the OMG pilot was a bounded attempt with the exact failure logged; I re-verified the JVM absence and the release-asset list without bypassing anything. |
| Counter-evidence recorded | **yes**: H9 is reported as failed, the -explain threat is disclosed, the negative results about B's own corpus (§10) are recorded, and the external arm's unflattering P6 outcome is reported. That is the strongest compliance signal in the submission. |

## 10. What I could not check, and why

- **The "first draft" pre-registration (`0106e082…`)**: the file was not preserved, and its hash is a literal
  inside the harness that generated the log. The claim that it differs only in a header is **unverifiable**
  (and, given AM1, not accurate as a description of the difference between the two *recorded* versions).
- **Whether the author revised an expectation before the freeze**: no drafts exist. The frozen content
  verifies; the drafting history does not.
- **"No delegation / no subagents"**: not provable from artefacts (C39).
- **Independence of the known-good models from the tool's own test suite**: OpenSysML's tests are not in
  this workspace; I found no evidence of their use, which is not the same as evidence of non-use.
- **The completeness of the 623-row catalogue**: I used it as B did, and spot-checked six constraints against
  the retrieved KerML/PDF text; I did not re-extract the XMI. My C7 check is against the specification text,
  not against the catalogue's completeness.
- **A's coding quality**: out of my scope (issue #7 is reviewed elsewhere). I verified only what B's external
  arm depends on: the subset is hash-stable, contains no validator-derived field, and matches A's live
  corpus byte-for-byte.
- **Page numbers per provenance file**: I verified the quoted text and the clause for KG-04 and KG-09 against
  the extracted PDF; I did not verify every page number in all ten provenance files.
- **The tool's internal behaviour**: I can characterise its outputs, not its implementation. Any claim about
  *why* a check does not fire is beyond both B's and my evidence.

**Disclosure.** Re-running `harness/analysis.py` (required by the task) rewrote three derived files
byte-identically; `diff` against pre-run copies is empty, so no content changed. I did not run the external
harness (RB-07) and I did not modify any frozen, empirical-subset or cross-review artefact.

## 11. Adjacent questions noticed, not researched

Logged, not pursued: (a) whether `[4..2]` is semantically unsatisfiable rather than merely un-named (the
systematic reading of KerML's MultiplicityRange semantics); (b) whether the KG-04 name-conflict and the
F5-01 silent miss share one cause — the tool not treating a same-named member as an implicit redefinition
(my hypothesis, **not established**: the tool documents a `feature-value-overriding` error code and did not
fire it, and it warned `name-conflict` instead; if the shared cause is real, the F5-01 miss and the KG-04
warning are one defect in the tool or one ambiguity in the spec, and that would be a sharper finding than
either pilot's current wording); (c) whether `-explain`'s documented `multiplicity-range` code should have
made F4-01's "expected undetectable" prediction impossible — which would strengthen RB-03's "informed, not
blind" reading; (d) construct-frequency reweighting of the 23/32 (B's own identified missing instrument);
(e) the `-self-check` surface, which B ran on F7-01/F7-03 and which reports 127 checks/0 violations on a
model with an unreachable state — a potentially better-measured target than `-validate` for the structural
class.

**End of review.** Every verdict above names the artefact and the check; where I could not check, I say so
rather than infer. The two things I would ask the adjudicator to rule on first are RB-01 (is a post-run hash
evidence of pre-registration?) and RB-02 (is an inverted multiplicity range a defect?), because both shape
what the pilot's headline means even though neither changes the arithmetic I reproduced.
