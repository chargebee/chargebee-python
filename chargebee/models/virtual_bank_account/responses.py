from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.models import customer, transaction


@dataclass
class VirtualBankAccountResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    customer_id: str = None
    email: str = None
    scheme: str = None
    bank_name: str = None
    account_number: str = None
    routing_number: str = None
    swift_code: str = None
    gateway: str = None
    gateway_account_id: str = None
    resource_version: int = None
    updated_at: int = None
    created_at: int = None
    reference_id: str = None
    deleted: bool = None


@dataclass
class CreateUsingPermanentTokenResponse:
    virtual_bank_account: VirtualBankAccountResponse
    customer: "customer.CustomerResponse" = None
    response_headers: Dict[Any, Any] = None


@dataclass
class CreateResponse:
    virtual_bank_account: VirtualBankAccountResponse
    customer: "customer.CustomerResponse" = None
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveResponse:
    virtual_bank_account: VirtualBankAccountResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ListVirtualBankAccountResponse:
    virtual_bank_account: VirtualBankAccountResponse


@dataclass
class ListResponse:
    list: List[ListVirtualBankAccountResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None


@dataclass
class DeleteResponse:
    virtual_bank_account: VirtualBankAccountResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class DeleteLocalResponse:
    virtual_bank_account: VirtualBankAccountResponse
    response_headers: Dict[Any, Any] = None
