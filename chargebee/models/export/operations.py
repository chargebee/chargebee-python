from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


@dataclass
class Export:
    env: environment.Environment

    class MimeType(Enum):
        PDF = "pdf"
        ZIP = "zip"

        def __str__(self):
            return self.value

    class Status(Enum):
        IN_PROCESS = "in_process"
        COMPLETED = "completed"
        FAILED = "failed"

        def __str__(self):
            return self.value

    class Download(TypedDict):
        download_url: Required[str]
        valid_till: Required[int]
        mime_type: NotRequired[str]

    class RevenueRecognitionInvoiceParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
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
        updated_at: NotRequired[Filters.TimestampFilter]
        channel: NotRequired[Filters.EnumFilter]

    class RevenueRecognitionSubscriptionParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        customer_id: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]
        cancel_reason: NotRequired[Filters.EnumFilter]
        remaining_billing_cycles: NotRequired[Filters.NumberFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        activated_at: NotRequired[Filters.TimestampFilter]
        next_billing_at: NotRequired[Filters.TimestampFilter]
        cancelled_at: NotRequired[Filters.TimestampFilter]
        has_scheduled_changes: NotRequired[Filters.BooleanFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        offline_payment_method: NotRequired[Filters.EnumFilter]
        auto_close_invoices: NotRequired[Filters.BooleanFilter]
        channel: NotRequired[Filters.EnumFilter]
        plan_id: NotRequired[Filters.StringFilter]

    class RevenueRecognitionCustomerParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        first_name: NotRequired[Filters.StringFilter]
        last_name: NotRequired[Filters.StringFilter]
        email: NotRequired[Filters.StringFilter]
        company: NotRequired[Filters.StringFilter]
        phone: NotRequired[Filters.StringFilter]
        auto_collection: NotRequired[Filters.EnumFilter]
        taxability: NotRequired[Filters.EnumFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        offline_payment_method: NotRequired[Filters.EnumFilter]
        auto_close_invoices: NotRequired[Filters.BooleanFilter]
        channel: NotRequired[Filters.EnumFilter]

    class RevenueRecognitionRelationshipParams(TypedDict):
        parent_id: NotRequired[Filters.StringFilter]
        payment_owner_id: NotRequired[Filters.StringFilter]
        invoice_owner_id: NotRequired[Filters.StringFilter]

    class DeferredRevenueInvoiceParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
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
        updated_at: NotRequired[Filters.TimestampFilter]
        channel: NotRequired[Filters.EnumFilter]

    class DeferredRevenueSubscriptionParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        customer_id: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]
        cancel_reason: NotRequired[Filters.EnumFilter]
        remaining_billing_cycles: NotRequired[Filters.NumberFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        activated_at: NotRequired[Filters.TimestampFilter]
        next_billing_at: NotRequired[Filters.TimestampFilter]
        cancelled_at: NotRequired[Filters.TimestampFilter]
        has_scheduled_changes: NotRequired[Filters.BooleanFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        offline_payment_method: NotRequired[Filters.EnumFilter]
        auto_close_invoices: NotRequired[Filters.BooleanFilter]
        channel: NotRequired[Filters.EnumFilter]
        plan_id: NotRequired[Filters.StringFilter]

    class DeferredRevenueCustomerParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        first_name: NotRequired[Filters.StringFilter]
        last_name: NotRequired[Filters.StringFilter]
        email: NotRequired[Filters.StringFilter]
        company: NotRequired[Filters.StringFilter]
        phone: NotRequired[Filters.StringFilter]
        auto_collection: NotRequired[Filters.EnumFilter]
        taxability: NotRequired[Filters.EnumFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        offline_payment_method: NotRequired[Filters.EnumFilter]
        auto_close_invoices: NotRequired[Filters.BooleanFilter]
        channel: NotRequired[Filters.EnumFilter]

    class DeferredRevenueRelationshipParams(TypedDict):
        parent_id: NotRequired[Filters.StringFilter]
        payment_owner_id: NotRequired[Filters.StringFilter]
        invoice_owner_id: NotRequired[Filters.StringFilter]

    class PlansPlanParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        name: NotRequired[Filters.StringFilter]
        price: NotRequired[Filters.NumberFilter]
        period: NotRequired[Filters.NumberFilter]
        period_unit: NotRequired[Filters.EnumFilter]
        trial_period: NotRequired[Filters.NumberFilter]
        trial_period_unit: NotRequired[Filters.EnumFilter]
        addon_applicability: NotRequired[Filters.EnumFilter]
        giftable: NotRequired[Filters.BooleanFilter]
        status: NotRequired[Filters.EnumFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        channel: NotRequired[Filters.EnumFilter]

    class AddonsAddonParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        name: NotRequired[Filters.StringFilter]
        charge_type: NotRequired[Filters.EnumFilter]
        price: NotRequired[Filters.NumberFilter]
        period: NotRequired[Filters.NumberFilter]
        period_unit: NotRequired[Filters.EnumFilter]
        status: NotRequired[Filters.EnumFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        channel: NotRequired[Filters.EnumFilter]

    class CouponsCouponParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        name: NotRequired[Filters.StringFilter]
        discount_type: NotRequired[Filters.EnumFilter]
        duration_type: NotRequired[Filters.EnumFilter]
        status: NotRequired[Filters.EnumFilter]
        apply_on: NotRequired[Filters.EnumFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        updated_at: NotRequired[Filters.TimestampFilter]

    class CustomersCustomerParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        first_name: NotRequired[Filters.StringFilter]
        last_name: NotRequired[Filters.StringFilter]
        email: NotRequired[Filters.StringFilter]
        company: NotRequired[Filters.StringFilter]
        phone: NotRequired[Filters.StringFilter]
        auto_collection: NotRequired[Filters.EnumFilter]
        taxability: NotRequired[Filters.EnumFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        offline_payment_method: NotRequired[Filters.EnumFilter]
        auto_close_invoices: NotRequired[Filters.BooleanFilter]
        channel: NotRequired[Filters.EnumFilter]

    class CustomersRelationshipParams(TypedDict):
        parent_id: NotRequired[Filters.StringFilter]
        payment_owner_id: NotRequired[Filters.StringFilter]
        invoice_owner_id: NotRequired[Filters.StringFilter]

    class SubscriptionsSubscriptionParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        customer_id: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]
        cancel_reason: NotRequired[Filters.EnumFilter]
        remaining_billing_cycles: NotRequired[Filters.NumberFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        activated_at: NotRequired[Filters.TimestampFilter]
        next_billing_at: NotRequired[Filters.TimestampFilter]
        cancelled_at: NotRequired[Filters.TimestampFilter]
        has_scheduled_changes: NotRequired[Filters.BooleanFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        offline_payment_method: NotRequired[Filters.EnumFilter]
        auto_close_invoices: NotRequired[Filters.BooleanFilter]
        channel: NotRequired[Filters.EnumFilter]
        plan_id: NotRequired[Filters.StringFilter]

    class InvoicesInvoiceParams(TypedDict):
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
        updated_at: NotRequired[Filters.TimestampFilter]
        channel: NotRequired[Filters.EnumFilter]

    class CreditNotesCreditNoteParams(TypedDict):
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
        channel: NotRequired[Filters.EnumFilter]

    class TransactionsTransactionParams(TypedDict):
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

    class OrdersOrderParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        subscription_id: NotRequired[Filters.StringFilter]
        customer_id: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]
        price_type: NotRequired[Filters.EnumFilter]
        order_date: NotRequired[Filters.TimestampFilter]
        shipping_date: NotRequired[Filters.TimestampFilter]
        shipped_at: NotRequired[Filters.TimestampFilter]
        delivered_at: NotRequired[Filters.TimestampFilter]
        cancelled_at: NotRequired[Filters.TimestampFilter]
        amount_paid: NotRequired[Filters.NumberFilter]
        refundable_credits: NotRequired[Filters.NumberFilter]
        refundable_credits_issued: NotRequired[Filters.NumberFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        resent_status: NotRequired[Filters.EnumFilter]
        is_resent: NotRequired[Filters.BooleanFilter]
        original_order_id: NotRequired[Filters.StringFilter]

    class ItemFamiliesItemFamilyParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        name: NotRequired[Filters.StringFilter]
        updated_at: NotRequired[Filters.TimestampFilter]

    class ItemsItemParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        item_family_id: NotRequired[Filters.StringFilter]
        type: NotRequired[Filters.EnumFilter]
        name: NotRequired[Filters.StringFilter]
        item_applicability: NotRequired[Filters.EnumFilter]
        status: NotRequired[Filters.EnumFilter]
        is_giftable: NotRequired[Filters.BooleanFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        enabled_for_checkout: NotRequired[Filters.BooleanFilter]
        enabled_in_portal: NotRequired[Filters.BooleanFilter]
        metered: NotRequired[Filters.BooleanFilter]
        usage_calculation: NotRequired[Filters.EnumFilter]
        channel: NotRequired[Filters.EnumFilter]

    class ItemPricesItemPriceParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        name: NotRequired[Filters.StringFilter]
        pricing_model: NotRequired[Filters.EnumFilter]
        item_id: NotRequired[Filters.StringFilter]
        price_variant_id: NotRequired[Filters.StringFilter]
        trial_period: NotRequired[Filters.NumberFilter]
        trial_period_unit: NotRequired[Filters.EnumFilter]
        status: NotRequired[Filters.EnumFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        period_unit: NotRequired[Filters.EnumFilter]
        period: NotRequired[Filters.NumberFilter]
        channel: NotRequired[Filters.EnumFilter]

    class AttachedItemsAttachedItemParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        item_id: NotRequired[Filters.StringFilter]
        type: NotRequired[Filters.EnumFilter]
        charge_on_event: NotRequired[Filters.EnumFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        parent_item_id: NotRequired[Filters.StringFilter]

    class DifferentialPricesDifferentialPriceParams(TypedDict):
        item_price_id: NotRequired[Filters.StringFilter]
        id: NotRequired[Filters.StringFilter]
        parent_item_id: NotRequired[Filters.StringFilter]

    class PriceVariantsPriceVariantParams(TypedDict):
        id: NotRequired[Filters.StringFilter]
        name: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        created_at: NotRequired[Filters.TimestampFilter]

    def wait_for_export_completion(
        self, export: ExportResponse, headers=None
    ) -> RetrieveResponse:
        import time

        response: RetrieveResponse = None
        count = 0
        retry_delay_ms = (
            10000 if self.env is None else self.env.export_retry_delay_ms
        ) / 1000.0

        while export.status == "in_process":
            if count > 50:
                raise RuntimeError("Export is taking too long")
            count += 1
            time.sleep(retry_delay_ms)
            response = self.retrieve(export.id, headers)
            export = response.export
        return response

    class RevenueRecognitionParams(TypedDict):
        invoice: NotRequired["Export.RevenueRecognitionInvoiceParams"]
        subscription: NotRequired["Export.RevenueRecognitionSubscriptionParams"]
        customer: NotRequired["Export.RevenueRecognitionCustomerParams"]
        relationship: NotRequired["Export.RevenueRecognitionRelationshipParams"]
        report_by: Required[enums.ReportBy]
        currency_code: NotRequired[str]
        report_from_month: Required[int]
        report_from_year: Required[int]
        report_to_month: Required[int]
        report_to_year: Required[int]
        include_discounts: NotRequired[bool]
        payment_owner: NotRequired[Filters.StringFilter]
        item_id: NotRequired[Filters.StringFilter]
        item_price_id: NotRequired[Filters.StringFilter]
        cancel_reason_code: NotRequired[Filters.StringFilter]
        business_entity_id: NotRequired[Filters.StringFilter]

    class DeferredRevenueParams(TypedDict):
        invoice: NotRequired["Export.DeferredRevenueInvoiceParams"]
        subscription: NotRequired["Export.DeferredRevenueSubscriptionParams"]
        customer: NotRequired["Export.DeferredRevenueCustomerParams"]
        relationship: NotRequired["Export.DeferredRevenueRelationshipParams"]
        report_by: Required[enums.ReportBy]
        currency_code: NotRequired[str]
        report_from_month: Required[int]
        report_from_year: Required[int]
        report_to_month: Required[int]
        report_to_year: Required[int]
        include_discounts: NotRequired[bool]
        payment_owner: NotRequired[Filters.StringFilter]
        item_id: NotRequired[Filters.StringFilter]
        item_price_id: NotRequired[Filters.StringFilter]
        cancel_reason_code: NotRequired[Filters.StringFilter]
        business_entity_id: NotRequired[Filters.StringFilter]

    class PlansParams(TypedDict):
        plan: NotRequired["Export.PlansPlanParams"]
        currency_code: NotRequired[Filters.StringFilter]

    class AddonsParams(TypedDict):
        addon: NotRequired["Export.AddonsAddonParams"]
        currency_code: NotRequired[Filters.StringFilter]

    class CouponsParams(TypedDict):
        coupon: NotRequired["Export.CouponsCouponParams"]
        currency_code: NotRequired[Filters.StringFilter]

    class CustomersParams(TypedDict):
        customer: NotRequired["Export.CustomersCustomerParams"]
        relationship: NotRequired["Export.CustomersRelationshipParams"]
        export_type: NotRequired[enums.ExportType]
        business_entity_id: NotRequired[Filters.StringFilter]

    class SubscriptionsParams(TypedDict):
        subscription: NotRequired["Export.SubscriptionsSubscriptionParams"]
        export_type: NotRequired[enums.ExportType]
        item_id: NotRequired[Filters.StringFilter]
        item_price_id: NotRequired[Filters.StringFilter]
        cancel_reason_code: NotRequired[Filters.StringFilter]

    class InvoicesParams(TypedDict):
        invoice: NotRequired["Export.InvoicesInvoiceParams"]
        payment_owner: NotRequired[Filters.StringFilter]

    class CreditNotesParams(TypedDict):
        credit_note: NotRequired["Export.CreditNotesCreditNoteParams"]

    class TransactionsParams(TypedDict):
        transaction: NotRequired["Export.TransactionsTransactionParams"]

    class OrdersParams(TypedDict):
        order: NotRequired["Export.OrdersOrderParams"]
        total: NotRequired[Filters.NumberFilter]

    class ItemFamiliesParams(TypedDict):
        item_family: NotRequired["Export.ItemFamiliesItemFamilyParams"]
        business_entity_id: NotRequired[Filters.StringFilter]
        include_site_level_resources: NotRequired[Filters.BooleanFilter]

    class ItemsParams(TypedDict):
        item: NotRequired["Export.ItemsItemParams"]
        business_entity_id: NotRequired[Filters.StringFilter]
        include_site_level_resources: NotRequired[Filters.BooleanFilter]

    class ItemPricesParams(TypedDict):
        item_price: NotRequired["Export.ItemPricesItemPriceParams"]
        item_family_id: NotRequired[Filters.StringFilter]
        item_type: NotRequired[Filters.EnumFilter]
        currency_code: NotRequired[Filters.StringFilter]
        business_entity_id: NotRequired[Filters.StringFilter]
        include_site_level_resources: NotRequired[Filters.BooleanFilter]

    class AttachedItemsParams(TypedDict):
        attached_item: NotRequired["Export.AttachedItemsAttachedItemParams"]
        item_type: NotRequired[Filters.EnumFilter]

    class DifferentialPricesParams(TypedDict):
        differential_price: NotRequired[
            "Export.DifferentialPricesDifferentialPriceParams"
        ]
        item_id: NotRequired[Filters.StringFilter]

    class PriceVariantsParams(TypedDict):
        price_variant: NotRequired["Export.PriceVariantsPriceVariantParams"]
        business_entity_id: NotRequired[Filters.StringFilter]
        include_site_level_resources: NotRequired[Filters.BooleanFilter]

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("exports", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def revenue_recognition(
        self, params: RevenueRecognitionParams, headers=None
    ) -> RevenueRecognitionResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "revenue_recognition"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RevenueRecognitionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def deferred_revenue(
        self, params: DeferredRevenueParams, headers=None
    ) -> DeferredRevenueResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "deferred_revenue"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeferredRevenueResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def plans(self, params: PlansParams = None, headers=None) -> PlansResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "plans"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PlansResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def addons(self, params: AddonsParams = None, headers=None) -> AddonsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "addons"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AddonsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def coupons(self, params: CouponsParams = None, headers=None) -> CouponsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "coupons"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CouponsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def customers(
        self, params: CustomersParams = None, headers=None
    ) -> CustomersResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "customers"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CustomersResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def subscriptions(
        self, params: SubscriptionsParams = None, headers=None
    ) -> SubscriptionsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "subscriptions"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            SubscriptionsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def invoices(self, params: InvoicesParams = None, headers=None) -> InvoicesResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "invoices"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            InvoicesResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def credit_notes(
        self, params: CreditNotesParams = None, headers=None
    ) -> CreditNotesResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "credit_notes"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreditNotesResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def transactions(
        self, params: TransactionsParams = None, headers=None
    ) -> TransactionsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "transactions"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            TransactionsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def orders(self, params: OrdersParams = None, headers=None) -> OrdersResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "orders"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            OrdersResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def item_families(
        self, params: ItemFamiliesParams = None, headers=None
    ) -> ItemFamiliesResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "item_families"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ItemFamiliesResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def items(self, params: ItemsParams = None, headers=None) -> ItemsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def item_prices(
        self, params: ItemPricesParams = None, headers=None
    ) -> ItemPricesResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "item_prices"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ItemPricesResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def attached_items(
        self, params: AttachedItemsParams = None, headers=None
    ) -> AttachedItemsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "attached_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AttachedItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def differential_prices(
        self, params: DifferentialPricesParams = None, headers=None
    ) -> DifferentialPricesResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "differential_prices"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DifferentialPricesResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def price_variants(
        self, params: PriceVariantsParams = None, headers=None
    ) -> PriceVariantsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("exports", "price_variants"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PriceVariantsResponse,
            None,
            False,
            jsonKeys,
            options,
        )
