from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.filters import Filters

@dataclass
class Preference:

    env: environment.Environment

    class Variant(TypedDict):
        value: Required[str]
        allow_override_in_interface: NotRequired[bool]
        allow_override_in_api: NotRequired[bool]
        criteria: NotRequired[List[Criteria]]

    class UpsertPreferenceParams(TypedDict):
        id: Required[str]
        value: Required[str]
        allow_override_in_interface: NotRequired[bool]
        allow_override_in_api: NotRequired[bool]
        variants: NotRequired[List[Dict[Any, Any]]]


    class ListParams(TypedDict):
        setting_group: Required[Filters.EnumFilter]

    class UpsertParams(TypedDict):
        preferences: NotRequired[List["Preference.UpsertPreferenceParams"]]

    def list(self, params: ListParams, headers=None) -> ListResponse:
        jsonKeys = {
        
        }
        options = {
        
        }
        return request.send_list_request(
            "get",
            request.uri_path("preferences"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="preference",
            operation="list",
        )

    def upsert(self, params: UpsertParams, headers=None) -> UpsertResponse:
        jsonKeys = {
        
            "variants": 1,
        
        }
        options = {
        
            "isIdempotent": True,
        
        }
        return request.send(
            "post",
            request.uri_path("preferences"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpsertResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="preference",
            operation="upsert",
        )