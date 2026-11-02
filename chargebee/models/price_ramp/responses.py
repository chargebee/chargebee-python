from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class RampIntervalResponse(Model):
    raw_data: Dict[Any, Any] = None
    starting_billing_cycle: int = None
    ending_billing_cycle: int = None
    apply_catalog_price: bool = None
    price: int = None
    price_in_decimal: str = None


@dataclass
class PriceRampResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    item_price_id: str = None
    status: str = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None
    archived_at: int = None
    ramp_intervals: List[RampIntervalResponse] = None
    business_entity_id: str = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    price_ramp: PriceRampResponse


@dataclass
class RetrieveResponse(Response):
    price_ramp: PriceRampResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    price_ramp: PriceRampResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    price_ramp: PriceRampResponse


@dataclass
class ListPriceRampResponse:
    price_ramp: PriceRampResponse


@dataclass
class ListResponse(Response):
    list: List[ListPriceRampResponse]
    next_offset: str = None
