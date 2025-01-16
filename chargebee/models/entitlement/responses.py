from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class EntitlementResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    entity_id: str = None
    entity_type: str = None
    feature_id: str = None
    feature_name: str = None
    value: str = None
    name: str = None


@dataclass
class ListEntitlementResponse:
    entitlement: EntitlementResponse


@dataclass
class ListResponse:
    list: List[ListEntitlementResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class CreateResponse(Response):
    entitlement: EntitlementResponse
    headers: Dict[str, str] = None
