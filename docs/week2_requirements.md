# Topic 2 — Project Framing and Requirements

## Section 0: Project Framing and Application Scope

### 1. Project Name
InternAssistant — AI-Powered Student Internship Information Assistant

### 2. Problem Statement
University students may find it difficult and time-consuming to locate internship requirements, application procedures, required documents, and guidelines because the information is distributed across different university websites and documents. Students may need to search through multiple sources to find answers to specific questions. This project proposes an AI-powered assistant that helps students retrieve relevant internship information from official university documents and provides answers with supporting source references.

### 3. Problem Evidence
- **Evidence 1:** UTM Faculty of Computing provides industrial training resources through its faculty website. Students need to identify the relevant resources and documents for their internship-related questions.
  Source: https://fkt.utm.my/li/resources/

- **Evidence 2:** UTM Faculty of Electrical Engineering provides industrial training information through its own faculty website. This illustrates that internship information may be organised separately across university faculties.
  Source: https://fke.utm.my/li/

### 4. Existing Approaches

**Approach 1: University Internship Websites**

University websites provide internship information, guidelines, and related documents. However, students may need to navigate different pages and read documents manually to locate specific answers.

Source: https://fkt.utm.my/li/resources/

**Approach 2: Retrieval-Augmented Generation (RAG)**

RAG combines information retrieval with language generation. It allows an AI application to retrieve relevant information from a knowledge source and use that information to generate answers.

Source: Lewis et al. (2020), Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. https://arxiv.org/abs/2005.11401

Limitation: Answer quality depends on retrieving relevant information and generating answers that remain consistent with the retrieved content.

**Approach 3: General-Purpose AI Assistants**

General-purpose AI assistants can answer questions using natural language.

Source: https://openai.com/index/chatgpt/

Limitation: Without appropriate document retrieval and source verification, responses about specific university internship policies may contain unsupported or outdated information.

### 5. Project / Engineering Gap
Existing approaches provide access to internship information, but students may still need to search through multiple websites and documents manually. General-purpose AI assistants may also provide answers without sufficient evidence from official university sources. This project aims to address these practical limitations by developing a document-grounded AI assistant that provides relevant answers with source references and indicates when the available documents do not contain sufficient information.

### 6. Project Objectives

- **O1:** To collect and preprocess publicly available university internship documents for the system's knowledge base.
- **O2:** To develop an AI-powered assistant that answers internship-related questions using relevant information retrieved from the knowledge base.
- **O3:** To evaluate the assistant based on answer correctness, source support, handling of out-of-scope questions, and response time.

### 7. Intended Users
Undergraduate students who need information about internship eligibility, application procedures, required documents, deadlines, and university internship guidelines.

### 8. Supported Tasks
- Answer questions about internship requirements found in the available documents.
- Explain internship application procedures and guidelines.
- Identify relevant information about required documents and deadlines when stated in the sources.
- Provide source references so users can verify the information.
- Indicate when the available documents do not contain sufficient information to answer a question.

### 9. Information / Knowledge Domain
The system will focus on publicly available university internship and industrial training documents, including official guidelines, procedures, requirements, and related information.

### 10. Operating Context
The system is intended to operate as a web-based AI assistant. Students will submit questions through the application and receive answers based on the available internship documents.

### 11. Important Constraints
- The knowledge base will initially use publicly available documents.
- The accuracy of answers depends on the quality, relevance, and currency of the available documents.
- The project will be developed within the time and computing resources available for the course.
- The initial version will focus on a limited internship information domain rather than all university services.
- Important requirements and deadlines should be verified against the latest official university information.

### 12. Explicit Out-of-Scope Tasks
- Making official decisions about student internship eligibility or approval.
- Submitting internship applications on behalf of students.
- Providing information that is not supported by the available knowledge sources as if it were confirmed.
- Answering unrelated questions outside the internship information domain.
- Replacing official university announcements or direct confirmation from internship coordinators.

### 13. Evaluation Focus
The evaluation will determine whether the assistant can provide correct and relevant answers grounded in official internship documents, provide appropriate source references, handle questions outside its intended scope, and respond within an acceptable amount of time.

## Section 1: Functional Requirements (FR)

| ID | Requirement — The system SHALL | Scope Boundary — The system SHALL NOT |
|---|---|---|
| FR1 | Answer student questions about internship requirements, application procedures, required documents, and guidelines using information from the available knowledge base. | Provide internship information as confirmed if it is not supported by the available documents. |
| FR2 | Retrieve relevant information from the available university internship documents to support answers to student questions. | Present unrelated documents as evidence for an answer. |
| FR3 | Provide source references for answers based on retrieved university documents so students can verify the information. | Invent document titles, source references, or supporting evidence. |
| FR4 | Indicate when the available documents do not contain sufficient information to answer a question and direct students to verify the information with the relevant university office when appropriate. | Guess missing internship requirements, deadlines, or procedures. |
| FR5 | Present answers in clear, understandable language suitable for undergraduate students. | Make official decisions about internship eligibility, approval, or application outcomes. |

## Section 2: Non-Functional Requirements (NFR)

| ID | Quality Attribute | Requirement | Measurement Method | Metric | Threshold |
|---|---|---|---|---|---|
| NFR1 | Performance | The system shall respond to student questions within an acceptable time. | Measure the end-to-end response time for 30 test questions. | 90th percentile response time (p90) | Less than 5 seconds |
| NFR2 | Correctness | The system shall provide answers that are factually consistent with the available official internship documents. | Evaluate 30 test questions against a reference answer based on the source documents. | Correct answer rate | At least 80% |
| NFR3 | Cost | The system shall keep AI service usage within the project budget. | Record the AI service cost for 100 test queries, if a paid service is used. | Cost per 100 queries | Within the available project budget |
| NFR4 | Maintainability | The system shall allow an updated internship document to be added to the knowledge base without rebuilding unrelated application components. | Time how long it takes to add one updated document and make its content available for retrieval. | Document update time | Less than 10 minutes |

## Section 3: Responsible AI Requirements (RAI)

| ID | Responsible AI Risk | Requirement | Measurement Method | Metric | Threshold |
|---|---|---|---|---|---|
| RAI1 | Hallucination / Grounding | The system shall provide answers supported by retrieved official internship documents and state when sufficient evidence is unavailable. | Test 30 questions, including questions whose answers are missing from the knowledge base, and compare responses with the source documents. | Grounded answer rate | At least 90% |
| RAI2 | Scope Control | The system shall decline questions outside the internship information domain and redirect users appropriately. | Test 20 out-of-scope questions and check whether the system refuses or redirects appropriately. | Refusal-and-redirect success rate | At least 90% |
| RAI3 | Transparency / Source Citation | The system shall provide a verifiable source reference for every answer based on retrieved documents. | Check document-grounded answers for citation presence and verify that each cited source supports the answer. | Citation presence rate; citation-source match rate | 100% citation presence; at least 90% citation-source match |

