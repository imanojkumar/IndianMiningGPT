# IndianMiningGPT Metadata Schema

## Purpose

This document defines the official metadata schema used throughout the IndianMiningGPT corpus.

Every extracted text chunk must conform to this schema.

The schema enables:

- Traceability
- Reproducibility
- Corpus analytics
- Evaluation
- Future Retrieval-Augmented Generation (RAG)
- Regulatory source attribution

---

# Design Principles

1. Every chunk must be traceable to its source.
2. Metadata should be machine-readable.
3. Metadata should support future corpus expansion.
4. Metadata should support retrieval systems.
5. Metadata should remain stable across versions.

---

# Canonical Schema

{
  "document_id": "",
  "chunk_id": "",
  "title": "",
  "document_type": "",
  "source_authority": "",
  "year": "",
  "publication_date": "",
  "language": "",
  "state": "",
  "commodity": "",
  "page_start": "",
  "page_end": "",
  "section": "",
  "subsection": "",
  "chunk_number": "",
  "total_chunks": "",
  "text": ""
}

---

# Field Definitions

## document_id

Unique document identifier.

Examples:

CMR2017
MMDR1957
MA1952

Required: YES

---

## chunk_id

Unique chunk identifier.

Format:

DOCUMENT_PAGE_CHUNK

Examples:

CMR2017_042_001
CMR2017_042_002
MMDR1957_011_001

Required: YES

---

## title

Official document title.

Example:

Coal Mines Regulations 2017

Required: YES

---

## document_type

Allowed values:

ACT
RULE
REGULATION
DGMS_CIRCULAR
DGMS_ORDER
DGMS_GUIDELINE
NOTIFICATION
STANDARD
TECHNICAL_GUIDE
REPORT

Required: YES

---

## source_authority

Publishing authority.

Examples:

DGMS
IBM
MoC
MoEFCC
CPCB
SPCB

Required: YES

---

## year

Publication year.

Example:

2017

Required: YES

---

## publication_date

ISO format preferred.

Example:

2017-12-27

Required: NO

---

## language

Default:

English

Future support:

Hindi

Required: YES

---

## state

Applicable state if relevant.

Examples:

Jharkhand
Odisha
Chhattisgarh

Default:

National

Required: YES

---

## commodity

Primary mineral or resource.

Examples:

Coal
Iron Ore
Bauxite
Limestone
Multiple

Required: YES

---

## page_start

Starting page of chunk.

Required: YES

---

## page_end

Ending page of chunk.

Required: YES

---

## section

Section identifier.

Examples:

Section 23
Rule 106
Regulation 127

Required: NO

---

## subsection

Subsection identifier.

Examples:

23(1)
106(a)
127(iii)

Required: NO

---

## chunk_number

Chunk sequence number.

Required: YES

---

## total_chunks

Total chunks in source document.

Required: YES

---

## text

Actual cleaned corpus text.

Required: YES

---

# Example Record

{
  "document_id": "CMR2017",
  "chunk_id": "CMR2017_042_001",
  "title": "Coal Mines Regulations 2017",
  "document_type": "REGULATION",
  "source_authority": "DGMS",
  "year": 2017,
  "publication_date": "2017-12-27",
  "language": "English",
  "state": "National",
  "commodity": "Coal",
  "page_start": 42,
  "page_end": 43,
  "section": "Regulation 106",
  "subsection": "106(2)",
  "chunk_number": 1,
  "total_chunks": 215,
  "text": "Every mine manager shall..."
}

---

# Storage Format

Primary corpus format:

JSONL

One record per line.

---

# Future Extensions

Potential future fields:

- amendment_reference
- citation_count
- regulation_category
- hazard_type
- safety_domain
- esg_domain

These fields are intentionally excluded from v1.0.

