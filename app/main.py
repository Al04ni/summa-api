from fastapi import FastAPI
from app.routers import movies, health
from app.config import Config

app = FastAPI(
    title="Summa API 🎬",
    description="Backend API for Summa CLI tool",
    version="0.2.0"
)

# Include routers
app.include_router(movies.router, prefix="/api/v1")
app.include_router(health.router)

@app.get("/")
async def root():
    return {
        "message": "🎬 Welcome to Summa API",
        "docs": "/docs",
        "status": "scalable"
    }