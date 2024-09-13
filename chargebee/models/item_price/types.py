from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


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


class ItemPrices(TypedDict):
    id: Required[str]
    name: Required[str]
    item_family_id: NotRequired[str]
    item_id: NotRequired[str]
    description: NotRequired[str]
    status: NotRequired[Status]
    external_name: NotRequired[str]
    price_variant_id: NotRequired[str]
    proration_type: NotRequired[ProrationType]
    pricing_model: Required[enums.PricingModel]
    price: NotRequired[int]
    price_in_decimal: NotRequired[str]
    period: NotRequired[int]
    currency_code: Required[str]
    period_unit: NotRequired[PeriodUnit]
    trial_period: NotRequired[int]
    trial_period_unit: NotRequired[TrialPeriodUnit]
    trial_end_action: NotRequired[TrialEndAction]
    shipping_period: NotRequired[int]
    shipping_period_unit: NotRequired[ShippingPeriodUnit]
    billing_cycles: NotRequired[int]
    free_quantity: Required[int]
    free_quantity_in_decimal: NotRequired[str]
    channel: NotRequired[enums.Channel]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    created_at: Required[int]
    usage_accumulation_reset_frequency: NotRequired[
        enums.UsageAccumulationResetFrequency
    ]
    archived_at: NotRequired[int]
    invoice_notes: NotRequired[str]
    tiers: NotRequired[List[Tier]]
    is_taxable: NotRequired[bool]
    tax_detail: NotRequired[TaxDetail]
    tax_providers_fields: NotRequired[List[TaxProvidersField]]
    accounting_detail: NotRequired[AccountingDetail]
    metadata: NotRequired[Dict[Any, Any]]
    item_type: NotRequired[enums.ItemType]
    archivable: NotRequired[bool]
    parent_item_id: NotRequired[str]
    show_description_in_invoices: NotRequired[bool]
    show_description_in_quotes: NotRequired[bool]


class CreateTierParams(TypedDict):
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


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
