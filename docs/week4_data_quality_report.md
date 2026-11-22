# Week 4 Data Quality and Responsible Data Practices Report

**Project:** InternAssistant  
**Dataset:** UTM *Garis Panduan Latihan Industri* (`GarisPanduanLI.pdf`)  
**Audited output:** `data/pipeline_v1/document/prepared_chunks.json`  
**Matching manifest:** `data/pipeline_v1/document/pipeline_manifest.json`  
**Assessment scope:** Existing document-processing pipeline and prepared chunks only  
**Decision:** **GO WITH CONDITIONS**

---

## 1. Project and Data Overview

InternAssistant is a university internship question-answering knowledge-base assistant. It is intended to help undergraduate students find information about internship requirements, application procedures, required documents and guidelines. The system should retrieve relevant information from available university documents, provide verifiable source references, use clear language, and state when information is insufficient instead of guessing. It must not make official eligibility or approval decisions.

This audit focuses on two relevant Topic 2 requirements:

- **FR1 — Answer student questions:** Answer student questions about internship requirements, application procedures, required documents and guidelines using information from the available knowledge base.
- **RAI3 — Transparency/source citation:** Provide source references so students can verify information; do not invent references or supporting evidence. The project target is 100% citation presence and at least 90% citation-source match during later system evaluation.

The selected data pathway is document processing. The source is the UTM internship guideline PDF, `data/raw/GarisPanduanLI.pdf`, obtained from an official UTM website or portal. The audited prepared output is `data/pipeline_v1/document/prepared_chunks.json`, with the matching processing record at `data/pipeline_v1/document/pipeline_manifest.json`.

The manifest records the source filename and path, source SHA-256 hash, extraction method (PyMuPDF), cleaning operations, chunking method (`RecursiveCharacterTextSplitter`), chunk size (1,200 characters), overlap (100 characters), execution script, input hash, and output hash. The pipeline produced 29 prepared chunks. The source PDF, extracted text, cleaned text, prepared chunks and manifest are tracked in Git. The working tree was clean when the tracking check was performed.

The assessment population is all 29 records in `prepared_chunks.json`; the checks described below examined all 29 records where applicable. This is a data-preparation audit, not a retrieval/model evaluation. No embeddings, vector database, retrieval pipeline or model calls were performed for this lab.

## 2. Five-Dimension Quality Scorecard

| Dimension | Evidence and finding | Decision |
|---|---|---|
| Completeness | All 29 chunks contain text and page metadata. Section metadata is present in 17/29 chunks and missing in 12/29 (41.38%). | Warning |
| Consistency | Source and language metadata were consistent in all 29 chunks. However, section metadata is not consistently populated in 12/29 chunks. | Warning |
| Accuracy | Explicit UTF-8 checks on extracted text, cleaned text and prepared chunks found no suspicious encoding patterns. A complete line-by-line comparison of all extracted content against the PDF was not performed. | Review |
| Timeliness | The document records UTM Senate approval on 15 February 2012. Its current validity or replacement status has not been verified. | Review |
| Uniqueness | 29/29 chunk IDs were unique and zero exact duplicate text groups were detected after trimming whitespace. Near-duplicates were not assessed. | Pass* |

\*The Pass decision applies only to the exact duplicate checks performed; it does not establish that there are no near-duplicates or semantically overlapping chunks.

The assessment found satisfactory results for basic text extraction and uniqueness checks. However, missing section context may reduce the precision of source references, while the document's age creates uncertainty about whether its guidance remains current. Accuracy is therefore marked Review because encoding checks passed but a full content-to-source verification was outside the completed checks.

## 3. Validation Findings

Two measurable validation rules were defined and applied to all 29 prepared chunks.

### Rule 1 — Section context completeness

- **Purpose:** Ensure every chunk has a section identifier or an explicit context label, such as “Continuation of Section 10.3” or “Appendix A”.
- **Requirement link:** FR1 and RAI3. Clear section context can help the assistant retrieve relevant guideline content and provide traceable source references.
- **Condition and target:** 100% of chunks (29/29) should contain section metadata or an equivalent explicit context label.
- **Evidence source:** `data/pipeline_v1/document/prepared_chunks.json`, particularly the `sections` field.
- **Failure action:** Flag chunks without context and add or verify section/continuation metadata before relying on them for precise citations.

