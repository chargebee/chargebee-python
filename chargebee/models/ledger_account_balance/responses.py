from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class ProvisionedBalanceResponse(Model):
    raw_data: Dict[Any, Any] = None
    total_balance: str = None
    usable_balance: str = None
    hold_amount: str = None


@dataclass
class OverdraftBalanceResponse(Model):
    raw_data: Dict[Any, Any] = None
    is_unlimited: bool = None
    limit: str = None
    total_balance: str = None
    usable_balance: str = None
    used_amount: str = None
    hold_amount: str = None


@dataclass
class LedgerAccountBalanceResponse(Model):
    raw_data: Dict[Any, Any] = None
    subscription_id: str = None
    unit_id: str = None
    unit_type: str = None
    modified_at: int = None
    provisioned_balance: ProvisionedBalanceResponse = None
    overdraft_balance: OverdraftBalanceResponse = None


@dataclass
class ListLedgerAccountBalancesLedgerAccountBalanceResponse:
    ledger_account_balance: LedgerAccountBalanceResponse


@dataclass
class ListLedgerAccountBalancesResponse(Response):
    list: List[ListLedgerAccountBalancesLedgerAccountBalanceResponse]
    next_offset: str = None
