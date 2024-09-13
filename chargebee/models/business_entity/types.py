from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class Status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def __str__(self):
        return self.value


class BusinessEntities(TypedDict):
    id: Required[str]
    name: Required[str]
    status: Required[Status]
    deleted: Required[bool]
    created_at: Required[int]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
