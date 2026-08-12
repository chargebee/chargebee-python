from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class VaultedPaymentMethodResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    customer_id: str = None
    credit_card_id: str = None
    created_at: int = None
    modified_at: int = None


@dataclass
class RetrieveResponse(Response):
    vaulted_payment_method: VaultedPaymentMethodResponse
