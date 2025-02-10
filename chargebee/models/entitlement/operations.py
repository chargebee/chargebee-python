from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


@dataclass
class Entitlement:

    env: environment.Environment

    class EntityType(Enum):
        PLAN = "plan"
        ADDON = "addon"
        CHARGE = "charge"
        PLAN_PRICE = "plan_price"
        ADDON_PRICE = "addon_price"

        def __str__(self):
            return self.value

    class CreateEntitlementParams(TypedDict):
        entity_id: Required[str]
        feature_id: Required[str]
        entity_type: NotRequired["Entitlement.EntityType"]
        value: NotRequired[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        feature_id: NotRequired[Filters.StringFilter]
        entity_type: NotRequired[Filters.EnumFilter]
        entity_id: NotRequired[Filters.StringFilter]
        include_drafts: NotRequired[bool]
        embed: NotRequired[str]

    class CreateParams(TypedDict):
        action: Required[enums.Action]
        entitlements: Required[List["Entitlement.CreateEntitlementParams"]]

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        return request.send_list_request(
            "get",
            request.uri_path("entitlements"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
        )

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("entitlements"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
        )
