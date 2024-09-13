from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.models import enums


class Export:

    class RevenueRecognitionParams(TypedDict):
        invoice: NotRequired[RevenueRecognitionInvoiceParams]
        subscription: NotRequired[RevenueRecognitionSubscriptionParams]
        customer: NotRequired[RevenueRecognitionCustomerParams]
        relationship: NotRequired[RevenueRecognitionRelationshipParams]
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
        invoice: NotRequired[DeferredRevenueInvoiceParams]
        subscription: NotRequired[DeferredRevenueSubscriptionParams]
        customer: NotRequired[DeferredRevenueCustomerParams]
        relationship: NotRequired[DeferredRevenueRelationshipParams]
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
        plan: NotRequired[PlansPlanParams]
        currency_code: NotRequired[Filters.StringFilter]

    class AddonsParams(TypedDict):
        addon: NotRequired[AddonsAddonParams]
        currency_code: NotRequired[Filters.StringFilter]

    class CouponsParams(TypedDict):
        coupon: NotRequired[CouponsCouponParams]
        currency_code: NotRequired[Filters.StringFilter]

    class CustomersParams(TypedDict):
        customer: NotRequired[CustomersCustomerParams]
        relationship: NotRequired[CustomersRelationshipParams]
        export_type: NotRequired[enums.ExportType]
        business_entity_id: NotRequired[Filters.StringFilter]

    class SubscriptionsParams(TypedDict):
        subscription: NotRequired[SubscriptionsSubscriptionParams]
        export_type: NotRequired[enums.ExportType]
        item_id: NotRequired[Filters.StringFilter]
        item_price_id: NotRequired[Filters.StringFilter]
        cancel_reason_code: NotRequired[Filters.StringFilter]

    class InvoicesParams(TypedDict):
        invoice: NotRequired[InvoicesInvoiceParams]
        payment_owner: NotRequired[Filters.StringFilter]

    class CreditNotesParams(TypedDict):
        credit_note: NotRequired[CreditNotesCreditNoteParams]

    class TransactionsParams(TypedDict):
        transaction: NotRequired[TransactionsTransactionParams]

    class OrdersParams(TypedDict):
        order: NotRequired[OrdersOrderParams]
        total: NotRequired[Filters.NumberFilter]

    class ItemFamiliesParams(TypedDict):
        item_family: NotRequired[ItemFamiliesItemFamilyParams]

    class ItemsParams(TypedDict):
        item: NotRequired[ItemsItemParams]

    class ItemPricesParams(TypedDict):
        item_price: NotRequired[ItemPricesItemPriceParams]
        item_family_id: NotRequired[Filters.StringFilter]
        item_type: NotRequired[Filters.EnumFilter]
        currency_code: NotRequired[Filters.StringFilter]

    class AttachedItemsParams(TypedDict):
        attached_item: NotRequired[AttachedItemsAttachedItemParams]
        item_type: NotRequired[Filters.EnumFilter]

    class DifferentialPricesParams(TypedDict):
        differential_price: NotRequired[DifferentialPricesDifferentialPriceParams]
        item_id: NotRequired[Filters.StringFilter]

    class PriceVariantsParams(TypedDict):
        price_variant: NotRequired[PriceVariantsPriceVariantParams]

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get", request.uri_path("exports", id), None, env, headers, RetrieveResponse
        )

    @staticmethod
    def revenue_recognition(
        params: RevenueRecognitionParams, env=None, headers=None
    ) -> RevenueRecognitionResponse:
        return request.send(
            "post",
            request.uri_path("exports", "revenue_recognition"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RevenueRecognitionResponse,
        )

    @staticmethod
    def deferred_revenue(
        params: DeferredRevenueParams, env=None, headers=None
    ) -> DeferredRevenueResponse:
        return request.send(
            "post",
            request.uri_path("exports", "deferred_revenue"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            DeferredRevenueResponse,
        )

    @staticmethod
    def plans(params: PlansParams = None, env=None, headers=None) -> PlansResponse:
        return request.send(
            "post",
            request.uri_path("exports", "plans"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            PlansResponse,
        )

    @staticmethod
    def addons(params: AddonsParams = None, env=None, headers=None) -> AddonsResponse:
        return request.send(
            "post",
            request.uri_path("exports", "addons"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AddonsResponse,
        )

    @staticmethod
    def coupons(
        params: CouponsParams = None, env=None, headers=None
    ) -> CouponsResponse:
        return request.send(
            "post",
            request.uri_path("exports", "coupons"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CouponsResponse,
        )

    @staticmethod
    def customers(
        params: CustomersParams = None, env=None, headers=None
    ) -> CustomersResponse:
        return request.send(
            "post",
            request.uri_path("exports", "customers"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CustomersResponse,
        )

    @staticmethod
    def subscriptions(
        params: SubscriptionsParams = None, env=None, headers=None
    ) -> SubscriptionsResponse:
        return request.send(
            "post",
            request.uri_path("exports", "subscriptions"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            SubscriptionsResponse,
        )

    @staticmethod
    def invoices(
        params: InvoicesParams = None, env=None, headers=None
    ) -> InvoicesResponse:
        return request.send(
            "post",
            request.uri_path("exports", "invoices"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            InvoicesResponse,
        )

    @staticmethod
    def credit_notes(
        params: CreditNotesParams = None, env=None, headers=None
    ) -> CreditNotesResponse:
        return request.send(
            "post",
            request.uri_path("exports", "credit_notes"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreditNotesResponse,
        )

    @staticmethod
    def transactions(
        params: TransactionsParams = None, env=None, headers=None
    ) -> TransactionsResponse:
        return request.send(
            "post",
            request.uri_path("exports", "transactions"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            TransactionsResponse,
        )

    @staticmethod
    def orders(params: OrdersParams = None, env=None, headers=None) -> OrdersResponse:
        return request.send(
            "post",
            request.uri_path("exports", "orders"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            OrdersResponse,
        )

    @staticmethod
    def item_families(
        params: ItemFamiliesParams = None, env=None, headers=None
    ) -> ItemFamiliesResponse:
        return request.send(
            "post",
            request.uri_path("exports", "item_families"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ItemFamiliesResponse,
        )

    @staticmethod
    def items(params: ItemsParams = None, env=None, headers=None) -> ItemsResponse:
        return request.send(
            "post",
            request.uri_path("exports", "items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ItemsResponse,
        )

    @staticmethod
    def item_prices(
        params: ItemPricesParams = None, env=None, headers=None
    ) -> ItemPricesResponse:
        return request.send(
            "post",
            request.uri_path("exports", "item_prices"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ItemPricesResponse,
        )

    @staticmethod
    def attached_items(
        params: AttachedItemsParams = None, env=None, headers=None
    ) -> AttachedItemsResponse:
        return request.send(
            "post",
            request.uri_path("exports", "attached_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AttachedItemsResponse,
        )

    @staticmethod
    def differential_prices(
        params: DifferentialPricesParams = None, env=None, headers=None
    ) -> DifferentialPricesResponse:
        return request.send(
            "post",
            request.uri_path("exports", "differential_prices"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            DifferentialPricesResponse,
        )

    @staticmethod
    def price_variants(
        params: PriceVariantsParams = None, env=None, headers=None
    ) -> PriceVariantsResponse:
        return request.send(
            "post",
            request.uri_path("exports", "price_variants"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            PriceVariantsResponse,
        )
