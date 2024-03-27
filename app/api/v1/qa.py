from fastapi import APIRouter, UploadFile, File, Request
from fastapi.responses import HTMLResponse

from config.conf import settings
from app.services.files import save_file, get_answer
from app.schemas.responses import ResponseSchema


api_qa = APIRouter()
frontend = APIRouter()


@api_qa.post("/upload-file/", response_model=ResponseSchema, status_code=200)
def upload_file(file: UploadFile = File(...)):
    return save_file(file)


@api_qa.get("/qa/", response_model=ResponseSchema, status_code=200)
def qa(question: str):
    return get_answer(question)


# Frontend
@frontend.get("/", response_class=HTMLResponse)
async def front_upload_file(request: Request):
    return settings.TEMPLATES.TemplateResponse("index.html", {"request": request})


@frontend.get("/qa", response_class=HTMLResponse)
async def front_qa(request: Request):
    return settings.TEMPLATES.TemplateResponse("qa.html", {"request": request})
