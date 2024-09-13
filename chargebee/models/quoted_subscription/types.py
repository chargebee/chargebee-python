from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class ChangeOption(Enum):
    END_OF_TERM = "end_of_term"
    SPECIFIC_DATE = "specific_date"
    IMMEDIATELY = "immediately"

    def __str__(self):
        return self.value


class BillingPeriodUnit(Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"

    def __str__(self):
        return self.value


class QuotedContractTermActionAtTermEnd(Enum):
    RENEW = "renew"
    EVERGREEN = "evergreen"
    CANCEL = "cancel"
    RENEW_ONCE = "renew_once"

    def __str__(self):
        return self.value


class Coupon(TypedDict):
    coupon_id: Required[str]


class SubscriptionItem(TypedDict):
    item_price_id: Required[str]
    item_type: Required[enums.ItemType]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    metered_quantity: NotRequired[str]
    last_calculated_at: NotRequired[int]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    amount: NotRequired[int]
    amount_in_decimal: NotRequired[str]
    billing_period: NotRequired[int]
    billing_period_unit: NotRequired[BillingPeriodUnit]
    free_quantity: NotRequired[int]
    free_quantity_in_decimal: NotRequired[str]
    trial_end: NotRequired[int]
    billing_cycles: NotRequired[int]
    service_period_days: NotRequired[int]
    charge_on_event: NotRequired[enums.ChargeOnEvent]
    charge_once: NotRequired[bool]
    charge_on_option: NotRequired[enums.ChargeOnOption]
    proration_type: NotRequired[enums.ProrationType]


class ItemTier(TypedDict):
    item_price_id: Required[str]
    starting_unit: Required[int]
    ending_unit: NotRequired[int]
    price: Required[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]
    index: Required[int]


class QuotedContractTerm(TypedDict):
    contract_start: Required[int]
    contract_end: Required[int]
    billing_cycle: Required[int]
    action_at_term_end: Required[QuotedContractTermActionAtTermEnd]
    total_contract_value: Required[int]
    cancellation_cutoff_period: NotRequired[int]


class EventBasedAddon(TypedDict):
    id: Required[str]
    quantity: Required[int]
    unit_price: Required[int]
    service_period_in_days: NotRequired[int]
    on_event: Required[enums.OnEvent]
    charge_once: Required[bool]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]


class Addon(TypedDict):
    id: Required[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    amount: NotRequired[int]
    trial_end: NotRequired[int]
    remaining_billing_cycles: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    amount_in_decimal: NotRequired[str]
    proration_type: NotRequired[enums.ProrationType]


class QuotedSubscriptions(TypedDict):
    id: Required[str]
    plan_id: Required[str]
    plan_quantity: Required[int]
    plan_unit_price: NotRequired[int]
    setup_fee: NotRequired[int]
    billing_period: NotRequired[int]
    billing_period_unit: NotRequired[BillingPeriodUnit]
    start_date: NotRequired[int]
    trial_end: NotRequired[int]
    remaining_billing_cycles: NotRequired[int]
    po_number: NotRequired[str]
    auto_collection: NotRequired[enums.AutoCollection]
    plan_quantity_in_decimal: NotRequired[str]
    plan_unit_price_in_decimal: NotRequired[str]
    changes_scheduled_at: NotRequired[int]
    change_option: NotRequired[ChangeOption]
    contract_term_billing_cycle_on_renewal: NotRequired[int]
    addons: NotRequired[List[Addon]]
    event_based_addons: NotRequired[List[EventBasedAddon]]
    coupons: NotRequired[List[Coupon]]
    subscription_items: NotRequired[List[SubscriptionItem]]
    item_tiers: NotRequired[List[ItemTier]]
    quoted_contract_term: NotRequired[QuotedContractTerm]
