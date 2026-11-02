from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class CollectionsDispute:
    env: environment.Environment

    class Status(Enum):
        OPEN = "open"
        RESOLVED = "resolved"
        WITHDRAWN = "withdrawn"

        def __str__(self):
            return self.value

    pass
