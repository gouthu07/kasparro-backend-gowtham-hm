from datetime import datetime
from sqlalchemy import text
from core.database import engine
from schemas.unified import UnifiedRecord
from ingestion.csv_source import fetch_csv_data, fetch_csv2_data


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


def run_etl(api_data, csv_data):
    records = []

    api_checkpoint = get_last_checkpoint("api")
    csv_checkpoint = get_last_checkpoint("csv")

    # -------- API SOURCE --------
    for r in api_data:
        ts = datetime.fromisoformat(r["timestamp"])
        if api_checkpoint and ts <= api_checkpoint:
            continue

        records.append(UnifiedRecord(
            source="api",
            record_id=str(r["id"]),
            value=float(r["value"]),
            timestamp=ts
        ))

    # -------- CSV SOURCE --------
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

    # -------- CSV2 SOURCE (THIRD SOURCE) --------
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
        api_records = [r.timestamp for r in records if r.source == "api"]
        csv_records = [r.timestamp for r in records if r.source == "csv"]

        if api_records:
            update_checkpoint("api", max(api_records))
        if csv_records:
            update_checkpoint("csv", max(csv_records))

    return records
