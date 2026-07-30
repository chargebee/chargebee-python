from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class GrantBlockResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    subscription_id: str = None
    account_type: str = None
    unit_id: str = None
    unit_type: str = None
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
    metadata: Dict[Any, Any] = None


@dataclass
class ListGrantBlocksGrantBlockResponse:
    grant_block: GrantBlockResponse


@dataclass
class ListGrantBlocksResponse(Response):
    list: List[ListGrantBlocksGrantBlockResponse]
    next_offset: str = None
