# InternAssistant — Week 2: Architecture Decisions

## 1. Architecture Overview

InternAssistant uses a document-grounded question-answering architecture to help students find information about university internship requirements, application procedures, required documents, and guidelines.

The system receives a student's question, checks whether it is within the internship information domain, retrieves relevant information from the knowledge base, and provides the retrieved context to a language model. The system then returns an answer with source references when supporting information is available. If sufficient information cannot be found, the system should communicate this limitation instead of guessing.

## 2. Architecture Decision Records (ADRs)

| ADR ID | Decision | Reason | Trade-off / Limitation |
|---|---|---|---|
| ADR1 | Use official internship documents as the primary knowledge source. | This helps ensure that answers are based on relevant university information rather than unsupported general knowledge. | Answer quality depends on the accuracy, completeness, and currency of the documents. |
| ADR2 | Retrieve relevant document passages before generating an answer. | Providing relevant context helps the language model answer questions using available evidence. | Retrieval may miss relevant information or return passages that are not sufficiently useful. |
| ADR3 | Include source references and handle missing information explicitly. | Students can verify answers, and the system is less likely to present unsupported information as confirmed. | Source references must be checked for accuracy, and some questions may not be answerable using the available documents. |
| ADR4 | Apply internship-domain scope control. | This keeps the assistant focused on internship information and helps redirect unrelated questions. | Some relevant questions may be incorrectly classified as outside the supported domain. |

## 3. Requirements Traceability Matrix

| Objective / Requirement | Evaluation Criteria | Architecture Component | Evidence of Implementation |
|---|---|---|---|
| O1: Collect and preprocess public internship documents. | EC1, EC2 | Document Processing and Internship Knowledge Base | Processed documents are stored and can be retrieved during testing. |
| O2: Develop an assistant that answers questions using retrieved information. | EC1, EC3 | Retrieval, Prompt and Context Assembly, Language Model Service | Test questions receive answers based on relevant document passages. |
| FR3 / RAI3: Provide verifiable source references. | EC2 | Answer Generation and Source References | Answers contain references that can be checked against the original documents. |
| FR4 / RAI1: Handle missing information without guessing. | EC3 | Retrieval and Missing-Information Handling | Questions without sufficient supporting evidence receive an appropriate limitation message. |
| RAI2: Control questions outside the internship domain. | EC4 | Query Validation and Scope Control | Out-of-scope questions are declined or redirected appropriately. |
| NFR1: Respond within an acceptable time. | EC5 | Retrieval and Language Model Service | Response time is measured using the evaluation test questions. |

## 4. Design Considerations and Limitations

The initial architecture focuses on the main capabilities needed for InternAssistant rather than committing to a specific language model, database, or retrieval technology before implementation.

The system depends on the availability and quality of official internship documents. If the documents are outdated, incomplete, or unclear, the system may not provide a complete answer. Retrieval quality, source-reference accuracy, response time, and scope control must therefore be evaluated during implementation.

The architecture may be refined after testing, based on the evaluation results and the technical constraints of the project.