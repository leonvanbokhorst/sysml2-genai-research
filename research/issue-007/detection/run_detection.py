#!/usr/bin/env python3
"""Detection measurement: what does the pinned validator (OpenSysML v0.12.1) report?

Order matters and is fixed: this runs AFTER coding is frozen (METHODOLOGY-FROZEN.md §7).
It never edits a label in errors.csv. It writes:
  detection/raw/<artifact>.txt        verbatim stdout+stderr per run
  detection/diagnostics.csv           parsed diagnostics
  detection/summary.csv               per-artifact counts, exit code, parses_as_is
  detection/table.md                  per-class detection table (coded errors vs diagnostics)
and fills models.csv's `parses_as_is` / `raw_only_invalid` columns.

Offline: operates only on files already in the repository.

Usage: python3 research/issue-007/detection/run_detection.py
"""
import csv
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPO = ROOT.parent.parent
TOOL = REPO / ".tools" / "sysml"
RAWOUT = HERE / "raw"
DIAG_RE = re.compile(r"^(?P<path>.+?):(?P<line>\d+):(?P<col>\d+): "
                     r"(?P<sev>[a-z]+)\[(?P<code>[a-zA-Z0-9_-]+)\]: (?P<msg>.*)$")

VERDICT_NOTE = ("✓", "no errors", "no error that stops a check")


