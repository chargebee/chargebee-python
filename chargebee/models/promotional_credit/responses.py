from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
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


@dataclass
class AddResponse:
    customer: "customer.CustomerResponse"
    promotional_credit: PromotionalCreditResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class DeductResponse:
    customer: "customer.CustomerResponse"
    promotional_credit: PromotionalCreditResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class SetResponse:
    customer: "customer.CustomerResponse"
    promotional_credit: PromotionalCreditResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ListPromotionalCreditResponse:
    promotional_credit: PromotionalCreditResponse


@dataclass
class ListResponse:
    list: List[ListPromotionalCreditResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveResponse:
    promotional_credit: PromotionalCreditResponse
    response_headers: Dict[Any, Any] = None
