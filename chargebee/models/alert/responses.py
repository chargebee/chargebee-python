from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import filter_condition


@dataclass
class AlertResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    type: str = None
    name: str = None
    description: str = None
    metered_feature_id: str = None
    subscription_id: str = None
    status: str = None
    meta: str = None
    created_at: int = None
    updated_at: int = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    alert: AlertResponse


@dataclass
class RetrieveResponse(Response):
    alert: AlertResponse


@dataclass
class ListAlertResponse:
    alert: AlertResponse


@dataclass
class ListResponse(Response):
    list: List[ListAlertResponse]
    next_offset: str = None


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    alert: AlertResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    alert: AlertResponse


@dataclass
class ApplicationAlertsForSubscriptionAlertResponse:
    alert: AlertResponse


@dataclass
class ApplicationAlertsForSubscriptionResponse(Response):
    list: List[ApplicationAlertsForSubscriptionAlertResponse]
    next_offset: str = None
