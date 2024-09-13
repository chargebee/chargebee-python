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


class AttachedItems(TypedDict):
    id: Required[str]
    parent_item_id: Required[str]
    item_id: Required[str]
    type: Required[Type]
    status: NotRequired[Status]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]
    charge_on_event: Required[enums.ChargeOnEvent]
    charge_once: Required[bool]
    created_at: Required[int]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    channel: NotRequired[enums.Channel]
