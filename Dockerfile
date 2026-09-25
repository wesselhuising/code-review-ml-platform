FROM python:latest

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn scikit-learn pandas numpy

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
