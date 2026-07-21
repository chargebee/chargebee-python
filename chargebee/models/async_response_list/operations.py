from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import async_response


@dataclass
class AsyncResponseList:
    env: environment.Environment

    class AsyncResponseStatus(Enum):
        SUCCESS = "success"
        FAILED = "failed"

        def __str__(self):
            return self.value

    pass
