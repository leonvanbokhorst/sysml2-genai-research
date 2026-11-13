# Evidence note: industrial MBSE practice — model integration, traceability, review, and expert judgement

**Retrieval date for all sources below: 2026-11-13 (UTC).** Evidence-only note: no recommendations, no research questions.
Each claim carries a URL. Where a source could not be read (paywall, bot challenge), that is stated and the claim is
either dropped or flagged as unverified. Anecdotal material is labelled as such.

---

## 0. Access boundaries hit while gathering this evidence (relevant to how much can be claimed)

| Source | URL | Result |
|---|---|---|
| INCOSE, *Systems Engineering Vision 2035* | https://www.incose.org/resources-publications/technical-products/se-vision-2035/ and https://www.incose.org/about-systems-engineering/se-vision-2035 | **HTTP 403, Cloudflare access challenge** (cf-ray `a59d0674ad0766f8-AMS`). Not read. |
| AIAA *Journal of Aerospace Information Systems*, "Enhancing System Model Quality: Evaluation of the SysML-Driven Approach in Avionics" | https://arc.aiaa.org/doi/10.2514/1.I011476 | **HTTP 403, Cloudflare challenge.** Title/venue only; body not read. |
| Altmanninger et al., "A survey on model versioning approaches", *IJWIS* 5(3), 2009 | https://doi.org/10.1108/17440080911006171 ; https://dblp.org/rec/journals/ijwis/AltmanningerB09.html | DOI resolves 404; dblp returns a bot-check page. **Citation not verified beyond search metadata** — therefore not relied on below. |
| Microsoft Research, "Overreliance on AI: Literature Review and Synthesis" | https://www.microsoft.com/en-us/research/publication/overreliance-on-ai-literature-review-and-synthesis/ | HTTP 404 at that path. Not read. |
| ISO/IEC/IEEE 15288, ISO/IEC/IEEE 29148 | iso.org catalogue | Paywalled; no normative text read. Statements about them below are marked **unverified**. |
| Eclipse EMF Compare project page | https://www.eclipse.org/emf-compare/ | HTTP 404. Not read. |

Consequence: this note is strong on the SysML v2 / OMG / TNO / OSLC / one peer-reviewed MBSE-quality study, and
**thin on the standards documents themselves** (15288, 29148, INCOSE Vision 2035). That thinness is itself reported in §7.

---

## 1. What standards and tooling actually require of a model beyond parseability

### 1.1 SysML v2 is now a formal OMG standard (Sept 2025), with a large industrial contributor base
- OMG lists SysML v2.0 as **formal**, publication date **September 2025**; language spec document `formal/26-03-02`, transformation spec `formal/26-03-03`. Machine-readable artefacts are normative: MOF XMI for the abstract syntax, a JSON schema, and KerML model-interchange "KPAR" projects for the Systems Library and the Analysis, Cause-and-Effect, Geometry, Metadata, Quantities-and-Units, and **Requirement Derivation** domain libraries.
  https://www.omg.org/spec/SysML/2.0/
- Contributing/copyright-holding organisations on the language spec include Airbus, Boeing, Lockheed Martin, IBM, Siemens, Dassault Systèmes (No Magic), PTC, Ansys, Sparx Systems, The MathWorks, MITRE, JPL, NASA-adjacent labs (Draper), CEA, KTH, University of Arizona, and INCOSE itself — i.e. the standard is vendor- and primes-endorsed, not academic-only.
  https://www.omg.org/spec/SysML/2.0/Language/PDF (front matter)
- OMG's own description of the language positions it as *facilitating* MBSE, and explicitly says "the language is intended to support multiple systems engineering methods and practices. The specific methods and practices may impose additional constraints on how the language is used."
  https://www.omg.org/spec/SysML/2.0/
  → **Implication for "fitness for use":** conformance to the language is not conformance to a method. The standard itself defers method-level constraints to adopters.

### 1.2 The Systems Modeling API and Services v1.0 (formal, Sept 2025) — also OSLC-aligned
- Defines a platform-independent service model (PIM) plus platform-specific bindings, including **REST/HTTP and OSLC** PSMs; normative machine-readable artefacts include OpenAPI JSON and **OSLC shapes and vocabulary TTL for the KerML and SysML abstract syntaxes**.
  https://www.omg.org/spec/SystemsModelingAPI/
