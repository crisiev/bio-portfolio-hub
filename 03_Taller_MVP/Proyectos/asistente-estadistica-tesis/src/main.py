"""FastAPI Application Main Entry Point."""

from fastapi import FastAPI
from src.core.config import settings
from src.api.routes import router as stats_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Automated biostatistical test selection and interpretation engine for university theses.",
)

app.include_router(stats_router, prefix=settings.API_V1_STR)


@app.get("/", tags=["Health Check"])
def health_check():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
    }
