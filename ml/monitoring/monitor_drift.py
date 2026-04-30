"""
Drift monitoring module for the TruthGuard ML system.

This module monitors prediction confidence scores over time and
flags potential model drift when confidence degrades.

It DOES NOT retrain the model automatically.
Instead, it provides a recommendation to the ML engineer.

This design follows responsible MLOps practices.
"""

import json
import statistics
import time
from typing import List, Dict


class DriftMonitor:
    """
    DriftMonitor analyzes recent prediction confidence scores
    to detect potential model performance drift.

    Drift is flagged when:
    - Average confidence drops significantly
    - A large proportion of predictions fall below a threshold
    """

    def __init__(self, confidences: List[float], threshold: float = 0.6):
        """
        Initialize the DriftMonitor.

        Parameters:
        - confidences: list of recent confidence scores (0.0–1.0)
        - threshold: confidence threshold below which predictions
                     are considered low-confidence
        """
        if not confidences:
            raise ValueError("Confidence list must not be empty")

        self.confidences = confidences
        self.threshold = threshold

    def check_drift(self) -> Dict:
        """
        Compute drift metrics and determine whether drift is detected.

        Returns:
        Dictionary with:
        - mean_confidence
        - std_confidence
        - low_confidence_rate
        - drift_detected (bool)
        - recommendation (string)
        """

        mean_conf = statistics.mean(self.confidences)
        std_conf = statistics.stdev(self.confidences) if len(self.confidences) > 1 else 0.0

        low_conf_count = sum(1 for c in self.confidences if c < self.threshold)
        low_conf_rate = low_conf_count / len(self.confidences)

        drift_detected = (
            mean_conf < 0.65 or
            low_conf_rate > 0.3
        )

        recommendation = (
            "Model drift suspected. Retraining recommended."
            if drift_detected
            else "Model performance stable."
        )

        return {
            "mean_confidence": round(mean_conf, 3),
            "std_confidence": round(std_conf, 3),
            "low_confidence_rate": round(low_conf_rate, 3),
            "drift_detected": drift_detected,
            "recommendation": recommendation
        }

    def log_result(self, result: Dict, log_file: str = "ml/monitoring/drift_log.jsonl"):
        """
        Append drift analysis result to a JSONL log file.

        Each line represents one monitoring run with timestamp.
        """

        log_entry = {
            "timestamp": int(time.time()),
            **result
        }

        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")


# -----------------------------------------------------------------------------
# Demonstration (for development / grading / understanding)
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # Example confidence scores from recent predictions
    sample_confidences = [
        0.92, 0.88, 0.90, 0.72, 0.65,
        0.61, 0.59, 0.55, 0.58, 0.62
    ]

    monitor = DriftMonitor(sample_confidences)
    analysis = monitor.check_drift()
    monitor.log_result(analysis)

    print("Drift analysis result:")
    for key, value in analysis.items():
        print(f"  {key}: {value}")