from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class OmnichannelSubscriptionItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    item_id_at_source: str = None
    status: str = None
    current_term_start: int = None
    current_term_end: int = None
    expired_at: int = None
    expiration_reason: str = None
    cancelled_at: int = None
    cancellation_reason: str = None
    grace_period_expires_at: int = None
    resource_version: int = None
