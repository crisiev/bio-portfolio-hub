"""API Routers for statistical endpoints."""

from fastapi import APIRouter, HTTPException, status

from src.domain.models import StatRequest, StatResponse
from src.services.stats_service import StatsService

router = APIRouter(prefix="/stats", tags=["Statistical Analysis"])


@router.post("/ttest", response_model=StatResponse, status_code=status.HTTP_200_OK)
def calculate_ttest(payload: StatRequest) -> StatResponse:
    """Computes two-sample t-test hypothesis testing."""
    try:
        return StatsService.run_two_sample_ttest(
            sample_a=payload.sample_a, sample_b=payload.sample_b, alpha=payload.alpha
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
