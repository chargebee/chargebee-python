from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class InstallmentResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    invoice_id: str = None
    date: int = None
    amount: int = None
    status: str = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None


@dataclass
class RetrieveResponse:
    installment: InstallmentResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ListInstallmentResponse:
    installment: InstallmentResponse


@dataclass
class ListResponse:
    list: List[ListInstallmentResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None
