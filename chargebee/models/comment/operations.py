from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


class Comment:
    class Type(Enum):
        USER = "user"
        SYSTEM = "system"

        def __str__(self):
            return self.value

    class CreateParams(TypedDict):
        entity_type: Required[enums.EntityType]
        entity_id: Required[str]
        notes: Required[str]
        added_by: NotRequired[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        entity_type: NotRequired[enums.EntityType]
        entity_id: NotRequired[str]
        created_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("comments"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("comments", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("comments"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("comments", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )
