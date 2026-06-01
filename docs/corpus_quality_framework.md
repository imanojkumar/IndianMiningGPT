# IndianMiningGPT Corpus Quality Framework

## Purpose

This document defines the quality standards, validation rules, and acceptance criteria used for corpus generation.

The objective is to ensure that only high-quality, traceable, and domain-relevant content enters the IndianMiningGPT training corpus.

---

# Guiding Principles

1. Accuracy over volume.
2. Quality over quantity.
3. Traceability over convenience.
4. Reproducibility over manual intervention.
5. Domain relevance over generic content.

---

# Corpus Acceptance Criteria

A document may enter the corpus only if:

- Source is identifiable.
- Source is authoritative.
- Content is relevant to mining and natural resources.
- Text extraction quality is acceptable.
- Metadata is complete.
- Duplicate checks have passed.

---

# Approved Source Categories

## Mining Legislation

Examples:

- Mines Act
- MMDR Act
- Related amendments

Priority:

CRITICAL

---

## Mining Regulations

Examples:

- Coal Mines Regulations
- Metalliferous Mines Regulations

Priority:

CRITICAL

---

## DGMS Publications

Examples:

- Circulars
- Orders
- Guidelines

Priority:

HIGH

---

## Environmental Regulations

Examples:

- EIA Notifications
- Air Standards
- Water Standards

Priority:

HIGH

---

## Government Publications

Examples:

- IBM Guidelines
- Ministry Reports

Priority:

HIGH

---

# OCR Quality Standards

## Native PDF

Preferred.

No OCR required.

Acceptance:

AUTOMATIC

---

## OCR PDF

Acceptance Criteria:

- Readable text
- Correct page ordering
- Minimal character corruption

---

# OCR Rejection Conditions

Reject or manually review if:

- Large text corruption
- Missing pages
- Broken formatting
- Excessive recognition errors

Examples:

Incorrect:

M1N3 SAF3TY REGULAT10NS

Correct:

MINE SAFETY REGULATIONS

---

# Header Removal Rules

Remove repetitive headers.

Examples:

Coal Mines Regulations 2017

Page 45

DGMS Circular No. 02

These should not appear repeatedly in corpus chunks.

---

# Footer Removal Rules

Remove:

- Page numbers
- Repeated publication references
- Repeated copyright notices

Unless legally required.

---

# Page Number Policy

Remove page numbers from text.

Store page references only in metadata.

Example:

page_start
page_end

---

# Table Handling Rules

## Keep Tables If

They contain:

- Limits
- Thresholds
- Standards
- Compliance values
- Safety parameters

Examples:

Dust limits
Water quality standards
Noise standards

---

## Remove Tables If

They contain only:

- Formatting artifacts
- Navigation indexes
- Repeated administrative content

---

# Figure Handling Rules

Remove:

- Decorative figures
- Logos
- Watermarks

Preserve:

- Figure captions if informative

---

# Deduplication Framework

## Exact Duplicates

Remove.

---

## Near Duplicates

Flag for review.

Examples:

Original Regulation
Amended Regulation

---

## Amendment Policy

Preserve amendments.

Do not automatically remove amendment content.

---

# Text Cleaning Rules

Normalize:

- Multiple spaces
- Repeated line breaks
- OCR spacing errors

Preserve:

- Section numbers
- Regulation references
- Rule references
- Legal numbering

---

# Language Standards

Current Version:

English Only

Future:

English + Hindi

---

# Chunk Quality Rules

Each chunk should:

- Be semantically complete.
- Preserve context.
- Avoid breaking regulations mid-sentence.
- Preserve section continuity.

---

# Metadata Validation Rules

Required fields:

- document_id
- chunk_id
- title
- document_type
- source_authority
- year
- page_start
- page_end
- text

Missing required fields:

REJECT

---

# Corpus Validation Checklist

For every processed document:

- [ ] Document registered
- [ ] Metadata validated
- [ ] Text extracted
- [ ] OCR reviewed
- [ ] Headers removed
- [ ] Footers removed
- [ ] Duplicate check completed
- [ ] Chunking completed
- [ ] JSONL exported
- [ ] Validation approved

---

# Quality Scoring Framework

Each processed document receives a score.

## Metadata Completeness

20 Points

## Extraction Quality

20 Points

## OCR Quality

20 Points

## Deduplication Quality

20 Points

## Chunk Integrity

20 Points

---

# Acceptance Threshold

90–100
Excellent

80–89
Acceptable

70–79
Manual Review Required

Below 70
Reject

---

# Corpus Release Criteria

A corpus version may be released only if:

- All documents validated.
- Quality score ≥ 90.
- Metadata complete.
- JSONL export generated.
- Registry updated.

---

# Version History

v1.0

Initial quality framework for the IndianMiningGPT corpus.

