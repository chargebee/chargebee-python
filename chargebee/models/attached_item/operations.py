from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


class AttachedItem:
    class Type(Enum):
        RECOMMENDED = "recommended"
        MANDATORY = "mandatory"
        OPTIONAL = "optional"

        def __str__(self):
            return self.value

    class Status(Enum):
        ACTIVE = "active"
        ARCHIVED = "archived"
        DELETED = "deleted"

        def __str__(self):
            return self.value

    class CreateParams(TypedDict):
        item_id: Required[str]
        type: NotRequired["AttachedItem.Type"]
        billing_cycles: NotRequired[int]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        charge_on_event: NotRequired[enums.ChargeOnEvent]
        charge_once: NotRequired[bool]

    class UpdateParams(TypedDict):
        parent_item_id: Required[str]
        type: NotRequired["AttachedItem.Type"]
        billing_cycles: NotRequired[int]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        charge_on_event: NotRequired[enums.ChargeOnEvent]
        charge_once: NotRequired[bool]

    class RetrieveParams(TypedDict):
        parent_item_id: Required[str]

    class DeleteParams(TypedDict):
        parent_item_id: Required[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        item_id: NotRequired[Filters.StringFilter]
        type: NotRequired[Filters.EnumFilter]
        item_type: NotRequired[Filters.EnumFilter]
        charge_on_event: NotRequired[Filters.EnumFilter]
        updated_at: NotRequired[Filters.TimestampFilter]

    @staticmethod
    def create(id, params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("items", id, "attached_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def update(id, params: UpdateParams, env=None, headers=None) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("attached_items", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def retrieve(
        id, params: RetrieveParams, env=None, headers=None
    ) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("attached_items", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def delete(id, params: DeleteParams, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("attached_items", id, "delete"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def list(id, params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("items", id, "attached_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )
