from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


@dataclass
class Ramp:
    env: environment.Environment

    class Status(Enum):
        SCHEDULED = "scheduled"
        SUCCEEDED = "succeeded"
        FAILED = "failed"
        DRAFT = "draft"

        def __str__(self):
            return self.value

    class DiscountsToAddType(Enum):
        FIXED_AMOUNT = "fixed_amount"
        PERCENTAGE = "percentage"

        def __str__(self):
            return self.value

    class ContractTermActionAtTermEnd(Enum):
        RENEW = "renew"
        EVERGREEN = "evergreen"
        CANCEL = "cancel"
        RENEW_ONCE = "renew_once"

        def __str__(self):
            return self.value

    class ItemsToAdd(TypedDict):
        item_price_id: Required[str]
        item_type: Required[enums.ItemType]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        unit_price: NotRequired[int]
        unit_price_in_decimal: NotRequired[str]
        amount: NotRequired[int]
        amount_in_decimal: NotRequired[str]
        free_quantity: NotRequired[int]
        free_quantity_in_decimal: NotRequired[str]
        billing_cycles: NotRequired[int]
        service_period_days: NotRequired[int]
        metered_quantity: NotRequired[str]
        charge_once: NotRequired[bool]
        charge_on_option: NotRequired[enums.ChargeOnOption]
        charge_on_event: NotRequired[enums.ChargeOnEvent]

    class ItemsToUpdate(TypedDict):
        item_price_id: Required[str]
        item_type: Required[enums.ItemType]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        unit_price: NotRequired[int]
        unit_price_in_decimal: NotRequired[str]
        amount: NotRequired[int]
        amount_in_decimal: NotRequired[str]
        free_quantity: NotRequired[int]
        free_quantity_in_decimal: NotRequired[str]
        billing_cycles: NotRequired[int]
        service_period_days: NotRequired[int]
        metered_quantity: NotRequired[str]
        charge_once: NotRequired[bool]
        charge_on_option: NotRequired[enums.ChargeOnOption]
        charge_on_event: NotRequired[enums.ChargeOnEvent]

    class CouponsToAdd(TypedDict):
        coupon_id: Required[str]
        apply_till: NotRequired[int]

    class DiscountsToAdd(TypedDict):
        id: Required[str]
        invoice_name: NotRequired[str]
        type: Required["Ramp.DiscountsToAddType"]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        duration_type: Required[enums.DurationType]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: Required[bool]
        apply_on: Required[enums.ApplyOn]
        item_price_id: NotRequired[str]
        created_at: Required[int]

    class ItemTier(TypedDict):
        item_price_id: Required[str]
        starting_unit: Required[int]
        ending_unit: NotRequired[int]
        price: Required[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]
        index: Required[int]

    class ContractTerm(TypedDict):
        cancellation_cutoff_period: NotRequired[int]
        renewal_billing_cycles: NotRequired[int]
        action_at_term_end: Required["Ramp.ContractTermActionAtTermEnd"]

    class StatusTransitionReason(TypedDict):
        code: NotRequired[str]
        message: NotRequired[str]

    class CreateForSubscriptionItemsToAddParams(TypedDict):
        item_price_id: Required[str]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        unit_price: NotRequired[int]
        unit_price_in_decimal: NotRequired[str]
        billing_cycles: NotRequired[int]
        service_period_days: NotRequired[int]
        charge_on_event: NotRequired[enums.ChargeOnEvent]
        charge_once: NotRequired[bool]
        charge_on_option: NotRequired[enums.ChargeOnOption]

    class CreateForSubscriptionItemsToUpdateParams(TypedDict):
        item_price_id: Required[str]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        unit_price: NotRequired[int]
        unit_price_in_decimal: NotRequired[str]
        billing_cycles: NotRequired[int]
        service_period_days: NotRequired[int]
        charge_on_event: NotRequired[enums.ChargeOnEvent]
        charge_once: NotRequired[bool]
        charge_on_option: NotRequired[enums.ChargeOnOption]

    class CreateForSubscriptionItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

    class CreateForSubscriptionCouponsToAddParams(TypedDict):
        coupon_id: NotRequired[str]
        apply_till: NotRequired[int]

    class CreateForSubscriptionDiscountsToAddParams(TypedDict):
        apply_on: Required[enums.ApplyOn]
        duration_type: Required[enums.DurationType]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: NotRequired[bool]
        item_price_id: NotRequired[str]

    class CreateForSubscriptionContractTermParams(TypedDict):
        action_at_term_end: NotRequired["Ramp.ContractTermActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]
        renewal_billing_cycles: NotRequired[int]

    class UpdateItemsToAddParams(TypedDict):
        item_price_id: Required[str]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        unit_price: NotRequired[int]
        unit_price_in_decimal: NotRequired[str]
        billing_cycles: NotRequired[int]
        service_period_days: NotRequired[int]
        charge_on_event: NotRequired[enums.ChargeOnEvent]
        charge_once: NotRequired[bool]
        charge_on_option: NotRequired[enums.ChargeOnOption]

    class UpdateItemsToUpdateParams(TypedDict):
        item_price_id: Required[str]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        unit_price: NotRequired[int]
        unit_price_in_decimal: NotRequired[str]
        billing_cycles: NotRequired[int]
        service_period_days: NotRequired[int]
        charge_on_event: NotRequired[enums.ChargeOnEvent]
        charge_once: NotRequired[bool]
        charge_on_option: NotRequired[enums.ChargeOnOption]

    class UpdateItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

    class UpdateCouponsToAddParams(TypedDict):
        coupon_id: NotRequired[str]
        apply_till: NotRequired[int]

    class UpdateDiscountsToAddParams(TypedDict):
        apply_on: Required[enums.ApplyOn]
        duration_type: Required[enums.DurationType]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: NotRequired[bool]
        item_price_id: NotRequired[str]

    class UpdateContractTermParams(TypedDict):
        action_at_term_end: NotRequired["Ramp.ContractTermActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]
        renewal_billing_cycles: NotRequired[int]

    class CreateForSubscriptionParams(TypedDict):
        effective_from: Required[int]
        description: NotRequired[str]
        coupons_to_remove: NotRequired[List[str]]
        discounts_to_remove: NotRequired[List[str]]
        items_to_remove: NotRequired[List[str]]
        items_to_add: Required[List["Ramp.CreateForSubscriptionItemsToAddParams"]]
        items_to_update: Required[List["Ramp.CreateForSubscriptionItemsToUpdateParams"]]
        item_tiers: NotRequired[List["Ramp.CreateForSubscriptionItemTierParams"]]
        coupons_to_add: NotRequired[
            List["Ramp.CreateForSubscriptionCouponsToAddParams"]
        ]
        discounts_to_add: Required[
            List["Ramp.CreateForSubscriptionDiscountsToAddParams"]
        ]
        contract_term: NotRequired["Ramp.CreateForSubscriptionContractTermParams"]

    class UpdateParams(TypedDict):
        effective_from: Required[int]
        description: NotRequired[str]
        coupons_to_remove: NotRequired[List[str]]
        discounts_to_remove: NotRequired[List[str]]
        items_to_remove: NotRequired[List[str]]
        items_to_add: Required[List["Ramp.UpdateItemsToAddParams"]]
        items_to_update: Required[List["Ramp.UpdateItemsToUpdateParams"]]
        item_tiers: NotRequired[List["Ramp.UpdateItemTierParams"]]
        coupons_to_add: NotRequired[List["Ramp.UpdateCouponsToAddParams"]]
        discounts_to_add: Required[List["Ramp.UpdateDiscountsToAddParams"]]
        contract_term: NotRequired["Ramp.UpdateContractTermParams"]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        include_deleted: NotRequired[bool]
        status: NotRequired[Filters.EnumFilter]
        subscription_id: Required[Filters.StringFilter]
        effective_from: NotRequired[Filters.TimestampFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]

    def create_for_subscription(
        self, id, params: CreateForSubscriptionParams, headers=None
    ) -> CreateForSubscriptionResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "create_ramp"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateForSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update(self, id, params: UpdateParams, headers=None) -> UpdateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("ramps", id, "update"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
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
            request.uri_path("ramps", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
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
            request.uri_path("ramps", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def list(self, params: ListParams, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("ramps"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )
