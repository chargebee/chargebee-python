from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class InstallmentStatus(Enum):
    POSTED = "posted"
    PAYMENT_DUE = "payment_due"
    PAID = "paid"

    def __str__(self):
        return self.value


class Installment(TypedDict):
    id: Required[str]
    invoice_id: Required[str]
    date: Required[int]
    amount: Required[int]
    status: Required[InstallmentStatus]
    created_at: Required[int]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
