from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class ColumnDefinitionResponse(Model):
    raw_data: Dict[Any, Any] = None
    column_name: str = None
    data_type: str = None