def run(path: Path) -> tuple:
    proc = subprocess.run([str(TOOL), "-validate", str(path)],
                          capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def parse_diags(text: str, artifact: str, scope: str) -> list:
    out = []
    for line in text.split("\n"):
        m = DIAG_RE.match(line.strip())
        if m:
            d = m.groupdict()
            d.update(artifact=artifact, scope=scope, line=int(d["line"]))
            out.append(d)
    return out


def main() -> None:
    RAWOUT.mkdir(parents=True, exist_ok=True)
    arts = []
    for p in sorted((ROOT / "corpus" / "normalized").glob("*.sysml")):
        arts.append((f"{p.stem}.normalised", "normalised", p))
    for p in sorted((ROOT / "raw").glob("*.md")):
        arts.append((f"{p.stem}.raw", "raw", p))
    for p in sorted((HERE / "external").glob("*.sysml")):
        arts.append((f"{p.stem}", "external", p))
    for p in sorted((HERE / "probes").glob("*.sysml")):
        arts.append((f"{p.stem}", "probe", p))

    diagnostics, summary = [], []
    for artifact, scope, path in arts:
        code, out, err = run(path)
        text = f"$ .tools/sysml -validate {path}\n[exit {code}]\n--- stdout ---\n{out}\n--- stderr ---\n{err}"
        (RAWOUT / f"{artifact}.txt").write_text(text, encoding="utf-8")
        diags = parse_diags(out + "\n" + err, artifact, scope)
        diagnostics += diags
        nonblocking = "no error that stops a check" in out
        clean = code == 0 and not diags
        summary.append({
            "artifact": artifact, "scope": scope,
            "path": str(path.relative_to(REPO)),
            "exit_code": code, "n_diagnostics": len(diags),
            "n_error": sum(d["sev"] == "error" for d in diags),
            "codes": ";".join(sorted({d["code"] for d in diags})),
            "parses_as_is": "yes" if clean else "no",
            "nonblocking_notation_only": "yes" if (diags and nonblocking) else "no",
        })
        print(f"{artifact:34s} exit={code} diags={len(diags):2d} "
              f"{';'.join(sorted({d['code'] for d in diags}))}")

    with (HERE / "diagnostics.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["artifact", "scope", "path", "line", "col",
                                           "sev", "code", "msg"])
        w.writeheader()
        for d in diagnostics:
            w.writerow({k: d.get(k, "") for k in w.fieldnames})
    with (HERE / "summary.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(summary[0]))
        w.writeheader()
        w.writerows(summary)

    # --- models.csv: fill the two detection columns (single owner per phase, see README) ---
    models_path = ROOT / "coding" / "models.csv"
    rows = list(csv.DictReader(models_path.open(encoding="utf-8")))
    raw_by = {r["artifact"]: r for r in summary if r["scope"] == "raw"}
    norm_by = {r["artifact"]: r for r in summary if r["scope"] == "normalised"}
    for r in rows:
        r["parses_as_is"] = raw_by[f"{r['model_id']}.raw"]["parses_as_is"]
        n_ok = norm_by[f"{r['model_id']}.normalised"]["parses_as_is"] == "yes"
        r["raw_only_invalid"] = "yes" if (r["parses_as_is"] == "no" and n_ok) else "no"
    with models_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    # --- per-class detection table ---
    def lines_of(spec: str) -> set:
        out = set()
        for part in spec.split(","):
            part = part.strip()
            if "-" in part:
                a, b = part.split("-")
                out |= set(range(int(a), int(b) + 1))
            elif part:
                out.add(int(part))
        return out

    def build_rows(errors):
        rows = []
        for e in errors:
            lines = lines_of(e["line_range"])
            hits = [d for d in by_model_diag[e["model_id"]] if d["line"] in lines]
            rows.append({
                "model_id": e["model_id"], "error_id": e["error_id"], "class": e["class"],
                "layer": e["layer"], "line_range": e["line_range"],
                "detected": "yes" if hits else "no",
                "diagnostics": ";".join(f"{d['code']}@{d['line']}" for d in hits),
                "severity_reported": ";".join(sorted({d["sev"] for d in hits})),
            })
        return rows

    def table(rows, heading, intro):
        cls = defaultdict(lambda: [0, 0])
        for r in rows:
            cls[r["class"]][0] += 1
            if r["detected"] == "yes":
                cls[r["class"]][1] += 1
        md = [heading, "", intro, "",
              "| Class | Coded errors | Detected | Silent | Recall on this corpus |",
              "|---|---|---|---|---|"]
        for c in sorted(cls):
            n, det = cls[c]
            md.append(f"| {c} | {n} | {det} | {n-det} | {det}/{n} |")
        md += ["", "| Model | Error | Class | Lines | Detected | Diagnostic |",
               "|---|---|---|---|---|---|"]
        for r in rows:
            md.append(f"| {r['model_id']} | {r['error_id']} | {r['class']} | {r['line_range']} | "
                      f"{r['detected']} | {r['diagnostics'] or '—'} |")
        return md, {c: (v[1], v[0]) for c, v in cls.items()}

    errors = list(csv.DictReader((ROOT / "coding" / "errors.csv").open(encoding="utf-8")))
    by_model_diag = defaultdict(list)
    for d in diagnostics:
        if d["scope"] == "normalised":
            by_model_diag[d["artifact"].replace(".normalised", "")].append(d)
    rows_tbl = build_rows(errors)
    md, cls = table(rows_tbl,
                    "# Detection table — coded errors vs OpenSysML v0.12.1 diagnostics",
                    "Primary population: `coding/errors.csv`, frozen **before** this run (14 records). "
                    "A record counts as **detected** only if the tool emitted at least one diagnostic "
                    "whose line falls inside the record's `line_range`; a diagnostic elsewhere in the "
                    "file is not credited to it. Silence neither removes nor reclassifies a coded error.")
    md += ["", "---", ""]
    combined = ROOT / "coding" / "errors-combined.csv"
    if combined.exists():
        allrows = build_rows(list(csv.DictReader(combined.open(encoding="utf-8"))))
        md2, cls2 = table(allrows,
                          f"### Corrected combined population ({len(allrows)} records: frozen + live "
                          "post-inspection)",
                          "The post-inspection additions were found by inspection **after** the "
                          "detection run drew attention to them, and each was verified against "
                          "SysML 2.0 §8.2.2.1.2 (reserved keywords) or the attribute-typing prose "
                          "(§7.7.1) / `checkAttributeUsageSpecialization` (8.3.7.3). Corrections "
                          "applied here are listed in `coding/errors-corrections.csv` (Gate-2 "
                          "response); the frozen population in `coding/errors.csv` is untouched.")
        md += md2[2:]
    (HERE / "table.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print("\ncodes:", dict(Counter(d["code"] for d in diagnostics)))
    print("by scope:", dict(Counter(d["scope"] for d in diagnostics)))
    print("detection by class:", {c: f"{v[1]}/{v[0]}" for c, v in sorted(cls.items())})


if __name__ == "__main__":
    main()
