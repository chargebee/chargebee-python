from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


@dataclass
class Addon:

    env: environment.Environment

    class Type(Enum):
        ON_OFF = "on_off"
        QUANTITY = "quantity"
        TIERED = "tiered"
        VOLUME = "volume"
        STAIRSTEP = "stairstep"

        def __str__(self):
            return self.value

    class ChargeType(Enum):
        RECURRING = "recurring"
        NON_RECURRING = "non_recurring"

        def __str__(self):
            return self.value

    class PeriodUnit(Enum):
        DAY = "day"
        WEEK = "week"
        MONTH = "month"
        YEAR = "year"
        NOT_APPLICABLE = "not_applicable"

        def __str__(self):
            return self.value

    class Status(Enum):
        ACTIVE = "active"
        ARCHIVED = "archived"
        DELETED = "deleted"

        def __str__(self):
            return self.value

    class ShippingFrequencyPeriodUnit(Enum):
        YEAR = "year"
        MONTH = "month"
        WEEK = "week"
        DAY = "day"

        def __str__(self):
            return self.value

    class ProrationType(Enum):
        SITE_DEFAULT = "site_default"
        PARTIAL_TERM = "partial_term"
        FULL_TERM = "full_term"

        def __str__(self):
            return self.value

    class Tier(TypedDict):
        starting_unit: Required[int]
        ending_unit: NotRequired[int]
        price: Required[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

    class TaxProvidersField(TypedDict):
        provider_name: Required[str]
        field_id: Required[str]
        field_value: Required[str]

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

    class CreateParams(TypedDict):
        id: Required[str]
        name: Required[str]
        invoice_name: NotRequired[str]
        description: NotRequired[str]
        charge_type: Required["Addon.ChargeType"]
        price: NotRequired[int]
        tiers: NotRequired[List["Addon.CreateTierParams"]]
        currency_code: NotRequired[str]
        period: NotRequired[int]
        period_unit: NotRequired["Addon.PeriodUnit"]
        pricing_model: NotRequired[enums.PricingModel]
        type: NotRequired["Addon.Type"]
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
        shipping_frequency_period_unit: NotRequired["Addon.ShippingFrequencyPeriodUnit"]
        included_in_mrr: NotRequired[bool]
        show_description_in_invoices: NotRequired[bool]
        show_description_in_quotes: NotRequired[bool]
        price_in_decimal: NotRequired[str]
        tax_providers_fields: Required[List["Addon.CreateTaxProvidersFieldParams"]]
        proration_type: NotRequired["Addon.ProrationType"]
        status: NotRequired["Addon.Status"]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        invoice_name: NotRequired[str]
        description: NotRequired[str]
        charge_type: NotRequired["Addon.ChargeType"]
        price: NotRequired[int]
        tiers: NotRequired[List["Addon.UpdateTierParams"]]
        currency_code: NotRequired[str]
        period: NotRequired[int]
        period_unit: NotRequired["Addon.PeriodUnit"]
        pricing_model: NotRequired[enums.PricingModel]
        type: NotRequired["Addon.Type"]
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
        shipping_frequency_period_unit: NotRequired["Addon.ShippingFrequencyPeriodUnit"]
        included_in_mrr: NotRequired[bool]
        show_description_in_invoices: NotRequired[bool]
        show_description_in_quotes: NotRequired[bool]
        price_in_decimal: NotRequired[str]
        tax_providers_fields: Required[List["Addon.UpdateTaxProvidersFieldParams"]]
        proration_type: NotRequired["Addon.ProrationType"]

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

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {
            "meta_data": 0,
        }
        return request.send(
            "post",
            request.uri_path("addons"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
        )

    def update(self, id, params: UpdateParams, headers=None) -> UpdateResponse:
        jsonKeys = {
            "meta_data": 0,
        }
        return request.send(
            "post",
            request.uri_path("addons", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        return request.send_list_request(
            "get",
            request.uri_path("addons"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("addons", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("addons", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
        )

    def copy(self, params: CopyParams, headers=None) -> CopyResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("addons", "copy"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CopyResponse,
            None,
            False,
            jsonKeys,
        )

    def unarchive(self, id, headers=None) -> UnarchiveResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("addons", id, "unarchive"),
            self.env,
            None,
            headers,
            UnarchiveResponse,
            None,
            False,
            jsonKeys,
        )
