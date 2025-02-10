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
        business_entity_id: NotRequired[str]

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
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("items", id, "attached_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
        )

    def update(self, id, params: UpdateParams, headers=None) -> UpdateResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("attached_items", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
        )

    def retrieve(self, id, params: RetrieveParams, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("attached_items", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
        )

    def delete(self, id, params: DeleteParams, headers=None) -> DeleteResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("attached_items", id, "delete"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
        )

    def list(self, id, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        return request.send_list_request(
            "get",
            request.uri_path("items", id, "attached_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
        )
