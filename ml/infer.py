from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

# Load trained model
model, vectorizer = pickle.load(open("model.pkl", "rb"))

class NewsRequest(BaseModel):
    text: str

@app.post("/predict")
def predict_news(request: NewsRequest):
    text = request.text
    vector = vectorizer.transform([text])
    probability = model.predict_proba(vector)[0][1]
    label = "REAL" if probability >= 0.5 else "FAKE"

    return {
        "prediction": label,
        "confidence": round(probability * 100, 2),
        "explanation": "Prediction generated using learned linguistic patterns from verified news sources."
    }