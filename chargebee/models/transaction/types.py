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


class Transactions(TypedDict):
    id: Required[str]
    customer_id: NotRequired[str]
    subscription_id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    payment_source_id: NotRequired[str]
    payment_method: Required[enums.PaymentMethod]
    reference_number: NotRequired[str]
    gateway: Required[enums.Gateway]
    type: Required[Type]
    date: NotRequired[int]
    settled_at: NotRequired[int]
    exchange_rate: NotRequired[float]
    currency_code: Required[str]
    amount: NotRequired[int]
    id_at_gateway: NotRequired[str]
    status: NotRequired[Status]
    fraud_flag: NotRequired[FraudFlag]
    initiator_type: NotRequired[InitiatorType]
    three_d_secure: NotRequired[bool]
    authorization_reason: NotRequired[AuthorizationReason]
    error_code: NotRequired[str]
    error_text: NotRequired[str]
    voided_at: NotRequired[int]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    fraud_reason: NotRequired[str]
    custom_payment_method_id: NotRequired[str]
    amount_unused: NotRequired[int]
    masked_card_number: NotRequired[str]
    reference_transaction_id: NotRequired[str]
    refunded_txn_id: NotRequired[str]
    reference_authorization_id: NotRequired[str]
    amount_capturable: NotRequired[int]
    reversal_transaction_id: NotRequired[str]
    linked_invoices: NotRequired[List[LinkedInvoice]]
    linked_credit_notes: NotRequired[List[LinkedCreditNote]]
    linked_refunds: NotRequired[List[LinkedRefund]]
    linked_payments: NotRequired[List[LinkedPayment]]
    deleted: Required[bool]
    iin: NotRequired[str]
    last4: NotRequired[str]
    merchant_reference_id: NotRequired[str]
    business_entity_id: NotRequired[str]
    payment_method_details: NotRequired[str]
    error_detail: NotRequired[GatewayErrorDetail]
    custom_payment_method_name: NotRequired[str]
