from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


class Entitlement:
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

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("entitlements"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("entitlements"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )
