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


class PortalSessions(TypedDict):
    id: Required[str]
    token: Required[str]
    access_url: Required[str]
    redirect_url: NotRequired[str]
    status: Required[Status]
    created_at: Required[int]
    expires_at: NotRequired[int]
    customer_id: Required[str]
    login_at: NotRequired[int]
    logout_at: NotRequired[int]
    login_ipaddress: NotRequired[str]
    logout_ipaddress: NotRequired[str]
    linked_customers: NotRequired[List[LinkedCustomer]]


class CreateCustomerParams(TypedDict):
    id: Required[str]
