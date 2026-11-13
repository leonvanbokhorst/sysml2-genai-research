#!/usr/bin/env python3
"""Extract the SysML v2 / KerML well-formedness constraint catalogue from the
pinned normative artefacts.

Why XMI rather than the PDF: the specification's Clause 2 states that "if there
are any conflicts between this document and the machine-readable files, the
machine-readable files take precedence."  The normative machine-readable
artefact for the abstract syntax is the MOF XMI (SysML ptc/25-02-15,
KerML ptc/25-04-04).  The XMI carries every constraint with its constrained
metaclass, its prose comment and its OCL body.  The PDF is the human-readable
rendering and is used here as a cross-check, not as the primary source.

Usage:
    python3 extract_constraints.py --fetch --out-dir .
    python3 extract_constraints.py --source-dir /tmp/sysml --out-dir .

Outputs (written to --out-dir):
    constraints.csv              one row per named constraint (SysML and KerML)
    pdf-only-names.csv           names used in a specification PDF but not defined
                                 in either normative XMI (candidate "informative only")
    extraction-report.json       counts, checksums, cross-check results

Every row is traceable to a pinned artefact via PINNED below.
"""

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Pinned artefacts.  sha256 recorded at retrieval on 2026-11-13 (UTC).
# The PDFs are not committed; --fetch downloads them from OMG and verifies.
# ---------------------------------------------------------------------------
PINNED = {
    "sysml": {
        "spec": "SysML 2.0",
        "omg_doc": "formal/2026-03-02",
        "date": "March 2026",
        "xmi_url": "https://www.omg.org/spec/SysML/20250201/SysML.xmi",
        "xmi_sha256": "caa65d54f56798bf7582d173f7567e1eea37a49c45984f8bd7df145011cf8c6f",
        "pdf_url": "https://www.omg.org/spec/SysML/2.0/Language/PDF",
        "pdf_sha256": "46e6c0476a6f1f34f367d57e039d56659bff75e41d2e4b3d37ca4cadea84a83a",
        "pdf_name": "sysml-2.0-language.pdf",
        "txt_name": "sysml.txt",
        "heading_re": r"^8\.3\.\d+(?:\.\d+)*\s+\w[\w ]*$",
    },
    "kerml": {
        "spec": "KerML 1.0",
        "omg_doc": "formal/2026-03-01",
        "date": "March 2026",
        "xmi_url": "https://www.omg.org/spec/KerML/20250201/KerML.xmi",
        "xmi_sha256": "45b18775afe2b2fcdc70e24f37c6d2f344defcc3f38a02075a193354e2d7b466",
        "pdf_url": "https://www.omg.org/spec/KerML/1.0/PDF",
        "pdf_sha256": "3bcc96f989bfa9d05cd28e026df3351b795fe8d494187b87bff3db7d96373697",
        "pdf_name": "kerml-1.0.pdf",
        "txt_name": "kerml.txt",
        "heading_re": r"^8\.3\.\d+(?:\.\d+)*\s+\w[\w ]*$",
    },
}

XMI_NS = "{http://www.omg.org/spec/XMI/20161101}"
NAMED_RE = re.compile(r"^(validate|check|derive)[A-Z][A-Za-z0-9]*$")

# Signals used (mechanically, reproducibly) in the classification step.
LIBRARY_HELPERS = [
    "specializesFromLibrary",
    "specializesFromLibrary(",
    "redefinesFromLibrary",
    "libraryNamespace",
    "resolveGlobal",
    "isLibraryElement",
    "libraryTypeName",
    "libraryFeatureName",
]
IMPLIED_HELPERS = ["isImplied", "implied", "Implied"]
RESOLUTION_HELPERS = ["resolveGlobal", "resolveLocal", "resolveVisible", "resolve(", "qualifiedName"]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch(url: str, dest: Path) -> None:
    if dest.exists():
        return
    print(f"fetching {url} -> {dest}", file=sys.stderr)
    urllib.request.urlretrieve(url, dest)


