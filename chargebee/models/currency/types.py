from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class ForexType(Enum):
    MANUAL = "manual"
    AUTO = "auto"

    def __str__(self):
        return self.value
