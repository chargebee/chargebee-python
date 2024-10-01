from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


class PortalSession:
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

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("portal_sessions"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("portal_sessions", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def logout(id, env=None, headers=None) -> LogoutResponse:
        return request.send(
            "post",
            request.uri_path("portal_sessions", id, "logout"),
            None,
            env,
            headers,
            LogoutResponse,
        )

    @staticmethod
    def activate(
        id, params: ActivateParams, env=None, headers=None
    ) -> ActivateResponse:
        return request.send(
            "post",
            request.uri_path("portal_sessions", id, "activate"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ActivateResponse,
        )
