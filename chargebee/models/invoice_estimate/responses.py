from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class LineItemResponse(Model):
    id: str = None
    subscription_id: str = None
    date_from: int = None
    date_to: int = None
    unit_amount: int = None
    quantity: int = None
    amount: int = None
    pricing_model: str = None
    is_taxed: bool = None
    tax_amount: int = None
    tax_rate: float = None
    unit_amount_in_decimal: str = None
    quantity_in_decimal: str = None
    amount_in_decimal: str = None
    discount_amount: int = None
    item_level_discount_amount: int = None
    usage_percentage: str = None
    reference_line_item_id: str = None
    description: str = None
    entity_description: str = None
    entity_type: str = None
    tax_exempt_reason: str = None
    entity_id: str = None
    customer_id: str = None


@dataclass
class DiscountResponse(Model):
    amount: int = None
    description: str = None
    entity_type: str = None
    entity_id: str = None
    coupon_set_code: str = None


@dataclass
class TaxResponse(Model):
    name: str = None
    amount: int = None
    description: str = None


@dataclass
class LineItemTaxResponse(Model):
    line_item_id: str = None
    tax_name: str = None
    tax_rate: float = None
    date_to: int = None
    date_from: int = None
    prorated_taxable_amount: float = None
    is_partial_tax_applied: bool = None
    is_non_compliance_tax: bool = None
    taxable_amount: int = None
    tax_amount: int = None
    tax_juris_type: str = None
    tax_juris_name: str = None
    tax_juris_code: str = None
    tax_amount_in_local_currency: int = None
    local_currency_code: str = None


@dataclass
class LineItemTierResponse(Model):
    line_item_id: str = None
    starting_unit: int = None
    ending_unit: int = None
    quantity_used: int = None
    unit_amount: int = None
    starting_unit_in_decimal: str = None
    ending_unit_in_decimal: str = None
    quantity_used_in_decimal: str = None
    unit_amount_in_decimal: str = None


@dataclass
class LineItemDiscountResponse(Model):
    line_item_id: str = None
    discount_type: str = None
    coupon_id: str = None
    entity_id: str = None
    discount_amount: int = None


@dataclass
class InvoiceEstimateResponse(Model):
    raw_data: Dict[Any, Any] = None
    recurring: bool = None
    price_type: str = None
    currency_code: str = None
    sub_total: int = None
    total: int = None
    credits_applied: int = None
    amount_paid: int = None
    amount_due: int = None
    line_items: List[LineItemResponse] = None
    discounts: List[DiscountResponse] = None
    taxes: List[TaxResponse] = None
    line_item_taxes: List[LineItemTaxResponse] = None
    line_item_tiers: List[LineItemTierResponse] = None
    line_item_discounts: List[LineItemDiscountResponse] = None
    round_off_amount: int = None
    customer_id: str = None
