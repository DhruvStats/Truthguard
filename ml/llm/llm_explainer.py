"""
LLM-style explanation module for TruthGuard.

This module generates a human-readable explanation for a prediction
based on the model's output and confidence score.

NOTE:
- No external API calls are used yet.
- This simulates an LLM explanation layer in a controlled, testable way.
"""

def explain_prediction(prediction: str, confidence: float) -> str:
    """
    Generate a natural-language explanation based on prediction and confidence.

    Parameters:
    - prediction: "REAL" or "FAKE"
    - confidence: confidence percentage (0–100)

    Returns:
    - explanation string
    """

    if confidence >= 85:
        confidence_level = "high"
    elif confidence >= 65:
        confidence_level = "medium"
    else:
        confidence_level = "low"

    if prediction == "REAL":
        return (
            f"Classified as REAL with {confidence_level} confidence ({confidence}%). "
            "The text exhibits linguistic patterns and structure commonly found in "
            "verified news reporting."
        )

    if prediction == "FAKE":
        return (
            f"Classified as FAKE with {confidence_level} confidence ({confidence}%). "
            "The text shows characteristics often associated with misinformation, "
            "such as exaggerated claims or weak factual grounding."
        )

    return (
        "The system could not confidently classify this text. "
        "Manual review is recommended."
    )