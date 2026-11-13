#!/usr/bin/env python3
"""Shallow mechanisation audit of the normative OCL constraint bodies.

Purpose: audit "specified, but the published OCL cannot be implemented literally",
separately from the dependency class (which records what a checker needs).  This is NOT an OCL parser.  It
does three reproducible things:

1. Builds a vocabulary of every name declared in the normative XMI models
   (metaclasses, properties, operations, enumerations, literals, packages).
2. Tokenises each constraint's OCL body and flags identifiers that are neither in
   that vocabulary, nor a local variable, nor a standard OCL / Kerml helper name.
3. Flags unknown identifiers that are within Levenshtein distance 2 of a
   vocabulary name as *likely typos*, and flags malformed library literals
   (quoted strings containing '::' that do not resolve to a known package).

The output is a review list, not a verdict: each flagged item must be checked by
a human against the cited clause before it is reported as a defect.

Usage:
    python3 audit_ocl.py --source-dir /tmp/sysml --catalogue constraints.csv \
        --out suppositions.csv
"""

import argparse
import csv
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

XMI_NS = "{http://www.omg.org/spec/XMI/20161101}"

# Top-level packages of the normative Kernel Semantic Library and Systems Model
# Library (the model libraries are separate normative kpar artefacts, so they do
# not appear as packages in the metamodel XMI).  Used only to flag malformed or
# misspelled library literals.
KNOWN_LIBRARY_PACKAGES = set(
    """
    Base Links Objects Occurrences Performances Actions States Transfers
    Calculations Clocks Constraints Cases AnalysisCases VerificationCases
    UseCases Views Parts Ports Items Interfaces Connections Flows Allocations
    Requirements Metadata Metaobjects ScalarValues Collections Quantities ISQBase
    Time ControlPerformances TransitionPerformances FeatureReferencingPerformances
    KerML ControlFunctions
    """.split()
)

# OCL 2.0 and KerML helper names used in the constraint bodies.
OCL_STDLIB = set(
    """
    self null true false and or not xor implies let in if then else endif
    forAll exists select reject collect collectNested any one isUnique closure
    size isEmpty notEmpty includes excludes including excluding union intersection
    flatten asSet asSequence asOrderedSet asBag first last at indexOf subSequence
    subOrderedSet append prepend insertAt sortedBy iterate
    oclIsKindOf oclIsTypeOf oclAsType oclIsNew oclIsInState oclType oclContainer
    oclContents oclAsSet allInstances
    selectByKind selectAsKind selectByKindAsSet conformsTo specializes
    specializesFromLibrary redefines redefinesFromLibrary isCompatibleWith
    resolveGlobal resolveLocal resolveVisible resolve qualificationOf
    inputParameter inputParameters outputParameters ownedFeatureMembership
    multiplicityHasBounds hasBounds modelLevelEvaluable evaluate
    referencedFeatureTarget libraryNamespace instantiatedType directionOf
    directionOfExcluding subsetsChain asCartesianProduct isCartesianProduct
    ownedCrossFeature hasBounds valueOf isFeaturedWith isFeaturedWithin
    syntaxElement isSyntactic isSemantic isDistinguishableFrom
    Sequence OrderedSet Set Bag Collection Tuple OclAny Integer Real String
    Boolean UnlimitedNatural
    """.split()
)

TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
COMMENT_RE = re.compile(r"--[^\n]*")
LET_RE = re.compile(r"\blet\s+([A-Za-z_][A-Za-z0-9_]*)")
LAMBDA_RE = re.compile(r"(?:forAll|exists|select|reject|collect|any|one|closure|isUnique|sortedBy)\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)")
PIPE_RE = re.compile(r"\|\s*([A-Za-z_][A-Za-z0-9_]*(?:\s*,\s*[A-Za-z_][A-Za-z0-9_]*)*)\s*(?:,|\)|\||in\b)")
QUOTED_RE = re.compile(r"'[^']*'")


