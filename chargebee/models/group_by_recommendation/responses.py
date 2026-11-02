from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class GroupByRecommendationResponse(Model):
    raw_data: Dict[Any, Any] = None
    attribute_name: str = None
    rank: int = None
    reason: str = None
