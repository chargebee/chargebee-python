from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


class Plan:
    class PeriodUnit(Enum):
        DAY = "day"
        WEEK = "week"
        MONTH = "month"
        YEAR = "year"

        def __str__(self):
            return self.value

    class TrialPeriodUnit(Enum):
        DAY = "day"
        MONTH = "month"

        def __str__(self):
            return self.value

    class TrialEndAction(Enum):
        SITE_DEFAULT = "site_default"
        ACTIVATE_SUBSCRIPTION = "activate_subscription"
        CANCEL_SUBSCRIPTION = "cancel_subscription"

        def __str__(self):
            return self.value

    class ChargeModel(Enum):
        FLAT_FEE = "flat_fee"
        PER_UNIT = "per_unit"
        TIERED = "tiered"
        VOLUME = "volume"
        STAIRSTEP = "stairstep"

        def __str__(self):
            return self.value

    class Status(Enum):
        ACTIVE = "active"
        ARCHIVED = "archived"
        DELETED = "deleted"

        def __str__(self):
            return self.value

    class AddonApplicability(Enum):
        ALL = "all"
        RESTRICTED = "restricted"

        def __str__(self):
            return self.value

    class ShippingFrequencyPeriodUnit(Enum):
        YEAR = "year"
        MONTH = "month"
        WEEK = "week"
        DAY = "day"

        def __str__(self):
            return self.value

    class AttachedAddonType(Enum):
        RECOMMENDED = "recommended"
        MANDATORY = "mandatory"

        def __str__(self):
            return self.value

    class Tier(TypedDict):
        starting_unit: Required[int]
        ending_unit: NotRequired[int]
        price: Required[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]

    class TaxProvidersField(TypedDict):
        provider_name: Required[str]
        field_id: Required[str]
        field_value: Required[str]

    class ApplicableAddon(TypedDict):
        id: Required[str]

    class AttachedAddon(TypedDict):
        id: Required[str]
        quantity: Required[int]
        billing_cycles: NotRequired[int]
        type: Required["Plan.AttachedAddonType"]
        quantity_in_decimal: NotRequired[str]

    class EventBasedAddon(TypedDict):
        id: Required[str]
        quantity: Required[int]
        on_event: Required[enums.OnEvent]
        charge_once: Required[bool]
        quantity_in_decimal: NotRequired[str]

    class CreateTierParams(TypedDict):
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]

    class CreateTaxProvidersFieldParams(TypedDict):
        provider_name: Required[str]
        field_id: Required[str]
        field_value: Required[str]

    class CreateApplicableAddonParams(TypedDict):
        id: NotRequired[str]

    class CreateEventBasedAddonParams(TypedDict):
        id: NotRequired[str]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        on_event: NotRequired[enums.OnEvent]
        charge_once: NotRequired[bool]

    class CreateAttachedAddonParams(TypedDict):
        id: NotRequired[str]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        billing_cycles: NotRequired[int]
        type: NotRequired["Plan.AttachedAddonType"]

    class UpdateTierParams(TypedDict):
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]

    class UpdateTaxProvidersFieldParams(TypedDict):
        provider_name: Required[str]
        field_id: Required[str]
        field_value: Required[str]

    class UpdateApplicableAddonParams(TypedDict):
        id: NotRequired[str]

    class UpdateEventBasedAddonParams(TypedDict):
        id: NotRequired[str]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        on_event: NotRequired[enums.OnEvent]
        charge_once: NotRequired[bool]

    class UpdateAttachedAddonParams(TypedDict):
        id: NotRequired[str]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        billing_cycles: NotRequired[int]
        type: NotRequired["Plan.AttachedAddonType"]

    class CreateParams(TypedDict):
        id: Required[str]
        name: Required[str]
        invoice_name: NotRequired[str]
        description: NotRequired[str]
        trial_period: NotRequired[int]
        trial_period_unit: NotRequired["Plan.TrialPeriodUnit"]
        trial_end_action: NotRequired["Plan.TrialEndAction"]
        period: NotRequired[int]
        period_unit: NotRequired["Plan.PeriodUnit"]
        setup_cost: NotRequired[int]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]
        tiers: NotRequired[List["Plan.CreateTierParams"]]
        currency_code: NotRequired[str]
        billing_cycles: NotRequired[int]
        pricing_model: NotRequired[enums.PricingModel]
        charge_model: NotRequired["Plan.ChargeModel"]
        free_quantity: NotRequired[int]
        free_quantity_in_decimal: NotRequired[str]
        addon_applicability: NotRequired["Plan.AddonApplicability"]
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
        shipping_frequency_period_unit: NotRequired["Plan.ShippingFrequencyPeriodUnit"]
        tax_providers_fields: Required[List["Plan.CreateTaxProvidersFieldParams"]]
        applicable_addons: NotRequired[List["Plan.CreateApplicableAddonParams"]]
        event_based_addons: NotRequired[List["Plan.CreateEventBasedAddonParams"]]
        attached_addons: NotRequired[List["Plan.CreateAttachedAddonParams"]]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        show_description_in_invoices: NotRequired[bool]
        show_description_in_quotes: NotRequired[bool]
        giftable: NotRequired[bool]
        status: NotRequired["Plan.Status"]
        claim_url: NotRequired[str]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        invoice_name: NotRequired[str]
        description: NotRequired[str]
        trial_period: NotRequired[int]
        trial_period_unit: NotRequired["Plan.TrialPeriodUnit"]
        trial_end_action: NotRequired["Plan.TrialEndAction"]
        period: NotRequired[int]
        period_unit: NotRequired["Plan.PeriodUnit"]
        setup_cost: NotRequired[int]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]
        tiers: NotRequired[List["Plan.UpdateTierParams"]]
        currency_code: NotRequired[str]
        billing_cycles: NotRequired[int]
        pricing_model: NotRequired[enums.PricingModel]
        charge_model: NotRequired["Plan.ChargeModel"]
        free_quantity: NotRequired[int]
        free_quantity_in_decimal: NotRequired[str]
        addon_applicability: NotRequired["Plan.AddonApplicability"]
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
        shipping_frequency_period_unit: NotRequired["Plan.ShippingFrequencyPeriodUnit"]
        tax_providers_fields: Required[List["Plan.UpdateTaxProvidersFieldParams"]]
        applicable_addons: NotRequired[List["Plan.UpdateApplicableAddonParams"]]
        event_based_addons: NotRequired[List["Plan.UpdateEventBasedAddonParams"]]
        attached_addons: NotRequired[List["Plan.UpdateAttachedAddonParams"]]
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
