from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class PriceVariant:

    env: environment.Environment

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
        business_entity_id: NotRequired[str]
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
        business_entity_id: NotRequired[Filters.StringFilter]
        include_site_level_resources: NotRequired[Filters.BooleanFilter]
        sort_by: NotRequired[Filters.SortFilter]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("price_variants"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("price_variants", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
        )

    def update(self, id, params: UpdateParams, headers=None) -> UpdateResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("price_variants", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("price_variants", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        return request.send_list_request(
            "get",
            request.uri_path("price_variants"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
        )
