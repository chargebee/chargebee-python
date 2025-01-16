from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class HierarchyResponse(Model):
    raw_data: Dict[Any, Any] = None
    customer_id: str = None
    parent_id: str = None
    payment_owner_id: str = None
    invoice_owner_id: str = None
    children_ids: List[str] = None
