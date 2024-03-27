from langchain_openai.chat_models import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings

from config.conf import settings
from config.databases import get_or_create_collection


class ChatOpenAISingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            llm_model = settings.OPENAI_VERSION
            cls._instance = ChatOpenAI(temperature=0.0, model=llm_model)
        return cls._instance


def get_llm_response(query) -> str:
    llm = ChatOpenAISingleton()

    collection_name = get_or_create_collection()
    vectordb = Chroma(
        collection_name=collection_name.name,
        embedding_function=OpenAIEmbeddings(),
        persist_directory=settings.CHROMADB_DIRECTORY
    )

    docs = vectordb.similarity_search(query)
    q_docs = "".join([docs[i].page_content for i in range(len(docs))])
    answer = llm.invoke(
        f"{q_docs} Question: {query}. and in the end write the title of the section in which the answer was found")
    return answer.content.replace("\n\n", " ")
