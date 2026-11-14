
import json
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

METADATA_FILE = (
    BASE_DIR / "data" / "processed"
    / "GarisPanduanLI_chunks_metadata.json"
)

OUTPUT_DIR = (
    BASE_DIR / "data" / "pipeline_v1" / "document"
)

OUTPUT_FILE = OUTPUT_DIR / "prepared_chunks.json"

# Create output folder if it does not exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load the existing chunk metadata
with open(METADATA_FILE, "r", encoding="utf-8") as file:
    chunks = json.load(file)

# Check that the metadata contains chunks
if not isinstance(chunks, list) or not chunks:
    raise ValueError("The metadata file is empty or has an unexpected format.")

# Prepare reusable chunk records
prepared_chunks = []

for chunk in chunks:
    prepared_chunks.append({
        "chunk_id": chunk["chunk_id"],
        "source": chunk["source"],
        "pages": chunk.get("pages", []),
        "sections": chunk.get("sections", []),
        "language": chunk.get("language", "Malay"),
        "text": chunk["text"]
    })

# Save prepared output
with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(prepared_chunks, file, ensure_ascii=False, indent=4)

print("Prepared chunks successfully!")
print("Total chunks:", len(prepared_chunks))
print("Output file:", OUTPUT_FILE)
