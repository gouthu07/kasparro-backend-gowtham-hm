from fastapi import FastAPI
from sqlalchemy import text
import time
import uuid

from core.database import engine
from ingestion.etl_runner import run_etl

app = FastAPI(title="Kasparro Backend & ETL System")


# ---------------- STARTUP EVENT ----------------
@app.on_event("startup")
def startup_event():
    """
    Runs ETL when the application starts.
    Ensures database is ready before execution.
    """
    # small delay to ensure DB readiness (extra safety)
    time.sleep(2)
    run_etl()


# ---------------- HEALTH CHECK ----------------
@app.get("/health")
def health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {
            "db": "ok",
            "etl_last_run": "success"
        }
    except Exception as e:
        return {
            "db": "error",
            "error": str(e)
        }


# ---------------- DATA ENDPOINT ----------------
@app.get("/data")
def get_data():
    start_time = time.time()

    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT source, record_id, symbol, value, timestamp
            FROM records
            ORDER BY timestamp DESC
            LIMIT 50
        """))

        rows = [
            {
                "source": r.source,
                "record_id": r.record_id,
                "symbol": r.symbol,
                "value": r.value,
                "timestamp": r.timestamp.isoformat()
            }
            for r in result
        ]

    return {
        "request_id": str(uuid.uuid4()),
        "api_latency_ms": int((time.time() - start_time) * 1000),
        "data": rows
    }


# ---------------- ETL STATS ----------------
@app.get("/stats")
def stats():
    return {
        "records_processed": "available via /data",
        "last_run": "on application startup",
        "sources": ["coinpaprika", "coingecko", "csv", "csv2"]
    }
