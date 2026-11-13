#!/usr/bin/env python3
"""Mechanical indicators to support (not replace) inspection.

Emits coding/_audit-view.txt (all models, line-numbered) and coding/indicators.json with
cheap, reproducible signals: prelude presence, bare scalar-type uses, satisfy forms, connect/
flow/transition lines, declared vs referenced names. Every indicator is a pointer for a human
check; none of them is an error verdict.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
NORM = HERE.parent / "corpus" / "normalized"
SCALARS = ("Real", "Integer", "Boolean", "String", "Natural", "Positive")
DECL = re.compile(r"^\s*(?:abstract\s+|private\s+|public\s+)?"
                  r"(part def|attribute def|item def|port def|action def|state def|requirement def|"
                  r"part|attribute|port|action|state|connection|flow|requirement|satisfy|package|import|"
                  r"enum def|enum|transition|first|then|entry|in|out|ref)\s+([A-Za-z_][A-Za-z0-9_]*)")
IDENT = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def main() -> None:
    view, indicators = [], {}
    for path in sorted(NORM.glob("*.sysml")):
        mid = path.stem
        text = path.read_text(encoding="utf-8")
        lines = text.split("\n")
        view.append(f"\n===== {mid} ({len(lines)-1} lines) =====")
        for i, line in enumerate(lines, 1):
            view.append(f"{i:3d}| {line}")

        declared, refs, cand = set(), [], []
        for i, line in enumerate(lines, 1):
            for m in DECL.finditer(line):
                declared.add(m.group(2))
            if re.match(r"^\s*(connection|flow|satisfy)\b", line):
                cand.append({"line": i, "text": line.strip()})
                body = re.sub(r"^\s*(connection|flow|satisfy)\s+", "", line)
                refs += [(i, t) for t in IDENT.findall(body)]
        bare_scalars = sorted({s for s in SCALARS
                               if re.search(rf":\s*{s}\b", text)}) if "ScalarValues" not in text else []
        # identifiers used in connect/flow/satisfy bodies that are never declared in the file
        undeclared = sorted({t for _, t in refs
                             if t not in declared and t not in SCALARS
                             and t not in {"connect", "from", "to", "by", "of", "self"}})
        indicators[mid] = {
            "lines": len(lines) - 1,
            "has_scalarvalues_import": "ScalarValues" in text,
            "bare_scalar_types_without_import": bare_scalars,
            "satisfy_lines": [c for c in cand if c["text"].startswith("satisfy")],
            "connection_flow_lines": [c for c in cand if not c["text"].startswith("satisfy")],
            "declared_names": len(declared),
            "undeclared_names_in_connect_flow_satisfy": undeclared,
            "uses_from_to_on": [i for i, l in enumerate(lines, 1)
                                if re.search(r"\b(from|on|when)\b", l)],
            "port_usages_untyped": len(re.findall(r"^\s*port\s+[A-Za-z_][A-Za-z0-9_]*\s*;", text, re.M)),
        }
    (HERE / "_audit-view.txt").write_text("\n".join(view) + "\n", encoding="utf-8")
    (HERE / "indicators.json").write_text(json.dumps(indicators, indent=2) + "\n", encoding="utf-8")
    print("models:", len(indicators))
    for mid, d in indicators.items():
        print(f"{mid}: prelude={d['has_scalarvalues_import']} bare={d['bare_scalar_types_without_import']} "
              f"undeclared={d['undeclared_names_in_connect_flow_satisfy']} satisfy={len(d['satisfy_lines'])} "
              f"cf={len(d['connection_flow_lines'])} from_to_on={d['uses_from_to_on']}")


if __name__ == "__main__":
    main()
