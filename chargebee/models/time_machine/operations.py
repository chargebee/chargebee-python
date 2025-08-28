from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
import json
from chargebee import OperationFailedError


@dataclass
class TimeMachine:
    env: environment.Environment

    class TimeTravelStatus(Enum):
        NOT_ENABLED = "not_enabled"
        IN_PROGRESS = "in_progress"
        SUCCEEDED = "succeeded"
        FAILED = "failed"

        def __str__(self):
            return self.value

    def wait_for_time_travel_completion(
        self, time_machine: TimeMachineResponse
    ) -> RetrieveResponse:
        import time

        response: RetrieveResponse = None
        count = 0
        retry_delay_ms = (
            3000 if self.env is None else self.env.time_travel_retry_delay_ms
        ) / 1000.0

        while time_machine.time_travel_status == "in_progress":
            if count > 30:
                raise RuntimeError("Time travel is taking too much time")
            count += 1
            time.sleep(retry_delay_ms)
            response = self.retrieve(time_machine.name)
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

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("time_machines", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def start_afresh(
        self, id, params: StartAfreshParams = None, headers=None
    ) -> StartAfreshResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("time_machines", id, "start_afresh"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            StartAfreshResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def travel_forward(
        self, id, params: TravelForwardParams = None, headers=None
    ) -> TravelForwardResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("time_machines", id, "travel_forward"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            TravelForwardResponse,
            None,
            False,
            jsonKeys,
            options,
        )
