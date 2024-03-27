import os

from dotenv import load_dotenv
from pydantic import BaseConfig

from fastapi.templating import Jinja2Templates


load_dotenv()


class Settings(BaseConfig):

    # DIRS
    UPLOAD_DIRECTORY: str = "app/files"
    CHROMADB_DIRECTORY: str = "chromadb"

    # CHROMADB
    CHROMADB_COLLECTION: str = "documents_collection"

    # OPENAI API
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    OPENAI_VERSION: str = os.getenv("OPENAI_VERSION")

    # Allowed hosts
    BACKEND_CORS_ORIGINS: list = [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:47930",
        "http://127.0.0.1:47930"
        "http://localhost:8000",
        "http://localhost:8080",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:8080",
    ]

    TEMPLATES = Jinja2Templates(directory="app/static/templates")


settings = Settings()
