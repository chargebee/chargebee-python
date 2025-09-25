from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class PersonalizedOffer:
    env: environment.Environment

    class OptionProcessingType(Enum):
        BILLING_UPDATE = "billing_update"
        CHECKOUT = "checkout"
        URL_REDIRECT = "url_redirect"
        WEBHOOK = "webhook"
        EMAIL = "email"

        def __str__(self):
            return self.value

    class OptionProcessingLayout(Enum):
        IN_APP = "in_app"
        FULL_PAGE = "full_page"

        def __str__(self):
            return self.value

    class Content(TypedDict):
        title: Required[str]
        description: Required[str]

    class Option(TypedDict):
        id: Required[str]
        label: Required[str]
        processing_type: Required["PersonalizedOffer.OptionProcessingType"]
        processing_layout: Required["PersonalizedOffer.OptionProcessingLayout"]
        redirect_url: Required[str]

    class PersonalizedOffersRequestContextParams(TypedDict):
        user_agent: NotRequired[str]
        locale: NotRequired[str]
        timezone: NotRequired[str]
        url: NotRequired[str]
        referrer_url: NotRequired[str]

    class PersonalizedOffersParams(TypedDict):
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        email: NotRequired[str]
        roles: NotRequired[List[str]]
        external_user_id: NotRequired[str]
        subscription_id: NotRequired[str]
        customer_id: Required[str]
        custom: NotRequired[Dict[Any, Any]]
        request_context: NotRequired[
            "PersonalizedOffer.PersonalizedOffersRequestContextParams"
        ]

    def personalized_offers(
        self, params: PersonalizedOffersParams, headers=None
    ) -> PersonalizedOffersResponse:
        jsonKeys = {
            "custom": 0,
        }
        options = {}
        return request.send(
            "post",
            request.uri_path("personalized_offers"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PersonalizedOffersResponse,
            "grow",
            True,
            jsonKeys,
            options,
        )
