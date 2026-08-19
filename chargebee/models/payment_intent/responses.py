from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import gateway_error_detail


@dataclass
class PaymentAttemptResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    status: str = None
    payment_method_type: str = None
    id_at_gateway: str = None
    error_code: str = None
    error_text: str = None
    checkout_details: str = None
    created_at: int = None
    modified_at: int = None
    error_detail: gateway_error_detail.GatewayErrorDetailResponse = None
    routing_rule_id: str = None
    payment_method_display_rule_id: str = None


@dataclass
class PaymentAttemptResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    status: str = None
    payment_method_type: str = None
    id_at_gateway: str = None
    error_code: str = None
    error_text: str = None
    checkout_details: str = None
    created_at: int = None
    modified_at: int = None
    error_detail: gateway_error_detail.GatewayErrorDetailResponse = None
    routing_rule_id: str = None
    payment_method_display_rule_id: str = None


@dataclass
class PaymentIntentMetadataResponse(Model):
    raw_data: Dict[Any, Any] = None
    source: str = None
    client_ip_address: str = None
    user_agent: str = None
    created_at: int = None


@dataclass
class PaymentIntentResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    status: str = None
    currency_code: str = None
    amount: int = None
    gateway_account_id: str = None
    expires_at: int = None
    reference_id: str = None
    payment_method_type: str = None
    success_url: str = None
    failure_url: str = None
    created_at: int = None
    modified_at: int = None
    resource_version: int = None
    updated_at: int = None
    payment_method_options: Dict[Any, Any] = None
    customer_id: str = None
    gateway: str = None
    active_payment_attempt: PaymentAttemptResponse = None
    payment_attempts: List[PaymentAttemptResponse] = None
    payment_intent_metadata: PaymentIntentMetadataResponse = None
    business_entity_id: str = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    payment_intent: PaymentIntentResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    payment_intent: PaymentIntentResponse


@dataclass
class RetrieveResponse(Response):
    payment_intent: PaymentIntentResponse
