from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class ItemType(Enum):
    PLAN = "plan"
    ADDON = "addon"
    CHARGE = "charge"
    SUBSCRIPTION = "subscription"
    ITEM = "item"

    def __str__(self):
        return self.value


class ItemEntitlements(TypedDict):
    id: Required[str]
    item_id: NotRequired[str]
    item_type: NotRequired[ItemType]
    feature_id: NotRequired[str]
    feature_name: NotRequired[str]
    value: NotRequired[str]
    name: NotRequired[str]


class AddItemEntitlementsItemEntitlementParams(TypedDict):
    item_id: Required[str]
    item_type: NotRequired[ItemType]
    value: NotRequired[str]


class UpsertOrRemoveItemEntitlementsForItemItemEntitlementParams(TypedDict):
    feature_id: Required[str]
    value: NotRequired[str]
