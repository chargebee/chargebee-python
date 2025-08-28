from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import business_entity_transfer


@dataclass
class BusinessEntityResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    status: str = None
    deleted: bool = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None


@dataclass
class CreateTransfersResponse(Response):
    is_idempotency_replayed: bool
    business_entity_transfer: "business_entity_transfer.BusinessEntityTransferResponse"


@dataclass
class GetTransfersBusinessEntityResponse:
    business_entity_transfer: "business_entity_transfer.BusinessEntityTransferResponse"


@dataclass
class GetTransfersResponse(Response):
    list: List[GetTransfersBusinessEntityResponse]
    next_offset: str = None
