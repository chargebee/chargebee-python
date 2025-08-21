from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class OmnichannelOneTimeOrderItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    item_id_at_source: str = None
    item_type_at_source: str = None
    quantity: int = None
    cancelled_at: int = None
    cancellation_reason: str = None
    created_at: int = None
    resource_version: int = None
