# Evidence note: prior published work on LLM/GenAI generation of SysML v2 (and transferable SysML/UML/MDE) models

**Retrieval date: 2026-11-13** (all web retrieval in this note was performed on this date; every URL below was fetched or attempted on 2026-11-13).

**Scope of this note.** Fact gathering only. It records (a) what two designated anchor papers built, measured and admitted, and (b) what else exists in the literature that a project on GenAI-generated SysML v2 models would have to position against. It contains no recommendations, no research questions, no novelty claims and no ranking of approaches.

**Verification legend used throughout**

- **[read full text]** — I read the full text of the source itself (PDF/HTML body text, not just the abstract).
- **[abstract/metadata only]** — I read only abstract/metadata (publisher blocked full text); all claims from such items are second-hand.
- **[cited-in-anchor]** — the item is known to me only because an anchor paper cites it; I did not open it. Treat as a pointer, not evidence.
- **[author-reported, unverified]** — a number or claim asserted by authors that I could not independently check (no shared data, no replication, no independent judge).

---

## 0. Access log — what I could and could not read

| Target | URL | Outcome |
|---|---|---|
| Anchor B (MDPI, *AI* 7(8):274) HTML | https://www.mdpi.com/2673-2688/7/8/274 | **403** (blocked, 397 bytes, no content) |
| Anchor B PDF | https://www.mdpi.com/2673-2688/7/8/274/pdf | **403** (blocked) |
| Anchor B, read via text proxy | https://r.jina.ai/https://www.mdpi.com/2673-2688/7/8/274 | **200**, full body text retrieved (~64.6 kB). Tables A1–A4 and Figures 4–6 are captions only in this representation — **table bodies and figure values were not captured**. |
| Anchor A (Elsevier, *Computers in Industry* 172:104350) on ScienceDirect | https://www.sciencedirect.com/science/article/pii/S0166361525001150 | not attempted after UC3M route succeeded |
| Anchor A, open-access VoR in UC3M repository | https://e-archivo.uc3m.es/bitstreams/44c9142f-1165-4fe6-8e0d-ebaddb6a489c/download (item https://hdl.handle.net/10016/48940) | **200**, 576 kB PDF, `pdftotext` extraction (~105 kB text). CC BY-NC. **Full text read, including Tables 1–4 and limitations.** |
| Wang et al. 2025 (Internetware) full text at ACM | https://dl.acm.org/doi/full/10.1145/3755881.3755926 | **403 Cloudflare access challenge** (cf-ray `a59d07a14cd9931d-AMS`). Not bypassed. |
| Olivert-Iserte et al. 2026 (MODELS) PDF | https://dl.acm.org/doi/pdf/10.1145/3837062.3839542 | **403 Cloudflare challenge** (cf-ray `a59d087fbe72662a-AMS`). Not bypassed. |
| Bucchiarone et al. 2026 (MODELS) PDF | https://dl.acm.org/doi/pdf/10.1145/3837062.3839372 | **403 Cloudflare challenge** (cf-ray `a59d08807a8b0e20-AMS`). Not bypassed. |
| Metadata for the two MODELS 2026 and the Internetware 2025 papers | Semantic Scholar Graph API (`api.semanticscholar.org/graph/v1/paper/DOI:...`) | **200**; abstracts retrieved. One search query returned **429** (rate limit). |

Consequence: for the three ACM-published items (Wang et al. 2025; Olivert-Iserte 2026; Bucchiarone et al. 2026) I have **abstract + search-snippet-level** information only, and I say so at each point.

---

## 1. Anchor A — Cibrián, Olivert-Iserte, Llorens, Álvarez-Rodríguez (2025), "An agent-based approach for the automatic generation of valid SysMLv2 Models in industrial contexts"

