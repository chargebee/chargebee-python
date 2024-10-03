from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class PreferredScheduleResponse(Model):
    period: int = None
    amount_percentage: float = None


@dataclass
class PaymentScheduleSchemeResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    description: str = None
    number_of_schedules: int = None
    period_unit: str = None
    period: int = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None
    preferred_schedules: List[PreferredScheduleResponse] = None


@dataclass
class CreateResponse:
    payment_schedule_scheme: PaymentScheduleSchemeResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveResponse:
    payment_schedule_scheme: PaymentScheduleSchemeResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class DeleteResponse:
    payment_schedule_scheme: PaymentScheduleSchemeResponse
    response_headers: Dict[Any, Any] = None
