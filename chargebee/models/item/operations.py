from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


class Item:
    class Status(Enum):
        ACTIVE = "active"
        ARCHIVED = "archived"
        DELETED = "deleted"

        def __str__(self):
            return self.value

    class Type(Enum):
        PLAN = "plan"
        ADDON = "addon"
        CHARGE = "charge"

        def __str__(self):
            return self.value

    class ItemApplicability(Enum):
        ALL = "all"
        RESTRICTED = "restricted"

        def __str__(self):
            return self.value

    class UsageCalculation(Enum):
        SUM_OF_USAGES = "sum_of_usages"
        LAST_USAGE = "last_usage"
        MAX_USAGE = "max_usage"

        def __str__(self):
            return self.value

    class BundleConfigurationType(Enum):
        FIXED = "fixed"

        def __str__(self):
            return self.value

    class ApplicableItem(TypedDict):
        id: NotRequired[str]

    class BundleItem(TypedDict):
        item_id: Required[str]
        item_type: NotRequired[enums.ItemType]
        quantity: NotRequired[int]
        price_allocation: NotRequired[float]

    class BundleConfiguration(TypedDict):
        type: NotRequired["Item.BundleConfigurationType"]

    class CreateBundleConfigurationParams(TypedDict):
        type: NotRequired["Item.BundleConfigurationType"]

    class CreateBundleItemsToAddParams(TypedDict):
        item_id: NotRequired[str]
        item_type: NotRequired[enums.ItemType]
        quantity: NotRequired[int]
        price_allocation: NotRequired[float]

    class UpdateBundleConfigurationParams(TypedDict):
        type: NotRequired["Item.BundleConfigurationType"]

    class UpdateBundleItemsToAddParams(TypedDict):
        item_id: NotRequired[str]
        item_type: NotRequired[enums.ItemType]
        quantity: NotRequired[int]
        price_allocation: NotRequired[float]

    class UpdateBundleItemsToUpdateParams(TypedDict):
        item_id: NotRequired[str]
        item_type: NotRequired[enums.ItemType]
        quantity: NotRequired[int]
        price_allocation: NotRequired[float]

    class UpdateBundleItemsToRemoveParams(TypedDict):
        item_id: NotRequired[str]
        item_type: NotRequired[enums.ItemType]

    class ListBundleConfigurationParams(TypedDict):
        type: NotRequired[Filters.EnumFilter]

    class CreateParams(TypedDict):
        id: Required[str]
        name: Required[str]
        type: Required["Item.Type"]
        description: NotRequired[str]
        item_family_id: Required[str]
        is_giftable: NotRequired[bool]
        is_shippable: NotRequired[bool]
        external_name: NotRequired[str]
        enabled_in_portal: NotRequired[bool]
        redirect_url: NotRequired[str]
        enabled_for_checkout: NotRequired[bool]
        item_applicability: NotRequired["Item.ItemApplicability"]
        applicable_items: NotRequired[List[str]]
        bundle_configuration: NotRequired["Item.CreateBundleConfigurationParams"]
        unit: NotRequired[str]
        gift_claim_redirect_url: NotRequired[str]
        included_in_mrr: NotRequired[bool]
        metered: NotRequired[bool]
        usage_calculation: NotRequired["Item.UsageCalculation"]
        metadata: NotRequired[Dict[Any, Any]]
        bundle_items_to_add: NotRequired[List["Item.CreateBundleItemsToAddParams"]]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        description: NotRequired[str]
        is_shippable: NotRequired[bool]
        external_name: NotRequired[str]
        item_family_id: NotRequired[str]
        enabled_in_portal: NotRequired[bool]
        redirect_url: NotRequired[str]
        enabled_for_checkout: NotRequired[bool]
        item_applicability: NotRequired["Item.ItemApplicability"]
        clear_applicable_items: NotRequired[bool]
        applicable_items: NotRequired[List[str]]
        bundle_configuration: NotRequired["Item.UpdateBundleConfigurationParams"]
        unit: NotRequired[str]
        gift_claim_redirect_url: NotRequired[str]
        metadata: NotRequired[Dict[Any, Any]]
        included_in_mrr: NotRequired[bool]
        status: NotRequired["Item.Status"]
        bundle_items_to_add: NotRequired[List["Item.UpdateBundleItemsToAddParams"]]
        bundle_items_to_update: NotRequired[
            List["Item.UpdateBundleItemsToUpdateParams"]
        ]
        bundle_items_to_remove: NotRequired[
            List["Item.UpdateBundleItemsToRemoveParams"]
        ]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        bundle_configuration: NotRequired["Item.ListBundleConfigurationParams"]
        id: NotRequired[Filters.StringFilter]
        item_family_id: NotRequired[Filters.StringFilter]
        type: NotRequired[Filters.EnumFilter]
        name: NotRequired[Filters.StringFilter]
        item_applicability: NotRequired[Filters.EnumFilter]
        status: NotRequired[Filters.EnumFilter]
        is_giftable: NotRequired[Filters.BooleanFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        enabled_for_checkout: NotRequired[Filters.BooleanFilter]
        enabled_in_portal: NotRequired[Filters.BooleanFilter]
        metered: NotRequired[Filters.BooleanFilter]
        usage_calculation: NotRequired[Filters.EnumFilter]
        channel: NotRequired[Filters.EnumFilter]
        sort_by: NotRequired[Filters.SortFilter]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get", request.uri_path("items", id), None, env, headers, RetrieveResponse
        )

    @staticmethod
    def update(
        id, params: UpdateParams = None, env=None, headers=None
    ) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("items", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("items", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )
