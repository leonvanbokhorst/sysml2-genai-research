# A version-pinned catalogue of SysML v2 / KerML well-formedness constraints

This directory is the audit artefact for research issue
[#1](https://github.com/leonvanbokhorst/sysml2-genai-research/issues/1): *which
well-formedness constraints does SysML v2 / KerML actually impose, how are they
specified, and which are left to tool discretion?*

It is generated, not hand-written. Every row is traceable to a pinned OMG
artefact by name, clause and file hash. The headline analysis is in
[`../reports/issue-001-constraint-catalogue.md`](../reports/issue-001-constraint-catalogue.md).

---

## 1. Pinned artefacts

Retrieved 2026-11-13 (UTC) from OMG. The PDFs are not committed (size); the
script fetches them and verifies the hash. The two XMI files are the normative
machine-readable abstract syntax and are the primary extraction source: SysML
Clause 2 states that "if there are any conflicts between this document and the
machine-readable files, the machine-readable files take precedence."

| Artefact | OMG document | URL | sha256 |
|---|---|---|---|
| SysML 2.0, Part 1: Language Specification (PDF, 691 pp.) | `formal/2026-03-02`, March 2026 | <https://www.omg.org/spec/SysML/2.0/Language/PDF> | `46e6c0476a6f1f34f367d57e039d56659bff75e41d2e4b3d37ca4cadea84a83a` |
| KerML 1.0 Specification (PDF) | `formal/2026-03-01`, March 2026 | <https://www.omg.org/spec/KerML/1.0/PDF> | `3bcc96f989bfa9d05cd28e026df3351b795fe8d494187b87bff3db7d96373697` |
| SysML abstract syntax (MOF XMI) | `ptc/25-02-15` | <https://www.omg.org/spec/SysML/20250201/SysML.xmi> | `caa65d54f56798bf7582d173f7567e1eea37a49c45984f8bd7df145011cf8c6f` |
| KerML abstract syntax (MOF XMI) | `ptc/25-04-04` | <https://www.omg.org/spec/KerML/20250201/KerML.xmi> | `45b18775afe2b2fcdc70e24f37c6d2f344defcc3f38a02075a193354e2d7b466` |

**Date conflict, recorded not resolved.** The OMG catalogue pages say
*September 2025*; the PDFs say *March 2026* and the file IDs are `formal/26-03-*`.
The Systems Modeling release README explains the later date as an editorial
update for ISO submission. This catalogue cites the PDF cover date and document
number, which is what a reader can verify.

**Version skew caveat.** The pilot implementation has targeted **KerML 1.1 Beta 2
/ SysML 2.1 Beta 2** since its 2026-07 release. There is no published 2.1
specification page (`omg.org/spec/SysML/2.1` → 404 on 2026-11-13). This
catalogue is pinned to **1.0/2.0**. Any comparison with the pilot is therefore a
comparison across revisions; it is labelled as such wherever it appears.

---

## 2. What was extracted, and why from the XMI

The normative metamodel represents a well-formedness constraint as a
`uml:Constraint` owned by a metaclass, with:

- a **name** following the specification's own convention:
  `derive…` (derivation), `check…` (semantic constraint), `validate…`
  (validation constraint);
- an **ownedComment** holding the prose condition;
- a **specification** `uml:OpaqueExpression` holding the OCL body.

The extraction yields **623 named constraints**: SysML 365, KerML 258. It
excludes 17 SysML + 78 KerML anonymous constraints that are operation
body/pre/post conditions (`unnamed1`, `inputParametersBody`, …), which are not
well-formedness rules and do not follow the naming convention.

**Cross-check against the PDF.** All 623 names occur in the corresponding PDF as
a definition-style heading, and the nearest preceding `8.3.x.y` metaclass
heading supplies the clause number recorded in each row. Conversely, **39
constraint-name occurrences in the PDFs (38 distinct names) have no definition
in either XMI**. These are registered separately in
[`prose-only-names.csv`](prose-only-names.csv) and are *not* included in the 623.
They are a finding, not a rounding error: 31 of them state conditions in
normative Clause 8.4 prose.

### The specification's own three-way taxonomy

SysML §8.3.1 and KerML §8.3.1 define three kinds of constraint and give each a
different modal force. This is the catalogue's `obligation` column:

| Kind | Specification's words | Obligation |
|---|---|---|
| `derive…` | "A tool conformant to the SysML abstract syntax **shall always enforce** derivation constraints." | SHALL |
| `check…` | "[A tool] **may** satisfy the constraints by introducing implied relationships into the model, it **may** simply report their violation, or it **may ignore** the violations." | MAY |
| `validate…` | "A tool conformant to the SysML abstract syntax **should report** violations of validation constraints." | SHOULD |

This taxonomy is the specification's own, not the study's. It already answers
part of the research question: the normative text grades obligation, and the
largest single block (208 `check…` constraints) is explicitly discretionary in
its reporting.

---

## 3. Classification (the issue's four-way split)

Two independent dimensions are recorded in `classified.csv`:

*Terminology note (2026-11-13, after review): A/B/U are **dependency classes**;
the frozen rule and all counts are unchanged. "Mechanically checkable" in the issue
is operationalised as "no external library/semantic dependency"; executability is
a separate column.*

1. **Dependency class — A / B / U** (from the frozen code frame in
   [`coding/codebook.md`](coding/codebook.md)). The class records what a
   checker needs under the rule; it is **not** a claim that the published OCL
   executes as written. Executability is recorded separately in
   `executable_ocl_status` and audited in [`ocl-defects.csv`](ocl-defects.csv):
   - **A**: the OCL body is decidable from the model's abstract syntax alone;
     no Kernel Semantic Library / Systems Model Library element and no
     library-path resolution.
   - **B**: the body names a model-library element (`'Package::Element'`) or a
     helper defined in terms of the semantic layer (`specializesFromLibrary`,
     `redefinesFromLibrary`, `resolveGlobal` on a library path), so the check
     needs semantics beyond the abstract syntax.
   - **U**: not decidable as published (the body is a placeholder — two KerML
     `check…` constraints have the literal body `TBD`).
2. **Obligation — SHALL / SHOULD / MAY**, as above.

The mapping to the issue's four classes:

| Issue class | Operationalisation | Count |
|---|---|---|
| Normative and mechanically checkable | **dependency class A** — no external library/semantic dependency under the frozen rule (intended decidability; executability audited separately) | 437 (233 derive, 35 check, 169 validate) |
| Normative but requiring semantics beyond the abstract syntax | class B | 184 (2 derive, 171 check, 11 validate) |
| Present only in informative text or examples | **not** the `prose-only` block as a whole: see `prose-only-names.csv` | 3 example-only names, 3 non-constraint names, and 31 Clause-8.4 conditions with no metamodel definition (the 31 include 2 of the examples and 1 of the non-constraint names) |
| Absent / discretion / delegation (distinguished) | [`silence-register.md`](silence-register.md) | 10 registered areas: 4 absent, 2 explicit discretion/delegation, 1 ambiguity, 1 outside the well-formedness surface, 2 oracle/provenance gaps |

**Important nuance.** Dependency class A ≠ "required". 35 `check…` constraints
are model-local under the frozen rule, but their reporting obligation is MAY. Conversely, 11 `validate…`
constraints are class B: they are SHOULD-report, but need the model library.
The two dimensions must be read together; that is the central table of the
report.

### Headline counts

| | SysML 2.0 | KerML 1.0 | Total |
|---|---:|---:|---:|
| named constraints | 365 | 258 | **623** |
| `derive…` (SHALL) | 145 | 90 | 235 |
| `check…` (MAY) | 128 | 80 | 208 |
| `validate…` (SHOULD) | 92 | 88 | 180 |
| class A (model-local dependency) | 242 | 195 | **437** |
| class B (library/semantics) | 123 | 61 | **184** |
| class U (published `TBD`) | 0 | 2 | 2 |

Dependency class A/B by kind: derive 233/2; check 35/171 (plus 2 U); validate 169/11.

**Dependency class is not executability.** 27 of the 437 class-A rows and 14 of
the 184 class-B rows carry a high-confidence defect in their published OCL (two
bodies are `TBD`; others have misspelled identifiers or malformed library paths).
`classified.csv` records `executable_ocl_status` as a separate column, and
[`ocl-defects.csv`](ocl-defects.csv) gives the evidence. A class-A label means
"no external library semantics are needed under the frozen rule", not "this OCL
can be run as written".

---

## 4. Files

| File | What it is |
|---|---|
| [`constraints.csv`](constraints.csv) | 623 rows, one per named constraint: spec, name, kind, context metaclass, clause, OCL language/body, prose, library/resolution signals, PDF presence |
| [`classified.csv`](classified.csv) | the same rows plus `class`/`class_label` (dependency class), `class_basis`, `obligation`, defect counts, and `executable_ocl_status` (kept separate from the dependency class) |
| [`classification-summary.json`](classification-summary.json) | counts by spec × kind × class |
| [`extraction-report.json`](extraction-report.json) | artefact hashes, counts, PDF cross-check, anonymous constraints |
| [`ocl-defects.csv`](ocl-defects.csv) | 48 named constraints whose published OCL is a placeholder, typo or malformed library path; confidence and verification per row |
| [`ocl-audit.raw.csv`](ocl-audit.raw.csv) | the raw identifier-audit output from which `ocl-defects.csv` was curated (includes false positives) |
| [`prose-only-names.csv`](prose-only-names.csv) | 38 names used in a specification PDF but defined in neither XMI, categorised (renamed / missing / typo / example / not-a-constraint / subsumed) |
| [`pdf-only-names.raw.csv`](pdf-only-names.raw.csv) | the raw pre-curation output (includes line-wrapped fragments and false positives) |
| [`silence-register.md`](silence-register.md) | 10 registered areas with a `Kind` label (absent, discretion, delegation, ambiguity, outside-surface, oracle, provenance), evidence, and observed implementation choices |
| [`deep-trace.md`](deep-trace.md) | 18 constraints traced from clause to two implementations (where available) |
| [`impl-evidence.md`](impl-evidence.md) | implementation-behaviour evidence: pilot source inventory, release notes 2026-01→2026-09.1, OpenSysML, Syside, SYSML21-185 |
| [`validator-inventory.csv`](validator-inventory.csv) | 116 pilot `@Check` methods, with lines and the constraint names the source attributes to them |
| [`validator-coverage.json`](validator-coverage.json) | **identifier-coverage** cross-check of the catalogue against the pilot inventory (156/623 exact identifiers; 149 in non-TODO methods, 7 TODO-only). Not implementation or enforcement coverage |
| [`coding/`](coding/) | frozen codebook, 60-row stratified sample, coder A and coder B labels, agreement script |
| [`extract_constraints.py`](extract_constraints.py) | XMI extraction + PDF cross-check; pinned URLs and hashes |
| [`audit_ocl.py`](audit_ocl.py) | shallow OCL identifier audit that produced `ocl-defects.csv` candidates |
| [`classify.py`](classify.py) | applies the frozen dependency-class rule and records published-OCL executability as a separate column |
| [`coverage.py`](coverage.py) | catalogue ↔ validator name cross-check |

---

## 5. Reproduce

```bash
# 1. fetch and verify pinned artefacts, extract, cross-check against the PDFs
python3 catalogue/extract_constraints.py --fetch --source-dir /tmp/sysml --out-dir catalogue

# 2. shallow OCL identifier audit (needs pdftotext-free XMI only)
python3 catalogue/audit_ocl.py --source-dir /tmp/sysml \
    --out catalogue/ocl-audit.raw.csv   # candidates; curated register is ocl-defects.csv

# 3. classify
python3 catalogue/classify.py --catalogue catalogue/constraints.csv \
    --defects catalogue/ocl-defects.csv --out catalogue/classified.csv \
    --summary catalogue/classification-summary.json

# 4. coding sample and agreement (coder-b.csv is the independent coder's output)
python3 catalogue/coding/make_sample.py
python3 catalogue/coding/agreement.py

# 5. catalogue vs pilot validator
python3 catalogue/coverage.py        # needs validator-inventory.csv
```

`extract_constraints.py` needs `pdftotext` (poppler) for the PDF text
extraction. The XMI extraction alone needs no external tool.

---

## 6. Limitations, stated as limits

1. **Extraction is syntactic.** A constraint is "named" if it is a `uml:Constraint`
   with a convention-conforming name in the normative XMI. An unnamed operation
   body condition is excluded by decision, not oversight.
2. **Dependency class A/B is a decision procedure, not a proof of executability.**
   It operationalises "needs semantics beyond the abstract syntax" as "names a
   model-library element or library helper". It does not decide whether an
   individual OCL expression is evaluable in reasonable time, nor whether a
   helper's own body is library-dependent. A class-A label therefore means
   "model-local under the frozen rule", not "the published OCL runs as written";
   27 class-A rows have a high-confidence defect in their published body.
3. **The OCL audit is shallow.** It flags identifiers that do not occur as
   declared names in either XMI and malformed library literals. It does not
   parse OCL; a flagged identifier can be a legitimate name from a model library
   used unqualified. The 48-row register is curated and carries a confidence
   column; the raw candidate list is reproducible.
4. **The coding study has a ceiling.** Two coders (the principal researcher's
   stated rule and an independent LLM coder) agreed 60/60, κ = 1.000, on a
   60-row stratified sample. That establishes that the rule is applicable
   without drift on ordinary rows; it is not evidence of expert-human agreement,
   and the sample did not deliberately concentrate the hardest cases.
5. **The implementation comparison is cross-revision.** The pilot targets
   unpublished 2.1 Beta 2; the catalogue is 1.0/2.0. Exact-name matching is a
   lower bound and unmatched pilot identifiers are not automatically
   implementation-specific.
6. **No validator was built or run.** All implementation claims are source- or
   document-level. The only behavioural evidence is third-party (OpenSysML,
   Syside) and is labelled as such.

---

## 7. Licence and attribution

The OMG specification text and machine-readable files are © Object Management
Group and the contributing organisations (see the PDF copyright page). They are
cited, not redistributed here. The extraction, classification, registers and
prose in this directory are the project's own work.
