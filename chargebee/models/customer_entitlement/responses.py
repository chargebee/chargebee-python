from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


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
class EntitlementsForCustomerResponse(Response):
    list: List[EntitlementsForCustomerCustomerEntitlementResponse]
    next_offset: str = None
