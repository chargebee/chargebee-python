from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class TimeTravelStatus(Enum):
    NOT_ENABLED = "not_enabled"
    IN_PROGRESS = "in_progress"
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def __str__(self):
        return self.value
