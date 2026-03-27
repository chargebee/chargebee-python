from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class Alert:
    env: environment.Environment

    class Status(Enum):
        ENABLED = "enabled"
        DISABLED = "disabled"

        def __str__(self):
            return self.value

    class Scope(Enum):
        GLOBAL = "global"
        SUBSCRIPTION = "subscription"

        def __str__(self):
            return self.value

    pass
