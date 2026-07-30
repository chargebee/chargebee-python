from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class LedgerEntryResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    subscription_id: str = None
    account_type: str = None
    unit_id: str = None
    unit_type: str = None
    amount: str = None
    grant_block_start_balance: str = None
    grant_block_end_balance: str = None
    account_start_balance: str = None
    account_end_balance: str = None
    type: str = None
    ledger_operation_id: str = None
    grant_block_id: str = None
    created_at: int = None
    modified_at: int = None
