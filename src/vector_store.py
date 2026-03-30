import os
import shutil
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from config import Config

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


def create_vector_store(chunks, persist_directory):
    if os.path.exists(persist_directory):
        shutil.rmtree(persist_directory)

    return Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )


def load_vector_store(persist_directory):
    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )


def retrieve_context(vector_store, query, k=Config.TOP_K):
    docs = vector_store.similarity_search(query, k=k)
    return [doc.page_content for doc in docs]