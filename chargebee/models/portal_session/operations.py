from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class PortalSession:
    env: environment.Environment

    class Status(Enum):
        CREATED = "created"
        LOGGED_IN = "logged_in"
        LOGGED_OUT = "logged_out"
        NOT_YET_ACTIVATED = "not_yet_activated"
        ACTIVATED = "activated"

        def __str__(self):
            return self.value

    class LinkedCustomer(TypedDict):
        customer_id: Required[str]
        email: NotRequired[str]
        has_billing_address: Required[bool]
        has_payment_method: Required[bool]
        has_active_subscription: Required[bool]

    class CreateCustomerParams(TypedDict):
        id: Required[str]

    class CreateParams(TypedDict):
        customer: Required["PortalSession.CreateCustomerParams"]
        redirect_url: NotRequired[str]
        forward_url: NotRequired[str]

    class ActivateParams(TypedDict):
        token: Required[str]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("portal_sessions"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("portal_sessions", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def logout(self, id, headers=None) -> LogoutResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("portal_sessions", id, "logout"),
            self.env,
            None,
            headers,
            LogoutResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def activate(self, id, params: ActivateParams, headers=None) -> ActivateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("portal_sessions", id, "activate"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ActivateResponse,
            None,
            False,
            jsonKeys,
            options,
        )
