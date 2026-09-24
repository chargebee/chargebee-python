from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class DisputeResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    customer_id: str = None
    transaction_id: str = None
    gateway_account_id: str = None
    id_at_gateway: str = None
    currency_code: str = None
    amount: int = None
    reason: str = None
    status: str = None
    type: str = None
    is_partial_dispute: bool = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None


@dataclass
class RetrieveResponse(Response):
    dispute: DisputeResponse


@dataclass
class ListDisputeResponse:
    dispute: DisputeResponse


@dataclass
class ListResponse(Response):
    list: List[ListDisputeResponse]
    next_offset: str = None
