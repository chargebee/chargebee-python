from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class QuoteEntitlement:
    env: environment.Environment

    class EntityType(Enum):
        PLAN_PRICE = "plan_price"
        ADDON_PRICE = "addon_price"
        CHARGE_PRICE = "charge_price"

        def __str__(self):
            return self.value

    class ActionType(Enum):
        UPSERT = "upsert"
        REMOVE = "remove"

        def __str__(self):
            return self.value

    class ListQuoteEntitlementsParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        entity_id: NotRequired[Filters.StringFilter]
        start_date: NotRequired[Filters.TimestampFilter]
        end_date: NotRequired[Filters.TimestampFilter]

    def list_quote_entitlements(
        self, id, params: ListQuoteEntitlementsParams = None, headers=None
    ) -> ListQuoteEntitlementsResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("quotes", id, "quote_entitlements"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListQuoteEntitlementsResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="quoteEntitlement",
            operation="listQuoteEntitlements",
        )
