# Agentic RAG Execo

An intelligent **document information extraction system** built using **Retrieval-Augmented Generation (RAG)** with **agentic workflows** to extract structured data from PDF documents, especially financial and legal agreements such as **Stock Purchase Agreements (SPAs)**.

The system combines **PDF parsing, semantic retrieval, vector search, and agent-driven reasoning** to convert unstructured agreements into structured JSON output.

---

## Problem Statement

Financial and legal agreements often contain critical business information embedded inside long unstructured PDF documents.

Manual extraction of these fields is:

* time-consuming
* error-prone
* difficult to scale

This project solves the problem using an **Agentic RAG pipeline** that intelligently retrieves relevant document chunks and extracts structured key fields using an LLM-powered workflow.

---

## Features

* **PDF Text Extraction** – Reads and processes text from PDF documents
* **Intelligent Chunking** – Splits documents into contextual chunks with overlap
* **Vector Store Integration** – Uses ChromaDB for semantic similarity search
* **Agentic Workflow** – Uses LangGraph based agent nodes for extraction logic
* **LLM Integration** – Supports local inference via Ollama
* **Configurable Field Extraction** – Extracts predefined financial fields
* **Fallback Mechanism** – Regex-based fallback extraction for critical fields
* **Structured JSON Output** – Saves extracted results in JSON format
* **Modular Code Design** – Clean and scalable project structure

---

## Architecture Flow

PDF Document
↓
Text Extraction
↓
Chunking + Overlap
↓
Embedding Generation
↓
Vector Store (Chroma)
↓
Retriever
↓
LangGraph Agent Workflow
↓
Structured JSON Output

---

## Tech Stack

* Python
* LangGraph
* LangChain
* Ollama
* Chroma
* HuggingFace Embeddings
* PyPDF
* Sentence Transformers

---

## Installation

### Prerequisites

* Python 3.10+
* Ollama installed and running
* `llama3.1:8b` model downloaded

---

## Setup

### 1. Clone repository

```
git clone https://github.com/swapnil-35/agentic_rag_execo.git
cd agentic_rag_execo
```

---

### 2. Create virtual environment

```
python -m venv venv
```

Activate environment:
```
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Start Ollama

```
ollama serve
ollama pull llama3.1:8b
```

---

## Usage

### 1. Place PDF inside `data/`

Example:

```text
data/POC_TEST_SPA.pdf
```

---

### 2. Update config

Modify `config.py`:

```python
PDF_PATH = "data/POC_TEST_SPA.pdf"
```

---

### 3. Run project

```
python main.py
```

---

### 4. Output

The extracted fields will be saved to:

```text
output/extracted.json
```

---

## Sample Output

```json
{
  "Document Type": "Share Purchase Agreement",
  "Effective Date": "May 22, 2018",
  "Buyer": "Virgil AcquisitionCo Inc.",
  "Company (Target)": "OnTargetJobs Canada",
  "Seller": "Not Found",
  "Cash Purchase Price": "$120,000,000",
  "Governing Law": "New York"
}
```

---

## Configuration

Update `config.py` to customize:

* `PDF_PATH` – input PDF path
* `VECTOR_STORE_PATH` – ChromaDB storage location
* `OLLAMA_MODEL` – LLM model
* `CHUNK_SIZE` – chunk length
* `CHUNK_OVERLAP` – overlap size
* `TOP_K` – retrieved chunks count

---

## Project Structure

```text
agentic_rag_execo/
│
├── config.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── POC_TEST_SPA.pdf
│   └── chroma_db/
│
├── output/
│   └── extracted.json
│
└── src/
    ├── __init__.py
    ├── chunker.py
    ├── document_loader.py
    ├── extractor_agent.py
    ├── prompts.py
    ├── utils.py
    └── vector_store.py
```

---

## Dependencies

Main libraries used:

* `langgraph`
* `langchain`
* `langchain-ollama`
* `langchain-huggingface`
* `sentence-transformers`
* `pypdf`
* `chromadb`
* `tiktoken`
* `python-dotenv`

Install all dependencies using:

```
pip install -r requirements.txt
```

---

## Extracted Fields

The system extracts the following fields:

* Document Type
* Effective Date
* Buyer
* Company (Target)
* Seller
* Shares Transacted
* Cash Purchase Price
* Escrow Agent
* Escrow Amount
* Target Working Capital
* Indemnification De Minimis Amount
* Indemnification Basket Amount
* Indemnification Cap Amount
* Governing Law

---

## Future Improvements

* Multi-document retrieval
* Better agent orchestration
* Confidence score for extracted fields
* Human review workflow
* FastAPI deployment
* Docker support
* Cloud deployment on AWS / Render

---

## Use Cases

* Legal document extraction
* Financial agreement parsing
* Due diligence automation
* Contract intelligence
* Enterprise document workflows

---

## Author

Developed as an **Agentic RAG assignment project** with modular architecture and production-style workflow design.
