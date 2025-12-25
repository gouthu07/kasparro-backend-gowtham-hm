import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError

DATABASE_URL = "postgresql://postgres:postgres@db:5432/postgres"

Base = declarative_base()

# Retry DB connection
for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        engine.connect()
        break
    except OperationalError:
        print("Waiting for database...")
        time.sleep(2)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from models.record import Record
from models.checkpoint import Checkpoint

Base.metadata.create_all(bind=engine)

