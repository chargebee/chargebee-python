from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import (
    credit_note,
    payment_reference_number,
    payment_intent,
    transaction,
    card,
    credit_note,
    transaction,
    payment_schedule,
    payment_reference_number,
    download,
)


@dataclass
class LineItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    subscription_id: str = None
    date_from: int = None
    date_to: int = None
    unit_amount: int = None
    quantity: int = None
    amount: int = None
    pricing_model: str = None
    is_taxed: bool = None
    tax_amount: int = None
    tax_rate: float = None
    unit_amount_in_decimal: str = None
    quantity_in_decimal: str = None
    amount_in_decimal: str = None
    discount_amount: int = None
    item_level_discount_amount: int = None
    metered: bool = None
    is_percentage_pricing: bool = None
    reference_line_item_id: str = None
    description: str = None
    entity_description: str = None
    entity_type: str = None
    tax_exempt_reason: str = None
    entity_id: str = None
    customer_id: str = None


@dataclass
class LineItemTierResponse(Model):
    raw_data: Dict[Any, Any] = None
    line_item_id: str = None
    starting_unit: int = None
    ending_unit: int = None
    quantity_used: int = None
    unit_amount: int = None
    starting_unit_in_decimal: str = None
    ending_unit_in_decimal: str = None
    quantity_used_in_decimal: str = None
    unit_amount_in_decimal: str = None
    pricing_type: str = None
    package_size: int = None


@dataclass
class LineItemDiscountResponse(Model):
    raw_data: Dict[Any, Any] = None
    line_item_id: str = None
    discount_type: str = None
    coupon_id: str = None
    entity_id: str = None
    discount_amount: int = None


@dataclass
class LineItemTaxResponse(Model):
    raw_data: Dict[Any, Any] = None
    line_item_id: str = None
    tax_name: str = None
    tax_rate: float = None
    date_to: int = None
    date_from: int = None
    prorated_taxable_amount: float = None
    is_partial_tax_applied: bool = None
    is_non_compliance_tax: bool = None
    taxable_amount: int = None
    tax_amount: int = None
    tax_juris_type: str = None
    tax_juris_name: str = None
    tax_juris_code: str = None
    tax_amount_in_local_currency: int = None
    local_currency_code: str = None


@dataclass
class LineItemCreditResponse(Model):
    raw_data: Dict[Any, Any] = None
    cn_id: str = None
    applied_amount: float = None
    line_item_id: str = None


@dataclass
class LineItemAddressResponse(Model):
    raw_data: Dict[Any, Any] = None
    line_item_id: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    company: str = None
    phone: str = None
    line1: str = None
    line2: str = None
    line3: str = None
    city: str = None
    state_code: str = None
    state: str = None
    country: str = None
    zip: str = None
    validation_status: str = None


@dataclass
class DiscountResponse(Model):
    raw_data: Dict[Any, Any] = None
    amount: int = None
    description: str = None
    line_item_id: str = None
    entity_type: str = None
    discount_type: str = None
    entity_id: str = None
    coupon_set_code: str = None


@dataclass
class TaxResponse(Model):
    raw_data: Dict[Any, Any] = None
    name: str = None
    amount: int = None
    description: str = None


@dataclass
class TaxOriginResponse(Model):
    raw_data: Dict[Any, Any] = None
    country: str = None
    registration_number: str = None


@dataclass
class LinkedPaymentResponse(Model):
    raw_data: Dict[Any, Any] = None
    txn_id: str = None
    applied_amount: int = None
    applied_at: int = None
    txn_status: str = None
    txn_date: int = None
    txn_amount: int = None


@dataclass
class ReferenceTransactionResponse(Model):
    raw_data: Dict[Any, Any] = None
    applied_amount: int = None
    applied_at: int = None
    txn_id: str = None
    txn_status: str = None
    txn_date: int = None
    txn_amount: int = None
    txn_type: str = None
    amount_capturable: int = None
    authorization_reason: str = None


@dataclass
class DunningAttemptResponse(Model):
    raw_data: Dict[Any, Any] = None
    attempt: int = None
    transaction_id: str = None
    dunning_type: str = None
    created_at: int = None
    txn_status: str = None
    txn_amount: int = None
    retry_engine: str = None


