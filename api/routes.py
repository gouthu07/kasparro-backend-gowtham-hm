from fastapi import APIRouter
import time
import uuid

router = APIRouter()

@router.get("/health")
def health():
    return {
        "db": "ok",
        "etl_last_run": "success"
    }

@router.get("/data")
def get_data(limit: int = 10, offset: int = 0):
    start = time.time()
    return {
        "request_id": str(uuid.uuid4()),
        "api_latency_ms": int((time.time() - start) * 1000),
        "data": []
    }

@router.get("/stats")
def stats():
    return {
        "records_processed": 0,
        "duration_ms": 0,
        "last_success": "2025-12-25T17:00:00",
        "last_failure": None,
        "run_metadata": {
            "mode": "incremental",
            "sources": ["api", "csv"]
        }
    }
