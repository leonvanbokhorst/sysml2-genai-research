#!/usr/bin/env python3
"""Build and freeze A's empirical error subset for Researcher B's external challenge set.

Ground truth only: no detection results, no validator-derived fields, no expectations. Every item is
a record from the corrected frozen population (`coding/errors-combined.csv`, population =
frozen_pre_detection), with its verbatim model excerpt, citable basis and provenance. The models are
copied so B runs a frozen artefact, not a live file.

Outputs (all under research/relational/empirical-subset/):
  subset.json                machine-readable items + controls
  models/<model>.sysml       frozen copies of the normalised models (18)
  raws/<model>.md            frozen copies of the raw outputs (18, wrapper context)
  models/manifest.csv        per-file sha256 + source path
  ITEM-TABLE.md              generated per-item table (also embedded in FROZEN-SUBSET.md)
  FROZEN-SUBSET.md           the human-readable freeze document, incl. the hash
  FROZEN-SUBSET-HASH.txt     sha256(subset.json) + sha256(models/manifest.csv) + UTC time

Usage: python3 research/relational/empirical-subset/build_subset.py
"""
import csv
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CODING = REPO / "research" / "issue-007" / "coding"
NORM = REPO / "research" / "issue-007" / "corpus" / "normalized"
RAW = REPO / "research" / "issue-007" / "raw"

# ---------------------------------------------------------------- per-item authored fields
# contested flags and the rival reading, per the C07/C05/C06 corrections and report §16/§17
CONTESTED = {
    "T1-C3-E01": ("defect status", "Rival reading accepted as live: a documentation band of 35-75 % "
                  "contains the declared 35-55 % bound, so a tightened engineering limit is not a "
                  "contradiction on its face. The record is kept (fixed before detection) and marked "
                  "contested; report with and without it."),
    "T4-C1-E02": ("layer", "Defect status not disputed; layer contested between type/typing (end-"
                  "feature multiplicity conformance, the recorded reading) and structural/architectural "
                  "(the rival reading)."),
    "T4-C3-E01": ("layer", "As T4-C1-E02: the connector's end chains through a multi-valued usage; "
                  "layer contested, defect status not disputed."),
}

CONFIDENCE = {
    "T1-C2-E01": "high", "T2-C1-E01": "high", "T3-C2-E01": "high", "T3-C2-E02": "high",
    "T3-C1-E01": "high", "T4-C2-E01": "high", "T5-C2-E01": "high", "T6-C2-E01": "high",
    "T2-C2-E01": "medium", "T4-C1-E01": "medium", "T4-C1-E02": "medium", "T4-C3-E01": "medium",
    "T1-C3-E01": "low",
}

SPEC_BASIS = {
    "N1": "No named OCL constraint covers name resolution. Basis: the identifier used in this "
          "construct is declared nowhere in scope (name resolution, SysML 2.0 §7.5 / KerML §8.3.2.4). "
          "For the satisfy-target records the name is the requirement definition's subject parameter, "
          "which is a feature of the definition and not of the package.",
    "N2": "Basis: the model uses SysML/KerML standard-library scalar types with no library import. "
          "The normative model libraries declare Real/Boolean; no named constraint requires the import.",
    "S2": "checkSatisfyRequirementUsageBindingConnector (§8.3.21.10), a discretionary MAY constraint: "
          "a SatisfyRequirementUsage must have exactly one BindingConnector between its subject and a "
          "satisfying feature. The textual production (§8.2.2.21.2) makes the 'by' clause optional, so "
          "this is a constraint-layer, not a notation, defect.",
    "T1": "InitialNodeMember: 'first' takes memberFeature = [QualifiedName], a cross-reference to a "
          "feature (SysML 2.0 §8.2.2.17.2). The referenced name resolves to an action DEFINITION "
          "(a type), not a feature/usage, so the succession cannot be formed.",
    "R1": "End-feature multiplicity conformance: after resolving the feature chain the end denotes "
          "more than one feature, so it is not 1..1. Nearest named rule validateFeatureEndMultiplicity "
          "(KerML §8.3.3.3.4, SHOULD); §7.13.2 states the same for connection ends. No named constraint "
          "decides chains over multi-valued usages: this is an authored criterion, stated below.",
    "I1": "No constraint relates documentation to declared values (deriveElementDocumentation, "
          "§8.3.2.1.2, relates documentation to content only). Basis is an authored reading, and it is "
          "contested.",
    "T2": "Decisive basis: §7.7.1 prose on attribute typing. Adjacent constraint "
          "checkAttributeUsageSpecialization (§8.3.7.3, MAY) requires an AttributeUsage to specialise "
          "Base::dataValues; the attribute here is typed by a PartDefinition.",
}

