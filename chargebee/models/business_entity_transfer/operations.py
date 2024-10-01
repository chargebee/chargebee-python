from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


class BusinessEntityTransfer:
    class ResourceType(Enum):
        CUSTOMER = "customer"
        SUBSCRIPTION = "subscription"

        def __str__(self):
            return self.value

    class ReasonCode(Enum):
        CORRECTION = "correction"

        def __str__(self):
            return self.value

    pass
