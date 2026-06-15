from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class LedgerAccountBalance:
    env: environment.Environment

    class UnitType(Enum):
        CREDIT_UNIT = "credit_unit"

        def __str__(self):
            return self.value

    class ProvisionedBalance(TypedDict):
        total_balance: Required[str]
        usable_balance: Required[str]
        hold_amount: Required[str]

    class OverdraftBalance(TypedDict):
        is_unlimited: Required[bool]
        limit: NotRequired[str]
        total_balance: NotRequired[str]
        usable_balance: NotRequired[str]
        used_amount: Required[str]
        hold_amount: Required[str]

    class ListLedgerAccountBalancesParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        subscription_id: Required[Filters.StringFilter]
        unit_id: NotRequired[Filters.StringFilter]

    def list_ledger_account_balances(
        self, params: ListLedgerAccountBalancesParams, headers=None
    ) -> ListLedgerAccountBalancesResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("ledger_account_balances"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListLedgerAccountBalancesResponse,
            None,
            False,
            jsonKeys,
            options,
        )
