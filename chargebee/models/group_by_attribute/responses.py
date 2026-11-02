from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class GroupByAttributeResponse(Model):
    raw_data: Dict[Any, Any] = None
    attribute_name: str = None
    rank: int = None
    coverage_percent: int = None
    cardinality: int = None
    remaining_value_count: int = None
    warning: bool = None
    sample_values: List[str] = None
    warning_reasons: List[str] = None
