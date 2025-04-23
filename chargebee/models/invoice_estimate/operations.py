from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import enums


@dataclass
class InvoiceEstimate:

    env: environment.Environment

    class LineItemEntityType(Enum):
        ADHOC = "adhoc"
        PLAN_ITEM_PRICE = "plan_item_price"
        ADDON_ITEM_PRICE = "addon_item_price"
        CHARGE_ITEM_PRICE = "charge_item_price"
        PLAN_SETUP = "plan_setup"
        PLAN = "plan"
        ADDON = "addon"

        def __str__(self):
            return self.value

    class DiscountEntityType(Enum):
        ITEM_LEVEL_COUPON = "item_level_coupon"
        DOCUMENT_LEVEL_COUPON = "document_level_coupon"
        PROMOTIONAL_CREDITS = "promotional_credits"
        PRORATED_CREDITS = "prorated_credits"
        ITEM_LEVEL_DISCOUNT = "item_level_discount"
        DOCUMENT_LEVEL_DISCOUNT = "document_level_discount"

        def __str__(self):
            return self.value

    class DiscountDiscountType(Enum):
        FIXED_AMOUNT = "fixed_amount"
        PERCENTAGE = "percentage"

        def __str__(self):
            return self.value

    class LineItemDiscountDiscountType(Enum):
        ITEM_LEVEL_COUPON = "item_level_coupon"
        DOCUMENT_LEVEL_COUPON = "document_level_coupon"
        PROMOTIONAL_CREDITS = "promotional_credits"
        PRORATED_CREDITS = "prorated_credits"
        ITEM_LEVEL_DISCOUNT = "item_level_discount"
        DOCUMENT_LEVEL_DISCOUNT = "document_level_discount"

        def __str__(self):
            return self.value

    class LineItem(TypedDict):
        id: NotRequired[str]
        subscription_id: NotRequired[str]
        date_from: Required[int]
        date_to: Required[int]
        unit_amount: Required[int]
        quantity: NotRequired[int]
        amount: NotRequired[int]
        pricing_model: NotRequired[enums.PricingModel]
        is_taxed: Required[bool]
        tax_amount: NotRequired[int]
        tax_rate: NotRequired[float]
        unit_amount_in_decimal: NotRequired[str]
        quantity_in_decimal: NotRequired[str]
        amount_in_decimal: NotRequired[str]
        discount_amount: NotRequired[int]
        item_level_discount_amount: NotRequired[int]
        metered: NotRequired[bool]
        percentage: NotRequired[str]
        reference_line_item_id: NotRequired[str]
        description: Required[str]
        entity_description: NotRequired[str]
        entity_type: Required["InvoiceEstimate.LineItemEntityType"]
        tax_exempt_reason: NotRequired[enums.TaxExemptReason]
        entity_id: NotRequired[str]
        customer_id: NotRequired[str]

    class Discount(TypedDict):
        amount: Required[int]
        description: NotRequired[str]
        entity_type: Required["InvoiceEstimate.DiscountEntityType"]
        discount_type: NotRequired["InvoiceEstimate.DiscountDiscountType"]
        entity_id: NotRequired[str]
        coupon_set_code: NotRequired[str]

    class Tax(TypedDict):
        name: Required[str]
        amount: Required[int]
        description: NotRequired[str]

    class LineItemTax(TypedDict):
        line_item_id: NotRequired[str]
        tax_name: Required[str]
        tax_rate: Required[float]
        date_to: NotRequired[int]
        date_from: NotRequired[int]
        prorated_taxable_amount: NotRequired[float]
        is_partial_tax_applied: NotRequired[bool]
        is_non_compliance_tax: NotRequired[bool]
        taxable_amount: Required[int]
        tax_amount: Required[int]
        tax_juris_type: NotRequired[enums.TaxJurisType]
        tax_juris_name: NotRequired[str]
        tax_juris_code: NotRequired[str]
        tax_amount_in_local_currency: NotRequired[int]
        local_currency_code: NotRequired[str]

    class LineItemTier(TypedDict):
        line_item_id: NotRequired[str]
        starting_unit: Required[int]
        ending_unit: NotRequired[int]
        quantity_used: Required[int]
        unit_amount: Required[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        quantity_used_in_decimal: NotRequired[str]
        unit_amount_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

    class LineItemCredit(TypedDict):
        cn_id: Required[str]
        applied_amount: Required[float]
        line_item_id: NotRequired[str]

    class LineItemDiscount(TypedDict):
        line_item_id: Required[str]
        discount_type: Required["InvoiceEstimate.LineItemDiscountDiscountType"]
        coupon_id: NotRequired[str]
        entity_id: NotRequired[str]
        discount_amount: Required[int]

    class LineItemAddress(TypedDict):
        line_item_id: NotRequired[str]
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        email: NotRequired[str]
        company: NotRequired[str]
        phone: NotRequired[str]
        line1: NotRequired[str]
        line2: NotRequired[str]
        line3: NotRequired[str]
        city: NotRequired[str]
        state_code: NotRequired[str]
        state: NotRequired[str]
        country: NotRequired[str]
        zip: NotRequired[str]
        validation_status: NotRequired[enums.ValidationStatus]

    pass
