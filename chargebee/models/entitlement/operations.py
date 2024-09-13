from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.models import enums
from chargebee.filters import Filters


class Entitlement:

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
        entitlements: Required[List[CreateEntitlementParams]]

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
