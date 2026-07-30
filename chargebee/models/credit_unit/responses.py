from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class CreditUnitResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    external_name: str = None
    status: str = None
    resource_version: int = None
    updated_at: int = None
    created_at: int = None
    created_by: str = None
    updated_by: str = None
    is_unlimited: bool = None
    overdraft_amount: str = None


@dataclass
class ListCreditUnitResponse:
    credit_unit: CreditUnitResponse


@dataclass
class ListResponse(Response):
    list: List[ListCreditUnitResponse]
    next_offset: str = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    credit_unit: CreditUnitResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    credit_unit: CreditUnitResponse


@dataclass
class ArchiveResponse(Response):
    is_idempotency_replayed: bool
    credit_unit: CreditUnitResponse


@dataclass
class ReactivateResponse(Response):
    is_idempotency_replayed: bool
    credit_unit: CreditUnitResponse
