from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


class PriceVariant:
    class Status(Enum):
        ACTIVE = "active"
        ARCHIVED = "archived"
        DELETED = "deleted"

        def __str__(self):
            return self.value

    class Attribute(TypedDict):
        name: Required[str]
        value: Required[str]

    class CreateAttributeParams(TypedDict):
        name: Required[str]
        value: Required[str]

    class UpdateAttributeParams(TypedDict):
        name: Required[str]
        value: Required[str]

    class CreateParams(TypedDict):
        id: Required[str]
        name: Required[str]
        external_name: NotRequired[str]
        description: NotRequired[str]
        variant_group: NotRequired[str]
        attributes: Required[List["PriceVariant.CreateAttributeParams"]]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        external_name: NotRequired[str]
        description: NotRequired[str]
        variant_group: NotRequired[str]
        status: NotRequired["PriceVariant.Status"]
        attributes: Required[List["PriceVariant.UpdateAttributeParams"]]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        name: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("price_variants"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("price_variants", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def update(id, params: UpdateParams, env=None, headers=None) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("price_variants", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("price_variants", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("price_variants"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )
