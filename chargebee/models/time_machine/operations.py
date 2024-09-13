from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
import json
from chargebee import OperationFailedError


class TimeMachine:

    class StartAfreshParams(TypedDict):
        genesis_time: NotRequired[int]

    class TravelForwardParams(TypedDict):
        destination_time: NotRequired[int]

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("time_machines", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def start_afresh(
        id, params: StartAfreshParams = None, env=None, headers=None
    ) -> StartAfreshResponse:
        return request.send(
            "post",
            request.uri_path("time_machines", id, "start_afresh"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            StartAfreshResponse,
        )

    @staticmethod
    def travel_forward(
        id, params: TravelForwardParams = None, env=None, headers=None
    ) -> TravelForwardResponse:
        return request.send(
            "post",
            request.uri_path("time_machines", id, "travel_forward"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            TravelForwardResponse,
        )
