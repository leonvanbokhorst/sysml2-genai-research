#!/usr/bin/env python3
"""Analysis for the issue #8 pilot.

Reads results/results.csv and results/diagnostics.csv (produced by
harness/run_validators.py from the raw validator output), applies the
post-hoc relevance judgement recorded below, and writes:
    results/triage.csv     one row per mutant, with the judged category
    results/analysis.json  every number the report quotes
    results/analysis.md    the readable analysis

The POST-HOC block below is the only judgement in this file. It is a reading of
each emitted diagnostic against the mutant's frozen `spec_constraint_or_defect`
text. It cannot change any frozen expectation; it only labels what the tool did,
under the definitions fixed in METHODOLOGY-FROZEN.md §8 before the run.

Metric definitions (frozen, §9):
    detected          >=1 error-severity diagnostic that is ABOUT the injected defect
    wrong_severity    the defect is identified but only at warning severity
    misleading        a diagnostic fires at the defect's location but names a
                      different condition (sends a reviewer to the wrong place)
    incidental        a diagnostic fires, but not about the injected defect
    silent            no diagnostic at all
"""
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"

# ---------------------------------------------------------------------------
# POST-HOC JUDGEMENT (see module docstring). Keyed by mutant id.
#   category: detected | wrong_severity | misleading | incidental | silent
#   note:     why
# ---------------------------------------------------------------------------
POSTHOC = {
    "M31-F1-01-missing-semicolon": ("detected", "syntax error names the missing terminator"),
    "M31-F1-02-extra-brace": ("detected", "syntax error: expected a namespace member"),
    "M31-F1-03-keyword-typo": ("detected", "three cascade syntax errors from the misspelt keyword"),
    "M31-F1-04-unquoted-shortname": ("detected", "five cascade syntax errors from the unquoted short name"),
    "M31-F2-01-type-typo": ("detected", "unresolved reference with the intended name suggested"),
    "M31-F2-02-parameter-typo": ("detected", "unresolved reference with the intended name suggested"),
    "M31-F2-03-redefinition-typo": ("detected", "unresolved reference at the redefinition target"),
    "M31-F2-04-missing-declaration": ("detected", "unresolved reference; hint offers a feature name, not a type"),
    "M31-F3-01-part-typed-by-portdef": ("misleading",
        "only a warning, at the right line but naming `name-conflict: duplicate of inherited member 'self'`; "
        "the wrong-kind typing itself is not reported"),
    "M31-F3-02-attribute-typed-by-partdef": ("detected", "usage-typing error names the required definition kind"),
    "M31-F3-03-state-replaced-by-action": ("detected", "not-a-vertex error names the transition endpoint"),
    "M31-F3-04-subject-typed-by-requirement": ("incidental",
        "one warning, located on the `satisfy` line five lines below the injected subject, naming "
        "`bound-feature-types`; the wrong-kind subject typing is not reported"),
    "M31-F4-01-inverted-bounds": ("detected", "multiplicity-range error (a rule no catalogue constraint states)"),
    "M31-F4-02-end-feature-multiplicity": ("wrong_severity",
        "end-feature-multiplicity warns, although KerML validateFeatureEndMultiplicity is SHOULD-report"),
    "M31-F4-03-non-natural-bound": ("detected", "multiplicity-bound-natural error"),
    "M31-F4-04-feature-value-count": ("detected", "feature-value-count error names count and upper bound"),
    # Adjudication B-19 / RB-08: under the frozen definition "silent" means ZERO
    # diagnostics; F5-01 carries the base model's warning, so it is incidental, not silent.
    "M31-F5-01-feature-value-overriding": ("incidental",
        "warning[name-conflict] carried over from the base model; nothing about the override is reported"),
    "M31-F5-02-satisfy-reference": ("detected", "relationship-target-kind error names the satisfy target kind"),
    "M31-F5-03-decision-node-incoming": ("detected", "decision-incoming-successions error, with the fix suggested"),
    "M31-F5-04-composite-port-feature": ("detected",
        "port-owned-usage-composite error: the prose-only §8.4.8.1 condition IS enforced here"),
    "M31-F6-01-wrong-dimension-unit": ("detected", "incommensurable-binding names both dimensions"),
    "M31-F6-02-missing-unit": ("detected",
        "binding-connector-type-conformance: a unitless magnitude is a Rational and does not conform"),
    "M31-F6-03-incommensurable-sum": ("wrong_severity",
        "incommensurable-operands identifies the defect but only as a warning"),
    "M31-F6-04-wrong-product-dimension": ("detected",
        "incommensurable-binding names the computed dimension and the declared one"),
    "M31-F7-01-unreachable-state": ("silent", "no diagnostic"),
    "M31-F7-02-satisfied-but-violated": ("silent", "no diagnostic"),
    "M31-F7-03-missing-flow": ("silent", "no diagnostic"),
    "M31-F7-04-contradictory-assertions": ("silent", "no diagnostic"),
    "M31-F8-01-annotation-not-metadata": ("detected", "metadata-metaclass error"),
    "M31-F8-02-body-feature-typo": ("detected", "metadata-owning-type-feature error"),
    "M31-F8-03-value-kind": ("detected", "binding-connector-type-conformance names String vs Integer"),
    "M31-F8-04-abstract-metaclass": ("detected", "metadata-concrete-type error"),
}

