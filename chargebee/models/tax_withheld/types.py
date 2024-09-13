from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class Type(Enum):
    PAYMENT = "payment"
    REFUND = "refund"

    def __str__(self):
        return self.value


class PaymentMethod(Enum):
    CASH = "cash"
    CHECK = "check"
    CHARGEBACK = "chargeback"
    BANK_TRANSFER = "bank_transfer"
    OTHER = "other"

    def __str__(self):
        return self.value


class TaxWithhelds(TypedDict):
    id: Required[str]
    user: NotRequired[str]
    reference_number: NotRequired[str]
    description: NotRequired[str]
    type: Required[Type]
    payment_method: Required[PaymentMethod]
    date: NotRequired[int]
    currency_code: Required[str]
    amount: NotRequired[int]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    exchange_rate: NotRequired[float]
