from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


@dataclass
class Coupon:

    env: environment.Environment

    class DiscountType(Enum):
        FIXED_AMOUNT = "fixed_amount"
        PERCENTAGE = "percentage"
        OFFER_QUANTITY = "offer_quantity"

        def __str__(self):
            return self.value

    class DurationType(Enum):
        ONE_TIME = "one_time"
        FOREVER = "forever"
        LIMITED_PERIOD = "limited_period"

        def __str__(self):
            return self.value

    class Status(Enum):
        ACTIVE = "active"
        EXPIRED = "expired"
        ARCHIVED = "archived"
        DELETED = "deleted"
        FUTURE = "future"

        def __str__(self):
            return self.value

    class ApplyDiscountOn(Enum):
        PLANS = "plans"
        PLANS_AND_ADDONS = "plans_and_addons"
        PLANS_WITH_QUANTITY = "plans_with_quantity"
        NOT_APPLICABLE = "not_applicable"

        def __str__(self):
            return self.value

    class ApplyOn(Enum):
        INVOICE_AMOUNT = "invoice_amount"
        EACH_SPECIFIED_ITEM = "each_specified_item"

        def __str__(self):
            return self.value

    class AddonConstraint(Enum):
        NONE = "none"
        ALL = "all"
        SPECIFIC = "specific"
        NOT_APPLICABLE = "not_applicable"

        def __str__(self):
            return self.value

    class PlanConstraint(Enum):
        NONE = "none"
        ALL = "all"
        SPECIFIC = "specific"
        NOT_APPLICABLE = "not_applicable"

        def __str__(self):
            return self.value

    class ItemConstraintItemType(Enum):
        PLAN = "plan"
        ADDON = "addon"
        CHARGE = "charge"

        def __str__(self):
            return self.value

    class ItemConstraintConstraint(Enum):
        NONE = "none"
        ALL = "all"
        SPECIFIC = "specific"
        CRITERIA = "criteria"

        def __str__(self):
            return self.value

    class ItemConstraintCriteriaItemType(Enum):
        PLAN = "plan"
        ADDON = "addon"
        CHARGE = "charge"

        def __str__(self):
            return self.value

    class CouponConstraintEntityType(Enum):
        CUSTOMER = "customer"

        def __str__(self):
            return self.value

    class CouponConstraintType(Enum):
        MAX_REDEMPTIONS = "max_redemptions"
        UNIQUE_BY = "unique_by"
        EXISTING_CUSTOMER = "existing_customer"
        NEW_CUSTOMER = "new_customer"

        def __str__(self):
            return self.value

    class ItemConstraint(TypedDict):
        item_type: Required["Coupon.ItemConstraintItemType"]
        constraint: Required["Coupon.ItemConstraintConstraint"]
        item_price_ids: NotRequired[List[Dict[Any, Any]]]

    class ItemConstraintCriteria(TypedDict):
        item_type: Required["Coupon.ItemConstraintCriteriaItemType"]
        currencies: NotRequired[List[Dict[Any, Any]]]
        item_family_ids: NotRequired[List[Dict[Any, Any]]]
        item_price_periods: NotRequired[List[Dict[Any, Any]]]

    class CouponConstraint(TypedDict):
        entity_type: Required["Coupon.CouponConstraintEntityType"]
        type: Required["Coupon.CouponConstraintType"]
        value: NotRequired[str]

    class CreateForItemsItemConstraintParams(TypedDict):
        constraint: Required["Coupon.ItemConstraintConstraint"]
        item_type: Required["Coupon.ItemConstraintItemType"]
        item_price_ids: NotRequired[List[Dict[Any, Any]]]

    class CreateForItemsItemConstraintCriteriaParams(TypedDict):
        item_type: NotRequired["Coupon.ItemConstraintCriteriaItemType"]
        item_family_ids: NotRequired[List[Dict[Any, Any]]]
        currencies: NotRequired[List[Dict[Any, Any]]]
        item_price_periods: NotRequired[List[Dict[Any, Any]]]

    class CreateForItemsCouponConstraintParams(TypedDict):
        entity_type: Required["Coupon.CouponConstraintEntityType"]
        type: Required["Coupon.CouponConstraintType"]
        value: NotRequired[str]

    class UpdateForItemsItemConstraintParams(TypedDict):
        constraint: Required["Coupon.ItemConstraintConstraint"]
        item_type: Required["Coupon.ItemConstraintItemType"]
        item_price_ids: NotRequired[List[Dict[Any, Any]]]

    class UpdateForItemsItemConstraintCriteriaParams(TypedDict):
        item_type: NotRequired["Coupon.ItemConstraintCriteriaItemType"]
        item_family_ids: NotRequired[List[Dict[Any, Any]]]
        currencies: NotRequired[List[Dict[Any, Any]]]
        item_price_periods: NotRequired[List[Dict[Any, Any]]]

    class UpdateForItemsCouponConstraintParams(TypedDict):
        entity_type: Required["Coupon.CouponConstraintEntityType"]
        type: Required["Coupon.CouponConstraintType"]
        value: NotRequired[str]

    class CreateParams(TypedDict):
        id: Required[str]
        name: Required[str]
        invoice_name: NotRequired[str]
        discount_type: NotRequired["Coupon.DiscountType"]
        discount_amount: NotRequired[int]
        currency_code: NotRequired[str]
        discount_percentage: NotRequired[float]
        discount_quantity: NotRequired[int]
        apply_on: Required["Coupon.ApplyOn"]
        duration_type: NotRequired["Coupon.DurationType"]
        duration_month: NotRequired[int]
        valid_till: NotRequired[int]
        max_redemptions: NotRequired[int]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        included_in_mrr: NotRequired[bool]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        plan_constraint: NotRequired["Coupon.PlanConstraint"]
        addon_constraint: NotRequired["Coupon.AddonConstraint"]
        plan_ids: NotRequired[List[str]]
        addon_ids: NotRequired[List[str]]
        status: NotRequired["Coupon.Status"]

    class CreateForItemsParams(TypedDict):
        id: Required[str]
        name: Required[str]
        invoice_name: NotRequired[str]
        discount_type: NotRequired["Coupon.DiscountType"]
        discount_amount: NotRequired[int]
        currency_code: NotRequired[str]
        discount_percentage: NotRequired[float]
        discount_quantity: NotRequired[int]
        apply_on: Required["Coupon.ApplyOn"]
        duration_type: NotRequired["Coupon.DurationType"]
        duration_month: NotRequired[int]
        valid_from: NotRequired[int]
        valid_till: NotRequired[int]
        max_redemptions: NotRequired[int]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        included_in_mrr: NotRequired[bool]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        item_constraints: Required[List["Coupon.CreateForItemsItemConstraintParams"]]
        item_constraint_criteria: NotRequired[
            List["Coupon.CreateForItemsItemConstraintCriteriaParams"]
        ]
        status: NotRequired["Coupon.Status"]
        coupon_constraints: Required[
            List["Coupon.CreateForItemsCouponConstraintParams"]
        ]

    class UpdateForItemsParams(TypedDict):
        name: NotRequired[str]
        invoice_name: NotRequired[str]
        discount_type: NotRequired["Coupon.DiscountType"]
        discount_amount: NotRequired[int]
        currency_code: NotRequired[str]
        discount_percentage: NotRequired[float]
        discount_quantity: NotRequired[int]
        apply_on: NotRequired["Coupon.ApplyOn"]
        duration_type: NotRequired["Coupon.DurationType"]
        duration_month: NotRequired[int]
        valid_from: NotRequired[int]
        valid_till: NotRequired[int]
        max_redemptions: NotRequired[int]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        included_in_mrr: NotRequired[bool]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        item_constraints: Required[List["Coupon.UpdateForItemsItemConstraintParams"]]
        item_constraint_criteria: NotRequired[
            List["Coupon.UpdateForItemsItemConstraintCriteriaParams"]
        ]
        coupon_constraints: Required[
            List["Coupon.UpdateForItemsCouponConstraintParams"]
        ]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        name: NotRequired[Filters.StringFilter]
        discount_type: NotRequired[Filters.EnumFilter]
        duration_type: NotRequired[Filters.EnumFilter]
        status: NotRequired[Filters.EnumFilter]
        apply_on: NotRequired[Filters.EnumFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]
        currency_code: NotRequired[Filters.StringFilter]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        invoice_name: NotRequired[str]
        discount_type: NotRequired["Coupon.DiscountType"]
        discount_amount: NotRequired[int]
        currency_code: NotRequired[str]
        discount_percentage: NotRequired[float]
        discount_quantity: NotRequired[int]
        apply_on: NotRequired["Coupon.ApplyOn"]
        duration_type: NotRequired["Coupon.DurationType"]
        duration_month: NotRequired[int]
        valid_till: NotRequired[int]
        max_redemptions: NotRequired[int]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        included_in_mrr: NotRequired[bool]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        plan_constraint: NotRequired["Coupon.PlanConstraint"]
        addon_constraint: NotRequired["Coupon.AddonConstraint"]
        plan_ids: NotRequired[List[str]]
        addon_ids: NotRequired[List[str]]

    class CopyParams(TypedDict):
        from_site: Required[str]
        id_at_from_site: Required[str]
        id: NotRequired[str]
        for_site_merging: NotRequired[bool]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {
            "meta_data": 0,
        }
        return request.send(
            "post",
            request.uri_path("coupons"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
        )

    def create_for_items(
        self, params: CreateForItemsParams, headers=None
    ) -> CreateForItemsResponse:
        jsonKeys = {
            "meta_data": 0,
            "item_price_ids": 1,
            "item_family_ids": 1,
            "currencies": 1,
            "item_price_periods": 1,
        }
        return request.send(
            "post",
            request.uri_path("coupons", "create_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateForItemsResponse,
            None,
            False,
            jsonKeys,
        )

    def update_for_items(
        self, id, params: UpdateForItemsParams, headers=None
    ) -> UpdateForItemsResponse:
        jsonKeys = {
            "meta_data": 0,
            "item_price_ids": 1,
            "item_family_ids": 1,
            "currencies": 1,
            "item_price_periods": 1,
        }
        return request.send(
            "post",
            request.uri_path("coupons", id, "update_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateForItemsResponse,
            None,
            False,
            jsonKeys,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        return request.send_list_request(
            "get",
            request.uri_path("coupons"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("coupons", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
        )

    def update(self, id, params: UpdateParams = None, headers=None) -> UpdateResponse:
        jsonKeys = {
            "meta_data": 0,
        }
        return request.send(
            "post",
            request.uri_path("coupons", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("coupons", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
        )

    def copy(self, params: CopyParams, headers=None) -> CopyResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("coupons", "copy"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CopyResponse,
            None,
            False,
            jsonKeys,
        )

    def unarchive(self, id, headers=None) -> UnarchiveResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("coupons", id, "unarchive"),
            self.env,
            None,
            headers,
            UnarchiveResponse,
            None,
            False,
            jsonKeys,
        )