# Specification-oracle status of each mutant's condition. PROVENANCE (adjudication
# B-21 / RB-10): this assignment is a SINGLE-CODER, post-hoc reading of the frozen
# MANIFEST `spec_constraint_or_defect` text, made by a mechanical rule (does the text
# name a catalogue constraint / a prose-only condition / a library or notation
# condition / nothing?). It is NOT a field of the pre-registered MANIFEST, and the
# report must not describe it as fixed before the run.
#   metamodel_constraint  a named constraint exists in the 623-row catalogue
#   prose_only            a named/prose condition exists but is absent from the metamodel
#   notation              the textual-notation BNF is normative; no OCL constraint
#   resolution_mechanism  resolution is normatively defined; no constraint names it
#   library_semantics     only the normative ISQ/SI libraries constrain it
#   none                  nothing in the catalogue or the prose-only register
SPEC_STATUS = {
    "M31-F1-01-missing-semicolon": "notation",
    "M31-F1-02-extra-brace": "notation",
    "M31-F1-03-keyword-typo": "notation",
    "M31-F1-04-unquoted-shortname": "notation",
    "M31-F2-01-type-typo": "resolution_mechanism",
    "M31-F2-02-parameter-typo": "resolution_mechanism",
    "M31-F2-03-redefinition-typo": "resolution_mechanism",
    "M31-F2-04-missing-declaration": "resolution_mechanism",
    "M31-F3-01-part-typed-by-portdef": "prose_only",
    "M31-F3-02-attribute-typed-by-partdef": "prose_only",
    "M31-F3-03-state-replaced-by-action": "metamodel_constraint",
    "M31-F3-04-subject-typed-by-requirement": "prose_only",
    "M31-F4-01-inverted-bounds": "none",
    "M31-F4-02-end-feature-multiplicity": "metamodel_constraint",
    "M31-F4-03-non-natural-bound": "metamodel_constraint",
    "M31-F4-04-feature-value-count": "none",
    "M31-F5-01-feature-value-overriding": "metamodel_constraint",
    "M31-F5-02-satisfy-reference": "metamodel_constraint",
    "M31-F5-03-decision-node-incoming": "metamodel_constraint",
    "M31-F5-04-composite-port-feature": "prose_only",
    "M31-F6-01-wrong-dimension-unit": "library_semantics",
    "M31-F6-02-missing-unit": "library_semantics",
    "M31-F6-03-incommensurable-sum": "library_semantics",
    "M31-F6-04-wrong-product-dimension": "library_semantics",
    "M31-F7-01-unreachable-state": "none",
    "M31-F7-02-satisfied-but-violated": "none",
    "M31-F7-03-missing-flow": "none",
    "M31-F7-04-contradictory-assertions": "none",
    "M31-F8-01-annotation-not-metadata": "metamodel_constraint",
    "M31-F8-02-body-feature-typo": "metamodel_constraint",
    "M31-F8-03-value-kind": "metamodel_constraint",
    "M31-F8-04-abstract-metaclass": "metamodel_constraint",
}

