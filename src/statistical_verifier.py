"""
Statistical Verifier for ISPE GAMP® AI & Computer Software Assurance
Calculates Wilson Score Confidence Intervals and evaluates statistical acceptance criteria.
"""

import math
from typing import Dict, Any

class StatisticalVerifier:
    @staticmethod
    def calculate_wilson_interval(successes: int, total: int, confidence: float = 0.95) -> Dict[str, float]:
        """
        Calculates the Wilson Score Confidence Interval for binomial proportion.
        Used to validate non-deterministic AI/ML systems under GAMP AI guidelines.
        """
        if total == 0:
            return {"point_estimate": 0.0, "lower_bound": 0.0, "upper_bound": 0.0}
            
        p_hat = successes / total
        z = 1.96 if confidence == 0.95 else 2.576 # 95% or 99%
        
        denominator = 1 + (z**2 / total)
        center_adjusted_probability = p_hat + (z**2 / (2 * total))
        adjusted_standard_deviation = math.sqrt((p_hat * (1 - p_hat) / total) + (z**2 / (4 * (total**2))))
        
        lower_bound = (center_adjusted_probability - (z * adjusted_standard_deviation)) / denominator
        upper_bound = (center_adjusted_probability + (z * adjusted_standard_deviation)) / denominator
        
        return {
            "successes": successes,
            "total_trials": total,
            "point_estimate": round(p_hat, 4),
            "lower_bound_95ci": round(max(0.0, lower_bound), 4),
            "upper_bound_95ci": round(min(1.0, upper_bound), 4),
            "passes_90_percent_threshold": lower_bound >= 0.90
        }
