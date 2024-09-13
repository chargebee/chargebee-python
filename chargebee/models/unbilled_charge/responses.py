from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.models import estimate, invoice


@dataclass
class TierResponse(Model):
    starting_unit: int = None
    ending_unit: int = None
    quantity_used: int = None
    unit_amount: int = None
    starting_unit_in_decimal: str = None
    ending_unit_in_decimal: str = None
    quantity_used_in_decimal: str = None
    unit_amount_in_decimal: str = None


@dataclass
class UnbilledChargeResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    customer_id: str = None
    subscription_id: str = None
    date_from: int = None
    date_to: int = None
    unit_amount: int = None
    pricing_model: str = None
    quantity: int = None
    amount: int = None
    currency_code: str = None
    discount_amount: int = None
    description: str = None
    entity_type: str = None
    entity_id: str = None
    is_voided: bool = None
    voided_at: int = None
    unit_amount_in_decimal: str = None
    quantity_in_decimal: str = None
    amount_in_decimal: str = None
    updated_at: int = None
    tiers: List[TierResponse] = None
    is_advance_charge: bool = None
    business_entity_id: str = None
    deleted: bool = None


@dataclass
class CreateUnbilledChargeResponse:
    unbilled_charges: List[UnbilledChargeResponse]
    response_headers: Dict[Any, Any] = None


@dataclass
class CreateResponse:
    unbilled_charges: List[UnbilledChargeResponse]
    response_headers: Dict[Any, Any] = None


@dataclass
class InvoiceUnbilledChargesResponse:
    invoices: List["invoice.InvoiceResponse"]
    response_headers: Dict[Any, Any] = None


@dataclass
class DeleteResponse:
    unbilled_charge: UnbilledChargeResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ListUnbilledChargeResponse:
    unbilled_charge: UnbilledChargeResponse


@dataclass
class ListResponse:
    list: List[ListUnbilledChargeResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None


@dataclass
class InvoiceNowEstimateResponse:
    estimate: "estimate.EstimateResponse"
    response_headers: Dict[Any, Any] = None
