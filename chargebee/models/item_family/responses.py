from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class ItemFamilyResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    description: str = None
    status: str = None
    resource_version: int = None
    updated_at: int = None
    channel: str = None
    business_entity_id: str = None
    deleted: bool = None


@dataclass
class CreateResponse(Response):
    item_family: ItemFamilyResponse
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    item_family: ItemFamilyResponse
    headers: Dict[str, str] = None


@dataclass
class ListItemFamilyResponse:
    item_family: ItemFamilyResponse


@dataclass
class ListResponse:
    list: List[ListItemFamilyResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class UpdateResponse(Response):
    item_family: ItemFamilyResponse
    headers: Dict[str, str] = None


@dataclass
class DeleteResponse(Response):
    item_family: ItemFamilyResponse
    headers: Dict[str, str] = None
