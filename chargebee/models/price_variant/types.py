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


class PriceVariants(TypedDict):
    id: Required[str]
    name: Required[str]
    external_name: NotRequired[str]
    variant_group: NotRequired[str]
    description: NotRequired[str]
    status: NotRequired[Status]
    created_at: Required[int]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    archived_at: NotRequired[int]
    attributes: NotRequired[List[Attribute]]


class CreateAttributeParams(TypedDict):
    name: Required[str]
    value: Required[str]


class UpdateAttributeParams(TypedDict):
    name: Required[str]
    value: Required[str]
