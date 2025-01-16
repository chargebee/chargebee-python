from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class OmnichannelTransactionResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    id_at_source: str = None
    app_id: str = None
    price_currency: str = None
    price_units: int = None
    price_nanos: int = None
    type: str = None
    transacted_at: int = None
    created_at: int = None
    resource_version: int = None
