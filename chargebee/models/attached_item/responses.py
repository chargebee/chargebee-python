from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class AttachedItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    parent_item_id: str = None
    item_id: str = None
    type: str = None
    status: str = None
    quantity: int = None
    quantity_in_decimal: str = None
    billing_cycles: int = None
    charge_on_event: str = None
    charge_once: bool = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None
    channel: str = None
    business_entity_id: str = None


@dataclass
class CreateResponse(Response):
    attached_item: AttachedItemResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateResponse(Response):
    attached_item: AttachedItemResponse
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    attached_item: AttachedItemResponse
    headers: Dict[str, str] = None


@dataclass
class DeleteResponse(Response):
    attached_item: AttachedItemResponse
    headers: Dict[str, str] = None


@dataclass
class ListAttachedItemResponse:
    attached_item: AttachedItemResponse


@dataclass
class ListResponse:
    list: List[ListAttachedItemResponse]
    next_offset: str = None
    headers: Dict[str, str] = None
