from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class AsyncResponse:
    env: environment.Environment

    class Status(Enum):
        SUCCESS = "success"
        FAILED = "failed"

        def __str__(self):
            return self.value

    class RequestAsyncApi(TypedDict):
        id: Required[str]
        resource: NotRequired[str]
        operation_type: NotRequired[str]
        method: NotRequired[str]
        uri: NotRequired[str]
        idempotency_key: NotRequired[str]

    class Error(TypedDict):
        message: NotRequired[str]
        type: NotRequired[str]
        api_error_code: NotRequired[str]
        error_code: NotRequired[str]
        error_msg: NotRequired[str]
        http_status_code: NotRequired[str]

    pass
