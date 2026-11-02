from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class RampIntervalResponse(Model):
    raw_data: Dict[Any, Any] = None
    starting_billing_cycle: int = None
    ending_billing_cycle: int = None
    apply_catalog_price: bool = None
    price: int = None
    price_in_decimal: str = None
