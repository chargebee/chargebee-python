from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


class BusinessEntity:
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

    @staticmethod
    def create_transfers(
        params: CreateTransfersParams, env=None, headers=None
    ) -> CreateTransfersResponse:
        return request.send(
            "post",
            request.uri_path("business_entities", "transfers"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateTransfersResponse,
        )

    @staticmethod
    def get_transfers(
        params: GetTransfersParams = None, env=None, headers=None
    ) -> GetTransfersResponse:
        return request.send(
            "get",
            request.uri_path("business_entities", "transfers"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            GetTransfersResponse,
        )
