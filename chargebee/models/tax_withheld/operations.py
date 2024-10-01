from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


class TaxWithheld:
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

    pass
