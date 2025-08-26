from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


@dataclass
class PaymentVoucher:
    env: environment.Environment

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

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_vouchers"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
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
            request.uri_path("payment_vouchers", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def payment_vouchers_for_invoice(
        self, id, params: PaymentVouchersForInvoiceParams = None, headers=None
    ) -> PaymentVouchersForInvoiceResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("invoices", id, "payment_vouchers"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PaymentVouchersForInvoiceResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def payment_vouchers_for_customer(
        self, id, params: PaymentVouchersForCustomerParams = None, headers=None
    ) -> PaymentVouchersForCustomerResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("customers", id, "payment_vouchers"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PaymentVouchersForCustomerResponse,
            None,
            False,
            jsonKeys,
            options,
        )
