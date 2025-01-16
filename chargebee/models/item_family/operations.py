from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class ItemFamily:

    env: environment.Environment

    class Status(Enum):
        ACTIVE = "active"
        DELETED = "deleted"

        def __str__(self):
            return self.value

    class CreateParams(TypedDict):
        id: Required[str]
        name: Required[str]
        description: NotRequired[str]
        business_entity_id: NotRequired[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        name: NotRequired[Filters.StringFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        business_entity_id: NotRequired[Filters.StringFilter]
        include_site_level_resources: NotRequired[Filters.BooleanFilter]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        description: NotRequired[str]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("item_families"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("item_families", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("item_families"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
        )

    def update(self, id, params: UpdateParams = None, headers=None) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("item_families", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("item_families", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
        )
