from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


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
    type: Required[AttachedAddonType]
    quantity_in_decimal: NotRequired[str]


class EventBasedAddon(TypedDict):
    id: Required[str]
    quantity: Required[int]
    on_event: Required[enums.OnEvent]
    charge_once: Required[bool]
    quantity_in_decimal: NotRequired[str]


class Plans(TypedDict):
    id: Required[str]
    name: Required[str]
    invoice_name: NotRequired[str]
    description: NotRequired[str]
    price: NotRequired[int]
    currency_code: Required[str]
    period: Required[int]
    period_unit: Required[PeriodUnit]
    trial_period: NotRequired[int]
    trial_period_unit: NotRequired[TrialPeriodUnit]
    trial_end_action: NotRequired[TrialEndAction]
    pricing_model: Required[enums.PricingModel]
    charge_model: Required[ChargeModel]
    free_quantity: Required[int]
    setup_cost: NotRequired[int]
    downgrade_penalty: NotRequired[float]
    status: Required[Status]
    archived_at: NotRequired[int]
    billing_cycles: NotRequired[int]
    redirect_url: NotRequired[str]
    enabled_in_hosted_pages: Required[bool]
    enabled_in_portal: Required[bool]
    addon_applicability: Required[AddonApplicability]
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
    giftable: Required[bool]
    claim_url: NotRequired[str]
    free_quantity_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]
    channel: NotRequired[enums.Channel]
    invoice_notes: NotRequired[str]
    taxable: NotRequired[bool]
    tax_profile_id: NotRequired[str]
    meta_data: NotRequired[Dict[Any, Any]]
    tiers: NotRequired[List[Tier]]
    tax_providers_fields: NotRequired[List[TaxProvidersField]]
    applicable_addons: NotRequired[List[ApplicableAddon]]
    attached_addons: NotRequired[List[AttachedAddon]]
    event_based_addons: NotRequired[List[EventBasedAddon]]
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
    type: NotRequired[AttachedAddonType]


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
    type: NotRequired[AttachedAddonType]
