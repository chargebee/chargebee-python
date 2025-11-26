from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast


@dataclass
class QuotedDeltaRamp:
    env: environment.Environment

    class LineItem(TypedDict):
        item_level_discount_per_billing_cycle_in_decimal: NotRequired[str]

    pass
