# IndianMiningGPT Corpus Inventory Process

## Purpose

This document defines the process used to register, classify, and inventory source documents before corpus generation.

No document may enter the corpus pipeline without first being registered.

---

# Objectives

The inventory process ensures:

- Complete source traceability
- Proper classification
- Metadata consistency
- Corpus auditing capability
- Future corpus expansion

---

# Inventory Workflow

Source PDF
    ↓
Document Registration
    ↓
Document Classification
    ↓
Metadata Assignment
    ↓
Registry Entry Creation
    ↓
Validation
    ↓
Corpus Processing

---

# Required Information

For each document collect:

- Document ID
- Title
- Document Type
- Source Authority
- Year
- Version
- Language
- State
- Commodity
- Page Count
- Filename
- Source URL (if available)

---

# Registration Rules

Every document must:

- Have a unique document_id
- Have a valid classification
- Have a source authority
- Be traceable to an official source

---

# Inventory Deliverables

data/metadata/

├── document_registry.csv
├── corpus_statistics.json
├── inventory_summary.md

---

# Validation Checklist

For each document:

- [ ] Document ID assigned
- [ ] Classification assigned
- [ ] Authority identified
- [ ] Metadata completed
- [ ] Registry updated

