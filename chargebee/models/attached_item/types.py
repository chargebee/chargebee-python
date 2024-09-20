from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Type(Enum):
    RECOMMENDED = "recommended"
    MANDATORY = "mandatory"
    OPTIONAL = "optional"

    def __str__(self):
        return self.value


class Status(Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"

    def __str__(self):
        return self.value
