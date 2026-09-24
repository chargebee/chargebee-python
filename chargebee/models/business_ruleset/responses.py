from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import business_ruleset_rule


@dataclass
class BusinessRulesetResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    description: str = None
    active: bool = None
    execute_mode: str = None
    updated_at: int = None
    updated_by: str = None
    created_by: str = None
    created_at: int = None
    rules: List[Dict[Any, Any]] = None
    resource_version: int = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    business_ruleset: BusinessRulesetResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    business_ruleset: BusinessRulesetResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    business_ruleset: BusinessRulesetResponse


@dataclass
class ActivateResponse(Response):
    is_idempotency_replayed: bool
    business_ruleset: BusinessRulesetResponse


@dataclass
class DeactivateResponse(Response):
    is_idempotency_replayed: bool
    business_ruleset: BusinessRulesetResponse


@dataclass
class AddRulesResponse(Response):
    is_idempotency_replayed: bool
    business_ruleset: BusinessRulesetResponse


@dataclass
class RemoveRulesResponse(Response):
    is_idempotency_replayed: bool
    business_ruleset: BusinessRulesetResponse


@dataclass
class ListRulesResponse(Response):
    business_ruleset_rule: "business_ruleset_rule.BusinessRulesetRuleResponse"


@dataclass
class ListBusinessRulesetResponse:
    business_ruleset: BusinessRulesetResponse


@dataclass
class ListResponse(Response):
    list: List[ListBusinessRulesetResponse]
    next_offset: str = None


@dataclass
class RetrieveResponse(Response):
    business_ruleset: BusinessRulesetResponse
