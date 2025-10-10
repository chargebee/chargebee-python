from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class EntitlementOverrideResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    entity_id: str = None
    entity_type: str = None
    feature_id: str = None
    feature_name: str = None
    value: str = None
    name: str = None
    expires_at: int = None
    effective_from: int = None
    schedule_status: str = None


@dataclass
class AddEntitlementOverrideForSubscriptionEntitlementOverrideResponse:
    entitlement_override: EntitlementOverrideResponse


@dataclass
class AddEntitlementOverrideForSubscriptionResponse(Response):
    is_idempotency_replayed: bool
    list: List[AddEntitlementOverrideForSubscriptionEntitlementOverrideResponse]


@dataclass
class ListEntitlementOverrideForSubscriptionEntitlementOverrideResponse:
    entitlement_override: EntitlementOverrideResponse


@dataclass
class ListEntitlementOverrideForSubscriptionResponse(Response):
    list: List[ListEntitlementOverrideForSubscriptionEntitlementOverrideResponse]
    next_offset: str = None
