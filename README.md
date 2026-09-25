# Fraud Risk Scoring Service

A small service that trains a logistic regression model to flag potentially
fraudulent transactions, and serves predictions over a REST API.

## Local setup

```bash
uv sync
uv run python -m src.train        # trains the model, writes models/model.pkl
uv run uvicorn src.app:app --host 0.0.0.0 --port 8000
```

## Example request

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"amount": 120.5, "customer_age_days": 400, "num_previous_orders": 2, "avg_order_value": 60.0, "country_risk_score": 0.3}'
```

## Docker

```bash
docker build -t fraud-risk-service .
docker run -p 8000:8000 fraud-risk-service
```

## Deploying with Helm

```bash
helm template fraud-risk-service deploy/helm/fraud-risk-service
helm install fraud-risk-service deploy/helm/fraud-risk-service
```