def localname(tag: str) -> str:
    return tag.split("}")[-1]


def library_literal(body: str) -> bool:
    """True if the OCL body names a model-library element ('Package::Element').

    Metamodel enumerations (VisibilityKind, FeatureDirectionKind, ...) are part of
    the abstract syntax and are therefore *not* library dependencies.  The set of
    enumeration names is passed via a module-level variable set by parse_xmi.
    """
    enums = globals().get("_ENUM_NAMES", set())
    for lit in re.findall(r"'([^']*)'", body):
        if "::" in lit and "\\" not in lit:
            head = lit.split("::")[0]
            if head and head not in enums:
                return True
    return False


def parse_xmi(path: Path, spec: str) -> list[dict]:
    """Return one record per named well-formedness constraint.

    Constraints are `uml:Constraint` elements owned (directly) by a metaclass
    (uml:Class) or by an operation/property.  Named constraints follow the
    spec's own convention: validateXxx / checkXxx / deriveXxx.  Anonymous
    constraints are operation body conditions, not catalogue entries; they are
    counted separately in the report.
    """
    root = ET.parse(path).getroot()
    parent: dict[ET.Element, ET.Element] = {}
    for p in root.iter():
        for c in p:
            parent[c] = p

    # Package path: the XMI id is e.g. Systems-DefinitionAndUsage-Definition-validateX
    constraints = [el for el in root.iter() if el.get(XMI_NS + "type") == "uml:Constraint"]

    enum_names = {
        e.get("name")
        for e in root.iter()
        if e.get(XMI_NS + "type") == "uml:Enumeration" and e.get("name")
    }
    globals()["_ENUM_NAMES"] = enum_names
    # metaclass inheritance from the XMI model (uml:Class generalization refs)
    classes = {}
    for el in root.iter():
        if el.get(XMI_NS + "type") == "uml:Class" and el.get("name"):
            classes[el.get(XMI_NS + "id")] = el

    rows = []
    anonymous = 0
    for c in constraints:
        name = (c.get("name") or "").strip()
        if not NAMED_RE.match(name):
            anonymous += 1
            continue

        owner = parent.get(c)
        while owner is not None and owner.get(XMI_NS + "type") not in ("uml:Class", "uml:Property", "uml:Operation"):
            owner = parent.get(owner)

        specs = [x for x in c if localname(x.tag) == "specification"]
        comments = [x for x in c if localname(x.tag) == "ownedComment"]
        body = specs[0].get("body") if specs else ""
        # Normalise trailing whitespace so CSV fields are stable and diff-clean;
        # this changes no token, only line-end spaces from the XMI.
        body = "\n".join(line.rstrip() for line in (body or "").splitlines()).strip()
        language = specs[0].get("language") if specs else ""
        prose = " ".join(
            re.sub(r"<[^>]+>", "", cm.get("body") or "") for cm in comments
        ).strip()
        prose = re.sub(r"\s+", " ", prose)

        cid = c.get(XMI_NS + "id") or ""
        # package path: strip the trailing constraint name segment
        parts = cid.split("-")
        package = parts[1] if len(parts) > 1 else ""

        rows.append(
            {
                "spec": spec,
                "name": name,
                "kind": NAMED_RE.match(name).group(1),
                "context_metaclass": (owner.get("name") if owner is not None else ""),
                "context_element_type": (owner.get(XMI_NS + "type") if owner is not None else ""),
                "package": package,
                "xmi_id": cid,
                "ocl_language": language,
                "ocl_body": (body or "").strip(),
                "prose": prose,
                "ocl_chars": len((body or "").strip()),
                "uses_library_helper": int(any(h in (body or "") for h in LIBRARY_HELPERS)),
                "uses_library_literal": int(library_literal(body or "")),
                "uses_implied": int("implied" in (body or "").lower()),
                "uses_resolution": int(any(h in (body or "") for h in RESOLUTION_HELPERS)),
                "has_ocl": int(bool((body or "").strip()) and "No OCL" not in (body or "")),
                "language_mismatch": int(language != "OCL2.0" and bool((body or "").strip())),
            }
        )

    rows.sort(key=lambda r: (r["kind"], r["context_metaclass"], r["name"]))
    return rows, anonymous


