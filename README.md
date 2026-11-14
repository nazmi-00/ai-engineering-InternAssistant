# ai-engineering-InternAssistant
# AI-Powered Student Internship Information Assistant

> An AI assistant that helps university students find internship requirements, application procedures, and guidelines using official university documents.

## Problem Statement
University students often struggle to find internship information because requirements, application procedures, and guidelines are spread across different websites and documents. Searching through these resources manually can be time-consuming. AI engineering can help by developing a document-grounded assistant that retrieves relevant information and provides answers with supporting sources.

## Evidence of the Problem
- UTM Faculty of Computing provides industrial training resources, including internship-related documents and forms, through its faculty website. Source: [UTM Faculty of Computing — Industrial Training Resources](https://fkt.utm.my/li/resources/)
- UTM Faculty of Electrical Engineering provides industrial training information through a separate faculty website, illustrating that students may need to consult faculty-specific resources. Source: [UTM Faculty of Electrical Engineering — Industrial Training](https://fke.utm.my/li/)

## Initial Related Work / Existing Approaches
- **Retrieval-Augmented Generation (RAG):** Lewis et al. (2020), *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. Source: https://arxiv.org/abs/2005.11401. Key limitation: Answer quality depends on retrieval accuracy, document quality, and the language model's ability to use retrieved information correctly.
- **University internship websites:** UTM Faculty of Computing Industrial Training Resources. Source: https://fkt.utm.my/li/resources/. Key limitation: Students may need to navigate webpages and documents manually to find specific answers.
- **Static internship guidelines and PDF documents:** University-provided internship guidelines and forms. Example source: https://fke.utm.my/li/. Key limitation: Students must identify the relevant document and search for the required information themselves.

## Project Objectives
- O1: To collect and preprocess official university internship documents for use as the AI assistant's knowledge base.
- O2: To develop a retrieval-based AI assistant that answers internship-related questions using relevant documents and supporting sources.
- O3: To evaluate the assistant based on answer accuracy, groundedness, source relevance, and response time.

## Target Users
Undergraduate students who need information about internship eligibility, application procedures, required documents, deadlines, and university internship guidelines.

## Data Sources
- UTM Faculty of Computing — Industrial Training Resources: https://fkt.utm.my/li/resources/
- UTM Faculty of Electrical Engineering — Industrial Training Information: https://fke.utm.my/li/
- UTM School of Undergraduate Studies — Industrial Training: https://ugs.utm.my/industrial-training-li/

## Weekly Progress
| Week | Focus                      | Deliverable    | Status |
|------|----------------------------|----------------|--------|
| W1   | System map + project scope | README + docs  | ✅    |

## Week 3 – Data Preparation Pipeline

### Project Overview
This week, the InternAssistant project implemented a document-processing pipeline using the UTM Industrial Training Guidelines PDF.

### Selected Data Pathway
- Pathway: PDF document processing
- Source: `GarisPanduanLI.pdf`
- Document language: Malay
- Total pages: 16

### Pipeline Process
1. Extract text from the PDF using PyMuPDF.
2. Clean the extracted text.
3. Split the text into chunks using RecursiveCharacterTextSplitter.
4. Generate metadata for each chunk.
5. Record data lineage and processing information.
6. Prepare structured chunks for the next pipeline stage.

### Chunking Configuration
- Chunking method: RecursiveCharacterTextSplitter
- Chunk size: 1200 characters
- Chunk overlap: 100 characters
- Total chunks generated: 29

### Week 3 Deliverables
- Notebook: `notebooks/week3_pipeline.ipynb`
- Data inventory: `docs/week3_data_inventory.md`
- Pipeline diagram: `docs/week3_pipeline_diagram.png`
- Pipeline decisions: `docs/week3_pipeline_decisions.md`
- Part B lineage manifest: `data/week3_manifest.json`
- Processed data: `data/processed/`
- Part C prepared chunks: `data/pipeline_v1/document/prepared_chunks.json`
- Part C pipeline manifest: `data/pipeline_v1/document/pipeline_manifest.json`

### Execution Scripts
Run the following commands from the project root:

```bash
python src/prepare_chunks.py
python src/create_pipeline_manifest.py
```

### Current Progress
The Week 3 document-processing pipeline has been executed successfully, producing 29 prepared chunks with metadata and recorded lineage information.

