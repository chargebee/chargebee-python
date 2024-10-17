from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import (
    contract_term,
    quoted_subscription,
    quoted_charge,
    quote_line_group,
    download,
    customer,
    subscription,
    invoice,
    credit_note,
    unbilled_charge,
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
class QuoteResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    po_number: str = None
    customer_id: str = None
    subscription_id: str = None
    invoice_id: str = None
    status: str = None
    operation_type: str = None
    vat_number: str = None
    price_type: str = None
    valid_till: int = None
    date: int = None
    total_payable: int = None
    charge_on_acceptance: int = None
    sub_total: int = None
    total: int = None
    credits_applied: int = None
    amount_paid: int = None
    amount_due: int = None
    version: int = None
    resource_version: int = None
    updated_at: int = None
    vat_number_prefix: str = None
    line_items: List[LineItemResponse] = None
    discounts: List[DiscountResponse] = None
    line_item_discounts: List[LineItemDiscountResponse] = None
    taxes: List[TaxResponse] = None
    line_item_taxes: List[LineItemTaxResponse] = None
    line_item_tiers: List[LineItemTierResponse] = None
    tax_category: str = None
    currency_code: str = None
    notes: List[Dict[Any, Any]] = None
    shipping_address: ShippingAddressResponse = None
    billing_address: BillingAddressResponse = None
    contract_term_start: int = None
    contract_term_end: int = None
    contract_term_termination_fee: int = None
    business_entity_id: str = None


@dataclass
class RetrieveResponse:
    quote: QuoteResponse
    quoted_subscription: "quoted_subscription.QuotedSubscriptionResponse" = None
    quoted_charge: "quoted_charge.QuotedChargeResponse" = None
    headers: Dict[str, str] = None


@dataclass
class CreateSubForCustomerQuoteResponse(Response):
    quote: QuoteResponse
    quoted_subscription: "quoted_subscription.QuotedSubscriptionResponse" = None
    headers: Dict[str, str] = None


@dataclass
class EditCreateSubForCustomerQuoteResponse(Response):
    quote: QuoteResponse
    quoted_subscription: "quoted_subscription.QuotedSubscriptionResponse" = None
    headers: Dict[str, str] = None


@dataclass
class UpdateSubscriptionQuoteResponse(Response):
    quote: QuoteResponse
    quoted_subscription: "quoted_subscription.QuotedSubscriptionResponse" = None
    headers: Dict[str, str] = None


@dataclass
class EditUpdateSubscriptionQuoteResponse(Response):
    quote: QuoteResponse
    quoted_subscription: "quoted_subscription.QuotedSubscriptionResponse" = None
    headers: Dict[str, str] = None


@dataclass
class CreateForOnetimeChargesResponse(Response):
    quote: QuoteResponse
    quoted_charge: "quoted_charge.QuotedChargeResponse" = None
    headers: Dict[str, str] = None


@dataclass
class EditOneTimeQuoteResponse(Response):
    quote: QuoteResponse
    quoted_charge: "quoted_charge.QuotedChargeResponse" = None
    headers: Dict[str, str] = None


@dataclass
class CreateSubItemsForCustomerQuoteResponse(Response):
    quote: QuoteResponse
    quoted_subscription: "quoted_subscription.QuotedSubscriptionResponse" = None
    headers: Dict[str, str] = None


@dataclass
class EditCreateSubCustomerQuoteForItemsResponse(Response):
    quote: QuoteResponse
    quoted_subscription: "quoted_subscription.QuotedSubscriptionResponse" = None
    headers: Dict[str, str] = None


@dataclass
class UpdateSubscriptionQuoteForItemsResponse(Response):
    quote: QuoteResponse
    quoted_subscription: "quoted_subscription.QuotedSubscriptionResponse" = None
    headers: Dict[str, str] = None


@dataclass
class EditUpdateSubscriptionQuoteForItemsResponse(Response):
    quote: QuoteResponse
    quoted_subscription: "quoted_subscription.QuotedSubscriptionResponse" = None
    headers: Dict[str, str] = None


@dataclass
class CreateForChargeItemsAndChargesResponse(Response):
    quote: QuoteResponse
    quoted_charge: "quoted_charge.QuotedChargeResponse" = None
    headers: Dict[str, str] = None


@dataclass
class EditForChargeItemsAndChargesResponse(Response):
    quote: QuoteResponse
    quoted_charge: "quoted_charge.QuotedChargeResponse" = None
    headers: Dict[str, str] = None


@dataclass
class ListQuoteResponse:
    quote: QuoteResponse
    quoted_subscription: "quoted_subscription.QuotedSubscriptionResponse" = None


@dataclass
class ListResponse:
    list: List[ListQuoteResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class QuoteLineGroupsForQuoteQuoteResponse:
    quote_line_group: "quote_line_group.QuoteLineGroupResponse"


@dataclass
class QuoteLineGroupsForQuoteResponse:
    list: List[QuoteLineGroupsForQuoteQuoteResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class ConvertResponse(Response):
    quote: QuoteResponse
    customer: "customer.CustomerResponse"
    quoted_subscription: "quoted_subscription.QuotedSubscriptionResponse" = None
    quoted_charge: "quoted_charge.QuotedChargeResponse" = None
    subscription: "subscription.SubscriptionResponse" = None
    invoice: "invoice.InvoiceResponse" = None
    credit_note: "credit_note.CreditNoteResponse" = None
    unbilled_charges: List["unbilled_charge.UnbilledChargeResponse"] = None
    headers: Dict[str, str] = None


@dataclass
class UpdateStatusResponse(Response):
    quote: QuoteResponse
    quoted_subscription: "quoted_subscription.QuotedSubscriptionResponse" = None
    quoted_charge: "quoted_charge.QuotedChargeResponse" = None
    headers: Dict[str, str] = None


@dataclass
class ExtendExpiryDateResponse(Response):
    quote: QuoteResponse
    quoted_subscription: "quoted_subscription.QuotedSubscriptionResponse" = None
    quoted_charge: "quoted_charge.QuotedChargeResponse" = None
    headers: Dict[str, str] = None


@dataclass
class DeleteResponse(Response):
    quote: QuoteResponse
    quoted_subscription: "quoted_subscription.QuotedSubscriptionResponse" = None
    quoted_charge: "quoted_charge.QuotedChargeResponse" = None
    headers: Dict[str, str] = None


@dataclass
class PdfResponse(Response):
    download: "download.DownloadResponse"
    headers: Dict[str, str] = None
