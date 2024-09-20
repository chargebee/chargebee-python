from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Status(Enum):
    SCHEDULED = "scheduled"
    FAILED = "failed"
    SUCCEEDED = "succeeded"

    def __str__(self):
        return self.value
