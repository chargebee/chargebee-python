from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


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


class TaxProvidersField(TypedDict):
    provider_name: Required[str]
    field_id: Required[str]
    field_value: Required[str]


class Addons(TypedDict):
    id: Required[str]
    name: Required[str]
    invoice_name: NotRequired[str]
    description: NotRequired[str]
    pricing_model: Required[enums.PricingModel]
    type: Required[Type]
    charge_type: Required[ChargeType]
    price: NotRequired[int]
    currency_code: Required[str]
    period: NotRequired[int]
    period_unit: Required[PeriodUnit]
    unit: NotRequired[str]
    status: Required[Status]
    archived_at: NotRequired[int]
    enabled_in_portal: Required[bool]
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
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    price_in_decimal: NotRequired[str]
    included_in_mrr: NotRequired[bool]
    channel: NotRequired[enums.Channel]
    proration_type: NotRequired[ProrationType]
    invoice_notes: NotRequired[str]
    taxable: NotRequired[bool]
    tax_profile_id: NotRequired[str]
    meta_data: NotRequired[Dict[Any, Any]]
    tiers: NotRequired[List[Tier]]
    tax_providers_fields: NotRequired[List[TaxProvidersField]]
    show_description_in_invoices: NotRequired[bool]
    show_description_in_quotes: NotRequired[bool]


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
