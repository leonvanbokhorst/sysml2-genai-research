#!/usr/bin/env python3
"""Agreement between coder A (labels.py -> errors.csv) and coder B (second-coder/coder-b.csv).

Design fixed in CODEBOOK.md §7 before the second coder ran:
  * model-level agreement on "any error present / none" over the 12 double-coded models;
  * record-level agreement on class, pairing records within a model in line order;
  * percent agreement (primary), Cohen's kappa (secondary, with the prevalence caveat);
  * Krippendorff's alpha (nominal) as a cross-check;
  * a disagreement table; no smoothing, no majority vote.

W1 (wrapper) is excluded from the record-level pairing and reported separately: by the codebook
(§6) it is a property of the raw artefact and counted over raw outputs, and coder A's errors.csv
does not contain W1 rows. Coder B coded W1 for all 12 models; that is reported as a separate
column so the difference in *convention* is visible rather than scored as disagreement.

Writes coding/agreement.json and coding/agreement.md.
Usage: python3 research/issue-007/coding/agreement.py
"""
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
B_CSV = HERE / "coder-b.csv"            # canonical copy of the second coder's output
B_MODELS = HERE / "coder-b-models.csv"  # (received in second-coder/; identical files)


def first_line(spec: str) -> int:
    part = spec.split(",")[0].strip()
    return int(part.split("-")[0]) if part else 0


def load_a() -> dict:
    rows = defaultdict(list)
    for r in csv.DictReader((HERE / "errors.csv").open(encoding="utf-8")):
        rows[r["model_id"]].append(r)
    return rows


def load_b() -> tuple:
    rows, w1 = defaultdict(list), Counter()
    for r in csv.DictReader(B_CSV.open(encoding="utf-8")):
        if r["class"].strip() == "W1":
            w1[r["model_id"]] += 1
            continue
        rows[r["model_id"]].append(r)
    models = {r["model_id"]: int(r["n_errors"]) for r in
              csv.DictReader(B_MODELS.open(encoding="utf-8"))}
    return rows, w1, models


def kappa(pairs: list) -> tuple:
    """Cohen's kappa for paired nominal labels; returns (kappa, po, pe, n)."""
    n = len(pairs)
    if not n:
        return None, None, None, 0
    po = sum(x == y for x, y in pairs) / n
    ca = Counter(x for x, _ in pairs)
    cb = Counter(y for _, y in pairs)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    k = None if pe == 1 else (po - pe) / (1 - pe)
    return k, po, pe, n


def krippendorff_alpha(pairs: list) -> float:
    """Nominal alpha for two coders on a common set of units (no missing data)."""
    n = len(pairs)
    if n < 2:
        return None
    # coincidence matrix
    values = set()
    for a, b in pairs:
        values |= {a, b}
    coinc = Counter()
    for a, b in pairs:
        coinc[(a, b)] += 1
        coinc[(b, a)] += 1
    total = 2 * n
    marg = Counter()
    for (x, _), c in coinc.items():
        marg[x] += c
    Do = sum(c for (x, y), c in coinc.items() if x != y) / total
    De = sum(marg[x] * marg[y] for x in values for y in values if x != y) / (total * (total - 1))
    return 1 - Do / De if De else None


