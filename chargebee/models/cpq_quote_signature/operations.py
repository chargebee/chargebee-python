from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class CpqQuoteSignature:
    env: environment.Environment

    class Status(Enum):
        DRAFT = "draft"
        ACTIVE = "active"
        SIGNED = "signed"
        EXPIRED = "expired"
        CANCELLED = "cancelled"
        DECLINED = "declined"

        def __str__(self):
            return self.value

    class CustomerAcceptanceMethod(Enum):
        ESIGN_AND_PAY = "esign_and_pay"
        ESIGN = "esign"
        PAY = "pay"

        def __str__(self):
            return self.value

    class QuoteType(Enum):
        CONSOLIDATED = "consolidated"
        DETAILED = "detailed"

        def __str__(self):
            return self.value

    pass
