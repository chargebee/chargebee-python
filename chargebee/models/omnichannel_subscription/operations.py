from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import omnichannel_subscription_item


@dataclass
class OmnichannelSubscription:

    env: environment.Environment

    class Source(Enum):
        APPLE_APP_STORE = "apple_app_store"

        def __str__(self):
            return self.value

    class OmnichannelSubscriptionItemStatus(Enum):
        ACTIVE = "active"
        EXPIRED = "expired"
        CANCELLED = "cancelled"
        IN_DUNNING = "in_dunning"
        IN_GRACE_PERIOD = "in_grace_period"

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

        def __str__(self):
            return self.value

    class OmnichannelTransactionType(Enum):
        PURCHASE = "purchase"
        RENEWAL = "renewal"

        def __str__(self):
            return self.value

    class OmnichannelTransaction(TypedDict):
        id: Required[str]
        id_at_source: Required[str]
        app_id: Required[str]
        price_currency: Required[str]
        price_units: Required[int]
        price_nanos: Required[int]
        type: Required["OmnichannelSubscription.OmnichannelTransactionType"]
        transacted_at: Required[int]
        created_at: Required[int]
        resource_version: NotRequired[int]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        customer_id: NotRequired[Filters.StringFilter]

    class OmnichannelTransactionsForOmnichannelSubscriptionParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
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
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
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
        )

    def omnichannel_transactions_for_omnichannel_subscription(
        self,
        id,
        params: OmnichannelTransactionsForOmnichannelSubscriptionParams = None,
        headers=None,
    ) -> OmnichannelTransactionsForOmnichannelSubscriptionResponse:
        jsonKeys = {}
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
        )
