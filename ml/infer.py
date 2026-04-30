"""
TruthGuard ML Inference Service

This FastAPI service provides:
- /predict : REAL/FAKE prediction with confidence and explanation
- /explain : SHAP-based word-level interpretability
- /health  : health check for CI/CD and Kubernetes

Designed for:
- Local execution
- Pytest
- Docker
- Kubernetes
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import os
import numpy as np
import shap

from llm.llm_explainer import explain_prediction

# -----------------------------------------------------------------------------
# FastAPI application
# -----------------------------------------------------------------------------

app = FastAPI(
    title="TruthGuard ML Inference Service",
    version="1.2.0"
)

# -----------------------------------------------------------------------------
# Load model and vectorizer safely
# -----------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"Model file not found at {MODEL_PATH}")

with open(MODEL_PATH, "rb") as f:
    model, vectorizer = pickle.load(f)

LABEL_MAP = {
    0: "FAKE",
    1: "REAL"
}

# -----------------------------------------------------------------------------
# Schemas
# -----------------------------------------------------------------------------

class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    prediction: str
    confidence: float
    explanation: str


# -----------------------------------------------------------------------------
# Health endpoint (CI/CD & Kubernetes)
# -----------------------------------------------------------------------------

@app.get("/health")
def health():
    return {"status": "ok"}


# -----------------------------------------------------------------------------
# Prediction endpoint
# -----------------------------------------------------------------------------

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    text = request.text

    # Input validation
    if not text or not text.strip():
        raise HTTPException(
            status_code=422,
            detail="Input text must not be empty"
        )

    try:
        # Vectorize
        X = vectorizer.transform([text])

        # Predict numeric class
        numeric_pred = int(model.predict(X)[0])
        prediction = LABEL_MAP.get(numeric_pred, "UNKNOWN")

        # Confidence from probabilities
        probs = model.predict_proba(X)[0]
        confidence = round(float(np.max(probs) * 100), 2)

        # Explanation (LLM-style, deterministic)
        explanation = explain_prediction(prediction, confidence)

        return {
            "prediction": prediction,
            "confidence": confidence,
            "explanation": explanation
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Inference failed: {str(e)}"
        )


# -----------------------------------------------------------------------------
# SHAP interpretability endpoint
# -----------------------------------------------------------------------------

@app.get("/explain")
def explain(text: str):
    """
    SHAP-based interpretability endpoint.

    Returns the most influential words pushing the decision
    toward REAL or FAKE.
    """

    if not text or not text.strip():
        raise HTTPException(
            status_code=422,
            detail="Text must not be empty"
        )

    try:
        # Vectorize input
        X = vectorizer.transform([text])

        # Predict label
        numeric_pred = int(model.predict(X)[0])
        prediction = LABEL_MAP.get(numeric_pred, "UNKNOWN")

        # SHAP explainer (Linear model)
        explainer = shap.LinearExplainer(model, X, feature_perturbation="interventional")
        shap_values = explainer.shap_values(X)

        feature_names = vectorizer.get_feature_names_out()
        shap_pairs = list(zip(feature_names, shap_values[0]))

        # Sort SHAP values
        positive = sorted(
            [(w, float(v)) for w, v in shap_pairs if v > 0],
            key=lambda x: x[1],
            reverse=True
        )[:10]

        negative = sorted(
            [(w, float(v)) for w, v in shap_pairs if v < 0],
            key=lambda x: x[1]
        )[:10]

        probs = model.predict_proba(X)[0]
        confidence = round(float(np.max(probs) * 100), 2)

        return {
            "prediction": prediction,
            "confidence": confidence,
            "top_positive_words": [
                {"word": w, "shap_value": v} for w, v in positive
            ],
            "top_negative_words": [
                {"word": w, "shap_value": v} for w, v in negative
            ]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Explanation failed: {str(e)}"
        )