from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import apply_rule


@dataclass
class BusinessRuleResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    description: str = None
    latest_version: int = None
    active: bool = None
    released_at: int = None
    released_by: str = None
    updated_at: int = None
    updated_by: str = None
    created_by: str = None
    created_at: int = None
    tags: List[Dict[Any, Any]] = None
    structured_expression: Dict[Any, Any] = None
    actions_on_success: List[Dict[Any, Any]] = None
    resource_version: int = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    business_rule: BusinessRuleResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    business_rule: BusinessRuleResponse


@dataclass
class UpdateDraftResponse(Response):
    is_idempotency_replayed: bool
    business_rule: BusinessRuleResponse


@dataclass
class ListBusinessRuleResponse:
    business_rule: BusinessRuleResponse


@dataclass
class ListResponse(Response):
    list: List[ListBusinessRuleResponse]
    next_offset: str = None


@dataclass
class RetrieveResponse(Response):
    business_rule: BusinessRuleResponse


@dataclass
class RetrieveDraftResponse(Response):
    business_rule: BusinessRuleResponse


@dataclass
class DeleteDraftResponse(Response):
    is_idempotency_replayed: bool
    business_rule: BusinessRuleResponse


@dataclass
class ActivateRuleResponse(Response):
    is_idempotency_replayed: bool
    business_rule: BusinessRuleResponse


@dataclass
class DeactivateRuleResponse(Response):
    is_idempotency_replayed: bool
    business_rule: BusinessRuleResponse


@dataclass
class ReleaseRuleResponse(Response):
    is_idempotency_replayed: bool
    business_rule: BusinessRuleResponse


@dataclass
class ApplyRulesResponse(Response):
    is_idempotency_replayed: bool
    apply_rule: "apply_rule.ApplyRuleResponse"
