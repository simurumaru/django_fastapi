import asyncio
from contextlib import asynccontextmanager
from fastapi import APIRouter, FastAPI

from category.api.routers import router as category_router
from product.api.routers import router as product_router

__all__ = (
    "routers",
    "lifespan",
)

routers: list[APIRouter] = [
    category_router,
    product_router,
]

@asynccontextmanager
async def lifespan(application: FastAPI):
    yield
