from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class Execution:
    env: environment.Environment

    class Status(Enum):
        SUCCESS = "success"
        FAILED = "failed"

        def __str__(self):
            return self.value

    pass