def local(tag: str) -> str:
    return tag.split("}")[-1]


def build_vocab(paths):
    vocab = set()
    packages = set()
    for p in paths:
        root = ET.parse(p).getroot()
        for el in root.iter():
            typ = el.get(XMI_NS + "type") or ""
            name = el.get("name")
            if not name:
                continue
            if typ in (
                "uml:Class", "uml:Property", "uml:Operation", "uml:Enumeration",
                "uml:EnumerationLiteral", "uml:Association", "uml:DataType",
                "uml:PrimitiveType",
            ):
                vocab.add(name)
            if typ == "uml:Package":
                packages.add(name)
                vocab.add(name)
            if typ == "uml:EnumerationLiteral":
                vocab.add(name)
    return vocab, packages


def levenshtein(a, b, cap=3):
    if abs(len(a) - len(b)) > cap:
        return cap + 1
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def audit_row(row, vocab, packages):
    body = COMMENT_RE.sub("", row["ocl_body"])
    stripped = QUOTED_RE.sub("''", body)
    locals_ = set(LET_RE.findall(body)) | set(PIPE_RE.findall(body))
    for m in LAMBDA_RE.findall(body):
        locals_.add(m)
    # split comma lists from lambda params
    locals_ = {x.strip() for item in locals_ for x in item.split(",") if x.strip()}

    unknown = []
    for tok in set(TOKEN_RE.findall(stripped)):
        if tok in vocab or tok in OCL_STDLIB or tok in locals_:
            continue
        unknown.append(tok)

    typos = []
    for u in unknown:
        best, dist = "", 99
        for v in vocab:
            d = levenshtein(u, v)
            if d < dist:
                best, dist = v, d
        if dist <= 2:
            typos.append((u, best, dist))

    bad_literals = []
    for lit in re.findall(r"'([^']*)'", body):
        if "::" in lit:
            head = lit.split("::")[0]
            if "\\" in lit or "::" in lit.replace("::", "", 1) and "" in lit.split("::"):
                bad_literals.append(lit)
            elif head and head not in KNOWN_LIBRARY_PACKAGES:
                bad_literals.append(lit)

    return sorted(unknown), typos, bad_literals


def main():
    ap = argparse.ArgumentParser()
    here = Path(__file__).resolve().parent
    ap.add_argument("--source-dir", type=Path, default=Path("/tmp/sysml"))
    ap.add_argument("--catalogue", type=Path, default=here / "constraints.csv")
    ap.add_argument("--out", type=Path, default=here / "ocl-audit.csv")
    args = ap.parse_args()

    vocab, packages = build_vocab([args.source_dir / "SysML.xmi", args.source_dir / "KerML.xmi"])
    rows = list(csv.DictReader(open(args.catalogue)))
    out = []
    for r in rows:
        unknown, typos, bad_literals = audit_row(r, vocab, packages)
        if not unknown and not bad_literals:
            continue
        out.append(
            {
                "spec": r["spec"],
                "name": r["name"],
                "kind": r["kind"],
                "context_metaclass": r["context_metaclass"],
                "clause": r["pdf_clause"],
                "unknown_identifiers": ";".join(unknown),
                "likely_typos": ";".join(f"{u}->{b} (d={d})" for u, b, d in typos),
                "bad_library_literals": ";".join(sorted(set(bad_literals))),
                "ocl_body": "\n".join(line.rstrip() for line in r["ocl_body"].splitlines()).strip(),
            }
        )

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "spec", "name", "kind", "context_metaclass", "clause",
                "unknown_identifiers", "likely_typos", "bad_library_literals", "ocl_body",
            ],
            lineterminator="\n",
        )
        w.writeheader()
        w.writerows(out)
    print(f"{len(out)} constraints with at least one unexplained identifier or literal")
    print(f"likely typos: {sum(1 for r in out if r['likely_typos'])}; bad literals: {sum(1 for r in out if r['bad_library_literals'])}")


if __name__ == "__main__":
    main()
