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


class BusinessEntityTransfers(TypedDict):
    id: Required[str]
    resource_type: Required[ResourceType]
    resource_id: Required[str]
    active_resource_id: Required[str]
    destination_business_entity_id: Required[str]
    source_business_entity_id: Required[str]
    reason_code: Required[ReasonCode]
    created_at: Required[int]
