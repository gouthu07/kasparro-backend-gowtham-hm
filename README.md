# Kasparro Backend & ETL System

## Overview
This project is a Dockerized backend and ETL system that ingests data from multiple sources,
normalizes it into a unified schema, stores it in PostgreSQL, and exposes REST APIs for data access
and system monitoring.

The system is designed as a small production-style backend with incremental ingestion
and cloud deployment.

---

## How the System Works (Simple Explanation)

1. Data is collected from multiple sources:
   - One API source
   - Two CSV files

2. An ETL (Extract, Transform, Load) process:
   - Extracts data from all sources
   - Transforms and cleans the data into a common format
   - Loads the processed data into PostgreSQL

3. Incremental ingestion:
   - The system stores checkpoints for each source
   - Only new data is processed on the next run
   - Prevents duplicate data and supports safe restarts

4. A backend API exposes endpoints to:
   - Check system health
   - Fetch stored data
   - View ETL statistics

5. The entire application runs inside Docker and is deployed on the cloud.

---

## Tech Stack / Tools Used

- **Programming Language:** Python  
- **Backend Framework:** FastAPI  
- **Database:** PostgreSQL  
- **Database Access:** SQLAlchemy  
- **Data Validation:** Pydantic  
- **ETL Processing:** Custom Python ETL pipeline  
- **API Communication:** REST APIs  
- **Containerization:** Docker, Docker Compose  
- **Testing:** Pytest  
- **Cloud Deployment:** Railway  

---

## Features
- Multi-source data ingestion (API + CSV)
- Unified schema normalization
- Incremental ETL using checkpoints
- REST APIs with metadata
- Fully Dockerized setup
- Public cloud deployment

---

## API Endpoints

### GET /health
Checks whether the system is running correctly.
It verifies database connectivity and reports the last ETL execution status.

Example response:
```json
{
  "db": "ok",
  "etl_last_run": "success"
}
