from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import customer


@dataclass
class PromotionalCreditResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    customer_id: str = None
    type: str = None
    amount_in_decimal: str = None
    amount: int = None
    currency_code: str = None
    description: str = None
    credit_type: str = None
    reference: str = None
    closing_balance: int = None
    done_by: str = None
    created_at: int = None
    business_entity_id: str = None


@dataclass
class AddResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    promotional_credit: PromotionalCreditResponse


@dataclass
class DeductResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    promotional_credit: PromotionalCreditResponse


@dataclass
class SetResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    promotional_credit: PromotionalCreditResponse


@dataclass
class ListPromotionalCreditResponse:
    promotional_credit: PromotionalCreditResponse


@dataclass
class ListResponse(Response):
    list: List[ListPromotionalCreditResponse]
    next_offset: str = None


@dataclass
class RetrieveResponse(Response):
    promotional_credit: PromotionalCreditResponse
