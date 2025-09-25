from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import payment_intent, subscription, invoice


@dataclass
class GifterResponse(Model):
    raw_data: Dict[Any, Any] = None
    customer_id: str = None
    invoice_id: str = None
    signature: str = None
    note: str = None


@dataclass
class GiftReceiverResponse(Model):
    raw_data: Dict[Any, Any] = None
    customer_id: str = None
    subscription_id: str = None
    first_name: str = None
    last_name: str = None
    email: str = None


@dataclass
class GiftTimelineResponse(Model):
    raw_data: Dict[Any, Any] = None
    status: str = None
    occurred_at: int = None


@dataclass
class GiftResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    status: str = None
    scheduled_at: int = None
    auto_claim: bool = None
    no_expiry: bool = None
    claim_expiry_date: int = None
    resource_version: int = None
    updated_at: int = None
    gifter: GifterResponse = None
    gift_receiver: GiftReceiverResponse = None
    gift_timelines: List[GiftTimelineResponse] = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    gift: GiftResponse
    subscription: "subscription.SubscriptionResponse"
    invoice: "invoice.InvoiceResponse" = None


@dataclass
class CreateForItemsResponse(Response):
    is_idempotency_replayed: bool
    gift: GiftResponse
    subscription: "subscription.SubscriptionResponse"
    invoice: "invoice.InvoiceResponse" = None


@dataclass
class RetrieveResponse(Response):
    gift: GiftResponse
    subscription: "subscription.SubscriptionResponse"


@dataclass
class ListGiftResponse:
    gift: GiftResponse
    subscription: "subscription.SubscriptionResponse"


@dataclass
class ListResponse(Response):
    list: List[ListGiftResponse]
    next_offset: str = None


@dataclass
class ClaimResponse(Response):
    is_idempotency_replayed: bool
    gift: GiftResponse
    subscription: "subscription.SubscriptionResponse"


@dataclass
class CancelResponse(Response):
    is_idempotency_replayed: bool
    gift: GiftResponse
    subscription: "subscription.SubscriptionResponse"


@dataclass
class UpdateGiftResponse(Response):
    is_idempotency_replayed: bool
    gift: GiftResponse
    subscription: "subscription.SubscriptionResponse"
