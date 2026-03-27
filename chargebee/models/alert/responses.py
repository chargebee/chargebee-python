from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class AlertResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    type: str = None
    name: str = None
    description: str = None
    metered_feature_id: str = None
    subscription_id: str = None
    status: str = None
    alarm_triggered_at: int = None
    scope: str = None
    meta: str = None
    created_at: int = None
    updated_at: int = None
