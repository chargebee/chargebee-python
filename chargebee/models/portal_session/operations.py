from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any


class PortalSession:

    class CreateParams(TypedDict):
        customer: Required[CreateCustomerParams]
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
