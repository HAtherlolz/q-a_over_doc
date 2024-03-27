from fastapi import APIRouter

from app.api.v1.qa import api_qa, frontend


router = APIRouter()

router.include_router(frontend, prefix="", tags=["frontend"])
router.include_router(api_qa, prefix="/api/v1", tags=["qa"])
