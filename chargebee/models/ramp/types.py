from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


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


class CouponsToAdd(TypedDict):
    coupon_id: Required[str]
    apply_till: NotRequired[int]


class DiscountsToAdd(TypedDict):
    id: Required[str]
    invoice_name: NotRequired[str]
    type: Required[DiscountsToAddType]
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
    index: Required[int]


class StatusTransitionReason(TypedDict):
    code: NotRequired[str]
    message: NotRequired[str]


class Ramps(TypedDict):
    id: Required[str]
    description: NotRequired[str]
    subscription_id: Required[str]
    effective_from: Required[int]
    status: Required[Status]
    created_at: Required[int]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    items_to_add: NotRequired[List[ItemsToAdd]]
    items_to_update: NotRequired[List[ItemsToUpdate]]
    coupons_to_add: NotRequired[List[CouponsToAdd]]
    discounts_to_add: NotRequired[List[DiscountsToAdd]]
    item_tiers: NotRequired[List[ItemTier]]
    items_to_remove: NotRequired[List[str]]
    coupons_to_remove: NotRequired[List[str]]
    discounts_to_remove: NotRequired[List[str]]
    deleted: Required[bool]
    status_transition_reason: NotRequired[StatusTransitionReason]


class CreateForSubscriptionItemsToAddParams(TypedDict):
    item_price_id: Required[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]
    service_period_days: NotRequired[int]


class CreateForSubscriptionItemsToUpdateParams(TypedDict):
    item_price_id: Required[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]
    service_period_days: NotRequired[int]


class CreateForSubscriptionItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


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


class UpdateItemsToAddParams(TypedDict):
    item_price_id: Required[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]
    service_period_days: NotRequired[int]


class UpdateItemsToUpdateParams(TypedDict):
    item_price_id: Required[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]
    service_period_days: NotRequired[int]


class UpdateItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


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