- Corroborated in an independent public research report: the specification "includes a REST/HTTP PSM and OSLC PSM"; the API is "a Git-inspired way of handling" models and "includes functionality for model management, and diffing to compare model versions of different commits."
  TNO 2024 R12436, *SysML v2 as foundation for ESI tools?*, §2.2.1 — https://publications.tno.nl/publication/34643480/aS8CRr71/TNO-2024-R12436.pdf

### 1.3 What a model must additionally carry to be *used*: an independent 2024 assessment
TNO (Netherlands applied research organisation), Dec 2024, evaluated SysML v2 as a foundation for industrial embedded-systems tooling. Read in full; key statements:
- "As SysML v2 is not yet available as language in commercial tools, there are few concrete examples showing how SysML v2 model can…" (§2, around p.7).
- "Commercial tool support: industrial-grade tooling with commercial support is key for industrial adoption. **Currently, no commercial tools are available that support SysML v2**, but it is expected that these will become available in the near future." (§5.3)
- "There is **no documentation yet on how to add model validations**, and what is the advised [approach]" (§7 evaluation bullets).
- "Native support for viewpoints is part of the SysML v2 specification, but is **not yet implemented in the current tooling**." (§5.3)
- "SysML v2 is claimed to have a formal semantics, but **accessible documentation on this aspect is not available yet**." (§5.3)
  https://publications.tno.nl/publication/34643480/aS8CRr71/TNO-2024-R12436.pdf

### 1.4 What "fitness for use" is operationalised as, empirically
The clearest peer-reviewed operationalisation found is not a standard but a design-research study in automotive MBSE:
- Graessler, Wiechel, Oezcan & Taplick, "Tailored metrics for assessing the quality of MBSE models", *Proceedings of the Design Society: DESIGN 2024*, doi 10.1017/pds.2024.257.
  https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B6870DF22E1BA029FEF8D25AA56E9C97/S2732527X24002578a.pdf/tailored-metrics-for-assessing-the-quality-of-mbse-models.pdf
  Claims it makes that bear directly on "usable by systems engineers":
  - "The system model is the **authoritative source of information**"; MBSE's central artefact spans requirements, functions, logical and physical elements, and V&V ("RFLPV²").
  - Model quality "**depends on the object of observation**" and on project phase/maturity: "Models are at different stages of maturity … which means that the quality of the objective of observation varies."
  - Three stated shortcomings of existing quality approaches: (1) "standardised metrics without considering **company-specific and role-specific needs**"; (2) metrics "not tailored to the different phases"; (3) most address "information quality, not … the quality of an interdisciplinary system model".
  - "the experts **cannot use existing standards and norms, because these are too general** to determine the quality of specific artefacts" (citing Parra et al. 2019).
  - Determining information quality of engineering artefacts is "a demanding and **labour-intensive** activity"; quality assurance is treated as "an independent management task".
  → Empirically, "fit for use" is **stakeholder-, role-, phase- and company-specific**, and explicitly *not* derivable from a general standard.

### 1.5 INCOSE SE Vision 2035 / ISO 15288
- **Not retrieved** (see §0). Nothing in this note rests on their content. Any claim that these documents require a specific model property is therefore **unverified here** and must be checked against the primary text.

---

## 2. Model management in practice: versioning, diff/merge, baselines

- The SysML v2 API is explicitly "Git-inspired", with model management and **diffing between commits**; two version-control routes exist: plain Git over the textual notation, or the API. The report states the API "seems the preferred approach" once graphical models exist, "as the API works with **stable identifiers** for model elements. This provides also an advantage when restructuring the model, such that it is clear for example that **only model elements moved to a different location, instead of the whole model being flagged as changed**."
  TNO 2024 R12436 §2.2.1 — https://publications.tno.nl/publication/34643480/aS8CRr71/TNO-2024-R12436.pdf
  → This is direct evidence for the known failure mode of line-based VCS on models: **identity loss on restructuring**, producing whole-file churn rather than semantic diffs.
