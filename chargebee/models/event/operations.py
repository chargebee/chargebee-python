from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
import json
from chargebee.main import Environment
from chargebee.filters import Filters


class Event:
    class WebhookStatus(Enum):
        NOT_CONFIGURED = "not_configured"
        SCHEDULED = "scheduled"
        SUCCEEDED = "succeeded"
        RE_SCHEDULED = "re_scheduled"
        FAILED = "failed"
        SKIPPED = "skipped"
        NOT_APPLICABLE = "not_applicable"

        def __str__(self):
            return self.value

    class WebhookWebhookStatus(Enum):
        NOT_CONFIGURED = "not_configured"
        SCHEDULED = "scheduled"
        SUCCEEDED = "succeeded"
        RE_SCHEDULED = "re_scheduled"
        FAILED = "failed"
        SKIPPED = "skipped"
        NOT_APPLICABLE = "not_applicable"

        def __str__(self):
            return self.value

    class Webhook(TypedDict):
        id: Required[str]
        webhook_status: Required["Event.WebhookWebhookStatus"]

    @staticmethod
    def deserialize(json_data) -> EventResponse:
        try:
            webhook_data = json.loads(json_data)
        except (TypeError, ValueError) as ex:
            raise Exception(
                "The passed json_data is not JSON formatted . " + ex.message
            )

        api_version = webhook_data.get("api_version", None)
        env_version = Environment.API_VERSION
        if api_version != None and api_version.upper() != env_version.upper():
            raise Exception(
                "API version ["
                + api_version.upper()
                + "] in response does not match "
                + "with client library API version ["
                + env_version.upper()
                + "]"
            )
        return EventResponse.construct(webhook_data)

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        start_time: NotRequired[int]
        end_time: NotRequired[int]
        id: NotRequired[Filters.StringFilter]
        webhook_status: NotRequired[Filters.EnumFilter]
        event_type: NotRequired[Filters.EnumFilter]
        source: NotRequired[Filters.EnumFilter]
        occurred_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("events"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get", request.uri_path("events", id), None, env, headers, RetrieveResponse
        )
