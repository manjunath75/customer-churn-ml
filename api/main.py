from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI

from api.schemas import CustomerData

app = FastAPI(title="Customer Churn Prediction API", version="1.0")

MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "churn_pipeline.joblib"
model = joblib.load(MODEL_PATH)

THRESHOLD = 0.2

@app.get("/health", tags=["Health Check"])
def health():
    return {"status": "healthy"}

@app.post("/predict", tags=["Prediction"])
def predict(customer: CustomerData):
    customer_df = pd.DataFrame([customer.model_dump()])

    churn_probability = float(model.predict_proba(customer_df)[0,1])

    prediction = ("Yes" if churn_probability >= THRESHOLD else "No")

    return {
        "churn_probability": round(churn_probability, 4),
        "prediction": prediction,
        "threshold": THRESHOLD
    }