from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class CouponSetResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    coupon_id: str = None
    name: str = None
    total_count: int = None
    redeemed_count: int = None
    archived_count: int = None
    meta_data: Dict[Any, Any] = None


@dataclass
class CreateResponse:
    coupon_set: CouponSetResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class AddCouponCodesResponse:
    coupon_set: CouponSetResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ListCouponSetResponse:
    coupon_set: CouponSetResponse


@dataclass
class ListResponse:
    list: List[ListCouponSetResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveResponse:
    coupon_set: CouponSetResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class UpdateResponse:
    coupon_set: CouponSetResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class DeleteResponse:
    coupon_set: CouponSetResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class DeleteUnusedCouponCodesResponse:
    coupon_set: CouponSetResponse
    response_headers: Dict[Any, Any] = None
