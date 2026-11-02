from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class ActionLogResponse(Model):
    raw_data: Dict[Any, Any] = None
    action_type: str = None
    status: str = None
    reason_code: str = None
    executed_at: int = None
    scheduled_at: int = None


@dataclass
class CollectionsReminderSequenceResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    invoice_id: str = None
    customer_id: str = None
    status: str = None
    paused_until: int = None
    pause_note: str = None
    started_at: int = None
    completed_at: int = None
    created_at: int = None
    updated_at: int = None
    resource_version: int = None
    action_logs: List[ActionLogResponse] = None
