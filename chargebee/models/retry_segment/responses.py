from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class RetrySegmentResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    invoice_id: str = None
    enabled: bool = None
    priority: int = None
    condition_logic: str = None
    criteria: List[Dict[Any, Any]] = None
    retry_settings: Dict[Any, Any] = None


@dataclass
class RetrieveResponse(Response):
    retry_segment: RetrySegmentResponse
