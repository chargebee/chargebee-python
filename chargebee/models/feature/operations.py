from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class Feature:
    env: environment.Environment

    class Status(Enum):
        ACTIVE = "active"
        ARCHIVED = "archived"
        DRAFT = "draft"

        def __str__(self):
            return self.value

    class Type(Enum):
        SWITCH = "switch"
        CUSTOM = "custom"
        QUANTITY = "quantity"
        RANGE = "range"

        def __str__(self):
            return self.value

    class Level(TypedDict):
        name: NotRequired[str]
        value: Required[str]
        level: Required[int]
        is_unlimited: Required[bool]

    class CreateLevelParams(TypedDict):
        name: NotRequired[str]
        value: NotRequired[str]
        is_unlimited: NotRequired[bool]
        level: NotRequired[int]

    class UpdateLevelParams(TypedDict):
        name: NotRequired[str]
        value: NotRequired[str]
        is_unlimited: NotRequired[bool]
        level: NotRequired[int]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        name: NotRequired[Filters.StringFilter]
        id: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]
        type: NotRequired[Filters.EnumFilter]

    class CreateParams(TypedDict):
        id: NotRequired[str]
        name: Required[str]
        description: NotRequired[str]
        type: NotRequired["Feature.Type"]
        unit: NotRequired[str]
        levels: NotRequired[List["Feature.CreateLevelParams"]]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        description: NotRequired[str]
        unit: NotRequired[str]
        levels: NotRequired[List["Feature.UpdateLevelParams"]]

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("features"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("features"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update(self, id, params: UpdateParams = None, headers=None) -> UpdateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("features", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
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
            request.uri_path("features", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("features", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def activate(self, id, headers=None) -> ActivateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("features", id, "activate_command"),
            self.env,
            None,
            headers,
            ActivateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def archive(self, id, headers=None) -> ArchiveResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("features", id, "archive_command"),
            self.env,
            None,
            headers,
            ArchiveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def reactivate(self, id, headers=None) -> ReactivateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("features", id, "reactivate_command"),
            self.env,
            None,
            headers,
            ReactivateResponse,
            None,
            False,
            jsonKeys,
            options,
        )
