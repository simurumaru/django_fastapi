"""
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""
import os
from pathlib import Path
from dotenv import load_dotenv
import django

from django.conf import settings
from django.core.asgi import get_asgi_application
from fastapi.routing import Mount
from fastapi.staticfiles import StaticFiles

from core.application import factory
from core.errors import EnvVariableMissingError

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / '.env')

STATE = os.getenv("BACKEND__STATE")

if not STATE:
    raise EnvVariableMissingError("BACKEND__STATE")

settings_module = f"server.settings.{STATE}"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
django.setup()

from server.api import lifespan, routers

django_app = get_asgi_application()

app = factory.create(
    lifespan=lifespan,
    rest_routers=routers,
    mount_routers=[
        Mount(
            "/static/",
            StaticFiles(directory=settings.STATIC_ROOT),
            name='static'
        ),
        Mount("/", django_app, name="django")
    ],
)
