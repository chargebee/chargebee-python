from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class EinvoiceResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    reference_number: str = None
    status: str = None
    message: str = None
