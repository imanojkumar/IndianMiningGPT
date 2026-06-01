# IndianMiningGPT Inventory Workflow

## Purpose

This document defines the workflow used to discover, inventory, classify, and register source documents before corpus generation.

The inventory workflow is the first operational step of corpus engineering.

No document should enter the extraction pipeline until it has been inventoried and registered.

---

# Current Corpus Status

Current source location:

~/mining_gpt/data/raw_pdfs

Current document count:

112 PDFs

Status:

UNCLASSIFIED

---

# Inventory Objectives

The inventory process must:

1. Discover all PDF files.
2. Record file metadata.
3. Determine page counts.
4. Identify document titles.
5. Identify source authorities.
6. Detect duplicates.
7. Assign document identifiers.
8. Populate the document registry.

---

# Workflow

Raw PDF Collection
        ↓
File Discovery
        ↓
Basic Metadata Extraction
        ↓
Raw Inventory Generation
        ↓
Manual Review
        ↓
Document Classification
        ↓
Document Registry Population
        ↓
Corpus Processing

---

# Phase 1 — File Discovery

Input:

~/mining_gpt/data/raw_pdfs

Output:

raw_inventory.csv

Collected fields:

- file_name
- file_path
- file_size
- page_count

---

# Phase 2 — Metadata Discovery

Extract:

- title
- author
- creation date
- producer

when available.

Output:

enriched_inventory.csv

---

# Phase 3 — Document Classification

Assign:

- document_type
- source_authority
- commodity
- year

Examples:

ACT
RULE
REGULATION
DGMS_CIRCULAR
STANDARD

---

# Phase 4 — Registry Creation

Generate:

data/metadata/document_registry.csv

This becomes the authoritative source inventory.

---

# Duplicate Detection

Check:

- identical filenames
- identical page counts
- identical content hashes

Potential duplicates must be reviewed manually.

---

# Deliverables

data/metadata/

├── raw_inventory.csv
├── enriched_inventory.csv
├── document_registry.csv

---

# Success Criteria

The inventory phase is complete when:

- All PDFs discovered.
- Metadata extracted.
- Documents classified.
- Registry populated.
- Duplicates reviewed.

---

# Future Automation

Future versions may include:

- automatic title extraction
- authority detection
- duplicate clustering
- metadata enrichment

Current Version:

Manual review assisted by automated extraction.

