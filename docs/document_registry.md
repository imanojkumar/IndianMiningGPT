# IndianMiningGPT Document Registry Specification

## Purpose

This document defines how source documents are identified, catalogued, tracked, versioned, and managed within the IndianMiningGPT corpus.

The Document Registry acts as the authoritative inventory of all source documents used for corpus generation.

Every document entering the corpus must first be registered here.

---

# Objectives

The registry enables:

- Source traceability
- Version control
- Amendment tracking
- Corpus auditing
- Corpus statistics
- Future corpus expansion

---

# Registry Principles

1. Every document must have a unique identifier.
2. Every document must be classified.
3. Every document must have a source authority.
4. Every document must be traceable to its origin.
5. Every document version must be preserved.

---

# Registry Storage

Primary format:

CSV

File location:

data/metadata/document_registry.csv

---

# Registry Schema

Each row represents one document.

Columns:

document_id
title
document_type
source_authority
year
version
language
state
commodity
pages
file_name
file_path
source_url
status
notes

---

# Field Definitions

## document_id

Unique identifier.

Examples:

MA1952
MMDR1957
CMR2017
MMR1961

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

Examples:

DGMS
IBM
Ministry of Mines
MoEFCC
CPCB
State Government

Required: YES

---

## year

Publication year.

Required: YES

---

## version

Document version.

Examples:

Original
Amended
Revision 1
Revision 2

Required: YES

---

## language

Examples:

English
Hindi

Required: YES

---

## state

Examples:

National
Jharkhand
Odisha
Chhattisgarh

Required: YES

---

## commodity

Examples:

Coal
Iron Ore
Bauxite
Limestone
Multiple

Required: YES

---

## pages

Total pages in source document.

Required: YES

---

## file_name

Original PDF filename.

Required: YES

---

## file_path

Location within repository.

Example:

data/raw/Coal_Mines_Regulations_2017.pdf

Required: YES

---

## source_url

Official source URL if available.

Required: NO

---

## status

Allowed values:

REGISTERED
EXTRACTED
CLEANED
VALIDATED
ARCHIVED

Required: YES

---

## notes

Free-form comments.

Required: NO

---

# Document ID Naming Convention

## Acts

Format:

MA1952
MMDR1957

Examples:

MA1952
MMDR1957

---

## Regulations

Format:

CMR2017
MMR1961

Examples:

CMR2017
MMR1961

---

## DGMS Circulars

Format:

DGMSC_YYYY_NNN

Examples:

DGMSC_2024_001
DGMSC_2024_015

---

## DGMS Orders

Format:

DGMSO_YYYY_NNN

Examples:

DGMSO_2023_005

---

## Standards

Format:

STD_YYYY_NNN

Examples:

STD_2024_001

---

# Amendment Policy

If a document has amendments:

Store as separate registry entries.

Example:

CMR2017
CMR2017_A1
CMR2017_A2

Original document remains preserved.

---

# Lifecycle Status

REGISTERED
    ↓
EXTRACTED
    ↓
CLEANED
    ↓
VALIDATED
    ↓
ARCHIVED

---

# Example Registry Entry

document_id,title,document_type,source_authority,year,version,language,state,commodity,pages,file_name,file_path,status

CMR2017,"Coal Mines Regulations 2017",REGULATION,DGMS,2017,Original,English,National,Coal,450,Coal_Mines_Regulations_2017.pdf,data/raw/Coal_Mines_Regulations_2017.pdf,REGISTERED

---

# Future Enhancements

Potential future fields:

- checksum
- sha256
- publication_date
- amendment_reference
- jurisdiction
- document_category

These fields are intentionally excluded from v1.0.

