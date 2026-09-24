from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class AppliedBusinessRule:
    env: environment.Environment

    class EntityType(Enum):
        CPQ_QUOTE = "cpq_quote"

        def __str__(self):
            return self.value

    pass
