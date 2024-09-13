from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class TokenResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    gateway: str = None
    gateway_account_id: str = None
    payment_method_type: str = None
    status: str = None
    id_at_vault: str = None
    vault: str = None
    ip_address: str = None
    resource_version: int = None
    updated_at: int = None
    created_at: int = None
    expired_at: int = None
