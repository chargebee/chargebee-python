from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any


class PricingPageSession:

    class CreateForNewSubscriptionParams(TypedDict):
        redirect_url: NotRequired[str]
        pricing_page: Required[CreateForNewSubscriptionPricingPageParams]
        subscription: NotRequired[CreateForNewSubscriptionSubscriptionParams]
        business_entity_id: NotRequired[str]
        customer: NotRequired[CreateForNewSubscriptionCustomerParams]
        billing_address: NotRequired[CreateForNewSubscriptionBillingAddressParams]
        shipping_address: NotRequired[CreateForNewSubscriptionShippingAddressParams]

    class CreateForExistingSubscriptionParams(TypedDict):
        redirect_url: NotRequired[str]
        pricing_page: Required[CreateForExistingSubscriptionPricingPageParams]
        subscription: Required[CreateForExistingSubscriptionSubscriptionParams]

    @staticmethod
    def create_for_new_subscription(
        params: CreateForNewSubscriptionParams, env=None, headers=None
    ) -> CreateForNewSubscriptionResponse:
        return request.send(
            "post",
            request.uri_path("pricing_page_sessions", "create_for_new_subscription"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateForNewSubscriptionResponse,
        )

    @staticmethod
    def create_for_existing_subscription(
        params: CreateForExistingSubscriptionParams, env=None, headers=None
    ) -> CreateForExistingSubscriptionResponse:
        return request.send(
            "post",
            request.uri_path(
                "pricing_page_sessions", "create_for_existing_subscription"
            ),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateForExistingSubscriptionResponse,
        )
