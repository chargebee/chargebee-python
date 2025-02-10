from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums, credit_note, invoice, transaction


@dataclass
class Transaction:

    env: environment.Environment

    class Type(Enum):
        AUTHORIZATION = "authorization"
        PAYMENT = "payment"
        REFUND = "refund"
        PAYMENT_REVERSAL = "payment_reversal"

        def __str__(self):
            return self.value

    class Status(Enum):
        IN_PROGRESS = "in_progress"
        SUCCESS = "success"
        VOIDED = "voided"
        FAILURE = "failure"
        TIMEOUT = "timeout"
        NEEDS_ATTENTION = "needs_attention"
        LATE_FAILURE = "late_failure"

        def __str__(self):
            return self.value

    class FraudFlag(Enum):
        SAFE = "safe"
        SUSPICIOUS = "suspicious"
        FRAUDULENT = "fraudulent"

        def __str__(self):
            return self.value

    class InitiatorType(Enum):
        CUSTOMER = "customer"
        MERCHANT = "merchant"

        def __str__(self):
            return self.value

    class AuthorizationReason(Enum):
        BLOCKING_FUNDS = "blocking_funds"
        VERIFICATION = "verification"

        def __str__(self):
            return self.value

    class LinkedPaymentStatus(Enum):
        IN_PROGRESS = "in_progress"
        SUCCESS = "success"
        VOIDED = "voided"
        FAILURE = "failure"
        TIMEOUT = "timeout"
        NEEDS_ATTENTION = "needs_attention"
        LATE_FAILURE = "late_failure"

        def __str__(self):
            return self.value

    class LinkedInvoice(TypedDict):
        invoice_id: Required[str]
        applied_amount: Required[int]
        applied_at: Required[int]
        invoice_date: NotRequired[int]
        invoice_total: NotRequired[int]
        invoice_status: Required["invoice.Invoice.Status"]

    class LinkedCreditNote(TypedDict):
        cn_id: Required[str]
        applied_amount: Required[int]
        applied_at: Required[int]
        cn_reason_code: NotRequired["credit_note.CreditNote.ReasonCode"]
        cn_create_reason_code: NotRequired[str]
        cn_date: NotRequired[int]
        cn_total: NotRequired[int]
        cn_status: Required["credit_note.CreditNote.Status"]
        cn_reference_invoice_id: NotRequired[str]

    class LinkedRefund(TypedDict):
        txn_id: Required[str]
        txn_status: Required["transaction.Transaction.Status"]
        txn_date: Required[int]
        txn_amount: Required[int]

    class LinkedPayment(TypedDict):
        id: Required[str]
        status: NotRequired["Transaction.LinkedPaymentStatus"]
        amount: NotRequired[int]
        date: NotRequired[int]

    class GatewayErrorDetail(TypedDict):
        request_id: NotRequired[str]
        error_category: NotRequired[str]
        error_code: NotRequired[str]
        error_message: NotRequired[str]
        decline_code: NotRequired[str]
        decline_message: NotRequired[str]
        network_error_code: NotRequired[str]
        network_error_message: NotRequired[str]
        error_field: NotRequired[str]
        recommendation_code: NotRequired[str]
        recommendation_message: NotRequired[str]
        processor_error_code: NotRequired[str]
        processor_error_message: NotRequired[str]
        error_cause_id: NotRequired[str]

    class CreateAuthorizationParams(TypedDict):
        customer_id: Required[str]
        payment_source_id: NotRequired[str]
        currency_code: NotRequired[str]
        amount: Required[int]

    class RecordRefundParams(TypedDict):
        amount: NotRequired[int]
        payment_method: Required[enums.PaymentMethod]
        date: Required[int]
        reference_number: NotRequired[str]
        custom_payment_method_id: NotRequired[str]
        comment: NotRequired[str]

    class ReconcileParams(TypedDict):
        id_at_gateway: NotRequired[str]
        customer_id: NotRequired[str]
        status: NotRequired["Transaction.Status"]

    class RefundParams(TypedDict):
        amount: NotRequired[int]
        comment: NotRequired[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        include_deleted: NotRequired[bool]
        id: NotRequired[Filters.StringFilter]
        customer_id: NotRequired[Filters.StringFilter]
        subscription_id: NotRequired[Filters.StringFilter]
        payment_source_id: NotRequired[Filters.StringFilter]
        payment_method: NotRequired[Filters.EnumFilter]
        gateway: NotRequired[Filters.EnumFilter]
        gateway_account_id: NotRequired[Filters.StringFilter]
        id_at_gateway: NotRequired[Filters.StringFilter]
        reference_number: NotRequired[Filters.StringFilter]
        type: NotRequired[Filters.EnumFilter]
        date: NotRequired[Filters.TimestampFilter]
        amount: NotRequired[Filters.NumberFilter]
        amount_capturable: NotRequired[Filters.NumberFilter]
        status: NotRequired[Filters.EnumFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]

    class TransactionsForCustomerParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class TransactionsForSubscriptionParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class PaymentsForInvoiceParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class DeleteOfflineTransactionParams(TypedDict):
        comment: NotRequired[str]

    def create_authorization(
        self, params: CreateAuthorizationParams, headers=None
    ) -> CreateAuthorizationResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("transactions", "create_authorization"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateAuthorizationResponse,
            None,
            False,
            jsonKeys,
        )

    def void_transaction(self, id, headers=None) -> VoidTransactionResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("transactions", id, "void"),
            self.env,
            None,
            headers,
            VoidTransactionResponse,
            None,
            False,
            jsonKeys,
        )

    def record_refund(
        self, id, params: RecordRefundParams, headers=None
    ) -> RecordRefundResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("transactions", id, "record_refund"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RecordRefundResponse,
            None,
            False,
            jsonKeys,
        )

    def reconcile(
        self, id, params: ReconcileParams = None, headers=None
    ) -> ReconcileResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("transactions", id, "reconcile"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ReconcileResponse,
            None,
            False,
            jsonKeys,
        )

    def refund(self, id, params: RefundParams = None, headers=None) -> RefundResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("transactions", id, "refund"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RefundResponse,
            None,
            False,
            jsonKeys,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        return request.send_list_request(
            "get",
            request.uri_path("transactions"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
        )

    def transactions_for_customer(
        self, id, params: TransactionsForCustomerParams = None, headers=None
    ) -> TransactionsForCustomerResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("customers", id, "transactions"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            TransactionsForCustomerResponse,
            None,
            False,
            jsonKeys,
        )

    def transactions_for_subscription(
        self, id, params: TransactionsForSubscriptionParams = None, headers=None
    ) -> TransactionsForSubscriptionResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "transactions"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            TransactionsForSubscriptionResponse,
            None,
            False,
            jsonKeys,
        )

    def payments_for_invoice(
        self, id, params: PaymentsForInvoiceParams = None, headers=None
    ) -> PaymentsForInvoiceResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("invoices", id, "payments"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PaymentsForInvoiceResponse,
            None,
            False,
            jsonKeys,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("transactions", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
        )

    def delete_offline_transaction(
        self, id, params: DeleteOfflineTransactionParams = None, headers=None
    ) -> DeleteOfflineTransactionResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("transactions", id, "delete_offline_transaction"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeleteOfflineTransactionResponse,
            None,
            False,
            jsonKeys,
        )
