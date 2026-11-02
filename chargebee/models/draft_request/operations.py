from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class DraftRequest:
    env: environment.Environment

    class Status(Enum):
        OPEN = "open"
        EXECUTED = "executed"

        def __str__(self):
            return self.value

    class ExecutionStatus(Enum):
        SUCCESS = "success"
        FAILED = "failed"

        def __str__(self):
            return self.value

    class DraftRevision(TypedDict):
        version: Required[int]
        created_at: Required[int]
        payload: NotRequired[Dict[Any, Any]]

    class Validation(TypedDict):
        category: NotRequired[str]
        level: NotRequired[str]
        message: NotRequired[str]
        param_name: NotRequired[str]
        type: NotRequired[str]

    class Execution(TypedDict):
        status: Required["DraftRequest.ExecutionStatus"]
        created_at: Required[int]
        result: NotRequired[Dict[Any, Any]]
        error_detail: NotRequired[Dict[Any, Any]]
        revision_version: NotRequired[int]

    pass
