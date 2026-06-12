from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import ledger_operation, grant_block


@dataclass
class PromotionalGrantResponse(Model):
    raw_data: Dict[Any, Any] = None
    subscription_id: str = None
    unit_id: str = None
    amount: str = None
    expires_at: int = None
    metadata: str = None


@dataclass
class PromotionalGrantsResponse(Response):
    is_idempotency_replayed: bool
    ledger_operations: List["ledger_operation.LedgerOperationResponse"]
    grant_blocks: List["grant_block.GrantBlockResponse"]
