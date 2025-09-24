from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class CouponCodeResponse(Model):
    raw_data: Dict[Any, Any] = None
    code: str = None
    status: str = None
    coupon_id: str = None
    coupon_set_id: str = None
    coupon_set_name: str = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    coupon_code: CouponCodeResponse


@dataclass
class RetrieveResponse(Response):

    coupon_code: CouponCodeResponse


@dataclass
class ListCouponCodeResponse:
    coupon_code: CouponCodeResponse


@dataclass
class ListResponse(Response):

    list: List[ListCouponCodeResponse]
    next_offset: str = None


@dataclass
class ArchiveResponse(Response):
    is_idempotency_replayed: bool
    coupon_code: CouponCodeResponse
