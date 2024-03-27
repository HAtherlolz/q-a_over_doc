from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from config.conf import settings
from config.databases import init_db
from app.api.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up")
    init_db()
    yield
    print("Shutting down")


app = FastAPI(
    openapi_url="/api/v1/",
    docs_url="/api/v1/docs/",
    redoc_url="/api/v1/redoc/",
    title="LLM Q&A over PDF Document",
    description="Backend for LLM Q&A over PDF Document",
    version="1.1",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

