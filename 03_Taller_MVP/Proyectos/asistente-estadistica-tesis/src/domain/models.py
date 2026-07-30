"""Domain models and Pydantic validation schemas."""

from pydantic import BaseModel, Field


class StatRequest(BaseModel):
    sample_a: list[float] = Field(..., description="First group numerical sample")
    sample_b: list[float] = Field(..., description="Second group numerical sample")
    alpha: float = Field(
        default=0.05, ge=0.001, le=0.1, description="Significance level alpha"
    )


class StatResponse(BaseModel):
    test_name: str
    statistic: float
    p_value: float
    is_statistically_significant: bool
    interpretation: str
    recommendation: str
