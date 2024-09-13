from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class Order:

    class CreateParams(TypedDict):
        id: NotRequired[str]
        invoice_id: Required[str]
        status: NotRequired[Status]
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
        cancellation_reason: NotRequired[CancellationReason]
        shipped_at: NotRequired[int]
        delivered_at: NotRequired[int]
        order_line_items: NotRequired[List[UpdateOrderLineItemParams]]
        tracking_url: NotRequired[str]
        tracking_id: NotRequired[str]
        shipment_carrier: NotRequired[str]
        fulfillment_status: NotRequired[str]
        status: NotRequired[Status]
        shipping_address: NotRequired[UpdateShippingAddressParams]

    class ImportOrderParams(TypedDict):
        id: NotRequired[str]
        document_number: NotRequired[str]
        invoice_id: Required[str]
        status: Required[Status]
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
        cancellation_reason: NotRequired[CancellationReason]
        refundable_credits_issued: NotRequired[int]
        shipping_address: NotRequired[ImportOrderShippingAddressParams]
        billing_address: NotRequired[ImportOrderBillingAddressParams]

    class CancelParams(TypedDict):
        cancellation_reason: Required[CancellationReason]
        credit_note: NotRequired[CancelCreditNoteParams]
        customer_notes: NotRequired[str]
        comment: NotRequired[str]
        cancelled_at: NotRequired[int]

    class CreateRefundableCreditNoteParams(TypedDict):
        credit_note: Required[CreateRefundableCreditNoteCreditNoteParams]
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
        order_line_items: NotRequired[List[ResendOrderLineItemParams]]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("orders"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def update(
        id, params: UpdateParams = None, env=None, headers=None
    ) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("orders", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def import_order(
        params: ImportOrderParams, env=None, headers=None
    ) -> ImportOrderResponse:
        return request.send(
            "post",
            request.uri_path("orders", "import_order"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ImportOrderResponse,
        )

    @staticmethod
    def assign_order_number(id, env=None, headers=None) -> AssignOrderNumberResponse:
        return request.send(
            "post",
            request.uri_path("orders", id, "assign_order_number"),
            None,
            env,
            headers,
            AssignOrderNumberResponse,
        )

    @staticmethod
    def cancel(id, params: CancelParams, env=None, headers=None) -> CancelResponse:
        return request.send(
            "post",
            request.uri_path("orders", id, "cancel"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CancelResponse,
        )

    @staticmethod
    def create_refundable_credit_note(
        id, params: CreateRefundableCreditNoteParams, env=None, headers=None
    ) -> CreateRefundableCreditNoteResponse:
        return request.send(
            "post",
            request.uri_path("orders", id, "create_refundable_credit_note"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateRefundableCreditNoteResponse,
        )

    @staticmethod
    def reopen(
        id, params: ReopenParams = None, env=None, headers=None
    ) -> ReopenResponse:
        return request.send(
            "post",
            request.uri_path("orders", id, "reopen"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ReopenResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get", request.uri_path("orders", id), None, env, headers, RetrieveResponse
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("orders", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("orders"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def orders_for_invoice(
        id, params: OrdersForInvoiceParams = None, env=None, headers=None
    ) -> OrdersForInvoiceResponse:
        return request.send(
            "get",
            request.uri_path("invoices", id, "orders"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            OrdersForInvoiceResponse,
        )

    @staticmethod
    def resend(
        id, params: ResendParams = None, env=None, headers=None
    ) -> ResendResponse:
        return request.send(
            "post",
            request.uri_path("orders", id, "resend"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ResendResponse,
        )
