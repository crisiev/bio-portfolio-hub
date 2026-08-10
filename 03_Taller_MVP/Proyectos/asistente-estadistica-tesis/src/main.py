"""FastAPI Application Main Entry Point."""
from fastapi import Query
from src.services.tm_calculator import calculate_tm

from fastapi import FastAPI

from src.api.routes import router as stats_router
from src.core.config import settings

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
@app.get("/tm")
def get_tm(secuencia: str = Query(..., description="Secuencia de ADN a calcular")):
    """
    Recibe una secuencia de ADN por URL, la normaliza a mayúsculas,
    y devuelve su Temperatura de Fusión (Tm).
    """
    sec_upper = secuencia.upper()
    tm_val = calculate_tm(sec_upper)
    
    return {
        "secuencia": sec_upper,
        "tm_wallace": tm_val
    }
