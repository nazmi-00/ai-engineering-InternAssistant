# InternAssistant — Week 2: Architecture Decisions

## 1. Architecture Overview

InternAssistant uses a document-grounded question-answering architecture to help students find information about university internship requirements, application procedures, required documents, and guidelines.

The system receives a student's question and checks whether it is within the internship information domain. If the question is relevant, the system retrieves supporting information from the internship knowledge base and provides the retrieved context to a Large Language Model (LLM).

The language model generates a natural-language answer based on the retrieved document passages. The system then returns the answer with source references when supporting information is available.

If sufficient information cannot be found, the system should communicate this limitation instead of guessing. Questions outside the internship information domain should be declined or redirected appropriately.

The architecture consists of the following main components:

1. Document Source
2. Document Processing
3. Internship Knowledge Base
4. User Interface
5. Query Validation and Scope Control
6. Information Retrieval
7. Prompt and Context Assembly
8. Language Model Service
9. Answer Generation and Source References
10. Missing-Information Handling

The architecture supports the following development objectives:

- **O1:** To identify publicly available university internship documents for use as the AI assistant's knowledge base.
- **O2:** To develop a retrieval-based AI assistant that answers internship-related questions using relevant document content and supporting sources.
- **O3:** To evaluate the system based on answer accuracy, groundedness, retrieval relevance, and response time.

## 2. Architecture Decision Records (ADRs)

| ADR ID | Decision | Reason | Trade-off / Limitation |
|---|---|---|---|
| ADR1 | Use official internship documents as the primary knowledge source. | This helps ensure that answers are based on relevant university information rather than unsupported general knowledge. | Answer quality depends on the accuracy, completeness, and currency of the documents. |
| ADR2 | Retrieve relevant document passages before generating an answer. | Providing relevant context helps the language model answer questions using available evidence. | Retrieval may miss relevant information or return passages that are not sufficiently useful. |
| ADR3 | Include source references and handle missing information explicitly. | Students can verify answers, and the system is less likely to present unsupported information as confirmed. | Source references must be checked for accuracy, and some questions may not be answerable using the available documents. |
| ADR4 | Apply internship-domain scope control. | This keeps the assistant focused on internship information and helps redirect unrelated questions. | Some relevant questions may be incorrectly classified as outside the supported domain. |

## 3. Evaluation Criteria

The evaluation criteria are designed to measure whether InternAssistant meets its functional, performance and responsible AI requirements.

Five evaluation criteria (EC1–EC5) are used to connect the project requirements with the architecture components and testing activities.

| Evaluation ID | Evaluation Criterion | Measurement Method | Target |
|---|---|---|---|
| EC1 | Answer Accuracy | Percentage of correct answers compared with manually prepared reference answers for answerable questions. | At least 80% |
| EC2 | Groundedness and Source Reference Accuracy | Check whether factual claims are supported by retrieved documents, whether source references are present, and whether they match the supporting source. | Groundedness at least 90%; citation presence 100%; source match at least 90% |
| EC3 | Retrieval Relevance | Precision@5, measuring the proportion of relevant document chunks among the top five retrieved chunks. | Average of at least 70% |
| EC4 | Scope Control and Missing-Information Handling | Percentage of unanswerable and out-of-scope questions that receive an appropriate limitation, refusal or redirection. | At least 90% |
| EC5 | Response Time | 90th percentile (P90) response time measured from question submission until the answer is completed. | Less than 5 seconds |

### 3.1 Evaluation Notes

**EC1 – Answer Accuracy**

The generated answer is compared with a manually prepared reference answer. Only questions that can be answered using the available knowledge base are included in the answer accuracy calculation.

**EC2 – Groundedness and Source Reference Accuracy**

Factual claims in generated answers are checked against the retrieved document content. Source references are also checked to ensure that they point to the correct document and supporting location.

**EC3 – Retrieval Relevance**

The five highest-ranked retrieved chunks are checked against manually labelled relevant chunks. This helps determine whether the retrieval component identifies useful information for each question.

**EC4 – Scope Control and Missing-Information Handling**

The system is tested using questions that cannot be answered from the knowledge base and questions unrelated to internship information. The system should communicate limitations or redirect users instead of guessing or providing unrelated answers.

**EC5 – Response Time**

The time taken to produce a completed response is recorded for each test question. P90 is used to understand the response time experienced by most requests while accounting for slower responses.

