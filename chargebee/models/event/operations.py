from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
import json
from chargebee.main import Environment
from chargebee.filters import Filters


class Event:

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        start_time: NotRequired[int]
        end_time: NotRequired[int]
        id: NotRequired[Filters.StringFilter]
        webhook_status: NotRequired[Filters.EnumFilter]
        event_type: NotRequired[Filters.EnumFilter]
        source: NotRequired[Filters.EnumFilter]
        occurred_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("events"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get", request.uri_path("events", id), None, env, headers, RetrieveResponse
        )
