from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums, credit_note


@dataclass
class Order:
    env: environment.Environment

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
        STORE = "store"

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
        status: NotRequired["Order.OrderLineItemStatus"]
        entity_type: Required["Order.OrderLineItemEntityType"]
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
        discount_type: Required["Order.LineItemDiscountDiscountType"]
        coupon_id: NotRequired[str]
        entity_id: NotRequired[str]
        discount_amount: Required[int]

    class LinkedCreditNote(TypedDict):
        amount: NotRequired[int]
        type: Required["Order.OrderLineItemLinkedCreditType"]
        id: Required[str]
        status: Required["Order.OrderLineItemLinkedCreditStatus"]
        amount_adjusted: NotRequired[int]
        amount_refunded: NotRequired[int]

    class ResentOrder(TypedDict):
        order_id: Required[str]
        reason: NotRequired[str]
        amount: NotRequired[int]

    class UpdateOrderLineItemParams(TypedDict):
        id: NotRequired[str]
        status: NotRequired["Order.OrderLineItemStatus"]
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
        reason_code: Required["credit_note.CreditNote.ReasonCode"]
        total: Required[int]

    class ResendOrderLineItemParams(TypedDict):
        id: NotRequired[str]
        fulfillment_quantity: NotRequired[int]

    class CreateParams(TypedDict):
        id: NotRequired[str]
        invoice_id: Required[str]
        status: NotRequired["Order.Status"]
        reference_id: NotRequired[str]
        fulfillment_status: NotRequired[str]
        note: NotRequired[str]
        tracking_id: NotRequired[str]
        tracking_url: NotRequired[str]
        batch_id: NotRequired[str]

    class UpdateParams(TypedDict):
        reference_id: NotRequired[str]
        batch_id: NotRequired[str]
        note: NotRequired[str]
        shipping_date: NotRequired[int]
        order_date: NotRequired[int]
        cancelled_at: NotRequired[int]
        cancellation_reason: NotRequired["Order.CancellationReason"]
        shipped_at: NotRequired[int]
        delivered_at: NotRequired[int]
        order_line_items: NotRequired[List["Order.UpdateOrderLineItemParams"]]
        tracking_url: NotRequired[str]
        tracking_id: NotRequired[str]
        shipment_carrier: NotRequired[str]
        fulfillment_status: NotRequired[str]
        status: NotRequired["Order.Status"]
        shipping_address: NotRequired["Order.UpdateShippingAddressParams"]

    class ImportOrderParams(TypedDict):
        id: NotRequired[str]
        document_number: NotRequired[str]
        invoice_id: Required[str]
        status: Required["Order.Status"]
        subscription_id: NotRequired[str]
        customer_id: NotRequired[str]
        created_at: Required[int]
        order_date: Required[int]
        shipping_date: Required[int]
        reference_id: NotRequired[str]
        fulfillment_status: NotRequired[str]
        note: NotRequired[str]
        tracking_id: NotRequired[str]
        tracking_url: NotRequired[str]
        batch_id: NotRequired[str]
        shipment_carrier: NotRequired[str]
        shipping_cut_off_date: NotRequired[int]
        delivered_at: NotRequired[int]
        shipped_at: NotRequired[int]
        cancelled_at: NotRequired[int]
        cancellation_reason: NotRequired["Order.CancellationReason"]
        refundable_credits_issued: NotRequired[int]
        shipping_address: NotRequired["Order.ImportOrderShippingAddressParams"]
        billing_address: NotRequired["Order.ImportOrderBillingAddressParams"]

    class CancelParams(TypedDict):
        cancellation_reason: Required["Order.CancellationReason"]
        credit_note: NotRequired["Order.CancelCreditNoteParams"]
        customer_notes: NotRequired[str]
        comment: NotRequired[str]
        cancelled_at: NotRequired[int]

    class CreateRefundableCreditNoteParams(TypedDict):
        credit_note: Required["Order.CreateRefundableCreditNoteCreditNoteParams"]
        customer_notes: NotRequired[str]
        comment: NotRequired[str]

    class ReopenParams(TypedDict):
        void_cancellation_credit_notes: NotRequired[bool]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        include_deleted: NotRequired[bool]
        exclude_deleted_credit_notes: NotRequired[bool]
        id: NotRequired[Filters.StringFilter]
        invoice_id: NotRequired[Filters.StringFilter]
        subscription_id: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]
        shipping_date: NotRequired[Filters.TimestampFilter]
        shipped_at: NotRequired[Filters.TimestampFilter]
        order_type: NotRequired[Filters.EnumFilter]
        order_date: NotRequired[Filters.TimestampFilter]
        paid_on: NotRequired[Filters.TimestampFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        resent_status: NotRequired[Filters.EnumFilter]
        is_resent: NotRequired[Filters.BooleanFilter]
        original_order_id: NotRequired[Filters.StringFilter]
        sort_by: NotRequired[Filters.SortFilter]

    class OrdersForInvoiceParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class ResendParams(TypedDict):
        shipping_date: NotRequired[int]
        resend_reason: NotRequired[str]
        order_line_items: NotRequired[List["Order.ResendOrderLineItemParams"]]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("orders"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update(self, id, params: UpdateParams = None, headers=None) -> UpdateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("orders", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def import_order(
        self, params: ImportOrderParams, headers=None
    ) -> ImportOrderResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("orders", "import_order"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ImportOrderResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def assign_order_number(self, id, headers=None) -> AssignOrderNumberResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("orders", id, "assign_order_number"),
            self.env,
            None,
            headers,
            AssignOrderNumberResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def cancel(self, id, params: CancelParams, headers=None) -> CancelResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("orders", id, "cancel"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CancelResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_refundable_credit_note(
        self, id, params: CreateRefundableCreditNoteParams, headers=None
    ) -> CreateRefundableCreditNoteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("orders", id, "create_refundable_credit_note"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateRefundableCreditNoteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def reopen(self, id, params: ReopenParams = None, headers=None) -> ReopenResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("orders", id, "reopen"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ReopenResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("orders", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("orders", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("orders"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def orders_for_invoice(
        self, id, params: OrdersForInvoiceParams = None, headers=None
    ) -> OrdersForInvoiceResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("invoices", id, "orders"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            OrdersForInvoiceResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def resend(self, id, params: ResendParams = None, headers=None) -> ResendResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("orders", id, "resend"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ResendResponse,
            None,
            False,
            jsonKeys,
            options,
        )
