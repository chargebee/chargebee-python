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
    in_app_subscription: InAppSubscriptionResponse
    headers: Dict[str, str] = None


@dataclass
class ImportReceiptResponse(Response):
    in_app_subscriptions: List[InAppSubscriptionResponse]
    headers: Dict[str, str] = None


@dataclass
class ImportSubscriptionResponse(Response):
    in_app_subscription: InAppSubscriptionResponse
    headers: Dict[str, str] = None


@dataclass
class RetrieveStoreSubsResponse(Response):
    in_app_subscriptions: List[InAppSubscriptionResponse]
    headers: Dict[str, str] = None
