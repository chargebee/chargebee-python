from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Type(Enum):
    FIXED_AMOUNT = "fixed_amount"
    PERCENTAGE = "percentage"

    def __str__(self):
        return self.value


class Discounts(TypedDict):
    id: Required[str]
    invoice_name: NotRequired[str]
    type: Required[Type]
    percentage: NotRequired[float]
    amount: NotRequired[int]
    currency_code: NotRequired[str]
    duration_type: Required[enums.DurationType]
    period: NotRequired[int]
    period_unit: NotRequired[enums.PeriodUnit]
    included_in_mrr: Required[bool]
    apply_on: Required[enums.ApplyOn]
    item_price_id: NotRequired[str]
    created_at: Required[int]
    apply_till: NotRequired[int]
    applied_count: NotRequired[int]
    coupon_id: Required[str]
    index: Required[int]
