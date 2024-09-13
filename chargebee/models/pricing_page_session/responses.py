from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class PricingPageSessionResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    url: str = None
    created_at: int = None
    expires_at: int = None


@dataclass
class CreateForNewSubscriptionResponse:
    pricing_page_session: PricingPageSessionResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CreateForExistingSubscriptionResponse:
    pricing_page_session: PricingPageSessionResponse
    response_headers: Dict[Any, Any] = None
