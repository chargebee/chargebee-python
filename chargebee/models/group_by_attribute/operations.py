from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class GroupByAttribute:
    env: environment.Environment

    class WarningReasons(Enum):
        LOW_COVERAGE = "low_coverage"
        HIGH_CARDINALITY = "high_cardinality"

        def __str__(self):
            return self.value

    pass
