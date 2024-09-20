from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Status(Enum):
    ACTIVE = "active"
    DELETED = "deleted"

    def __str__(self):
        return self.value
