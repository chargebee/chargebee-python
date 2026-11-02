from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class Citation:
    env: environment.Environment

    class ConfidenceLevel(Enum):
        LOW = "low"
        MEDIUM = "medium"
        HIGH = "high"
        NOT_PROVIDED = "not_provided"

        def __str__(self):
            return self.value

    pass
