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
    is_idempotency_replayed: bool
    coupon_set: CouponSetResponse


@dataclass
class AddCouponCodesResponse(Response):
    is_idempotency_replayed: bool
    coupon_set: CouponSetResponse


@dataclass
class ListCouponSetResponse:
    coupon_set: CouponSetResponse


@dataclass
class ListResponse(Response):

    list: List[ListCouponSetResponse]
    next_offset: str = None


@dataclass
class RetrieveResponse(Response):

    coupon_set: CouponSetResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    coupon_set: CouponSetResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    coupon_set: CouponSetResponse


@dataclass
class DeleteUnusedCouponCodesResponse(Response):
    is_idempotency_replayed: bool
    coupon_set: CouponSetResponse
