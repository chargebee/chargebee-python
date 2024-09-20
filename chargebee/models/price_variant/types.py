from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class Status(Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"

    def __str__(self):
        return self.value


class Attribute(TypedDict):
    name: Required[str]
    value: Required[str]


class CreateAttributeParams(TypedDict):
    name: Required[str]
    value: Required[str]


class UpdateAttributeParams(TypedDict):
    name: Required[str]
    value: Required[str]
