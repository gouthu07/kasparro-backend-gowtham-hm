from pydantic import BaseModel
from datetime import datetime

class UnifiedRecord(BaseModel):
    source: str
    record_id: str
    value: float
    timestamp: datetime