def parse_pdf_text(path: Path, heading_re: str) -> dict:
    """Return clause + occurrence information for every constraint name.

    The PDF renders each constraint as a heading followed by prose and then by
    its OCL body.  We record, for each name, every line it occurs on, the
    nearest preceding 8.3.x.y metaclass heading (clause), and whether the
    occurrence looks like a definition (name alone on a line) rather than a
    prose mention.
    """
    lines = path.read_text(errors="replace").splitlines()
    heading = re.compile(heading_re)
    name_re = re.compile(r"\b(validate|check|derive)[A-Z][A-Za-z0-9]*\b")

    current_clause = ""
    current_heading = ""
    occurrences = defaultdict(list)  # name -> list of dicts
    for i, line in enumerate(lines):
        s = line.strip()
        # Skip table-of-contents lines and page headers: they contain dot leaders.
        if "...." in s:
            continue
        if heading.match(s):
            # "8.3.6.3 ReferenceUsage"
            m = re.match(r"^(8\.3\.\d+(?:\.\d+)*)\s+(.+)$", s)
            if m:
                current_clause = m.group(1)
                current_heading = m.group(2).strip()
        for m in name_re.finditer(line):
            name = m.group(0)
            # definition style: the name is the only token on the line
            definition_style = s == name
            occurrences[name].append(
                {
                    "line": i + 1,
                    "clause": current_clause,
                    "heading": current_heading,
                    "definition_style": definition_style,
                }
            )
    return occurrences


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-dir", type=Path, default=Path("."))
    ap.add_argument("--out-dir", type=Path, default=Path("."))
    ap.add_argument("--fetch", action="store_true", help="download pinned artefacts")
    ap.add_argument("--no-pdf", action="store_true", help="skip PDF cross-check")
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    report = {"pinned": {}, "counts": {}, "cross_checks": {}, "anonymous_constraints": {}}
    all_rows = []
    pdf_occ = {}

    for key, pin in PINNED.items():
        src = args.source_dir
        xmi_path = src / f"{pin['spec'].split()[0]}.xmi"
        if args.fetch:
            fetch(pin["xmi_url"], xmi_path)
            want = pin["pdf_url"]
            pdf_path = src / pin["pdf_name"]
            if not args.no_pdf:
                fetch(want, pdf_path)
        else:
            pdf_path = src / pin["pdf_name"]

        got = sha256(xmi_path)
        if got != pin["xmi_sha256"]:
            print(f"WARNING: {xmi_path} sha256 {got} != pinned {pin['xmi_sha256']}", file=sys.stderr)
        report["pinned"][key] = {
            "spec": pin["spec"],
            "omg_doc": pin["omg_doc"],
            "date": pin["date"],
            "xmi_url": pin["xmi_url"],
            "xmi_sha256": got,
            "xmi_sha256_pinned": pin["xmi_sha256"],
            "pdf_url": pin["pdf_url"],
            "pdf_sha256": pin["pdf_sha256"],
        }

        rows, anonymous = parse_xmi(xmi_path, pin["spec"])
        report["anonymous_constraints"][key] = anonymous

        if not args.no_pdf:
            if not pdf_path.exists():
                subprocess.run(["curl", "-sSL", "--max-time", "180", "-o", str(pdf_path), pin["pdf_url"]], check=True)
            got_pdf = sha256(pdf_path)
            report["pinned"][key]["pdf_sha256_actual"] = got_pdf
            if got_pdf != pin["pdf_sha256"]:
                print(f"WARNING: {pdf_path} sha256 mismatch", file=sys.stderr)
            txt = pdf_path.with_suffix(".txt")
            if not txt.exists():
                subprocess.run(["pdftotext", "-layout", str(pdf_path), str(txt)], check=True)
            occ = parse_pdf_text(txt, pin["heading_re"])
            pdf_occ[key] = occ
            for r in rows:
                o = occ.get(r["name"], [])
                defs = [x for x in o if x["definition_style"]]
                r["in_pdf"] = int(bool(o))
                r["pdf_clause"] = (defs[0]["clause"] if defs else (o[0]["clause"] if o else ""))
                r["pdf_definition_style"] = int(bool(defs))
                r["pdf_occurrences"] = len(o)
        else:
            r_default = {"in_pdf": "", "pdf_clause": "", "pdf_definition_style": "", "pdf_occurrences": ""}
            for r in rows:
                r.update(r_default)

        all_rows.extend(rows)
        counts = Counter(r["kind"] for r in rows)
        report["counts"][key] = {
            "total_named": len(rows),
            "by_kind": dict(counts),
            "with_ocl": sum(r["has_ocl"] for r in rows),
            "without_ocl": sum(1 - r["has_ocl"] for r in rows),
            "with_library_helper": sum(r["uses_library_helper"] for r in rows),
            "with_library_literal": sum(r["uses_library_literal"] for r in rows),
            "language_mismatch": sum(r["language_mismatch"] for r in rows),
            "with_implied": sum(r["uses_implied"] for r in rows),
            "with_resolution": sum(r["uses_resolution"] for r in rows),
        }

    # ---- cross-check: names in the PDF that are defined in neither XMI ----
    xmi_names = {r["name"]: r["spec"] for r in all_rows}
    # A token like `checkAssociation` in a PDF table is usually the first part of
    # a line-wrapped `checkAssociationSpecialization`.  Exclude any candidate that
    # is a proper prefix of a name defined in the normative XMI, recording the
    # longer name, so that this artefact of PDF layout is not mistaken for a
    # specification divergence.
    def prefix_of(name):
        for xname in xmi_names:
            if xname != name and xname.startswith(name) and len(xname) > len(name):
                return xname
        return ""

    pdf_only = []
    wrapped = []
    for key, occ in pdf_occ.items():
        for name, os_ in occ.items():
            if name in xmi_names:
                continue
            longer = prefix_of(name)
            defs = [x for x in os_ if x["definition_style"]]
            row = {
                "name": name,
                "kind": NAMED_RE.match(name).group(1) if NAMED_RE.match(name) else "",
                "mentioned_in": PINNED[key]["spec"],
                "pdf_clause": (defs[0]["clause"] if defs else os_[0]["clause"]),
                "pdf_heading": (defs[0]["heading"] if defs else os_[0]["heading"]),
                "definition_style": int(bool(defs)),
                "occurrences": len(os_),
                "prefix_of_xmi_name": longer,
            }
            if longer:
                wrapped.append(row)
            else:
                pdf_only.append(row)
    pdf_only.sort(key=lambda r: (r["kind"], r["name"]))
    report["counts"]["pdf_only_names"] = len(pdf_only)
    report["counts"]["pdf_wrapped_name_fragments"] = len(wrapped)
    report["counts"]["pdf_only_by_kind"] = dict(Counter(r["kind"] for r in pdf_only))

    # ---- write outputs ----
    cols = [
        "spec", "name", "kind", "context_metaclass", "context_element_type", "package",
        "ocl_language", "language_mismatch", "ocl_chars", "has_ocl", "uses_library_helper",
        "uses_library_literal", "uses_implied",
        "uses_resolution", "in_pdf", "pdf_definition_style", "pdf_occurrences", "pdf_clause",
        "prose", "ocl_body", "xmi_id",
    ]
    with open(args.out_dir / "constraints.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for r in all_rows:
            w.writerow(r)

    with open(args.out_dir / "pdf-only-names.raw.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["name", "kind", "mentioned_in", "pdf_clause", "pdf_heading", "definition_style", "occurrences", "prefix_of_xmi_name"],
            lineterminator="\n",
        )
        w.writeheader()
        for r in pdf_only:
            w.writerow(r)

    with open(args.out_dir / "extraction-report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(json.dumps(report["counts"], indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
