from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class AttributeResponse(Model):
    raw_data: Dict[Any, Any] = None
    name: str = None
    value: str = None
