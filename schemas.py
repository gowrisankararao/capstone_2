from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


class AlertCreate(BaseModel):
    title: str
    severity: Literal["critical", "warning", "info"]
    source: str
    metric_name: str
    metric_value: float
    threshold: float


class AlertOut(AlertCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ExplainResponse(BaseModel):
    alert_id: int
    explanation: str
    generated_at: datetime
