from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.models import gateway_error_detail


@dataclass
class PaymentAttemptResponse(Model):
    id: str = None
    status: str = None
    payment_method_type: str = None
    id_at_gateway: str = None
    error_code: str = None
    error_text: str = None
    created_at: int = None
    modified_at: int = None
    error_detail: gateway_error_detail.GatewayErrorDetailResponse = None


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
    customer_id: str = None
    gateway: str = None
    active_payment_attempt: PaymentAttemptResponse = None
    business_entity_id: str = None


@dataclass
class CreateResponse:
    payment_intent: PaymentIntentResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class UpdateResponse:
    payment_intent: PaymentIntentResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveResponse:
    payment_intent: PaymentIntentResponse
    response_headers: Dict[Any, Any] = None
