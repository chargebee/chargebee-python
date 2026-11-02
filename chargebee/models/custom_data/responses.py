from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class CustomDataResponse(Model):
    raw_data: Dict[Any, Any] = None
    entity_type: str = None
    id: str = None
    schema_id: str = None
    schema_values: str = None
    created_at: int = None
    modified_at: int = None
    updated_at: int = None
