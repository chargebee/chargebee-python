from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class RuleResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    version: int = None
    name: str = None
    description: str = None
    evaluation_result: bool = None
    error_message: str = None
    actions: List[Dict[Any, Any]] = None


@dataclass
class ApplyRuleResponse(Model):
    raw_data: Dict[Any, Any] = None
    evaluate: bool = None
    rule_id: str = None
    ruleset_id: str = None
    skip_failed_rules: bool = None
    structured_expression: Dict[Any, Any] = None
    context: Dict[Any, Any] = None
    rules: List[RuleResponse] = None
