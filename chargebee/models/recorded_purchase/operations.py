from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class RecordedPurchase:

    env: environment.Environment

    class Source(Enum):
        APPLE_APP_STORE = "apple_app_store"

        def __str__(self):
            return self.value

    class Status(Enum):
        IN_PROCESS = "in_process"
        COMPLETED = "completed"
        FAILED = "failed"
        IGNORED = "ignored"

        def __str__(self):
            return self.value

    class LinkedOmnichannelSubscription(TypedDict):
        omnichannel_subscription_id: NotRequired[str]

    class ErrorDetail(TypedDict):
        error_message: NotRequired[str]

    class CreateCustomerParams(TypedDict):
        id: Required[str]

    class CreateAppleAppStoreParams(TypedDict):
        transaction_id: NotRequired[str]

    class CreateParams(TypedDict):
        app_id: Required[str]
        customer: Required["RecordedPurchase.CreateCustomerParams"]
        apple_app_store: NotRequired["RecordedPurchase.CreateAppleAppStoreParams"]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("recorded_purchases"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("recorded_purchases", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
        )
