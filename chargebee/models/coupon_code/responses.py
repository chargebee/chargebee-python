from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class CouponCodeResponse(Model):
    raw_data: Dict[Any, Any] = None
    code: str = None
    status: str = None
    coupon_id: str = None
    coupon_set_id: str = None
    coupon_set_name: str = None


@dataclass
class CreateResponse:
    coupon_code: CouponCodeResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveResponse:
    coupon_code: CouponCodeResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ListCouponCodeResponse:
    coupon_code: CouponCodeResponse


@dataclass
class ListResponse:
    list: List[ListCouponCodeResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None


@dataclass
class ArchiveResponse:
    coupon_code: CouponCodeResponse
    response_headers: Dict[Any, Any] = None
