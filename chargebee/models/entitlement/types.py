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


class CreateEntitlementParams(TypedDict):
    entity_id: Required[str]
    feature_id: Required[str]
    entity_type: NotRequired[EntityType]
    value: NotRequired[str]
