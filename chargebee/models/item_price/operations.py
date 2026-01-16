from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


@dataclass
class ItemPrice:
    env: environment.Environment

    class Status(Enum):
        ACTIVE = "active"
        ARCHIVED = "archived"
        DELETED = "deleted"

        def __str__(self):
            return self.value

    class ProrationType(Enum):
        SITE_DEFAULT = "site_default"
        PARTIAL_TERM = "partial_term"
        FULL_TERM = "full_term"

        def __str__(self):
            return self.value

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

    class ShippingPeriodUnit(Enum):
        DAY = "day"
        WEEK = "week"
        MONTH = "month"
        YEAR = "year"

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

    class TaxDetail(TypedDict):
        tax_profile_id: NotRequired[str]
        avalara_sale_type: NotRequired[enums.AvalaraSaleType]
        avalara_transaction_type: NotRequired[int]
        avalara_service_type: NotRequired[int]
        avalara_tax_code: NotRequired[str]
        hsn_code: NotRequired[str]
        taxjar_product_code: NotRequired[str]

    class TaxProvidersField(TypedDict):
        provider_name: Required[str]
        field_id: Required[str]
        field_value: Required[str]

    class AccountingDetail(TypedDict):
        sku: NotRequired[str]
        accounting_code: NotRequired[str]
        accounting_category1: NotRequired[str]
        accounting_category2: NotRequired[str]
        accounting_category3: NotRequired[str]
        accounting_category4: NotRequired[str]

    class CreateTierParams(TypedDict):
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

    class CreateTaxDetailParams(TypedDict):
        tax_profile_id: NotRequired[str]
        avalara_tax_code: NotRequired[str]
        hsn_code: NotRequired[str]
        avalara_sale_type: NotRequired[enums.AvalaraSaleType]
        avalara_transaction_type: NotRequired[int]
        avalara_service_type: NotRequired[int]
        taxjar_product_code: NotRequired[str]

    class CreateTaxProvidersFieldParams(TypedDict):
        provider_name: Required[str]
        field_id: Required[str]
        field_value: Required[str]

    class CreateAccountingDetailParams(TypedDict):
        sku: NotRequired[str]
        accounting_code: NotRequired[str]
        accounting_category1: NotRequired[str]
        accounting_category2: NotRequired[str]
        accounting_category3: NotRequired[str]
        accounting_category4: NotRequired[str]

    class UpdateTierParams(TypedDict):
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

    class UpdateTaxDetailParams(TypedDict):
        tax_profile_id: NotRequired[str]
        avalara_tax_code: NotRequired[str]
        hsn_code: NotRequired[str]
        avalara_sale_type: NotRequired[enums.AvalaraSaleType]
        avalara_transaction_type: NotRequired[int]
        avalara_service_type: NotRequired[int]
        taxjar_product_code: NotRequired[str]

    class UpdateTaxProvidersFieldParams(TypedDict):
        provider_name: Required[str]
        field_id: Required[str]
        field_value: Required[str]

    class UpdateAccountingDetailParams(TypedDict):
        sku: NotRequired[str]
        accounting_code: NotRequired[str]
        accounting_category1: NotRequired[str]
        accounting_category2: NotRequired[str]
        accounting_category3: NotRequired[str]
        accounting_category4: NotRequired[str]

    class CreateParams(TypedDict):
        id: Required[str]
        name: Required[str]
        description: NotRequired[str]
        item_id: Required[str]
        invoice_notes: NotRequired[str]
        proration_type: NotRequired["ItemPrice.ProrationType"]
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
        business_entity_id: NotRequired[str]
        pricing_model: NotRequired[enums.PricingModel]
        tiers: NotRequired[List["ItemPrice.CreateTierParams"]]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]
        period_unit: NotRequired["ItemPrice.PeriodUnit"]
        period: NotRequired[int]
        trial_period_unit: NotRequired["ItemPrice.TrialPeriodUnit"]
        trial_period: NotRequired[int]
        shipping_period: NotRequired[int]
        shipping_period_unit: NotRequired["ItemPrice.ShippingPeriodUnit"]
        billing_cycles: NotRequired[int]
        trial_end_action: NotRequired["ItemPrice.TrialEndAction"]
        tax_detail: NotRequired["ItemPrice.CreateTaxDetailParams"]
        tax_providers_fields: Required[List["ItemPrice.CreateTaxProvidersFieldParams"]]
        accounting_detail: NotRequired["ItemPrice.CreateAccountingDetailParams"]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        description: NotRequired[str]
        proration_type: NotRequired["ItemPrice.ProrationType"]
        price_variant_id: NotRequired[str]
        status: NotRequired["ItemPrice.Status"]
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
        tiers: NotRequired[List["ItemPrice.UpdateTierParams"]]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]
        period_unit: NotRequired["ItemPrice.PeriodUnit"]
        period: NotRequired[int]
        trial_period_unit: NotRequired["ItemPrice.TrialPeriodUnit"]
        trial_period: NotRequired[int]
        shipping_period: NotRequired[int]
        shipping_period_unit: NotRequired["ItemPrice.ShippingPeriodUnit"]
        billing_cycles: NotRequired[int]
        trial_end_action: NotRequired["ItemPrice.TrialEndAction"]
        tax_detail: NotRequired["ItemPrice.UpdateTaxDetailParams"]
        tax_providers_fields: Required[List["ItemPrice.UpdateTaxProvidersFieldParams"]]
        accounting_detail: NotRequired["ItemPrice.UpdateAccountingDetailParams"]
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
        business_entity_id: NotRequired[Filters.StringFilter]
        include_site_level_resources: NotRequired[Filters.BooleanFilter]
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

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {
            "metadata": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("item_prices"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("item_prices", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update(self, id, params: UpdateParams, headers=None) -> UpdateResponse:
        jsonKeys = {
            "metadata": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("item_prices", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
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
            request.uri_path("item_prices"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("item_prices", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def find_applicable_items(
        self, id, params: FindApplicableItemsParams = None, headers=None
    ) -> FindApplicableItemsResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("item_prices", id, "applicable_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            FindApplicableItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def find_applicable_item_prices(
        self, id, params: FindApplicableItemPricesParams = None, headers=None
    ) -> FindApplicableItemPricesResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("item_prices", id, "applicable_item_prices"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            FindApplicableItemPricesResponse,
            None,
            False,
            jsonKeys,
            options,
        )
