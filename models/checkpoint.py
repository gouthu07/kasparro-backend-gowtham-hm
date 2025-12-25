from sqlalchemy import Column, String, DateTime
from core.database import Base

class Checkpoint(Base):
    __tablename__ = "checkpoints"

    source = Column(String, primary_key=True)
    last_timestamp = Column(DateTime)
