import os
from minio import Minio
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def get_minio_client():
    return Minio(
        os.getenv("MINIO_ENDPOINT", "localhost:9000").replace("http://", "").replace("https://", ""),
        access_key=os.getenv("MINIO_ACCESS_KEY", "minioadmin"),
        secret_key=os.getenv("MINIO_SECRET_KEY", "minioadmin"),
        secure=os.getenv("MINIO_ENDPOINT", "").startswith("https"),
    )

def download_file(object_name, local_path):
    client = get_minio_client()
    bucket = os.getenv("MINIO_BUCKET", "marketlens-data")
    local_path = Path(local_path)
    local_path.parent.mkdir(parents=True, exist_ok=True)
    client.fget_object(bucket, object_name, str(local_path))
    return local_path

def upload_file(local_path, object_name):
    client = get_minio_client()
    bucket = os.getenv("MINIO_BUCKET", "marketlens-data")
    if not client.bucket_exists(bucket):
        client.make_bucket(bucket)
    client.fput_object(bucket, object_name, str(local_path))
