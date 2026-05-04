from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class FilterConditionResponse(Model):
    raw_data: Dict[Any, Any] = None
    field: str = None
    operator: str = None
    value: str = None
