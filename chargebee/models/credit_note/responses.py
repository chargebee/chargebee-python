from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import invoice, transaction, transaction, invoice, download


@dataclass
class EinvoiceResponse(Model):
    id: str = None
    reference_number: str = None
    status: str = None
    message: str = None


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
class LinkedRefundResponse(Model):
    txn_id: str = None
    applied_amount: int = None
    applied_at: int = None
    txn_status: str = None
    txn_date: int = None
    txn_amount: int = None
    refund_reason_code: str = None


@dataclass
class AllocationResponse(Model):
    invoice_id: str = None
    allocated_amount: int = None
    allocated_at: int = None
    invoice_date: int = None
    invoice_status: str = None


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
class SiteDetailsAtCreationResponse(Model):
    timezone: str = None
    organization_address: Dict[Any, Any] = None


@dataclass
class TaxOriginResponse(Model):
    country: str = None
    registration_number: str = None


@dataclass
class CreditNoteResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    customer_id: str = None
    subscription_id: str = None
    reference_invoice_id: str = None
    type: str = None
    reason_code: str = None
    status: str = None
    vat_number: str = None
    date: int = None
    price_type: str = None
    currency_code: str = None
    total: int = None
    amount_allocated: int = None
    amount_refunded: int = None
    amount_available: int = None
    refunded_at: int = None
    voided_at: int = None
    generated_at: int = None
    resource_version: int = None
    updated_at: int = None
    channel: str = None
    einvoice: EinvoiceResponse = None
    sub_total: int = None
    sub_total_in_local_currency: int = None
    total_in_local_currency: int = None
    local_currency_code: str = None
    round_off_amount: int = None
    fractional_correction: int = None
    line_items: List[LineItemResponse] = None
    discounts: List[DiscountResponse] = None
    line_item_discounts: List[LineItemDiscountResponse] = None
    line_item_tiers: List[LineItemTierResponse] = None
    taxes: List[TaxResponse] = None
    line_item_taxes: List[LineItemTaxResponse] = None
    linked_refunds: List[LinkedRefundResponse] = None
    allocations: List[AllocationResponse] = None
    deleted: bool = None
    tax_category: str = None
    local_currency_exchange_rate: float = None
    create_reason_code: str = None
    vat_number_prefix: str = None
    business_entity_id: str = None
    shipping_address: ShippingAddressResponse = None
    billing_address: BillingAddressResponse = None
    site_details_at_creation: SiteDetailsAtCreationResponse = None
    tax_origin: TaxOriginResponse = None


@dataclass
class CreateResponse(Response):
    credit_note: CreditNoteResponse
    invoice: "invoice.InvoiceResponse" = None
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    credit_note: CreditNoteResponse
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
class RefundResponse(Response):
    credit_note: CreditNoteResponse
    transaction: "transaction.TransactionResponse"
    headers: Dict[str, str] = None


@dataclass
class RecordRefundResponse(Response):
    credit_note: CreditNoteResponse
    transaction: "transaction.TransactionResponse" = None
    headers: Dict[str, str] = None


@dataclass
class VoidCreditNoteResponse(Response):
    credit_note: CreditNoteResponse
    headers: Dict[str, str] = None


@dataclass
class ListCreditNoteResponse:
    credit_note: CreditNoteResponse


@dataclass
class ListResponse:
    list: List[ListCreditNoteResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class CreditNotesForCustomerCreditNoteResponse:
    credit_note: CreditNoteResponse


@dataclass
class CreditNotesForCustomerResponse:
    list: List[CreditNotesForCustomerCreditNoteResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class DeleteResponse(Response):
    credit_note: CreditNoteResponse
    headers: Dict[str, str] = None


@dataclass
class RemoveTaxWithheldRefundResponse(Response):
    credit_note: CreditNoteResponse
    headers: Dict[str, str] = None


@dataclass
class ResendEinvoiceResponse(Response):
    credit_note: CreditNoteResponse
    headers: Dict[str, str] = None


@dataclass
class SendEinvoiceResponse(Response):
    credit_note: CreditNoteResponse
    headers: Dict[str, str] = None


@dataclass
class ImportCreditNoteResponse(Response):
    credit_note: CreditNoteResponse
    headers: Dict[str, str] = None
