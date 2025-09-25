from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import omnichannel_subscription_item, omnichannel_transaction


@dataclass
class OmnichannelSubscription:
    env: environment.Environment

    class Source(Enum):
        APPLE_APP_STORE = "apple_app_store"
        GOOGLE_PLAY_STORE = "google_play_store"

        def __str__(self):
            return self.value

    class OmnichannelSubscriptionItemStatus(Enum):
        ACTIVE = "active"
        EXPIRED = "expired"
        CANCELLED = "cancelled"
        IN_DUNNING = "in_dunning"
        IN_GRACE_PERIOD = "in_grace_period"
        PAUSED = "paused"

        def __str__(self):
            return self.value

    class OmnichannelSubscriptionItemAutoRenewStatus(Enum):
        OFF = "off"
        ON = "on"

        def __str__(self):
            return self.value

    class OmnichannelSubscriptionItemExpirationReason(Enum):
        BILLING_ERROR = "billing_error"
        PRODUCT_NOT_AVAILABLE = "product_not_available"
        OTHER = "other"

        def __str__(self):
            return self.value

    class OmnichannelSubscriptionItemCancellationReason(Enum):
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

    class OmnichannelTransactionsForOmnichannelSubscriptionParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class MoveParams(TypedDict):
        to_customer_id: Required[str]

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("omnichannel_subscriptions", id),
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
            request.uri_path("omnichannel_subscriptions"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def omnichannel_transactions_for_omnichannel_subscription(
        self,
        id,
        params: OmnichannelTransactionsForOmnichannelSubscriptionParams = None,
        headers=None,
    ) -> OmnichannelTransactionsForOmnichannelSubscriptionResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path(
                "omnichannel_subscriptions", id, "omnichannel_transactions"
            ),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            OmnichannelTransactionsForOmnichannelSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def move(self, id, params: MoveParams, headers=None) -> MoveResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("omnichannel_subscriptions", id, "move"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            MoveResponse,
            None,
            False,
            jsonKeys,
            options,
        )
