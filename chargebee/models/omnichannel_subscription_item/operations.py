from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import omnichannel_subscription_item_offer


@dataclass
class OmnichannelSubscriptionItem:
    env: environment.Environment

    class Status(Enum):
        ACTIVE = "active"
        EXPIRED = "expired"
        CANCELLED = "cancelled"
        IN_DUNNING = "in_dunning"
        IN_GRACE_PERIOD = "in_grace_period"
        PAUSED = "paused"

        def __str__(self):
            return self.value

    class AutoRenewStatus(Enum):
        OFF = "off"
        ON = "on"

        def __str__(self):
            return self.value

    class ExpirationReason(Enum):
        BILLING_ERROR = "billing_error"
        PRODUCT_NOT_AVAILABLE = "product_not_available"
        OTHER = "other"

        def __str__(self):
            return self.value

    class CancellationReason(Enum):
        CUSTOMER_CANCELLED = "customer_cancelled"
        CUSTOMER_DID_NOT_CONSENT_TO_PRICE_INCREASE = (
            "customer_did_not_consent_to_price_increase"
        )
        REFUNDED_DUE_TO_APP_ISSUE = "refunded_due_to_app_issue"
        REFUNDED_FOR_OTHER_REASON = "refunded_for_other_reason"
        MERCHANT_REVOKED = "merchant_revoked"

        def __str__(self):
            return self.value

    class UpcomingRenewal(TypedDict):
        price_currency: NotRequired[str]
        price_units: NotRequired[int]
        price_nanos: NotRequired[int]

    class LinkedItem(TypedDict):
        id: Required[str]
        linked_at: NotRequired[int]

    class ListOmniSubItemScheduleChangesParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    def list_omni_sub_item_schedule_changes(
        self, id, params: ListOmniSubItemScheduleChangesParams = None, headers=None
    ) -> ListOmniSubItemScheduleChangesResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("omnichannel_subscription_items", id, "scheduled_changes"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListOmniSubItemScheduleChangesResponse,
            None,
            False,
            jsonKeys,
            options,
        )
