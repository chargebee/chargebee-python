from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class Discount:
    env: environment.Environment

    class Type(Enum):
        FIXED_AMOUNT = "fixed_amount"
        PERCENTAGE = "percentage"
        OFFER_QUANTITY = "offer_quantity"

        def __str__(self):
            return self.value

    pass
