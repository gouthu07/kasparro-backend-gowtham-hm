# Kasparro Backend & ETL System

## Overview
This project implements a simple backend and ETL system that ingests data from multiple sources,
normalizes them into a unified schema, and exposes REST APIs.

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- Docker

## Features
- API and CSV ingestion
- Incremental ETL using checkpoints
- Unified schema
- REST APIs with metadata

## Run Locally
```bash
docker compose up --build
