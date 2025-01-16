from fastapi import FastAPI
from app.core import settings
from app.api import router

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
app.include_router(router, prefix="/api/v1")
