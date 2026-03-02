from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.filters import Filters


@dataclass
class UsageCharge:
    env: environment.Environment

    class RetrieveUsageChargesForSubscriptionParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        feature_id: NotRequired[Filters.StringFilter]

    def retrieve_usage_charges_for_subscription(
        self, id, params: RetrieveUsageChargesForSubscriptionParams = None, headers=None
    ) -> RetrieveUsageChargesForSubscriptionResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "usage_charges"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveUsageChargesForSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )
