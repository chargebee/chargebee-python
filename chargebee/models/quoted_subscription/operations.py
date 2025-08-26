from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import enums


@dataclass
class QuotedSubscription:
    env: environment.Environment

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
        current_term_start: NotRequired[int]
        current_term_end: NotRequired[int]
        next_billing_at: NotRequired[int]
        amount_in_decimal: NotRequired[str]
        billing_period: NotRequired[int]
        billing_period_unit: NotRequired[enums.BillingPeriodUnit]
        free_quantity: NotRequired[int]
        free_quantity_in_decimal: NotRequired[str]
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        service_period_days: NotRequired[int]
        charge_on_event: NotRequired[enums.ChargeOnEvent]
        charge_once: NotRequired[bool]
        charge_on_option: NotRequired[enums.ChargeOnOption]
        proration_type: NotRequired[enums.ProrationType]
        usage_accumulation_reset_frequency: NotRequired[
            enums.UsageAccumulationResetFrequency
        ]

    class ItemTier(TypedDict):
        item_price_id: Required[str]
        starting_unit: Required[int]
        ending_unit: NotRequired[int]
        price: Required[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]
        index: Required[int]

    class QuotedContractTerm(TypedDict):
        contract_start: Required[int]
        contract_end: Required[int]
        billing_cycle: Required[int]
        action_at_term_end: Required[
            "QuotedSubscription.QuotedContractTermActionAtTermEnd"
        ]
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

    pass
