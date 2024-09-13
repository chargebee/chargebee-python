from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums, credit_note


class Status(Enum):
    NEW = "new"
    PROCESSING = "processing"
    COMPLETE = "complete"
    CANCELLED = "cancelled"
    VOIDED = "voided"
    QUEUED = "queued"
    AWAITING_SHIPMENT = "awaiting_shipment"
    ON_HOLD = "on_hold"
    DELIVERED = "delivered"
    SHIPPED = "shipped"
    PARTIALLY_DELIVERED = "partially_delivered"
    RETURNED = "returned"

    def __str__(self):
        return self.value


class CancellationReason(Enum):
    SHIPPING_CUT_OFF_PASSED = "shipping_cut_off_passed"
    PRODUCT_UNSATISFACTORY = "product_unsatisfactory"
    THIRD_PARTY_CANCELLATION = "third_party_cancellation"
    PRODUCT_NOT_REQUIRED = "product_not_required"
    DELIVERY_DATE_MISSED = "delivery_date_missed"
    ALTERNATIVE_FOUND = "alternative_found"
    INVOICE_WRITTEN_OFF = "invoice_written_off"
    INVOICE_VOIDED = "invoice_voided"
    FRAUDULENT_TRANSACTION = "fraudulent_transaction"
    PAYMENT_DECLINED = "payment_declined"
    SUBSCRIPTION_CANCELLED = "subscription_cancelled"
    PRODUCT_NOT_AVAILABLE = "product_not_available"
    OTHERS = "others"
    ORDER_RESENT = "order_resent"

    def __str__(self):
        return self.value


class PaymentStatus(Enum):
    NOT_PAID = "not_paid"
    PAID = "paid"

    def __str__(self):
        return self.value


class OrderType(Enum):
    MANUAL = "manual"
    SYSTEM_GENERATED = "system_generated"

    def __str__(self):
        return self.value


class ResentStatus(Enum):
    FULLY_RESENT = "fully_resent"
    PARTIALLY_RESENT = "partially_resent"

    def __str__(self):
        return self.value


class OrderLineItemStatus(Enum):
    QUEUED = "queued"
    AWAITING_SHIPMENT = "awaiting_shipment"
    ON_HOLD = "on_hold"
    DELIVERED = "delivered"
    SHIPPED = "shipped"
    PARTIALLY_DELIVERED = "partially_delivered"
    RETURNED = "returned"
    CANCELLED = "cancelled"

    def __str__(self):
        return self.value


class OrderLineItemEntityType(Enum):
    ADHOC = "adhoc"
    PLAN_ITEM_PRICE = "plan_item_price"
    ADDON_ITEM_PRICE = "addon_item_price"
    CHARGE_ITEM_PRICE = "charge_item_price"
    PLAN_SETUP = "plan_setup"
    PLAN = "plan"
    ADDON = "addon"

    def __str__(self):
        return self.value


class LineItemDiscountDiscountType(Enum):
    ITEM_LEVEL_COUPON = "item_level_coupon"
    DOCUMENT_LEVEL_COUPON = "document_level_coupon"
    PROMOTIONAL_CREDITS = "promotional_credits"
    PRORATED_CREDITS = "prorated_credits"
    CUSTOM_DISCOUNT = "custom_discount"
    ITEM_LEVEL_DISCOUNT = "item_level_discount"
    DOCUMENT_LEVEL_DISCOUNT = "document_level_discount"

    def __str__(self):
        return self.value


class OrderLineItemLinkedCreditType(Enum):
    ADJUSTMENT = "adjustment"
    REFUNDABLE = "refundable"

    def __str__(self):
        return self.value


class OrderLineItemLinkedCreditStatus(Enum):
    ADJUSTED = "adjusted"
    REFUNDED = "refunded"
    REFUND_DUE = "refund_due"
    VOIDED = "voided"

    def __str__(self):
        return self.value


class OrderLineItem(TypedDict):
    id: Required[str]
    invoice_id: Required[str]
    invoice_line_item_id: Required[str]
    unit_price: NotRequired[int]
    description: NotRequired[str]
    amount: NotRequired[int]
    fulfillment_quantity: NotRequired[int]
    fulfillment_amount: NotRequired[int]
    tax_amount: NotRequired[int]
    amount_paid: NotRequired[int]
    amount_adjusted: NotRequired[int]
    refundable_credits_issued: NotRequired[int]
    refundable_credits: NotRequired[int]
    is_shippable: Required[bool]
    sku: NotRequired[str]
    status: NotRequired[OrderLineItemStatus]
    entity_type: Required[OrderLineItemEntityType]
    item_level_discount_amount: NotRequired[int]
    discount_amount: NotRequired[int]
    entity_id: NotRequired[str]


