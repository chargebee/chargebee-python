from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast


@dataclass
class PromotionalGrant:
    env: environment.Environment

    class PromotionalGrantsParams(TypedDict):
        subscription_id: Required[str]
        unit_id: Required[str]
        amount: Required[str]
        expires_at: Required[int]
        metadata: NotRequired[Dict[Any, Any]]

    def promotional_grants(
        self, params: PromotionalGrantsParams, headers=None
    ) -> PromotionalGrantsResponse:
        jsonKeys = {
            "metadata": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("promotional_grants"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PromotionalGrantsResponse,
            None,
            True,
            jsonKeys,
            options,
            resource="promotionalGrant",
            operation="promotionalGrants",
        )
