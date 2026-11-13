from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.models import billing_line_item


@dataclass
class BillingMetadataResponse(Model):
    raw_data: Dict[Any, Any] = None
    item_price_id: str = None
    line_items: List["billing_line_item.BillingLineItemResponse"] = None
