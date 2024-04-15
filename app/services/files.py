import shutil

from pathlib import Path

from fastapi import UploadFile

from config.conf import settings
from app.services.llm import get_llm_response
from app.schemas.responses import ResponseSchema
from app.repositories.chroma.docs import store_doc


def save_file(file: UploadFile) -> ResponseSchema:
    # TODO: Check if it pdf
    saved_file = save_file_to_dir(file)
    store_doc(saved_file)
    return ResponseSchema(response="Ok")


def save_file_to_dir(file: UploadFile) -> Path:
    upload_path = Path(settings.UPLOAD_DIRECTORY) / file.filename
    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return upload_path


def get_answer(question: str) -> ResponseSchema:
    answer = get_llm_response(question)
    return ResponseSchema(response=answer)
