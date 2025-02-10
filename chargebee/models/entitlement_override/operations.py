from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import enums


@dataclass
class EntitlementOverride:

    env: environment.Environment

    class ScheduleStatus(Enum):
        ACTIVATED = "activated"
        SCHEDULED = "scheduled"
        FAILED = "failed"

        def __str__(self):
            return self.value

    class AddEntitlementOverrideForSubscriptionEntitlementOverrideParams(TypedDict):
        feature_id: Required[str]
        value: NotRequired[str]
        expires_at: NotRequired[int]
        effective_from: NotRequired[int]

    class AddEntitlementOverrideForSubscriptionParams(TypedDict):
        action: NotRequired[enums.Action]
        entitlement_overrides: Required[
            List[
                "EntitlementOverride.AddEntitlementOverrideForSubscriptionEntitlementOverrideParams"
            ]
        ]

    class ListEntitlementOverrideForSubscriptionParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        embed: NotRequired[str]
        include_drafts: NotRequired[bool]
        include_scheduled_overrides: NotRequired[bool]

    def add_entitlement_override_for_subscription(
        self, id, params: AddEntitlementOverrideForSubscriptionParams, headers=None
    ) -> AddEntitlementOverrideForSubscriptionResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "entitlement_overrides"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AddEntitlementOverrideForSubscriptionResponse,
            None,
            False,
            jsonKeys,
        )

    def list_entitlement_override_for_subscription(
        self,
        id,
        params: ListEntitlementOverrideForSubscriptionParams = None,
        headers=None,
    ) -> ListEntitlementOverrideForSubscriptionResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "entitlement_overrides"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListEntitlementOverrideForSubscriptionResponse,
            None,
            False,
            jsonKeys,
        )