*Computers in Industry* 172:104350. Elsevier, peer-reviewed journal. CC BY-NC open access. Received 11 June 2025; accepted 13 Aug 2025; online 24 Aug 2025. DOI [10.1016/j.compind.2025.104350](https://doi.org/10.1016/j.compind.2025.104350); full text read from the UC3M repository copy: [hdl 10016/48940](https://hdl.handle.net/10016/48940). **[read full text]**

### 1.1 What exactly was built

A single-agent ("SysMLAgent", BDI-style architecture) pipeline that maps a natural-language prompt to SysML v2 textual notation, composed of:

- **RAG over a curated local repository of 92 SysML v2 examples** (code + natural-language descriptions). Retrieval by cosine similarity on sentence embeddings of dimension 384, `k = 1` nearest example injected into the prompt.
- **Validation engine based on the official SysML v2 ANTLR grammar** (lexer + parser); parse diagnostics are fed back to the LLM for iterative repair. The paper describes validation as "a two-stage process that encompasses both syntactic and semantic analysis", but the implemented checker documented in §3.4 is the ANTLR parser; the authors concede in the limitations that it "does not yet capture high-level domain-specific semantics, behavioral correctness, or system-level constraints."
- Beliefs/desires/intentions agent loop orchestrating retrieval → generation → validation → repair.

### 1.2 Models used

- Generation: **GPT-4o-mini** (OpenAI API) for the proposed system and for baseline BL1 and for the `LLM_Raw+RAG` ablation.
- Second baseline: **Gemini 2.5 Pro**, prompted directly (BL2).
- Decoding: "consistent low temperature setting (e.g., T = 0.2)".

### 1.3 What "valid" operationally meant

1. **Syntactic validity rate (%)** = proportion of generated models that pass the **official SysML v2 ANTLR grammar** via the authors' ValidationEngine. This is a parser-conformance check, nothing more.
2. **Solved prompts (%)** = system produced some model output for the prompt.
3. **Manual quality score (1–3)** using a published rubric (Table 3): 1 = low fidelity/incorrect; 2 = partial fidelity/incomplete or noisy; 3 = high fidelity/accurate and complete. Judged by **a single expert with MBSE/SysML v2 experience**.

No semantic checker, no simulation, no metamodel-constraint validation, and no comparison against reference models — "valid" in this paper means *parses under the official grammar* plus *one expert's 1–3 rubric score*.

### 1.4 Evaluation design

- **Task set:** `N = 20` hand-curated natural-language prompts (Table 2, verbatim in the paper: e.g. U1 "Create a part called AvionicMotor…", U14 "Create a requirement that an elevator stops at requested floors within 3 s"), spanning aerospace, automotive, healthcare, smart home, industrial automation, consumer electronics. "Approximately 15% of the prompts were specifically designed to involve concepts or combinations not explicitly present in the examples within the RAG database" — i.e. an explicitly intended (but small, ~3-prompt) generalisation probe.
- **Ground truth:** none. There are **no reference SysML v2 models** and no held-out test set. Quality is judged from the prompt alone by one expert. The prompt set was "designed such that at least one valid SysML v2 representation exists".
- **Generator/judge independence:** **not independent** — the manual scoring was done inside the author team ("Manual quality assessment was performed by a single expert… ensuring consistency across tasks"), with no inter-rater agreement, no blinding reported, and no second annotator.
- **Repeats:** not reported as repeated runs; one output per prompt per configuration (temperature 0.2).
- **Denominator caveat (author-stated):** configurations with a validation loop *discard* non-converging models, so `Agent_NoRAG` has fewer than 20 scored instances; "For approaches that do not include an iterative validation loop (such as BL1, BL2, and LLM_Raw+RAG), the output is always recorded, regardless of syntactic correctness, so the total number of evaluated outputs is consistently 20."

### 1.5 Headline numbers (Table 4, quoted exactly) **[author-reported, unverified]**

| System | Solved (%) (prompts) | Syntactic validity rate (%) | Manual quality (1–3), avg ± std |
|---|---|---|---|
| SysMLAgent (GPT-4o-mini) | 100 | 100 | 2.5 ± 0.3 |
| BL1: GPT-4o-mini | 100 | 0 | 1 ± 0 |
| BL2: Gemini 2.5 Pro | 100 | 0 | 1 ± 0 |
| Agent_NoRAG (ablation) | 20 | 20 | 1 ± 0 |
| LLM_Raw+RAG (ablation) | 100 | 55 | 1.9 ± 0.4 |

Supporting statements: RAG improves GPT-4o-mini from 0% to **55%** syntactic validity without the repair loop; adding the repair loop without RAG yields only **20%**; full system 100%/100%. The paper's claim about the combination being "not merely additive" rests on these five rows.

### 1.6 Threats to validity the authors admit

1. Performance "heavily depends on the quality and diversity of the examples stored in the RAG database"; novel constructs may not be covered.
2. The validator "does not yet capture high-level domain-specific semantics, behavioral correctness, or system-level constraints"; semantic validation layers are future work.
3. **"The manual evaluation … was conducted by a single expert, which may introduce subjective bias. Future evaluations should include multiple annotators and inter-rater agreement metrics."**
4. Offline, controlled setting with a curated prompt set; real-time/industrial deployment untested; latency from inference + retrieval/validation loop acknowledged.
5. Dataset size `N = 20` "poses a constraint on the broader generalizability".
6. "This study highlights a critical knowledge gap in current LLMs with respect to the SysML v2 language" — general-purpose models lack intrinsic SysML v2 syntax/semantics.

### 1.7 Threats to validity the authors do **not** admit (my reading of the text)

1. **Circularity between "validity" and the repair loop.** 100% syntactic validity is obtained *by construction*: invalid outputs are re-generated until they parse or discarded. The metric therefore measures the loop's convergence, not the model's generation quality; the authors report convergence failures only indirectly (the 20% in `Agent_NoRAG`).
2. **Non-comparable denominators.** The `Agent_NoRAG` 20% is computed over *successfully validated* models only (explicitly stated), while BL1/BL2 are 0% over all 20 outputs — so the ablation rows are not on the same footing as the baselines.
3. **The 0%/100% gap is suspiciously absolute** for two different frontier models (GPT-4o-mini *and* Gemini 2.5 Pro both at exactly 0% syntactic validity on 20 prompts). Either the parser is extremely strict (plausible for official SysML v2 grammar versions) or extraction/formatting (markdown fences, code blocks) dominated the failures. The paper does not analyse this: no per-output error taxonomy, no inter-model error comparison, no examples of the 0% outputs.
4. **The manual rubric conflates syntax and semantics.** BL1/BL2 score 1.0 ("significant semantic misalignment") partly because their outputs do not parse, so the quality column is not an independent semantic measure. Conversely `LLM_Raw+RAG` at 1.9 mixes 55% unparseable outputs into the average.
5. **No non-GenAI baseline, and this is a deliberate choice.** §4.3: "most existing tools in this category rely on structured inputs (e.g., predefined forms, logical expressions, or system templates) rather than free-form natural language, making direct comparison with our unstructured-input pipeline methodologically inappropriate. Second, many rule-based tools are domain-specific, proprietary, or do not support the latest SysML v2 standard". So the paper cannot say whether the agent beats a deterministic template/transformation baseline.
6. **Reference integrity.** Several bibliography entries are unverifiable or plainly mismatched. Example checked: "Jiang, Z., et al., 2024. A survey of large language models as agents. arXiv preprint arXiv:2401.12345" — [arXiv:2401.12345](https://arxiv.org/abs/2401.12345) resolves to *"Distributionally Robust Receive Combining"* (eess.SP), not to a survey of LLM agents. Other entries follow the same placeholder pattern (e.g. `arXiv:2402.12345`, `arXiv:2403.45678`, "Smith, J., et al., 2023. Automated model validation in MBSE. IEEE Syst. J.", several vendor-blog citations). I did not verify each one; the pattern is flagged as an evidence-quality signal about the state-of-the-art framing, not about the experiments themselves.
7. **No failure analysis of semantic errors at scale:** the paper asserts semantic shortcomings ("Prompts that combined multiple domain-specific elements … often led to incomplete or simplified models") qualitatively, with no counts, no error taxonomy frequencies, and no per-prompt breakdown.

### 1.8 Related item from the same group (in-progress programme)

Olivert-Iserte, J. (2026), "Trustworthy generation of SysML v2 models for physical systems: a multi-agent approach", *Proceedings of ACM/IEEE 29th MODELS*, DOI [10.1145/3837062.3839542](https://doi.org/10.1145/3837062.3839542). **[abstract/metadata only — ACM full text blocked by Cloudflare]**. This is a doctoral-consortium/Design-Science problem statement (same first author as Anchor A). Abstract states: LLM outputs "yield frequent violations of the language's formal ANTLR grammar and silent semantic inconsistencies"; the planned method couples "constrained generation with a layered validation authority (grammar-grounded syntactic repair and standards-aligned semantic judgement)" and connects Modelica/Simscape simulation models to SysML v2; planned evaluation "across the electronic and aerospace domains"; timeline to completion **2029**. Evidence content: none yet — it is a plan plus reference to already-published papers.

---

## 2. Anchor B — Stein, A. et al. (2026), "Prompt-Strategy-Driven SysML-v2 Artefact Generation Using Large Language Models for Model-Based Systems Engineering"

*AI* (MDPI) 7(8):274, published **23 July 2026**, 22 pages, open access CC BY. DOI [10.3390/ai7080274](https://doi.org/10.3390/ai7080274). Authors at Institute for Engineering Design, TU Braunschweig (A. Stein, N. W…, B. K…, S. B.-S., A. D., U. V. K., T. V.; initials only, as printed). **[read full text via text proxy; appendix tables not captured]**

### 2.1 What exactly was built

Not a system but a **five-phase human-in-the-loop workflow plus a comparison grid**: (1) input preparation, (2) prompt-strategy selection, (3) LLM selection, (4) artefact generation with a syntax-repair loop, (5) evaluation. Prompt strategies compared: **Zero-Shot, Few-Shot, Chain-of-Thought, Chain-of-Verification, RAG** (plus a platform-native "RAG Upload" condition). Artefact types: **requirements, block definition (BDD), state machine (STM)**.

Prior-state-of-the-art framing: a PRISMA-style search identifying **1207 studies**, reducing to **8 primary studies** after de-duplication, title/abstract screening, full-text assessment and snowballing, then scored with a "Harvey-Balls-based" scheme on methodological clarity, application relevance, LLM integration, MBSE relevance, SysML-v2 support, prompt engineering, tool/API integration and reusability.

### 2.2 Models used

- Generation: **ChatGPT-5.4 Pro (OpenAI), Gemini 3.1 Pro (Google), Llama 4 Maverick (Meta), DeepSeek-v3**.
- **Judge: Claude Opus 4.6** — explicitly "used separately for the LLM-as-a-Judge evaluation and was not one of the models compared for artefact generation." (Cross-provider judge; stated.)
- ChatGPT-5.5 used only for language editing/translation of the manuscript (disclosed in the AI-use statement).
- Human-in-the-loop: no human expert evaluation of artefact quality was performed (see 2.6).

### 2.3 What "valid" operationally meant

Two separate things:

1. **Syntactic validity:** the generated SysML v2 code "was imported into Cameo (Magic Systems of Systems Architect/Cameo Enterprise Architecture 2026x). An artefact was considered syntactically valid when the import was completed successfully and no syntax errors preventing parsing were reported by the tool." Failure diagnostics drive **up to five correction iterations** ("part of the syntax-repair procedure… did not constitute independent repeated experimental runs").
2. **Quality:** (a) **precision/recall/F1 against "reference artefacts"** for requirements and selected structural elements; (b) **LLM-as-a-Judge**, criteria "completeness, consistency, syntactic plausibility, semantic correctness, and suitability for the intended MBSE task", criterion ratings summed and divided by the maximum attainable score → normalized 0–1.

### 2.4 Evaluation design

- **Case study:** one traction battery system for BEVs; three tasks (requirements, BDD, STM).
- **Design size:** "20 core model–prompt configurations for each modelling task, supplemented by two platform-native RAG Upload configurations for requirements generation, resulting in **62 configurations overall**." (4 models × 5 strategies = 20 per task; RAG Upload was only available for ChatGPT and Gemini.)
- **Repeats:** **"Each model–prompt–task configuration was generated once."** The authors state this explicitly and interpret accordingly ("these results should be interpreted as descriptive findings for the investigated case study rather than as generally optimal prompt–model configurations").
- **Ground truth:** author-constructed "reference artefacts designed for this use case on the basis of the same data the LLMs are given". There is **no independently authored ground truth, no held-out task set, no second case study, and no train/test separation** (not applicable, since there is no training — but equally no held-out evaluation).
- **Generator/judge independence:** partially addressed — the judge is a *different provider* from all four generators, which removes direct self-preference for the generator family; but the judge rubric was defined by the authors, judging runs are single (number of judging runs is stated to be in Table A4, whose body I could not retrieve), there is **no human expert panel**, and judge scores were **not** "independently calibrated against assessments by multiple MBSE experts" (author-stated).
- **Reported numbers are only partly numeric in the body text:** requirements F1 values are given in prose; BDD F1 and judge values are given only in Figures A2–A5 (which I could not read), with only qualitative statements ("CoT and CoVe received the highest average normalized judge scores, while RAG received lower scores in the BDD task").

### 2.5 Headline numbers, quoted exactly **[author-reported, unverified; single generation per configuration]**

Requirements generation:
- "ChatGPT and Gemini each achieved an overall F1-score of **0.80**" under RAG Upload — "the highest observed values in this task".
- "ChatGPT improves from **0.47** in the Zero-Shot setting to **0.80** with RAG Upload, while Gemini improves from **0.45** to **0.80**."
- RAG (without platform upload) "produced lower observed scores" than RAG Upload; values not given in prose.
- Ordering: RAG Upload > CoVe > CoT in the requirements task.

State-machine modelling (LLM-as-a-Judge, normalized 0–1):
- CoT "reaches the highest average normalized prompt-strategy score of **0.88** and is the only strategy for which all four models achieve at least **0.75**."
- By model: **ChatGPT 0.95**, **DeepSeek 0.85**, **Gemini 0.80**, **Llama 0.55**; ChatGPT "received the … maximum rubric score in four of the five prompt strategies".

Block definition modelling:
- CoVe "achieved the highest combined observed performance for this task … considering both the F1-based and judge-based assessments"; ChatGPT had high judge ratings "even though its F1-score was low in several configurations due to over-modelling and terminology mismatch". **No BDD F1 numbers appear in the body text.**

Cross-task: "no single prompt–model configuration achieved the highest observed score across all investigated SysML-v2 artefact types."

### 2.6 Threats to validity the authors admit

1. One engineering case study; a fixed set of LLMs and prompt strategies; results are "descriptive findings for the investigated case study".
2. "F1-score evaluation depends on the selected reference artefacts" / "depends on the chosen ground truth".
3. "LLM-as-a-Judge assessment may introduce evaluator bias" and provides "rubric-based comparative indicators rather than definitive measures of engineering validity"; scores "were not independently calibrated against assessments by multiple MBSE experts".
4. F1 is insensitive to naming, granularity and decomposition choices, so "semantically useful models may differ from the reference"; F1 alone is "insufficient as the sole evaluation method for structural SysML-v2 artefacts".
5. The RAG Upload condition was platform-specific and confounds retrieval with platform document-ingestion/context handling ("does not isolate the effect of retrieval augmentation").
6. Prompt wording, model-version changes and available context may influence results; hidden provider reasoning "was neither accessible nor assessed".
7. Each configuration generated once.
8. Future work: compare LLM-as-a-Judge against "assessments from experienced systems engineers".

### 2.7 Threats to validity the authors do **not** admit (my reading)

1. **No human ground truth at all.** For a paper whose central claim is about engineering-artefact quality, no systems engineer scored any artefact. The only external quality signal is another LLM (Claude Opus 4.6) scored against an author-written rubric, run once.
2. **Reference artefacts derived from the same input the generators received.** This makes F1 a closeness-to-the-authors'-own-modelling-choices measure; because reference design followed the same source text, high F1 cannot distinguish "correct" from "copied phrasing/structure".
3. **No held-out task set and no second domain** — so the cross-task, cross-model conclusions are within-sample descriptions of one battery case.
4. **Repair loop is inside the measurement.** Up to five syntax-repair iterations precede "syntactic validity"; the paper does not report how many configurations needed repair, how many converged, or how many failed after five iterations. So the reader cannot tell whether "valid" artefacts were first-pass or sixth-pass generations, nor the residual failure rate.
5. **Single generation plus per-configuration claims.** With n = 1 per cell and normalized judge scores to two decimals (0.95, 0.88, 0.85, 0.80, 0.55), no variance estimate exists; the "no single strategy wins everywhere" conclusion is asserted from unreplicated cells.
6. **Judge scale construction** ("summed and divided by the maximum attainable total") is described, but criterion weights, scale granularity, prompt to the judge, and number of judging runs live in Table A4, which I could not retrieve — so judge reliability is not verifiable from the text I read.
7. **No negative or null result is reported** anywhere: every configuration appears to produce scoreable artefacts, no configuration is reported as failing, and no error taxonomy with frequencies is given.
8. **Data availability:** "The dataset available on request from the authors" — no artefact repository, no prompts published, no reference artefacts published, no code.

---

## 3. The wider landscape: LLM-driven SysML/UML/requirements-to-model generation

### 3.1 Empirical studies of LLM → SysML behaviour models

**Wang, Y.; Ge, N.; Liu, J.-X.; Cao, Z.; Chen, Z.-P.; Hu, C.-M. (2025). "Generating SysML Behavior Models via Large Language Models: an Empirical Study." *Proceedings of the 16th International Conference on Internetware* (ACM), pp. 366–377. DOI [10.1145/3755881.3755926](https://doi.org/10.1145/3755881.3755926).** Peer-reviewed conference paper, hybrid open access (CC BY per Semantic Scholar metadata). **[abstract/metadata only — full text blocked by Cloudflare]**

Abstract-level facts: they (1) "construct and publish a dataset of **107 SysML behavior models** spanning various domains" and (2) analyse hallucinations in LLM-assisted SysML behaviour-model generation "from syntactic and semantic perspectives" and propose model-checking rules to mitigate them. Reported results: "Across both phases, LLMs achieve **over 90% grammar accuracy**. For semantic accuracy, the average **F1-score for ACT reaches 95%, while SD drops to just 50%**." Conclusion quoted: model-checking rules "effectively correct format and syntax" but are "insufficient for addressing deeper semantic gaps"; remediation needs "counterexamples and simulation traces"; and "model-checking in LLM-based generation is costly".

Search-snippet-level detail (from indexed ACM full text, **not verified against the paper**): the dataset is "107 SysML behavior models: **36 activity diagrams, 34 state machine diagrams, and 35 sequence diagrams**"; the paper contains per-case error-type tables with percentages (e.g. a row reading "STM: Transition syntax error 4 16.00%"), and evaluates on engineering cases including a pump/control-system case. Model providers: snippet-level evidence suggests "three models from one provider" for at least part of the setup — **[unverified]**, and note this is the *opposite* design choice to Anchor B's four-provider grid.

Why it matters for the landscape: this is the only item found that (a) publishes a SysML behaviour-model dataset, (b) separates grammar accuracy from semantic accuracy with a *semantic* metric, and (c) reports a **non-trivial negative result** (sequence-diagram semantic F1 ≈ 50%, semantic repair unsolved).

### 3.2 A validated SysML dataset + benchmark (preprint, Oct 2026)

**Aryashad, A.; Jin, Y. (2026). "A Validated Dataset and Benchmark for Coherent Multi-Diagram SysML Models." arXiv:2610.07356 [cs.SE], submitted 5 Oct 2026.** **[preprint — not peer-reviewed at time of retrieval]** Abstract read: [arxiv.org/abs/2610.07356](https://arxiv.org/abs/2610.07356). **[abstract/metadata only]**

Reported content: **SEMAADB** ("Systems Engineering Modeling Assistant with AI Dataset and Benchmark"), "a dataset of **3,000 engineering contexts and 15,000 diagrams**", each context containing five linked SysML views (Requirement, Block Definition, Activity, State Machine, Sequence); diagram sets "checked … for consistency and valid rendering"; "a set of **100 contexts is also human-verified** and forms the benchmark test set". Tasks: diagram repair and cross-diagram update. Headline numbers quoted: "the strongest model repairs **64.3%** of semantic errors"; "the best propagation **F1 is 80.7%**". Conclusion quoted: "syntax repair is nearly solved, but semantic repair and consistency across diagrams are still challenging".

Caveats I flag: the abstract does **not** state whether the artefacts are SysML v2 textual notation or SysML v1 diagram interchange (the term used is "SysML views"/"diagram"), nor which models were evaluated, nor whether the 100-context test set was used as a held-out set for model selection; the "human-verified" set is described as verified for consistency/rendering, not as an expert-modelling-quality judgement. It is a single-author-team preprint with no replication yet.

### 3.3 SysML v2-specific LLM work that is *not* model generation

- **Li, Z.; Husung, S.; Wang, H. (2025). "LLM-Assisted Semantic Alignment and Integration in Collaborative Model-Based Systems Engineering Using SysML v2."** arXiv:2508.16181 (v2, 6 Jul 2026); journal reference: *2025 IEEE International Symposium on Systems Engineering (ISSE)*, DOI [10.1109/ISSE65546.2025.11369983](https://doi.org/10.1109/ISSE65546.2025.11369983). **[abstract read; peer-reviewed venue per journal reference]**. A "structured, prompt-driven approach" using a GPT-based LLM for model extraction, semantic matching and verification across independently developed SysML v2 models, using alias/import/metadata extensions for "traceable, soft alignment". Demonstrated on **a single example (a measurement system)**; "benefits and limitations are discussed" — i.e. demonstration paper, no quantitative benchmark, no ground-truth scoring reported in the abstract.
- Other SysML v2 + LLM items are known to me only from Anchor B's reference list: DeHart (2024), "Leveraging LLMs for Direct Interaction with SysML v2", *INCOSE Int. Symp.* 34:2168–2185, DOI 10.1002/iis2.13262 (conversational interaction with models, not generation); Rafique, Shah, Dalecke, Grimm (2025), "Enhancing Model-Based Systems Engineering with LLMs", INCOSE Int. Symp., pp. 1523–1543; Crabb & Jones (2024), SoSE, pp. 110–115; Patel, Maheshwaran, Santhya (2024), IEEE SPACE, pp. 871–874. **[cited-in-anchor — not opened]**

### 3.4 Non-GenAI baselines: what comparator evidence exists

- **Anchor A deliberately reports none**, with the quoted justification in §1.7(5). This is the single most conspicuous baseline gap in the SysML v2 generation literature I found.
- **The nearest comparator precedent is in model-transformation research, not SysML:** **Bucchiarone, A.; Di Rocco, J.; Pierantonio, A. (2026). "How Well Do LLMs Suggest Metamodel Mappings? A Multi-Provider Benchmark on Hand-Written ATL Transformations."** *Proceedings of ACM/IEEE 29th MODELS*. DOI [10.1145/3837062.3839372](https://doi.org/10.1145/3837062.3839372). **[abstract/metadata only — ACM full text blocked]**. Abstract facts: they build "a **multi-provider benchmark** of LLM-based metamodel-mapping suggestion … over **eight canonical ATL Transformation Zoo transformations**, with a **ground truth reverse-engineered automatically from the hand-written .atl sources** and a **partial-match-aware comparison scheme**", evaluating **GPT-4o, Claude Opus 4.6 and Mistral Large against a non-LLM EMFCompare baseline**. Reported: "All three providers suggest class-level mappings precisely and clearly outperform the baseline; feature-level quality is lower but does not collapse, with references harder than attributes." Also: "the matched mappings are almost all exact, the partial-match weight has little leverage"; "providers' self-reported confidence is well-aligned with correctness, letting a confidence threshold trade recall for precision"; "All artefacts are publicly available." Explicit framing: existing evidence "typically rests on a single provider, on manually curated ground truth, and on hit-or-miss scoring" — i.e. the same three weaknesses visible in §1 and §2 above.
- Other non-GenAI/non-LLM comparator work located but **not read**: a metamorphic-testing approach to bidirectional model transformations (Elsevier, *Information and Software Technology*, [S0950584918301538](https://www.sciencedirect.com/science/article/abs/pii/S0950584918301538)); a rule-based NLP vs fine-tuned-LLM UML comparison in an educational setting (IEEE, [document 11271276](https://ieeexplore.ieee.org/abstract/document/11271276)). **[located only, not verified]**

### 3.5 Benchmarks, datasets, shared evaluation protocols — what exists

What I found:

| Artefact | What it is | Status |
|---|---|---|
| Wang et al. 2025 dataset of 107 SysML behaviour models (36 ACT / 34 SM / 35 SD) | Dataset released with a peer-reviewed Internetware 2025 paper; SysML (version not confirmed from abstract) behaviour diagrams | **Exists** (paper states it is published; I did not access the artefact itself) |
| SEMAADB (arXiv:2610.07356) — 3,000 contexts / 15,000 diagrams, 100 human-verified test contexts | Dataset + benchmark for *multi-diagram coherence* (repair, cross-diagram update) | **Exists as a preprint**; SysML version unconfirmed from abstract |
| Anchor A prompt set (N = 20) | Curated prompts published as Table 2 in the paper; **no reference models released**; "Data will be made available on request" | Partial, not an evaluation asset |
| Anchor B artefacts | Not released ("dataset available on request"); reference artefacts unpublished; prompts unpublished | Not a shared asset |

**No shared evaluation protocol, metric suite, held-out task set, or leaderboard for "GenAI → SysML v2 model" exists in anything I retrieved.** The two anchors use **incompatible, non-overlapping** operational definitions of success: parser-pass rate + single-expert 1–3 rubric (Anchor A) versus Cameo-import success + author-reference F1 + single-provider LLM judge (Anchor B) versus grammar accuracy + semantic F1 against a released 107-model dataset (Wang et al.). No paper I read reports inter-rater agreement, a human expert panel, or a held-out test set for SysML v2 generation.

### 3.6 Validating generated formal artefacts: bounding evidence from outside MBSE

- **Format restriction degrades reasoning — peer-reviewed, EMNLP 2024 Industry Track.** Tam, Z. R.; Wu, C.-K.; Tsai, Y.-L.; Lin, C.-Y.; Lee, H.-y.; Chen, Y.-N. (2024). "Let Me Speak Freely? A Study On The Impact Of Format Restrictions On Large Language Model Performance." *Proc. EMNLP 2024: Industry Track*, pp. 1218–1236, DOI [10.18653/v1/2024.emnlp-industry.91](https://doi.org/10.18653/v1/2024.emnlp-industry.91). **[abstract read, full text not read]** Abstract: "we observe a **significant decline in LLMs' reasoning abilities under format restrictions**" and "**stricter format constraints generally lead to greater performance degradation in reasoning tasks**". Relevance to SysML v2: the language's textual notation is exactly a strict format; this is the clearest published warning that forcing grammar-conformant output can cost semantic quality — the trade-off neither anchor measures.
- **Grammar-constrained decoding** (peer-reviewed, NeurIPS 2024): "Grammar-Aligned Decoding" (Park et al.), [neurips.cc/virtual/2024/poster/96599](https://neurips.cc/virtual/2024/poster/96599). **[located only, not read]** — I record it as the canonical pointer for constrained-decoding distortion; I did not verify its numbers, so no figures are quoted here.
- **Self-repair has measured limits — peer-reviewed, ICLR 2024.** Olausson, T. X.; Inala, J. P.; Wang, C.; Gao, J.; Solar-Lezama, A. (2024). "Is Self-Repair a Silver Bullet for Code Generation?" arXiv:2306.09896v5 / ICLR 2024. **[read full text]** Key numbers, quoted: with cost accounted for, "performance gains are often modest, vary a lot between subsets of the data, and are sometimes not present at all"; for GPT-4 on APPS, "drawing 10 samples up front and then 1 repair candidate each (up to 20 samples total) leads to a pass rate **1.05×** higher than pass@20 from the same model without repair; drawing 2 samples up front and then drawing 10 repair candidates each (up to 22 samples total) leads to a pass rate which is **lower** than the baseline pass@22 (**0.97×**)"; replacing GPT-4's own feedback with an expert human programmer's "increas[es] the fraction of repaired programs which pass the tests by a factor of **1.58×** (from **33.3%** to **52.6%**)" (Table 1: GPT-4 feedback 42.64% / 19.33% / 3.67% / 33.30% vs human 62.21% / 45.67% / 14.67% / 52.60% across Introductory/Interview/Competition/Overall). Qualitative: GPT-4's feedback "is much more likely to be inaccurate (32/80 vs. 7/80 for the human feedback)"; GPT-4 "never" expresses uncertainty (0/80 vs 7/80). Relevance: both anchors rely on a validation-feedback repair loop; this is the best published evidence that such loops are bottlenecked by feedback quality and that **the compute-matched baseline (more independent samples, filtered by the same validator) is the comparison that determines whether the loop helped at all**. Neither anchor runs a compute-matched or sample-matched comparison against repeated independent generation filtered by the same validator.
- **Model checking is expensive and repairs syntax more than semantics** (Wang et al. 2025, abstract, quoted in §3.1): model-checking rules fix format/syntax but not semantic gaps.

---

## 4. Explicitly: where the literature has no evidence

These are gaps, stated as absences, not filled with inference:

1. **No independent ground-truth SysML v2 model corpus for generation tasks.** Neither anchor used reference models not authored by the same team from the same source text. (Wang et al.'s 107-model dataset and SEMAADB are the only candidates found; neither is used by either anchor; Wang's full text and SEMAADB's artefact licence/availability were not verified by me.)
2. **No human expert panel with reported inter-rater agreement** for SysML v2 generation quality, in any paper I read. Anchor A: one expert, author-side, no IRR. Anchor B: no human judging at all. **[no evidence found]**
3. **No held-out task set, no cross-domain generalisation test, no second case study** in either anchor (Anchor A: one prompt set; Anchor B: one traction-battery case).
4. **No negative results** in either anchor: no configuration reported as failing, no error taxonomy with frequencies, no per-prompt failure list, and no report of how many artefacts failed after maximum repair iterations (Anchor B: up to five; Anchor A: convergence failure inferred only from the 20% ablation).
5. **No compute-matched or sample-matched comparison** anywhere in the SysML v2 generation literature: no paper I found compares "N independent samples filtered by validator" against "1 sample + repair loop", which is the comparison Olausson et al. show can reverse conclusions in code.
6. **No comparison to non-GenAI baselines** for SysML v2 generation: Anchor A explicitly declines; Anchor B has none; I found no other SysML v2 paper with a rule-based/template/ATL baseline. The only LLM-vs-non-LLM comparator evidence I found is in metamodel mapping (EMFCompare, §3.4), not SysML generation. **[no evidence found]**
7. **No published human-vs-LLM-judge correlation study** for SysML artefact quality; Anchor B lists this as future work.
8. **No benchmark or shared metric protocol** for LLM→SysML v2 generation; metric definitions differ in kind (parser pass vs tool import vs element F1 vs LLM rubric), so cross-paper numbers are not comparable. **[no evidence found]**
9. **No evidence on semantic/behavioural correctness of generated SysML v2** (does the state machine actually match the requirement? does the model simulate?) — no paper I read reports simulation-based or constraint-based semantic validation of generated SysML v2; all "semantic" measurements are either LLM rubric scores or element-level F1 against author references. Anchor A states explicitly that behavioural correctness is out of scope.
10. **No SysML v2-specific dataset scale statistics**: nothing reports token-level or element-level complexity distributions of SysML v2 corpora, or how much SysML v2 text exists in model pre-training data (Anchor A asserts a "critical knowledge gap in current LLMs with respect to the SysML v2 language" without measurement).
11. **No evidence on whether "valid" per parser equals "usable" in a tool**: Anchor B uses Cameo import as the validity gate and Anchor A uses ANTLR; no paper cross-validates the two gates, so a parser-passing artefact's tool-level usability is unmeasured.
12. **No reproducibility artefacts** for either anchor (Anchor A: "data available on request"; Anchor B: "dataset available on request", no code, no prompts, no reference models).

---

## 5. Consolidated reference list (with access status)

| # | Item | Venue / year | Peer-reviewed? | Access |
|---|---|---|---|---|
| 1 | Cibrián, Olivert-Iserte, Llorens, Álvarez-Rodríguez, "An agent-based approach for the automatic generation of valid SysMLv2 Models in industrial contexts", DOI 10.1016/j.compind.2025.104350 | *Computers in Industry* 172:104350, 2025 | Yes (journal, CC BY-NC) | read full text (UC3M repository) |
| 2 | Stein et al., "Prompt-Strategy-Driven SysML-v2 Artefact Generation Using Large Language Models for Model-Based Systems Engineering", DOI 10.3390/ai7080274 | *AI* (MDPI) 7(8):274, 2026 | Yes (journal, CC BY) | read full text except appendix tables/figures |
| 3 | Wang, Ge, Liu, Cao, Chen, Hu, "Generating SysML Behavior Models via Large Language Models: an Empirical Study", DOI 10.1145/3755881.3755926 | Internetware 2025, pp. 366–377 | Yes (conference) | abstract + indexed snippets only |
| 4 | Aryashad & Jin, "A Validated Dataset and Benchmark for Coherent Multi-Diagram SysML Models", arXiv:2610.07356 | arXiv, 5 Oct 2026 | **No — preprint** | abstract only |
| 5 | Olivert-Iserte, "Trustworthy generation of SysML v2 models for physical systems: a multi-agent approach", DOI 10.1145/3837062.3839542 | ACM/IEEE MODELS 2026 | Yes (conference, doctoral-style problem statement) | abstract only |
| 6 | Bucchiarone, Di Rocco, Pierantonio, "How Well Do LLMs Suggest Metamodel Mappings? A Multi-Provider Benchmark on Hand-Written ATL Transformations", DOI 10.1145/3837062.3839372 | ACM/IEEE MODELS 2026 | Yes (conference) | abstract only |
| 7 | Li, Husung, Wang, "LLM-Assisted Semantic Alignment and Integration in Collaborative MBSE Using SysML v2", arXiv:2508.16181; DOI 10.1109/ISSE65546.2025.11369983 | IEEE ISSE 2025 | Yes (conference) | abstract read |
| 8 | Olausson, Inala, Wang, Gao, Solar-Lezama, "Is Self-Repair a Silver Bullet for Code Generation?", arXiv:2306.09896v5 | ICLR 2024 | Yes (conference) | read full text |
| 9 | Tam, Wu, Tsai, Lin, Lee, Chen, "Let Me Speak Freely? …", DOI 10.18653/v1/2024.emnlp-industry.91 | EMNLP 2024 Industry Track, pp. 1218–1236 | Yes (conference) | abstract read |
| 10 | DeHart, "Leveraging Large Language Models for Direct Interaction with SysML v2", DOI 10.1002/iis2.13262 | INCOSE Int. Symp. 34:2168–2185, 2024 | Yes (conference) | **[cited-in-anchor only]** |
| 11 | Rafique, Shah, Dalecke, Grimm, "Enhancing Model-Based Systems Engineering with Large Language Models" | INCOSE Int. Symp. 2025, pp. 1523–1543 | Yes (conference) | **[cited-in-anchor only]** |
| 12 | "Grammar-Aligned Decoding" (Park et al.) | NeurIPS 2024 | Yes (conference) | **[located only, unread]** |
| 13 | Metamorphic testing of bidirectional model transformations, DOI-linked ScienceDirect article S0950584918301538 | *Information and Software Technology* | Yes (journal) | **[located only, unread]** |
