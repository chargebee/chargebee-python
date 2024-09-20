from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums, credit_note, invoice, transaction


class Type(Enum):
    AUTHORIZATION = "authorization"
    PAYMENT = "payment"
    REFUND = "refund"
    PAYMENT_REVERSAL = "payment_reversal"

    def __str__(self):
        return self.value


class Status(Enum):
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    VOIDED = "voided"
    FAILURE = "failure"
    TIMEOUT = "timeout"
    NEEDS_ATTENTION = "needs_attention"

    def __str__(self):
        return self.value


class FraudFlag(Enum):
    SAFE = "safe"
    SUSPICIOUS = "suspicious"
    FRAUDULENT = "fraudulent"

    def __str__(self):
        return self.value


class InitiatorType(Enum):
    CUSTOMER = "customer"
    MERCHANT = "merchant"

    def __str__(self):
        return self.value


class AuthorizationReason(Enum):
    BLOCKING_FUNDS = "blocking_funds"
    VERIFICATION = "verification"

    def __str__(self):
        return self.value


class LinkedPaymentStatus(Enum):
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    VOIDED = "voided"
    FAILURE = "failure"
    TIMEOUT = "timeout"
    NEEDS_ATTENTION = "needs_attention"

    def __str__(self):
        return self.value


class LinkedInvoice(TypedDict):
    invoice_id: Required[str]
    applied_amount: Required[int]
    applied_at: Required[int]
    invoice_date: NotRequired[int]
    invoice_total: NotRequired[int]
    invoice_status: Required["invoice.Status"]


class LinkedCreditNote(TypedDict):
    cn_id: Required[str]
    applied_amount: Required[int]
    applied_at: Required[int]
    cn_reason_code: NotRequired["credit_note.ReasonCode"]
    cn_create_reason_code: NotRequired[str]
    cn_date: NotRequired[int]
    cn_total: NotRequired[int]
    cn_status: Required["credit_note.Status"]
    cn_reference_invoice_id: Required[str]


class LinkedRefund(TypedDict):
    txn_id: Required[str]
    txn_status: Required["transaction.Status"]
    txn_date: Required[int]
    txn_amount: Required[int]


class LinkedPayment(TypedDict):
    id: Required[str]
    status: NotRequired[LinkedPaymentStatus]
    amount: NotRequired[int]
    date: NotRequired[int]


class GatewayErrorDetail(TypedDict):
    request_id: NotRequired[str]
    error_category: NotRequired[str]
    error_code: NotRequired[str]
    error_message: NotRequired[str]
    decline_code: NotRequired[str]
    decline_message: NotRequired[str]
    network_error_code: NotRequired[str]
    network_error_message: NotRequired[str]
    error_field: NotRequired[str]
    recommendation_code: NotRequired[str]
    recommendation_message: NotRequired[str]
    processor_error_code: NotRequired[str]
    processor_error_message: NotRequired[str]
