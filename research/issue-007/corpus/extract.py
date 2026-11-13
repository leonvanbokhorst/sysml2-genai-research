#!/usr/bin/env python3
"""Extract intended SysML v2 text from raw LLM outputs — wrapper removal ONLY.

Rules are frozen in research/issue-007/METHODOLOGY-FROZEN.md §3. No semantic repair:
nothing inside the chosen model body is added, renamed, reordered or deleted.

Deterministic, offline. Writes:
  corpus/normalized/<model>.sysml
  corpus/extraction-log.json
  corpus/manifest.csv

Usage:  python3 research/issue-007/corpus/extract.py
"""
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent                      # research/issue-007
RAW = ROOT / "raw"
NORM = HERE / "normalized"
GENERATOR = "DeepSeek-family model served through DSH (exact checkpoint not exposed)"

SYSML_KEYWORDS = ("package", "part ", "part\n", "requirement", "action", "state",
                  "connection", "attribute", "port", "import", "satisfy", "flow")

FENCE_RE = re.compile(r"^```([A-Za-z0-9_+-]*)[ \t]*$")


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fenced_blocks(text: str):
    """Return [(lang, body, start_line, end_line)] for each ``` fenced block."""
    lines = text.split("\n")
    blocks, open_at, lang = [], None, ""
    for i, line in enumerate(lines):
        m = FENCE_RE.match(line.rstrip())
        if m and open_at is None:
            open_at, lang = i, m.group(1)
        elif line.rstrip() == "```" and open_at is not None:
            body = "\n".join(lines[open_at + 1:i])
            blocks.append((lang, body, open_at + 1, i + 1))
            open_at = None
    return blocks


def looks_like_sysml(body: str) -> bool:
    return any(k in body for k in SYSML_KEYWORDS)


def extract(model_id: str, raw_text: str) -> dict:
    blocks = fenced_blocks(raw_text)
    log = {
        "model_id": model_id,
        "raw_sha256": sha(raw_text),
        "raw_char_count": len(raw_text),
        "n_fenced_blocks": len(blocks),
        "fence_languages": [b[0] for b in blocks],
    }

    if not blocks:
        # R3 — no fence: the whole raw text is the candidate model. Prose is NOT stripped,
        # because deciding where prose ends is a judgement that would destroy the wrapper signal.
        body = raw_text
        log.update(rule="R3_no_fence", wrapper_status="no_fence",
                   preamble="", trailing="", extra_blocks=[])
    else:
        sysml_blocks = [b for b in blocks if looks_like_sysml(b[1])]
        chosen = sysml_blocks[0] if sysml_blocks else blocks[0]
        lines = raw_text.split("\n")
        start_idx, end_idx = chosen[2] - 1, chosen[3]      # fence line indices
        body = chosen[1]
        preamble = "\n".join(lines[:start_idx])
        trailing = "\n".join(lines[end_idx:])
        extra = [{"lang": b[0], "sha256": sha(b[1]), "chars": len(b[1])}
                 for b in blocks if b is not chosen]
        rule = "R1_single_sysml_fence" if len(blocks) == 1 else "R2_multi_first_sysml_fence"
        log.update(rule=rule, wrapper_status="fenced" if len(blocks) == 1 else "multi_block",
                   fence_lang=chosen[0], preamble=preamble, trailing=trailing,
                   extra_blocks=extra,
                   chosen_block_lines=[chosen[2], chosen[3]])

    # Rules R1/R2 remove the fence lines only; body text is byte-identical to the source.
    out = body.strip("\n") + "\n"
    log.update(normalized_sha256=sha(out), normalized_char_count=len(out),
               normalized_lines=out.count("\n"),
               contains_scalar_import="private import ScalarValues::*" in out,
               stub_line="stub" if False else None)
    return log, out


def main() -> None:
    NORM.mkdir(parents=True, exist_ok=True)
    logs, rows = [], []
    for path in sorted(RAW.glob("*.md")):
        model_id = path.stem
        task, config = model_id.split("-")
        raw_text = path.read_text(encoding="utf-8")
        log, out = extract(model_id, raw_text)
        (NORM / f"{model_id}.sysml").write_text(out, encoding="utf-8")
        mtime = datetime.fromtimestamp(os.stat(path).st_mtime, tz=timezone.utc)
        log["generation_timestamp_utc"] = mtime.strftime("%Y-%m-%dT%H:%M:%SZ")
        logs.append(log)
        rows.append({
            "model_id": model_id,
            "task": task,
            "configuration": config,
            "generator": GENERATOR,
            "generation_timestamp_utc": log["generation_timestamp_utc"],
            "char_count_raw": len(raw_text),
            "sha256_raw": log["raw_sha256"],
            "raw_path": f"research/issue-007/raw/{model_id}.md",
            "wrapper_status": log["wrapper_status"],
            "extraction_rule": log["rule"],
            "normalized_sha256": log["normalized_sha256"],
            "normalized_path": f"research/issue-007/corpus/normalized/{model_id}.sysml",
        })

    (HERE / "extraction-log.json").write_text(
        json.dumps(logs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    import csv
    with (HERE / "manifest.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    print(f"{len(rows)} models; wrapper status:",
          {s: sum(r["wrapper_status"] == s for r in rows) for s in
           {r["wrapper_status"] for r in rows}})
    print(f"manifest: {HERE/'manifest.csv'}")


if __name__ == "__main__":
    main()
