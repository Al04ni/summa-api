from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="Summa API 🎬",
    description="Backend API for Summa CLI tool.",
    version="0.1.0"
)

app.include_router(router)
