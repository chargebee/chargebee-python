from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class Currency:
    env: environment.Environment

    class ForexType(Enum):
        MANUAL = "manual"
        AUTO = "auto"

        def __str__(self):
            return self.value

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class CreateParams(TypedDict):
        currency_code: Required[str]
        forex_type: Required["Currency.ForexType"]
        manual_exchange_rate: NotRequired[str]

    class UpdateParams(TypedDict):
        forex_type: Required["Currency.ForexType"]
        manual_exchange_rate: NotRequired[str]

    class AddScheduleParams(TypedDict):
        manual_exchange_rate: Required[str]
        schedule_at: Required[int]

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("currencies", "list"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
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
            request.uri_path("currencies", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("currencies"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update(self, id, params: UpdateParams, headers=None) -> UpdateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("currencies", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def add_schedule(
        self, id, params: AddScheduleParams, headers=None
    ) -> AddScheduleResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("currencies", id, "add_schedule"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AddScheduleResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def remove_schedule(self, id, headers=None) -> RemoveScheduleResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("currencies", id, "remove_schedule"),
            self.env,
            None,
            headers,
            RemoveScheduleResponse,
            None,
            False,
            jsonKeys,
            options,
        )
