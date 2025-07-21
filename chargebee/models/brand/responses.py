from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class BrandResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
