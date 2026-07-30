"""Biostatistical computation service layer."""

import numpy as np
from scipy import stats

from src.domain.models import StatResponse


class StatsService:
    """Service layer for executing biostatistical hypothesis testing."""

    @staticmethod
    def run_two_sample_ttest(
        sample_a: list[float], sample_b: list[float], alpha: float = 0.05
    ) -> StatResponse:
        """Executes a two-sample Student's t-test after a minimum-size check."""
        if len(sample_a) < 3 or len(sample_b) < 3:
            raise ValueError(
                "Each sample group must contain at least 3 numerical data points."
            )

        arr_a = np.array(sample_a)
        arr_b = np.array(sample_b)

        # Execute Independent 2-Sample T-Test
        t_stat, p_val = stats.ttest_ind(arr_a, arr_b, equal_var=True)
        is_sig = bool(p_val < alpha)

        interp = (
            f"Statistically significant difference detected (p = {p_val:.4f} < {alpha}). "
            "Reject null hypothesis."
            if is_sig
            else f"No statistically significant difference detected (p = {p_val:.4f} >= {alpha}). "
            "Fail to reject null hypothesis."
        )

        recomm = (
            "Proceed to report effect size (Cohen's d) and confidence intervals for your thesis."
            if is_sig
            else "Consider increasing sample size or checking for non-parametric distribution."
        )

        return StatResponse(
            test_name="Two-Sample Student's T-Test",
            statistic=float(t_stat),
            p_value=float(p_val),
            is_statistically_significant=is_sig,
            interpretation=interp,
            recommendation=recomm,
        )
