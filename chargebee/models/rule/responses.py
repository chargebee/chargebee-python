from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class RuleResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    namespace: str = None
    rule_name: str = None
    rule_order: int = None
    status: str = None
    conditions: str = None
    outcome: str = None
    deleted: bool = None
    created_at: int = None
    modified_at: int = None


@dataclass
class RetrieveResponse(Response):
    rule: RuleResponse
