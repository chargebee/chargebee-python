from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class Status(Enum):
    POSTED = "posted"
    PAYMENT_DUE = "payment_due"
    PAID = "paid"

    def __str__(self):
        return self.value
