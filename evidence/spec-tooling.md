# Evidence note: SysML v2 / KerML specs, Systems Modeling API, and the pilot implementation — versions and validation surfaces

**Retrieval date (all sources below): 2026-11-13 (UTC).**
**Method:** every source listed was retrieved and read in full or in the retrieved representation noted in the source table (§8). No claim in this note rests on a search-engine snippet alone; where a snippet was seen but the page could not be read, it is marked **NOT VERIFIED** in §7.
**Scope of this note:** facts, gaps and citations only. No synthesis, no research questions, no recommendations.

**Reading conventions used throughout**

- A plain statement with a link is a *quoted or closely paraphrased* source claim.
- **[INFERENCE]** marks my own reasoning from the cited material, not something a source asserts.
- **[CONFLICT]** marks two sources that disagree; the disagreement is reported, not resolved.

---

## 1. OMG SysML v2 and KerML: current formal versions

### 1.1 SysML 2.0 is formally adopted, not "in process"

- The OMG specification page for [SysML 2.0](https://www.omg.org/spec/SysML/2.0) lists **Document Status: `formal`**, **Publication Date: September 2025**, and a History table whose entry for 2.0 gives an **Adoption Date of September 2025**.
- The Systems Modeling community release repository states explicitly: "In June 2023, the OMG adopted the following three beta specifications for KerML, SysML v2 and the Systems Modeling API, which then entered the OMG finalization process… As of **30 June 2025**, these specifications have been formally adopted by OMG. The formal specifications were **updated editorially in March 2026** for submission to the International Organization for Standards (ISO)." ([SysML-v2-Release README](https://github.com/Systems-Modeling/SysML-v2-Release))
- Neither source describes SysML 2.0 as a draft, beta, or in-process document *at the 2.0 level*. A **2.1 revision is nonetheless in progress** — see §4.1 — but no published OMG specification page exists for it: `https://www.omg.org/spec/SysML/2.1` returned **HTTP 404** on retrieval (2026-11-13).

### 1.2 Exact document numbers

Normative documents listed on the [SysML 2.0 page](https://www.omg.org/spec/SysML/2.0):

| Document | OMG File ID | Format |
|---|---|---|
| Specification — Language | `formal/26-03-02` | PDF |
| Specification — Transformation (SysML v1 → v2) | `formal/26-03-03` | PDF |
| MOF XMI for the SysML v2 Abstract Syntax | `ptc/25-02-15` | XMI |
| UML XMI for the SysML v1 → v2 Transformation Model | `ptc/25-04-10` | XMI |
| KerML model interchange projects (KPAR), 7 domain/system libraries | `ptc/25-04-24` … `ptc/25-04-30` | KPAR |
| JSON schema for the JSON representation of the SysML Abstract Syntax | `ptc/25-04-32` | JSON |
| *Informative:* SysML textual notation file for the Simple Vehicle Model | `ptc/25-04-31` | `.sysml` |

The PDF itself confirms its own identity on the cover: "**OMG Document Number: formal/2026-03-02**, Date: March 2026, Part 1: Language Specification" ([SysML/2.0/Language/PDF](https://www.omg.org/spec/SysML/2.0/Language/PDF)).

KerML 1.0 ([spec page](https://www.omg.org/spec/KerML/1.0)): status `formal`, publication date **September 2025**, specification PDF **`formal/26-03-01`**, abstract-syntax MOF XMI `ptc/25-04-04`, four KPAR library projects, and two JSON schemas (`KerML.json` `ptc/25-04-21`, `KerML-Model-Interchange.json` `ptc/25-04-20`). It supersedes `KerML/1.0/Beta4`; SysML 2.0 supersedes `SysML/2.0/Beta4`.

**[CONFLICT — reported, not resolved]** The same specification carries two different dates: the OMG catalogue page says **Publication Date September 2025**, while the PDF cover says **Date: March 2026** and the file IDs are `formal/26-03-xx` (i.e. 2026-03). The Systems Modeling release README offers an explanation — adoption in June/September 2025, then an *editorial* update in March 2026 for ISO submission — but the two dates on OMG's own artefacts are not reconciled on any page I read. Anyone citing "the SysML 2.0 spec, dated X" must pick a convention and say which.

### 1.3 Spec structure: what is normative

Verified structure (from the [Language PDF](https://www.omg.org/spec/SysML/2.0/Language/PDF) table of contents):

- Clause **1 Scope**, **2 Conformance**, **3 Normative References**, **4 Terms and Definitions**, **5 Symbols**, **6 Introduction** (6.1 Document Overview, 6.2 Document Organization).
- Clause **7 Language Description** — the semantic description of each language area (from 7.2 Elements and Relationships onward, e.g. 7.5 Namespaces and Packages, 7.6 Definition and Usage, 7.17 Actions, 7.18 States), each area split into an "…Overview" clause and a "…Definitions and Usages" clause.
- Clause **8** — **8.2 Notation** (8.2.2 Textual Notation, 8.2.3 Graphical Notation), **8.3 Abstract Syntax** (metaclasses, and the OCL constraints that appear in release notes as `validateXxx`/`checkXxx`), and further sub-clauses of the same clause.
- OMG classifies the deliverable set itself: the two PDFs are under **"Normative Documents"**; the XMI/JSON/KPAR artefacts are under **"Normative Machine Readable Documents"**; the Simple Vehicle Model `.sysml` file is the only item under **"Informative Machine Readable Documents"** ([SysML 2.0 page](https://www.omg.org/spec/SysML/2.0)). The model libraries are separately described as "**Normative** model libraries for both KerML and SysML" ([SysML-v2-Release README](https://github.com/Systems-Modeling/SysML-v2-Release)).
- The spec's own compliance boilerplate states: "Software developed under the terms of this license may claim compliance or conformance with this specification **if and only if** the software compliance is of a nature fully matching the applicable compliance points as stated in the specification… In the event that testing suites are implemented or approved by Object Management Group, Inc., software… may claim compliance or conformance… only if the software satisfactorily completes the testing suites." ([Language PDF](https://www.omg.org/spec/SysML/2.0/Language/PDF))

**NOT VERIFIED (§7):** I did not retrieve the text of clause 2 "Conformance" or the back-matter annex list, so I cannot state from the document which annexes are labelled informative. The *catalogue-level* normative/informative split above is verified; the *annex-level* split is not.

### 1.4 KerML as the semantic foundation

KerML 1.0 is described on its own spec page as "an application-independent modeling language with a **well-grounded formal semantics**", providing "general syntactic constructs for structuring models… core semantic constructs that have semantics based on classification; and additional constructs for commonly needed modeling capabilities, such as associations and behaviors" ([KerML 1.0](https://www.omg.org/spec/KerML/1.0)). SysML's KerML-derived constructs are visible in the constraint names cited in pilot release notes (`validateEndFeatureMembership`, `validateFeatureValueOverriding`, `checkConnectorTypeFeaturing`), which are KerML constraints enforced when validating SysML models — see §3.3.

---

## 2. OMG Systems Modeling API and Services 1.0

- [Spec page](https://www.omg.org/spec/SystemsModelingAPI/1.0): status **`formal`**, publication date **September 2025**, specification PDF **`formal/26-03-04`**, supersedes `SystemsModelingAPI/1.0/Beta3`.
- What it standardises, per the page's own abstract: "(1) **Platform-Independent Model (PIM)** provides a service specification independent of any platform or technology. This specification defines each of the services and their operations with inputs and outputs. The PIM serves as the logical API model. (2) **Platform-Specific Models (PSMs)** are bindings of the PIM using a particular technology, such as **REST/HTTP, SOAP, Java, and .NET**. Multiple platform-specific models can exist for a given PIM."
- Normative machine-readable artefacts are the operative part for tooling:
  - MOF XMI for the API PIM — `ptc/25-02-29`
  - **JSON schema for OpenAPI Specification — `ptc/25-02-30`** (`OpenAPI.json`)
  - JSON schemas for KerML, SysML and API PIM — `ptc/25-02-31` (`Schema.json`)
  - OSLC shapes and vocabulary TTL for the **KerML** abstract syntax — `ptc/25-02-32`, `ptc/25-02-33`
  - OSLC shapes and vocabulary TTL for the **SysML** abstract syntax — `ptc/25-02-34`, `ptc/25-02-35`
  - Informative: "Zip archive of systems modeling API cookbook" — `ptc/25-02-36.zip`
- The API therefore standardises an OpenAPI-described REST surface, a JSON payload schema for the KerML/SysML abstract syntax, and **RDF/OSLC shapes** for the same abstract syntax. Project/repository structure is implied by the schema and shapes rather than stated in the abstract; the pilot API implementation is organised around projects, commits, branches and elements (see §5.4). **[INFERENCE]** — I did not read the API PDF, so the precise resource model (Project/Commit/Branch/Element/Relationship, query operators) is inferred from artefact names and from the pilot API server's usage, not quoted.

---

## 3. SysML-v2-Pilot-Implementation: releases, components, and what validation actually does

Repository: <https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation> ("Pilot implementation of the SysML v2 textual notation and visualization"). 268 stars, 72 forks, 22 open issues, 4,940 commits, default branch `master`. Licence changed from LGPL to **EPL-2.0** in the 2026-04 release.

### 3.1 Release lineage and cadence

Monthly tagged releases; the repository publishes 10 on the first releases page plus earlier pages (8 further pages exist). Latest and near-latest, from the [releases page](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/releases):

| Tag | Released | Eclipse plugin version | Headline content |
|---|---|---|---|
| **2026-09.1** | 28 Oct 2026 (**latest**) | **0.63.1** | Same as 2026-09 plus one bug fix |
| 2026-09 | 22 Oct 2026 | 0.63.0 | Default multiplicity change; new checks that connection/flow def end features are usages |
| 2026-08 | 11 Sep 2026 | 0.62.0 | Caching fixes; parse post-processing moved out of adapters |
| 2026-07 | 20 Aug 2026 | 0.61.0 | **"brings the implementation into conformance with the KerML 1.1 Beta 2 and SysML 2.1 Beta 2 metamodels"** and their model libraries |
| 2026-05 | 2 Jul 2026 | 0.60.1 | Metamodel updated for KerML 1.1/SysML 2.1 **Beta 1**, but "to promote compatibility, the metamodel URI is being kept the same as for 1.0/2.0 (**version date 20250201**)" |
| 2026-04 | 13 May 2026 | 0.59.0 | Licence LGPL → EPL; `org.omg.sysml.model` split out of the Eclipse plug-in |
| 2026-03 | 8 Apr 2026 | 0.58.0 | A **nonconformity** removed: filter expressions were not reporting `checkConnectorTypeFeaturing` violations |
| 2026-02 | 7 Mar 2026 | 0.57.0 | Removed metamodel-altering `isNonunique` |
| 2026-01 | 10 Feb 2026 | 0.56.0 | Getter overrides removed; **constraints that had never been checked are now checked** (see §3.3) |
| 2025-12 | 12 Jan 2026 | 0.55.0 | BNF Extractor tool (`tool-support/bnf-grammar`) to extract normative grammar from the spec PDFs |

Release assets (2026-09.1) are `jupyter-sysml-kernel-0.63.1.zip` (120 MB), `jupyterlab-sysml-0.63.1.tgz`, seven `.kpar` model-library archives, and source archives. **There is no standalone "validator" binary, CLI, or container published as a release asset.**

### 3.2 What the repository ships

From the [repository root listing and README](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation):

- **Xtext grammars and editors**: `org.omg.kerml.xtext{,.ide,.ui}`, `org.omg.sysml.xtext{,.ide,.ui}`, `org.omg.kerml.expressions.xtext{,.ide,.ui}` — i.e. the textual notation is implemented as Xtext grammars with generated Eclipse editors.
- **EMF model layers**: `org.omg.sysml.model`, `org.omg.sysml.model.bundle`, and (added 2026-05) `org.omg.sysml.logic`, `org.omg.sysml.logic.bundle` — the 2026-04/2026-05 refactor exists, in the release notes' words, "to allow its code to be more easily used outside the framework of Eclipse plugins".
- **Jupyter kernel**: `org.omg.sysml.jupyter.kernel`, `org.omg.sysml.jupyter.installer`, `org.omg.sysml.jupyter.jupyterlab`.
- **Visualisation**: `org.omg.sysml.plantuml` (+ `.eclipse`, `.feature`) — PlantUML rendering of the model.
- **Execution**: `org.omg.sysml.execution`, `org.omg.sysml.interactive`, `org.omg.sysml.interactive.tests` — the "interactive" layer that the Jupyter kernel and third-party CLIs drive.
- **KerML→OWL**: `org.omg.kerml.owl{,.ide,.ui}`.
- **Import/export**: `org.omg.sysml.uml.ecore.importer` (UML/Ecore import), and XMI serialisation handled inside the model layer (see §5.3).
- **Test suites**: `org.omg.sysml.xpect.tests`, `org.omg.kerml.xpect.tests` — Xpect-based grammar/semantics tests (the "pilot authors' test intent", per the third-party characterisation in §6).
- **Libraries**: `kerml`, `sysml`, `sysml.library` (normative model libraries, textual notation), plus `sysml/src/validation` and `sysml/src/examples` corpora (corpus names taken from the third-party differential harness in §6.1; **[INFERENCE]** I did not list those directories directly).
- Build: Maven/Tycho multi-project build; README pins **Eclipse 2025-12 (4.38)**, **Java 21**, "Xtext Complete SDK" and "QVT Operational SDK"; PlantUML view via a third-party p2 site (`https://github.com/himi/p2-update-puml-sysmlv2/...`).

### 3.3 What the validator actually checks — and does not

**(a) The validator is one Xtext validator file per language.** The SysML validation package contains exactly one source file: [`org.omg.sysml.xtext/src/org/omg/sysml/xtext/validation/SysMLValidator.xtend`](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/tree/master/org.omg.sysml.xtext/src/org/omg/sysml/xtext/validation) (directory listing; the file itself was not read in full). A third-party harness reports the corresponding compiled artefacts in the released kernel JAR: `org/omg/sysml/xtext/validation/SysMLValidator.class` (~79 KB), `org/omg/kerml/xtext/validation/KerMLValidator.class` (~88 KB), plus `KerMLResourceValidator`, `AbstractKerMLValidator`, `KerMLStandaloneSetup` ([OpenSysML, pilot differential](https://raw.githubusercontent.com/Open-MBEE/OpenSysML/0a5fa2d9405e24fc874379e1b5e1b5a3b3e0194e/docs/project/pilot-differential.md)).

**[INFERENCE]** Because validation is an Xtext `IResourceValidator` over an Xtext grammar, the three layers it can report are: (i) parse errors from the generated grammar, (ii) link/name-resolution errors from Xtext's linker, and (iii) `@Check` methods in `SysMLValidator.xtend`/`KerMLValidator.xtend`. The third-party harness confirms (i) and (ii) behaviourally — "on a malformed file… exits 1 with `no viable alternative at input 'def'`… and on a file that parses but does not resolve… it reports unresolved references, so it is exercising name resolution too, not just the parser" — and the release notes confirm (iii) by naming individual constraints.

**(b) Layer (iii) is a per-constraint OCL check set that has grown over time, with documented gaps.** Verbatim from the [2026-01 release notes](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/releases), where handwritten getter overrides were removed: "The following validation constraints were previously **not being checked**, since they were automatically satisfied due to getter overrides. Since these getter overrides have now been removed, checks have been implemented for all the constraints." The list given is KerML `validateEndFeatureMembership`, `validateParameterMembership`, `validateCollectExpressionOperator`, `validateFeatureChainExpressionOperator`, `validateIndexExpressionOperator`, `validateSelectExpressionOperator`, `validateFlowEndIsEnd`; SysML `validateUsageIsReferential`, `validateReferenceUsageIsReferential`, `validateAttributeUsageIsReferential`, `validateEnumerationDefinitionIsVariation`, `validateEventOccurrenceUsageIsReference`, `validatePortUsageIsReference`. **As of the 2026-01 release, those constraints effectively did not exist as checks.**

**(c) There are documented historical cases of the pilot accepting models the normative metamodel forbids.** The 2026-03 release notes state, of filter expressions using qualified names: "the `checkConnectorTypeFeaturing` constraint is impossible to satisfy for the binding connectors implied by these feature references. **The Pilot Implementation was not reporting this as an error, which was not conformant with the normative metamodel for KerML** (and, so, SysML, too)." The release "Removed code that suppressed violations of `checkConnectorTypeFeaturing`". This is a first-party admission that the pilot had a *suppression* in it, and that removing it is a **backward incompatibility** ("the above feature references will cause 'Must be accessible feature' errors").

**(d) Some behaviour is the implementation's choice where the specification is silent — acknowledged first-party.** The 2026-09 notes change default multiplicity so that "a usage with an explicit, non-redefinition owned subsetting does get the SysML 1..1 default multiplicity", and add: "For the specification, it is expected that this situation will be handled as part of the resolution to **SYSML21-185 ("Default multiplicities are not formally specified")**." The same notes list the change as a **Backward Incompatibility** that "may result in multiplicity violations in the interpretation of some models."

**(e) Validation is not the kernel's headline verb.** The kernel's magic-command directory contains `Eval.java`, `Export.java`, `Help.java`, `Listing.java`, `Load.java`, `MyMagicParser.java`, `Projects.java`, `Publish.java`, `Repo.java`, `Show.java`, `View.java`, `Viz.java` ([magic directory listing](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/tree/master/org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/magic)). **NOT VERIFIED:** whether a `%validate` command hides inside one of these files (e.g. `Listing.java` or `Load.java`); I read the file *names*, not their contents. What is verifiable is that no file is named for validation, whereas export, publish-to-repository, view and visualisation each are.

**(f) What the pilot demonstrably does not check (all third-party assertions, each with a stated basis).** From Sensmetry's vendor documentation, [Differences to the Pilot Implementation](https://docs.sensmetry.com/1.0.1/about/differences/) (Syside 1.0.1 docs):

- "**The Pilot Implementation sets out to implement the specification exactly as written, and deliberately adds no validation the specification does not call for.** Syside sets out to let you build models you can rely on, so it adds the checks that software engineering practice has shown to be worth having. **Type checking and type inference, which the specification does not mention at all**, are the largest example."
- Worked example: `attribute num : ScalarValues::Positive = 5.0;` — "This is fine according to the Pilot Implementation", because the pilot "tries to perform type checking by looking at bound feature types symmetrically", while an assignment should require one-way conformance.
- "Some implicit model elements are **not constructed, e.g. implicit binding connectors**. This is done for performance reasons… As a result, strict type checking is not working for all cases yet."
- "Multiplicity bounds are parsed as arbitrary `Expressions` and are not bound by LL parser limitations. **Pilot Implementation has this marked with TODO.**"
- Diamond/feature-hiding: a worked example where "Pilot Implementation does not detect any issues, but the example above is semantically inconsistent", and the pilot's own resolution gives `b0 == 7` where `validateFeatureValueOverriding` should yield `42` plus an error.
- `CauseAndEffect` metadata: "Pilot implementation **silently ignores** this unintended behavior. The result of this is that `CauseMetadata` and `EffectMetadata` can be applied to any element type without triggering diagnostics."
- Name resolution of expression bodies: "Syside resolves the last `fn` to `MinimizeObjective::fn`, whereas Pilot implementation does so to the body Expression itself".

From the OpenSysML differential (third-party, §6.1): the pilot "**evaluates expressions but executes neither actions nor state machines**"; and among authored invalid models, "the control-node succession rules the pinned pilot leaves **unimplemented**" are named as a permissiveness gap.

**Summary of the verified split.** Normative on OMG's side: the abstract syntax and its OCL constraints, the textual notation BNF, the model libraries, and the JSON schemas (§1, §2). Implementation choice on the pilot's side: which of those constraints are actually implemented and enforced (a set that grew materially in 2026-01 and 2026-03), how deep resolution goes, whether type checking or inference exists at all, whether implicit elements are materialised, and the diagnostics' wording, severity and location. **[INFERENCE]** No conformance statement, compliance claim, or test-attestation for the pilot against formal/26-03-02 appears in any artefact I read — the release notes and README make no conformance claim.

---

## 4. Version skew and known divergences

### 4.1 The tool is not tracking the 2.0/1.0 formal documents — it is tracking 2.1/1.1 betas

- Formal, published: **SysML 2.0 / KerML 1.0**, `formal/26-03-0x` (§1).
- Pilot, from the 2026-07 release: "This release brings the implementation into conformance with the **KerML 1.1 Beta 2 and SysML 2.1 Beta 2** metamodels" and model libraries, implementing issue resolutions "approved on KerML 1.1 RTF Ballot 3" and "SysML 2.1 RTF Ballot 3" ([releases](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/releases)).
- Earlier steps on that path: 2026-05 updated metamodels "for KerML 1.1/SysML 2.1 **Beta 1**"; that same release implemented resolutions from "KerML 1.1 RTF Ballot 2 (Ballot 1 vote was not quorate)" and "SysML 2.1 RTF Ballot 1/2".
- There is **no published OMG specification page for SysML 2.1** (`https://www.omg.org/spec/SysML/2.1` → HTTP 404, 2026-11-13). **[INFERENCE]** The validation semantics a 2026-09/2026-10 pilot enforces are therefore aligned to a revision whose normative text is not yet publicly downloadable at a stable URL; a third party aiming at "SysML v2 conformance" has no published 2.1 target to read.

### 4.2 Metamodel identity is deliberately frozen across versions

The 2026-05 release changed the metamodel for Beta 1, but: "The new metamodel is structurally the same as the KerML 1.0/SysML 2.0 metamodel. To promote compatibility, **the metamodel URI is being kept the same as for 1.0/2.0 (version date `20250201`)**." KPAR builds set `METAMODEL_TAG = 20250201` and a separate `BUILD_TAG` (e.g. `20260501`). **Practical consequence:** the version string inside a serialised model does **not** distinguish "2.0-era" from "2.1 Beta-era" artefacts. **[INFERENCE]** Any validation layer that wants to pin "which semantics was this model written for" cannot read that answer off the metamodel URI.

### 4.3 Release-date skew inside one OMG deliverable set

See **[CONFLICT]** in §1.2 (page says Sept 2025; PDF says March 2026; file IDs are `formal/26-03-*`).

### 4.4 Divergence inside the tool ecosystem on which revision is "current"

**[CONFLICT — reported, not resolved]** The pilot says it conforms to **SysML 2.1 Beta 2 / KerML 1.1 Beta 2** (2026-07 onward). OpenSysML's README states its own target as "**OMG SysML v2.1 Beta 1 / KerML 1.1 (2026-09 release)**" while pinning its comparison reference to pilot `2026-09` (artifact 0.63.0). Sensmetry's Syside 1.0.1 documents support for "**SysML v2 Standard Library 2026-03**". Three tools, three different statements of the semantic target, all published within months of each other. This is version skew, not necessarily error — but nothing I read establishes which revision each tool *actually* enforces.

### 4.5 Documented spec-level defects in the reference material

OpenSysML's conformance statement declares "**13 defect(s) in the published reference material** — 6 with a specification-derived correction, 7 documented without one, since no intended reading can be inferred" ([OpenSysML README](https://github.com/Open-MBEE/OpenSysML)). This is a third-party claim about the OMG corpus/spec, self-reported and not independently checked here; the underlying registry is at `docs/project/omg-issues.md` and `tools/oracle/errata` in that repository. **[INFERENCE]** Its existence demonstrates that at least one implementer found the published materials insufficient to decide some cases.

---

## 5. Interoperability mechanisms that exist today — and their status

### 5.1 Textual notation (`.sysml` / `.kerml`) — the de facto interchange surface

- The only *informative machine-readable* artefact on the SysML 2.0 page is a `.sysml` file (the Simple Vehicle Model, `ptc/25-04-31`). The normative machine-readable interchange formats are JSON schemas and KPAR archives.
- The pilot implements the textual notation as Xtext grammars (`org.omg.sysml.xtext`, `org.omg.kerml.xtext`), and in 2026-07 "Corrects textual notation BNF non-conformities between the implementation and the KerML and SysML specifications" — i.e. **the implementation's grammar and the normative BNF were, until that release, not identical** ([releases](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/releases)).
- A BNF Extractor tool was added in 2025-12 (`tool-support/bnf-grammar`) which "extracts the normative BNF for the KerML textual notation and SysML textual and graphical notations **from the corresponding specification documents**" — the normative grammar lives in PDF, and tooling to machine-read it is recent and maintained inside the pilot repo.
- **[INFERENCE]** Because the published normative grammar is a PDF annex and the only machine-readable grammar is an Xtext file inside one implementation, third-party parsers bootstrap from the pilot's Xtext grammar rather than from OMG. This is stated explicitly by OpenSysML: "Grammar source: **OMG pilot Xtext grammars** (`SysML.xtext` and `KerMLExpressions`)".

### 5.2 JSON / JSON-LD

- Normative JSON schemas exist for both abstract syntaxes: `SysML.json` (`ptc/25-04-32`), `KerML.json` (`ptc/25-04-21`), plus `KerML-Model-Interchange.json` (`ptc/25-04-20`) and API `Schema.json` (`ptc/25-02-31`).
- OMG's own catalogue pages are also published as RDF and JSON-LD (`…/About-SysML.jsonld`, `…/About-KerML.jsonld`) — that is metadata about the specification, **not** a model-interchange format.
- The pilot's kernel exposes an `Export.java` magic command and a `Publish.java`/`Repo.java` pair, i.e. export to file formats and publishing to an API repository are separate user-facing operations ([magic listing](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/tree/master/org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/magic)). **[INFERENCE]** The precise set of export formats is not stated in any page I read; I did not read `Export.java`.

### 5.3 XMI — exists, but explicitly *not* the normative model-interchange path

The clearest first-party statement is in the [SysML-v2-Release README](https://github.com/Systems-Modeling/SysML-v2-Release), describing the shipped library representations:

> "`sysml.library.xmi` — Normative model libraries… XMI representation. **Note: These are Eclipse XMI files (`.kermlx` and `.sysmlx` extensions), which is not a fully normative OMG XMI representation.** The XMI is exported without derived property values or implied relationships."
> "`sysml.library.xmi.implied` — … exported **with** derived property values and implied relationships."

So: (i) XMI serialisation exists and is used for the libraries; (ii) it carries a non-standard file extension and is described as not fully normative; (iii) there are two mutually different XMI flavours in circulation (with and without derived/implied elements). Release notes corroborate that XMI round-tripping has had conformance defects as recently as 2026-08 ("so that `isComposite = false` is preserved on an XMI roundtrip") and stability bugs (2026-07: "Fixes a StackOverflowError when loading a ResourceSet containing TransitionUsage elements"). The *normative* XMI on the spec page (`ptc/25-02-15`) is **MOF XMI for the abstract syntax**, i.e. the metamodel, not a model exchange format.

### 5.4 The API as the intended interchange path — implemented as a proof of concept

- Standard: SystemsModelingAPI 1.0, REST/HTTP PSM normative via `OpenAPI.json` (§2).
- Implementation: [`SysML-v2-API-Services`](https://github.com/Systems-Modeling/SysML-v2-API-Services) — self-described as a "**Proof-of-concept** pilot implementation for the Systems Modeling API and Services" and a "Pilot implementation of REST/HTTP Platform-specific model (PSM)… managed by the SysML v2 Submission Team (SST)". Stack: **Play framework, sbt, JDK 11, PostgreSQL**; 97 stars, 40 forks, 18 open issues, 599 commits.
- Two usage scenarios are offered: a deployed SST server (reachable via Swagger/Postman), or a local instance at `localhost:9000/docs`. The release README points at a **live prototype** at `http://sysml2.intercax.com:9000/docs/` and calls it "an API front end to a live prototype repository implementation" ([SysML-v2-Release](https://github.com/Systems-Modeling/SysML-v2-Release)).
- **NOT production-grade, by the maintainers' own words:** "proof-of-concept", "pilot", "live prototype", JDK 11 pinned, single-node PostgreSQL, no availability/deprecation statement on any page I read.

### 5.5 What does *not* exist (verified absence, as of 2026-11-13)

- **No OMG conformance test suite** in any artefact read: the spec's compliance clause mentions testing suites only conditionally ("In the event that testing suites are implemented or approved by Object Management Group"), and OpenSysML states "the OMG corpora are **demonstrations rather than an official conformance suite**" and "**no conformance certification is claimed**".
- **No standalone validator CLI** published by the pilot project (§3.1).
- **No published SysML 2.1 specification page** (§4.1).
- **No normative model-interchange XMI** for SysML v2, only the Eclipse-flavoured `.kermlx`/`.sysmlx` (§5.3).
- **No execution/behavioural reference**: the pilot "evaluates expressions but executes neither actions nor state machines" (third-party); OpenSysML accordingly self-assesses its own action/state-machine coverage "since no external referee executes behavior".

---

## 6. Independent / third-party parsers, validators and runtimes

Each entry states what it actually is — several are *wrappers around the pilot*, not independent implementations.

### 6.1 OpenSysML (Open-MBEE) — independent implementation in Go

<https://github.com/Open-MBEE/OpenSysML> — "Open Source SysML v2 Implementation in Go", **Apache-2.0**, 59 stars, 20 forks, ~19,024 commits, default branch `develop`. Self-described as "a SysML v2 and KerML 1.1 implementation in Go" providing "a language server, an interactive REPL, an execution runtime, an embeddable Go API, and Python, Node/TypeScript, Java, Rust, Julia and MATLAB client libraries". Architecture: "Parser/Lexer: **Hand-written recursive descent**", "Pluggable validation: **tiered passes (syntax → names → types → constraints)**". Ships `sysml`, `sysml-lsp`, `sysml-grpc`, `sysml-jupyter-kernel`, and notably `sysml-mcp` — "**MCP Server for Coding Agents**… serves the toolchain to OpenCode, Claude Code, Cursor, Codex, VS Code Copilot, Gemini CLI, Devin and any other Model Context Protocol host". Releases at v0.9.x/v0.12.x (pre-1.0).

Maturity caveats, in the project's own words: "no conformance certification is claimed"; the differential "is **one-directional**"; "the Xpect suites are the pilot authors' test intent rather than a certification oracle"; "**none of these is a percentage of the specification — no global compliance figure is claimed anywhere**"; the extension libraries (`DocumentQueries.sysml`, `OOSEM.sysml`, `MOSA.sysml`, `SysMLValidation.sysml`, …) are "**non-normative** OpenSysML extensions" — i.e. part of its validation surface is its own vocabulary, not OMG's. Self-reported differential against pilot `2026-09`: "524 of 924 files agree diagnostic-by-diagnostic; 122 diagnostics are ours alone and 2462 the reference's alone". (Its internal counts are not fully self-consistent across paragraphs of the README — one paragraph says "the reference rejects 5 that we accept", another says "0 the pinned pilot rejects and we accept" — so treat these as self-reported indicators, not measurements.)

It is also the source of the most detailed published account of the pilot's validation behaviour: [`docs/project/pilot-differential.md`](https://raw.githubusercontent.com/Open-MBEE/OpenSysML/0a5fa2d9405e24fc874379e1b5e1b5a3b3e0194e/docs/project/pilot-differential.md), which describes driving the pilot's own `IResourceValidator` and enumerating disagreement classes (`syntax`, `unresolved-reference`, `kind-mismatch`, `multiplicity`, `units`, `unmapped`).

### 6.2 DeciSym/sysmlv2-validator — a CLI wrapper, not an independent parser

<https://github.com/DeciSym/sysmlv2-validator> — "Command-line validator for SysML v2 files **using the OMG Pilot Implementation**". ISC licence, **1 star, 0 forks, 7 commits**. Requires Java 21+ and Maven; the `setup-dependency` profile "downloads the release and installs the kernel JAR into your local Maven repository" because "The OMG SysML v2 Pilot Implementation is released on GitHub, not published to Maven Central". Output is "GNU format (`file:line:col: severity: message`)". **Caveat:** whatever it reports is the pilot's verdict, wrapped; it adds no checks. Useful precisely because it makes the pilot scriptable — the OpenSysML harness used it as its initial oracle before replacing it with its own bridge.

### 6.3 Fabi303/sysmlv2tool — third-party, build status unresolved

Named in the OpenSysML differential as a candidate wrapper over the pilot jars with a better "directory mode", but: "**Not used — could not be built here.** Its directory mode is the better fit (one batch, one resource set), but it builds the pilot from a submodule through Tycho, and the build fails… `No implementation for org.eclipse.tycho.core.resolver.MavenTargetLocationFactory was bound`. Re-tried with Maven 3.9.9 without success." **NOT VERIFIED** — I did not read this repository; the claim is second-hand from OpenSysML.

### 6.4 Syside (Sensmetry) — commercial tool with an explicit divergence register

<https://docs.sensmetry.com/1.0.1/about/differences/> — vendor documentation, not open source. It is the only source I found that publishes a *structured list of places where it deliberately departs from the pilot*, with worked counter-examples (§3.3(f)). Its stated position: "SysML v2 arrives as two artifacts, and Syside is measured against both. The specification and its standard library are the normative text… The Pilot Implementation is the reference tool… **In practice it is also what other tools get compared against.**" Supports "SysML v2 Standard Library 2026-03". **Caveat:** vendor-authored; its characterisation of the pilot is not neutral, though its examples are concrete and checkable.

### 6.5 Named but NOT VERIFIED

- `cli_sysmlv2_syntaxchecker` (Ludovic Apvrille, Télécom Paris, `gitlab.telecom-paris.fr`) — appeared in search results only; the GitLab host served an anti-bot interstitial and I did not read it. Appears, from the name, to be a CLI syntax checker. **NOT VERIFIED.**
- An IEEE paper, "Ensuring Semantic Consistency in SysML v2 Models Through Metamodel-Driven Validation" (`ieeexplore.ieee.org/abstract/document/11077130`) — search result only, not read. **NOT VERIFIED.**
- An INCOSE paper, "OMG's Approach to Developing its SysMLv2 Certification Program" (`incose.org/wp-content/uploads/2026/01/Paper-238.pdf`) — **retrieval blocked**: HTTP 403, Cloudflare access challenge (`cf-ray a59d07b08d33656f-AMS`), recorded and **not** bypassed. Its existence suggests an OMG certification programme is being defined; **no claim about its content is made here.**

---

## 7. Gaps, access boundaries and things I could not verify

1. **SysML 2.0 clause 2 (Conformance) text** — not retrieved. Whether the spec defines named compliance points (and what they are) is unknown.
2. **Annex-level normative/informative split** — not verified (§1.3). Only the catalogue-level split is verified.
3. **`SysMLValidator.xtend` contents** — the file was not read; the *number* and *identity* of constraints it implements today is unknown. What is known is the set that was added in 2026-01 and specific constraints named in release notes.
4. **Whether the Jupyter kernel has a `%validate` command** — not verified (§3.3(e)).
5. **The API PDF's resource/service model** — not read; §2's resource model is inference.
6. **Export formats supported by the pilot** (`Export.java`) — not read.
7. **INCOSE certification paper** — Cloudflare 403, recorded, not bypassed (§6.5).
8. **Second-hand sources** — Fabi303/sysmlv2tool, and all OpenSysML characterisations of the pilot, are third-party statements I did not independently re-derive; they are attributed as such throughout.
9. **No file in this workspace other than `evidence/spec-tooling.md` was created or modified.** No `git`/`gh` commands were run.

---

## 8. Sources read (with retrieval timestamps, UTC, 2026-11-13)

| # | Source | URL | Retrieved | Status |
|---|---|---|---|---|
| 1 | OMG SysML 2.0 spec page | https://www.omg.org/spec/SysML/2.0 | 10:16:47 | 200 |
| 2 | OMG KerML 1.0 spec page | https://www.omg.org/spec/KerML/1.0 | 10:16:49 | 200 |
| 3 | OMG SystemsModelingAPI 1.0 spec page | https://www.omg.org/spec/SystemsModelingAPI/1.0 | 10:16:49 | 200 |
| 4 | SysML-v2-Pilot-Implementation repository | https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation | 10:16:52 | 200 |
| 5 | SysML-v2-Pilot-Implementation releases | https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/releases | 10:16:53 | 200 |
| 6 | SysML-v2-Release repository README | https://github.com/Systems-Modeling/SysML-v2-Release | 10:16:58 | 200 |
| 7 | SysML 2.0 Language Specification PDF (`formal/2026-03-02`) | https://www.omg.org/spec/SysML/2.0/Language/PDF | 10:17:27, 10:17:35 | 200 (front matter + TOC; 64,000 of 1,718,380 chars) |
| 8 | Pilot Jupyter kernel `magic/` directory | https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/tree/master/org.omg.sysml.jupyter.kernel/src/main/java/org/omg/sysml/jupyter/kernel/magic | 10:17:26 | 200 |
| 9 | Pilot `org.omg.sysml.xtext/.../validation/` directory | https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/tree/master/org.omg.sysml.xtext/src/org/omg/sysml/xtext/validation | 10:17:52 | 200 |
| 10 | SysML-v2-API-Services repository | https://github.com/Systems-Modeling/SysML-v2-API-Services | 10:17:23 | 200 |
| 11 | Sensmetry Syside — Differences to the Pilot Implementation | https://docs.sensmetry.com/1.0.1/about/differences/ | 10:18:01 | 200 |
| 12 | Open-MBEE OpenSysML repository README | https://github.com/Open-MBEE/OpenSysML | 10:17:43 | 200 |
| 13 | OpenSysML — Pilot Differential Diagnostics | https://raw.githubusercontent.com/Open-MBEE/OpenSysML/0a5fa2d9405e24fc874379e1b5e1b5a3b3e0194e/docs/project/pilot-differential.md | 10:17:12 | 200 (100,000 of 317,732 chars) |
| 14 | DeciSym/sysmlv2-validator | https://github.com/DeciSym/sysmlv2-validator | 10:17:40 | 200 |
| 15 | `https://www.omg.org/spec/SysML/2.1` | (same) | 10:18:07 | **404** |
| 16 | SysML-v2-Release `install/jupyter` | https://github.com/Systems-Modeling/SysML-v2-Release/tree/master/install/jupyter | 10:17:12 | 200 (contains no validation documentation; install instructions only) |
| 17 | INCOSE Paper-238 (certification programme) | https://www.incose.org/wp-content/uploads/2026/01/Paper-238.pdf | 10:18:01 | **403 Cloudflare challenge — access boundary, not bypassed** |
