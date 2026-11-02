from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class ExecutionResponse(Model):
    raw_data: Dict[Any, Any] = None
    status: str = None
    created_at: int = None
    result: Dict[Any, Any] = None
    error_detail: Dict[Any, Any] = None
    revision_version: int = None
