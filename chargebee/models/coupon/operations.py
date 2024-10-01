from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


class Coupon:
    class DiscountType(Enum):
        FIXED_AMOUNT = "fixed_amount"
        PERCENTAGE = "percentage"

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

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("coupons"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def create_for_items(
        params: CreateForItemsParams, env=None, headers=None
    ) -> CreateForItemsResponse:
        return request.send(
            "post",
            request.uri_path("coupons", "create_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateForItemsResponse,
        )

    @staticmethod
    def update_for_items(
        id, params: UpdateForItemsParams, env=None, headers=None
    ) -> UpdateForItemsResponse:
        return request.send(
            "post",
            request.uri_path("coupons", id, "update_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateForItemsResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("coupons"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get", request.uri_path("coupons", id), None, env, headers, RetrieveResponse
        )

    @staticmethod
    def update(
        id, params: UpdateParams = None, env=None, headers=None
    ) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("coupons", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("coupons", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def copy(params: CopyParams, env=None, headers=None) -> CopyResponse:
        return request.send(
            "post",
            request.uri_path("coupons", "copy"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CopyResponse,
        )

    @staticmethod
    def unarchive(id, env=None, headers=None) -> UnarchiveResponse:
        return request.send(
            "post",
            request.uri_path("coupons", id, "unarchive"),
            None,
            env,
            headers,
            UnarchiveResponse,
        )