@dataclass
class AppliedCreditResponse(Model):
    raw_data: Dict[Any, Any] = None
    cn_id: str = None
    applied_amount: int = None
    applied_at: int = None
    cn_reason_code: str = None
    cn_create_reason_code: str = None
    cn_date: int = None
    cn_status: str = None
    tax_application: str = None


@dataclass
class AdjustmentCreditNoteResponse(Model):
    raw_data: Dict[Any, Any] = None
    cn_id: str = None
    cn_reason_code: str = None
    cn_create_reason_code: str = None
    cn_date: int = None
    cn_total: int = None
    cn_status: str = None


@dataclass
class IssuedCreditNoteResponse(Model):
    raw_data: Dict[Any, Any] = None
    cn_id: str = None
    cn_reason_code: str = None
    cn_create_reason_code: str = None
    cn_date: int = None
    cn_total: int = None
    cn_status: str = None


@dataclass
class LinkedOrderResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    document_number: str = None
    status: str = None
    order_type: str = None
    reference_id: str = None
    fulfillment_status: str = None
    batch_id: str = None
    created_at: int = None


@dataclass
class NoteResponse(Model):
    raw_data: Dict[Any, Any] = None
    note: str = None
    entity_id: str = None
    entity_type: str = None


@dataclass
class ShippingAddressResponse(Model):
    raw_data: Dict[Any, Any] = None
    first_name: str = None
    last_name: str = None
    email: str = None
    company: str = None
    phone: str = None
    line1: str = None
    line2: str = None
    line3: str = None
    city: str = None
    state_code: str = None
    state: str = None
    country: str = None
    zip: str = None
    validation_status: str = None


@dataclass
class BillingAddressResponse(Model):
    raw_data: Dict[Any, Any] = None
    first_name: str = None
    last_name: str = None
    email: str = None
    company: str = None
    phone: str = None
    line1: str = None
    line2: str = None
    line3: str = None
    city: str = None
    state_code: str = None
    state: str = None
    country: str = None
    zip: str = None
    validation_status: str = None


@dataclass
class StatementDescriptorResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    descriptor: str = None


@dataclass
class EinvoiceResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    reference_number: str = None
    status: str = None
    message: str = None


@dataclass
class SiteDetailsAtCreationResponse(Model):
    raw_data: Dict[Any, Any] = None
    timezone: str = None
    organization_address: Dict[Any, Any] = None


@dataclass
class InvoiceResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    customer_id: str = None
    payment_owner: str = None
    subscription_id: str = None
    recurring: bool = None
    status: str = None
    date: int = None
    due_date: int = None
    net_term_days: int = None
    po_number: str = None
    vat_number: str = None
    price_type: str = None
    exchange_rate: float = None
    local_currency_exchange_rate: float = None
    currency_code: str = None
    local_currency_code: str = None
    tax: int = None
    sub_total: int = None
    sub_total_in_local_currency: int = None
    total: int = None
    total_in_local_currency: int = None
    amount_due: int = None
    amount_adjusted: int = None
    amount_paid: int = None
    paid_at: int = None
    write_off_amount: int = None
    credits_applied: int = None
    dunning_status: str = None
    next_retry_at: int = None
    voided_at: int = None
    resource_version: int = None
    updated_at: int = None
    line_items_next_offset: str = None
    first_invoice: bool = None
    new_sales_amount: int = None
    has_advance_charges: bool = None
    term_finalized: bool = None
    is_gifted: bool = None
    generated_at: int = None
    expected_payment_date: int = None
    amount_to_collect: int = None
    round_off_amount: int = None
    line_items: List[LineItemResponse] = None
    line_item_tiers: List[LineItemTierResponse] = None
    line_item_discounts: List[LineItemDiscountResponse] = None
    line_item_taxes: List[LineItemTaxResponse] = None
    line_item_credits: List[LineItemCreditResponse] = None
    line_item_addresses: List[LineItemAddressResponse] = None
    discounts: List[DiscountResponse] = None
    taxes: List[TaxResponse] = None
    tax_origin: TaxOriginResponse = None
    linked_payments: List[LinkedPaymentResponse] = None
    reference_transactions: List[ReferenceTransactionResponse] = None
    dunning_attempts: List[DunningAttemptResponse] = None
    applied_credits: List[AppliedCreditResponse] = None
    adjustment_credit_notes: List[AdjustmentCreditNoteResponse] = None
    issued_credit_notes: List[IssuedCreditNoteResponse] = None
    linked_orders: List[LinkedOrderResponse] = None
    notes: List[NoteResponse] = None
    shipping_address: ShippingAddressResponse = None
    billing_address: BillingAddressResponse = None
    statement_descriptor: StatementDescriptorResponse = None
    einvoice: EinvoiceResponse = None
    void_reason_code: str = None
    deleted: bool = None
    tax_category: str = None
    vat_number_prefix: str = None
    channel: str = None
    business_entity_id: str = None
    site_details_at_creation: SiteDetailsAtCreationResponse = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class CreateForChargeItemsAndChargesResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class ChargeResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class ChargeAddonResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class CreateForChargeItemResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class StopDunningResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class PauseDunningResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class ResumeDunningResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class ImportInvoiceResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse
    credit_note: "credit_note.CreditNoteResponse" = None


