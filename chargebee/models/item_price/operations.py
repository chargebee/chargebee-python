from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class ItemPrice:

    class CreateParams(TypedDict):
        id: Required[str]
        name: Required[str]
        description: NotRequired[str]
        item_id: Required[str]
        invoice_notes: NotRequired[str]
        proration_type: NotRequired[ProrationType]
        external_name: NotRequired[str]
        currency_code: NotRequired[str]
        price_variant_id: NotRequired[str]
        is_taxable: NotRequired[bool]
        free_quantity: NotRequired[int]
        free_quantity_in_decimal: NotRequired[str]
        metadata: NotRequired[Dict[Any, Any]]
        show_description_in_invoices: NotRequired[bool]
        show_description_in_quotes: NotRequired[bool]
        usage_accumulation_reset_frequency: NotRequired[
            enums.UsageAccumulationResetFrequency
        ]
        pricing_model: NotRequired[enums.PricingModel]
        tiers: NotRequired[List[CreateTierParams]]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]
        period_unit: NotRequired[PeriodUnit]
        period: NotRequired[int]
        trial_period_unit: NotRequired[TrialPeriodUnit]
        trial_period: NotRequired[int]
        shipping_period: NotRequired[int]
        shipping_period_unit: NotRequired[ShippingPeriodUnit]
        billing_cycles: NotRequired[int]
        trial_end_action: NotRequired[TrialEndAction]
        tax_detail: NotRequired[CreateTaxDetailParams]
        tax_providers_fields: Required[List[CreateTaxProvidersFieldParams]]
        accounting_detail: NotRequired[CreateAccountingDetailParams]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        description: NotRequired[str]
        proration_type: NotRequired[ProrationType]
        price_variant_id: NotRequired[str]
        status: NotRequired[Status]
        external_name: NotRequired[str]
        usage_accumulation_reset_frequency: NotRequired[
            enums.UsageAccumulationResetFrequency
        ]
        currency_code: NotRequired[str]
        invoice_notes: NotRequired[str]
        is_taxable: NotRequired[bool]
        free_quantity: NotRequired[int]
        free_quantity_in_decimal: NotRequired[str]
        metadata: NotRequired[Dict[Any, Any]]
        pricing_model: NotRequired[enums.PricingModel]
        tiers: NotRequired[List[UpdateTierParams]]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]
        period_unit: NotRequired[PeriodUnit]
        period: NotRequired[int]
        trial_period_unit: NotRequired[TrialPeriodUnit]
        trial_period: NotRequired[int]
        shipping_period: NotRequired[int]
        shipping_period_unit: NotRequired[ShippingPeriodUnit]
        billing_cycles: NotRequired[int]
        trial_end_action: NotRequired[TrialEndAction]
        tax_detail: NotRequired[UpdateTaxDetailParams]
        tax_providers_fields: Required[List[UpdateTaxProvidersFieldParams]]
        accounting_detail: NotRequired[UpdateAccountingDetailParams]
        show_description_in_invoices: NotRequired[bool]
        show_description_in_quotes: NotRequired[bool]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        name: NotRequired[Filters.StringFilter]
        pricing_model: NotRequired[Filters.EnumFilter]
        item_id: NotRequired[Filters.StringFilter]
        item_family_id: NotRequired[Filters.StringFilter]
        item_type: NotRequired[Filters.EnumFilter]
        currency_code: NotRequired[Filters.StringFilter]
        price_variant_id: NotRequired[Filters.StringFilter]
        trial_period: NotRequired[Filters.NumberFilter]
        trial_period_unit: NotRequired[Filters.EnumFilter]
        status: NotRequired[Filters.EnumFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        period_unit: NotRequired[Filters.EnumFilter]
        period: NotRequired[Filters.NumberFilter]
        channel: NotRequired[Filters.EnumFilter]
        sort_by: NotRequired[Filters.SortFilter]

    class FindApplicableItemsParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        sort_by: NotRequired[Filters.SortFilter]

    class FindApplicableItemPricesParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        item_id: NotRequired[str]
        sort_by: NotRequired[Filters.SortFilter]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("item_prices"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("item_prices", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def update(id, params: UpdateParams, env=None, headers=None) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("item_prices", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("item_prices"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("item_prices", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def find_applicable_items(
        id, params: FindApplicableItemsParams = None, env=None, headers=None
    ) -> FindApplicableItemsResponse:
        return request.send(
            "get",
            request.uri_path("item_prices", id, "applicable_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            FindApplicableItemsResponse,
        )

    @staticmethod
    def find_applicable_item_prices(
        id, params: FindApplicableItemPricesParams = None, env=None, headers=None
    ) -> FindApplicableItemPricesResponse:
        return request.send(
            "get",
            request.uri_path("item_prices", id, "applicable_item_prices"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            FindApplicableItemPricesResponse,
        )
