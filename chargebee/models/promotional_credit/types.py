from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Type(Enum):
    INCREMENT = "increment"
    DECREMENT = "decrement"

    def __str__(self):
        return self.value
