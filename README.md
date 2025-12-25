# 🚀 Kasparro Backend & ETL System

A production-style **Backend & ETL (Extract–Transform–Load) system** built using **FastAPI, PostgreSQL, Docker, and SQLAlchemy**.  
The system ingests data from **multiple sources**, normalizes it into a unified schema, stores it persistently, and exposes REST APIs for monitoring and data access.

---

## 📌 Project Overview

This project demonstrates the design and implementation of a **scalable backend system with an ETL pipeline**.

The backend:
- Fetches crypto market data from **public APIs**
- Reads structured data from **CSV files**
- Converts all incoming data into a **single unified format**
- Stores data in **PostgreSQL**
- Avoids duplicate data using **composite primary keys**
- Exposes REST APIs for health checks, data access, and ETL monitoring

The ETL pipeline runs **automatically on application startup**.

---

## 🧠 What is an ETL System? (Simple English)

An **ETL system** works in three steps:

1. **Extract** – Collect data from different sources (APIs, CSV files)
2. **Transform** – Convert the data into a common structure
3. **Load** – Store the transformed data into a database

In this project, crypto data from APIs and CSV files is processed, stored, and made available through REST APIs.

---

## 🔁 ETL Design Highlights

- **Multiple Data Sources**
  - CoinPaprika API
  - CoinGecko API
  - CSV file (`data.csv`)
  - CSV file (`data2.csv`)

- **Unified Schema**
  - All incoming data is normalized into a single structure

- **Incremental Processing**
  - Uses a `checkpoints` table to track the last processed timestamp

- **Idempotent Loads**
  - Duplicate records are prevented using composite primary keys
  - Duplicate inserts are safely ignored

- **Automatic Execution**
  - ETL pipeline runs when the backend starts

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Backend Framework:** FastAPI  
- **Database:** PostgreSQL  
- **ORM:** SQLAlchemy  
- **ETL Pipeline:** Custom Python ETL  
- **Containerization:** Docker, Docker Compose  
- **APIs Integrated:** CoinPaprika, CoinGecko  
- **Cloud Deployment:** Railway  

---

## 🌐 API Endpoints

### ✅ Health Check
Checks database connectivity and ETL execution status.

**Sample Response**
```json
{
  "db": "ok",
  "etl_last_run": "success"
}


### ✅ Data Check
{
  "request_id": "uuid",
  "api_latency_ms": 7,
  "data": [
    {
      "source": "coingecko",
      "record_id": "bitcoin",
      "value": 87781,
      "timestamp": "2025-12-25T22:26:40"
    }
  ]
}

### ✅ Stats Check
{
  "records_processed": "available via /data",
  "last_run": "on application startup",
  "sources": ["coinpaprika", "coingecko", "csv", "csv2"]
}

## ✅ Verification After Checking `/stats`

After validating the `/stats` endpoint, the following were confirmed:

- The **ETL pipeline executed successfully on application startup**
- Data was ingested from **multiple sources** (CoinPaprika, CoinGecko, CSV, CSV2)
- The backend correctly tracked **ETL execution metadata**
- The system is **stable across restarts** with duplicate-safe ingestion
- Data is persistently stored and accessible through the `/data` endpoint

This verification confirms that the backend, database, and ETL pipeline are functioning correctly as an integrated system.

