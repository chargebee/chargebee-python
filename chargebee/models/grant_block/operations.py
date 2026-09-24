from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class GrantBlock:
    env: environment.Environment

    class UnitType(Enum):
        CREDIT_UNIT = "credit_unit"

        def __str__(self):
            return self.value

    class AccountType(Enum):
        PROVISIONED = "provisioned"
        OVERDRAFT = "overdraft"

        def __str__(self):
            return self.value

    class GrantSource(Enum):
        SUBSCRIPTION_CREATED = "subscription_created"
        SUBSCRIPTION_CHANGED = "subscription_changed"
        TOP_UP = "top_up"
        PROMOTIONAL_GRANTS = "promotional_grants"
        ROLLOVER = "rollover"
        GRANT_RENEWAL = "grant_renewal"
        SUBSCRIPTION_RENEWED = "subscription_renewed"

        def __str__(self):
            return self.value

    class ProvisionedBlockBalance(TypedDict):
        granted_amount: NotRequired[str]
        total_balance: NotRequired[str]
        usable_balance: NotRequired[str]
        hold_amount: NotRequired[str]
        used_amount: NotRequired[str]
        expired_amount: NotRequired[str]
        rolled_over_amount: NotRequired[str]
        voided_amount: NotRequired[str]

    class OverdraftBlockBalance(TypedDict):
        is_unlimited: Required[bool]
        limit: NotRequired[str]
        total_balance: NotRequired[str]
        usable_balance: NotRequired[str]
        used_amount: NotRequired[str]

    class ListGrantBlocksParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        subscription_id: Required[Filters.StringFilter]
        unit_id: NotRequired[Filters.StringFilter]
        account_type: NotRequired[Filters.EnumFilter]
        effective_from: NotRequired[Filters.TimestampFilter]
        expires_at: NotRequired[Filters.TimestampFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]

    def list_grant_blocks(
        self, params: ListGrantBlocksParams, headers=None
    ) -> ListGrantBlocksResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("grant_blocks"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListGrantBlocksResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="grantBlock",
            operation="listGrantBlocks",
        )
