from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class ShippingAddressResponse(Model):
    raw_data: Dict[Any, Any] = None
    first_name: str = None
    last_name: str = None
    email: str = None
    company: str = None
    phone: str = None
    line1: str = None
    line2: str = None
    line3: str = None
    city: str = None
    state_code: str = None
    state: str = None
    country: str = None
    zip: str = None
    validation_status: str = None
    index: int = None


@dataclass
class ContractTermResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    status: str = None
    contract_start: int = None
    contract_end: int = None
    billing_cycle: int = None
    action_at_term_end: str = None
    total_contract_value: int = None
    total_contract_value_before_tax: int = None
    cancellation_cutoff_period: int = None
    created_at: int = None
    subscription_id: str = None
    remaining_billing_cycles: int = None


@dataclass
class SubscriptionEstimateResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    currency_code: str = None
    status: str = None
    trial_end_action: str = None
    next_billing_at: int = None
    pause_date: int = None
    resume_date: int = None
    shipping_address: ShippingAddressResponse = None
    contract_term: ContractTermResponse = None
