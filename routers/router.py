from fastapi import APIRouter

from .user import router as user_router
from .cafe import router as cafe_router

api_router = APIRouter()

api_router.include_router(user_router, prefix="/user")
api_router.include_router(cafe_router, prefix="/cafe")

