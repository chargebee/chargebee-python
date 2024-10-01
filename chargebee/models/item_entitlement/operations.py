from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import enums


class ItemEntitlement:
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

    @staticmethod
    def item_entitlements_for_item(
        id, params: ItemEntitlementsForItemParams = None, env=None, headers=None
    ) -> ItemEntitlementsForItemResponse:
        return request.send(
            "get",
            request.uri_path("items", id, "item_entitlements"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ItemEntitlementsForItemResponse,
        )

    @staticmethod
    def item_entitlements_for_feature(
        id, params: ItemEntitlementsForFeatureParams = None, env=None, headers=None
    ) -> ItemEntitlementsForFeatureResponse:
        return request.send(
            "get",
            request.uri_path("features", id, "item_entitlements"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ItemEntitlementsForFeatureResponse,
        )

    @staticmethod
    def add_item_entitlements(
        id, params: AddItemEntitlementsParams, env=None, headers=None
    ) -> AddItemEntitlementsResponse:
        return request.send(
            "post",
            request.uri_path("features", id, "item_entitlements"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AddItemEntitlementsResponse,
        )

    @staticmethod
    def upsert_or_remove_item_entitlements_for_item(
        id, params: UpsertOrRemoveItemEntitlementsForItemParams, env=None, headers=None
    ) -> UpsertOrRemoveItemEntitlementsForItemResponse:
        return request.send(
            "post",
            request.uri_path("items", id, "item_entitlements"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpsertOrRemoveItemEntitlementsForItemResponse,
        )
