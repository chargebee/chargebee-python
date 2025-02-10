from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import entitlement_override


@dataclass
class SubscriptionEntitlement:

    env: environment.Environment

    class ScheduleStatus(Enum):
        ACTIVATED = "activated"
        SCHEDULED = "scheduled"
        FAILED = "failed"

        def __str__(self):
            return self.value

    class Component(TypedDict):
        entitlement_overrides: NotRequired[
            entitlement_override.EntitlementOverrideResponse
        ]

    class SetSubscriptionEntitlementAvailabilitySubscriptionEntitlementParams(
        TypedDict
    ):
        feature_id: Required[str]

    class SubscriptionEntitlementsForSubscriptionParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        include_drafts: NotRequired[bool]
        embed: NotRequired[str]
        include_scheduled_overrides: NotRequired[bool]

    class SetSubscriptionEntitlementAvailabilityParams(TypedDict):
        is_enabled: Required[bool]
        subscription_entitlements: Required[
            List[
                "SubscriptionEntitlement.SetSubscriptionEntitlementAvailabilitySubscriptionEntitlementParams"
            ]
        ]

    def subscription_entitlements_for_subscription(
        self,
        id,
        params: SubscriptionEntitlementsForSubscriptionParams = None,
        headers=None,
    ) -> SubscriptionEntitlementsForSubscriptionResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "subscription_entitlements"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            SubscriptionEntitlementsForSubscriptionResponse,
            None,
            False,
            jsonKeys,
        )

    def set_subscription_entitlement_availability(
        self, id, params: SetSubscriptionEntitlementAvailabilityParams, headers=None
    ) -> SetSubscriptionEntitlementAvailabilityResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path(
                "subscriptions", id, "subscription_entitlements/set_availability"
            ),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            SetSubscriptionEntitlementAvailabilityResponse,
            None,
            False,
            jsonKeys,
        )
