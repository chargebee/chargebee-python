from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class BusinessEntityTransferResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    resource_type: str = None
    resource_id: str = None
    active_resource_id: str = None
    destination_business_entity_id: str = None
    source_business_entity_id: str = None
    reason_code: str = None
    created_at: int = None
