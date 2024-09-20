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
