from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class CouponCode:

    class CreateParams(TypedDict):
        coupon_id: Required[str]
        coupon_set_name: Required[str]
        code: Required[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        code: NotRequired[Filters.StringFilter]
        coupon_id: NotRequired[Filters.StringFilter]
        coupon_set_name: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("coupon_codes"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("coupon_codes", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("coupon_codes"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def archive(id, env=None, headers=None) -> ArchiveResponse:
        return request.send(
            "post",
            request.uri_path("coupon_codes", id, "archive"),
            None,
            env,
            headers,
            ArchiveResponse,
        )
