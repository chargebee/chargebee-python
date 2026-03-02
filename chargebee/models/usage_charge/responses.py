from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class UsageChargeResponse(Model):
    raw_data: Dict[Any, Any] = None
    subscription_id: str = None
    feature_id: str = None
    included_usage: str = None
    total_usage: str = None
    on_demand_usage: str = None
    metered_item_price_id: str = None
    amount: str = None
    currency_code: str = None
    usage_from: int = None
    usage_to: int = None


@dataclass
class RetrieveUsageChargesForSubscriptionUsageChargeResponse:
    usage_charge: UsageChargeResponse


@dataclass
class RetrieveUsageChargesForSubscriptionResponse(Response):
    list: List[RetrieveUsageChargesForSubscriptionUsageChargeResponse]
    next_offset: str = None
