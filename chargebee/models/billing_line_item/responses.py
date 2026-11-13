from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class BillingLineItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    invoice_number: str = None
    quantity: float = None
