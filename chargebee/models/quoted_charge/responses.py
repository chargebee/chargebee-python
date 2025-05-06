from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class ChargeResponse(Model):
    raw_data: Dict[Any, Any] = None
    amount: int = None
    amount_in_decimal: str = None
    description: str = None
    service_period_in_days: int = None
    avalara_sale_type: str = None
    avalara_transaction_type: int = None
    avalara_service_type: int = None


@dataclass
class InvoiceItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    item_price_id: str = None
    quantity: int = None
    quantity_in_decimal: str = None
    unit_price: int = None
    unit_price_in_decimal: str = None
    service_period_days: int = None


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
class CouponResponse(Model):
    raw_data: Dict[Any, Any] = None
    coupon_id: str = None


@dataclass
class AddonResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    quantity: int = None
    unit_price: int = None
    quantity_in_decimal: str = None
    unit_price_in_decimal: str = None
    proration_type: str = None
    service_period: int = None


@dataclass
class QuotedChargeResponse(Model):
    raw_data: Dict[Any, Any] = None
    charges: List[ChargeResponse] = None
    addons: List[AddonResponse] = None
    invoice_items: List[InvoiceItemResponse] = None
    item_tiers: List[ItemTierResponse] = None
    coupons: List[CouponResponse] = None
