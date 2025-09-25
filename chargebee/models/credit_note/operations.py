from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums, invoice, transaction


@dataclass
class CreditNote:
    env: environment.Environment

    class Type(Enum):
        ADJUSTMENT = "adjustment"
        REFUNDABLE = "refundable"
        STORE = "store"

        def __str__(self):
            return self.value

    class ReasonCode(Enum):
        WRITE_OFF = "write_off"
        SUBSCRIPTION_CHANGE = "subscription_change"
        SUBSCRIPTION_CANCELLATION = "subscription_cancellation"
        SUBSCRIPTION_PAUSE = "subscription_pause"
        CHARGEBACK = "chargeback"
        PRODUCT_UNSATISFACTORY = "product_unsatisfactory"
        SERVICE_UNSATISFACTORY = "service_unsatisfactory"
        ORDER_CHANGE = "order_change"
        ORDER_CANCELLATION = "order_cancellation"
        WAIVER = "waiver"
        OTHER = "other"
        FRAUDULENT = "fraudulent"

        def __str__(self):
            return self.value

    class Status(Enum):
        ADJUSTED = "adjusted"
        REFUNDED = "refunded"
        REFUND_DUE = "refund_due"
        VOIDED = "voided"

        def __str__(self):
            return self.value

    class LineItemEntityType(Enum):
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
        ITEM_LEVEL_DISCOUNT = "item_level_discount"
        DOCUMENT_LEVEL_DISCOUNT = "document_level_discount"

        def __str__(self):
            return self.value

    class DiscountEntityType(Enum):
        ITEM_LEVEL_COUPON = "item_level_coupon"
        DOCUMENT_LEVEL_COUPON = "document_level_coupon"
        PROMOTIONAL_CREDITS = "promotional_credits"
        PRORATED_CREDITS = "prorated_credits"
        ITEM_LEVEL_DISCOUNT = "item_level_discount"
        DOCUMENT_LEVEL_DISCOUNT = "document_level_discount"

        def __str__(self):
            return self.value

    class DiscountDiscountType(Enum):
        FIXED_AMOUNT = "fixed_amount"
        PERCENTAGE = "percentage"

        def __str__(self):
            return self.value

    class AppliedCreditTaxApplication(Enum):
        PRE_TAX = "pre_tax"
        POST_TAX = "post_tax"

        def __str__(self):
            return self.value

    class EinvoiceStatus(Enum):
        SCHEDULED = "scheduled"
        SKIPPED = "skipped"
        IN_PROGRESS = "in_progress"
        SUCCESS = "success"
        FAILED = "failed"
        REGISTERED = "registered"

        def __str__(self):
            return self.value

    class LineItem(TypedDict):
        id: NotRequired[str]
        subscription_id: NotRequired[str]
        date_from: Required[int]
        date_to: Required[int]
        unit_amount: Required[int]
        quantity: NotRequired[int]
        amount: NotRequired[int]
        pricing_model: NotRequired[enums.PricingModel]
        is_taxed: Required[bool]
        tax_amount: NotRequired[int]
        tax_rate: NotRequired[float]
        unit_amount_in_decimal: NotRequired[str]
        quantity_in_decimal: NotRequired[str]
        amount_in_decimal: NotRequired[str]
        discount_amount: NotRequired[int]
        item_level_discount_amount: NotRequired[int]
        metered: NotRequired[bool]
        is_percentage_pricing: NotRequired[bool]
        reference_line_item_id: NotRequired[str]
        description: Required[str]
        entity_description: NotRequired[str]
        entity_type: Required["CreditNote.LineItemEntityType"]
        tax_exempt_reason: NotRequired[enums.TaxExemptReason]
        entity_id: NotRequired[str]
        customer_id: NotRequired[str]

    class LineItemTier(TypedDict):
        line_item_id: NotRequired[str]
        starting_unit: Required[int]
        ending_unit: NotRequired[int]
        quantity_used: Required[int]
        unit_amount: Required[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        quantity_used_in_decimal: NotRequired[str]
        unit_amount_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

    class LineItemDiscount(TypedDict):
        line_item_id: Required[str]
        discount_type: Required["CreditNote.LineItemDiscountDiscountType"]
        coupon_id: NotRequired[str]
        entity_id: NotRequired[str]
        discount_amount: Required[int]

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

    class LineItemAddress(TypedDict):
        line_item_id: NotRequired[str]
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

    class Discount(TypedDict):
        amount: Required[int]
        description: NotRequired[str]
        entity_type: Required["CreditNote.DiscountEntityType"]
        discount_type: NotRequired["CreditNote.DiscountDiscountType"]
        entity_id: NotRequired[str]
        coupon_set_code: NotRequired[str]

    class Tax(TypedDict):
        name: Required[str]
        amount: Required[int]
        description: NotRequired[str]

    class TaxOrigin(TypedDict):
        country: NotRequired[str]
        registration_number: NotRequired[str]

    class LinkedRefund(TypedDict):
        txn_id: Required[str]
        applied_amount: Required[int]
        applied_at: Required[int]
        txn_status: NotRequired["transaction.Transaction.Status"]
        txn_date: NotRequired[int]
        txn_amount: NotRequired[int]
        refund_reason_code: NotRequired[str]

    class Allocation(TypedDict):
        invoice_id: Required[str]
        allocated_amount: Required[int]
        allocated_at: Required[int]
        invoice_date: NotRequired[int]
        invoice_status: Required["invoice.Invoice.Status"]
        tax_application: NotRequired["CreditNote.AppliedCreditTaxApplication"]

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

    class Einvoice(TypedDict):
        id: Required[str]
        reference_number: NotRequired[str]
        status: Required["CreditNote.EinvoiceStatus"]
        message: NotRequired[str]

    class SiteDetailsAtCreation(TypedDict):
        timezone: NotRequired[str]
        organization_address: NotRequired[Dict[Any, Any]]

    class CreateLineItemParams(TypedDict):
        reference_line_item_id: NotRequired[str]
        unit_amount: NotRequired[int]
        unit_amount_in_decimal: NotRequired[str]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        amount: NotRequired[int]
        date_from: NotRequired[int]
        date_to: NotRequired[int]
        description: NotRequired[str]
        entity_type: NotRequired["CreditNote.LineItemEntityType"]
        entity_id: NotRequired[str]

    class RetrieveLineItemParams(TypedDict):
        subscription_id: NotRequired[Filters.StringFilter]
        customer_id: NotRequired[Filters.StringFilter]

    class RecordRefundTransactionParams(TypedDict):
        id: NotRequired[str]
        amount: NotRequired[int]
        payment_method: Required[enums.PaymentMethod]
        reference_number: NotRequired[str]
        custom_payment_method_id: NotRequired[str]
        date: Required[int]

    class ListEinvoiceParams(TypedDict):
        status: NotRequired[Filters.EnumFilter]

    class RemoveTaxWithheldRefundTaxWithheldParams(TypedDict):
        id: Required[str]

    class ImportCreditNoteLineItemParams(TypedDict):
        reference_line_item_id: NotRequired[str]
        id: NotRequired[str]
        date_from: NotRequired[int]
        date_to: NotRequired[int]
        subscription_id: NotRequired[str]
        description: Required[str]
        unit_amount: NotRequired[int]
        quantity: NotRequired[int]
        amount: NotRequired[int]
        unit_amount_in_decimal: NotRequired[str]
        quantity_in_decimal: NotRequired[str]
        amount_in_decimal: NotRequired[str]
        entity_type: NotRequired["CreditNote.LineItemEntityType"]
        entity_id: NotRequired[str]
        item_level_discount1_entity_id: NotRequired[str]
        item_level_discount1_amount: NotRequired[int]
        item_level_discount2_entity_id: NotRequired[str]
        item_level_discount2_amount: NotRequired[int]
        tax1_name: NotRequired[str]
        tax1_amount: NotRequired[int]
        tax2_name: NotRequired[str]
        tax2_amount: NotRequired[int]
        tax3_name: NotRequired[str]
        tax3_amount: NotRequired[int]
        tax4_name: NotRequired[str]
        tax4_amount: NotRequired[int]
        tax5_name: NotRequired[str]
        tax5_amount: NotRequired[int]
        tax6_name: NotRequired[str]
        tax6_amount: NotRequired[int]
        tax7_name: NotRequired[str]
        tax7_amount: NotRequired[int]
        tax8_name: NotRequired[str]
        tax8_amount: NotRequired[int]
        tax9_name: NotRequired[str]
        tax9_amount: NotRequired[int]
        tax10_name: NotRequired[str]
        tax10_amount: NotRequired[int]

    class ImportCreditNoteLineItemTierParams(TypedDict):
        line_item_id: Required[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        quantity_used: NotRequired[int]
        unit_amount: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        quantity_used_in_decimal: NotRequired[str]
        unit_amount_in_decimal: NotRequired[str]

    class ImportCreditNoteDiscountParams(TypedDict):
        entity_type: Required["CreditNote.DiscountEntityType"]
        entity_id: NotRequired[str]
        description: NotRequired[str]
        amount: Required[int]

    class ImportCreditNoteTaxParams(TypedDict):
        name: Required[str]
        rate: Required[float]
        amount: NotRequired[int]
        description: NotRequired[str]
        juris_type: NotRequired[enums.TaxJurisType]
        juris_name: NotRequired[str]
        juris_code: NotRequired[str]

    class ImportCreditNoteAllocationParams(TypedDict):
        invoice_id: Required[str]
        allocated_amount: Required[int]
        allocated_at: Required[int]

    class ImportCreditNoteLinkedRefundParams(TypedDict):
        id: NotRequired[str]
        amount: Required[int]
        payment_method: Required[enums.PaymentMethod]
        date: Required[int]
        reference_number: NotRequired[str]

    class CreateParams(TypedDict):
        reference_invoice_id: NotRequired[str]
        customer_id: NotRequired[str]
        total: NotRequired[int]
        type: Required["CreditNote.Type"]
        reason_code: NotRequired["CreditNote.ReasonCode"]
        create_reason_code: NotRequired[str]
        date: NotRequired[int]
        customer_notes: NotRequired[str]
        currency_code: NotRequired[str]
        line_items: NotRequired[List["CreditNote.CreateLineItemParams"]]
        comment: NotRequired[str]

    class RetrieveParams(TypedDict):
        line_item: NotRequired["CreditNote.RetrieveLineItemParams"]

    class PdfParams(TypedDict):
        disposition_type: NotRequired[enums.DispositionType]

    class RefundParams(TypedDict):
        refund_amount: NotRequired[int]
        customer_notes: NotRequired[str]
        refund_reason_code: NotRequired[str]

    class RecordRefundParams(TypedDict):
        transaction: Required["CreditNote.RecordRefundTransactionParams"]
        refund_reason_code: NotRequired[str]
        comment: NotRequired[str]

    class VoidCreditNoteParams(TypedDict):
        comment: NotRequired[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        einvoice: NotRequired["CreditNote.ListEinvoiceParams"]
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
        tax_withheld: Required["CreditNote.RemoveTaxWithheldRefundTaxWithheldParams"]

    class ImportCreditNoteParams(TypedDict):
        id: Required[str]
        customer_id: NotRequired[str]
        subscription_id: NotRequired[str]
        reference_invoice_id: Required[str]
        type: Required["CreditNote.Type"]
        currency_code: NotRequired[str]
        create_reason_code: Required[str]
        date: Required[int]
        status: NotRequired["CreditNote.Status"]
        total: NotRequired[int]
        refunded_at: NotRequired[int]
        voided_at: NotRequired[int]
        sub_total: NotRequired[int]
        round_off_amount: NotRequired[int]
        fractional_correction: NotRequired[int]
        vat_number_prefix: NotRequired[str]
        line_items: Required[List["CreditNote.ImportCreditNoteLineItemParams"]]
        line_item_tiers: Required[List["CreditNote.ImportCreditNoteLineItemTierParams"]]
        discounts: Required[List["CreditNote.ImportCreditNoteDiscountParams"]]
        taxes: Required[List["CreditNote.ImportCreditNoteTaxParams"]]
        allocations: Required[List["CreditNote.ImportCreditNoteAllocationParams"]]
        linked_refunds: Required[List["CreditNote.ImportCreditNoteLinkedRefundParams"]]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("credit_notes"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve(
        self, id, params: RetrieveParams = None, headers=None
    ) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("credit_notes", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def pdf(self, id, params: PdfParams = None, headers=None) -> PdfResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "pdf"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PdfResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def download_einvoice(self, id, headers=None) -> DownloadEinvoiceResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("credit_notes", id, "download_einvoice"),
            self.env,
            None,
            headers,
            DownloadEinvoiceResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def refund(self, id, params: RefundParams = None, headers=None) -> RefundResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "refund"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RefundResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def record_refund(
        self, id, params: RecordRefundParams, headers=None
    ) -> RecordRefundResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "record_refund"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RecordRefundResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def void_credit_note(
        self, id, params: VoidCreditNoteParams = None, headers=None
    ) -> VoidCreditNoteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "void"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            VoidCreditNoteResponse,
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
            request.uri_path("credit_notes"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def credit_notes_for_customer(
        self, id, params: CreditNotesForCustomerParams = None, headers=None
    ) -> CreditNotesForCustomerResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("customers", id, "credit_notes"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreditNotesForCustomerResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def delete(self, id, params: DeleteParams = None, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "delete"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def remove_tax_withheld_refund(
        self, id, params: RemoveTaxWithheldRefundParams, headers=None
    ) -> RemoveTaxWithheldRefundResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "remove_tax_withheld_refund"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RemoveTaxWithheldRefundResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def resend_einvoice(self, id, headers=None) -> ResendEinvoiceResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "resend_einvoice"),
            self.env,
            None,
            headers,
            ResendEinvoiceResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def send_einvoice(self, id, headers=None) -> SendEinvoiceResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("credit_notes", id, "send_einvoice"),
            self.env,
            None,
            headers,
            SendEinvoiceResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def import_credit_note(
        self, params: ImportCreditNoteParams, headers=None
    ) -> ImportCreditNoteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("credit_notes", "import_credit_note"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ImportCreditNoteResponse,
            None,
            False,
            jsonKeys,
            options,
        )
