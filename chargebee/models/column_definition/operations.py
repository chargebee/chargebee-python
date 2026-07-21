from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class ColumnDefinition:
    env: environment.Environment

    class DataType(Enum):
        NUMBER = "number"
        STRING = "string"

        def __str__(self):
            return self.value

    pass
