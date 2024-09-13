from typing import TypedDict, Required, NotRequired, Dict, List, Any


class CouponSets(TypedDict):
    id: Required[str]
    coupon_id: Required[str]
    name: Required[str]
    total_count: NotRequired[int]
    redeemed_count: NotRequired[int]
    archived_count: NotRequired[int]
    meta_data: NotRequired[Dict[Any, Any]]
