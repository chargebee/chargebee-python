from typing import TypedDict, Required, NotRequired, Dict, List, Any
from chargebee.models import enums


class Charge(TypedDict):
    amount: NotRequired[int]
    amount_in_decimal: NotRequired[str]
    description: NotRequired[str]
    service_period_in_days: NotRequired[int]
    avalara_sale_type: NotRequired[enums.AvalaraSaleType]
    avalara_transaction_type: NotRequired[int]
    avalara_service_type: NotRequired[int]


class InvoiceItem(TypedDict):
    item_price_id: Required[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    service_period_days: NotRequired[int]


class ItemTier(TypedDict):
    item_price_id: Required[str]
    starting_unit: Required[int]
    ending_unit: NotRequired[int]
    price: Required[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]
    index: Required[int]


class Coupon(TypedDict):
    coupon_id: Required[str]


class Addon(TypedDict):
    id: Required[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    proration_type: NotRequired[enums.ProrationType]
    service_period: NotRequired[int]


class QuotedCharges(TypedDict):
    charges: NotRequired[List[Charge]]
    addons: NotRequired[List[Addon]]
    invoice_items: NotRequired[List[InvoiceItem]]
    item_tiers: NotRequired[List[ItemTier]]
    coupons: NotRequired[List[Coupon]]
