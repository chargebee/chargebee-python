from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class Status(Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DRAFT = "draft"

    def __str__(self):
        return self.value


class Type(Enum):
    SWITCH = "switch"
    CUSTOM = "custom"
    QUANTITY = "quantity"
    RANGE = "range"

    def __str__(self):
        return self.value


class Level(TypedDict):
    name: NotRequired[str]
    value: Required[str]
    level: Required[int]
    is_unlimited: Required[bool]


class CreateLevelParams(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]
    is_unlimited: NotRequired[bool]
    level: NotRequired[int]


class UpdateLevelParams(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]
    is_unlimited: NotRequired[bool]
    level: NotRequired[int]
