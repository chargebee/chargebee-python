from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class Installment:

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        sort_by: NotRequired[Filters.SortFilter]
        invoice_id: Required[Filters.StringFilter]

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("installments", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def list(params: ListParams, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("installments"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )
