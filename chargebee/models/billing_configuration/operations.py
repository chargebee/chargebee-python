from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast


@dataclass
class BillingConfiguration:
    env: environment.Environment

    class BillingDate(TypedDict):
        start_date: NotRequired[int]
        end_date: NotRequired[int]

    pass
