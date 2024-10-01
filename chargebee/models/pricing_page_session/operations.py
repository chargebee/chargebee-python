from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.models import enums


class PricingPageSession:

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

    class CreateForNewSubscriptionParams(TypedDict):
        redirect_url: NotRequired[str]
        pricing_page: Required[
            "PricingPageSession.CreateForNewSubscriptionPricingPageParams"
        ]
        subscription: NotRequired[
            "PricingPageSession.CreateForNewSubscriptionSubscriptionParams"
        ]
        business_entity_id: NotRequired[str]
        customer: NotRequired[
            "PricingPageSession.CreateForNewSubscriptionCustomerParams"
        ]
        billing_address: NotRequired[
            "PricingPageSession.CreateForNewSubscriptionBillingAddressParams"
        ]
        shipping_address: NotRequired[
            "PricingPageSession.CreateForNewSubscriptionShippingAddressParams"
        ]

    class CreateForExistingSubscriptionParams(TypedDict):
        redirect_url: NotRequired[str]
        pricing_page: Required[
            "PricingPageSession.CreateForExistingSubscriptionPricingPageParams"
        ]
        subscription: Required[
            "PricingPageSession.CreateForExistingSubscriptionSubscriptionParams"
        ]

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
