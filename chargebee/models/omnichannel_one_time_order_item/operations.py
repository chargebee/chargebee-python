from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class OmnichannelOneTimeOrderItem:
    env: environment.Environment

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

    pass
