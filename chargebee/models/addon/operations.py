from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class Addon:

    class CreateParams(TypedDict):
        id: Required[str]
        name: Required[str]
        invoice_name: NotRequired[str]
        description: NotRequired[str]
        charge_type: Required[ChargeType]
        price: NotRequired[int]
        tiers: NotRequired[List[CreateTierParams]]
        currency_code: NotRequired[str]
        period: NotRequired[int]
        period_unit: NotRequired[PeriodUnit]
        pricing_model: NotRequired[enums.PricingModel]
        type: NotRequired[Type]
        unit: NotRequired[str]
        enabled_in_portal: NotRequired[bool]
        taxable: NotRequired[bool]
        tax_profile_id: NotRequired[str]
        avalara_sale_type: NotRequired[enums.AvalaraSaleType]
        avalara_transaction_type: NotRequired[int]
        avalara_service_type: NotRequired[int]
        tax_code: NotRequired[str]
        hsn_code: NotRequired[str]
        taxjar_product_code: NotRequired[str]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        sku: NotRequired[str]
        accounting_code: NotRequired[str]
        accounting_category1: NotRequired[str]
        accounting_category2: NotRequired[str]
        accounting_category3: NotRequired[str]
        accounting_category4: NotRequired[str]
        is_shippable: NotRequired[bool]
        shipping_frequency_period: NotRequired[int]
        shipping_frequency_period_unit: NotRequired[ShippingFrequencyPeriodUnit]
        included_in_mrr: NotRequired[bool]
        show_description_in_invoices: NotRequired[bool]
        show_description_in_quotes: NotRequired[bool]
        price_in_decimal: NotRequired[str]
        tax_providers_fields: Required[List[CreateTaxProvidersFieldParams]]
        proration_type: NotRequired[ProrationType]
        status: NotRequired[Status]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        invoice_name: NotRequired[str]
        description: NotRequired[str]
        charge_type: NotRequired[ChargeType]
        price: NotRequired[int]
        tiers: NotRequired[List[UpdateTierParams]]
        currency_code: NotRequired[str]
        period: NotRequired[int]
        period_unit: NotRequired[PeriodUnit]
        pricing_model: NotRequired[enums.PricingModel]
        type: NotRequired[Type]
        unit: NotRequired[str]
        enabled_in_portal: NotRequired[bool]
        taxable: NotRequired[bool]
        tax_profile_id: NotRequired[str]
        avalara_sale_type: NotRequired[enums.AvalaraSaleType]
        avalara_transaction_type: NotRequired[int]
        avalara_service_type: NotRequired[int]
        tax_code: NotRequired[str]
        hsn_code: NotRequired[str]
        taxjar_product_code: NotRequired[str]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        sku: NotRequired[str]
        accounting_code: NotRequired[str]
        accounting_category1: NotRequired[str]
        accounting_category2: NotRequired[str]
        accounting_category3: NotRequired[str]
        accounting_category4: NotRequired[str]
        is_shippable: NotRequired[bool]
        shipping_frequency_period: NotRequired[int]
        shipping_frequency_period_unit: NotRequired[ShippingFrequencyPeriodUnit]
        included_in_mrr: NotRequired[bool]
        show_description_in_invoices: NotRequired[bool]
        show_description_in_quotes: NotRequired[bool]
        price_in_decimal: NotRequired[str]
        tax_providers_fields: Required[List[UpdateTaxProvidersFieldParams]]
        proration_type: NotRequired[ProrationType]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        name: NotRequired[Filters.StringFilter]
        pricing_model: NotRequired[Filters.EnumFilter]
        type: NotRequired[Filters.EnumFilter]
        charge_type: NotRequired[Filters.EnumFilter]
        price: NotRequired[Filters.NumberFilter]
        period: NotRequired[Filters.NumberFilter]
        period_unit: NotRequired[Filters.EnumFilter]
        status: NotRequired[Filters.EnumFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        currency_code: NotRequired[Filters.StringFilter]
        channel: NotRequired[Filters.EnumFilter]
        include_deleted: NotRequired[bool]

    class CopyParams(TypedDict):
        from_site: Required[str]
        id_at_from_site: Required[str]
        id: NotRequired[str]
        for_site_merging: NotRequired[bool]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("addons"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def update(id, params: UpdateParams, env=None, headers=None) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("addons", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("addons"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get", request.uri_path("addons", id), None, env, headers, RetrieveResponse
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("addons", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def copy(params: CopyParams, env=None, headers=None) -> CopyResponse:
        return request.send(
            "post",
            request.uri_path("addons", "copy"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CopyResponse,
        )

    @staticmethod
    def unarchive(id, env=None, headers=None) -> UnarchiveResponse:
        return request.send(
            "post",
            request.uri_path("addons", id, "unarchive"),
            None,
            env,
            headers,
            UnarchiveResponse,
        )
