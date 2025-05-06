from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class CurrentStateResponse(Model):
    raw_data: Dict[Any, Any] = None
    item_id_at_source: str = None


@dataclass
class ScheduledStateResponse(Model):
    raw_data: Dict[Any, Any] = None
    item_id_at_source: str = None


@dataclass
class OmnichannelSubscriptionItemScheduledChangeResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    omnichannel_subscription_item_id: str = None
    scheduled_at: int = None
    change_type: str = None
    created_at: int = None
    modified_at: int = None
    resource_version: int = None
    current_state: CurrentStateResponse = None
    scheduled_state: ScheduledStateResponse = None
