from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class CouponResponse(Model):
    raw_data: Dict[Any, Any] = None
    coupon_id: str = None


@dataclass
class SubscriptionItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    item_price_id: str = None
    item_type: str = None
    quantity: int = None
    quantity_in_decimal: str = None
    metered_quantity: str = None
    last_calculated_at: int = None
    unit_price: int = None
    unit_price_in_decimal: str = None
    amount: int = None
    current_term_start: int = None
    current_term_end: int = None
    next_billing_at: int = None
    amount_in_decimal: str = None
    billing_period: int = None
    billing_period_unit: str = None
    free_quantity: int = None
    free_quantity_in_decimal: str = None
    trial_end: int = None
    billing_cycles: int = None
    service_period_days: int = None
    charge_on_event: str = None
    charge_once: bool = None
    charge_on_option: str = None
    proration_type: str = None
    usage_accumulation_reset_frequency: str = None


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
    pricing_type: str = None
    package_size: int = None
    index: int = None


@dataclass
class QuotedContractTermResponse(Model):
    raw_data: Dict[Any, Any] = None
    contract_start: int = None
    contract_end: int = None
    billing_cycle: int = None
    action_at_term_end: str = None
    total_contract_value: int = None
    cancellation_cutoff_period: int = None


@dataclass
class EventBasedAddonResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    quantity: int = None
    unit_price: int = None
    service_period_in_days: int = None
    on_event: str = None
    charge_once: bool = None
    quantity_in_decimal: str = None
    unit_price_in_decimal: str = None


@dataclass
class AddonResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    quantity: int = None
    unit_price: int = None
    amount: int = None
    trial_end: int = None
    remaining_billing_cycles: int = None
    quantity_in_decimal: str = None
    unit_price_in_decimal: str = None
    amount_in_decimal: str = None
    proration_type: str = None


@dataclass
class QuotedSubscriptionResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    plan_id: str = None
    plan_quantity: int = None
    plan_unit_price: int = None
    setup_fee: int = None
    billing_period: int = None
    billing_period_unit: str = None
    start_date: int = None
    trial_end: int = None
    remaining_billing_cycles: int = None
    po_number: str = None
    auto_collection: str = None
    plan_quantity_in_decimal: str = None
    plan_unit_price_in_decimal: str = None
    changes_scheduled_at: int = None
    change_option: str = None
    contract_term_billing_cycle_on_renewal: int = None
    addons: List[AddonResponse] = None
    event_based_addons: List[EventBasedAddonResponse] = None
    coupons: List[CouponResponse] = None
    subscription_items: List[SubscriptionItemResponse] = None
    item_tiers: List[ItemTierResponse] = None
    quoted_contract_term: QuotedContractTermResponse = None