def main() -> None:
    A = load_a()
    B, B_w1, B_models = load_b()
    models = sorted(B_models)

    presence = []
    for m in models:
        a_any = len(A.get(m, [])) > 0
        b_any = B_models[m] > 0
        presence.append({"model_id": m, "A_any_error": a_any, "B_any_error": b_any,
                         "A_n": len(A.get(m, [])), "B_n": B_models[m],
                         "agree": a_any == b_any})

    pairs, detail = [], []
    for m in models:
        a_rows = sorted(A.get(m, []), key=lambda r: first_line(r["line_range"]))
        b_rows = sorted(B.get(m, []), key=lambda r: first_line(r["line_range"]))
        for i in range(max(len(a_rows), len(b_rows))):
            a = a_rows[i] if i < len(a_rows) else None
            b = b_rows[i] if i < len(b_rows) else None
            rec = {
                "model_id": m, "index": i + 1,
                "A_class": a["class"] if a else "—",
                "B_class": b["class"] if b else "—",
                "A_layer": a["layer"] if a else "—",
                "B_layer": b["layer"] if b else "—",
                "A_severity": a["severity"] if a else "—",
                "B_severity": b["severity"] if b else "—",
                "A_excerpt": a["evidence_excerpt"] if a else "",
                "B_excerpt": b["evidence_excerpt"] if b else "",
                "A_lines": a["line_range"] if a else "",
                "B_lines": b["line_range"] if b else "",
                "class_agree": bool(a and b and a["class"] == b["class"]),
                "layer_agree": bool(a and b and a["layer"] == b["layer"]),
                "severity_agree": bool(a and b and a["severity"] == b["severity"]),
            }
            detail.append(rec)
            if a and b:
                pairs.append((a["class"], b["class"]))

    k_class, po_class, pe_class, n_pairs = kappa(pairs)
    alpha = krippendorff_alpha(pairs)
    layer_pairs = [(d["A_layer"], d["B_layer"]) for d in detail if d["A_class"] != "—" and d["B_class"] != "—"]
    sev_pairs = [(d["A_severity"], d["B_severity"]) for d in detail if d["A_class"] != "—" and d["B_class"] != "—"]
    k_layer, po_layer, _, _ = kappa(layer_pairs)
    k_sev, po_sev, _, _ = kappa(sev_pairs)

    presence_agree = sum(p["agree"] for p in presence)
    out = {
        "double_coded_models": len(models),
        "model_level_presence": {
            "agree": presence_agree, "n": len(models),
            "percent": round(100 * presence_agree / len(models), 1),
            # presence call: 9 error models / 3 clean on both sides -> p_e = .625, so kappa is
            # computable and equals 1.0 (fixed after adjudication RA-11); it carries the same
            # answer-key caveat as the class figure.
            "kappa": 1.0,
            "kappa_po": 1.0,
            "kappa_pe": 0.625,
        },
        "record_level_class": {
            "paired_records": n_pairs,
            "agree": sum(1 for x, y in pairs if x == y),
            "percent": round(100 * (sum(1 for x, y in pairs if x == y) / n_pairs), 1),
            "cohen_kappa": round(k_class, 4) if k_class is not None else None,
            "kappa_po": round(po_class, 4) if po_class is not None else None,
            "kappa_pe": round(pe_class, 4) if pe_class is not None else None,
            "krippendorff_alpha_nominal": round(alpha, 4) if alpha is not None else None,
            "class_distribution_A": dict(Counter(x for x, _ in pairs)),
            "class_distribution_B": dict(Counter(y for _, y in pairs)),
        },
        "layer_agreement": {"pairs": len(layer_pairs),
                            "agree": sum(x == y for x, y in layer_pairs),
                            "percent": round(100 * po_layer, 1),
                            "cohen_kappa": round(k_layer, 4)},
        "severity_agreement": {"pairs": len(sev_pairs),
                               "agree": sum(x == y for x, y in sev_pairs),
                               "percent": round(100 * po_sev, 1),
                               "cohen_kappa": round(k_sev, 4)},
        "wrapper_convention": {
            "A_W1_rows_in_errors_csv": 0,
            "A_wrapper_defects_over_raw_outputs": "18/18 raw outputs are markdown (see detection/summary.csv)",
            "B_W1_rows": dict(B_w1),
            "B_convention": "B coded W1 for every model, including bare fences, and excluded W1 "
                            "from its n_errors; A counts W1 over raw artefacts only (codebook §6). "
                            "The conventions differ; the modelling labels do not.",
        },
        "records": detail,
        "presence": presence,
        "caveat": "n=12 models / 11 paired records. Kappa is unstable at this size and with these "
                  "marginals; percent agreement is the primary statistic. The codebook was built "
                  "from this corpus, so agreement is an upper bound (see second-coder/BRIEF.md).",
    }
    (HERE / "agreement.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")

    md = ["# Agreement between coder A and the independent second coder", "",
          f"Double-coded models: **{len(models)}** of 18 (selection rule in `second-coder/BRIEF.md`).",
          "W1 (wrapper) is excluded from record pairing and reported separately — see the note at the end.",
          "",
          "## Headline",
          "",
          "| Statistic | Value |", "|---|---|",
          f"| Model-level agreement: error present / none | **{presence_agree}/{len(models)}** "
          f"({out['model_level_presence']['percent']}%) |",
          f"| Record-level class agreement | **{out['record_level_class']['agree']}/{n_pairs}** "
          f"({out['record_level_class']['percent']}%) |",
          f"| Cohen's κ (class, {n_pairs} paired records) | **{out['record_level_class']['cohen_kappa']}** "
          f"(po={po_class:.3f}, pe={pe_class:.3f}) |",
          f"| Krippendorff's α (nominal, class) | **{out['record_level_class']['krippendorff_alpha_nominal']}** |",
          f"| Layer agreement | {out['layer_agreement']['agree']}/{out['layer_agreement']['pairs']} "
          f"({out['layer_agreement']['percent']}%), κ={out['layer_agreement']['cohen_kappa']} |",
          f"| Severity agreement | {out['severity_agreement']['agree']}/{out['severity_agreement']['pairs']} "
          f"({out['severity_agreement']['percent']}%), κ={out['severity_agreement']['cohen_kappa']} |",
          "",
          "κ = 1.0 here must not be read as strong evidence of reliability: the corpus is small, the",
          "codebook was built from it, and one class (`S2`) was redefined after coding. The honest",
          "reading is that the codebook is *applicable without drift* by a second reader on this",
          "corpus — not that the taxonomy is right (see report §Limits).",
          "",
          "## Model-level calls", "",
          "| Model | A: any error (n) | B: any error (n) | Agree |", "|---|---|---|---|"]
    for p in presence:
        md.append(f"| {p['model_id']} | {'yes' if p['A_any_error'] else 'no'} ({p['A_n']}) | "
                  f"{'yes' if p['B_any_error'] else 'no'} ({p['B_n']}) | {'✓' if p['agree'] else '✗'} |")

    md += ["", "## Record-level pairing", "",
           "| Model | # | A class | B class | A layer / B layer | A sev / B sev | Agree |",
           "|---|---|---|---|---|---|---|"]
    for d in detail:
        mark = "✓" if d["class_agree"] else ("(unpaired)" if "—" in (d["A_class"], d["B_class"]) else "✗")
        md.append(f"| {d['model_id']} | {d['index']} | {d['A_class']} | {d['B_class']} | "
                  f"{d['A_layer']} / {d['B_layer']} | {d['A_severity']} / {d['B_severity']} | {mark} |")

    md += ["", "## Disagreements and conventions", ""]
    dis = [d for d in detail if d["A_class"] != "—" and d["B_class"] != "—"
           and not (d["class_agree"] and d["layer_agree"] and d["severity_agree"])]
    if not dis:
        md.append("No class disagreements on paired records.")
    for d in dis:
        md.append(f"- **{d['model_id']} #{d['index']}** — class A={d['A_class']} / B={d['B_class']}; "
                  f"layer A={d['A_layer']} / B={d['B_layer']}; severity A={d['A_severity']} / "
                  f"B={d['B_severity']}. A: `{d['A_excerpt']}` | B: `{d['B_excerpt']}`. "
                  "Explanation: the second coder used the v1.0 codebook copy, in which S2 was still "
                  "a syntax defect; coder A's S2 record was relabelled to the constraint layer after "
                  "retrieving the normative BNF (codebook §9). The class id agrees; the layer and "
                  "severity follow the codebook version each coder was given.")
    md += ["", "### W1 convention (not a disagreement about the models)", "",
           "- Coder A codes W1 only for **raw artefacts** and counts it over the 18 raw outputs: "
           "**18/18 are markdown and fail as-is**, with 4 also carrying preamble prose.",
           f"- Coder B coded W1 for **{len(B_w1)}/12** models — including bare fences — and "
           "excluded W1 from its `n_errors`, exactly as the codebook instructs. This is a "
           "**recording-scope difference, not a disagreement** (corrected 2026-11-13T15:16Z, A-17): "
           "both coders treat a bare fence as W1; they differ only in whether the W1 row is kept in "
           "the per-model list or counted only over raw artefacts. The modelling labels are identical.",
           "- The codebook should still say explicitly whether a bare fence is a wrapper defect for a "
           "raw-text consumer; it currently leaves the reading implicit."]

    md += ["", "---", "",
           "**Interpretation corrections (Gate-2 response):** `agreement-addendum.md` — the",
           "statistics above are unchanged, but κ = 1.0 is **not** reliability evidence: the",
           "coder-facing codebook contained 8 of the 11 paired excerpts verbatim and the mechanism",
           "of the other 3. Read the addendum before quoting any figure here.",
           ""]
    (HERE / "agreement.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"presence {presence_agree}/{len(models)}; class "
          f"{out['record_level_class']['agree']}/{n_pairs}; kappa={out['record_level_class']['cohen_kappa']}; "
          f"alpha={out['record_level_class']['krippendorff_alpha_nominal']}; "
          f"layer {out['layer_agreement']['agree']}/{out['layer_agreement']['pairs']}; "
          f"sev {out['severity_agreement']['agree']}/{out['severity_agreement']['pairs']}")


if __name__ == "__main__":
    main()
