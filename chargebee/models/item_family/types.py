from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Status(Enum):
    ACTIVE = "active"
    DELETED = "deleted"

    def __str__(self):
        return self.value


class ItemFamilies(TypedDict):
    id: Required[str]
    name: Required[str]
    description: NotRequired[str]
    status: NotRequired[Status]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    channel: NotRequired[enums.Channel]