The targets are proposed evaluation thresholds. Actual performance will only be reported after the system has been implemented and tested.

## 4. Requirements Traceability Matrix

The following matrix connects the project objectives and system requirements with their evaluation criteria, architecture components and expected implementation evidence.

| Objective / Requirement | Evaluation Criteria | Architecture Component | Expected Evidence of Implementation |
|---|---|---|---|
| O1: Identify publicly available university internship documents for the knowledge base. | EC2, EC3 | Document Source, Document Processing and Internship Knowledge Base | Selected documents, processed text, prepared chunks and associated metadata. |
| O2: Develop a retrieval-based assistant that answers internship questions using relevant document content and supporting sources. | EC1, EC2, EC3 | User Interface, Information Retrieval, Prompt and Context Assembly, Language Model Service | Test questions receive answers based on relevant document passages with supporting references. |
| O3: Evaluate the system based on answer accuracy, groundedness, retrieval relevance and response time. | EC1, EC2, EC3, EC5 | Evaluation Process and all relevant system components | Evaluation dataset, test results, performance measurements and comparison against targets. |
| FR1: Answer questions about internship requirements, application procedures, required documents and guidelines. | EC1 | Query Validation, Information Retrieval and Language Model Service | Relevant internship questions receive appropriate answers. |
| FR2: Retrieve relevant information from available internship documents. | EC3 | Information Retrieval and Internship Knowledge Base | Relevant document chunks are retrieved for test questions. |
| FR3 / RAI3: Provide verifiable source references. | EC2 | Answer Generation and Source References | Answers contain references that can be checked against the original documents. |
| FR4 / RAI1: Handle missing information without guessing. | EC2, EC4 | Information Retrieval and Missing-Information Handling | Questions without sufficient supporting evidence receive an appropriate limitation message. |
| RAI2: Control questions outside the internship domain. | EC4 | Query Validation and Scope Control | Out-of-scope questions are declined or redirected appropriately. |
| NFR1: Respond within an acceptable time. | EC5 | Information Retrieval and Language Model Service | Response time is measured using the evaluation test questions. |

## 5. Evaluation Dataset and Testing Approach

The evaluation dataset will contain questions representing different internship information categories and system behaviour.

The initial proposed dataset consists of 30 questions:

| Question Category | Number of Questions | Purpose |
|---|---:|---|
| Internship requirements | 6 | Test questions about registration and requirements. |
| Internship duration | 5 | Test questions about internship duration and related conditions. |
| Application and placement | 6 | Test questions about application procedures and placement. |
| Student responsibilities | 5 | Test questions about student responsibilities during internship. |
| Assessment and reporting | 4 | Test questions about assessment and reporting procedures. |
| Unanswerable questions | 4 | Test whether the system identifies insufficient supporting information. |
| **Total** | **30** | |

The 26 answerable questions will be used for answer accuracy evaluation. The four unanswerable questions will be assessed separately for missing-information handling.

An additional set of 10 out-of-scope questions will be used to evaluate internship-domain scope control.

For EC4, the four unanswerable questions and ten out-of-scope questions will form a separate 14-question test set. The target is at least 90% appropriate handling, meaning at least 13 out of 14 questions must receive the expected limitation, refusal or redirection.

The evaluation process will include:

1. Prepare questions and manually verified reference answers.
2. Identify the relevant document sections and chunk IDs.
3. Label answerable, unanswerable and out-of-scope questions.
4. Submit questions to the implemented system.
5. Record retrieved chunks, generated answers, source references and response times.
6. Calculate the evaluation results for EC1–EC5.
7. Compare the results against the predefined targets.
8. Identify weaknesses and propose improvements.

The evaluation results will be documented after implementation and testing. The prepared data and data quality assessment alone will not be treated as evidence of retrieval or LLM answer-generation performance.

## 6. Design Considerations and Limitations

The initial architecture focuses on the main capabilities needed for InternAssistant rather than committing to a specific language model, database or retrieval technology before implementation.

The system depends on the availability and quality of official internship documents. If the documents are outdated, incomplete or unclear, the system may not provide a complete answer.

The initial dataset uses the UTM Industrial Training Guideline approved in 2012. Its current validity has not been verified. Therefore, the system should identify the document source and date and avoid presenting its content as confirmed current university policy.

Retrieval quality, source-reference accuracy, answer groundedness, response time and scope control must be evaluated during implementation.

The architecture may be refined after testing based on evaluation results and the technical constraints of the project.