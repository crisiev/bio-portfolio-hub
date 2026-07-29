"""Automated unit tests for statistical services."""

import pytest
from src.services.stats_service import StatsService


def test_two_sample_ttest_significant():
    sample_a = [12.1, 11.8, 12.5, 12.0, 11.9]
    sample_b = [18.2, 17.9, 18.5, 18.1, 18.4]

    res = StatsService.run_two_sample_ttest(sample_a, sample_b, alpha=0.05)

    assert res.is_statistically_significant is True
    assert res.p_value < 0.05
    assert "Reject null hypothesis" in res.interpretation


def test_two_sample_ttest_insufficient_sample():
    sample_a = [12.1]
    sample_b = [18.2]

    with pytest.raises(ValueError, match="at least 3 numerical data points"):
        StatsService.run_two_sample_ttest(sample_a, sample_b)
