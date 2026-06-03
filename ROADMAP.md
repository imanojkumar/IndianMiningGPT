# IndianMiningGPT Development Roadmap

This document defines the official development roadmap for IndianMiningGPT and serves as the primary project planning reference.

The roadmap is organized into sequential phases with clearly defined objectives, deliverables, success criteria, and exit criteria.

---

# Project Goal

To build a lightweight, domain-specific Small Language Model (SLM) for the Indian mining and natural resources sector using the JAX ecosystem, capable of understanding mining regulations, operational terminology, safety requirements, environmental compliance frameworks, and sustainability practices.

---

# Development Philosophy

The project follows five guiding principles:

1. Domain specialization over generality.
2. Reproducibility over rapid experimentation.
3. Simplicity over unnecessary complexity.
4. Open-source development.
5. Efficient deployment on modest hardware.

---

# Current Status

| Item                  | Status      |
| --------------------- | ----------- |
| Repository Created    | Complete    |
| Project Architecture  | Complete    |
| Roadmap Definition    | In Progress |
| Corpus Engineering    | Not Started |
| Tokenizer Development | Not Started |
| Model Development     | Not Started |
| Training              | Not Started |
| Evaluation            | Not Started |
| Deployment            | Not Started |



```
[x] Inventory Builder
[x] Metadata Enrichment
[x] Title Extraction
[x] Extraction Assessment
[x] Text Extraction
[x] Corpus Registry
[x] Document Classification
[x] Chunk Generation

[x] Embedding Generation
[x] Vector Database
[x] Semantic Search
[x] RAG Pipeline
[ ] Chat Interface

```

---

# Phase 0 — Foundation & Architecture Freeze

## Objective

Establish the project structure, technical direction, governance model, and development environment before implementation begins.

---

## Deliverables

### Repository Foundation

* README.md
* ROADMAP.md
* CONTRIBUTING.md
* LICENSE
* .gitignore
* requirements.txt
* pyproject.toml

### Architecture Definition

* Model family defined
* Technical stack frozen
* Hardware target frozen
* Training strategy documented

### Development Environment

* Ubuntu setup
* Python environment
* JAX verification
* CUDA verification

---

## Success Criteria

* Repository publicly available
* Documentation complete
* Architecture approved
* Environment reproducible

---

## Exit Criteria

All foundational documents approved and committed.

---

# Phase 1 — Corpus Engineering

## Objective

Create a clean, structured, traceable mining knowledge corpus suitable for tokenizer training and model development.

---

## Deliverables

### Corpus Inventory

* Document catalog
* Source tracking
* Metadata registry

### PDF Processing Pipeline

* Text extraction
* OCR verification
* Cleaning pipeline
* Normalization

### Metadata Schema

```json
{
  "document_id": "",
  "title": "",
  "source": "",
  "year": "",
  "document_type": "",
  "section": "",
  "text": ""
}
```

### Corpus Statistics

* Document count
* Word count
* Token estimates
* Vocabulary analysis

---

## Success Criteria

* All source documents processed
* Metadata attached
* Duplicate content removed
* Corpus quality validated

---

## Exit Criteria

Corpus approved for tokenizer development.

---

# Phase 2 — Tokenizer Development

## Objective

Develop a mining-specific tokenizer capable of preserving industry terminology efficiently.

---

## Deliverables

### Tokenizer Architecture

* Byte-Level BPE
* Domain vocabulary preservation

### Vocabulary Audit

Examples:

* DGMS
* MMDR
* HEMM
* Overburden
* Beneficiation
* Ventilation
* Subsidence

### Evaluation

* Token efficiency
* Compression ratio
* Mining terminology preservation

---

## Success Criteria

* Vocabulary generated
* Tokenizer validated
* Compression metrics documented

---

## Exit Criteria

Tokenizer approved for model training.

---

# Phase 3 — Model Development

## Objective

Implement the IndianMiningGPT architecture.

---

## Target Model

### IndianMiningGPT-20M

| Component   | Specification |
| ----------- | ------------- |
| Layers      | 8             |
| Hidden Size | 512           |
| Heads       | 8             |
| FFN         | 2048          |
| Context     | 512           |
| Vocabulary  | 8192          |

---

## Deliverables

### Core Components

* Transformer Blocks
* RoPE
* RMSNorm
* SwiGLU
* AdamW
* Checkpointing

### Infrastructure

* Training loop
* Validation loop
* Logging
* Metrics

---

## Success Criteria

* Forward pass operational
* Training loop operational
* Checkpointing operational

---

## Exit Criteria

Model ready for pretraining.

---

# Phase 4 — Foundation Pretraining

## Objective

Teach the model language structure, syntax, and technical reasoning foundations.

---

## Deliverables

### Training

* Pretraining dataset
* Training runs
* Loss tracking

### Monitoring

* TensorBoard integration
* Training metrics

---

## Success Criteria

* Stable training
* Loss convergence
* Checkpoint generation

---

## Exit Criteria

Base model available.

---

# Phase 5 — Mining Domain Adaptation

## Objective

Specialize the base model on mining, safety, environmental, and regulatory knowledge.

