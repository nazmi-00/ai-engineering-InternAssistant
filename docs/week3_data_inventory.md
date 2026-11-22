# Week 3 – Data Inventory

## 1. Project Information

- **Project Name:** InternAssistant
- **Pipeline Version:** V1
- **Data Pathway:** Document / PDF Processing

## 2. Source Data

| Attribute | Description |
|---|---|
| Source File | GarisPanduanLI.pdf |
| File Format | PDF |
| Document Type | UTM Industrial Training Guidelines |
| Language | Malay |
| Number of Pages | 16 |
| Storage Location | data/raw/GarisPanduanLI.pdf |

## 3. Data Inspection

The source document was inspected and processed using PyMuPDF. Text was successfully extracted from all 16 pages. The extracted content was checked to confirm that it contained readable text.

## 4. Data Preparation

The following preparation steps were performed:

1. PDF text extraction using PyMuPDF.
2. Text cleaning and whitespace normalization.
3. Text chunking using RecursiveCharacterTextSplitter.
4. Metadata generation for document chunks.
5. Data lineage recording.

## 5. Prepared Outputs

| Output File | Description |
|---|---|
| GarisPanduanLI_extracted.txt | Extracted PDF text |
| GarisPanduanLI_cleaned.txt | Cleaned text |
| GarisPanduanLI_chunks.txt | Text chunks |
| GarisPanduanLI_chunks_metadata.json | Chunk metadata |

## 6. Initial Data Quality Observations

- All 16 PDF pages contained extractable text.
- The document is primarily written in Malay.
- Some chunks may contain overlapping content.
- Page and section metadata should be checked to maintain accurate source traceability.

## 7. Intended Use

The prepared document chunks will be used as the knowledge source for InternAssistant's future document retrieval and question-answering functionality.