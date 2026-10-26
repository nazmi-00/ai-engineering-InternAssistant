# Week 2: Evaluation Criteria

## 1. Evaluation Objective

The purpose of this evaluation is to determine whether the InternAssistant can provide correct, relevant, source-supported answers to students' internship-related questions. The evaluation will also assess how the system handles questions outside its scope and whether its response time is acceptable.

## 2. Evaluation Criteria

| ID | Related Requirement / Objective | Capability Bucket | Evaluation Method | Metric | Target Threshold | Expected User Outcome |
|---|---|---|---|---|---|---|
| EC1 | O3, NFR2 | Domain-specific capability | Test 30 internship-related questions and compare the answers with reference answers prepared from official internship documents. | Correct answer rate | At least 80% | Students receive accurate internship information. |
| EC2 | FR3, RAI3 | Instruction-following capability | Check whether answers based on retrieved documents include source references and whether the references support the answers. | Citation presence rate; citation-source match rate | 100% citation presence; at least 90% citation-source match | Students can verify answers using the original documents. |
| EC3 | FR4, RAI1 | Generation capability | Test 30 questions, including questions whose answers are unavailable in the knowledge base. Check whether the assistant gives supported answers or clearly states when information is missing. | Grounded answer rate | At least 90% | Students are less likely to receive unsupported internship information. |
| EC4 | RAI2 | Instruction-following capability | Test 20 questions unrelated to internship information and check whether the assistant declines or redirects them appropriately. | Refusal-and-redirect success rate | At least 90% | Students receive clear guidance when questions are outside the assistant's scope. |
| EC5 | NFR1 | Cost and latency | Measure end-to-end response time for 30 test questions. | 90th percentile response time (p90) | Less than 5 seconds | Students receive responses within an acceptable time. |

## 3. Test Data

The evaluation will use a set of test questions based on the available official university internship documents. Each test question will have a reference answer or an expected response behaviour.

The test set will include:
- Questions about internship requirements and eligibility information stated in the documents.
- Questions about application procedures and required documents.
- Questions about deadlines or guidelines when this information is available.
- Questions whose answers are missing from the knowledge base.
- Questions unrelated to internship information.

## 4. Evaluation Notes

The thresholds in this document are proposed evaluation targets, not measured results. Actual performance will be recorded after the system is implemented and tested.

The quality of the evaluation depends on the accuracy, relevance, and currency of the source documents and reference answers.

