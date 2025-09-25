from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import omnichannel_one_time_order_item, omnichannel_transaction


@dataclass
class OmnichannelOneTimeOrder:
    env: environment.Environment

    class Source(Enum):
        APPLE_APP_STORE = "apple_app_store"
        GOOGLE_PLAY_STORE = "google_play_store"

        def __str__(self):
            return self.value

    class OmnichannelOneTimeOrderItemCancellationReason(Enum):
        CUSTOMER_CANCELLED = "customer_cancelled"
        CUSTOMER_DID_NOT_CONSENT_TO_PRICE_INCREASE = (
            "customer_did_not_consent_to_price_increase"
        )
        REFUNDED_DUE_TO_APP_ISSUE = "refunded_due_to_app_issue"
        REFUNDED_FOR_OTHER_REASON = "refunded_for_other_reason"
        MERCHANT_REVOKED = "merchant_revoked"

        def __str__(self):
            return self.value

    class OmnichannelTransactionType(Enum):
        PURCHASE = "purchase"
        RENEWAL = "renewal"

        def __str__(self):
            return self.value

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        source: NotRequired[Filters.EnumFilter]
        customer_id: NotRequired[Filters.StringFilter]

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("omnichannel_one_time_orders", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("omnichannel_one_time_orders"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )
