from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
import json
from chargebee import OperationFailedError


class TimeMachine:
    class TimeTravelStatus(Enum):
        NOT_ENABLED = "not_enabled"
        IN_PROGRESS = "in_progress"
        SUCCEEDED = "succeeded"
        FAILED = "failed"

        def __str__(self):
            return self.value

    def wait_for_time_travel_completion(
        time_machine: TimeMachineResponse, env=None
    ) -> RetrieveResponse:
        import time

        count = 0
        sleep_time_millis = (
            3000 if env == None else env.time_travel_sleep_millis
        ) / 1000.0

        while time_machine.time_travel_status == "in_progress":
            if count > 30:
                raise RuntimeError("Time travel is taking too much time")
            count += 1
            time.sleep(sleep_time_millis)
            response = TimeMachine.retrieve(time_machine.name, env)
            time_machine = response.time_machine

        if time_machine.time_travel_status == "failed":
            err = json.loads(time_machine.error_json)
            raise OperationFailedError(err["http_code"], err)

        if time_machine.time_travel_status in ("not_enabled", "_unknown"):
            raise RuntimeError(
                "Time travel is in wrong state '"
                + time_machine.time_travel_status
                + "'"
            )

        return response

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
