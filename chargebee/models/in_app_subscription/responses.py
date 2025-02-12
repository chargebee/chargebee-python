from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


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
class ProcessReceiptResponse(Response):
    is_idempotency_replayed: bool
    in_app_subscription: InAppSubscriptionResponse


@dataclass
class ImportReceiptResponse(Response):
    is_idempotency_replayed: bool
    in_app_subscriptions: List[InAppSubscriptionResponse]


@dataclass
class ImportSubscriptionResponse(Response):
    is_idempotency_replayed: bool
    in_app_subscription: InAppSubscriptionResponse


@dataclass
class RetrieveStoreSubsResponse(Response):
    is_idempotency_replayed: bool
    in_app_subscriptions: List[InAppSubscriptionResponse]
