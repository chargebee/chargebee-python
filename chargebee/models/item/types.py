from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Status(Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"

    def __str__(self):
        return self.value


class Type(Enum):
    PLAN = "plan"
    ADDON = "addon"
    CHARGE = "charge"

    def __str__(self):
        return self.value


class ItemApplicability(Enum):
    ALL = "all"
    RESTRICTED = "restricted"

    def __str__(self):
        return self.value


class UsageCalculation(Enum):
    SUM_OF_USAGES = "sum_of_usages"
    LAST_USAGE = "last_usage"
    MAX_USAGE = "max_usage"

    def __str__(self):
        return self.value


class ApplicableItem(TypedDict):
    id: NotRequired[str]
