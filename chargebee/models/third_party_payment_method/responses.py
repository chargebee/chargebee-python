from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class ThirdPartyPaymentMethodResponse(Model):
    raw_data: Dict[Any, Any] = None
    type: str = None
    gateway: str = None
    gateway_account_id: str = None
    reference_id: str = None
