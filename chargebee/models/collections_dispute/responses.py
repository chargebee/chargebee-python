from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class CollectionsDisputeResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    customer_id: str = None
    invoice_id: str = None
    line_item_id: str = None
    currency_code: str = None
    billed_amount: int = None
    claimed_deduction: int = None
    status: str = None
    dispute_reason_code: str = None
    resolved_reason_code: str = None
    reason: str = None
    opened_at: int = None
    resolved_at: int = None
    created_at: int = None
    updated_at: int = None
    resource_version: int = None
    undisputed_amount: int = None
