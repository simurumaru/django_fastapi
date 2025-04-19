from typing import Iterable, Optional

from django.conf import settings
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import Mount
from starlette.types import Lifespan


__all__ = ("create",)

def create(
    *_,
    rest_routers: Iterable[APIRouter],
    mount_routers: Iterable[Mount],
    lifespan: Optional[Lifespan[FastAPI]] = None,
) -> FastAPI:
    """The application factory using FastAPI framework.
    🎉 Only passing routes is mandatory to start.
    """
    app = FastAPI(
        title='api',
        lifespan=lifespan,
        docs_url='/api/docs',
        redoc_url='/api/redoc',
    )

    # Include REST API routers
    for router in rest_routers:
        app.include_router(router, prefix="/api")

    for mount in mount_routers:
        app.mount(path=mount.path, app=mount.app, name=mount.name)

    # ========= Middleware =========
    # Setup middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
