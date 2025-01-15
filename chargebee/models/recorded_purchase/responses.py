from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import customer


@dataclass
class LinkedOmnichannelSubscriptionResponse(Model):
    omnichannel_subscription_id: str = None


@dataclass
class ErrorDetailResponse(Model):
    error_message: str = None


@dataclass
class RecordedPurchaseResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    customer_id: str = None
    app_id: str = None
    source: str = None
    status: str = None
    omnichannel_transaction_id: str = None
    created_at: int = None
    resource_version: int = None
    linked_omnichannel_subscriptions: List[LinkedOmnichannelSubscriptionResponse] = None
    error_detail: ErrorDetailResponse = None


@dataclass
class CreateResponse(Response):
    recorded_purchase: RecordedPurchaseResponse
    customer: "customer.CustomerResponse"
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    recorded_purchase: RecordedPurchaseResponse
    headers: Dict[str, str] = None
