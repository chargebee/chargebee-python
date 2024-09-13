from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class Ramp:

    class CreateForSubscriptionParams(TypedDict):
        effective_from: Required[int]
        description: NotRequired[str]
        coupons_to_remove: NotRequired[List[str]]
        discounts_to_remove: NotRequired[List[str]]
        items_to_remove: NotRequired[List[str]]
        items_to_add: Required[List[CreateForSubscriptionItemsToAddParams]]
        items_to_update: Required[List[CreateForSubscriptionItemsToUpdateParams]]
        item_tiers: NotRequired[List[CreateForSubscriptionItemTierParams]]
        coupons_to_add: NotRequired[List[CreateForSubscriptionCouponsToAddParams]]
        discounts_to_add: Required[List[CreateForSubscriptionDiscountsToAddParams]]

    class UpdateParams(TypedDict):
        effective_from: Required[int]
        description: NotRequired[str]
        coupons_to_remove: NotRequired[List[str]]
        discounts_to_remove: NotRequired[List[str]]
        items_to_remove: NotRequired[List[str]]
        items_to_add: Required[List[UpdateItemsToAddParams]]
        items_to_update: Required[List[UpdateItemsToUpdateParams]]
        item_tiers: NotRequired[List[UpdateItemTierParams]]
        coupons_to_add: NotRequired[List[UpdateCouponsToAddParams]]
        discounts_to_add: Required[List[UpdateDiscountsToAddParams]]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        include_deleted: NotRequired[bool]
        status: NotRequired[Filters.EnumFilter]
        subscription_id: Required[Filters.StringFilter]
        effective_from: NotRequired[Filters.TimestampFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]

    @staticmethod
    def create_for_subscription(
        id, params: CreateForSubscriptionParams, env=None, headers=None
    ) -> CreateForSubscriptionResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "create_ramp"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateForSubscriptionResponse,
        )

    @staticmethod
    def update(id, params: UpdateParams, env=None, headers=None) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("ramps", id, "update"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get", request.uri_path("ramps", id), None, env, headers, RetrieveResponse
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("ramps", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def list(params: ListParams, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("ramps"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )
