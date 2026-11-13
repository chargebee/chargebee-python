from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class GatewayWebhookLogResponse(Model):
    raw_data: Dict[Any, Any] = None
    webhook_id: str = None
    url: str = None
    method: str = None
    status_code: str = None
    gateway: str = None
    id_at_gateway: str = None
    customer_handle: str = None
    invoice_handle: str = None
    transaction_handle: str = None
    payment_method_handle: str = None
    gateway_credential_handle: str = None
    payment_attempt_handle: str = None
    payment_intent_handle: str = None
    payment_method_name: str = None
    request_body: str = None
    response_body: str = None
    request_headers: str = None
    response_headers: str = None
    received_at: int = None
    response_time: int = None


@dataclass
class ListGatewayWebhookLogResponse:
    gateway_webhook_log: GatewayWebhookLogResponse


@dataclass
class ListResponse(Response):
    list: List[ListGatewayWebhookLogResponse]
    next_offset: str = None


@dataclass
class RetrieveResponse(Response):
    gateway_webhook_log: GatewayWebhookLogResponse
