from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class SubscriptionEntitlementsCreatedDetailResponse(Model):
    raw_data: Dict[Any, Any] = None
    subscription_id: str = None
    has_next: bool = None
