from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


class Feature:
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

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("features"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("features"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def update(
        id, params: UpdateParams = None, env=None, headers=None
    ) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("features", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("features", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("features", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def activate(id, env=None, headers=None) -> ActivateResponse:
        return request.send(
            "post",
            request.uri_path("features", id, "activate_command"),
            None,
            env,
            headers,
            ActivateResponse,
        )

    @staticmethod
    def archive(id, env=None, headers=None) -> ArchiveResponse:
        return request.send(
            "post",
            request.uri_path("features", id, "archive_command"),
            None,
            env,
            headers,
            ArchiveResponse,
        )

    @staticmethod
    def reactivate(id, env=None, headers=None) -> ReactivateResponse:
        return request.send(
            "post",
            request.uri_path("features", id, "reactivate_command"),
            None,
            env,
            headers,
            ReactivateResponse,
        )
