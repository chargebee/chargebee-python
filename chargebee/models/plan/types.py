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
