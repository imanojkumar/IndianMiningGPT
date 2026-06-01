# IndianMiningGPT Data Architecture

## Purpose

This document defines the directory structure, storage standards, and data lifecycle used by IndianMiningGPT.

The objective is to ensure reproducibility, traceability, and maintainability throughout the corpus engineering process.

---

# Repository Data Structure

data/
├── raw/
├── interim/
├── processed/
├── metadata/
├── tokenizer/
├── evaluation/
└── exports/

---

# raw/

Purpose:

Store original source documents exactly as obtained.

Characteristics:

- Read-only
- No modifications
- Original filenames preserved

Examples:

data/raw/
├── Mines_Act_1952.pdf
├── Coal_Mines_Regulations_2017.pdf
├── DGMS_Circular_01_2024.pdf

---

# interim/

Purpose:

Intermediate outputs generated during extraction.

Examples:

- OCR outputs
- Raw extracted text
- Temporary cleaning outputs

Characteristics:

- Regenerable
- Not considered final

---

# processed/

Purpose:

Final cleaned corpus ready for tokenizer training and model training.

Formats:

- JSONL
- Structured text

Examples:

data/processed/
├── corpus_v1.jsonl
├── corpus_v1_clean.jsonl

---

# metadata/

Purpose:

Document inventory and metadata management.

Examples:

data/metadata/
├── document_registry.csv
├── document_inventory.xlsx
├── corpus_statistics.json

---

# tokenizer/

Purpose:

Tokenizer training assets.

Examples:

data/tokenizer/
├── tokenizer.json
├── vocab.json
├── merges.txt

---

# evaluation/

Purpose:

Evaluation datasets and benchmark questions.

Examples:

data/evaluation/
├── mining_qa.jsonl
├── regulatory_qa.jsonl
├── safety_qa.jsonl

---

# exports/

Purpose:

Packaged releases of corpus assets.

Examples:

data/exports/
├── corpus_v1.zip
├── tokenizer_v1.zip

---

# Data Lifecycle

Raw PDF
    ↓
Extraction
    ↓
Interim Text
    ↓
Cleaning
    ↓
Metadata Enrichment
    ↓
Processed JSONL
    ↓
Tokenizer Training
    ↓
Model Training

---

# Versioning

Corpus versions:

v1.0
v1.1
v2.0

Tokenizer versions:

v1.0
v1.1
v2.0

Model versions:

v0.1.0
v0.2.0
v1.0.0

---

# Storage Principles

1. Never modify raw files.
2. All processed outputs must be reproducible.
3. Metadata must accompany every document.
4. Corpus versions must be traceable.
5. Training datasets must be reproducible.

