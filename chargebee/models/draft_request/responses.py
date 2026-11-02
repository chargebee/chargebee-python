from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import citation, draft_estimate, comment


@dataclass
class DraftRevisionResponse(Model):
    raw_data: Dict[Any, Any] = None
    version: int = None
    created_at: int = None
    payload: Dict[Any, Any] = None


@dataclass
class ValidationResponse(Model):
    raw_data: Dict[Any, Any] = None
    category: str = None
    level: str = None
    message: str = None
    param_name: str = None
    type: str = None


@dataclass
class ExecutionResponse(Model):
    raw_data: Dict[Any, Any] = None
    status: str = None
    created_at: int = None
    result: Dict[Any, Any] = None
    error_detail: Dict[Any, Any] = None
    revision_version: int = None


@dataclass
class DraftRequestResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    path_param: str = None
    request_uri: str = None
    operation_id: str = None
    status: str = None
    executed_at: int = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None
    current_revision: DraftRevisionResponse = None
    validations: List[ValidationResponse] = None
    has_comments: bool = None
    has_citations: bool = None
    executions: List[ExecutionResponse] = None
