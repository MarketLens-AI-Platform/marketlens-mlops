FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ml_models/ /app/ml_models/
COPY pipelines/ /app/pipelines/

ENV PYTHONPATH=/app
