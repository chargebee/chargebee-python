from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class ScheduleStatus(Enum):
    ACTIVATED = "activated"
    SCHEDULED = "scheduled"
    FAILED = "failed"

    def __str__(self):
        return self.value


class AddEntitlementOverrideForSubscriptionEntitlementOverrideParams(TypedDict):
    feature_id: Required[str]
    value: NotRequired[str]
    expires_at: NotRequired[int]
    effective_from: NotRequired[int]
