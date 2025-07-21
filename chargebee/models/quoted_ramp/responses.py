from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class LineItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    item_price_id: str = None
    item_type: str = None
    quantity: int = None
    quantity_in_decimal: str = None
    metered_quantity: str = None
    unit_price: int = None
    unit_price_in_decimal: str = None
    amount: int = None
    amount_in_decimal: str = None
    billing_period: int = None
    billing_period_unit: str = None
    free_quantity: int = None
    free_quantity_in_decimal: str = None
    billing_cycles: int = None
    service_period_days: int = None
    charge_on_event: str = None
    charge_once: bool = None
    charge_on_option: str = None
    start_date: int = None
    end_date: int = None
    ramp_tier_id: str = None
    discount_per_billing_cycle: int = None
    discount_per_billing_cycle_in_decimal: str = None
    item_level_discount_per_billing_cycle: int = None
    item_level_discount_per_billing_cycle_in_decimal: str = None
    amount_per_billing_cycle: int = None
    amount_per_billing_cycle_in_decimal: str = None
    net_amount_per_billing_cycle: int = None
    net_amount_per_billing_cycle_in_decimal: str = None


@dataclass
class DiscountResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    invoice_name: str = None
    type: str = None
    percentage: float = None
    amount: int = None
    duration_type: str = None
    entity_type: str = None
    entity_id: str = None
    period: int = None
    period_unit: str = None
    included_in_mrr: bool = None
    apply_on: str = None
    item_price_id: str = None
    created_at: int = None
    updated_at: int = None
    start_date: int = None
    end_date: int = None


@dataclass
class ItemTierResponse(Model):
    raw_data: Dict[Any, Any] = None
    item_price_id: str = None
    starting_unit: int = None
    ending_unit: int = None
    price: int = None
    starting_unit_in_decimal: str = None
    ending_unit_in_decimal: str = None
    price_in_decimal: str = None
    ramp_tier_id: str = None
    pricing_type: str = None
    package_size: int = None


@dataclass
class CouponApplicabilityMappingResponse(Model):
    raw_data: Dict[Any, Any] = None
    coupon_id: str = None
    applicable_item_price_ids: List[str] = None


@dataclass
class QuotedRampResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    line_items: List[LineItemResponse] = None
    discounts: List[DiscountResponse] = None
    item_tiers: List[ItemTierResponse] = None
    coupon_applicability_mappings: List[CouponApplicabilityMappingResponse] = None