**Applied result:** 17/29 chunks had section metadata (58.62%), while 12/29 (41.38%) did not. The affected chunk IDs were `GLI_004`, `GLI_006`, `GLI_010`, `GLI_014`, `GLI_015`, `GLI_019`, `GLI_022`, `GLI_024`, `GLI_026`, `GLI_027`, `GLI_028` and `GLI_029`. Manual inspection indicated that these chunks mostly contain continuation text, transitions between sections, or Appendix A, rather than clear evidence of missing text. The rule did not meet its 100% target. The missing context may make it harder to identify the correct section when presenting a source reference.

### Rule 2 — Chunk uniqueness

- **Purpose:** Prevent identical chunks or repeated identifiers from unnecessarily duplicating content in the knowledge base.
- **Requirement link:** FR1, because duplicate records may cause repeated or less useful retrieved evidence.
- **Condition and target:** Zero duplicate `chunk_id` values and zero exact duplicate text groups after trimming surrounding whitespace.
- **Evidence source:** `data/pipeline_v1/document/prepared_chunks.json`.
- **Failure action:** Investigate duplicate records and identifiers before deciding whether to correct or remove them.

**Applied result:** All 29 chunk IDs were unique, with zero duplicate IDs and zero exact duplicate text groups. The rule passed. This check does not detect near-duplicates or expected overlap introduced by the 100-character chunk overlap.

Overall, the uniqueness rule passed, while section-context completeness did not meet its target. The section metadata issue should be addressed before relying on these chunks for highly precise source citations.

## 4. Duplicate, Anomaly and Coverage Findings

The prepared dataset contains 29 chunks from one 16-page Malay-language UTM internship guideline. The chunks cover topics including internship registration requirements, duration, placement, student responsibilities, assessment and reporting, leave, plagiarism, and disciplinary procedures. The dataset also contains an Appendix A flowchart relating to an overseas student application process.

The exact duplicate checks found no repeated chunk IDs and no exact duplicate text groups. Chunk lengths ranged from 109 characters (`GLI_024`) to 1,188 characters (`GLI_009`), remaining below the configured chunk size of 1,200 characters. Shorter chunks are not automatically errors because the splitter may preserve paragraph or section boundaries. The configured 100-character overlap may produce some related text between neighbouring chunks and was not treated as an exact-duplicate defect.

A metadata anomaly was identified: 12 chunks have no populated `sections` field. Manual inspection suggests that these are generally continuation or appendix chunks. This is a context/metadata issue and does not, by itself, demonstrate that source content was lost.

Coverage is limited because the current dataset contains only one guideline. It may not include every faculty-specific procedure, current form, or recent policy update that students may ask about. This limitation should be considered when assessing whether the knowledge base can answer the full range of student questions.

## 5. Bias Assessment

This assessment considers potential dataset coverage and historical-data risks. It does not claim to measure model fairness or prove statistical bias.

**Case 1 — Topic and source coverage.** The knowledge base currently contains one UTM internship guideline. Faculty-specific procedures, updated forms and more recent policy changes have not been verified in the audited dataset. This creates a possible coverage bias: topics represented in the selected guideline may be easier for the future assistant to answer than topics absent from it. The chain of risk is: one-source dataset → missing or underrepresented faculty/current procedures → potentially incomplete or unsuitable answers for some student questions. The control is to add verified current official UTM and faculty documents, record their source and version details, and require the assistant to state when evidence is insufficient and refer students to the relevant university office.

**Case 2 — Historical information.** The guideline records approval by the UTM Senate on 15 February 2012, but its current validity has not been confirmed. The chain of risk is: older source document → possible changes to requirements or procedures not represented → risk of outdated answers. The control is to verify the document against the latest official UTM source, record publication/approval and access dates, and replace or supplement obsolete material.

These are plausible data coverage and historical-source risks. They are not evidence that the model has discriminatory behaviour; no model fairness testing was performed.

## 6. Privacy, Rights and Governance

The dataset was obtained from an official UTM website or portal. The original PDF, extracted text, cleaned text, prepared chunks and pipeline manifest are tracked in the project repository. The manifest records the source filename, source SHA-256 hash, processing method and output information, supporting provenance and traceability.

