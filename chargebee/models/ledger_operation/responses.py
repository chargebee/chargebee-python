from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import ledger_account_balance, grant_block, ledger_entry


@dataclass
class LedgerOperationResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    subscription_id: str = None
    unit_id: str = None
    unit_type: str = None
    type: str = None
    amount: str = None
    provisioned_start_balance: str = None
    provisioned_end_balance: str = None
    overdraft_start_balance: str = None
    overdraft_end_balance: str = None
    parent_ledger_operation_id: str = None
    ledger_operation_timestamp: int = None
    auto_release_timestamp: int = None
    created_at: int = None
    modified_at: int = None
    metadata: Dict[Any, Any] = None


@dataclass
class RetrieveLedgerOperationResponse(Response):
    ledger_operation: LedgerOperationResponse


@dataclass
class ListLedgerOperationsLedgerOperationResponse:
    ledger_operation: LedgerOperationResponse


@dataclass
class ListLedgerOperationsResponse(Response):
    list: List[ListLedgerOperationsLedgerOperationResponse]
    next_offset: str = None


@dataclass
class CaptureResponse(Response):
    is_idempotency_replayed: bool
    ledger_operation: LedgerOperationResponse
    ledger_account_balance: "ledger_account_balance.LedgerAccountBalanceResponse"
    grant_blocks: List["grant_block.GrantBlockResponse"]
    ledger_entries: List["ledger_entry.LedgerEntryResponse"]


@dataclass
class AuthorizeResponse(Response):
    is_idempotency_replayed: bool
    ledger_operation: LedgerOperationResponse
    ledger_account_balance: "ledger_account_balance.LedgerAccountBalanceResponse"
    grant_blocks: List["grant_block.GrantBlockResponse"]
    ledger_entries: List["ledger_entry.LedgerEntryResponse"]


@dataclass
class CaptureAuthorizationResponse(Response):
    is_idempotency_replayed: bool
    ledger_operation: LedgerOperationResponse
    ledger_account_balance: "ledger_account_balance.LedgerAccountBalanceResponse"
    grant_blocks: List["grant_block.GrantBlockResponse"]
    ledger_entries: List["ledger_entry.LedgerEntryResponse"]


@dataclass
class ReleaseAuthorizationResponse(Response):
    is_idempotency_replayed: bool
    ledger_operation: LedgerOperationResponse
    ledger_account_balance: "ledger_account_balance.LedgerAccountBalanceResponse"
    grant_blocks: List["grant_block.GrantBlockResponse"]
    ledger_entries: List["ledger_entry.LedgerEntryResponse"]


@dataclass
class AllocateResponse(Response):
    is_idempotency_replayed: bool
    ledger_account_balance: "ledger_account_balance.LedgerAccountBalanceResponse"
    ledger_operations: List[LedgerOperationResponse]
    grant_blocks: List["grant_block.GrantBlockResponse"]
    ledger_entries: List["ledger_entry.LedgerEntryResponse"]
