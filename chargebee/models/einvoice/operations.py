from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class Einvoice:
    env: environment.Environment

    class Status(Enum):
        SCHEDULED = "scheduled"
        SKIPPED = "skipped"
        IN_PROGRESS = "in_progress"
        SUCCESS = "success"
        FAILED = "failed"
        REGISTERED = "registered"

        def __str__(self):
            return self.value

    pass