---

## Domains

### Mining Operations

* Surface Mining
* Underground Mining
* HEMM

### Regulations

* Mines Act
* MMDR
* DGMS

### Environment

* EIA
* EMP
* ESG

---

## Success Criteria

* Mining terminology retention
* Regulatory understanding improvement
* Reduced hallucinations

---

## Exit Criteria

Domain-adapted model available.

---

Phase 5.3 — Reranking

Model:
cross-encoder/ms-marco-MiniLM-L-6-v2

Purpose:
Improve retrieval relevance after FAISS search.

Input:
Top 20 retrieved chunks

Output:
Top 5 reranked chunks

---

# Phase 6 — Instruction Tuning

## Objective

Convert the base model into an assistant capable of answering user questions.

---

## Deliverables

### Instruction Dataset

* Compliance QA
* Safety QA
* ESG QA
* Technical QA

### Fine-Tuning

* SFT pipeline
* Alignment evaluation

---

## Success Criteria

* Coherent responses
* Improved factuality
* Domain-specific assistance

---

## Exit Criteria

Assistant model available.

---

# Phase 7 — Evaluation & Benchmarking

## Objective

Measure model quality using domain-specific benchmarks.

---

## Benchmark Categories

### Regulatory Knowledge

* DGMS
* MMDR
* Mining legislation

### Safety

* Ventilation
* Hazard management
* Risk assessment

### Environment

* EIA
* EMP
* Sustainability

### Operations

* Mining methods
* HEMM
* Beneficiation

---

## Metrics

* Accuracy
* Recall
* Precision
* Hallucination Rate
* Response Quality

---

## Success Criteria

Benchmark targets achieved.

---

## Exit Criteria

Model approved for deployment.

---

# Phase 8 — Deployment

## Objective

Make IndianMiningGPT usable by industry professionals.

---

## Deliverables

### Deployment Options

#### V1

CLI Interface

#### V2

Gradio Application

#### V3

REST API

---

## Future Possibilities

* Local desktop application
* Enterprise deployment
* Air-gapped mining environments
* On-premise deployment

---

## Success Criteria

Stable inference environment.

---

## Exit Criteria

Production-ready release.

---

# Versioning Strategy

| Version | Description          |
| ------- | -------------------- |
| v0.1.0  | Foundation Complete  |
| v0.2.0  | Corpus Engineering   |
| v0.3.0  | Tokenizer Complete   |
| v0.4.0  | Model Development    |
| v0.5.0  | Pretraining Complete |
| v0.6.0  | Domain Adaptation    |
| v0.7.0  | Instruction Tuning   |
| v0.8.0  | Evaluation           |
| v1.0.0  | First Public Release |

---

# Guiding Principle

IndianMiningGPT is not intended to be the largest model.

It is intended to be one of the most specialized, practical, and deployable open-source language models for the Indian mining and natural resources sector.


## Phase 8 — Corpus Cleanup & Optimization

Purpose:
Improve retrieval quality by identifying and removing noisy chunks and OCR artifacts.

Planned Activities

### Chunk Quality Assessment

Compute:

- alphabetic ratio
- unique token ratio
- language confidence
- OCR noise score
- unicode corruption score

### Language Detection

Classify chunks as:

- English
- Hindi
- Mixed

### Noise Filtering

Identify:

- OCR damaged chunks
- Gazette extraction artifacts
- corrupted unicode text
- low-information chunks

### Quality Labels

Assign:

- GOOD
- FAIR
- POOR

### Optimized Index Build

Future FAISS versions may exclude:

- POOR chunks

Expected Benefits

- Higher retrieval precision
- Better RAG responses
- Lower hallucination risk


## Phase 8.6

Logging & Silent Startup

- Replace print statements with logging
- Global VERBOSE flag
- Lazy model loading
- Silent CLI startup mode


----------


# Enterprise Deployment Roadmap

## Vision

IndianMiningGPT will support fully air-gapped enterprise deployments
for mining companies, government agencies, consultants, and industrial
organizations handling confidential information.

## Key Objectives

- Zero data leaves customer infrastructure
- No dependency on OpenAI APIs
- No dependency on cloud LLM providers
- No document uploads to third-party services
- Full control over embeddings, vector databases, and models
- Regulatory and compliance-friendly architecture
- Support for confidential operational and ESG datasets

## Enterprise Architecture

User
 ↓
Web Interface
 ↓
IndianMiningGPT
 ↓
FAISS / Qdrant
 ↓
Local Embedding Models
 ↓
Local Cross Encoder
 ↓
Local LLM (Ollama)

Supported Models:

- Gemma 3
- Qwen 3
- DeepSeek
- Llama

Deployment Modes:

- Laptop
- Workstation
- Private Server
- On-Premise Datacenter
- Air-Gapped Environment

Target Industries:

- Mining
- Metals
- Cement
- Oil & Gas
- Manufacturing
- Government

---------------


## Phase 9.1 – Query Rewriter
Status: COMPLETE

## Phase 9.2 – Conversational Retrieval
Status: COMPLETE

------------
