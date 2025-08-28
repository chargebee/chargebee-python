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
    deleted: bool = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    attached_item: AttachedItemResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    attached_item: AttachedItemResponse


@dataclass
class RetrieveResponse(Response):
    attached_item: AttachedItemResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    attached_item: AttachedItemResponse


@dataclass
class ListAttachedItemResponse:
    attached_item: AttachedItemResponse


@dataclass
class ListResponse(Response):
    list: List[ListAttachedItemResponse]
    next_offset: str = None
