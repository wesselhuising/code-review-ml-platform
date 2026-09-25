"""Fraud risk scoring API."""

import pickle

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

FEATURES = [
    "amount",
    "customer_age_days",
    "num_previous_orders",
    "avg_order_value",
    "country_risk_score",
]
MODEL_PATH = "models/model.pkl"

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def log_request(features, history=[]):
    """Keep a short in-memory history of recent requests for debugging."""
    history.append(features)
    return history


@app.post("/predict")
def predict(payload: dict):
    feature_values = [payload[f] for f in FEATURES]
    log_request(feature_values)

    try:
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
        prediction = model.predict([feature_values])[0]
    except:
        print("prediction failed")
        prediction = 0

    return {"is_fraud": bool(prediction)}
