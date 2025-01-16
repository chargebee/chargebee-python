from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
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
class CreateUsingPermanentTokenResponse(Response):
    virtual_bank_account: VirtualBankAccountResponse
    customer: "customer.CustomerResponse" = None
    headers: Dict[str, str] = None


@dataclass
class CreateResponse(Response):
    virtual_bank_account: VirtualBankAccountResponse
    customer: "customer.CustomerResponse" = None
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    virtual_bank_account: VirtualBankAccountResponse
    headers: Dict[str, str] = None


@dataclass
class ListVirtualBankAccountResponse:
    virtual_bank_account: VirtualBankAccountResponse


@dataclass
class ListResponse:
    list: List[ListVirtualBankAccountResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class DeleteResponse(Response):
    virtual_bank_account: VirtualBankAccountResponse
    headers: Dict[str, str] = None


@dataclass
class DeleteLocalResponse(Response):
    virtual_bank_account: VirtualBankAccountResponse
    headers: Dict[str, str] = None
