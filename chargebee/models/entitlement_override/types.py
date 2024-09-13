from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class ScheduleStatus(Enum):
    ACTIVATED = "activated"
    SCHEDULED = "scheduled"
    FAILED = "failed"

    def __str__(self):
        return self.value


class EntitlementOverrides(TypedDict):
    id: Required[str]
    entity_id: NotRequired[str]
    entity_type: NotRequired[str]
    feature_id: NotRequired[str]
    feature_name: NotRequired[str]
    value: NotRequired[str]
    name: NotRequired[str]
    expires_at: NotRequired[int]
    effective_from: NotRequired[int]
    schedule_status: NotRequired[ScheduleStatus]


class AddEntitlementOverrideForSubscriptionEntitlementOverrideParams(TypedDict):
    feature_id: Required[str]
    value: NotRequired[str]
    expires_at: NotRequired[int]
    effective_from: NotRequired[int]
