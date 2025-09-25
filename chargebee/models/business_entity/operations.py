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
        )