S1_BASIS = {
    "T1-C2-E01": "SatisfyRequirementUsage textual production (SysML 2.0 §8.2.2.21.2): the notation is "
                 "'satisfy <requirement> by <feature>' — neither 'to' nor the reversed operand order "
                 "is admitted, so the text is not in the language.",
    "T2-C1-E01": "States textual notation, transition productions (SysML 2.0 §8.2.2.18): a transition "
                 "states its ends as 'transition first <source> … then <target>'. 'from … to … on …' "
                 "is SysML v1/UML notation and is not admitted.",
    "T3-C2-E01": "Reserved-keyword list (SysML 2.0 §8.2.2.1.2) applied to the ID terminal: 'in' and "
                 "'out' are reserved keywords and cannot be written as unquoted feature names in a port "
                 "declaration; line 33 references the illegal name.",
}

# second-coder coverage: which of the 12 double-coded models each record sits in
DOUBLE_CODED = {"T1-C1", "T1-C2", "T2-C1", "T2-C2", "T3-C2", "T3-C3",
                "T4-C1", "T4-C2", "T5-C1", "T5-C2", "T6-C2", "T6-C3"}

CONTROL_NOTES = {
    "T1-C1": ("clean", "No coded defect in any population after C12 (the 'first start;' record was "
                       "withdrawn: Actions::Action declares an inherited 'start')."),
    "T2-C3": ("clean", "No coded defect in any population."),
    "T3-C3": ("clean", "No coded defect in any population; imports SI without writing a unit literal."),
    "T5-C1": ("clean", "No coded defect in any population; imports SI without writing a unit literal."),
    "T5-C3": ("frozen-clean-only", "NOT A CONTROL: carries a verified post-inspection defect "
                                    "(attribute window : VisibilityWindow; line 11, attribute typed by a "
                                    "part definition). A diagnostic on this model is not a false positive."),
    "T6-C1": ("frozen-clean-only", "NOT A CONTROL: carries a verified post-inspection defect "
                                    "(port return; line 26, reserved keyword as a name). A diagnostic on "
                                    "this model is not a false positive."),
    "T6-C3": ("frozen-clean-only", "NOT A CONTROL: carries a verified post-inspection defect "
                                    "(port return; line 26). A diagnostic on this model is not a false "
                                    "positive."),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    (HERE / "models").mkdir(exist_ok=True)
    (HERE / "raws").mkdir(exist_ok=True)

    combined = [r for r in csv.DictReader((CODING / "errors-combined.csv").open(encoding="utf-8"))
                if r["population"] == "frozen_pre_detection"]
    models = {r["model_id"]: r for r in csv.DictReader((CODING / "models.csv").open(encoding="utf-8"))}

    # ---- freeze the model files: every model that appears as an item or a control ----
    all_models = sorted({r["model_id"] for r in combined} |
                        {m for m in models})
    manifest = []
    for m in all_models:
        for kind, src, dst in (("normalised", NORM / f"{m}.sysml", HERE / "models" / f"{m}.sysml"),
                               ("raw", RAW / f"{m}.md", HERE / "raws" / f"{m}.md")):
            shutil.copyfile(src, dst)
            manifest.append({"model_id": m, "kind": kind,
                             "frozen_path": str(dst.relative_to(REPO)),
                             "source_path": str(src.relative_to(REPO)),
                             "sha256": sha(dst), "bytes": dst.stat().st_size})
    with (HERE / "models" / "manifest.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(manifest[0]))
        w.writeheader()
        w.writerows(manifest)

    items = []
    for r in combined:
        model = r["model_id"]
        npath = HERE / "models" / f"{model}.sysml"
        rpath = HERE / "raws" / f"{model}.md"
        cls = r["class"]
        basis = r["spec_constraint"].strip() or SPEC_BASIS.get(cls, "")
        if cls == "S1":
            basis = S1_BASIS.get(r["error_id"], basis)
        elif cls in ("S2", "R1", "T1", "N1", "N2", "I1"):
            basis = SPEC_BASIS[cls]
            if cls == "R1":
                basis += (" Criterion: a connection end is defective iff, after resolving its feature "
                          "chain, it denotes more than one feature.")
        contested, cnote = CONTESTED.get(r["error_id"], (False, ""))
        corr = ("second coder assigned the same class to this text; corroboration is WEAK because "
                "the coder-facing codebook contained this excerpt verbatim or its exemplar (see "
                "coding/agreement-addendum.md)") if model in DOUBLE_CODED else \
               "no independent corroboration (this model was not double-coded)"
        items.append({
            "item_id": f"ES-{r['error_id']}",
            "item_type": "error",
            "selection_batch": "frozen-1",
            "source_model": model,
            "normalized_path": str(npath.relative_to(REPO)),
            "raw_path": str(rpath.relative_to(REPO)),
            "model_sha256": sha(npath),
            "raw_sha256": sha(rpath),
            "error_class": cls,
            "layer": r["layer"],
            "spec_basis": basis,
            "evidence_excerpt": r["evidence_excerpt"],
            "line_range": r["line_range"],
            "frozen_label": cls,
            "contested": bool(contested),
            "contested_as": contested if contested else "",
            "contested_note": cnote,
            "confidence": CONFIDENCE[r["error_id"]],
            "independent_corroboration": corr,
            "second_coder_covered": model in DOUBLE_CODED,
            "notes": r["notes"],
        })

    controls = []
    for m, (tier, note) in CONTROL_NOTES.items():
        npath = HERE / "models" / f"{m}.sysml"
        rpath = HERE / "raws" / f"{m}.md"
        controls.append({
            "item_id": f"CTRL-{m}",
            "item_type": "control",
            "selection_batch": "controls-1",
            "control_tier": tier,
            "source_model": m,
            "normalized_path": str(npath.relative_to(REPO)),
            "raw_path": str(rpath.relative_to(REPO)),
            "model_sha256": sha(npath),
            "raw_sha256": sha(rpath),
            "error_class": None, "layer": None, "spec_basis": None,
            "evidence_excerpt": None, "line_range": None, "frozen_label": None,
            "contested": False, "contested_as": "", "contested_note": "",
            "confidence": None,
            "independent_corroboration": "not applicable (control)",
            "second_coder_covered": m in DOUBLE_CODED,
            "notes": note,
        })

    subset = {
        "subset": "A's empirical SysML v2 error subset (issue #7 pilot) — external challenge set for B",
        "frozen_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_population": "research/issue-007/coding/errors-combined.csv, population="
                             "frozen_pre_detection, after corrections C01-C12",
        "selection_rule": "include every frozen record that survived the corrections — a verbatim "
                          "excerpt in its own model, a citable basis, not withdrawn; mark contested "
                          "records contested with the rival reading; exclude withdrawn records and "
                          "records whose discovery was instrument-surfaced without independent "
                          "verification; add the models with no coded defect as controls in two tiers.",
        "counts": {"error_items": len(items), "contested_items": sum(i["contested"] for i in items),
                   "control_items": len(controls),
                   "controls_clean": sum(c["control_tier"] == "clean" for c in controls),
                   "controls_frozen_clean_only": sum(c["control_tier"] == "frozen-clean-only"
                                                     for c in controls),
                   "models_frozen": len(all_models)},
        "excluded": [
            {"id": "T1-C1-E01", "reason": "withdrawn under correction C12: the normative library "
                                          "declares Actions::Action::start, so 'first start;' resolves"},
            {"id": "T5-C3-P01", "reason": "withdrawn under correction C01: excerpt 'port return;' does "
                                          "not exist in T5-C3 (phantom duplicate of T6-C1-P01)"},
            {"id": "post-inspection batch (6 records)", "reason": "verified notation defects that the "
             "instrument's diagnostics surfaced; kept out of the challenge set because their discovery "
             "route makes them non-independent for a detection measurement. They remain in "
             "research/issue-007/coding/errors-combined.csv with status=post_inspection."},
        ],
        "operational_criterion_R1": "A connection end is defective iff, after resolving its feature "
                                    "chain, it denotes more than one feature (the chain traverses a "
                                    "usage whose multiplicity admits more than one instance), so the "
                                    "connector as written does not relate individual features.",
        "items": items + controls,
    }

    (HERE / "subset.json").write_text(json.dumps(subset, indent=2) + "\n", encoding="utf-8")
    h_json = sha(HERE / "subset.json")
    h_man = sha(HERE / "models" / "manifest.csv")
    stamp = subset["frozen_utc"]

    # ---- generated per-item table ----
    md = ["| item_id | model | class | layer | contested | confidence | excerpt | lines |",
          "|---|---|---|---|---|---|---|---|"]
    for i in items:
        md.append(f"| {i['item_id']} | {i['source_model']} | {i['error_class']} | {i['layer']} | "
                  f"{'yes (' + i['contested_as'] + ')' if i['contested'] else 'no'} | {i['confidence']} | "
                  f"`{i['evidence_excerpt'][:58]}` | {i['line_range']} |")
    md += ["", "| control_id | model | tier | second coder covered | note |", "|---|---|---|---|---|"]
    for c in controls:
        md.append(f"| {c['item_id']} | {c['source_model']} | {c['control_tier']} | "
                  f"{'yes' if c['second_coder_covered'] else 'no'} | {c['notes'][:90]} |")
    (HERE / "ITEM-TABLE.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    doc = f"""# FROZEN SUBSET — A's empirical SysML v2 errors, for B's external challenge set

**Frozen at (UTC):** {stamp}
**subset.json sha256:** `{h_json}`
**models/manifest.csv sha256:** `{h_man}`
**Owner:** Researcher A (issue #7 pilot). **Consumer:** Researcher B (issue #8), as the *external*
challenge set — separate from B's synthetic mutants.

## What this is

{len(items)} error items from the corrected frozen error population of A's 18-model corpus, plus
{len(controls)} control models. Each item is one defect mechanism, with the verbatim model excerpt,
the line range, the class and layer A assigned, the specification or model-text basis, A's
confidence, and its corroboration status. The normalised model and the raw output are copied into
`models/` and `raws/` and hashed in `models/manifest.csv`, so this is a frozen artefact: B runs the
files here, not the live corpus.

## Selection rule (stated before freezing)

> Include every record from the frozen population that **survived the corrections**: supported by a
> verbatim excerpt in its own model, with a citable basis, and not withdrawn. Include contested
> records and mark them contested with the rival reading named. Exclude withdrawn records and any
> record whose discovery was instrument-surfaced without independent verification. Add the models
> with no coded defect as controls, in two tiers, clearly labelled.

The rule produced: **13 error items** (10 unqualified, 3 contested), **0 withdrawn**, **7 controls**
(4 clean-tier, 3 frozen-clean-only), across all 18 models. No item was selected for its detection
outcome; this file contains **no detection results and no validator-derived fields** (rule 1 of the
freeze instruction). A's detection results stay in A's own report; B must measure independently.

## Items

{open(HERE / 'ITEM-TABLE.md').read()}

## Per-item notes that matter for B's measurement

- **Contested records.** `T1-C3-E01` (I1) has a live rival reading (a tightened limit is not a
  contradiction); report the rate with and without it. `T4-C1-E02` and `T4-C3-E01` (R1) are not
  disputed as defects, but their *layer* is contested between `type/typing` (recorded) and
  `structural/architectural` (rival).
- **R1's operational criterion** (so a new model can be judged without asking me): *a connection end
  is defective iff, after resolving its feature chain, it denotes more than one feature.*
- **Corroboration.** 10 of the 13 items sit in models the second coder also coded, but its
  corroboration is weak: the coder-facing codebook contained those excerpts verbatim or their
  exemplars (`research/issue-007/coding/agreement-addendum.md`). 3 items (`T1-C3-E01`, `T3-C1-E01`,
  `T4-C3-E01`) have **no** independent corroboration. No item is corroborated by the external corpus.
- **Confidence** is A's own: 8 high, 4 medium, 1 low (the contested I1).

## Controls — read the tiers before using them as a false-positive arm

- **`clean` tier (4 models: T1-C1, T2-C3, T3-C3, T5-C1):** no coded defect in any population. They
  are *clean as far as A's coding goes* — **not** known-good by construction and **not**
  independently certified. A false-positive rate computed on four short models is a falsification of
  a gross over-reach, not an estimate.
- **`frozen-clean-only` tier (3 models: T5-C3, T6-C1, T6-C3):** clean in the *frozen* population but
  each carries a **verified post-inspection defect** (a reserved keyword used as a name; an attribute
  typed by a part definition). **Do not use these as controls**: a diagnostic on them is not a false
  positive. They are included so the record is complete, not so they can be scored.

## What this subset is NOT

1. **Not a representative sample of generation errors.** 13 records from 18 models, one generator
   family, six prompts authored by the same agent that coded the models. Any rate computed on it is
   a property of this corpus.
2. **Not independently labelled.** The generator, coder and selector are the same agent. The second
   coder's agreement is weak evidence (see above), and there is no human expert.
3. **Not a validator's fault model, and not validator-derived.** Nothing here was chosen because a
   tool caught it or missed it. The six records *excluded* for that reason are listed in
   `subset.json` under `excluded`.
4. **Not a benchmark.** It is a challenge set for one instrument on one corpus, with a stated
   criterion per item.
5. **Not stable against further evidence.** Two records from the original 14 have already left the
   population on evidence (a phantom excerpt; a legal construct). If an item is shown wrong, the
   honest outcome is a dated correction and a new frozen hash, not an edit here.

## Provenance

- Frozen population: `research/issue-007/coding/errors.csv` (sha256 `30265ff5…15f6`, untouched),
  corrected by `research/issue-007/coding/errors-corrections.csv` (C01–C12) into
  `errors-combined.csv`; corrections documented in report §16–§17 and `AMENDMENTS.md` A6–A7.
- Codebook: `research/issue-007/coding/CODEBOOK.md` v1.3 (`fc476b1c…c9cd`).
- Model files: `models/` and `raws/` copies, hashed in `models/manifest.csv`.
- Post-inspection verification basis: SysML 2.0 §8.2.2.1.2 (reserved keywords), §7.7.1 (attribute
  typing), and the normative `Actions.sysml` library for the C12 withdrawal.

## Freeze record

`FROZEN-SUBSET-HASH.txt` contains both hashes and the UTC freeze time. B should verify them before
running, and should not regenerate `subset.json` (that would change the hash).
"""
    (HERE / "FROZEN-SUBSET.md").write_text(doc, encoding="utf-8")
    h_doc = sha(HERE / "FROZEN-SUBSET.md")
    (HERE / "FROZEN-SUBSET-HASH.txt").write_text(
        f"frozen_utc {stamp}\n"
        f"{h_json}  subset.json\n"
        f"{h_man}  models/manifest.csv\n"
        f"{h_doc}  FROZEN-SUBSET.md\n"
        f"{len(items)} error items ({sum(i['contested'] for i in items)} contested); "
        f"{len(controls)} controls\n", encoding="utf-8")
    print(f"items: {len(items)} ({sum(i['contested'] for i in items)} contested); "
          f"controls: {len(controls)}; models copied: {len(all_models)}")
    print(f"subset.json {h_json}")
    print(f"manifest    {h_man}")


if __name__ == "__main__":
    main()
