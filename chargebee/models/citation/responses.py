from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class CitationResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    param_name: str = None
    author_name: str = None
    confidence_level: str = None
    created_at: int = None
    content: Dict[Any, Any] = None
