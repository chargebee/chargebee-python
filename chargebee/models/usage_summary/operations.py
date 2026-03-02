from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.models import enums


@dataclass
class UsageSummary:
    env: environment.Environment

    class RetrieveUsageSummaryForSubscriptionParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        feature_id: Required[str]
        window_size: NotRequired[enums.WindowSize]
        timeframe_start: NotRequired[int]
        timeframe_end: NotRequired[int]

    def retrieve_usage_summary_for_subscription(
        self, id, params: RetrieveUsageSummaryForSubscriptionParams, headers=None
    ) -> RetrieveUsageSummaryForSubscriptionResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "usage_summary"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveUsageSummaryForSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )
