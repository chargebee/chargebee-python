from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class TierResponse(Model):
    raw_data: Dict[Any, Any] = None
    starting_unit: int = None
    ending_unit: int = None
    price: int = None
    starting_unit_in_decimal: str = None
    ending_unit_in_decimal: str = None
    price_in_decimal: str = None
    pricing_type: str = None
    package_size: int = None


@dataclass
class ParentPeriodResponse(Model):
    raw_data: Dict[Any, Any] = None
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
    business_entity_id: str = None
    deleted: bool = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    differential_price: DifferentialPriceResponse


@dataclass
class RetrieveResponse(Response):

    differential_price: DifferentialPriceResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    differential_price: DifferentialPriceResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    differential_price: DifferentialPriceResponse


@dataclass
class ListDifferentialPriceResponse:
    differential_price: DifferentialPriceResponse


@dataclass
class ListResponse(Response):

    list: List[ListDifferentialPriceResponse]
    next_offset: str = None
