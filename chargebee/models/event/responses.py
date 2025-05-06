from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class WebhookResponse(Model):
    raw_data: Dict[Any, Any] = None
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
class ListResponse(Response):

    list: List[ListEventResponse]
    next_offset: str = None


@dataclass
class RetrieveResponse(Response):

    event: EventResponse