- The same report notes model state "are in a Git-like version control system" as a property of the SysML v2 pilot/server environment (§2.1–2.2, same URL).
- The SysML v2 specification ships a normative **JSON schema** and MOF **XMI** for the abstract syntax, and KerML interchange projects (KPAR) for libraries — i.e. the standard does provide machine-level interchange artefacts that a baseline/release process can pin.
  https://www.omg.org/spec/SysML/2.0/
- **Thin evidence:** no peer-reviewed study was located in this pass that measures merge conflicts, false diffs, or baseline/release breakage in SysML v2 (or SysML v1) model repositories. The dedicated model-versioning survey literature could not be verified (§0). Empirical claims about "what breaks" in industrial model management should be treated as **unestablished** on this evidence.

---

## 3. Requirements traceability: what the standards actually encode

### 3.1 Traceability in SysML v2 is language-level, not tool-level
From the normative language specification (`formal/26-03-02`), verified in the document text:
- §7.21 "Requirements".
- §8.3.21.8 `RequirementDefinition`; §8.3.21.9 `RequirementUsage`; §8.3.21.10 **`SatisfyRequirementUsage`**.
- §9.6 "Requirement Derivation Domain Library", including §9.6.2.2.3 `derivedRequirements` and §9.6.3 "Requirement Derivation".
- Framing: "The modeling of requirements, which is a special kind of constraint that **a subject must satisfy** to be a [valid design/…]" (§ around line 1847).
  https://www.omg.org/spec/SysML/2.0/Language/PDF
- Verification linkage exists in the language too: `VerificationCaseUsage` records "`verifiedRequirements`" (spec text, figure "Satisfied Requirements").
  Same URL.
  → So satisfy / derive / verify are **typed model elements with resolvable references**, not annotations. An automated producer can, in principle, emit them as first-class model content.

### 3.2 The adjacent integration standards a tool must speak
- **OSLC Requirements Management 2.1**, OASIS Standard, 21 June 2021 (editors from Boeing and KTH): defines "key RESTful web service interfaces for the management of Requirements, Requirements Collections and supporting resources defined in the OSLC Core specification."
  https://docs.oasis-open-projects.org/oslc-op/rm/v2.1/requirements-management-spec.html
- OSLC is named in the SysML v2 API specification as a supported PSM, with normative OSLC shapes/vocabulary for the SysML abstract syntax.
  https://www.omg.org/spec/SystemsModelingAPI/
- Industrial linkage in practice: "linking requirements specified in an external tool with their representation in the SysML v2 model"; an example OSLC server for the SysML v2 REST API exists on GitHub, and "Other commercial tooling will also support this integration, like PTC Windchill."
  TNO 2024 R12436 §2.2.1 — https://publications.tno.nl/publication/34643480/aS8CRr71/TNO-2024-R12436.pdf
  → Note the modality: "**will** also support". Vendor support for the OSLC/SysML v2 bridge is announced, not demonstrated in that report.
- **ReqIF** and **ISO/IEC/IEEE 29148**: not read in this pass (ReqIF not retrieved; 29148 paywalled). No claim is made here about their exact normative content.

### 3.3 What "traceability-compliant output" plausibly entails (synthesis of the above, stated as inference)
Not a recommendation, but a reading of the sources: identifiable requirement elements with stable identifiers (API/spec), typed satisfy/derive/verify links pointing at resolvable targets (language spec §8.3.21), and exportable/queryable representations exposed through REST/OSLC so external RM tools can dereference them (OSLC RM 2.1 + Systems Modeling API). *This is an inference from the three documents, not a quoted requirement.*

---

## 4. Interoperability reality: standard availability vs shipping support

