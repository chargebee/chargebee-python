from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Status(Enum):
    MOVED_IN = "moved_in"
    MOVED_OUT = "moved_out"
    MOVING_OUT = "moving_out"

    def __str__(self):
        return self.value
