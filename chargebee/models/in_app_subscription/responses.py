from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class InAppSubscriptionResponse(Model):
    raw_data: Dict[Any, Any] = None
    app_id: str = None
    subscription_id: str = None
    customer_id: str = None
    plan_id: str = None
    store_status: str = None
    invoice_id: str = None


@dataclass
class ProcessReceiptResponse:
    in_app_subscription: InAppSubscriptionResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ImportReceiptResponse:
    in_app_subscriptions: List[InAppSubscriptionResponse]
    response_headers: Dict[Any, Any] = None


@dataclass
class ImportSubscriptionResponse:
    in_app_subscription: InAppSubscriptionResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveStoreSubsResponse:
    in_app_subscriptions: List[InAppSubscriptionResponse]
    response_headers: Dict[Any, Any] = None
