from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


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
    response_headers: Dict[Any, Any] = None


@dataclass
class CreateResponse:
    entitlement: EntitlementResponse
    response_headers: Dict[Any, Any] = None
