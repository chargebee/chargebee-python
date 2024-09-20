from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Status(Enum):
    ACTIVE = "active"
    CONSUMED = "consumed"
    EXPIRED = "expired"
    FAILURE = "failure"

    def __str__(self):
        return self.value


class LinkedInvoice(TypedDict):
    invoice_id: Required[str]
    txn_id: Required[str]
    applied_at: Required[int]


class CreateVoucherPaymentSourceParams(TypedDict):
    voucher_type: Required[enums.VoucherType]


class CreateInvoiceAllocationParams(TypedDict):
    invoice_id: Required[str]
