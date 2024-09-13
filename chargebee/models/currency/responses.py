from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


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
class ListResponse:
    currency: CurrencyResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveResponse:
    currency: CurrencyResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CreateResponse:
    currency: CurrencyResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class UpdateResponse:
    currency: CurrencyResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class AddScheduleResponse:
    scheduled_at: int
    currency: CurrencyResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RemoveScheduleResponse:
    scheduled_at: int
    currency: CurrencyResponse
    response_headers: Dict[Any, Any] = None
