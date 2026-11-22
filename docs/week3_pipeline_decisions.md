# Week 3 – Pipeline Decisions

## 1. Overview

This document describes the technical decisions made during the development of the InternAssistant V1 data preparation pipeline.

The selected pathway focuses on processing PDF documents into structured text chunks that can be used for a future document retrieval system.

## 2. Source Document Selection

**Selected source:** `GarisPanduanLI.pdf`

The UTM Industrial Training Guidelines PDF was selected because it contains relevant information about internship requirements, procedures, objectives and guidelines.

## 3. PDF Extraction

**Selected tool:** PyMuPDF

**Reason for selection:**
- Supports PDF text extraction using Python.
- Extracts text from individual pages.
- Allows page-level processing and inspection.
- Suitable for documents containing selectable text.

## 4. Text Cleaning

The extracted text was cleaned to improve consistency before chunking.

The cleaning process included:
- Removing null characters.
- Normalizing spaces and tabs.
- Reducing excessive blank lines.
- Preserving page markers and document structure.

## 5. Text Chunking

**Selected method:** RecursiveCharacterTextSplitter

**Selected configuration:**

| Parameter | Value |
|---|---:|
| Chunk size | 1200 characters |
| Chunk overlap | 100 characters |

**Reason for selection:**

pipeline V1 was selected to divide the document into manageable text sections while maintaining some context between consecutive chunks.

The 100-character overlap helps reduce the loss of context when information is split between chunks.

## 6. Metadata Generation

Metadata was generated for each chunk to support document traceability.

The metadata includes:
- Chunk ID.
- Source filename.
- Page information.
- Section information.
- Language.
- Chunking configuration.
- Actual character count.
- Chunk text.

A total of 29 chunks were generated.

## 7. Data Lineage

A lineage JSON file was created to record the processing history.

It includes:
- Source document SHA-256 hash.
- Processing steps.
- Chunking configuration.
- Total number of chunks.
- Output metadata filename.
- Generation timestamp.

## 8. Engineering Trade-offs and Limitations

The selected chunking method provides a simple and practical approach for preparing PDF documents.

However, some limitations remain:
- Some sections may be split across chunks.
- Overlapping chunks may contain repeated information.
- Page and section metadata require careful validation.
- The current pipeline does not yet generate embeddings or perform semantic retrieval.

## 9. Conclusion

The selected pipeline provides an initial and repeatable approach for preparing internship guideline documents for InternAssistant.

The prepared chunks and metadata will support the next stage of development, which focuses on document retrieval and semantic search.