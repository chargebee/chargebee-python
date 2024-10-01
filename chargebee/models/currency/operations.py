from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


class Currency:
    class ForexType(Enum):
        MANUAL = "manual"
        AUTO = "auto"

        def __str__(self):
            return self.value

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

    @staticmethod
    def list(env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("currencies", "list"),
            None,
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("currencies", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("currencies"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def update(id, params: UpdateParams, env=None, headers=None) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("currencies", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def add_schedule(
        id, params: AddScheduleParams, env=None, headers=None
    ) -> AddScheduleResponse:
        return request.send(
            "post",
            request.uri_path("currencies", id, "add_schedule"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AddScheduleResponse,
        )

    @staticmethod
    def remove_schedule(id, env=None, headers=None) -> RemoveScheduleResponse:
        return request.send(
            "post",
            request.uri_path("currencies", id, "remove_schedule"),
            None,
            env,
            headers,
            RemoveScheduleResponse,
        )
