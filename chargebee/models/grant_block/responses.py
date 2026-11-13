from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import billing_line_item


@dataclass
class ProvisionedBlockBalanceResponse(Model):
    raw_data: Dict[Any, Any] = None
    granted_amount: str = None
    total_balance: str = None
    usable_balance: str = None
    hold_amount: str = None
    used_amount: str = None
    expired_amount: str = None
    rolled_over_amount: str = None
    voided_amount: str = None


@dataclass
class OverdraftBlockBalanceResponse(Model):
    raw_data: Dict[Any, Any] = None
    is_unlimited: bool = None
    limit: str = None
    total_balance: str = None
    usable_balance: str = None
    used_amount: str = None


@dataclass
class BillingMetadataResponse(Model):
    raw_data: Dict[Any, Any] = None
    item_price_id: str = None
    line_items: List[billing_line_item.BillingLineItemResponse] = None


@dataclass
class GrantBlockResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    subscription_id: str = None
    unit_id: str = None
    unit_type: str = None
    account_type: str = None
    granted_amount: str = None
    effective_from: int = None
    expires_at: int = None
    balance: str = None
    hold_amount: str = None
    used_amount: str = None
    expired_amount: str = None
    rolled_over_amount: str = None
    voided_amount: str = None
    origin_grant_block_id: str = None
    status: str = None
    grant_source: str = None
    created_at: int = None
    modified_at: int = None
    resource_version: int = None
    provisioned_block_balance: ProvisionedBlockBalanceResponse = None
    overdraft_block_balance: OverdraftBlockBalanceResponse = None
    billing_metadata: BillingMetadataResponse = None
    metadata: Dict[Any, Any] = None


@dataclass
class ListGrantBlocksGrantBlockResponse:
    grant_block: GrantBlockResponse


@dataclass
class ListGrantBlocksResponse(Response):
    list: List[ListGrantBlocksGrantBlockResponse]
    next_offset: str = None
