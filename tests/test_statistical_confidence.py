import pytest
from src.statistical_verifier import StatisticalVerifier

def test_wilson_interval_calculation():
    # 48 out of 50 successes
    res = StatisticalVerifier.calculate_wilson_interval(48, 50)
    assert res["point_estimate"] == 0.96
    assert res["lower_bound_95ci"] >= 0.86
    assert res["upper_bound_95ci"] <= 0.99

def test_threshold_gating():
    # 50 out of 50 successes
    res_pass = StatisticalVerifier.calculate_wilson_interval(50, 50)
    assert res_pass["lower_bound_95ci"] >= 0.90
    assert res_pass["passes_90_percent_threshold"] is True
    
    # 35 out of 50 successes (poor model)
    res_fail = StatisticalVerifier.calculate_wilson_interval(35, 50)
    assert res_fail["passes_90_percent_threshold"] is False
