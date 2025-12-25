# 🚀 Kasparro Backend & ETL System

A **Backend & ETL system** built using **FastAPI, PostgreSQL, Docker, and SQLAlchemy**.  
The application ingests crypto data from multiple sources, normalizes it into a unified format, stores it in a database, and exposes REST APIs for monitoring and access.

---

## 📌 Project Flow (Simple)

- **Extract:** Fetches data from CoinPaprika API, CoinGecko API, and CSV files  
- **Transform:** Converts all incoming data into a single unified schema  
- **Load:** Stores data in PostgreSQL while preventing duplicate records  
- The ETL pipeline runs **automatically on application startup**

---

## 🌐 API Endpoints

### `/health`
Checks database connectivity and confirms successful ETL execution.

### `/data`
Returns the latest ingested and normalized records from the database.

### `/stats`
Provides metadata about ETL execution and the data sources used.

---

## ✅ Conclusion

This project demonstrates a complete backend system with a reliable ETL pipeline, multi-source data ingestion, duplicate-safe storage, and REST APIs for monitoring and data access.
