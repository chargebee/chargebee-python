from typing import TypedDict, Required, NotRequired, Dict, List, Any
from chargebee.models import enums


class Addresses(TypedDict):
    label: Required[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    addr: NotRequired[str]
    extended_addr: NotRequired[str]
    extended_addr2: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    state: NotRequired[str]
    country: NotRequired[str]
    zip: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]
    subscription_id: Required[str]
