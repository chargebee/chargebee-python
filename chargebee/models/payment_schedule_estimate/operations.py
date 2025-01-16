from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class PaymentScheduleEstimate:

    env: environment.Environment

    class EntityType(Enum):
        INVOICE = "invoice"

        def __str__(self):
            return self.value

    class ScheduleEntryStatus(Enum):
        POSTED = "posted"
        PAYMENT_DUE = "payment_due"
        PAID = "paid"

        def __str__(self):
            return self.value

    class ScheduleEntry(TypedDict):
        id: Required[str]
        date: Required[int]
        amount: Required[int]
        status: Required["PaymentScheduleEstimate.ScheduleEntryStatus"]

    pass
