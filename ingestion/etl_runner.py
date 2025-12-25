from datetime import datetime
from sqlalchemy import text
from core.database import engine
from schemas.unified import UnifiedRecord
from ingestion.csv_source import fetch_csv_data, fetch_csv2_data
from ingestion.coinpaprika_source import fetch_coinpaprika_data
from ingestion.coingecko_source import fetch_coingecko_data
from core.database import SessionLocal
from models.record import Record



def get_last_checkpoint(source):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT last_timestamp FROM checkpoints WHERE source = :s"),
            {"s": source}
        ).fetchone()
        return result[0] if result else None


def update_checkpoint(source, timestamp):
    with engine.connect() as conn:
        conn.execute(text("""
            INSERT INTO checkpoints (source, last_timestamp)
            VALUES (:s, :t)
            ON CONFLICT (source)
            DO UPDATE SET last_timestamp = EXCLUDED.last_timestamp
        """), {"s": source, "t": timestamp})


def run_etl():
    records = []

    # -------- COIN API SOURCES --------
    coinpaprika_data = fetch_coinpaprika_data()
    coingecko_data = fetch_coingecko_data()

    for r in coinpaprika_data + coingecko_data:
        records.append(UnifiedRecord(
            source=r["source"],
            record_id=r["id"],
            symbol=r["symbol"],
            value=float(r["price"]),
            timestamp=datetime.fromisoformat(r["timestamp"])
        ))

    # -------- CSV SOURCE --------
    csv_checkpoint = get_last_checkpoint("csv")
    csv_data = fetch_csv_data()

    for r in csv_data:
        ts = datetime.fromisoformat(r["timestamp"])
        if csv_checkpoint and ts <= csv_checkpoint:
            continue

        records.append(UnifiedRecord(
            source="csv",
            record_id=r["id"],
            value=float(r["value"]),
            timestamp=ts
        ))

    # -------- CSV2 SOURCE --------
    csv2_data = fetch_csv2_data()

    for r in csv2_data:
        records.append(UnifiedRecord(
            source="csv2",
            record_id=r["id"],
            value=float(r["value"]),
            timestamp=datetime.fromisoformat(r["timestamp"])
        ))

    # -------- UPDATE CHECKPOINTS --------
    if records:
        csv_times = [r.timestamp for r in records if r.source == "csv"]
        if csv_times:
            update_checkpoint("csv", max(csv_times))

    if records:
        db = SessionLocal()
        try:
            for r in records:
                db.add(Record(**r.dict()))
            db.commit()
        finally:
            db.close()

    return records
