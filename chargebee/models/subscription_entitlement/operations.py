from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import entitlement_override


class SubscriptionEntitlement:
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

    @staticmethod
    def subscription_entitlements_for_subscription(
        id,
        params: SubscriptionEntitlementsForSubscriptionParams = None,
        env=None,
        headers=None,
    ) -> SubscriptionEntitlementsForSubscriptionResponse:
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "subscription_entitlements"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            SubscriptionEntitlementsForSubscriptionResponse,
        )

    @staticmethod
    def set_subscription_entitlement_availability(
        id, params: SetSubscriptionEntitlementAvailabilityParams, env=None, headers=None
    ) -> SetSubscriptionEntitlementAvailabilityResponse:
        return request.send(
            "post",
            request.uri_path(
                "subscriptions", id, "subscription_entitlements/set_availability"
            ),
            cast(Dict[Any, Any], params),
            env,
            headers,
            SetSubscriptionEntitlementAvailabilityResponse,
        )
