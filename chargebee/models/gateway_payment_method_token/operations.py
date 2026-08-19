from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class GatewayPaymentMethodToken:
    env: environment.Environment

    class Status(Enum):
        ACTIVE = "active"
        INACTIVE = "inactive"
        PENDING_VERIFICATION = "pending_verification"

        def __str__(self):
            return self.value

    pass
