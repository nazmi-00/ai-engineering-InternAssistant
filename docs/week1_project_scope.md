# Week 1 Project Scope — InternsAssistant

## Project Name
InternAssistant — AI-Powered Student Internship Information Assistant

## Domain
Artificial Intelligence Engineering / Machine Learning / Natural Language Processing (NLP)

## Problem Statement
University students often struggle to find internship information because requirements, application procedures, and guidelines are distributed across different university websites and documents. Searching through multiple sources manually can be time-consuming and confusing. This project aims to develop an AI-powered assistant that retrieves information from official internship documents and provides relevant answers with supporting sources.

## Evidence of the Problem
- **Evidence 1:** UTM Faculty of Computing provides industrial training resources and related documents through its faculty website, requiring students to locate the resources relevant to their questions.

  **Source:** UTM Faculty of Computing — Industrial Training Resources  
  https://fkt.utm.my/li/resources/

- **Evidence 2:** UTM Faculty of Electrical Engineering provides its own industrial training information and resources, illustrating that internship information can be organised separately across faculties.

  **Source:** UTM Faculty of Electrical Engineering  
  https://fke.utm.my/li/

## Initial Related Work / Existing Approaches

### 1. Retrieval-Augmented Generation (RAG)
**Source:** Lewis et al. (2020), *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*  
https://arxiv.org/abs/2005.11401

**Key limitation:** The quality of generated answers depends on retrieving relevant documents and generating responses that accurately reflect their content.

### 2. University Internship Websites
**Source:** UTM Faculty of Computing — Industrial Training Resources  
https://fkt.utm.my/li/resources/

**Key limitation:** Students may need to navigate multiple pages or documents to locate specific internship requirements and procedures.

### 3. General-Purpose AI Assistants
**Example:** Large language model-based conversational assistants.

**Source:** OpenAI, *Introducing ChatGPT*  
https://openai.com/index/chatgpt/

**Key limitation:** Without suitable document retrieval and source verification, an AI assistant may generate incorrect or unsupported information about internship requirements.

## Engineering Gap / Limitation
Existing approaches provide internship information but may require students to search through multiple resources manually. General-purpose AI assistants may also provide answers that are not supported by official university guidelines. This project aims to address these limitations by developing a document-grounded AI assistant that retrieves relevant information, provides answers with source references, and indicates when the available documents do not contain sufficient information.

## Initial Project Objectives
- **O1:** To collect and preprocess publicly available university internship documents for use as the AI assistant's knowledge base.
- **O2:** To develop a retrieval-based AI assistant that answers internship-related questions using relevant document content and supporting sources.
- **O3:** To evaluate the system based on answer accuracy, groundedness, retrieval relevance, and response time.

## Target Users
Undergraduate students who need information about internship eligibility, application procedures, required documents, deadlines, and university internship guidelines.

## Data Sources
- **Source 1:** UTM Faculty of Computing — Industrial Training Resources  
  URL: https://fkt.utm.my/li/resources/
- **Source 2:** UTM Faculty of Electrical Engineering — Industrial Training Information  
  URL: https://fke.utm.my/li/
- **Source 3:** UTM School of Undergraduate Studies — Industrial Training  
  URL: https://ugs.utm.my/industrial-training-li/



## Weekly Progress

| Week | Focus                       | Deliverable              | Status      |
|------|-----------------------------|--------------------------|-------------|
| W1   | Project framing and scoping | README and project scope | In progress |