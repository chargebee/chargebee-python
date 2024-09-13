from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


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
class ItemEntitlementsForItemResponse:
    list: List[ItemEntitlementsForItemItemEntitlementResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None


@dataclass
class ItemEntitlementsForFeatureItemEntitlementResponse:
    item_entitlement: ItemEntitlementResponse


@dataclass
class ItemEntitlementsForFeatureResponse:
    list: List[ItemEntitlementsForFeatureItemEntitlementResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None


@dataclass
class AddItemEntitlementsResponse:
    item_entitlement: ItemEntitlementResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class UpsertOrRemoveItemEntitlementsForItemResponse:
    item_entitlement: ItemEntitlementResponse
    response_headers: Dict[Any, Any] = None