class ShippingAddress(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    state: NotRequired[str]
    country: NotRequired[str]
    zip: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]
    index: Required[int]


class BillingAddress(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    state: NotRequired[str]
    country: NotRequired[str]
    zip: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class LineItemTax(TypedDict):
    line_item_id: NotRequired[str]
    tax_name: Required[str]
    tax_rate: Required[float]
    date_to: NotRequired[int]
    date_from: NotRequired[int]
    prorated_taxable_amount: NotRequired[float]
    is_partial_tax_applied: NotRequired[bool]
    is_non_compliance_tax: NotRequired[bool]
    taxable_amount: Required[int]
    tax_amount: Required[int]
    tax_juris_type: NotRequired[enums.TaxJurisType]
    tax_juris_name: NotRequired[str]
    tax_juris_code: NotRequired[str]
    tax_amount_in_local_currency: NotRequired[int]
    local_currency_code: NotRequired[str]


class LineItemDiscount(TypedDict):
    line_item_id: Required[str]
    discount_type: Required[LineItemDiscountDiscountType]
    coupon_id: NotRequired[str]
    entity_id: NotRequired[str]
    discount_amount: Required[int]


class LinkedCreditNote(TypedDict):
    amount: NotRequired[int]
    type: Required[OrderLineItemLinkedCreditType]
    id: Required[str]
    status: Required[OrderLineItemLinkedCreditStatus]
    amount_adjusted: NotRequired[int]
    amount_refunded: NotRequired[int]


class ResentOrder(TypedDict):
    order_id: Required[str]
    reason: NotRequired[str]
    amount: NotRequired[int]


class Orders(TypedDict):
    id: Required[str]
    document_number: NotRequired[str]
    invoice_id: NotRequired[str]
    subscription_id: NotRequired[str]
    customer_id: NotRequired[str]
    status: NotRequired[Status]
    cancellation_reason: NotRequired[CancellationReason]
    payment_status: NotRequired[PaymentStatus]
    order_type: NotRequired[OrderType]
    price_type: Required[enums.PriceType]
    reference_id: NotRequired[str]
    fulfillment_status: NotRequired[str]
    order_date: NotRequired[int]
    shipping_date: NotRequired[int]
    note: NotRequired[str]
    tracking_id: NotRequired[str]
    tracking_url: NotRequired[str]
    batch_id: NotRequired[str]
    created_by: NotRequired[str]
    shipment_carrier: NotRequired[str]
    invoice_round_off_amount: NotRequired[int]
    tax: NotRequired[int]
    amount_paid: NotRequired[int]
    amount_adjusted: NotRequired[int]
    refundable_credits_issued: NotRequired[int]
    refundable_credits: NotRequired[int]
    rounding_adjustement: NotRequired[int]
    paid_on: NotRequired[int]
    shipping_cut_off_date: NotRequired[int]
    created_at: Required[int]
    status_update_at: NotRequired[int]
    delivered_at: NotRequired[int]
    shipped_at: NotRequired[int]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    cancelled_at: NotRequired[int]
    resent_status: NotRequired[ResentStatus]
    is_resent: Required[bool]
    original_order_id: NotRequired[str]
    order_line_items: NotRequired[List[OrderLineItem]]
    shipping_address: NotRequired[ShippingAddress]
    billing_address: NotRequired[BillingAddress]
    discount: NotRequired[int]
    sub_total: NotRequired[int]
    total: NotRequired[int]
    line_item_taxes: NotRequired[List[LineItemTax]]
    line_item_discounts: NotRequired[List[LineItemDiscount]]
    linked_credit_notes: NotRequired[List[LinkedCreditNote]]
    deleted: Required[bool]
    currency_code: NotRequired[str]
    is_gifted: NotRequired[bool]
    gift_note: NotRequired[str]
    gift_id: NotRequired[str]
    resend_reason: NotRequired[str]
    resent_orders: NotRequired[List[ResentOrder]]
    business_entity_id: NotRequired[str]


class UpdateOrderLineItemParams(TypedDict):
    id: NotRequired[str]
    status: NotRequired[OrderLineItemStatus]
    sku: NotRequired[str]


class UpdateShippingAddressParams(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class ImportOrderShippingAddressParams(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class ImportOrderBillingAddressParams(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class CancelCreditNoteParams(TypedDict):
    total: NotRequired[int]


class CreateRefundableCreditNoteCreditNoteParams(TypedDict):
    reason_code: Required["credit_note.ReasonCode"]
    total: Required[int]


class ResendOrderLineItemParams(TypedDict):
    id: NotRequired[str]
    fulfillment_quantity: NotRequired[int]
