from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import entitlement_override


class ScheduleStatus(Enum):
    ACTIVATED = "activated"
    SCHEDULED = "scheduled"
    FAILED = "failed"

    def __str__(self):
        return self.value


class Component(TypedDict):
    entitlement_overrides: NotRequired[entitlement_override.EntitlementOverrideResponse]


class SetSubscriptionEntitlementAvailabilitySubscriptionEntitlementParams(TypedDict):
    feature_id: Required[str]
