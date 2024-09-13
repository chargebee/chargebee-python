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


class PaymentVouchers(TypedDict):
    id: Required[str]
    id_at_gateway: NotRequired[str]
    payment_voucher_type: Required[enums.PaymentVoucherType]
    expires_at: NotRequired[int]
    status: NotRequired[Status]
    subscription_id: NotRequired[str]
    currency_code: Required[str]
    amount: NotRequired[int]
    gateway_account_id: NotRequired[str]
    payment_source_id: NotRequired[str]
    gateway: Required[enums.Gateway]
    payload: NotRequired[str]
    error_code: NotRequired[str]
    error_text: NotRequired[str]
    url: NotRequired[str]
    date: NotRequired[int]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    customer_id: Required[str]
    linked_invoices: NotRequired[List[LinkedInvoice]]


class CreateVoucherPaymentSourceParams(TypedDict):
    voucher_type: Required[enums.VoucherType]


class CreateInvoiceAllocationParams(TypedDict):
    invoice_id: Required[str]
