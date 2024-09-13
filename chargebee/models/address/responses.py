from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class AddressResponse(Model):
    raw_data: Dict[Any, Any] = None
    label: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    company: str = None
    phone: str = None
    addr: str = None
    extended_addr: str = None
    extended_addr2: str = None
    city: str = None
    state_code: str = None
    state: str = None
    country: str = None
    zip: str = None
    validation_status: str = None
    subscription_id: str = None


@dataclass
class RetrieveResponse:
    address: AddressResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class UpdateResponse:
    address: AddressResponse
    response_headers: Dict[Any, Any] = None
