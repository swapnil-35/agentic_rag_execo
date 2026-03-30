# Agentic RAG Execo

An intelligent document extraction system using Retrieval-Augmented Generation (RAG) with agentic workflows to extract structured data from PDF documents, particularly financial agreements like Stock Purchase Agreements (SPAs).

## Features

- **PDF Text Extraction**: Loads and processes text from PDF documents
- **Intelligent Chunking**: Splits documents into meaningful chunks with overlap for better context
- **Vector Store Integration**: Uses ChromaDB for efficient similarity search
- **Agentic Extraction**: Employs LangGraph-based agents for structured data extraction
- **Ollama Integration**: Leverages local LLMs via Ollama for processing
- **Configurable Fields**: Extracts predefined financial agreement fields
- **Fallback Mechanisms**: Includes regex-based fallbacks for critical fields

## Installation

### Prerequisites

- Python 
- Ollama installed and running with `llama3.1:8b` model

### Setup

1. Clone the repository:
   
   git clone <repository-url>
   cd agentic_rag_execo
   

2. Create a virtual environment:
   
   Command -- python -m venv venv
   activate -- venv\Scripts\activate
   
   

3. Install dependencies:
   
   Command -- pip install -r requirements.txt


4. Ensure Ollama is running:
   
   ollama serve
   ollama pull llama3.1:8b


## Usage

1. Place your PDF document in the `data/` directory and update `config.py` with the correct path.

2. Run the main script:
   
   python main.py
   

3. The extracted data will be saved to `output/extracted.json`.

## Configuration

Edit `config.py` to customize:

- `PDF_PATH`: Path to the input PDF file
- `VECTOR_STORE_PATH`: Directory for ChromaDB storage
- `OLLAMA_MODEL`: Ollama model to use
- `CHUNK_SIZE`: Size of text chunks
- `CHUNK_OVERLAP`: Overlap between chunks
- `TOP_K`: Number of similar chunks to retrieve

## Project Structure

```
agentic_rag_execo/
├── config.py                 # Configuration settings
├── main.py                   # Main execution script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── data/
│   ├── POC_TEST_SPA.pdf      # Sample PDF document
│   └── chroma_db/            # Vector store database
├── output/
│   └── extracted.json        # Extracted data output
└── src/
    ├── __init__.py
    ├── chunker.py            # Document chunking logic
    ├── document_loader.py    # PDF text extraction
    ├── extractor_agent.py    # LangGraph agent for extraction
    ├── prompts.py            # LLM prompts
    ├── utils.py              # Utility functions
    └── vector_store.py       # ChromaDB integration
```

## Dependencies

- `langgraph`: For building agentic workflows
- `langchain`: Core LLM framework
- `langchain-ollama`: Ollama integration
- `langchain-huggingface`: HuggingFace embeddings
- `sentence-transformers`: Text embeddings
- `pypdf`: PDF text extraction
- `chromadb`: Vector database
- `tiktoken`: Token counting
- `python-dotenv`: Environment variable management

## Extracted Fields

The system extracts the following fields from financial documents:

- Document Type
- Effective Date
- Buyer
- Company (Target)
- Seller
- Shares Transacted
- Cash Purchase Price
- Escrow Agent
- Escrow Amount
- Target Working Capital
- Indemnification De Minimis Amount
- Indemnification Basket Amount
- Indemnification Cap Amount
- Governing Law
