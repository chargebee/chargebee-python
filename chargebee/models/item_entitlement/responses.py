from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class ItemEntitlementResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    item_id: str = None
    item_type: str = None
    feature_id: str = None
    feature_name: str = None
    value: str = None
    name: str = None


@dataclass
class ItemEntitlementsForItemItemEntitlementResponse:
    item_entitlement: ItemEntitlementResponse


@dataclass
class ItemEntitlementsForItemResponse(Response):
    list: List[ItemEntitlementsForItemItemEntitlementResponse]
    next_offset: str = None


@dataclass
class ItemEntitlementsForFeatureItemEntitlementResponse:
    item_entitlement: ItemEntitlementResponse


@dataclass
class ItemEntitlementsForFeatureResponse(Response):
    list: List[ItemEntitlementsForFeatureItemEntitlementResponse]
    next_offset: str = None


@dataclass
class AddItemEntitlementsResponse(Response):
    is_idempotency_replayed: bool
    item_entitlement: ItemEntitlementResponse


@dataclass
class UpsertOrRemoveItemEntitlementsForItemResponse(Response):
    is_idempotency_replayed: bool
    item_entitlement: ItemEntitlementResponse
