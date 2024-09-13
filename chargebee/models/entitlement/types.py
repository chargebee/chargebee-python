from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class EntityType(Enum):
    PLAN = "plan"
    ADDON = "addon"
    CHARGE = "charge"
    PLAN_PRICE = "plan_price"
    ADDON_PRICE = "addon_price"

    def __str__(self):
        return self.value


class Entitlements(TypedDict):
    id: Required[str]
    entity_id: NotRequired[str]
    entity_type: NotRequired[EntityType]
    feature_id: NotRequired[str]
    feature_name: NotRequired[str]
    value: NotRequired[str]
    name: NotRequired[str]


class CreateEntitlementParams(TypedDict):
    entity_id: Required[str]
    feature_id: Required[str]
    entity_type: NotRequired[EntityType]
    value: NotRequired[str]
