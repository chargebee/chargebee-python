from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class TaxWithheldResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    user: str = None
    reference_number: str = None
    description: str = None
    type: str = None
    payment_method: str = None
    date: int = None
    currency_code: str = None
    amount: int = None
    resource_version: int = None
    updated_at: int = None
    exchange_rate: float = None
