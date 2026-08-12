from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class GatewayPaymentMethodTokenResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    gateway_account_id: str = None
    gateway_name: str = None
    gateway_customer_id: str = None
    gateway_token: str = None
    status: str = None
    created_at: int = None
    updated_at: int = None
