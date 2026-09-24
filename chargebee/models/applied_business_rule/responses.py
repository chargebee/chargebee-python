from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class AppliedBusinessRuleResponse(Model):
    raw_data: Dict[Any, Any] = None
    handle: str = None
    entity_type: str = None
    entity_id: int = None
    entity_version: int = None
    rule_id: str = None
    version: int = None
    created_at: int = None
    modified_at: int = None
