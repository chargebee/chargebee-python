from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class UsageSummaryResponse(Model):
    raw_data: Dict[Any, Any] = None
    subscription_id: str = None
    feature_id: str = None
    aggregated_value: str = None
    aggregated_from: int = None
    aggregated_to: int = None


@dataclass
class RetrieveUsageSummaryForSubscriptionUsageSummaryResponse:
    usage_summary: UsageSummaryResponse


@dataclass
class RetrieveUsageSummaryForSubscriptionResponse(Response):
    list: List[RetrieveUsageSummaryForSubscriptionUsageSummaryResponse]
    next_offset: str = None
