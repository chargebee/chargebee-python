from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class VirtualBankAccount:

    class CreateUsingPermanentTokenParams(TypedDict):
        customer_id: Required[str]
        reference_id: Required[str]
        scheme: NotRequired[Scheme]

    class CreateParams(TypedDict):
        customer_id: Required[str]
        email: NotRequired[str]
        scheme: NotRequired[Scheme]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        customer_id: NotRequired[Filters.StringFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        created_at: NotRequired[Filters.TimestampFilter]

    @staticmethod
    def create_using_permanent_token(
        params: CreateUsingPermanentTokenParams, env=None, headers=None
    ) -> CreateUsingPermanentTokenResponse:
        return request.send(
            "post",
            request.uri_path("virtual_bank_accounts", "create_using_permanent_token"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateUsingPermanentTokenResponse,
        )

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("virtual_bank_accounts"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("virtual_bank_accounts", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("virtual_bank_accounts"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("virtual_bank_accounts", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def delete_local(id, env=None, headers=None) -> DeleteLocalResponse:
        return request.send(
            "post",
            request.uri_path("virtual_bank_accounts", id, "delete_local"),
            None,
            env,
            headers,
            DeleteLocalResponse,
        )
