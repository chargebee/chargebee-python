from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any


class Gift:

    class CreateParams(TypedDict):
        scheduled_at: NotRequired[int]
        auto_claim: NotRequired[bool]
        no_expiry: NotRequired[bool]
        claim_expiry_date: NotRequired[int]
        gifter: Required[CreateGifterParams]
        gift_receiver: Required[CreateGiftReceiverParams]
        coupon_ids: NotRequired[List[str]]
        payment_intent: NotRequired[CreatePaymentIntentParams]
        shipping_address: NotRequired[CreateShippingAddressParams]
        subscription: Required[CreateSubscriptionParams]
        addons: NotRequired[List[CreateAddonParams]]

    class CreateForItemsParams(TypedDict):
        scheduled_at: NotRequired[int]
        auto_claim: NotRequired[bool]
        no_expiry: NotRequired[bool]
        claim_expiry_date: NotRequired[int]
        gifter: Required[CreateForItemsGifterParams]
        gift_receiver: Required[CreateForItemsGiftReceiverParams]
        coupon_ids: NotRequired[List[str]]
        payment_intent: NotRequired[CreateForItemsPaymentIntentParams]
        shipping_address: NotRequired[CreateForItemsShippingAddressParams]
        subscription_items: NotRequired[List[CreateForItemsSubscriptionItemParams]]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        gift_receiver: NotRequired[ListGiftReceiverParams]
        gifter: NotRequired[ListGifterParams]
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
