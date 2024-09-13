from typing import TypedDict, Required, NotRequired, Dict, List, Any
from chargebee.models import enums


class PricingPageSessions(TypedDict):
    id: NotRequired[str]
    url: NotRequired[str]
    created_at: NotRequired[int]
    expires_at: NotRequired[int]


class CreateForNewSubscriptionPricingPageParams(TypedDict):
    id: Required[str]


class CreateForNewSubscriptionSubscriptionParams(TypedDict):
    id: NotRequired[str]


class CreateForNewSubscriptionCustomerParams(TypedDict):
    id: NotRequired[str]
    email: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    locale: NotRequired[str]


class CreateForNewSubscriptionBillingAddressParams(TypedDict):
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
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class CreateForNewSubscriptionShippingAddressParams(TypedDict):
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
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class CreateForExistingSubscriptionPricingPageParams(TypedDict):
    id: Required[str]


class CreateForExistingSubscriptionSubscriptionParams(TypedDict):
    id: Required[str]
