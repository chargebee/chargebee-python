from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Status(Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"

    def __str__(self):
        return self.value


class Type(Enum):
    PLAN = "plan"
    ADDON = "addon"
    CHARGE = "charge"

    def __str__(self):
        return self.value


class ItemApplicability(Enum):
    ALL = "all"
    RESTRICTED = "restricted"

    def __str__(self):
        return self.value


class UsageCalculation(Enum):
    SUM_OF_USAGES = "sum_of_usages"
    LAST_USAGE = "last_usage"
    MAX_USAGE = "max_usage"

    def __str__(self):
        return self.value


class ApplicableItem(TypedDict):
    id: NotRequired[str]


class Items(TypedDict):
    id: Required[str]
    name: Required[str]
    external_name: NotRequired[str]
    description: NotRequired[str]
    status: NotRequired[Status]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    item_family_id: NotRequired[str]
    type: Required[Type]
    is_shippable: NotRequired[bool]
    is_giftable: Required[bool]
    redirect_url: NotRequired[str]
    enabled_for_checkout: Required[bool]
    enabled_in_portal: Required[bool]
    included_in_mrr: NotRequired[bool]
    item_applicability: Required[ItemApplicability]
    gift_claim_redirect_url: NotRequired[str]
    unit: NotRequired[str]
    metered: Required[bool]
    usage_calculation: NotRequired[UsageCalculation]
    archived_at: NotRequired[int]
    channel: NotRequired[enums.Channel]
    applicable_items: NotRequired[List[ApplicableItem]]
    metadata: NotRequired[Dict[Any, Any]]
