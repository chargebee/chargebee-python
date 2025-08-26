from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


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
class RetrieveResponse(Response):
    address: AddressResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    address: AddressResponse
