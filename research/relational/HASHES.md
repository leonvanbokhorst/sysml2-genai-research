# Final artefact ledger — relational demonstration (2026-11-13)

Append-only record of the bytes a reader can verify. Hashes were taken by the Team Lead after the
Gate-4 corrections were applied and before the branches were created. If a file later changes, the
new bytes are a new row, not a correction of an old one (PROTOCOL.md Amendment A2).

## Reports and entry points

| File | sha256 |
|---|---|
| `README.md` | `75eb9e69f8cfa11b9a071e3ba4bbd11d5247c3e092890dfd0c56331e5134f35f` |
| `reports/issue-007-error-taxonomy-pilot.md` | `e50e19077c35afc80f44090b0498a148d9109e46ba6e26f5c84cb08dad71925b` |
| `reports/issue-008-validator-reliability-pilot.md` | `06dd07f403383354832b730e16fda59e35e059d80032dfba9283c5aab0104302` |
| `reports/relational-demo-synthesis.md` | `806fce4a278fe98f02c2f6666d451d7fe45d572c775e3f0b3111a7c4f0eed6c8` |
| `research/relational/demo-map.md` | `6818cf9f543f2ecb4cedf5af05766cfdb5a07a97ad830ecaf2a1fa3197554229` |
| `research/relational/PROTOCOL.md` | `7865174f5c933479161fd67fb0c9f6881025327458f5fc9646e41c079caecde9` |
| `research/relational/gate-log.md` | `91b690c6fd43759b2530909b1e7f957f76f5627b42607478c9150d60773330f9` |

## Frozen research instruments and populations

| File | sha256 | Note |
|---|---|---|
| `research/issue-007/METHODOLOGY-FROZEN.md` | `269d8dbe7228db83d20ca2be39991172f20fd23458ac1e5e6755ff7269564f76` | byte-identical throughout |
| `research/issue-008/METHODOLOGY-FROZEN.md` | `2c80d63e8800be9ca67a051aaffdbc4b6c56c1b576002fc4446fe82862e6f00b` | byte-identical throughout |
| `research/issue-007/coding/CODEBOOK.md` (v1.4) | `91f963bffb980924f4969da4200cb2a35231e23ca80a8afa4497435f886094b9` | v1.0 hash recorded in the second-coder brief |
| `research/issue-007/coding/errors.csv` (frozen 14 rows) | `30265ff57bdd1f4036304c6acbc1026678d36f0b3604c925a7b538455fc815f6` | immutable; corrections in `errors-corrections.csv` |
| `research/issue-008/mutants/MANIFEST.csv` (expectations) | `a9f479748aea10c76460421031a384ddda779d4c78ea1cb6a5fe2f208f157be7` | pre-registered before the first run |
| `research/relational/empirical-subset/subset.json` | `bc2b92a5fdff6e976ae7156b13beba3535f0895e4a41268cf76c1551a6c3dfaa` | frozen before B's external run; addendum carries later status notes |
| `research/relational/empirical-subset/FROZEN-SUBSET-HASH.txt` | `0d4bb1966197b50e9edf511db705ddf43b5da11958036162e507dba72506fb78` | also records `FROZEN-SUBSET.md` original/pointer hashes |

## Relational record

| File | sha256 |
|---|---|
| `research/relational/cross-reviews/A-reviews-B.md` | `05ca64ccaa4ceae4032ca36aa22f2090c5565449d021764a9da480bbbb1a8102` |
| `research/relational/cross-reviews/B-reviews-A.md` | `de2d99cea17587a9603e9602303873556db9b00f93d8101451c0db57be9af0b1` |
| `research/relational/cross-reviews/A-response-to-B-review.md` | `6e8ab42e6b85ff6e1f49fa1e34bd80ea34f4b72199e534a6039df01e06fadde8` |
| `research/relational/cross-reviews/B-response-to-A-review.md` | `3ccbfce43320a870611479bdd127a9d1b5b37cfd3b8be98ff88b62cace2612bb` |
| `research/relational/reviews/reviewer-a-issue-007.md` | `8e3b099246f0c53d38f73116e744b7372e9e37d32a31ffecf43b7683fb6631e7` |
| `research/relational/reviews/reviewer-b-issue-008.md` | `2090ba1c60f166f2664f65664244a682b1911de3bcd0a0d14b094d857a753fc1` |
| `research/relational/critique/semantic-ceiling-critique.md` | `e549ca6ea56c6a655f1bc7ba14f51b0dda3c3e658c509c7d3a4959c91093958a` |
| `research/relational/critique/CLAIMS.csv` | `47eecedc856c758957d6e64d103fe6d2073600659f235d5399c248276a2d8179` |
| `research/relational/adjudication/ADJUDICATION.md` | `ca196ae264e4d8c93f0f4f7570b40533c7231f0a1d8a361c1b9b1a8c0cbdf974` |
| `research/relational/adjudication/rulings.json` | `97303a58e046de4ae6cc6b50894a8c9f267361dd762599c0526e8eea3e53aa26` |
| `research/relational/adjudication/CORRECTIONS.md` | `b6c78202b938b3d2bdd78d858ed97abb8981e75f32bfcdefa3294b0bdef448ff` |

