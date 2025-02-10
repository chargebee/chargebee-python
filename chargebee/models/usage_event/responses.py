from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class UsageEventResponse(Model):
    raw_data: Dict[Any, Any] = None
    subscription_id: str = None
    deduplication_id: str = None
    usage_timestamp: int = None
    properties: Dict[Any, Any] = None


@dataclass
class CreateResponse(Response):
    usage_event: UsageEventResponse
    headers: Dict[str, str] = None


@dataclass
class BatchIngestResponse(Response):
    batch_id: str
    failed_events: List[Any]
    headers: Dict[str, str] = None
