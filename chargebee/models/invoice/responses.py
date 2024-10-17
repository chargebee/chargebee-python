from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import (
    credit_note,
    payment_reference_number,
    payment_intent,
    transaction,
    credit_note,
    transaction,
    payment_schedule,
    payment_reference_number,
    download,
)


@dataclass
class LineItemResponse(Model):
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
    usage_percentage: str = None
    reference_line_item_id: str = None
    description: str = None
    entity_description: str = None
    entity_type: str = None
    tax_exempt_reason: str = None
    entity_id: str = None
    customer_id: str = None


@dataclass
class DiscountResponse(Model):
    amount: int = None
    description: str = None
    entity_type: str = None
    entity_id: str = None
    coupon_set_code: str = None


@dataclass
class LineItemDiscountResponse(Model):
    line_item_id: str = None
    discount_type: str = None
    coupon_id: str = None
    entity_id: str = None
    discount_amount: int = None


@dataclass
class TaxResponse(Model):
    name: str = None
    amount: int = None
    description: str = None


@dataclass
class LineItemTaxResponse(Model):
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
class LineItemTierResponse(Model):
    line_item_id: str = None
    starting_unit: int = None
    ending_unit: int = None
    quantity_used: int = None
    unit_amount: int = None
    starting_unit_in_decimal: str = None
    ending_unit_in_decimal: str = None
    quantity_used_in_decimal: str = None
    unit_amount_in_decimal: str = None


@dataclass
class LinkedPaymentResponse(Model):
    txn_id: str = None
    applied_amount: int = None
    applied_at: int = None
    txn_status: str = None
    txn_date: int = None
    txn_amount: int = None


@dataclass
class DunningAttemptResponse(Model):
    attempt: int = None
    transaction_id: str = None
    dunning_type: str = None
    created_at: int = None
    txn_status: str = None
    txn_amount: int = None


@dataclass
class AppliedCreditResponse(Model):
    cn_id: str = None
    applied_amount: int = None
    applied_at: int = None
    cn_reason_code: str = None
    cn_create_reason_code: str = None
    cn_date: int = None
    cn_status: str = None


@dataclass
class AdjustmentCreditNoteResponse(Model):
    cn_id: str = None
    cn_reason_code: str = None
    cn_create_reason_code: str = None
    cn_date: int = None
    cn_total: int = None
    cn_status: str = None


@dataclass
class IssuedCreditNoteResponse(Model):
    cn_id: str = None
    cn_reason_code: str = None
    cn_create_reason_code: str = None
    cn_date: int = None
    cn_total: int = None
    cn_status: str = None


@dataclass
class LinkedOrderResponse(Model):
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
    entity_type: str = None
    note: str = None
    entity_id: str = None


@dataclass
class ShippingAddressResponse(Model):
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
    index: int = None


@dataclass
class StatementDescriptorResponse(Model):
    id: str = None
    descriptor: str = None


@dataclass
class BillingAddressResponse(Model):
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
class EinvoiceResponse(Model):
    id: str = None
    reference_number: str = None
    status: str = None
    message: str = None


@dataclass
class SiteDetailsAtCreationResponse(Model):
    timezone: str = None
    organization_address: Dict[Any, Any] = None


@dataclass
class TaxOriginResponse(Model):
    country: str = None
    registration_number: str = None


@dataclass
class InvoiceResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    po_number: str = None
    customer_id: str = None
    subscription_id: str = None
    recurring: bool = None
    status: str = None
    vat_number: str = None
    price_type: str = None
    date: int = None
    due_date: int = None
    net_term_days: int = None
    exchange_rate: float = None
    currency_code: str = None
    total: int = None
    amount_paid: int = None
    amount_adjusted: int = None
    write_off_amount: int = None
    credits_applied: int = None
    amount_due: int = None
    paid_at: int = None
    dunning_status: str = None
    next_retry_at: int = None
    voided_at: int = None
    resource_version: int = None
    updated_at: int = None
    sub_total: int = None
    sub_total_in_local_currency: int = None
    total_in_local_currency: int = None
    local_currency_code: str = None
    tax: int = None
    local_currency_exchange_rate: float = None
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
    discounts: List[DiscountResponse] = None
    line_item_discounts: List[LineItemDiscountResponse] = None
    taxes: List[TaxResponse] = None
    line_item_taxes: List[LineItemTaxResponse] = None
    line_item_tiers: List[LineItemTierResponse] = None
    linked_payments: List[LinkedPaymentResponse] = None
    dunning_attempts: List[DunningAttemptResponse] = None
    applied_credits: List[AppliedCreditResponse] = None
    adjustment_credit_notes: List[AdjustmentCreditNoteResponse] = None
    issued_credit_notes: List[IssuedCreditNoteResponse] = None
    linked_orders: List[LinkedOrderResponse] = None
    notes: List[NoteResponse] = None
    shipping_address: ShippingAddressResponse = None
    statement_descriptor: StatementDescriptorResponse = None
    billing_address: BillingAddressResponse = None
    einvoice: EinvoiceResponse = None
    payment_owner: str = None
    void_reason_code: str = None
    deleted: bool = None
    tax_category: str = None
    vat_number_prefix: str = None
    channel: str = None
    business_entity_id: str = None
    site_details_at_creation: SiteDetailsAtCreationResponse = None
    tax_origin: TaxOriginResponse = None


