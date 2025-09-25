from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import enums


@dataclass
class QuotedRamp:
    env: environment.Environment

    class DiscountType(Enum):
        FIXED_AMOUNT = "fixed_amount"
        PERCENTAGE = "percentage"

        def __str__(self):
            return self.value

    class DiscountEntityType(Enum):
        ITEM_LEVEL_COUPON = "item_level_coupon"
        DOCUMENT_LEVEL_COUPON = "document_level_coupon"
        ITEM_LEVEL_DISCOUNT = "item_level_discount"
        DOCUMENT_LEVEL_DISCOUNT = "document_level_discount"

        def __str__(self):
            return self.value

    class LineItem(TypedDict):
        item_price_id: Required[str]
        item_type: Required[enums.ItemType]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        metered_quantity: NotRequired[str]
        unit_price: NotRequired[int]
        unit_price_in_decimal: NotRequired[str]
        amount: NotRequired[int]
        amount_in_decimal: NotRequired[str]
        billing_period: NotRequired[int]
        billing_period_unit: NotRequired["QuotedRamp.BillingPeriodUnit"]
        free_quantity: NotRequired[int]
        free_quantity_in_decimal: NotRequired[str]
        billing_cycles: NotRequired[int]
        service_period_days: NotRequired[int]
        charge_on_event: NotRequired[enums.ChargeOnEvent]
        charge_once: NotRequired[bool]
        charge_on_option: NotRequired[enums.ChargeOnOption]
        start_date: NotRequired[int]
        end_date: NotRequired[int]
        ramp_tier_id: NotRequired[str]
        discount_per_billing_cycle: NotRequired[int]
        discount_per_billing_cycle_in_decimal: NotRequired[str]
        item_level_discount_per_billing_cycle: NotRequired[int]
        item_level_discount_per_billing_cycle_in_decimal: NotRequired[str]
        amount_per_billing_cycle: NotRequired[int]
        amount_per_billing_cycle_in_decimal: NotRequired[str]
        net_amount_per_billing_cycle: NotRequired[int]
        net_amount_per_billing_cycle_in_decimal: NotRequired[str]

    class Discount(TypedDict):
        id: Required[str]
        invoice_name: NotRequired[str]
        type: Required["QuotedRamp.DiscountType"]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        duration_type: Required[enums.DurationType]
        entity_type: Required["QuotedRamp.DiscountEntityType"]
        entity_id: NotRequired[str]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: Required[bool]
        apply_on: Required[enums.ApplyOn]
        item_price_id: NotRequired[str]
        created_at: Required[int]
        updated_at: NotRequired[int]
        start_date: NotRequired[int]
        end_date: NotRequired[int]

    class ItemTier(TypedDict):
        item_price_id: Required[str]
        starting_unit: Required[int]
        ending_unit: NotRequired[int]
        price: Required[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        ramp_tier_id: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

    class CouponApplicabilityMapping(TypedDict):
        coupon_id: NotRequired[str]
        applicable_item_price_ids: NotRequired[List[str]]

    pass
