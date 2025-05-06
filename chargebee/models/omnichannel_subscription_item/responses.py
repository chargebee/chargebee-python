from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import omnichannel_subscription_item_scheduled_change


@dataclass
class UpcomingRenewalResponse(Model):
    raw_data: Dict[Any, Any] = None
    price_currency: str = None
    price_units: int = None
    price_nanos: int = None


@dataclass
class OmnichannelSubscriptionItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    item_id_at_source: str = None
    item_parent_id_at_source: str = None
    status: str = None
    auto_renew_status: str = None
    current_term_start: int = None
    current_term_end: int = None
    expired_at: int = None
    expiration_reason: str = None
    cancelled_at: int = None
    cancellation_reason: str = None
    grace_period_expires_at: int = None
    has_scheduled_changes: bool = None
    resource_version: int = None
    upcoming_renewal: UpcomingRenewalResponse = None


@dataclass
class ListOmniSubItemScheduleChangesOmnichannelSubscriptionItemResponse:
    omnichannel_subscription_item_scheduled_change: "omnichannel_subscription_item_scheduled_change.OmnichannelSubscriptionItemScheduledChangeResponse"


@dataclass
class ListOmniSubItemScheduleChangesResponse(Response):

    list: List[ListOmniSubItemScheduleChangesOmnichannelSubscriptionItemResponse]
    next_offset: str = None
