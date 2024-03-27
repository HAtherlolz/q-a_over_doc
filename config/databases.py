import chromadb

from config.conf import settings


def get_or_create_collection() -> chromadb.Collection:
    client = chromadb.Client()
    collection = client.get_or_create_collection(settings.CHROMADB_COLLECTION)
    return collection


def init_db():
    client = chromadb.Client()
    try:
        client.create_collection(settings.CHROMADB_COLLECTION)
    except BaseException as e:
        print("Collection is already exists: ", e)