- **December 2024 (TNO, primary assessment):** "Currently, **no commercial tools are available that support SysML v2**". Open-source tools supporting *subsets*: SysIDE (Sensmetry, textual), SysON (Obeo, graphical/Sirius), and the SysML v2 Submission Team's Jupyter and Eclipse plugins (textual editing + graphical viewing).
  Tools listed as **"will support SysML v2 later on"**: Dassault CATIA Magic / 3DEXPERIENCE; IBM Rhapsody/Harmony; Siemens SysML v2 Modeler + Teamcenter; Ansys Systems Architecture Modeler; Intercax Syndeia; Tom Sawyer Model-Based Engineer (graphical viewer via API); PTC modeler (graphical editing, **OSLC server**); Sparx Enterprise Architect (graphical editing, API); MathWorks System Composer (API).
  https://publications.tno.nl/publication/34643480/aS8CRr71/TNO-2024-R12436.pdf (§2.6, Tables 2.2/2.3)
- **Contrast, same period:** the OMG contributor lists for the SysML v2 language and API specs already include Dassault, IBM, Siemens, PTC, Ansys, Sparx and MathWorks — i.e. **standard authorship preceded product availability** by at least a year in these vendors.
  https://www.omg.org/spec/SysML/2.0/ ; https://www.omg.org/spec/SystemsModelingAPI/
- XMI/v1 exchange: the SysML v2 pilot tooling ships a `SysML2XMI` utility converting `.sysml` text to XMI files (TNO §2.2.2, same URL), and the MOF XMI for the v2 abstract syntax is a normative OMG document (`ptc/25-02-15`) — https://www.omg.org/spec/SysML/2.0/ . No vendor statement was found quantifying round-trip fidelity of XMI exchange; **not established**.
- No vendor documentation was located in this pass that states *shipped, generally available* SysML v2 import/export conformance (the AIAA and INCOSE vendor-adjacent pages were blocked, §0). **The gap between "standard published" and "tool ships it" is documented for Dec 2024 but not for 2026 here.**

---

## 5. Human judgement: review, quality, and the limits of automated checking

### 5.1 Review is labour-intensive, expert-dependent, and perspective-dependent
- Graessler et al. (DESIGN 2024): "As a varying group of experts need to be involved, the quality of the system model needs to be ensured from **different points of view**"; "for evaluation, the experts cannot use existing standards and norms, because these are too general"; quality assurance meetings are "conducted, to assess the model quality"; the activity is "demanding and labour-intensive".
  https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B6870DF22E1BA029FEF8D25AA56E9C97/S2732527X24002578a.pdf/tailored-metrics-for-assessing-the-quality-of-mbse-models.pdf
- TNO documents modelling decisions that validators do not settle, at the level of *which language construct is right*: §3.1.1 "Modeling an element as item, part, or attribute?", §3.1.2 "How to link structure and behavior?", §3.1.3 "Structuring a large model". Also: "Viewpoint for interface … users … would be valuable if they only have to look at interfaces, and can abstract from other aspects"; "User workflow … whether it is feasible to integrate with the workflow".
  https://publications.tno.nl/publication/34643480/aS8CRr71/TNO-2024-R12436.pdf
  → These are *adequacy-of-abstraction* questions (does this model express the right thing for this audience?), not conformance questions.

### 5.2 What automated checks can and cannot deliver (evidence from adjacent empirical work)
- Johnson, Song, Murphy-Hill & Bowdidge, "Why Don't Software Developers Use Static Analysis Tools to Find Bugs?", **ICSE 2013** (technical research track). Interviews with 20 developers at a large software company: all participants "felt that use is beneficial", yet "**false positives and the way in which the warnings are presented** … are barriers to use"; the authors call for "an interactive mechanism to help developers fix defects."
  http://2013.icse-conferences.org/content/why-dont-software-developers-use-static-analysis-tools-find-bugs.html
  → Empirical precedent that *sound-looking automated findings with false positives degrade acceptance*, and that tooling value depends on presentation, not just detection.
- TNO on validation mechanisms for SysML v2 (Dec 2024): only two routes exist — Eclipse IDE rules written in Xtend, or `constraint def`s inside the model (with an `assert constraint` example on mass budget); and "There is no documentation yet on how to add model validations, and what is the advised [approach]."
  https://publications.tno.nl/publication/34643480/aS8CRr71/TNO-2024-R12436.pdf (§2.5, §7)
  → At the time of writing, *the extension mechanism for domain-specific validation is an engineering task per organisation*, not a language feature.
