# FROZEN SUBSET — addendum (Gate-4 adjudication) — 2026-11-13T15:14Z

**Applies to:** `research/relational/empirical-subset/` (the external challenge set for Researcher B,
task 6). **Ruling sources:** adjudication `RA-03`, `RA-14`, `X-03`; corrections `A-6`, `A-11`, `A-21`.
**Frozen artefacts are not edited:** `subset.json` keeps the bytes B's run is pinned to
(sha256 `bc2b92a5fdff6e976ae7156b13beba3535f0895e4a41268cf76c1551a6c3dfaa`) and
`models/manifest.csv` keeps `a968ff34079a35cdab943dd72415853a4f05617eb353b8deb5665f93ae26b0cb`.
Only `FROZEN-SUBSET.md` changes, by a dated pointer and one relabelled summary line, so its hash
changes and **both** hashes are recorded below.

## 1. Two R1 items are contested as to DEFECT STATUS, not only as to layer

`T4-C1-E02` and `T4-C3-E01` were already marked contested **as to layer** (type/typing recorded, vs
structural/architectural rival). The adjudicator went further, and I accept it: their **defect status
itself** is contested, because

- the operative criterion is authored, and
- as worded it conflates a *feature* with its *instances*.

Restated criterion, with the contested step named:

> A connection end is defective iff, after resolving its feature chain, the end does not denote a
> single feature of the connector's domain. **Contested step:** whether a chain through a usage whose
> multiplicity admits more than one instance violates that requirement, or merely denotes a
> many-valued feature the language permits.

`subset.json` cannot be edited to carry this (B's run is pinned to its bytes), so this file is the
authoritative reading. **For B's measurement: report per item, and treat the two R1 items — and the
contested I1 item — as a separate contested group. Do not pool them into the primary rate.**

| Group | Items | n |
|---|---|---|
| Unqualified (defect status established, reporting mandatory) | ES-T1-C2-E01, ES-T2-C1-E01, ES-T3-C1-E01, ES-T3-C2-E01, ES-T3-C2-E02, ES-T4-C1-E01, ES-T4-C2-E01, ES-T5-C2-E01, ES-T6-C2-E01, ES-T2-C2-E01* | **10** |
| Contested (defect status and/or obligation) | ES-T4-C1-E02 (R1), ES-T4-C3-E01 (R1), ES-T1-C3-E01 (I1) | **3** |

\* `ES-T2-C2-E01` (S2) is unqualified as a *defect* but its obligation is discretionary (`check…`,
"MAY report, satisfy by implied relationships, or ignore"); B should label it as such rather than
pool it silently with mandatory obligations. The adjudicator's composition finding (9/9 established
and mandatory) excludes it — see `ADJUDICATION.md` §3.1.

**Effect on B's denominator (per B-34):** the primary external denominator is **10**, not 13; the
contested trio is reported separately. That is a denominator change, not a label change.

## 2. The control summary line was wrong: "4 controls + 3 descriptive models"

The subset summary said "7 controls". Three of those seven (`T5-C3`, `T6-C1`, `T6-C3`) were already
labelled `frozen-clean-only` and marked **not controls** in `FROZEN-SUBSET.md` and in each item's
`notes`, because each carries a verified post-inspection notation defect. The correct summary is:

- **4 controls** (`T1-C1`, `T2-C3`, `T3-C3`, `T5-C1`) — no coded defect in any population; clean as
  far as A's coding goes, **not** known-good by construction and not independently certified.
- **3 descriptive models** (`T5-C3`, `T6-C1`, `T6-C3`) — included so the record is complete; a
  diagnostic on them is **not** a false positive and they must not enter a specificity calculation.

The adjudicator **rejected** the underlying objection (RA-14) on the ground that the tiers were
already correctly labelled per item; the relabel is optional/cosmetic and is applied here so the
summary line cannot be misread.

## 3. Hashes

| Artefact | Before this addendum | After |
|---|---|---|
| `subset.json` | `bc2b92a5…3dfaa` | **unchanged** `bc2b92a5fdff6e976ae7156b13beba3535f0895e4a41268cf76c1551a6c3dfaa` |
| `models/manifest.csv` | `a968ff34…6b0cb` | **unchanged** `a968ff34079a35cdab943dd72415853a4f05617eb353b8deb5665f93ae26b0cb` |
| `FROZEN-SUBSET.md` | `fce76f47…c6c03` | **new** (recorded in `FROZEN-SUBSET-HASH.txt` after this edit) |

`FROZEN-SUBSET-HASH.txt` now carries both the original and the post-addendum document hash, so a
reader can tell which text they hold. The item set, excerpts, line ranges, classes and confidences
are unchanged; only the contested status reading and the control summary differ.
