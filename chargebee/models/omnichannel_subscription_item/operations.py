from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class OmnichannelSubscriptionItem:

    env: environment.Environment

    class Status(Enum):
        ACTIVE = "active"
        EXPIRED = "expired"
        CANCELLED = "cancelled"
        IN_DUNNING = "in_dunning"
        IN_GRACE_PERIOD = "in_grace_period"

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

        def __str__(self):
            return self.value

    pass
