# IndianMiningGPT Corpus Architecture

## Purpose

This document defines the architecture, standards, metadata structure, storage format, and quality requirements for the IndianMiningGPT training corpus.

The corpus is the most valuable asset of the project and serves as the foundation for tokenizer training, language model pretraining, domain adaptation, and evaluation.

---

# Corpus Objectives

The corpus should enable IndianMiningGPT to understand:

- Indian mining legislation
- Mine safety regulations
- Environmental compliance
- Mining operations
- Mineral processing
- Sustainability and ESG
- Natural resource governance

---

# Corpus Design Principles

1. Traceability
2. Reproducibility
3. Domain specificity
4. High signal-to-noise ratio
5. Regulatory accuracy

---

# Corpus Sources

The corpus consists of official Indian mining and natural resource documents.

## Primary Sources

### Mining Legislation

- Mines Act
- MMDR Act
- Coal Mines Regulations
- Metalliferous Mines Regulations

### DGMS

- DGMS Circulars
- DGMS Technical Guidelines
- DGMS Orders

### Environmental

- Environment Protection Act
- EIA Notifications
- Water Standards
- Air Standards

### Government Publications

- IBM Guidelines
- Ministry Notifications
- Technical Reports

---

# Document Taxonomy

Each document must belong to one category.

## Categories

- ACT
- RULE
- REGULATION
- DGMS_CIRCULAR
- DGMS_ORDER
- DGMS_GUIDELINE
- NOTIFICATION
- STANDARD
- TECHNICAL_GUIDE
- REPORT

---

# Metadata Schema

Each extracted chunk must contain metadata.

{
  "document_id": "",
  "title": "",
  "document_type": "",
  "source": "",
  "year": "",
  "page": "",
  "section": "",
  "text": ""
}

---

# Storage Format

Version 1 storage format:

JSONL

One record per chunk.

---

# Chunking Strategy

Target chunk size:

500-1000 words

Chunk overlap:

100 words

Chunking should preserve:

- Sections
- Clauses
- Rules
- Regulations

---

# Quality Rules

Remove:

- Headers
- Footers
- Page numbers
- Duplicate pages

Preserve:

- Section numbers
- Rule numbers
- Regulation references
- Tables when meaningful

---

# OCR Policy

If a PDF contains scanned pages:

- OCR required
- Manual verification required

---

# Deduplication Policy

Documents shall be checked for:

- Exact duplicates
- Near duplicates
- Amendment overlap

---

# Corpus Versioning

v1.0

Initial corpus based on 112 source documents.

---

# Success Criteria

The corpus is considered complete when:

- All source documents processed
- Metadata attached
- Quality checks passed
- JSONL export generated

