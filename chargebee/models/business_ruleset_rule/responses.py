from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class BusinessRulesetRuleResponse(Model):
    raw_data: Dict[Any, Any] = None
    rule_id: str = None
    priority: int = None
