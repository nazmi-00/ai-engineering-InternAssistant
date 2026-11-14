
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Input and output paths
DATA_DIR = BASE_DIR / "data"
PROCESSED_DIR = DATA_DIR / "processed"
PIPELINE_DIR = DATA_DIR / "pipeline_v1" / "document"

METADATA_FILE = PROCESSED_DIR / "GarisPanduanLI_chunks_metadata.json"
PREPARED_FILE = PIPELINE_DIR / "prepared_chunks.json"
OUTPUT_FILE = PIPELINE_DIR / "pipeline_manifest.json"
SCRIPT_FILE = BASE_DIR / "src" / "prepare_chunks.py"

SOURCE_FILE = DATA_DIR / "raw" / "GarisPanduanLI.pdf"


def sha256_file(file_path):
    if not file_path.exists():
        return None

    digest = hashlib.sha256()

    with open(file_path, "rb") as file:
        for block in iter(lambda: file.read(4096), b""):
            digest.update(block)

    return digest.hexdigest()


# Check required files
for path in [METADATA_FILE, PREPARED_FILE, SCRIPT_FILE]:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")

# Read prepared chunks
with open(PREPARED_FILE, "r", encoding="utf-8") as file:
    prepared_chunks = json.load(file)

if not isinstance(prepared_chunks, list) or not prepared_chunks:
    raise ValueError("Prepared chunks are empty or invalid.")

# Create execution manifest
manifest = {
    "project": "InternAssistant",
    "pipeline_name": "PDF Document Processing Pipeline",
    "pipeline_version": "V1",
    "selected_pathway": "document",
    "execution_status": "completed",
    "execution_timestamp_utc": datetime.now(
        timezone.utc
    ).isoformat(),

    "source": {
        "filename": "GarisPanduanLI.pdf",
        "path": "data/raw/GarisPanduanLI.pdf",
        "sha256": sha256_file(SOURCE_FILE)
    },

    "processing": {
        "extraction": "PyMuPDF",
        "cleaning": [
            "Remove null characters",
            "Normalize spaces and tabs",
            "Reduce excessive blank lines"
        ],
        "chunking_method": "RecursiveCharacterTextSplitter",
        "chunk_size": 1200,
        "chunk_overlap": 100
    },

    "execution": {
        "script": "src/prepare_chunks.py",
        "input": "data/processed/GarisPanduanLI_chunks_metadata.json",
        "input_sha256": sha256_file(METADATA_FILE),
        "total_chunks": len(prepared_chunks)
    },

    "outputs": [
        {
            "filename": "prepared_chunks.json",
            "path": "data/pipeline_v1/document/prepared_chunks.json",
            "sha256": sha256_file(PREPARED_FILE),
            "total_records": len(prepared_chunks)
        }
    ]
}

# Save manifest
with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(manifest, file, ensure_ascii=False, indent=4)

print("Pipeline manifest created successfully!")
print("Execution status:", manifest["execution_status"])
print("Total chunks:", manifest["execution"]["total_chunks"])
print("Output:", OUTPUT_FILE)
