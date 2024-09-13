from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class InstallmentResponse(Model):
    period: int = None
    amount_percentage: float = None


@dataclass
class InstallmentConfigResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    description: str = None
    number_of_installments: int = None
    period_unit: str = None
    period: int = None
    preferred_day: int = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None
    installments: List[InstallmentResponse] = None


@dataclass
class CreateResponse:
    installment_config: InstallmentConfigResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveResponse:
    installment_config: InstallmentConfigResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class DeleteResponse:
    installment_config: InstallmentConfigResponse
    response_headers: Dict[Any, Any] = None
