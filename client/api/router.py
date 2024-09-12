from fastapi import APIRouter

from api.bar_router import router as bar_router

router = APIRouter()

router.include_router(bar_router, tags=["bar"], prefix="/bar")