from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class AttributeResponse(Model):
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


@dataclass
class CreateResponse(Response):
    price_variant: PriceVariantResponse
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    price_variant: PriceVariantResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateResponse(Response):
    price_variant: PriceVariantResponse
    headers: Dict[str, str] = None


@dataclass
class DeleteResponse(Response):
    price_variant: PriceVariantResponse
    headers: Dict[str, str] = None


@dataclass
class ListPriceVariantResponse:
    price_variant: PriceVariantResponse


@dataclass
class ListResponse:
    list: List[ListPriceVariantResponse]
    next_offset: str = None
    headers: Dict[str, str] = None
