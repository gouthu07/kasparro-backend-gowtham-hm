from sqlalchemy import Column, String, Float, DateTime
from core.database import Base

class Record(Base):
    __tablename__ = "records"

    source = Column(String, primary_key=True)
    record_id = Column(String, primary_key=True)
    symbol = Column(String, nullable=True)
    value = Column(Float)
    timestamp = Column(DateTime)
