from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Status(Enum):
    MOVED_IN = "moved_in"
    MOVED_OUT = "moved_out"
    MOVING_OUT = "moving_out"

    def __str__(self):
        return self.value


class SiteMigrationDetails(TypedDict):
    entity_id: Required[str]
    other_site_name: Required[str]
    entity_id_at_other_site: Required[str]
    migrated_at: Required[int]
    entity_type: Required[enums.EntityType]
    status: Required[Status]
