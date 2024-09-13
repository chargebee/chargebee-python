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
    entitlement_overrides: NotRequired[entitlement_override.EntitlementOverrides]


class SubscriptionEntitlements(TypedDict):
    subscription_id: Required[str]
    feature_id: NotRequired[str]
    feature_name: NotRequired[str]
    feature_unit: NotRequired[str]
    feature_type: NotRequired[str]
    value: NotRequired[str]
    name: NotRequired[str]
    is_overridden: Required[bool]
    is_enabled: Required[bool]
    effective_from: NotRequired[int]
    schedule_status: NotRequired[ScheduleStatus]
    expires_at: NotRequired[int]
    components: NotRequired[Component]


class SetSubscriptionEntitlementAvailabilitySubscriptionEntitlementParams(TypedDict):
    feature_id: Required[str]
