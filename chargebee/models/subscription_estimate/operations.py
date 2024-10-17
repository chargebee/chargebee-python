from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import enums


@dataclass
class SubscriptionEstimate:

    env: environment.Environment

    class Status(Enum):
        FUTURE = "future"
        IN_TRIAL = "in_trial"
        ACTIVE = "active"
        NON_RENEWING = "non_renewing"
        PAUSED = "paused"
        CANCELLED = "cancelled"
        TRANSFERRED = "transferred"

        def __str__(self):
            return self.value

    class ContractTermStatus(Enum):
        ACTIVE = "active"
        COMPLETED = "completed"
        CANCELLED = "cancelled"
        TERMINATED = "terminated"

        def __str__(self):
            return self.value

    class ContractTermActionAtTermEnd(Enum):
        RENEW = "renew"
        EVERGREEN = "evergreen"
        CANCEL = "cancel"
        RENEW_ONCE = "renew_once"

        def __str__(self):
            return self.value

    class ShippingAddress(TypedDict):
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        email: NotRequired[str]
        company: NotRequired[str]
        phone: NotRequired[str]
        line1: NotRequired[str]
        line2: NotRequired[str]
        line3: NotRequired[str]
        city: NotRequired[str]
        state_code: NotRequired[str]
        state: NotRequired[str]
        country: NotRequired[str]
        zip: NotRequired[str]
        validation_status: NotRequired[enums.ValidationStatus]
        index: Required[int]

    class ContractTerm(TypedDict):
        id: Required[str]
        status: Required["SubscriptionEstimate.ContractTermStatus"]
        contract_start: Required[int]
        contract_end: Required[int]
        billing_cycle: Required[int]
        action_at_term_end: Required["SubscriptionEstimate.ContractTermActionAtTermEnd"]
        total_contract_value: Required[int]
        total_contract_value_before_tax: Required[int]
        cancellation_cutoff_period: NotRequired[int]
        created_at: Required[int]
        subscription_id: Required[str]
        remaining_billing_cycles: NotRequired[int]

    pass
