from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class TierResponse(Model):
    raw_data: Dict[Any, Any] = None
    starting_unit: int = None
    ending_unit: int = None
    price: int = None
    starting_unit_in_decimal: str = None
    ending_unit_in_decimal: str = None
    price_in_decimal: str = None
    pricing_type: str = None
    package_size: int = None


@dataclass
class TaxProvidersFieldResponse(Model):
    raw_data: Dict[Any, Any] = None
    provider_name: str = None
    field_id: str = None
    field_value: str = None


@dataclass
class ApplicableAddonResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None


@dataclass
class AttachedAddonResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    quantity: int = None
    billing_cycles: int = None
    type: str = None
    quantity_in_decimal: str = None


@dataclass
class EventBasedAddonResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    quantity: int = None
    on_event: str = None
    charge_once: bool = None
    quantity_in_decimal: str = None


@dataclass
class PlanResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    invoice_name: str = None
    description: str = None
    price: int = None
    currency_code: str = None
    period: int = None
    period_unit: str = None
    trial_period: int = None
    trial_period_unit: str = None
    trial_end_action: str = None
    pricing_model: str = None
    charge_model: str = None
    free_quantity: int = None
    setup_cost: int = None
    downgrade_penalty: float = None
    status: str = None
    archived_at: int = None
    billing_cycles: int = None
    redirect_url: str = None
    enabled_in_hosted_pages: bool = None
    enabled_in_portal: bool = None
    addon_applicability: str = None
    tax_code: str = None
    hsn_code: str = None
    taxjar_product_code: str = None
    avalara_sale_type: str = None
    avalara_transaction_type: int = None
    avalara_service_type: int = None
    sku: str = None
    accounting_code: str = None
    accounting_category1: str = None
    accounting_category2: str = None
    accounting_category3: str = None
    accounting_category4: str = None
    is_shippable: bool = None
    shipping_frequency_period: int = None
    shipping_frequency_period_unit: str = None
    resource_version: int = None
    updated_at: int = None
    giftable: bool = None
    claim_url: str = None
    free_quantity_in_decimal: str = None
    price_in_decimal: str = None
    channel: str = None
    invoice_notes: str = None
    taxable: bool = None
    tax_profile_id: str = None
    meta_data: Dict[Any, Any] = None
    tiers: List[TierResponse] = None
    tax_providers_fields: List[TaxProvidersFieldResponse] = None
    applicable_addons: List[ApplicableAddonResponse] = None
    attached_addons: List[AttachedAddonResponse] = None
    event_based_addons: List[EventBasedAddonResponse] = None
    show_description_in_invoices: bool = None
    show_description_in_quotes: bool = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    plan: PlanResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    plan: PlanResponse


@dataclass
class ListPlanResponse:
    plan: PlanResponse


@dataclass
class ListResponse(Response):

    list: List[ListPlanResponse]
    next_offset: str = None


@dataclass
class RetrieveResponse(Response):

    plan: PlanResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    plan: PlanResponse


@dataclass
class CopyResponse(Response):
    is_idempotency_replayed: bool
    plan: PlanResponse


@dataclass
class UnarchiveResponse(Response):
    is_idempotency_replayed: bool
    plan: PlanResponse
