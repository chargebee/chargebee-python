from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class Discount:
    env: environment.Environment

    class EntityType(Enum):
        ITEM_LEVEL_COUPON = "item_level_coupon"
        DOCUMENT_LEVEL_COUPON = "document_level_coupon"
        ITEM_LEVEL_DISCOUNT = "item_level_discount"
        DOCUMENT_LEVEL_DISCOUNT = "document_level_discount"

        def __str__(self):
            return self.value

    class Type(Enum):
        FIXED_AMOUNT = "fixed_amount"
        PERCENTAGE = "percentage"
        OFFER_QUANTITY = "offer_quantity"

        def __str__(self):
            return self.value

    pass
