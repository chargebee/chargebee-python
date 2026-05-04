from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class FilterCondition:
    env: environment.Environment

    class Field(Enum):
        PLAN_PRICE_ID = "plan_price_id"

        def __str__(self):
            return self.value

    class Operator(Enum):
        EQUALS = "equals"
        NOT_EQUALS = "not_equals"

        def __str__(self):
            return self.value

    pass
