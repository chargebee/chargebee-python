from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class OfferFulfillment:
    env: environment.Environment

    class ProcessingType(Enum):
        BILLING_UPDATE = "billing_update"
        CHECKOUT = "checkout"
        URL_REDIRECT = "url_redirect"
        WEBHOOK = "webhook"
        EMAIL = "email"

        def __str__(self):
            return self.value

    class Status(Enum):
        IN_PROGRESS = "in_progress"
        COMPLETED = "completed"
        FAILED = "failed"

        def __str__(self):
            return self.value

    class ErrorCode(Enum):
        BILLING_UPDATE_FAILED = "billing_update_failed"
        CHECKOUT_ABANDONED = "checkout_abandoned"
        EXTERNAL_FULFILLMENT_FAILED = "external_fulfillment_failed"
        INTERNAL_ERROR = "internal_error"
        FULFILLMENT_EXPIRED = "fulfillment_expired"

        def __str__(self):
            return self.value

    class Error(TypedDict):
        code: Required["OfferFulfillment.ErrorCode"]
        message: Required[str]

    class OfferFulfillmentsParams(TypedDict):
        personalized_offer_id: Required[str]
        option_id: Required[str]

    class OfferFulfillmentsUpdateParams(TypedDict):
        id: Required[str]
        status: Required["OfferFulfillment.Status"]
        failure_reason: NotRequired[str]

    def offer_fulfillments(
        self, params: OfferFulfillmentsParams, headers=None
    ) -> OfferFulfillmentsResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("offer_fulfillments"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            OfferFulfillmentsResponse,
            "grow",
            True,
            jsonKeys,
            options,
        )

    def offer_fulfillments_get(self, id, headers=None) -> OfferFulfillmentsGetResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("offer_fulfillments", id),
            self.env,
            None,
            headers,
            OfferFulfillmentsGetResponse,
            "grow",
            True,
            jsonKeys,
            options,
        )

    def offer_fulfillments_update(
        self, id, params: OfferFulfillmentsUpdateParams, headers=None
    ) -> OfferFulfillmentsUpdateResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("offer_fulfillments", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            OfferFulfillmentsUpdateResponse,
            "grow",
            True,
            jsonKeys,
            options,
        )
