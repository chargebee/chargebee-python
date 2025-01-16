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
class ListResponse:
    currency: CurrencyResponse
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    currency: CurrencyResponse
    headers: Dict[str, str] = None


@dataclass
class CreateResponse(Response):
    currency: CurrencyResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateResponse(Response):
    currency: CurrencyResponse
    headers: Dict[str, str] = None


@dataclass
class AddScheduleResponse(Response):
    scheduled_at: int
    currency: CurrencyResponse
    headers: Dict[str, str] = None


@dataclass
class RemoveScheduleResponse(Response):
    scheduled_at: int
    currency: CurrencyResponse
    headers: Dict[str, str] = None
