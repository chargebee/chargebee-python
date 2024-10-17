from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.filters import Filters


@dataclass
class CouponSet:

    env: environment.Environment

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

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("coupon_sets"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
        )

    def add_coupon_codes(
        self, id, params: AddCouponCodesParams = None, headers=None
    ) -> AddCouponCodesResponse:
        return request.send(
            "post",
            request.uri_path("coupon_sets", id, "add_coupon_codes"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AddCouponCodesResponse,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("coupon_sets"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("coupon_sets", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
        )

    def update(self, id, params: UpdateParams = None, headers=None) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("coupon_sets", id, "update"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("coupon_sets", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
        )

    def delete_unused_coupon_codes(
        self, id, headers=None
    ) -> DeleteUnusedCouponCodesResponse:
        return request.send(
            "post",
            request.uri_path("coupon_sets", id, "delete_unused_coupon_codes"),
            self.env,
            None,
            headers,
            DeleteUnusedCouponCodesResponse,
        )
