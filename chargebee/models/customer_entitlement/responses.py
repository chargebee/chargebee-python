from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class CustomerEntitlementResponse(Model):
    raw_data: Dict[Any, Any] = None
    customer_id: str = None
    subscription_id: str = None
    feature_id: str = None
    value: str = None
    name: str = None
    is_enabled: bool = None


@dataclass
class EntitlementsForCustomerCustomerEntitlementResponse:
    customer_entitlement: CustomerEntitlementResponse


@dataclass
class EntitlementsForCustomerResponse:
    list: List[EntitlementsForCustomerCustomerEntitlementResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None
