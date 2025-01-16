from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


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
class CreateResponse(Response):
    coupon_set: CouponSetResponse
    headers: Dict[str, str] = None


@dataclass
class AddCouponCodesResponse(Response):
    coupon_set: CouponSetResponse
    headers: Dict[str, str] = None


@dataclass
class ListCouponSetResponse:
    coupon_set: CouponSetResponse


@dataclass
class ListResponse:
    list: List[ListCouponSetResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    coupon_set: CouponSetResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateResponse(Response):
    coupon_set: CouponSetResponse
    headers: Dict[str, str] = None


@dataclass
class DeleteResponse(Response):
    coupon_set: CouponSetResponse
    headers: Dict[str, str] = None


@dataclass
class DeleteUnusedCouponCodesResponse(Response):
    coupon_set: CouponSetResponse
    headers: Dict[str, str] = None
