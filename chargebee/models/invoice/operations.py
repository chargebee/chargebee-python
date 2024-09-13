from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any


class Invoice:

    class CreateParams(TypedDict):
        customer_id: NotRequired[str]
        subscription_id: NotRequired[str]
        currency_code: NotRequired[str]
        addons: NotRequired[List[CreateAddonParams]]
        invoice_date: NotRequired[int]
        charges: NotRequired[List[CreateChargeParams]]
        tax_providers_fields: NotRequired[List[CreateTaxProvidersFieldParams]]
        invoice_note: NotRequired[str]
        remove_general_note: NotRequired[bool]
        notes_to_remove: NotRequired[List[CreateNotesToRemoveParams]]
        po_number: NotRequired[str]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        authorization_transaction_id: NotRequired[str]
        payment_source_id: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        shipping_address: NotRequired[CreateShippingAddressParams]
        statement_descriptor: NotRequired[CreateStatementDescriptorParams]
        card: NotRequired[CreateCardParams]
        bank_account: NotRequired[CreateBankAccountParams]
        token_id: NotRequired[str]
        payment_method: NotRequired[CreatePaymentMethodParams]
        payment_intent: NotRequired[CreatePaymentIntentParams]
        replace_primary_payment_source: NotRequired[bool]
        retain_payment_source: NotRequired[bool]
        payment_initiator: NotRequired[enums.PaymentInitiator]

    class CreateForChargeItemsAndChargesParams(TypedDict):
        customer_id: NotRequired[str]
        subscription_id: NotRequired[str]
        currency_code: NotRequired[str]
        item_prices: NotRequired[List[CreateForChargeItemsAndChargesItemPriceParams]]
        item_tiers: NotRequired[List[CreateForChargeItemsAndChargesItemTierParams]]
        charges: NotRequired[List[CreateForChargeItemsAndChargesChargeParams]]
        invoice_note: NotRequired[str]
        remove_general_note: NotRequired[bool]
        notes_to_remove: NotRequired[
            List[CreateForChargeItemsAndChargesNotesToRemoveParams]
        ]
        po_number: NotRequired[str]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        authorization_transaction_id: NotRequired[str]
        payment_source_id: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        tax_providers_fields: NotRequired[
            List[CreateForChargeItemsAndChargesTaxProvidersFieldParams]
        ]
        discounts: Required[List[CreateForChargeItemsAndChargesDiscountParams]]
        invoice_date: NotRequired[int]
        shipping_address: NotRequired[
            CreateForChargeItemsAndChargesShippingAddressParams
        ]
        statement_descriptor: NotRequired[
            CreateForChargeItemsAndChargesStatementDescriptorParams
        ]
        card: NotRequired[CreateForChargeItemsAndChargesCardParams]
        bank_account: NotRequired[CreateForChargeItemsAndChargesBankAccountParams]
        token_id: NotRequired[str]
        payment_method: NotRequired[CreateForChargeItemsAndChargesPaymentMethodParams]
        payment_intent: NotRequired[CreateForChargeItemsAndChargesPaymentIntentParams]
        replace_primary_payment_source: NotRequired[bool]
        retain_payment_source: NotRequired[bool]
        payment_initiator: NotRequired[enums.PaymentInitiator]

    class ChargeParams(TypedDict):
        customer_id: NotRequired[str]
        subscription_id: NotRequired[str]
        currency_code: NotRequired[str]
        amount: NotRequired[int]
        amount_in_decimal: NotRequired[str]
        description: Required[str]
        date_from: NotRequired[int]
        date_to: NotRequired[int]
        coupon_ids: NotRequired[List[str]]
        coupon: NotRequired[str]
        avalara_sale_type: NotRequired[enums.AvalaraSaleType]
        avalara_transaction_type: NotRequired[int]
        avalara_service_type: NotRequired[int]
        po_number: NotRequired[str]
        invoice_date: NotRequired[int]
        tax_providers_fields: NotRequired[List[ChargeTaxProvidersFieldParams]]
        payment_source_id: NotRequired[str]
        payment_initiator: NotRequired[enums.PaymentInitiator]

    class ChargeAddonParams(TypedDict):
        customer_id: NotRequired[str]
        subscription_id: NotRequired[str]
        addon_id: Required[str]
        addon_quantity: NotRequired[int]
        addon_unit_price: NotRequired[int]
        addon_quantity_in_decimal: NotRequired[str]
        addon_unit_price_in_decimal: NotRequired[str]
        date_from: NotRequired[int]
        date_to: NotRequired[int]
        coupon_ids: NotRequired[List[str]]
        coupon: NotRequired[str]
        po_number: NotRequired[str]
        invoice_date: NotRequired[int]
        payment_source_id: NotRequired[str]
        payment_initiator: NotRequired[enums.PaymentInitiator]

    class CreateForChargeItemParams(TypedDict):
        customer_id: NotRequired[str]
        subscription_id: NotRequired[str]
        item_price: Required[CreateForChargeItemItemPriceParams]
        item_tiers: NotRequired[List[CreateForChargeItemItemTierParams]]
        po_number: NotRequired[str]
        coupon: NotRequired[str]
        payment_source_id: NotRequired[str]
        payment_initiator: NotRequired[enums.PaymentInitiator]
        invoice_date: NotRequired[int]

    class StopDunningParams(TypedDict):
        comment: NotRequired[str]

    class ImportInvoiceParams(TypedDict):
        id: Required[str]
        currency_code: NotRequired[str]
        customer_id: NotRequired[str]
        subscription_id: NotRequired[str]
        po_number: NotRequired[str]
        price_type: NotRequired[enums.PriceType]
        tax_override_reason: NotRequired[enums.TaxOverrideReason]
        vat_number: NotRequired[str]
        vat_number_prefix: NotRequired[str]
        date: Required[int]
        total: Required[int]
        round_off: NotRequired[int]
        status: NotRequired[Status]
        voided_at: NotRequired[int]
        void_reason_code: NotRequired[str]
        is_written_off: NotRequired[bool]
        write_off_amount: NotRequired[int]
        write_off_date: NotRequired[int]
        due_date: NotRequired[int]
        net_term_days: NotRequired[int]
        has_advance_charges: NotRequired[bool]
        use_for_proration: NotRequired[bool]
        line_items: Required[List[ImportInvoiceLineItemParams]]
        payment_reference_numbers: Required[
            List[ImportInvoicePaymentReferenceNumberParams]
        ]
        line_item_tiers: Required[List[ImportInvoiceLineItemTierParams]]
        discounts: Required[List[ImportInvoiceDiscountParams]]
        taxes: Required[List[ImportInvoiceTaxParams]]
        credit_note: NotRequired[ImportInvoiceCreditNoteParams]
        payments: Required[List[ImportInvoicePaymentParams]]
        notes: NotRequired[List[ImportInvoiceNoteParams]]
        billing_address: NotRequired[ImportInvoiceBillingAddressParams]
        shipping_address: NotRequired[ImportInvoiceShippingAddressParams]

    class ApplyPaymentsParams(TypedDict):
        transactions: NotRequired[List[ApplyPaymentsTransactionParams]]
        comment: NotRequired[str]

    class DeleteLineItemsParams(TypedDict):
        line_items: NotRequired[List[DeleteLineItemsLineItemParams]]

    class ApplyCreditsParams(TypedDict):
        credit_notes: NotRequired[List[ApplyCreditsCreditNoteParams]]
        comment: NotRequired[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        einvoice: NotRequired[ListEinvoiceParams]
        paid_on_after: NotRequired[int]
        include_deleted: NotRequired[bool]
        id: NotRequired[Filters.StringFilter]
        subscription_id: NotRequired[Filters.StringFilter]
        customer_id: NotRequired[Filters.StringFilter]
        recurring: NotRequired[Filters.BooleanFilter]
        status: NotRequired[Filters.EnumFilter]
        price_type: NotRequired[Filters.EnumFilter]
        date: NotRequired[Filters.TimestampFilter]
        paid_at: NotRequired[Filters.TimestampFilter]
        total: NotRequired[Filters.NumberFilter]
        amount_paid: NotRequired[Filters.NumberFilter]
        amount_adjusted: NotRequired[Filters.NumberFilter]
        credits_applied: NotRequired[Filters.NumberFilter]
        amount_due: NotRequired[Filters.NumberFilter]
        dunning_status: NotRequired[Filters.EnumFilter]
        payment_owner: NotRequired[Filters.StringFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        channel: NotRequired[Filters.EnumFilter]
        voided_at: NotRequired[Filters.TimestampFilter]
        void_reason_code: NotRequired[Filters.StringFilter]
        sort_by: NotRequired[Filters.SortFilter]

    class InvoicesForCustomerParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class InvoicesForSubscriptionParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class PdfParams(TypedDict):
        disposition_type: NotRequired[enums.DispositionType]

    class ListPaymentReferenceNumbersParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        payment_reference_number: NotRequired[
            ListPaymentReferenceNumbersPaymentReferenceNumberParams
        ]
        id: NotRequired[Filters.StringFilter]

    class AddChargeParams(TypedDict):
        amount: Required[int]
        description: Required[str]
        avalara_sale_type: NotRequired[enums.AvalaraSaleType]
        avalara_transaction_type: NotRequired[int]
        avalara_service_type: NotRequired[int]
        avalara_tax_code: NotRequired[str]
        hsn_code: NotRequired[str]
        taxjar_product_code: NotRequired[str]
        line_item: NotRequired[AddChargeLineItemParams]
        comment: NotRequired[str]
        subscription_id: NotRequired[str]

    class AddAddonChargeParams(TypedDict):
        addon_id: Required[str]
        addon_quantity: NotRequired[int]
        addon_unit_price: NotRequired[int]
        addon_quantity_in_decimal: NotRequired[str]
        addon_unit_price_in_decimal: NotRequired[str]
        line_item: NotRequired[AddAddonChargeLineItemParams]
        comment: NotRequired[str]
        subscription_id: NotRequired[str]

    class AddChargeItemParams(TypedDict):
        item_price: Required[AddChargeItemItemPriceParams]
        item_tiers: NotRequired[List[AddChargeItemItemTierParams]]
        comment: NotRequired[str]
        subscription_id: NotRequired[str]

    class CloseParams(TypedDict):
        comment: NotRequired[str]
        invoice_note: NotRequired[str]
        remove_general_note: NotRequired[bool]
        notes_to_remove: NotRequired[List[CloseNotesToRemoveParams]]
        invoice_date: NotRequired[int]

    class CollectPaymentParams(TypedDict):
        amount: NotRequired[int]
        authorization_transaction_id: NotRequired[str]
        payment_source_id: NotRequired[str]
        comment: NotRequired[str]
        payment_initiator: NotRequired[enums.PaymentInitiator]

    class RecordPaymentParams(TypedDict):
        transaction: Required[RecordPaymentTransactionParams]
        comment: NotRequired[str]

    class RecordTaxWithheldParams(TypedDict):
        tax_withheld: Required[RecordTaxWithheldTaxWithheldParams]

    class RemoveTaxWithheldParams(TypedDict):
        tax_withheld: Required[RemoveTaxWithheldTaxWithheldParams]

    class RefundParams(TypedDict):
        refund_amount: NotRequired[int]
        credit_note: NotRequired[RefundCreditNoteParams]
        comment: NotRequired[str]
        customer_notes: NotRequired[str]

    class RecordRefundParams(TypedDict):
        transaction: Required[RecordRefundTransactionParams]
        credit_note: NotRequired[RecordRefundCreditNoteParams]
        comment: NotRequired[str]
        customer_notes: NotRequired[str]

    class RemovePaymentParams(TypedDict):
        transaction: Required[RemovePaymentTransactionParams]

    class RemoveCreditNoteParams(TypedDict):
        credit_note: Required[RemoveCreditNoteCreditNoteParams]

    class VoidInvoiceParams(TypedDict):
        comment: NotRequired[str]
        void_reason_code: NotRequired[str]

    class WriteOffParams(TypedDict):
        comment: NotRequired[str]

    class DeleteParams(TypedDict):
        comment: NotRequired[str]

    class UpdateDetailsParams(TypedDict):
        billing_address: NotRequired[UpdateDetailsBillingAddressParams]
        shipping_address: NotRequired[UpdateDetailsShippingAddressParams]
        statement_descriptor: NotRequired[UpdateDetailsStatementDescriptorParams]
        vat_number: NotRequired[str]
        vat_number_prefix: NotRequired[str]
        po_number: NotRequired[str]
        comment: NotRequired[str]

    class InstallmentsParams(TypedDict):
        config_id: Required[str]
        amount: NotRequired[int]

    @staticmethod
    def create(params: CreateParams = None, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("invoices"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def create_for_charge_items_and_charges(
        params: CreateForChargeItemsAndChargesParams, env=None, headers=None
    ) -> CreateForChargeItemsAndChargesResponse:
        return request.send(
            "post",
            request.uri_path("invoices", "create_for_charge_items_and_charges"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateForChargeItemsAndChargesResponse,
        )

    @staticmethod
    def charge(params: ChargeParams, env=None, headers=None) -> ChargeResponse:
        return request.send(
            "post",
            request.uri_path("invoices", "charge"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ChargeResponse,
        )

    @staticmethod
    def charge_addon(
        params: ChargeAddonParams, env=None, headers=None
    ) -> ChargeAddonResponse:
        return request.send(
            "post",
            request.uri_path("invoices", "charge_addon"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ChargeAddonResponse,
        )

    @staticmethod
    def create_for_charge_item(
        params: CreateForChargeItemParams, env=None, headers=None
    ) -> CreateForChargeItemResponse:
        return request.send(
            "post",
            request.uri_path("invoices", "create_for_charge_item"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateForChargeItemResponse,
        )

    @staticmethod
    def stop_dunning(
        id, params: StopDunningParams = None, env=None, headers=None
    ) -> StopDunningResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "stop_dunning"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            StopDunningResponse,
        )

    @staticmethod
    def import_invoice(
        params: ImportInvoiceParams, env=None, headers=None
    ) -> ImportInvoiceResponse:
        return request.send(
            "post",
            request.uri_path("invoices", "import_invoice"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ImportInvoiceResponse,
        )

    @staticmethod
    def apply_payments(
        id, params: ApplyPaymentsParams = None, env=None, headers=None
    ) -> ApplyPaymentsResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "apply_payments"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ApplyPaymentsResponse,
        )

    @staticmethod
    def sync_usages(id, env=None, headers=None) -> SyncUsagesResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "sync_usages"),
            None,
            env,
            headers,
            SyncUsagesResponse,
        )

    @staticmethod
    def delete_line_items(
        id, params: DeleteLineItemsParams = None, env=None, headers=None
    ) -> DeleteLineItemsResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "delete_line_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            DeleteLineItemsResponse,
        )

    @staticmethod
    def apply_credits(
        id, params: ApplyCreditsParams = None, env=None, headers=None
    ) -> ApplyCreditsResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "apply_credits"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ApplyCreditsResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("invoices"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def invoices_for_customer(
        id, params: InvoicesForCustomerParams = None, env=None, headers=None
    ) -> InvoicesForCustomerResponse:
        return request.send(
            "get",
            request.uri_path("customers", id, "invoices"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            InvoicesForCustomerResponse,
        )

    @staticmethod
    def invoices_for_subscription(
        id, params: InvoicesForSubscriptionParams = None, env=None, headers=None
    ) -> InvoicesForSubscriptionResponse:
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "invoices"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            InvoicesForSubscriptionResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("invoices", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def pdf(id, params: PdfParams = None, env=None, headers=None) -> PdfResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "pdf"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            PdfResponse,
        )

    @staticmethod
    def download_einvoice(id, env=None, headers=None) -> DownloadEinvoiceResponse:
        return request.send(
            "get",
            request.uri_path("invoices", id, "download_einvoice"),
            None,
            env,
            headers,
            DownloadEinvoiceResponse,
        )

    @staticmethod
    def list_payment_reference_numbers(
        params: ListPaymentReferenceNumbersParams = None, env=None, headers=None
    ) -> ListPaymentReferenceNumbersResponse:
        return request.send(
            "get",
            request.uri_path("invoices", "payment_reference_numbers"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListPaymentReferenceNumbersResponse,
        )

    @staticmethod
    def add_charge(
        id, params: AddChargeParams, env=None, headers=None
    ) -> AddChargeResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "add_charge"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AddChargeResponse,
        )

    @staticmethod
    def add_addon_charge(
        id, params: AddAddonChargeParams, env=None, headers=None
    ) -> AddAddonChargeResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "add_addon_charge"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AddAddonChargeResponse,
        )

    @staticmethod
    def add_charge_item(
        id, params: AddChargeItemParams, env=None, headers=None
    ) -> AddChargeItemResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "add_charge_item"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AddChargeItemResponse,
        )

    @staticmethod
    def close(id, params: CloseParams = None, env=None, headers=None) -> CloseResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "close"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CloseResponse,
        )

    @staticmethod
    def collect_payment(
        id, params: CollectPaymentParams = None, env=None, headers=None
    ) -> CollectPaymentResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "collect_payment"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CollectPaymentResponse,
        )

    @staticmethod
    def record_payment(
        id, params: RecordPaymentParams, env=None, headers=None
    ) -> RecordPaymentResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "record_payment"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RecordPaymentResponse,
        )

    @staticmethod
    def record_tax_withheld(
        id, params: RecordTaxWithheldParams, env=None, headers=None
    ) -> RecordTaxWithheldResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "record_tax_withheld"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RecordTaxWithheldResponse,
        )

    @staticmethod
    def remove_tax_withheld(
        id, params: RemoveTaxWithheldParams, env=None, headers=None
    ) -> RemoveTaxWithheldResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "remove_tax_withheld"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RemoveTaxWithheldResponse,
        )

    @staticmethod
    def refund(
        id, params: RefundParams = None, env=None, headers=None
    ) -> RefundResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "refund"),
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
            request.uri_path("invoices", id, "record_refund"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RecordRefundResponse,
        )

    @staticmethod
    def remove_payment(
        id, params: RemovePaymentParams, env=None, headers=None
    ) -> RemovePaymentResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "remove_payment"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RemovePaymentResponse,
        )

    @staticmethod
    def remove_credit_note(
        id, params: RemoveCreditNoteParams, env=None, headers=None
    ) -> RemoveCreditNoteResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "remove_credit_note"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RemoveCreditNoteResponse,
        )

    @staticmethod
    def void_invoice(
        id, params: VoidInvoiceParams = None, env=None, headers=None
    ) -> VoidInvoiceResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "void"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            VoidInvoiceResponse,
        )

    @staticmethod
    def write_off(
        id, params: WriteOffParams = None, env=None, headers=None
    ) -> WriteOffResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "write_off"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            WriteOffResponse,
        )

    @staticmethod
    def delete(
        id, params: DeleteParams = None, env=None, headers=None
    ) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "delete"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def update_details(
        id, params: UpdateDetailsParams = None, env=None, headers=None
    ) -> UpdateDetailsResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "update_details"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateDetailsResponse,
        )

    @staticmethod
    def installments(
        id, params: InstallmentsParams, env=None, headers=None
    ) -> InstallmentsResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "installments"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            InstallmentsResponse,
        )

    @staticmethod
    def resend_einvoice(id, env=None, headers=None) -> ResendEinvoiceResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "resend_einvoice"),
            None,
            env,
            headers,
            ResendEinvoiceResponse,
        )

    @staticmethod
    def send_einvoice(id, env=None, headers=None) -> SendEinvoiceResponse:
        return request.send(
            "post",
            request.uri_path("invoices", id, "send_einvoice"),
            None,
            env,
            headers,
            SendEinvoiceResponse,
        )
