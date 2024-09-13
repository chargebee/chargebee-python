from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class Status(Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    TERMINATED = "terminated"

    def __str__(self):
        return self.value


class ActionAtTermEnd(Enum):
    RENEW = "renew"
    EVERGREEN = "evergreen"
    CANCEL = "cancel"
    RENEW_ONCE = "renew_once"

    def __str__(self):
        return self.value


class ContractTerms(TypedDict):
    id: Required[str]
    status: Required[Status]
    contract_start: Required[int]
    contract_end: Required[int]
    billing_cycle: Required[int]
    action_at_term_end: Required[ActionAtTermEnd]
    total_contract_value: Required[int]
    total_contract_value_before_tax: Required[int]
    cancellation_cutoff_period: NotRequired[int]
    created_at: Required[int]
    subscription_id: Required[str]
    remaining_billing_cycles: NotRequired[int]
