from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


@dataclass
class AttachedItem:

    env: environment.Environment

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

    def create(self, id, params: CreateParams, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("items", id, "attached_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
        )

    def update(self, id, params: UpdateParams, headers=None) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("attached_items", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
        )

    def retrieve(self, id, params: RetrieveParams, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("attached_items", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveResponse,
        )

    def delete(self, id, params: DeleteParams, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("attached_items", id, "delete"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeleteResponse,
        )

    def list(self, id, params: ListParams = None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("items", id, "attached_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
        )
