# marketlens-mlops

![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)
![Kubeflow](https://img.shields.io/badge/Kubeflow-v2.5.0-orange.svg)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-blue.svg)

Kubeflow ML pipeline with XGBoost classification, K-Means + PCA unsupervised learning, Apriori association rule mining, and a composite Top-K scoring engine. Fully decoupled cloud-native architecture using MinIO for artifact passing.

## Pipeline DAG

| Stage | Component | Description |
|-------|-----------|-------------|
| 1 | Preprocessing | Cleans enriched data and prepares tabular features |
| 2 | Supervised Training | Trains XGBoost classifier for top-product prediction |
| 3 | Unsupervised Training | K-Means clustering and PCA for product segmentation |
| 4 | Association Rules | Market basket analysis using Apriori algorithm |
| 5 | Scoring Engine | Composite Top-K ranking based on multiple signals |

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment:
   ```bash
   cp .env.example .env
   ```

3. Run individual models locally:
   ```bash
   export PYTHONPATH=$PYTHONPATH:.
   python ml_models/preprocessing.py
   ```

## Kubeflow Deployment

To compile the pipeline:
```bash
python pipelines/main_pipeline.py
```
This generates `pipeline.yaml` which can be uploaded to the Kubeflow UI.

## Environment Variables

- `MINIO_ACCESS_KEY`: Access key for MinIO storage
- `MINIO_SECRET_KEY`: Secret key for MinIO storage
- `MINIO_ENDPOINT`: MinIO server endpoint (S3 compatible)
- `MINIO_BUCKET`: Target bucket for data artifacts

## Docker Usage

Build the image:
```bash
docker build -t ghcr.io/marketlens-ai-platform/marketlens-mlops:latest .
```

## Part of the MarketLens AI Platform

This repository focuses on the MLOps layer of the MarketLens platform, ensuring scalable and reproducible ML workflows.

---
**Author:** Yassine Kamouss — FST Tanger, LSI 2, 2025/2026
