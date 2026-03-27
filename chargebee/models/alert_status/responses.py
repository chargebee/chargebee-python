from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class AlertStatusResponse(Model):
    raw_data: Dict[Any, Any] = None
    alert_id: str = None
    subscription_id: str = None
    alert_status: str = None
    alarm_triggered_at: int = None
