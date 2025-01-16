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
    coupon_code: CouponCodeResponse
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    coupon_code: CouponCodeResponse
    headers: Dict[str, str] = None


@dataclass
class ListCouponCodeResponse:
    coupon_code: CouponCodeResponse


@dataclass
class ListResponse:
    list: List[ListCouponCodeResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class ArchiveResponse(Response):
    coupon_code: CouponCodeResponse
    headers: Dict[str, str] = None
