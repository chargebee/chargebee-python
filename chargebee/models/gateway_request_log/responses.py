from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class GatewayRequestLogResponse(Model):
    raw_data: Dict[Any, Any] = None
    log_id: str = None
    url: str = None
    status_code: str = None
    method: str = None
    request_body: str = None
    response_body: str = None
    request_headers: str = None
    response_headers: str = None
    gateway: str = None
    customer_handle: str = None
    invoice_handle: str = None
    transaction_handle: str = None
    payment_method_handle: str = None
    gateway_credential_handle: str = None
    payment_attempt_handle: str = None
    payment_intent_handle: str = None
    payment_method_name: str = None
    operation_name: str = None
    operation_type: str = None
    action_type: str = None
    source: str = None
    trace_id_hash: str = None
    invocation_time: int = None
    response_received_at: int = None
    response_time: int = None


@dataclass
class ListGatewayRequestLogResponse:
    gateway_request_log: GatewayRequestLogResponse


@dataclass
class ListResponse(Response):
    list: List[ListGatewayRequestLogResponse]
    next_offset: str = None


@dataclass
class RetrieveResponse(Response):
    gateway_request_log: GatewayRequestLogResponse
