from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import enums


@dataclass
class WebhookEndpoint:
    env: environment.Environment

    class ApiVersion(Enum):
        V1 = "v1"
        V2 = "v2"

        def __str__(self):
            return self.value

    class CreateParams(TypedDict):
        name: Required[str]
        api_version: NotRequired["WebhookEndpoint.ApiVersion"]
        url: Required[str]
        primary_url: NotRequired[bool]
        disabled: NotRequired[bool]
        basic_auth_password: NotRequired[str]
        basic_auth_username: NotRequired[str]
        send_card_resource: NotRequired[bool]
        chargebee_response_schema_type: NotRequired[enums.ChargebeeResponseSchemaType]
        enabled_events: NotRequired[List[enums.EventType]]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        api_version: NotRequired["WebhookEndpoint.ApiVersion"]
        url: NotRequired[str]
        primary_url: NotRequired[bool]
        send_card_resource: NotRequired[bool]
        basic_auth_password: NotRequired[str]
        basic_auth_username: NotRequired[str]
        disabled: NotRequired[bool]
        enabled_events: NotRequired[List[enums.EventType]]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("webhook_endpoints"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update(self, id, params: UpdateParams = None, headers=None) -> UpdateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("webhook_endpoints", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("webhook_endpoints", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("webhook_endpoints", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("webhook_endpoints"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )
