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
    is_idempotency_replayed: bool
    pricing_page_session: PricingPageSessionResponse


@dataclass
class CreateForExistingSubscriptionResponse(Response):
    is_idempotency_replayed: bool
    pricing_page_session: PricingPageSessionResponse
