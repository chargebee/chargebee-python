from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.models import contract_term, estimate


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
class CreateResponse:
    purchase: PurchaseResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class EstimateResponse:
    estimate: "estimate.EstimateResponse"
    response_headers: Dict[Any, Any] = None
