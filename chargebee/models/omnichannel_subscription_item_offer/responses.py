from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class OmnichannelSubscriptionItemOfferResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    offer_id_at_source: str = None
    category: str = None
    category_at_source: str = None
    type: str = None
    type_at_source: str = None
    discount_type: str = None
    duration: str = None
    percentage: float = None
    price_currency: str = None
    price_units: int = None
    price_nanos: int = None
    offer_term_start: int = None
    offer_term_end: int = None
    resource_version: int = None
