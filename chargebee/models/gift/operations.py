from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums, payment_intent


@dataclass
class Gift:

    env: environment.Environment

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

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {
            "additional_information": 1,
        }
        return request.send(
            "post",
            request.uri_path("gifts"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
        )

    def create_for_items(
        self, params: CreateForItemsParams, headers=None
    ) -> CreateForItemsResponse:
        jsonKeys = {
            "additional_information": 1,
        }
        return request.send(
            "post",
            request.uri_path("gifts", "create_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateForItemsResponse,
            None,
            False,
            jsonKeys,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("gifts", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        return request.send_list_request(
            "get",
            request.uri_path("gifts"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
        )

    def claim(self, id, headers=None) -> ClaimResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("gifts", id, "claim"),
            self.env,
            None,
            headers,
            ClaimResponse,
            None,
            False,
            jsonKeys,
        )

    def cancel(self, id, headers=None) -> CancelResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("gifts", id, "cancel"),
            self.env,
            None,
            headers,
            CancelResponse,
            None,
            False,
            jsonKeys,
        )

    def update_gift(
        self, id, params: UpdateGiftParams, headers=None
    ) -> UpdateGiftResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("gifts", id, "update_gift"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateGiftResponse,
            None,
            False,
            jsonKeys,
        )
