from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class ResourceType(Enum):
    CUSTOMER = "customer"
    SUBSCRIPTION = "subscription"

    def __str__(self):
        return self.value


class ReasonCode(Enum):
    CORRECTION = "correction"

    def __str__(self):
        return self.value
