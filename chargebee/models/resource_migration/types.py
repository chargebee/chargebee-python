from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Status(Enum):
    SCHEDULED = "scheduled"
    FAILED = "failed"
    SUCCEEDED = "succeeded"

    def __str__(self):
        return self.value


class ResourceMigrations(TypedDict):
    from_site: Required[str]
    entity_type: Required[enums.EntityType]
    entity_id: Required[str]
    status: Required[Status]
    errors: NotRequired[str]
    created_at: Required[int]
    updated_at: Required[int]
