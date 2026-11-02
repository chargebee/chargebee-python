from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class BusinessEntity:
    env: environment.Environment

    class Status(Enum):
        ACTIVE = "active"
        INACTIVE = "inactive"

        def __str__(self):
            return self.value

    class CreateParams(TypedDict):
        name: Required[str]
        status: Required["BusinessEntity.Status"]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        include_deleted: NotRequired[bool]
        name: NotRequired[Filters.StringFilter]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        status: NotRequired["BusinessEntity.Status"]

    class CreateTransfersParams(TypedDict):
        active_resource_ids: Required[List[str]]
        destination_business_entity_ids: Required[List[str]]
        source_business_entity_ids: NotRequired[List[str]]
        resource_types: Required[List[str]]
        reason_codes: Required[List[str]]

    class GetTransfersParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        resource_type: NotRequired[Filters.StringFilter]
        resource_id: NotRequired[Filters.StringFilter]
        active_resource_id: NotRequired[Filters.StringFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_entities"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessEntity",
            operation="create",
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("business_entities"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessEntity",
            operation="list",
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("business_entities", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessEntity",
            operation="retrieve",
        )

    def update(self, id, params: UpdateParams = None, headers=None) -> UpdateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_entities", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessEntity",
            operation="update",
        )

    def create_transfers(
        self, params: CreateTransfersParams, headers=None
    ) -> CreateTransfersResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_entities", "transfers"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateTransfersResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessEntity",
            operation="createTransfers",
        )

    def get_transfers(
        self, params: GetTransfersParams = None, headers=None
    ) -> GetTransfersResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("business_entities", "transfers"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            GetTransfersResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessEntity",
            operation="getTransfers",
        )
