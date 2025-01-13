from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class OmnichannelTransaction:

    env: environment.Environment

    class Type(Enum):
        PURCHASE = "purchase"
        RENEWAL = "renewal"

        def __str__(self):
            return self.value

    pass
