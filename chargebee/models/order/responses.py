from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import credit_note


@dataclass
class OrderLineItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    invoice_id: str = None
    invoice_line_item_id: str = None
    unit_price: int = None
    description: str = None
    amount: int = None
    fulfillment_quantity: int = None
    fulfillment_amount: int = None
    tax_amount: int = None
    amount_paid: int = None
    amount_adjusted: int = None
    refundable_credits_issued: int = None
    refundable_credits: int = None
    is_shippable: bool = None
    sku: str = None
    status: str = None
    entity_type: str = None
    item_level_discount_amount: int = None
    discount_amount: int = None
    entity_id: str = None


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
class LineItemDiscountResponse(Model):
    raw_data: Dict[Any, Any] = None
    line_item_id: str = None
    discount_type: str = None
    coupon_id: str = None
    entity_id: str = None
    discount_amount: int = None


@dataclass
class LinkedCreditNoteResponse(Model):
    raw_data: Dict[Any, Any] = None
    amount: int = None
    type: str = None
    id: str = None
    status: str = None
    amount_adjusted: int = None
    amount_refunded: int = None


@dataclass
class ResentOrderResponse(Model):
    raw_data: Dict[Any, Any] = None
    order_id: str = None
    reason: str = None
    amount: int = None


@dataclass
class OrderResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    document_number: str = None
    invoice_id: str = None
    subscription_id: str = None
    customer_id: str = None
    status: str = None
    cancellation_reason: str = None
    payment_status: str = None
    order_type: str = None
    price_type: str = None
    reference_id: str = None
    fulfillment_status: str = None
    order_date: int = None
    shipping_date: int = None
    note: str = None
    tracking_id: str = None
    tracking_url: str = None
    batch_id: str = None
    created_by: str = None
    shipment_carrier: str = None
    invoice_round_off_amount: int = None
    tax: int = None
    amount_paid: int = None
    amount_adjusted: int = None
    refundable_credits_issued: int = None
    refundable_credits: int = None
    rounding_adjustement: int = None
    paid_on: int = None
    shipping_cut_off_date: int = None
    created_at: int = None
    status_update_at: int = None
    delivered_at: int = None
    shipped_at: int = None
    resource_version: int = None
    updated_at: int = None
    cancelled_at: int = None
    resent_status: str = None
    is_resent: bool = None
    original_order_id: str = None
    order_line_items: List[OrderLineItemResponse] = None
    shipping_address: ShippingAddressResponse = None
    billing_address: BillingAddressResponse = None
    discount: int = None
    sub_total: int = None
    total: int = None
    line_item_taxes: List[LineItemTaxResponse] = None
    line_item_discounts: List[LineItemDiscountResponse] = None
    linked_credit_notes: List[LinkedCreditNoteResponse] = None
    deleted: bool = None
    currency_code: str = None
    is_gifted: bool = None
    gift_note: str = None
    gift_id: str = None
    resend_reason: str = None
    resent_orders: List[ResentOrderResponse] = None
    business_entity_id: str = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    order: OrderResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    order: OrderResponse


@dataclass
class ImportOrderResponse(Response):
    is_idempotency_replayed: bool
    order: OrderResponse


@dataclass
class AssignOrderNumberResponse(Response):
    is_idempotency_replayed: bool
    order: OrderResponse


@dataclass
class CancelResponse(Response):
    is_idempotency_replayed: bool
    order: OrderResponse


@dataclass
class CreateRefundableCreditNoteResponse(Response):
    is_idempotency_replayed: bool
    order: OrderResponse


@dataclass
class ReopenResponse(Response):
    is_idempotency_replayed: bool
    order: OrderResponse


@dataclass
class RetrieveResponse(Response):
    order: OrderResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    order: OrderResponse


@dataclass
class ListOrderResponse:
    order: OrderResponse


@dataclass
class ListResponse(Response):
    list: List[ListOrderResponse]
    next_offset: str = None


@dataclass
class OrdersForInvoiceOrderResponse:
    order: OrderResponse


@dataclass
class OrdersForInvoiceResponse(Response):
    list: List[OrdersForInvoiceOrderResponse]
    next_offset: str = None


@dataclass
class ResendResponse(Response):
    is_idempotency_replayed: bool
    order: OrderResponse
