from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import credit_note, invoice, transaction


@dataclass
class LinkedInvoiceResponse(Model):
    raw_data: Dict[Any, Any] = None
    invoice_id: str = None
    applied_amount: int = None
    applied_at: int = None
    invoice_date: int = None
    invoice_total: int = None
    invoice_status: str = None


@dataclass
class LinkedCreditNoteResponse(Model):
    raw_data: Dict[Any, Any] = None
    cn_id: str = None
    applied_amount: int = None
    applied_at: int = None
    cn_reason_code: str = None
    cn_create_reason_code: str = None
    cn_date: int = None
    cn_total: int = None
    cn_status: str = None
    cn_reference_invoice_id: str = None


@dataclass
class LinkedRefundResponse(Model):
    raw_data: Dict[Any, Any] = None
    txn_id: str = None
    txn_status: str = None
    txn_date: int = None
    txn_amount: int = None


@dataclass
class LinkedPaymentResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    status: str = None
    amount: int = None
    date: int = None


@dataclass
class GatewayErrorDetailResponse(Model):
    raw_data: Dict[Any, Any] = None
    request_id: str = None
    error_category: str = None
    error_code: str = None
    error_message: str = None
    decline_code: str = None
    decline_message: str = None
    network_error_code: str = None
    network_error_message: str = None
    error_field: str = None
    recommendation_code: str = None
    recommendation_message: str = None
    processor_error_code: str = None
    processor_error_message: str = None
    error_cause_id: str = None
    processor_advice_code: str = None


@dataclass
class TransactionResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    customer_id: str = None
    subscription_id: str = None
    gateway_account_id: str = None
    payment_source_id: str = None
    payment_method: str = None
    reference_number: str = None
    gateway: str = None
    type: str = None
    date: int = None
    settled_at: int = None
    exchange_rate: float = None
    currency_code: str = None
    amount: int = None
    id_at_gateway: str = None
    status: str = None
    fraud_flag: str = None
    initiator_type: str = None
    three_d_secure: bool = None
    authorization_reason: str = None
    error_code: str = None
    error_text: str = None
    voided_at: int = None
    resource_version: int = None
    updated_at: int = None
    fraud_reason: str = None
    custom_payment_method_id: str = None
    amount_unused: int = None
    masked_card_number: str = None
    reference_transaction_id: str = None
    refunded_txn_id: str = None
    reference_authorization_id: str = None
    amount_capturable: int = None
    reversal_transaction_id: str = None
    linked_invoices: List[LinkedInvoiceResponse] = None
    linked_credit_notes: List[LinkedCreditNoteResponse] = None
    linked_refunds: List[LinkedRefundResponse] = None
    linked_payments: List[LinkedPaymentResponse] = None
    deleted: bool = None
    iin: str = None
    last4: str = None
    merchant_reference_id: str = None
    business_entity_id: str = None
    payment_method_details: str = None
    error_detail: GatewayErrorDetailResponse = None
    custom_payment_method_name: str = None


@dataclass
class CreateAuthorizationResponse(Response):
    is_idempotency_replayed: bool
    transaction: TransactionResponse


@dataclass
class VoidTransactionResponse(Response):
    is_idempotency_replayed: bool
    transaction: TransactionResponse


@dataclass
class RecordRefundResponse(Response):
    is_idempotency_replayed: bool
    transaction: TransactionResponse


@dataclass
class ReconcileResponse(Response):
    is_idempotency_replayed: bool
    transaction: TransactionResponse


@dataclass
class RefundResponse(Response):
    is_idempotency_replayed: bool
    transaction: TransactionResponse


@dataclass
class ListTransactionResponse:
    transaction: TransactionResponse


@dataclass
class ListResponse(Response):
    list: List[ListTransactionResponse]
    next_offset: str = None


@dataclass
class TransactionsForCustomerTransactionResponse:
    transaction: TransactionResponse


@dataclass
class TransactionsForCustomerResponse(Response):
    list: List[TransactionsForCustomerTransactionResponse]
    next_offset: str = None


@dataclass
class TransactionsForSubscriptionTransactionResponse:
    transaction: TransactionResponse


@dataclass
class TransactionsForSubscriptionResponse(Response):
    list: List[TransactionsForSubscriptionTransactionResponse]
    next_offset: str = None


@dataclass
class PaymentsForInvoiceTransactionResponse:
    transaction: TransactionResponse


@dataclass
class PaymentsForInvoiceResponse(Response):
    list: List[PaymentsForInvoiceTransactionResponse]
    next_offset: str = None


@dataclass
class RetrieveResponse(Response):
    transaction: TransactionResponse


@dataclass
class DeleteOfflineTransactionResponse(Response):
    is_idempotency_replayed: bool
    transaction: TransactionResponse
