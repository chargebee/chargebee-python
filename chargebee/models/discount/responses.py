from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class DiscountResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    invoice_name: str = None
    type: str = None
    percentage: float = None
    amount: int = None
    currency_code: str = None
    duration_type: str = None
    period: int = None
    period_unit: str = None
    included_in_mrr: bool = None
    apply_on: str = None
    item_price_id: str = None
    created_at: int = None
    apply_till: int = None
    applied_count: int = None
    coupon_id: str = None
    index: int = None
