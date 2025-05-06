from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import payment_intent, contract_term, estimate


@dataclass
class PurchaseResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    customer_id: str = None
    created_at: int = None
    modified_at: int = None
    subscription_ids: List[str] = None
    invoice_ids: List[str] = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    purchase: PurchaseResponse


@dataclass
class EstimateResponse(Response):
    is_idempotency_replayed: bool
    estimate: "estimate.EstimateResponse"
