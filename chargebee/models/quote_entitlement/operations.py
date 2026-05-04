from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class QuoteEntitlement:
    env: environment.Environment

    class EntityType(Enum):
        PLAN_PRICE = "plan_price"
        ADDON_PRICE = "addon_price"
        CHARGE_PRICE = "charge_price"
        CHARGE = "charge"

        def __str__(self):
            return self.value

    pass
