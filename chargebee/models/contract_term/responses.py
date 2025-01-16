from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class ContractTermResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    status: str = None
    contract_start: int = None
    contract_end: int = None
    billing_cycle: int = None
    action_at_term_end: str = None
    total_contract_value: int = None
    total_contract_value_before_tax: int = None
    cancellation_cutoff_period: int = None
    created_at: int = None
    subscription_id: str = None
    remaining_billing_cycles: int = None
