from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class Coupon:

    class CreateParams(TypedDict):
        id: Required[str]
        name: Required[str]
        invoice_name: NotRequired[str]
        discount_type: NotRequired[DiscountType]
        discount_amount: NotRequired[int]
        currency_code: NotRequired[str]
        discount_percentage: NotRequired[float]
        discount_quantity: NotRequired[int]
        apply_on: Required[ApplyOn]
        duration_type: NotRequired[DurationType]
        duration_month: NotRequired[int]
        valid_till: NotRequired[int]
        max_redemptions: NotRequired[int]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        included_in_mrr: NotRequired[bool]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        plan_constraint: NotRequired[PlanConstraint]
        addon_constraint: NotRequired[AddonConstraint]
        plan_ids: NotRequired[List[str]]
        addon_ids: NotRequired[List[str]]
        status: NotRequired[Status]

    class CreateForItemsParams(TypedDict):
        id: Required[str]
        name: Required[str]
        invoice_name: NotRequired[str]
        discount_type: NotRequired[DiscountType]
        discount_amount: NotRequired[int]
        currency_code: NotRequired[str]
        discount_percentage: NotRequired[float]
        discount_quantity: NotRequired[int]
        apply_on: Required[ApplyOn]
        duration_type: NotRequired[DurationType]
        duration_month: NotRequired[int]
        valid_till: NotRequired[int]
        max_redemptions: NotRequired[int]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        included_in_mrr: NotRequired[bool]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        item_constraints: Required[List[CreateForItemsItemConstraintParams]]
        item_constraint_criteria: NotRequired[
            List[CreateForItemsItemConstraintCriteriaParams]
        ]
        status: NotRequired[Status]
        coupon_constraints: Required[List[CreateForItemsCouponConstraintParams]]

    class UpdateForItemsParams(TypedDict):
        name: NotRequired[str]
        invoice_name: NotRequired[str]
        discount_type: NotRequired[DiscountType]
        discount_amount: NotRequired[int]
        currency_code: NotRequired[str]
        discount_percentage: NotRequired[float]
        discount_quantity: NotRequired[int]
        apply_on: NotRequired[ApplyOn]
        duration_type: NotRequired[DurationType]
        duration_month: NotRequired[int]
        valid_till: NotRequired[int]
        max_redemptions: NotRequired[int]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        included_in_mrr: NotRequired[bool]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        item_constraints: Required[List[UpdateForItemsItemConstraintParams]]
        item_constraint_criteria: NotRequired[
            List[UpdateForItemsItemConstraintCriteriaParams]
        ]
        coupon_constraints: Required[List[UpdateForItemsCouponConstraintParams]]

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
        discount_type: NotRequired[DiscountType]
        discount_amount: NotRequired[int]
        currency_code: NotRequired[str]
        discount_percentage: NotRequired[float]
        discount_quantity: NotRequired[int]
        apply_on: NotRequired[ApplyOn]
        duration_type: NotRequired[DurationType]
        duration_month: NotRequired[int]
        valid_till: NotRequired[int]
        max_redemptions: NotRequired[int]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        included_in_mrr: NotRequired[bool]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        plan_constraint: NotRequired[PlanConstraint]
        addon_constraint: NotRequired[AddonConstraint]
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
