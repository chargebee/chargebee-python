from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums, payment_intent


class Status(Enum):
    SCHEDULED = "scheduled"
    UNCLAIMED = "unclaimed"
    CLAIMED = "claimed"
    CANCELLED = "cancelled"
    EXPIRED = "expired"

    def __str__(self):
        return self.value


class Gifter(TypedDict):
    customer_id: Required[str]
    invoice_id: NotRequired[str]
    signature: NotRequired[str]
    note: NotRequired[str]


class GiftReceiver(TypedDict):
    customer_id: Required[str]
    subscription_id: Required[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]


class GiftTimeline(TypedDict):
    status: Required[Status]
    occurred_at: NotRequired[int]


class CreateGifterParams(TypedDict):
    customer_id: Required[str]
    signature: Required[str]
    note: NotRequired[str]
    payment_src_id: NotRequired[str]


class CreateGiftReceiverParams(TypedDict):
    customer_id: Required[str]
    first_name: Required[str]
    last_name: Required[str]
    email: Required[str]


class CreatePaymentIntentParams(TypedDict):
    id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    gw_token: NotRequired[str]
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
    reference_id: NotRequired[str]
    gw_payment_method_id: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class CreateShippingAddressParams(TypedDict):
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


class CreateSubscriptionParams(TypedDict):
    plan_id: Required[str]
    plan_quantity: NotRequired[int]
    plan_quantity_in_decimal: NotRequired[str]


class CreateAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]


class CreateForItemsGifterParams(TypedDict):
    customer_id: Required[str]
    signature: Required[str]
    note: NotRequired[str]
    payment_src_id: NotRequired[str]


class CreateForItemsGiftReceiverParams(TypedDict):
    customer_id: Required[str]
    first_name: Required[str]
    last_name: Required[str]
    email: Required[str]


class CreateForItemsPaymentIntentParams(TypedDict):
    id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    gw_token: NotRequired[str]
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
    reference_id: NotRequired[str]
    gw_payment_method_id: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class CreateForItemsShippingAddressParams(TypedDict):
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


class CreateForItemsSubscriptionItemParams(TypedDict):
    item_price_id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]


class ListGiftReceiverParams(TypedDict):
    Email: NotRequired[Filters.StringFilter]
    CustomerId: NotRequired[Filters.StringFilter]


class ListGifterParams(TypedDict):
    CustomerId: NotRequired[Filters.StringFilter]
