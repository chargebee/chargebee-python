from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class CollectionsPaymentPromiseResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    customer_id: str = None
    invoice_id: str = None
    status: str = None
    reason: str = None
    promised_by: str = None
    promised_on: int = None
    created_at: int = None
    updated_at: int = None
    resource_version: int = None


@dataclass
class RetrieveResponse(Response):
    collections_payment_promise: CollectionsPaymentPromiseResponse


@dataclass
class ListCollectionsPaymentPromisesCollectionsPaymentPromiseResponse:
    collections_payment_promise: CollectionsPaymentPromiseResponse


@dataclass
class ListCollectionsPaymentPromisesResponse(Response):
    list: List[ListCollectionsPaymentPromisesCollectionsPaymentPromiseResponse]
    next_offset: str = None


@dataclass
class CreateCollectionsPaymentPromiseResponse(Response):
    is_idempotency_replayed: bool
    collections_payment_promises: List[CollectionsPaymentPromiseResponse]


@dataclass
class UpdateCollectionsPaymentPromiseResponse(Response):
    is_idempotency_replayed: bool
    collections_payment_promise: CollectionsPaymentPromiseResponse


@dataclass
class CancelResponse(Response):
    is_idempotency_replayed: bool
    collections_payment_promise: CollectionsPaymentPromiseResponse
