from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import transaction


@dataclass
class ScheduleEntryResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    date: int = None
    amount: int = None
    scheduled_amount: int = None
    status: str = None


@dataclass
class ReferenceTransactionResponse(Model):
    raw_data: Dict[Any, Any] = None
    schedule_entry_id: str = None
    applied_amount: int = None
    txn_id: str = None
    txn_status: str = None
    txn_date: int = None
    txn_amount: int = None


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
    reference_transactions: List[ReferenceTransactionResponse] = None


@dataclass
class ListPaymentScheduleResponse:
    payment_schedule: PaymentScheduleResponse


@dataclass
class ListResponse(Response):
    list: List[ListPaymentScheduleResponse]
    next_offset: str = None
