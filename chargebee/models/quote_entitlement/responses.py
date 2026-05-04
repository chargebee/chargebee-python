from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class QuoteEntitlementResponse(Model):
    raw_data: Dict[Any, Any] = None
    entity_id: str = None
    entity_type: str = None
    feature_id: str = None
    value: str = None
    is_enabled: bool = None
    start_date: int = None
    end_date: int = None
    created_at: int = None
    modified_at: int = None
