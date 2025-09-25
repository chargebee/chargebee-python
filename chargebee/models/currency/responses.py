from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class CurrencyResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    enabled: bool = None
    forex_type: str = None
    currency_code: str = None
    is_base_currency: bool = None
    manual_exchange_rate: str = None


@dataclass
class ListCurrencyResponse:
    currency: CurrencyResponse


@dataclass
class ListResponse(Response):
    list: List[ListCurrencyResponse]
    next_offset: str = None


@dataclass
class RetrieveResponse(Response):
    currency: CurrencyResponse


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    currency: CurrencyResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    currency: CurrencyResponse


@dataclass
class AddScheduleResponse(Response):
    is_idempotency_replayed: bool
    scheduled_at: int
    currency: CurrencyResponse


@dataclass
class RemoveScheduleResponse(Response):
    is_idempotency_replayed: bool
    scheduled_at: int
    currency: CurrencyResponse
