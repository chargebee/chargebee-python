from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class ItemsToAddResponse(Model):
    raw_data: Dict[Any, Any] = None
    item_price_id: str = None
    item_type: str = None
    quantity: int = None
    quantity_in_decimal: str = None
    unit_price: int = None
    unit_price_in_decimal: str = None
    amount: int = None
    amount_in_decimal: str = None
    free_quantity: int = None
    free_quantity_in_decimal: str = None
    billing_cycles: int = None
    service_period_days: int = None
    metered_quantity: str = None
    charge_once: bool = None
    charge_on_option: str = None
    charge_on_event: str = None


@dataclass
class ItemsToUpdateResponse(Model):
    raw_data: Dict[Any, Any] = None
    item_price_id: str = None
    item_type: str = None
    quantity: int = None
    quantity_in_decimal: str = None
    unit_price: int = None
    unit_price_in_decimal: str = None
    amount: int = None
    amount_in_decimal: str = None
    free_quantity: int = None
    free_quantity_in_decimal: str = None
    billing_cycles: int = None
    service_period_days: int = None
    metered_quantity: str = None
    charge_once: bool = None
    charge_on_option: str = None
    charge_on_event: str = None


@dataclass
class CouponsToAddResponse(Model):
    raw_data: Dict[Any, Any] = None
    coupon_id: str = None
    apply_till: int = None


@dataclass
class DiscountsToAddResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    invoice_name: str = None
    type: str = None
    percentage: float = None
    amount: int = None
    duration_type: str = None
    period: int = None
    period_unit: str = None
    included_in_mrr: bool = None
    apply_on: str = None
    item_price_id: str = None
    created_at: int = None


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
class ContractTermResponse(Model):
    raw_data: Dict[Any, Any] = None
    cancellation_cutoff_period: int = None
    renewal_billing_cycles: int = None
    action_at_term_end: str = None


@dataclass
class StatusTransitionReasonResponse(Model):
    raw_data: Dict[Any, Any] = None
    code: str = None
    message: str = None


@dataclass
class RampResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    description: str = None
    subscription_id: str = None
    effective_from: int = None
    status: str = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None
    items_to_add: List[ItemsToAddResponse] = None
    items_to_update: List[ItemsToUpdateResponse] = None
    coupons_to_add: List[CouponsToAddResponse] = None
    discounts_to_add: List[DiscountsToAddResponse] = None
    item_tiers: List[ItemTierResponse] = None
    items_to_remove: List[str] = None
    coupons_to_remove: List[str] = None
    discounts_to_remove: List[str] = None
    contract_term: ContractTermResponse = None
    deleted: bool = None
    status_transition_reason: StatusTransitionReasonResponse = None


@dataclass
class CreateForSubscriptionResponse(Response):
    is_idempotency_replayed: bool
    ramp: RampResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    ramp: RampResponse


@dataclass
class RetrieveResponse(Response):
    ramp: RampResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    ramp: RampResponse


@dataclass
class ListRampResponse:
    ramp: RampResponse


@dataclass
class ListResponse(Response):
    list: List[ListRampResponse]
    next_offset: str = None
