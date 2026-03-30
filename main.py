from src.document_loader import load_pdf_text
from src.chunker import chunk_document
from src.vector_store import create_vector_store
from src.extractor_agent import app
from config import Config


def main():
    text = load_pdf_text(Config.PDF_PATH)

    chunks = chunk_document(text)

    create_vector_store(chunks, Config.VECTOR_STORE_PATH)

    result = app.invoke({})

    print(result)


if __name__ == "__main__":
    main()