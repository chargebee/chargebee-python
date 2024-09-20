from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class Status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self):
        return self.value
