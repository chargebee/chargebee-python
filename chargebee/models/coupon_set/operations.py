from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.filters import Filters


class CouponSet:

    class CreateParams(TypedDict):
        coupon_id: Required[str]
        name: Required[str]
        id: Required[str]
        meta_data: NotRequired[Dict[Any, Any]]

    class AddCouponCodesParams(TypedDict):
        code: NotRequired[List[str]]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        name: NotRequired[Filters.StringFilter]
        coupon_id: NotRequired[Filters.StringFilter]
        total_count: NotRequired[Filters.NumberFilter]
        redeemed_count: NotRequired[Filters.NumberFilter]
        archived_count: NotRequired[Filters.NumberFilter]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("coupon_sets"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def add_coupon_codes(
        id, params: AddCouponCodesParams = None, env=None, headers=None
    ) -> AddCouponCodesResponse:
        return request.send(
            "post",
            request.uri_path("coupon_sets", id, "add_coupon_codes"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AddCouponCodesResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("coupon_sets"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("coupon_sets", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def update(
        id, params: UpdateParams = None, env=None, headers=None
    ) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("coupon_sets", id, "update"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("coupon_sets", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def delete_unused_coupon_codes(
        id, env=None, headers=None
    ) -> DeleteUnusedCouponCodesResponse:
        return request.send(
            "post",
            request.uri_path("coupon_sets", id, "delete_unused_coupon_codes"),
            None,
            env,
            headers,
            DeleteUnusedCouponCodesResponse,
        )