The document's current validity has not been verified. It records UTM Senate approval on 15 February 2012 and should be checked against the latest official internship guideline before being used to provide current information. Although the document came from an official UTM source, permission to redistribute it publicly through GitHub has not been established. Public availability at the source should not automatically be treated as permission for republication.

The extracted text contains a reference to a student information form with fields for name, IC number, passport number, permanent address and study address. The inspected matches appear to describe required form fields rather than actual student records. This text search does not prove that every page or image in the PDF is free of personal information. The project should avoid adding actual student records or unnecessary personal information to the knowledge base. Only information needed to answer internship questions should be processed, and access to project data should be controlled.

Recommended governance safeguards are:
1. Record the official source URL, access date, document title/version, approval or publication date, and SHA-256 hash.
2. Verify redistribution permission before placing the original PDF or extracted content in a public repository.
3. Do not include actual student personal records in the knowledge base; apply data minimisation and access controls.
4. Periodically check the official UTM source for updated guidelines and replace obsolete versions while retaining clear version history.
5. Keep source/page/section metadata with prepared chunks so answers can be traced to the supporting document.

## 7. Mitigation and Impact on Requirements

| Finding | Potential impact on project requirements | Mitigation |
|---|---|---|
| Missing section metadata in 12/29 chunks | May reduce source-reference precision and make it harder to verify evidence (FR1, RAI3). | Add section identifiers or explicit continuation/appendix labels; recheck all 29 chunks. |
| Current validity of 2012 guideline unverified | May cause incomplete or outdated answers to current internship questions (FR1). | Verify against the latest official UTM guideline and record version/date. |
| One-document coverage | Some faculty-specific or updated procedures may be absent (FR1). | Add verified official university/faculty documents and track their provenance. |
| Redistribution permission unverified | Public repository publication may create a rights/compliance issue. | Confirm permission or restrict/remove the source document and derived content from public distribution as appropriate. |
| Personal-information form fields referenced | Future ingestion of completed forms could expose unnecessary personal information. | Use only official blank guidance documents; exclude actual student records and apply data minimisation/access controls. |

Until the relevant checks are completed, the assistant should not infer missing requirements or present uncertain information as authoritative. When the knowledge base does not contain sufficient verified evidence, it should clearly state that limitation and direct the student to the relevant UTM office. Later system evaluation should separately test answer correctness, retrieval relevance and source matching; this data-quality audit does not establish those performance results.

## 8. Quality-Gate Decision

**Decision: GO WITH CONDITIONS**

The prepared dataset is suitable for continued development and controlled testing of InternAssistant, subject to the improvements and investigations identified in this assessment. This decision applies only to the audited dataset and its current preparation pipeline. It does not mean that the dataset is fully ready to provide authoritative answers to students.

Evidence supporting continued development includes: (1) all 29 prepared chunks contain text and page metadata; (2) no duplicate chunk IDs or exact duplicate text groups were detected; (3) explicit UTF-8 checks found no confirmed encoding problems; and (4) the source and processing artifacts are Git-tracked, with a source hash and processing details recorded in the manifest.

The main unresolved issues are: (1) 12/29 chunks (41.38%) have missing section metadata; (2) the 2012 guideline's current validity has not been verified; (3) permission for public redistribution has not been established; and (4) the single-document dataset may not cover all current faculty-specific procedures.

The two highest-priority actions are to improve the missing section metadata and verify the guideline against the latest official UTM source. Redistribution permission should be checked before public publication. Additional verified university and faculty documents should be included to improve coverage.

Residual risks include outdated information, incomplete topic coverage, and possible retrieval/citation errors caused by missing section context. The assistant should respond cautiously when evidence is insufficient and refer students to the relevant university office rather than guessing.

A further quality review is required when an updated UTM guideline becomes available, when new faculty-specific documents are added, or after section metadata is corrected. The decision should be reconsidered before operational use and after material changes to the source dataset or preparation pipeline.

---

**Audit limitation:** This report evaluates the existing document-processing output and selected metadata/quality checks. It does not evaluate live retrieval, embeddings, vector databases, model responses, answer correctness, or model fairness.
