from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class TierResponse(Model):
    starting_unit: int = None
    ending_unit: int = None
    price: int = None
    starting_unit_in_decimal: str = None
    ending_unit_in_decimal: str = None
    price_in_decimal: str = None


@dataclass
class ParentPeriodResponse(Model):
    period_unit: str = None
    period: List[Dict[Any, Any]] = None


@dataclass
class DifferentialPriceResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    item_price_id: str = None
    parent_item_id: str = None
    price: int = None
    price_in_decimal: str = None
    status: str = None
    resource_version: int = None
    updated_at: int = None
    created_at: int = None
    modified_at: int = None
    tiers: List[TierResponse] = None
    currency_code: str = None
    parent_periods: List[ParentPeriodResponse] = None


@dataclass
class CreateResponse:
    differential_price: DifferentialPriceResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveResponse:
    differential_price: DifferentialPriceResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class UpdateResponse:
    differential_price: DifferentialPriceResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class DeleteResponse:
    differential_price: DifferentialPriceResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ListDifferentialPriceResponse:
    differential_price: DifferentialPriceResponse


@dataclass
class ListResponse:
    list: List[ListDifferentialPriceResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None
