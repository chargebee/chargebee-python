from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class PreferredScheduleResponse(Model):
    raw_data: Dict[Any, Any] = None
    period: int = None
    amount_percentage: float = None


@dataclass
class PaymentScheduleSchemeResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    description: str = None
    number_of_schedules: int = None
    period_unit: str = None
    period: int = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None
    preferred_schedules: List[PreferredScheduleResponse] = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    payment_schedule_scheme: PaymentScheduleSchemeResponse


@dataclass
class RetrieveResponse(Response):
    payment_schedule_scheme: PaymentScheduleSchemeResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    payment_schedule_scheme: PaymentScheduleSchemeResponse
