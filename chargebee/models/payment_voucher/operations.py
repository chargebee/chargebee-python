from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


class PaymentVoucher:
    class Status(Enum):
        ACTIVE = "active"
        CONSUMED = "consumed"
        EXPIRED = "expired"
        FAILURE = "failure"

        def __str__(self):
            return self.value

    class LinkedInvoice(TypedDict):
        invoice_id: Required[str]
        txn_id: Required[str]
        applied_at: Required[int]

    class CreateVoucherPaymentSourceParams(TypedDict):
        voucher_type: Required[enums.VoucherType]

    class CreateInvoiceAllocationParams(TypedDict):
        invoice_id: Required[str]

    class CreateParams(TypedDict):
        customer_id: Required[str]
        voucher_payment_source: Required[
            "PaymentVoucher.CreateVoucherPaymentSourceParams"
        ]
        invoice_allocations: Required[
            List["PaymentVoucher.CreateInvoiceAllocationParams"]
        ]
        payment_source_id: NotRequired[str]

    class PaymentVouchersForInvoiceParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        status: NotRequired[Filters.EnumFilter]
        sort_by: NotRequired[Filters.SortFilter]

    class PaymentVouchersForCustomerParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        status: NotRequired[Filters.EnumFilter]
        sort_by: NotRequired[Filters.SortFilter]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("payment_vouchers"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("payment_vouchers", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def payment_vouchers_for_invoice(
        id, params: PaymentVouchersForInvoiceParams = None, env=None, headers=None
    ) -> PaymentVouchersForInvoiceResponse:
        return request.send(
            "get",
            request.uri_path("invoices", id, "payment_vouchers"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            PaymentVouchersForInvoiceResponse,
        )

    @staticmethod
    def payment_vouchers_for_customer(
        id, params: PaymentVouchersForCustomerParams = None, env=None, headers=None
    ) -> PaymentVouchersForCustomerResponse:
        return request.send(
            "get",
            request.uri_path("customers", id, "payment_vouchers"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            PaymentVouchersForCustomerResponse,
        )
