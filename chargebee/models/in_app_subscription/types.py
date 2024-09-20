from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class StoreStatus(Enum):
    IN_TRIAL = "in_trial"
    ACTIVE = "active"
    CANCELLED = "cancelled"
    PAUSED = "paused"

    def __str__(self):
        return self.value


class ProcessReceiptProductParams(TypedDict):
    id: Required[str]
    currency_code: Required[str]
    price: Required[int]
    name: NotRequired[str]
    price_in_decimal: NotRequired[str]
    period: NotRequired[str]
    period_unit: NotRequired[str]


class ProcessReceiptCustomerParams(TypedDict):
    id: NotRequired[str]
    email: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]


class ImportReceiptProductParams(TypedDict):
    currency_code: Required[str]


class ImportReceiptCustomerParams(TypedDict):
    id: NotRequired[str]
    email: NotRequired[str]


class ImportSubscriptionSubscriptionParams(TypedDict):
    id: Required[str]
    started_at: Required[int]
    term_start: Required[int]
    term_end: Required[int]
    product_id: Required[str]
    currency_code: Required[str]
    transaction_id: Required[str]
    is_trial: NotRequired[bool]


class ImportSubscriptionCustomerParams(TypedDict):
    id: NotRequired[str]
    email: NotRequired[str]
