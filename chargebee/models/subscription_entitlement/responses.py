from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import entitlement_override


@dataclass
class ComponentResponse(Model):
    raw_data: Dict[Any, Any] = None
    entitlement_overrides: entitlement_override.EntitlementOverrideResponse = None


@dataclass
class SubscriptionEntitlementResponse(Model):
    raw_data: Dict[Any, Any] = None
    subscription_id: str = None
    feature_id: str = None
    feature_name: str = None
    feature_unit: str = None
    feature_type: str = None
    value: str = None
    name: str = None
    is_overridden: bool = None
    is_enabled: bool = None
    effective_from: int = None
    schedule_status: str = None
    expires_at: int = None
    components: ComponentResponse = None


@dataclass
class SubscriptionEntitlementsForSubscriptionSubscriptionEntitlementResponse:
    subscription_entitlement: SubscriptionEntitlementResponse


@dataclass
class SubscriptionEntitlementsForSubscriptionResponse(Response):

    list: List[SubscriptionEntitlementsForSubscriptionSubscriptionEntitlementResponse]
    next_offset: str = None


@dataclass
class SetSubscriptionEntitlementAvailabilityResponse(Response):
    is_idempotency_replayed: bool
    subscription_entitlement: SubscriptionEntitlementResponse
