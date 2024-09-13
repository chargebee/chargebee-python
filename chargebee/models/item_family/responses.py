from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


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


@dataclass
class CreateResponse:
    item_family: ItemFamilyResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveResponse:
    item_family: ItemFamilyResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ListItemFamilyResponse:
    item_family: ItemFamilyResponse


@dataclass
class ListResponse:
    list: List[ListItemFamilyResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None


@dataclass
class UpdateResponse:
    item_family: ItemFamilyResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class DeleteResponse:
    item_family: ItemFamilyResponse
    response_headers: Dict[Any, Any] = None
