from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class CustomDataSchemaResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    display_name: str = None
    entity_type: str = None
    schema_definition: str = None
    status: str = None
    created_at: int = None
    modified_at: int = None
    updated_at: int = None
