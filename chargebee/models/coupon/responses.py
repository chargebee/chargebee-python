from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class ItemConstraintResponse(Model):
    item_type: str = None
    constraint: str = None
    item_price_ids: List[Dict[Any, Any]] = None


@dataclass
class ItemConstraintCriteriaResponse(Model):
    item_type: str = None
    currencies: List[Dict[Any, Any]] = None
    item_family_ids: List[Dict[Any, Any]] = None
    item_price_periods: List[Dict[Any, Any]] = None


@dataclass
class CouponConstraintResponse(Model):
    entity_type: str = None
    type: str = None
    value: str = None


@dataclass
class CouponResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    invoice_name: str = None
    discount_type: str = None
    discount_percentage: float = None
    discount_amount: int = None
    discount_quantity: int = None
    currency_code: str = None
    duration_type: str = None
    duration_month: int = None
    valid_till: int = None
    max_redemptions: int = None
    status: str = None
    apply_discount_on: str = None
    apply_on: str = None
    plan_constraint: str = None
    addon_constraint: str = None
    created_at: int = None
    archived_at: int = None
    resource_version: int = None
    updated_at: int = None
    included_in_mrr: bool = None
    period: int = None
    period_unit: str = None
    plan_ids: List[str] = None
    addon_ids: List[str] = None
    item_constraints: List[ItemConstraintResponse] = None
    item_constraint_criteria: List[ItemConstraintCriteriaResponse] = None
    redemptions: int = None
    invoice_notes: str = None
    meta_data: Dict[Any, Any] = None
    coupon_constraints: List[CouponConstraintResponse] = None


@dataclass
class CreateResponse(Response):
    coupon: CouponResponse
    headers: Dict[str, str] = None


@dataclass
class CreateForItemsResponse(Response):
    coupon: CouponResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateForItemsResponse(Response):
    coupon: CouponResponse
    headers: Dict[str, str] = None


@dataclass
class ListCouponResponse:
    coupon: CouponResponse


@dataclass
class ListResponse:
    list: List[ListCouponResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    coupon: CouponResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateResponse(Response):
    coupon: CouponResponse
    headers: Dict[str, str] = None


@dataclass
class DeleteResponse(Response):
    coupon: CouponResponse
    headers: Dict[str, str] = None


@dataclass
class CopyResponse(Response):
    coupon: CouponResponse
    headers: Dict[str, str] = None


@dataclass
class UnarchiveResponse(Response):
    coupon: CouponResponse
    headers: Dict[str, str] = None
