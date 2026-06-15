import os
import boto3
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def get_s3_client():
    """Returns an S3 client using the default credential provider chain (IRSA)."""
    return boto3.client('s3')

def download_file(object_name, local_path):
    """Download a file from S3."""
    client = get_s3_client()
    bucket = os.getenv("S3_BUCKET", "marketlens-raw-ingestion-v110")
    local_path = Path(local_path)
    local_path.parent.mkdir(parents=True, exist_ok=True)
    client.download_file(bucket, object_name, str(local_path))
    return local_path

def upload_file(local_path, object_name):
    """Upload a file to S3."""
    client = get_s3_client()
    bucket = os.getenv("S3_BUCKET", "marketlens-raw-ingestion-v110")
    client.upload_file(str(local_path), bucket, object_name)
