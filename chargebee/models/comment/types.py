from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Type(Enum):
    USER = "user"
    SYSTEM = "system"

    def __str__(self):
        return self.value


class Comments(TypedDict):
    id: Required[str]
    entity_type: Required[enums.EntityType]
    added_by: NotRequired[str]
    notes: Required[str]
    created_at: Required[int]
    type: Required[Type]
    entity_id: Required[str]
