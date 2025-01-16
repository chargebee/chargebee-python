from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


@dataclass
class Comment:

    env: environment.Environment

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

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("comments"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("comments", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("comments"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("comments", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
        )
