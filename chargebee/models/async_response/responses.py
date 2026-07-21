from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class RequestAsyncApiResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    resource: str = None
    operation_type: str = None
    method: str = None
    uri: str = None
    idempotency_key: str = None


@dataclass
class ErrorResponse(Model):
    raw_data: Dict[Any, Any] = None
    message: str = None
    type: str = None
    api_error_code: str = None
    error_code: str = None
    error_msg: str = None
    http_status_code: str = None


@dataclass
class AsyncResponseResponse(Model):
    raw_data: Dict[Any, Any] = None
    api_version: str = None
    created_at: int = None
    completed_at: int = None
    status: str = None
    request: RequestAsyncApiResponse = None
    error_detail: ErrorResponse = None
    result: Dict[Any, Any] = None
