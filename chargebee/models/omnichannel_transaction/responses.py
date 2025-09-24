from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class LinkedOmnichannelSubscriptionResponse(Model):
    raw_data: Dict[Any, Any] = None
    omnichannel_subscription_id: str = None


@dataclass
class LinkedOmnichannelOneTimeOrderResponse(Model):
    raw_data: Dict[Any, Any] = None
    omnichannel_one_time_order_id: str = None


@dataclass
class OmnichannelTransactionResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    id_at_source: str = None
    app_id: str = None
    price_currency: str = None
    price_units: int = None
    price_nanos: int = None
    type: str = None
    transacted_at: int = None
    created_at: int = None
    resource_version: int = None
    linked_omnichannel_subscriptions: List[LinkedOmnichannelSubscriptionResponse] = None
    linked_omnichannel_one_time_orders: List[LinkedOmnichannelOneTimeOrderResponse] = (
        None
    )
