from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class QuoteEntitlementResponse(Model):
    raw_data: Dict[Any, Any] = None
    entity_id: str = None
    entity_type: str = None
    action_type: str = None
    feature_id: str = None
    value: str = None
    is_enabled: bool = None
    start_date: int = None
    end_date: int = None
    created_at: int = None
    modified_at: int = None
    is_overridden: bool = None
    feature_name: str = None
    feature_unit: str = None
    feature_type: str = None
    name: str = None
    metered: bool = None


@dataclass
class ListQuoteEntitlementsQuoteEntitlementResponse:
    quote_entitlement: QuoteEntitlementResponse


@dataclass
class ListQuoteEntitlementsResponse(Response):
    list: List[ListQuoteEntitlementsQuoteEntitlementResponse]
    next_offset: str = None
