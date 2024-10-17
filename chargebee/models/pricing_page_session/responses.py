from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class PricingPageSessionResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    url: str = None
    created_at: int = None
    expires_at: int = None


@dataclass
class CreateForNewSubscriptionResponse(Response):
    pricing_page_session: PricingPageSessionResponse
    headers: Dict[str, str] = None


@dataclass
class CreateForExistingSubscriptionResponse(Response):
    pricing_page_session: PricingPageSessionResponse
    headers: Dict[str, str] = None