- **Not found (searched, not located):** any study reporting inter-rater agreement between human reviewers of SysML/MBSE models; any study measuring the false-negative rate of MBSE model linting versus expert review; any published empirical test of "this model is a valid representation of the system" as a judgeable property. See §7.

### 5.3 Semantics
- TNO: "Well-defined, unambiguous semantics is key for formal analysis … SysML v2 is claimed to have a formal semantics, but accessible documentation on this aspect is not available yet"; open questions listed about whether semantics are preserved in analysis.
  https://publications.tno.nl/publication/34643480/aS8CRr71/TNO-2024-R12436.pdf (§5.3)
  → A parse-clean or type-check-clean model does not, on this evidence, come with publicly documented semantics sufficient to underwrite formal analysis claims.

---

## 6. How engineers actually consume (LLM-)generated artefacts

- **DORA / Google Cloud, *Accelerate State of DevOps Report 2024*** — key findings as published: "AI adoption significantly increases individual productivity, flow, and job satisfaction. However, it also **negatively impacts software delivery stability and throughput**"; the report frames the tradeoff as requiring attention to "the human element".
  https://dora.dev/research/2024/dora-report/
- **METR, "Measuring the Impact of Early-2025 AI on Experienced-Open-Source Developer Productivity", July 2025** — randomised controlled trial: "when developers use AI tools, they take **19% longer** than without". METR has since annotated the page: "⚠️ These results are out of date… historical results no longer reflect the current impact of AI models" (Feb 2026 update referenced).
  https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
  → Two distinct signals: *self-reported* gains (DORA) coexist with *measured* slowdowns in a rigorous RCT (METR), and METR itself dates the finding. Neither is systems-engineering-specific.
- **Gap:** no empirical study was located in this pass on how *systems engineers* review/accept LLM-generated SysML or MBSE artefacts (acceptance rates, review time, error classes caught vs missed, trust calibration). Search results in this space were tool-vendor announcements and consultancy commentary — **anecdotal**, not empirical, and not cited as evidence here.

---

## 7. Where the evidence is thin or absent (explicit)

1. **Normative standards text not read.** ISO/IEC/IEEE 15288 and 29148 are paywalled; INCOSE *SE Vision 2035* is behind an access challenge; ReqIF not retrieved. No claim in this note depends on their content; any statement about what they "require" of a model would need the primary documents.
2. **No empirical study of SysML v2 in industrial production use** was found. The strongest available statement is a Dec-2024 national-lab assessment that *no commercial tool supported SysML v2* and that "there are few concrete examples". Whether this changed by 2026 is **not established here**.
3. **Model-management breakage is asserted, not measured.** The identity-loss/churn failure mode of line-based VCS is described in a research report and structurally implied by the API design, but no study quantifying merge conflicts, false diffs, or baseline breakage in SysML v2 repositories was located.
4. **Inter-rater agreement in model review: absent** from what this pass could find. No kappa/agreement figures for expert judgement of model quality or model validity in MBSE were located.
5. **Automated-check false confidence: adjacent evidence only.** The static-analysis acceptance study (ICSE 2013) is software code, not models, and is 13 years old. No study was found that measures MBSE/SysML linting precision/recall against expert judgement.
6. **Vendor support claims are unverified for the present.** The detailed vendor mapping is from Dec 2024 and phrased prospectively ("will support"). Current GA conformance statements from Dassault, IBM, Siemens, PTC, Ansys, Sparx and MathWorks were not retrieved (vendor pages either blocked or not located in this pass). Consultancy/vendor blog claims on SysML v2 readiness encountered during search were **anecdotal** and are excluded.
7. **Interoperability fidelity: no measurements.** Round-trip XMI/JSON/OSLC fidelity between tools is not quantified in any source read here.
8. **LLM-consumption evidence is software-engineering, not systems-engineering.** DORA (2024) and METR (2025) are the only empirical anchors located, both for code, and METR has flagged its own result as historical. No study of *review effort* or *trust calibration* for LLM-generated system models was located.
9. **Quality-metric evidence is single-study and design-research based.** The company/role/phase tailoring claim rests on one DESIGN 2024 paper (with its own cited literature); no replication or independent validation was found.
