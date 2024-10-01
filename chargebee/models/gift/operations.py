from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums, payment_intent


class Gift:
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
        status: Required["Gift.Status"]
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
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
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
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
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
        email: NotRequired[Filters.StringFilter]
        customer_id: NotRequired[Filters.StringFilter]

    class ListGifterParams(TypedDict):
        customer_id: NotRequired[Filters.StringFilter]

    class CreateParams(TypedDict):
        scheduled_at: NotRequired[int]
        auto_claim: NotRequired[bool]
        no_expiry: NotRequired[bool]
        claim_expiry_date: NotRequired[int]
        gifter: Required["Gift.CreateGifterParams"]
        gift_receiver: Required["Gift.CreateGiftReceiverParams"]
        coupon_ids: NotRequired[List[str]]
        payment_intent: NotRequired["Gift.CreatePaymentIntentParams"]
        shipping_address: NotRequired["Gift.CreateShippingAddressParams"]
        subscription: Required["Gift.CreateSubscriptionParams"]
        addons: NotRequired[List["Gift.CreateAddonParams"]]

    class CreateForItemsParams(TypedDict):
        scheduled_at: NotRequired[int]
        auto_claim: NotRequired[bool]
        no_expiry: NotRequired[bool]
        claim_expiry_date: NotRequired[int]
        gifter: Required["Gift.CreateForItemsGifterParams"]
        gift_receiver: Required["Gift.CreateForItemsGiftReceiverParams"]
        coupon_ids: NotRequired[List[str]]
        payment_intent: NotRequired["Gift.CreateForItemsPaymentIntentParams"]
        shipping_address: NotRequired["Gift.CreateForItemsShippingAddressParams"]
        subscription_items: NotRequired[
            List["Gift.CreateForItemsSubscriptionItemParams"]
        ]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        gift_receiver: NotRequired["Gift.ListGiftReceiverParams"]
        gifter: NotRequired["Gift.ListGifterParams"]
        status: NotRequired[Filters.EnumFilter]

    class UpdateGiftParams(TypedDict):
        scheduled_at: Required[int]
        comment: NotRequired[str]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("gifts"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def create_for_items(
        params: CreateForItemsParams, env=None, headers=None
    ) -> CreateForItemsResponse:
        return request.send(
            "post",
            request.uri_path("gifts", "create_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateForItemsResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get", request.uri_path("gifts", id), None, env, headers, RetrieveResponse
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("gifts"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def claim(id, env=None, headers=None) -> ClaimResponse:
        return request.send(
            "post",
            request.uri_path("gifts", id, "claim"),
            None,
            env,
            headers,
            ClaimResponse,
        )

    @staticmethod
    def cancel(id, env=None, headers=None) -> CancelResponse:
        return request.send(
            "post",
            request.uri_path("gifts", id, "cancel"),
            None,
            env,
            headers,
            CancelResponse,
        )

    @staticmethod
    def update_gift(
        id, params: UpdateGiftParams, env=None, headers=None
    ) -> UpdateGiftResponse:
        return request.send(
            "post",
            request.uri_path("gifts", id, "update_gift"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateGiftResponse,
        )