@dataclass
class ApplyPaymentsResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class SyncUsagesResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class DeleteLineItemsResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class ApplyCreditsResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class ListInvoiceResponse:
    invoice: InvoiceResponse


@dataclass
class ListResponse(Response):
    list: List[ListInvoiceResponse]
    next_offset: str = None


@dataclass
class InvoicesForCustomerInvoiceResponse:
    invoice: InvoiceResponse


@dataclass
class InvoicesForCustomerResponse(Response):
    list: List[InvoicesForCustomerInvoiceResponse]
    next_offset: str = None


@dataclass
class InvoicesForSubscriptionInvoiceResponse:
    invoice: InvoiceResponse


@dataclass
class InvoicesForSubscriptionResponse(Response):
    list: List[InvoicesForSubscriptionInvoiceResponse]
    next_offset: str = None


@dataclass
class RetrieveResponse(Response):
    invoice: InvoiceResponse


@dataclass
class PdfResponse(Response):
    is_idempotency_replayed: bool
    download: "download.DownloadResponse"


@dataclass
class DownloadEinvoiceResponse(Response):
    downloads: List["download.DownloadResponse"]


@dataclass
class ListPaymentReferenceNumbersInvoiceResponse:
    payment_reference_number: "payment_reference_number.PaymentReferenceNumberResponse"


@dataclass
class ListPaymentReferenceNumbersResponse(Response):
    list: List[ListPaymentReferenceNumbersInvoiceResponse]
    next_offset: str = None


@dataclass
class AddChargeResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class AddAddonChargeResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class AddChargeItemResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class CloseResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class CollectPaymentResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse
    transaction: "transaction.TransactionResponse"


@dataclass
class RecordPaymentResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse
    transaction: "transaction.TransactionResponse"


@dataclass
class RecordTaxWithheldResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class RemoveTaxWithheldResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class RefundResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse
    transaction: "transaction.TransactionResponse"
    credit_note: "credit_note.CreditNoteResponse" = None


@dataclass
class RecordRefundResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse
    transaction: "transaction.TransactionResponse" = None
    credit_note: "credit_note.CreditNoteResponse" = None


@dataclass
class RemovePaymentResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse
    transaction: "transaction.TransactionResponse"


@dataclass
class RemoveCreditNoteResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse
    credit_note: "credit_note.CreditNoteResponse"


@dataclass
class VoidInvoiceResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse
    credit_note: "credit_note.CreditNoteResponse" = None


@dataclass
class WriteOffResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse
    credit_note: "credit_note.CreditNoteResponse"


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class UpdateDetailsResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class ApplyPaymentScheduleSchemeResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class PaymentSchedulesResponse(Response):
    payment_schedules: List["payment_schedule.PaymentScheduleResponse"]


@dataclass
class ResendEinvoiceResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse


@dataclass
class SendEinvoiceResponse(Response):
    is_idempotency_replayed: bool
    invoice: InvoiceResponse
