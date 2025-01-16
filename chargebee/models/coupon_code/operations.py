from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class CouponCode:

    env: environment.Environment

    class Status(Enum):
        NOT_REDEEMED = "not_redeemed"
        REDEEMED = "redeemed"
        ARCHIVED = "archived"

        def __str__(self):
            return self.value

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

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("coupon_codes"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("coupon_codes", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("coupon_codes"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
        )

    def archive(self, id, headers=None) -> ArchiveResponse:
        return request.send(
            "post",
            request.uri_path("coupon_codes", id, "archive"),
            self.env,
            None,
            headers,
            ArchiveResponse,
        )