## Post-adjudication responses and support

| File | sha256 |
|---|---|
| `research/issue-007/ADJUDICATION-RESPONSE.md` | `1069cf7f40977ddeba8162b258811b069407863915b74cc3f37e04ad5126fcde` |
| `research/issue-008/ADJUDICATION-RESPONSE.md` | `4d6e26d7b170ea09ce336b503e127a000f0e54a8da53a4cb3852761328303395` |
| `research/issue-007/AMENDMENTS.md` | `34855cdfde7c71ce826b7db06ca667cfc5c828b8a038001b274d89e1d39fe559` (as reviewed) |
| `catalogue/README.md` | `f4551bb1fb13c3cd8e820fa6a943ce309df3d39ac8adcf34acae4361172ca958` |

## Tool

| Item | Value |
|---|---|
| OpenSysML CLI | `sysml v0.12.1`, commit `b2f0e9b802a334369da94312c35cefbd8726d3bf`, build 2026-11-06_03:25:57 |
| Binary sha256 | `ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0` |
| Release asset | `opensysml-darwin-arm64.tar.gz` sha256 `0f16d282ec50bfda916e74ef102e5b257bf2c9964f6e44df9db495db4fc96210` |

The binary is git-ignored; reproduce it with [`TOOLING.md`](TOOLING.md) §1.

## Corrections after delivery (append-only; 2026-11-13T16:20Z)

Two documentation corrections were requested at the human review gate, plus a PR-boundary change.
The rows above stay as the record of what was delivered; these are the new bytes. No research
artefact, report finding or adjudication ruling changed.

**(i) Adjudication arithmetic made explicit in the student-facing map.** The machine record has
**81 entries: 64 accepted challenges + 10 upheld status propositions + 3 rejected + 4 unresolved**.
`rulings.json` stores the ten upheld propositions with `ruling: "ACCEPTED"`, so its counters read
74/3/4. Both the map and the synthesis now show the four-way split, not three.

**(ii) Independence wording corrected in the map.** The map now distinguishes *independently
sourced evidence*, *independently authored test cases*, and *calibrated test cases*. B's 10
known-good models are specification-quoted but were iterated to tool-silence before the freeze
(ruling B-22); the 0/10 result is therefore a calibration probe, not a false-positive rate. The
map's earlier "independent of mutants" phrasing overstated what the arm supports.

**(iii) PR boundaries.** The three draft PRs now have disjoint file sets. The frozen empirical
subset (`research/relational/empirical-subset/`) and `.gitignore` live only in the relational PR
(#18); the #7 and #8 PRs reference them and depend on #18 merging first.

| File | sha256 (new) | Supersedes |
|---|---|---|
| `README.md` | `02ea306464f21f834cdd46babab3284e1133a955c25c523fc0301ae8cee5b937` | `75eb9e69…` |
| `reports/relational-demo-synthesis.md` | `42f9e28459edfcfe12f7bf53fa51c16eccc067a15f8b65c67759e81ab583fa2c` | `806fce4a…` |
| `research/relational/demo-map.md` | `e38dc097a3809f554176bff4258cf4263bcf80ad06f575bc4178851919ab743a` | `6818cf9f…` |

Unchanged by these corrections: every file under `research/issue-007/`, `research/issue-008/`,
`research/relational/adjudication/`, `cross-reviews/`, `reviews/` and `critique/`; all frozen
artefacts and their hashes; and `research/relational/gate-log.md`, which already recorded the ten
upheld propositions alongside the 64/3/4 split.
