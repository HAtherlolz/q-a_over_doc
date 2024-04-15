from pathlib import Path
from typing import List

from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

from config.conf import settings
from config.databases import get_or_create_collection


def store_doc(file: Path) -> Chroma:
    documents = list()
    loader = PyPDFLoader(str(file))
    documents.extend(loader.load())
    chunked_documents = split_text(documents)

    collection_name = get_or_create_collection()
    chroma = Chroma.from_documents(
        documents=chunked_documents,
        embedding=OpenAIEmbeddings(),
        persist_directory=settings.CHROMADB_DIRECTORY,
        collection_name=collection_name.name
    )
    chroma.persist()
    return chroma


def split_text(docs: List[Document]) -> List[Document]:
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    chunked_documents = text_splitter.split_documents(docs)
    return chunked_documents
