from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any


class CreditNote:

    class CreateParams(TypedDict):
        reference_invoice_id: NotRequired[str]
        customer_id: NotRequired[str]
        total: NotRequired[int]
        type: Required[Type]
        reason_code: NotRequired[ReasonCode]
        create_reason_code: NotRequired[str]
        date: NotRequired[int]
        customer_notes: NotRequired[str]
        currency_code: NotRequired[str]
        line_items: NotRequired[List[CreateLineItemParams]]
        comment: NotRequired[str]

    class PdfParams(TypedDict):
        disposition_type: NotRequired[enums.DispositionType]

    class RefundParams(TypedDict):
        refund_amount: NotRequired[int]
        customer_notes: NotRequired[str]
        refund_reason_code: NotRequired[str]

    class RecordRefundParams(TypedDict):
        transaction: Required[RecordRefundTransactionParams]
        refund_reason_code: NotRequired[str]
        comment: NotRequired[str]

    class VoidCreditNoteParams(TypedDict):
        comment: NotRequired[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        einvoice: NotRequired[ListEinvoiceParams]
        include_deleted: NotRequired[bool]
        id: NotRequired[Filters.StringFilter]
        customer_id: NotRequired[Filters.StringFilter]
        subscription_id: NotRequired[Filters.StringFilter]
        reference_invoice_id: NotRequired[Filters.StringFilter]
        type: NotRequired[Filters.EnumFilter]
        reason_code: NotRequired[Filters.EnumFilter]
        create_reason_code: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]
        date: NotRequired[Filters.TimestampFilter]
        total: NotRequired[Filters.NumberFilter]
        price_type: NotRequired[Filters.EnumFilter]
        amount_allocated: NotRequired[Filters.NumberFilter]
        amount_refunded: NotRequired[Filters.NumberFilter]
        amount_available: NotRequired[Filters.NumberFilter]
        voided_at: NotRequired[Filters.TimestampFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]
        channel: NotRequired[Filters.EnumFilter]

    class CreditNotesForCustomerParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class DeleteParams(TypedDict):
        comment: NotRequired[str]

    class RemoveTaxWithheldRefundParams(TypedDict):
        tax_withheld: Required[RemoveTaxWithheldRefundTaxWithheldParams]

    class ImportCreditNoteParams(TypedDict):
        id: Required[str]
        customer_id: NotRequired[str]
        subscription_id: NotRequired[str]
        reference_invoice_id: Required[str]
        type: Required[Type]
        currency_code: NotRequired[str]
        create_reason_code: Required[str]
        date: Required[int]
        status: NotRequired[Status]
        total: NotRequired[int]
        refunded_at: NotRequired[int]
        voided_at: NotRequired[int]
        sub_total: NotRequired[int]
        round_off_amount: NotRequired[int]
        fractional_correction: NotRequired[int]
        vat_number_prefix: NotRequired[str]
        line_items: Required[List[ImportCreditNoteLineItemParams]]
        line_item_tiers: Required[List[ImportCreditNoteLineItemTierParams]]
        discounts: Required[List[ImportCreditNoteDiscountParams]]
        taxes: Required[List[ImportCreditNoteTaxParams]]
        allocations: Required[List[ImportCreditNoteAllocationParams]]
        linked_refunds: Required[List[ImportCreditNoteLinkedRefundParams]]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("credit_notes"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("credit_notes", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def pdf(id, params: PdfParams = None, env=None, headers=None) -> PdfResponse:
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "pdf"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            PdfResponse,
        )

    @staticmethod
    def download_einvoice(id, env=None, headers=None) -> DownloadEinvoiceResponse:
        return request.send(
            "get",
            request.uri_path("credit_notes", id, "download_einvoice"),
            None,
            env,
            headers,
            DownloadEinvoiceResponse,
        )

    @staticmethod
    def refund(
        id, params: RefundParams = None, env=None, headers=None
    ) -> RefundResponse:
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "refund"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RefundResponse,
        )

    @staticmethod
    def record_refund(
        id, params: RecordRefundParams, env=None, headers=None
    ) -> RecordRefundResponse:
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "record_refund"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RecordRefundResponse,
        )

    @staticmethod
    def void_credit_note(
        id, params: VoidCreditNoteParams = None, env=None, headers=None
    ) -> VoidCreditNoteResponse:
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "void"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            VoidCreditNoteResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("credit_notes"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def credit_notes_for_customer(
        id, params: CreditNotesForCustomerParams = None, env=None, headers=None
    ) -> CreditNotesForCustomerResponse:
        return request.send(
            "get",
            request.uri_path("customers", id, "credit_notes"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreditNotesForCustomerResponse,
        )

    @staticmethod
    def delete(
        id, params: DeleteParams = None, env=None, headers=None
    ) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "delete"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def remove_tax_withheld_refund(
        id, params: RemoveTaxWithheldRefundParams, env=None, headers=None
    ) -> RemoveTaxWithheldRefundResponse:
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "remove_tax_withheld_refund"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RemoveTaxWithheldRefundResponse,
        )

    @staticmethod
    def resend_einvoice(id, env=None, headers=None) -> ResendEinvoiceResponse:
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "resend_einvoice"),
            None,
            env,
            headers,
            ResendEinvoiceResponse,
        )

    @staticmethod
    def send_einvoice(id, env=None, headers=None) -> SendEinvoiceResponse:
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "send_einvoice"),
            None,
            env,
            headers,
            SendEinvoiceResponse,
        )

    @staticmethod
    def import_credit_note(
        params: ImportCreditNoteParams, env=None, headers=None
    ) -> ImportCreditNoteResponse:
        return request.send(
            "post",
            request.uri_path("credit_notes", "import_credit_note"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ImportCreditNoteResponse,
        )
