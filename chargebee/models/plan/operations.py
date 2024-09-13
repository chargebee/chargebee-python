from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class Plan:

    class CreateParams(TypedDict):
        id: Required[str]
        name: Required[str]
        invoice_name: NotRequired[str]
        description: NotRequired[str]
        trial_period: NotRequired[int]
        trial_period_unit: NotRequired[TrialPeriodUnit]
        trial_end_action: NotRequired[TrialEndAction]
        period: NotRequired[int]
        period_unit: NotRequired[PeriodUnit]
        setup_cost: NotRequired[int]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]
        tiers: NotRequired[List[CreateTierParams]]
        currency_code: NotRequired[str]
        billing_cycles: NotRequired[int]
        pricing_model: NotRequired[enums.PricingModel]
        charge_model: NotRequired[ChargeModel]
        free_quantity: NotRequired[int]
        free_quantity_in_decimal: NotRequired[str]
        addon_applicability: NotRequired[AddonApplicability]
        downgrade_penalty: NotRequired[float]
        redirect_url: NotRequired[str]
        enabled_in_hosted_pages: NotRequired[bool]
        enabled_in_portal: NotRequired[bool]
        taxable: NotRequired[bool]
        tax_profile_id: NotRequired[str]
        tax_code: NotRequired[str]
        hsn_code: NotRequired[str]
        taxjar_product_code: NotRequired[str]
        avalara_sale_type: NotRequired[enums.AvalaraSaleType]
        avalara_transaction_type: NotRequired[int]
        avalara_service_type: NotRequired[int]
        sku: NotRequired[str]
        accounting_code: NotRequired[str]
        accounting_category1: NotRequired[str]
        accounting_category2: NotRequired[str]
        accounting_category3: NotRequired[str]
        accounting_category4: NotRequired[str]
        is_shippable: NotRequired[bool]
        shipping_frequency_period: NotRequired[int]
        shipping_frequency_period_unit: NotRequired[ShippingFrequencyPeriodUnit]
        tax_providers_fields: Required[List[CreateTaxProvidersFieldParams]]
        applicable_addons: NotRequired[List[CreateApplicableAddonParams]]
        event_based_addons: NotRequired[List[CreateEventBasedAddonParams]]
        attached_addons: NotRequired[List[CreateAttachedAddonParams]]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        show_description_in_invoices: NotRequired[bool]
        show_description_in_quotes: NotRequired[bool]
        giftable: NotRequired[bool]
        status: NotRequired[Status]
        claim_url: NotRequired[str]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        invoice_name: NotRequired[str]
        description: NotRequired[str]
        trial_period: NotRequired[int]
        trial_period_unit: NotRequired[TrialPeriodUnit]
        trial_end_action: NotRequired[TrialEndAction]
        period: NotRequired[int]
        period_unit: NotRequired[PeriodUnit]
        setup_cost: NotRequired[int]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]
        tiers: NotRequired[List[UpdateTierParams]]
        currency_code: NotRequired[str]
        billing_cycles: NotRequired[int]
        pricing_model: NotRequired[enums.PricingModel]
        charge_model: NotRequired[ChargeModel]
        free_quantity: NotRequired[int]
        free_quantity_in_decimal: NotRequired[str]
        addon_applicability: NotRequired[AddonApplicability]
        downgrade_penalty: NotRequired[float]
        redirect_url: NotRequired[str]
        enabled_in_hosted_pages: NotRequired[bool]
        enabled_in_portal: NotRequired[bool]
        taxable: NotRequired[bool]
        tax_profile_id: NotRequired[str]
        tax_code: NotRequired[str]
        hsn_code: NotRequired[str]
        taxjar_product_code: NotRequired[str]
        avalara_sale_type: NotRequired[enums.AvalaraSaleType]
        avalara_transaction_type: NotRequired[int]
        avalara_service_type: NotRequired[int]
        sku: NotRequired[str]
        accounting_code: NotRequired[str]
        accounting_category1: NotRequired[str]
        accounting_category2: NotRequired[str]
        accounting_category3: NotRequired[str]
        accounting_category4: NotRequired[str]
        is_shippable: NotRequired[bool]
        shipping_frequency_period: NotRequired[int]
        shipping_frequency_period_unit: NotRequired[ShippingFrequencyPeriodUnit]
        tax_providers_fields: Required[List[UpdateTaxProvidersFieldParams]]
        applicable_addons: NotRequired[List[UpdateApplicableAddonParams]]
        event_based_addons: NotRequired[List[UpdateEventBasedAddonParams]]
        attached_addons: NotRequired[List[UpdateAttachedAddonParams]]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        show_description_in_invoices: NotRequired[bool]
        show_description_in_quotes: NotRequired[bool]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        name: NotRequired[Filters.StringFilter]
        price: NotRequired[Filters.NumberFilter]
        period: NotRequired[Filters.NumberFilter]
        period_unit: NotRequired[Filters.EnumFilter]
        trial_period: NotRequired[Filters.NumberFilter]
        trial_period_unit: NotRequired[Filters.EnumFilter]
        addon_applicability: NotRequired[Filters.EnumFilter]
        giftable: NotRequired[Filters.BooleanFilter]
        charge_model: NotRequired[Filters.EnumFilter]
        pricing_model: NotRequired[Filters.EnumFilter]
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
            request.uri_path("plans"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def update(id, params: UpdateParams, env=None, headers=None) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("plans", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("plans"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get", request.uri_path("plans", id), None, env, headers, RetrieveResponse
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("plans", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def copy(params: CopyParams, env=None, headers=None) -> CopyResponse:
        return request.send(
            "post",
            request.uri_path("plans", "copy"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CopyResponse,
        )

    @staticmethod
    def unarchive(id, env=None, headers=None) -> UnarchiveResponse:
        return request.send(
            "post",
            request.uri_path("plans", id, "unarchive"),
            None,
            env,
            headers,
            UnarchiveResponse,
        )
