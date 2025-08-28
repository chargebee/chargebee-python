from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class WebhookEndpointResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    url: str = None
    send_card_resource: bool = None
    disabled: bool = None
    primary_url: bool = None
    api_version: str = None
    chargebee_response_schema_type: str = None
    enabled_events: List[str] = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    webhook_endpoint: WebhookEndpointResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    webhook_endpoint: WebhookEndpointResponse


@dataclass
class RetrieveResponse(Response):
    webhook_endpoint: WebhookEndpointResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    webhook_endpoint: WebhookEndpointResponse


@dataclass
class ListWebhookEndpointResponse:
    webhook_endpoint: WebhookEndpointResponse


@dataclass
class ListResponse(Response):
    list: List[ListWebhookEndpointResponse]
    next_offset: str = None
