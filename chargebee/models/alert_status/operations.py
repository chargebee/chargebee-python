from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.filters import Filters


@dataclass
class AlertStatus:
    env: environment.Environment

    class AlertStatusesForSubscriptionParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        alarm_status: NotRequired[Filters.EnumFilter]
        alert_id: NotRequired[Filters.StringFilter]

    class AlertStatusesForAlertParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        alarm_status: NotRequired[Filters.EnumFilter]

    def alert_statuses_for_subscription(
        self, id, params: AlertStatusesForSubscriptionParams = None, headers=None
    ) -> AlertStatusesForSubscriptionResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "alert_statuses"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AlertStatusesForSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def alert_statuses_for_alert(
        self, id, params: AlertStatusesForAlertParams = None, headers=None
    ) -> AlertStatusesForAlertResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("alerts", id, "alert_statuses"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AlertStatusesForAlertResponse,
            None,
            False,
            jsonKeys,
            options,
        )
