#!/usr/bin/env python3
"""Apply the Gate-2 corrections to the DERIVED population files, without editing the frozen ones.

Inputs (never modified here):
  coding/errors.csv                    the frozen pre-detection population (14 records)
  coding/errors-post-inspection.csv    the post-detection arm (7 records, one withdrawn)
  coding/errors-corrections.csv        the dated corrections (Gate-2 response)
  corpus/extraction-log.json           wrapper facts per raw output

Outputs:
  coding/errors-combined.csv           corrected combined population (status per record)
  coding/models.csv                    per-model counts refreshed; trailing_prose_present added
  coding/reconciliation.md             the per-row reconciliation table Reviewer B asked for

The frozen files keep their bytes (and their hashes, which Reviewer B pinned). Anything a reader
wants to check against the review can be diffed against `errors-corrections.csv`.

Usage: python3 research/issue-007/coding/apply_corrections.py
"""
import csv
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FIELDS = ["model_id", "error_id", "class", "layer", "severity", "evidence_excerpt",
          "line_range", "spec_constraint", "notes"]
EXTRA = ["discovery_route", "verification"]


def load(path):
    return list(csv.DictReader(path.open(encoding="utf-8")))


def main() -> None:
    frozen = load(HERE / "errors.csv")
    post = load(HERE / "errors-post-inspection.csv")
    corrections = load(HERE / "errors-corrections.csv")

    rows = {}
    for r in frozen:
        rows[r["error_id"]] = {**r, "population": "frozen_pre_detection", "status": "frozen",
                               "corrections": ""}
    for r in post:
        rows[r["error_id"]] = {**r, "population": "post_inspection_verified",
                               "status": "post_inspection", "corrections": ""}

    withdrawn = set()
    for c in corrections:
        if c["action"] == "withdraw":
            withdrawn.add(c["target_id"])
            continue
        if c["action"] == "note":
            continue          # a correction with no record-level effect (kept in the register)
        if c["action"] != "set":
            continue
        target = rows.get(c["target_id"])
        if target is None:
            raise SystemExit(f"correction target missing: {c['target_id']}")
        target[c["field"]] = c["new_value"]
        target["corrections"] = (target["corrections"] + ";" + c["correction_id"]).lstrip(";")

    combined = [rows[k] for k in sorted(rows) if k not in withdrawn]

    # Contract added after Reviewer B's O1: every excerpt part must be a substring of its model
    # (whitespace-normalised). This is the check that should have caught the phantom row.
    def norm(s):
        return " ".join(s.split())

    problems = []
    for r in combined:
        model = (ROOT / "corpus" / "normalized" / f"{r['model_id']}.sysml").read_text(encoding="utf-8")
        body = norm(model)
        for part in r["evidence_excerpt"].split(" / "):
            part = part.strip()
            if part and norm(part) not in body:
                problems.append((r["error_id"], part[:60]))
    if problems:
        print("EXCERPT VERIFICATION FAILED:")
        for eid, part in problems:
            print(f"  {eid}: {part!r} not found in its model")
        raise SystemExit(1)
    print(f"excerpt verification: {len(combined)} records, all excerpt parts found in their models")
    out_fields = FIELDS + ["population", "status", "corrections"] + \
        [f for f in EXTRA if f in post[0]]
    with (HERE / "errors-combined.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=out_fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(combined)

    # ---- models.csv: refresh derived counts, add the missing wrapper variable ----
    log = {l["model_id"]: l for l in json.loads((ROOT / "corpus" / "extraction-log.json").read_text())}
    models = load(HERE / "models.csv")
    fields = list(models[0].keys())
    for extra in ("trailing_prose_present", "n_errors_combined", "contested_records"):
        if extra not in fields:
            fields.append(extra)
    by_model = {}
    for r in combined:
        by_model.setdefault(r["model_id"], []).append(r)
    for m in models:
        recs = by_model.get(m["model_id"], [])
        m["trailing_prose_present"] = "yes" if log[m["model_id"]].get("trailing", "").strip() else "no"
        m["n_errors_combined"] = str(len(recs))
        m["contested_records"] = ";".join(r["error_id"] for r in recs if r["status"] == "frozen_contested")
        m["classes_post_inspection"] = ";".join(sorted({r["class"] for r in recs}))
    with (HERE / "models.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(models)

    # ---- reconciliation table (B-O1/O2/O3) ----
    md = ["# Reconciliation after the Gate-2 corrections", "",
          "Frozen population (`errors.csv`, never edited): **%d records**." % len(frozen),
          "Post-inspection arm (`errors-post-inspection.csv`, never edited): **%d rows**, of which "
          "**%d withdrawn** (C01) → **%d live**."
          % (len(post), len([w for w in withdrawn if w.startswith(tuple(f"{r['model_id']}-P" for r in post))]),
             len([r for r in post if r["error_id"] not in withdrawn])),
          "Corrected combined population (`errors-combined.csv`): **%d records**." % len(combined),
          "",
          "| Population | Records | Models with ≥1 | Models clean |", "|---|---|---|---|"]
    for name, recs in (("frozen", frozen),
                       ("post-inspection (live)", [r for r in post if r["error_id"] not in withdrawn]),
                       ("combined (corrected)", combined)):
        ms = {r["model_id"] for r in recs}
        md.append(f"| {name} | {len(recs)} | {len(ms)} | {18 - len(ms)} |")
    md += ["", "## Class counts, frozen vs corrected combined", "",
           "| Class | Frozen | Combined (corrected) |", "|---|---|---|"]
    cf, cc = Counter(r["class"] for r in frozen), Counter(r["class"] for r in combined)
    for c in sorted(set(cf) | set(cc)):
        md.append(f"| {c} | {cf.get(c, 0)} | {cc.get(c, 0)} |")
    md += ["", "## Records touched by a correction", "",
           "| Record | Correction | Field | Old → New |", "|---|---|---|---|"]
    for c in corrections:
        if c["action"] == "set":
            md.append(f"| {c['target_id']} | {c['correction_id']} | {c['field']} | "
                      f"`{c['old_value'][:70]}` → `{c['new_value'][:70]}` |")
        elif c["action"] == "withdraw":
            md.append(f"| {c['target_id']} | {c['correction_id']} | row | withdrawn |")
    (HERE / "reconciliation.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    post_withdrawn = len([w for w in withdrawn if w.startswith(tuple(f"{r['model_id']}-P" for r in post))])
    print(f"frozen {len(frozen)} ({len(withdrawn) - post_withdrawn} withdrawn) | "
          f"post {len(post)} ({post_withdrawn} withdrawn) | combined {len(combined)}")
    print("frozen classes:", dict(Counter(r["class"] for r in frozen)))
    print("combined classes:", dict(Counter(r["class"] for r in combined)))
    print("combined layers:", dict(Counter(r["layer"] for r in combined)))
    print("contested:", [r["error_id"] for r in combined if r["status"] == "frozen_contested"])


if __name__ == "__main__":
    main()
