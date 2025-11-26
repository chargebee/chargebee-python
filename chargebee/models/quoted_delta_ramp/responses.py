from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class LineItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    item_level_discount_per_billing_cycle_in_decimal: str = None


@dataclass
class QuotedDeltaRampResponse(Model):
    raw_data: Dict[Any, Any] = None
    line_items: List[LineItemResponse] = None
