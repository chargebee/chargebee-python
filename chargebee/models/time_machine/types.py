from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class TimeTravelStatus(Enum):
    NOT_ENABLED = "not_enabled"
    IN_PROGRESS = "in_progress"
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def __str__(self):
        return self.value


class TimeMachines(TypedDict):
    name: Required[str]
    time_travel_status: Required[TimeTravelStatus]
    genesis_time: Required[int]
    destination_time: Required[int]
    failure_code: NotRequired[str]
    failure_reason: NotRequired[str]
    error_json: NotRequired[str]
