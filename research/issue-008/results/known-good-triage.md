# Known-good corpus: triage of every firing

The corpus is `known-good/` — 10 small models built **before** the mutants, each with a
`PROVENANCE.md` stating which declarations are quoted from the pinned specification PDF, which I
supplied, and a constraint-level argument for validity (see `METHODOLOGY-FROZEN.md` §5).

Run: `results/raw/run1/known-good/*.json` (unedited). Summary row per model in
`results/results.csv`.

Triage categories, fixed in advance: **(i)** genuine defect I missed, **(ii)** validator
over-reach / legal-but-flagged, **(iii)** confound (missing import, library resolution, harness
artefact). Only (ii) counts as a false positive.
**A fourth category, (iv) unresolved / specification-ambiguous**, was added by adjudication
(B-15 / RB-04) for the one firing where the specification text supports both readings — see the dated
correction at the foot of this file.

## Result

| model | errors | warnings | triage |
|---|---:|---:|---|
| KG-01-parts | 0 | 0 | clean |
| KG-02-ports | 0 | 0 | clean — including the §7.12.3 conjugated port usage |
| KG-03-connections | 0 | 0 | clean |
| KG-04-featurevalues | 0 | 1 | **(iv) unresolved / spec-ambiguous** — see the dated correction at the foot of this file (was "(ii) candidate over-reach"; adjudication B-15 / RB-04) |
| KG-05-states | 0 | 0 | clean |
| KG-06-transitions | 0 | 0 | clean |
| KG-07-requirements | 0 | 0 | clean |
| KG-08-quantities | 0 | 0 | clean |
| KG-09-actions | 0 | 0 | clean — including the §7.17.3 control-node block |
| KG-10-asserts | 0 | 0 | clean |

**Error-level false-positive rate: 0/10.** **Warning-level: 1/10** (KG-04), triaged (ii).

## The one firing, in full

```
KG-04-featurevalues.sysml:17:19: warning[name-conflict]: Duplicate of inherited member name 'cutoff' from TestRecord
        attribute cutoff : Rational default = 0.75 * averageScore;
```

Line 17 is the specification's own example from §7.13.4 (p.72):

```
item def TestWithCutoff :> TestRecord {
    attribute cutoff : Rational default = 0.75 * averageScore;
}
```

**Why I judge it legal-but-flagged, not a defect of my model.**
1. The line is quoted verbatim from the specification, and the clause presents it as the
   illustration of *default* feature values on a specializing definition. A normative example is
   the strongest available evidence that the notation is admissible.
2. `cutoff` in `TestWithCutoff` is intended to redefine `TestRecord::cutoff`. §7.6.3 defines
   redefinition as a kind of subsetting and gives `:>>`/`redefines` as the *explicit* notation, but
   the specification's examples also rely on same-named members in a specializing definition
   (§7.6.5 discusses effective names for the unnamed case, which presupposes that the named case is
   ordinary). The checker itself resolves the member (it reports a duplicate name, not an ambiguity),
   so it is aware of the redefinition relationship and warns anyway.

**Reservation, stated rather than suppressed.** The diagnostic is a *warning*, and the specification
does not forbid a tool from warning about a construct. So this is not evidence of a wrong verdict;
it is evidence that a spec-verbatim example does not validate silently in this instrument. It is
counted in the warning-level false-positive rate (1/10) and excluded from nothing.

**What would change this judgement.** Retrieving and reading §7.6.1's naming rules in full (I read
§7.6.3 and §7.6.5, not all of §7.6.1) to establish whether same-named redeclaration without `:>>`
is explicitly admitted or merely conventional in the examples. That is a bounded retrieval the
reviewers can do; it does not affect any mutant result.

## Two firings that were *not* false positives (recorded so the corpus is not presented as
infallible)

These fired during **corpus construction**, before the freeze, and the models were corrected:

| model | firing | triage | action |
|---|---|---|---|
| KG-04 (v1) | `unresolved reference: sum` / `size` — "did you mean SequenceFunctions::sum, RealFunctions::sum …" | **(iii) confound** — missing library import, exactly the confound `TOOLING.md` §1 warns about | added `private import SequenceFunctions::*; private import RealFunctions::*;`, documented in the provenance file |
| KG-09 (v1) | `unresolved member: picture` on `bind picture = focus.picture;` | **(i) genuine defect — in the specification's example text**, not in my model: `focus` declares `out image`, not `picture` | one-token deviation to `focus.image`, recorded verbatim in `KG-09-actions.PROVENANCE.md`; carried into the report as an incidental observation about the source material |

The second row matters for the main research question: a normative example in the adopted
specification does not resolve against its own declarations. It is a data point about how carefully
"the specification says" can be used as an oracle.

---

## Adjudicated correction — 2026-11-13T15:10Z (B-15 / RB-04)

**Superseded:** the heading above, *"**(ii) candidate over-reach** — see below"*, and the claim that
the KG-04 `name-conflict` warning is a false positive because the construct is a legal implicit
redefinition.

**Corrected — reclassified as (iv) unresolved / specification-ambiguous.** "Over-reach" required the
premise that a same-named member in a specializing definition is a **legal implicit redefinition**,
and that premise is **not established**. What the retrieved text actually says:

- **KerML `validateNamespaceDistinguishibility`, §8.3.2.4.5** (`isDistinguishableFrom`) forbids the
  construct *as written*: two memberships in one namespace that are not distinguishable.
- **SysML §7.13.4** uses the construct anyway, in the specification's own `TestWithCutoff` example.
- **SysML §7.6.3 and §7.6.5** govern named and effective-name redefinition. **§7.6.1 is "Definition
  and Usage Overview"** and is *not* the clause that settles this — the earlier "what would settle it"
  pointer was wrong.

So either the specification's example is defective, or the constraint is meant to admit implicit
redefinition. **Neither is established**, and the two readings cannot both hold. The warning is
therefore `unresolved / specification-ambiguous`, not over-reach, and the tool may be correct on the
letter of the constraint.

The same question is `name-conflict` adjudication **X-01** (unresolved), where the adjudicator kept
both readings visible. It is also the rival reading on my F5-01 judgement (B-25): if a same-named
declaration is not a redefinition, F5-01 does not instantiate `validateFeatureValueOverriding` at all.

**Unchanged:** the summary row for KG-04 in this file now reads *"(iv) unresolved / spec-ambiguous"*
instead of "(ii) candidate over-reach". The **error**-level false-positive rate stays **0/10** —
this is a warning, and warnings are reported separately. The warning-level figure stays 1/10 with the
caveat that it is now ambiguous rather than decided.
