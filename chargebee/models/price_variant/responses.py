from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class AttributeResponse(Model):
    raw_data: Dict[Any, Any] = None
    name: str = None
    value: str = None


@dataclass
class PriceVariantResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    external_name: str = None
    variant_group: str = None
    description: str = None
    status: str = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None
    archived_at: int = None
    attributes: List[AttributeResponse] = None
    business_entity_id: str = None
    deleted: bool = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    price_variant: PriceVariantResponse


@dataclass
class RetrieveResponse(Response):

    price_variant: PriceVariantResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    price_variant: PriceVariantResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    price_variant: PriceVariantResponse


@dataclass
class ListPriceVariantResponse:
    price_variant: PriceVariantResponse


@dataclass
class ListResponse(Response):

    list: List[ListPriceVariantResponse]
    next_offset: str = None
