from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class AlertStatusResponse(Model):
    raw_data: Dict[Any, Any] = None
    alert_id: str = None
    subscription_id: str = None
    alarm_status: str = None
    alarm_triggered_at: int = None


@dataclass
class AlertStatusesForSubscriptionAlertStatusResponse:
    alert_status: AlertStatusResponse


@dataclass
class AlertStatusesForSubscriptionResponse(Response):
    list: List[AlertStatusesForSubscriptionAlertStatusResponse]
    next_offset: str = None


@dataclass
class AlertStatusesForAlertAlertStatusResponse:
    alert_status: AlertStatusResponse


@dataclass
class AlertStatusesForAlertResponse(Response):
    list: List[AlertStatusesForAlertAlertStatusResponse]
    next_offset: str = None
