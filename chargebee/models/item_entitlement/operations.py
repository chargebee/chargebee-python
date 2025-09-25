from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import enums


@dataclass
class ItemEntitlement:
    env: environment.Environment

    class ItemType(Enum):
        PLAN = "plan"
        ADDON = "addon"
        CHARGE = "charge"
        SUBSCRIPTION = "subscription"
        ITEM = "item"

        def __str__(self):
            return self.value

    class AddItemEntitlementsItemEntitlementParams(TypedDict):
        item_id: Required[str]
        item_type: NotRequired["ItemEntitlement.ItemType"]
        value: NotRequired[str]

    class UpsertOrRemoveItemEntitlementsForItemItemEntitlementParams(TypedDict):
        feature_id: Required[str]
        value: NotRequired[str]

    class ItemEntitlementsForItemParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        include_drafts: NotRequired[bool]
        embed: NotRequired[str]

    class ItemEntitlementsForFeatureParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        include_drafts: NotRequired[bool]

    class AddItemEntitlementsParams(TypedDict):
        action: Required[enums.Action]
        item_entitlements: Required[
            List["ItemEntitlement.AddItemEntitlementsItemEntitlementParams"]
        ]

    class UpsertOrRemoveItemEntitlementsForItemParams(TypedDict):
        action: Required[enums.Action]
        item_entitlements: Required[
            List[
                "ItemEntitlement.UpsertOrRemoveItemEntitlementsForItemItemEntitlementParams"
            ]
        ]

    def item_entitlements_for_item(
        self, id, params: ItemEntitlementsForItemParams = None, headers=None
    ) -> ItemEntitlementsForItemResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("items", id, "item_entitlements"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ItemEntitlementsForItemResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def item_entitlements_for_feature(
        self, id, params: ItemEntitlementsForFeatureParams = None, headers=None
    ) -> ItemEntitlementsForFeatureResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("features", id, "item_entitlements"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ItemEntitlementsForFeatureResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def add_item_entitlements(
        self, id, params: AddItemEntitlementsParams, headers=None
    ) -> AddItemEntitlementsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("features", id, "item_entitlements"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AddItemEntitlementsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def upsert_or_remove_item_entitlements_for_item(
        self, id, params: UpsertOrRemoveItemEntitlementsForItemParams, headers=None
    ) -> UpsertOrRemoveItemEntitlementsForItemResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("items", id, "item_entitlements"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpsertOrRemoveItemEntitlementsForItemResponse,
            None,
            False,
            jsonKeys,
            options,
        )
