from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class WebhookResponse(Model):
    id: str = None
    webhook_status: str = None


@dataclass
class EventResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    occurred_at: int = None
    source: str = None
    user: str = None
    webhook_status: str = None
    webhook_failure_reason: str = None
    webhooks: List[WebhookResponse] = None
    event_type: str = None
    api_version: str = None
    content: Dict[Any, Any] = None
    origin_user: str = None


@dataclass
class ListEventResponse:
    event: EventResponse


@dataclass
class ListResponse:
    list: List[ListEventResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    event: EventResponse
    headers: Dict[str, str] = None
