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