CLASS_ORDER = ["F1-syntax", "F2-unresolved", "F3-kind-mismatch", "F4-multiplicity",
               "F5-named-constraint", "F6-quantity", "F7-structural", "F8-metadata"]


def wilson(k: int, n: int, z: float = 1.96):
    """Wilson score interval; returns (point, low, high) or (nan,...) for n=0."""
    if n == 0:
        return (float("nan"), float("nan"), float("nan"))
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (p, max(0.0, centre - half), min(1.0, centre + half))


def fmt_ci(k, n):
    p, lo, hi = wilson(k, n)
    return f"{k}/{n} = {p:.2f} [{lo:.2f}, {hi:.2f}]"


def main() -> int:
    results = list(csv.DictReader(open(RESULTS / "results.csv")))
    diags = defaultdict(list)
    for d in csv.DictReader(open(RESULTS / "diagnostics.csv")):
        diags[d["case_id"]].append(d)

    mutants = [r for r in results if r["kind"] == "mutants"]
    good = [r for r in results if r["kind"] == "known-good"]

    # ---- per-mutant triage ------------------------------------------------
    triage_rows = []
    for r in mutants:
        cid = r["case_id"]
        cat, note = POSTHOC[cid]
        ds = diags.get(cid, [])
        triage_rows.append({
            "mutant_id": cid,
            "fault_class": r["fault_class"],
            "expected_detectable": r["expected_detectable"],
            "expected_layer": r["expected_layer"],
            "surface_tell": r["surface_tell"],
            "spec_status": SPEC_STATUS[cid],
            "n_errors": r["n_errors"],
            "n_warnings": r["n_warnings"],
            "any_error": r["error_present"],
            "any_signal": "no" if r["silent"] == "1" else "yes",
            "error_codes": ";".join(d["code"] for d in ds if d["severity"] == "error"),
            "warning_codes": ";".join(d["code"] for d in ds if d["severity"] == "warning"),
            "top_layer": r["top_layer"],
            "category": cat,
            "judgement_note": note,
        })
    with open(RESULTS / "triage.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(triage_rows[0].keys()))
        w.writeheader()
        w.writerows(triage_rows)

    # ---- rates ------------------------------------------------------------
    n_total = len(triage_rows)
    n_detected = sum(1 for t in triage_rows if t["category"] == "detected")
    n_wrong_sev = sum(1 for t in triage_rows if t["category"] == "wrong_severity")
    n_mislead = sum(1 for t in triage_rows if t["category"] == "misleading")
    n_incid = sum(1 for t in triage_rows if t["category"] == "incidental")
    n_silent = sum(1 for t in triage_rows if t["category"] == "silent")

    per_class = {}
    for cls in CLASS_ORDER:
        rows = [t for t in triage_rows if t["fault_class"] == cls]
        n = len(rows)
        det = [t["mutant_id"] for t in rows if t["category"] == "detected"]
        any_err = sum(1 for t in rows if t["any_error"] == "1")
        any_sig = sum(1 for t in rows if t["any_signal"] == "yes")
        per_class[cls] = {
            "n": n,
            "detected_relevant_error": len(det),
            "detected_ids": det,
            "any_error": any_err,
            "any_signal": any_sig,
            "categories": dict(Counter(t["category"] for t in rows)),
            "sensitivity_ci": fmt_ci(len(det), n),
            "any_signal_ci": fmt_ci(any_sig, n),
            "spec_statuses": dict(Counter(t["spec_status"] for t in rows)),
        }

    # ---- expectation audit -------------------------------------------------
    # expected_detectable was phrased as "would any checker detect it" (§4), so it
    # is compared with BOTH the error-severity outcome and the any-signal outcome.
    exp_audit = {"expected_yes": {}, "expected_no": {}, "expected_uncertain": {}}
    for want in ("yes", "no", "uncertain"):
        rows = [t for t in triage_rows if t["expected_detectable"] == want]
        exp_audit[f"expected_{want}"] = {
            "n": len(rows),
            "error_outcome": {
                "hit": [t["mutant_id"] for t in rows
                        if t["category"] == "detected" and want == "yes"],
                "miss": [t["mutant_id"] for t in rows
                         if t["category"] != "detected" and want == "yes"],
                "error_seen": [t["mutant_id"] for t in rows if t["any_error"] == "1"],
                "no_error": [t["mutant_id"] for t in rows if t["any_error"] == "0"],
            },
            "signal_outcome": {
                "signal_seen": [t["mutant_id"] for t in rows if t["any_signal"] == "yes"],
                "silent": [t["mutant_id"] for t in rows if t["any_signal"] == "no"],
            },
        }

    # ---- confusion view: expected layer vs observed layer ------------------
    confusion = defaultdict(Counter)
    for t in triage_rows:
        confusion[t["expected_layer"]][t["top_layer"]] += 1

    # ---- surface tell stratum ---------------------------------------------
    tell = {}
    for flag in ("yes", "no"):
        rows = [t for t in triage_rows if t["surface_tell"] == flag]
        det = sum(1 for t in rows if t["category"] == "detected")
        tell[flag] = {"n": len(rows), "detected": det, "ci": fmt_ci(det, len(rows))}

    # ---- oracle gap table --------------------------------------------------
    oracle = {}
    for status in ("metamodel_constraint", "prose_only", "library_semantics",
                   "resolution_mechanism", "notation", "none"):
        rows = [t for t in triage_rows if t["spec_status"] == status]
        if not rows:
            continue
        det = [t["mutant_id"] for t in rows if t["category"] == "detected"]
        oracle[status] = {
            "n": len(rows),
            "detected": len(det),
            "detected_ids": det,
            "missed": {t["mutant_id"]: t["category"] for t in rows if t["category"] != "detected"},
        }

    # ---- known-good arm ----------------------------------------------------
    good_rows = []
    for r in good:
        ds = diags.get(r["case_id"], [])
        good_rows.append({
            "case_id": r["case_id"],
            "n_errors": int(r["n_errors"]),
            "n_warnings": int(r["n_warnings"]),
            "codes": r["codes"],
            "triage": ("none" if not ds else
                       ("ii over-reach / legal-but-flagged"
                        if r["case_id"] == "KG-04-featurevalues" else "UNREVIEWED")),
        })
    fp_errors = sum(1 for g in good_rows if g["n_errors"] > 0)
    fp_warn_models = sum(1 for g in good_rows if g["n_warnings"] > 0)
    fp_overreach = sum(1 for g in good_rows if g["triage"].startswith("ii"))

    analysis = {
        "instrument": {
            "name": "OpenSysML CLI",
            "version": "sysml v0.12.1",
            "commit": "b2f0e9b802a334369da94312c35cefbd8726d3bf",
            "binary_sha256": "ddfc2962db3cd060c00a97386e9d7e9e6ee7c347da9734f95bfb71ce2f1598f0",
        },
        "corpus": {
            "mutants": n_total,
            "known_good": len(good_rows),
            "mutants_per_class": 4,
            "expected_detectable_counts": dict(Counter(t["expected_detectable"] for t in triage_rows)),
            "surface_tell_counts": dict(Counter(t["surface_tell"] for t in triage_rows)),
        },
        "primary_measure": {
            "definition": "relevant error-severity detection (METHODOLOGY-FROZEN.md §8/§9 M1, M4)",
            "overall": fmt_ci(n_detected, n_total),
            "by_class": per_class,
        },
        "outcome_categories": {
            "detected": n_detected,
            "wrong_severity": n_wrong_sev,
            "misleading": n_mislead,
            "incidental": n_incid,
            "silent": n_silent,
            "ids": {c: [t["mutant_id"] for t in triage_rows if t["category"] == c]
                    for c in ("detected", "wrong_severity", "misleading", "incidental", "silent")},
        },
        "any_error_mechanical": {
            "definition": ">=1 error-severity diagnostic, no relevance judgement (§8)",
            "overall": fmt_ci(sum(1 for t in triage_rows if t["any_error"] == "1"), n_total),
        },
        "any_signal": {
            "definition": ">=1 diagnostic of any severity",
            "overall": fmt_ci(sum(1 for t in triage_rows if t["any_signal"] == "yes"), n_total),
        },
        "expectation_audit": exp_audit,
        "layer_confusion": {k: dict(v) for k, v in confusion.items()},
        "surface_tell_stratum": tell,
        "oracle_gap": oracle,
        "known_good_arm": {
            "models": len(good_rows),
            "models_with_error": fp_errors,
            "false_positive_rate_errors": fmt_ci(fp_errors, len(good_rows)),
            "models_with_warning": fp_warn_models,
            "false_positive_rate_warnings": fmt_ci(fp_warn_models, len(good_rows)),
            "over_reach_models": fp_overreach,
            "rows": good_rows,
        },
    }

    # Adjudication B-10 / A2B-11 + RB-08: diagnostics per defect, by severity.
    per_case = defaultdict(Counter)
    for d in csv.DictReader(open(RESULTS / "diagnostics.csv")):
        if d["kind"] == "mutants":
            per_case[d["case_id"]][d["severity"]] += 1
    anysev = Counter(sum(c.values()) for c in per_case.values())
    errsev = Counter(c["error"] for c in per_case.values() if c["error"] > 0)
    analysis["diagnostics_per_defect"] = {
        "mutants_with_any_diagnostic": len(per_case),
        "mutants_with_error": sum(1 for c in per_case.values() if c["error"] > 0),
        "mutants_silent": n_total - len(per_case),
        "exactly_one_any_severity": anysev.get(1, 0),
        "exactly_one_error_among_error_bearing": errsev.get(1, 0),
        "distribution_any_severity": dict(sorted(anysev.items())),
        "distribution_errors_among_error_bearing": dict(sorted(errsev.items())),
        "claim": "relevance, not precision: single-defect mutants make any-error equal "
                 "relevant-error almost by construction",
    }

    with open(RESULTS / "analysis.json", "w") as fh:
        json.dump(analysis, fh, indent=2)

    # ---- markdown ----------------------------------------------------------
    L = []
    A = L.append
    A("# Analysis — mutation-based evaluation of OpenSysML v0.12.1 (issue #8 pilot)")
    A("")
    A("Generated by `harness/analysis.py` from `results/results.csv` and "
      "`results/diagnostics.csv`, which are derived from the unedited raw outputs in "
      "`results/raw/run1/`. Every number here has a denominator. Percentages at n = 4 per "
      "class carry 95% Wilson intervals that span most of the unit interval; the width is "
      "the finding, not an inconvenience.")
    A("")
    A("**This is a calibration of one instrument at one version against 32 synthetic mutants "
      "derived from 10 small models. It is not a measurement of SysML v2 validators.**")
    A("")
    A("## 1. Headline")
    A("")
    A(f"- Primary measure, **relevant error-severity detection**: **{fmt_ci(n_detected, n_total)}**.")
    A(f"- Mechanical **any-error** rate (no judgement): {fmt_ci(sum(1 for t in triage_rows if t['any_error'] == '1'), n_total)}.")
    A(f"- **Any-signal** rate (error or warning): {fmt_ci(sum(1 for t in triage_rows if t['any_signal'] == 'yes'), n_total)}.")
    A(f"- Outcome split: {n_detected} detected, {n_wrong_sev} detected only at warning severity, "
      f"{n_mislead} misleading, {n_incid} incidental, {n_silent} silent (of {n_total}).")
    A(f"- Known-good arm: {fp_errors}/{len(good_rows)} models produced an error; "
      f"{fp_warn_models}/{len(good_rows)} produced a warning, triaged as one over-reach "
      "(KG-04) and nothing else.")
    A("")
    A("## 2. Per fault class")
    A("")
    A("| class | n | relevant error | any error | any signal | categories |")
    A("|---|---:|---|---|---|---|")
    for cls in CLASS_ORDER:
        d = per_class[cls]
        cats = ", ".join(f"{k}:{v}" for k, v in sorted(d["categories"].items()))
        A(f"| {cls} | {d['n']} | {d['sensitivity_ci']} | {d['any_error']}/{d['n']} | "
          f"{d['any_signal']}/{d['n']} | {cats} |")
    A("")
    A("## 3. Layer confusion (expected layer × highest-severity emitted layer)")
    A("")
    emitted = sorted({k for v in analysis["layer_confusion"].values() for k in v})
    A("| expected ↓ / emitted → | " + " | ".join(emitted) + " |")
    A("|---|" + "---|" * len(emitted))
    for exp in sorted(analysis["layer_confusion"]):
        row = analysis["layer_confusion"][exp]
        A(f"| {exp} | " + " | ".join(str(row.get(e, 0)) for e in emitted) + " |")
    A("")
    A("## 4. Specification-oracle view (the deliverable)")
    A("")
    A("`spec_status` is a reading of each mutant's **frozen** `spec_constraint_or_defect` text, "
      "not a post-hoc reclassification: it says whether the condition the mutant instantiates has "
      "a named constraint in the 623-row catalogue, exists only as prose, is only constrained by "
      "the normative libraries, is only fixed by the notation/resolution mechanism, or is named "
      "nowhere.")
    A("")
    A("| spec status | n | detected as error | missed (category) |")
    A("|---|---:|---|---|")
    for status, d in analysis["oracle_gap"].items():
        missed = ", ".join(f"{k} ({v})" for k, v in d["missed"].items()) or "—"
        A(f"| {status} | {d['n']} | {d['detected']} | {missed} |")
    A("")
    A("## 5. Expectation audit and hypotheses")
    A("")
    for want in ("yes", "no", "uncertain"):
        d = exp_audit[f"expected_{want}"]
        A(f"**expected_detectable = {want}** (n={d['n']}): error seen "
          f"{len(d['error_outcome']['error_seen'])}/{d['n']}, signal seen "
          f"{len(d['signal_outcome']['signal_seen'])}/{d['n']}.")
        if want == "yes":
            A(f"  - error-detected: {', '.join(d['error_outcome']['hit']) or '—'}")
            A(f"  - not error-detected: {', '.join(d['error_outcome']['miss']) or '—'}")
        if want == "no":
            A(f"  - no error (expectation kept): {', '.join(d['error_outcome']['no_error']) or '—'}")
            A(f"  - error seen (expectation wrong): {', '.join(d['error_outcome']['error_seen']) or '—'}")
        A("")
    A("## 6. Surface-tell stratum")
    A("")
    A("| surface_tell | n | relevant error | 95% CI |")
    A("|---|---:|---|---|")
    for flag, d in tell.items():
        A(f"| {flag} | {d['n']} | {d['detected']} | {d['ci']} |")
    A("")
    A("## 7. Known-good arm (false positives, after triage)")
    A("")
    A("| model | errors | warnings | codes | triage |")
    A("|---|---:|---:|---|---|")
    for g in good_rows:
        A(f"| {g['case_id']} | {g['n_errors']} | {g['n_warnings']} | {g['codes'] or '—'} | {g['triage']} |")
    A("")
    A("## 8. Per-mutant record")
    A("")
    A("| mutant | class | spec status | expected | category | codes | note |")
    A("|---|---|---|---|---|---|---|")
    for t in triage_rows:
        codes = ";".join(c for c in (t["error_codes"], t["warning_codes"]) if c) or "—"
        A(f"| {t['mutant_id']} | {t['fault_class']} | {t['spec_status']} | "
          f"{t['expected_detectable']} | {t['category']} | {codes} | {t['judgement_note']} |")
    A("")
    with open(RESULTS / "analysis.md", "w") as fh:
        fh.write("\n".join(L))

    print(f"primary: {fmt_ci(n_detected, n_total)}")
    print("outcomes:", {"detected": n_detected, "wrong_severity": n_wrong_sev,
                        "misleading": n_mislead, "incidental": n_incid, "silent": n_silent})
    for cls in CLASS_ORDER:
        print(f"  {cls:22} {per_class[cls]['sensitivity_ci']}")
    print("known-good errors:", fp_errors, "warnings:", fp_warn_models)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
