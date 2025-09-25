from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


@dataclass
class Item:
    env: environment.Environment

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
        is_percentage_pricing: NotRequired[bool]
        metadata: NotRequired[Dict[Any, Any]]
        business_entity_id: NotRequired[str]
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
        is_percentage_pricing: NotRequired[bool]
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
        business_entity_id: NotRequired[Filters.StringFilter]
        include_site_level_resources: NotRequired[Filters.BooleanFilter]
        sort_by: NotRequired[Filters.SortFilter]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {
            "metadata": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("items", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update(self, id, params: UpdateParams = None, headers=None) -> UpdateResponse:
        jsonKeys = {
            "metadata": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("items", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("items", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
        )
