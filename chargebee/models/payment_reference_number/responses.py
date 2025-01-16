from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class PaymentReferenceNumberResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    type: str = None
    number: str = None
    invoice_id: str = None
