from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class OmnichannelSubscriptionItemMetricResponse(Model):
    raw_data: Dict[Any, Any] = None
    customer_id: str = None
    omnichannel_subscription_id: str = None
    omnichannel_subscription_item_id: str = None
    item_id_at_source: str = None
    mrr_currency: str = None
    mrr_units: int = None
    mrr_nanos: int = None
    effective_from: int = None
    calculated_at: int = None
    created_at: int = None
    resource_version: int = None
