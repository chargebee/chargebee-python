from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.models import enums


class EntitlementOverride:

    class AddEntitlementOverrideForSubscriptionParams(TypedDict):
        action: NotRequired[enums.Action]
        entitlement_overrides: Required[
            List[AddEntitlementOverrideForSubscriptionEntitlementOverrideParams]
        ]

    class ListEntitlementOverrideForSubscriptionParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        embed: NotRequired[str]
        include_drafts: NotRequired[bool]
        include_scheduled_overrides: NotRequired[bool]

    @staticmethod
    def add_entitlement_override_for_subscription(
        id, params: AddEntitlementOverrideForSubscriptionParams, env=None, headers=None
    ) -> AddEntitlementOverrideForSubscriptionResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "entitlement_overrides"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AddEntitlementOverrideForSubscriptionResponse,
        )

    @staticmethod
    def list_entitlement_override_for_subscription(
        id,
        params: ListEntitlementOverrideForSubscriptionParams = None,
        env=None,
        headers=None,
    ) -> ListEntitlementOverrideForSubscriptionResponse:
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "entitlement_overrides"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListEntitlementOverrideForSubscriptionResponse,
        )
