from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


class Discount:
    class Type(Enum):
        FIXED_AMOUNT = "fixed_amount"
        PERCENTAGE = "percentage"

        def __str__(self):
            return self.value

    pass