@dataclass
class CreateResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class CreateForChargeItemsAndChargesResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class ChargeResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class ChargeAddonResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class CreateForChargeItemResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class StopDunningResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class ImportInvoiceResponse(Response):
    invoice: InvoiceResponse
    credit_note: "credit_note.CreditNoteResponse" = None
    headers: Dict[str, str] = None


@dataclass
class ApplyPaymentsResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class SyncUsagesResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class DeleteLineItemsResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class ApplyCreditsResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class ListInvoiceResponse:
    invoice: InvoiceResponse


@dataclass
class ListResponse:
    list: List[ListInvoiceResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class InvoicesForCustomerInvoiceResponse:
    invoice: InvoiceResponse


@dataclass
class InvoicesForCustomerResponse:
    list: List[InvoicesForCustomerInvoiceResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class InvoicesForSubscriptionInvoiceResponse:
    invoice: InvoiceResponse


@dataclass
class InvoicesForSubscriptionResponse:
    list: List[InvoicesForSubscriptionInvoiceResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class PdfResponse(Response):
    download: "download.DownloadResponse"
    headers: Dict[str, str] = None


@dataclass
class DownloadEinvoiceResponse:
    downloads: List["download.DownloadResponse"]
    headers: Dict[str, str] = None


@dataclass
class ListPaymentReferenceNumbersInvoiceResponse:
    payment_reference_number: "payment_reference_number.PaymentReferenceNumberResponse"


@dataclass
class ListPaymentReferenceNumbersResponse:
    list: List[ListPaymentReferenceNumbersInvoiceResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class AddChargeResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class AddAddonChargeResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class AddChargeItemResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class CloseResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class CollectPaymentResponse(Response):
    invoice: InvoiceResponse
    transaction: "transaction.TransactionResponse"
    headers: Dict[str, str] = None


@dataclass
class RecordPaymentResponse(Response):
    invoice: InvoiceResponse
    transaction: "transaction.TransactionResponse"
    headers: Dict[str, str] = None


@dataclass
class RecordTaxWithheldResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class RemoveTaxWithheldResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class RefundResponse(Response):
    invoice: InvoiceResponse
    transaction: "transaction.TransactionResponse"
    credit_note: "credit_note.CreditNoteResponse" = None
    headers: Dict[str, str] = None


@dataclass
class RecordRefundResponse(Response):
    invoice: InvoiceResponse
    transaction: "transaction.TransactionResponse" = None
    credit_note: "credit_note.CreditNoteResponse" = None
    headers: Dict[str, str] = None


@dataclass
class RemovePaymentResponse(Response):
    invoice: InvoiceResponse
    transaction: "transaction.TransactionResponse"
    headers: Dict[str, str] = None


@dataclass
class RemoveCreditNoteResponse(Response):
    invoice: InvoiceResponse
    credit_note: "credit_note.CreditNoteResponse"
    headers: Dict[str, str] = None


@dataclass
class VoidInvoiceResponse(Response):
    invoice: InvoiceResponse
    credit_note: "credit_note.CreditNoteResponse" = None
    headers: Dict[str, str] = None


@dataclass
class WriteOffResponse(Response):
    invoice: InvoiceResponse
    credit_note: "credit_note.CreditNoteResponse"
    headers: Dict[str, str] = None


@dataclass
class DeleteResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateDetailsResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class ApplyPaymentScheduleSchemeResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class PaymentSchedulesResponse:
    payment_schedules: List["payment_schedule.PaymentScheduleResponse"]
    headers: Dict[str, str] = None


@dataclass
class ResendEinvoiceResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None


@dataclass
class SendEinvoiceResponse(Response):
    invoice: InvoiceResponse
    headers: Dict[str, str] = None
