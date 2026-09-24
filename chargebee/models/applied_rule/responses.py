from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class AppliedRuleResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    version: int = None
    name: str = None
    description: str = None
    evaluation_result: bool = None
    error_message: str = None
    actions: List[Dict[Any, Any]] = None
