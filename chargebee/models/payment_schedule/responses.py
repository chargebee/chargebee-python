from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class ScheduleEntryResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    date: int = None
    amount: int = None
    status: str = None


@dataclass
class PaymentScheduleResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    scheme_id: str = None
    entity_type: str = None
    entity_id: str = None
    amount: int = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None
    currency_code: str = None
    schedule_entries: List[ScheduleEntryResponse] = None
