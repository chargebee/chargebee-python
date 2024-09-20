from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class Status(Enum):
    CREATED = "created"
    LOGGED_IN = "logged_in"
    LOGGED_OUT = "logged_out"
    NOT_YET_ACTIVATED = "not_yet_activated"
    ACTIVATED = "activated"

    def __str__(self):
        return self.value


class LinkedCustomer(TypedDict):
    customer_id: Required[str]
    email: NotRequired[str]
    has_billing_address: Required[bool]
    has_payment_method: Required[bool]
    has_active_subscription: Required[bool]


class CreateCustomerParams(TypedDict):
    id: Required[str]
