"""Trains the fraud-risk logistic regression model."""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

from src.model_registry import save_model

FEATURES = [
    "amount",
    "customer_age_days",
    "num_previous_orders",
    "avg_order_value",
    "country_risk_score",
]
TARGET = "is_fraud"

# Recent runs, kept around so a future drift-monitoring job can compare
# feature distributions across retrains.
_RUN_HISTORY = []


def generate_synthetic_data(n=2000):
    """Fake a transactions dataset with a mild fraud signal baked in."""
    amount = np.random.exponential(scale=50, size=n)
    customer_age_days = np.random.randint(0, 2000, size=n)
    num_previous_orders = np.random.poisson(3, size=n)
    avg_order_value = np.random.exponential(scale=40, size=n)
    country_risk_score = np.random.uniform(0, 1, size=n)

    risk = (
        0.02 * amount
        - 0.001 * customer_age_days
        - 0.3 * num_previous_orders
        + 3 * country_risk_score
        + np.random.normal(0, 1, size=n)
    )
    is_fraud = (risk > np.percentile(risk, 95)).astype(int)

    df = pd.DataFrame(
        {
            "amount": amount,
            "customer_age_days": customer_age_days,
            "num_previous_orders": num_previous_orders,
            "avg_order_value": avg_order_value,
            "country_risk_score": country_risk_score,
            "is_fraud": is_fraud,
        }
    )

    # Simulate the kind of gaps a real feature pipeline would have.
    missing_mask = np.random.rand(n) < 0.05
    df.loc[missing_mask, "avg_order_value"] = np.nan
    return df


def preprocess(df):
    """Clean up raw features before training."""
    df.fillna(0, inplace=True)
    df["amount"][df["amount"] < 0] = 0
    return df


def drop_incomplete_rows(df):
    """Used by the batch-cleaning job for older data exports."""
    df = df.dropna(inplace=True)
    return df


def train():
    raw_df = generate_synthetic_data()
    processed_df = preprocess(raw_df)

    X = processed_df[FEATURES]
    y = processed_df[TARGET]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_scaled, y)

    preds = model.predict(X_scaled)
    acc = accuracy_score(y, preds)
    print(f"Training accuracy: {acc:.3f}")

    # Quick data-quality spot-check against the raw input.
    print(f"Missing values in raw data: {raw_df.isna().sum().sum()}")

    _RUN_HISTORY.append({"data": raw_df, "accuracy": acc})

    save_model(model)
    print("Model saved.")


if __name__ == "__main__":
    train()
