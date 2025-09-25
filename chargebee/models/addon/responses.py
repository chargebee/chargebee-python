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
class AddonResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    invoice_name: str = None
    description: str = None
    pricing_model: str = None
    type: str = None
    charge_type: str = None
    price: int = None
    currency_code: str = None
    period: int = None
    period_unit: str = None
    unit: str = None
    status: str = None
    archived_at: int = None
    enabled_in_portal: bool = None
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
    price_in_decimal: str = None
    included_in_mrr: bool = None
    channel: str = None
    proration_type: str = None
    invoice_notes: str = None
    taxable: bool = None
    tax_profile_id: str = None
    meta_data: Dict[Any, Any] = None
    tiers: List[TierResponse] = None
    tax_providers_fields: List[TaxProvidersFieldResponse] = None
    show_description_in_invoices: bool = None
    show_description_in_quotes: bool = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    addon: AddonResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    addon: AddonResponse


@dataclass
class ListAddonResponse:
    addon: AddonResponse


@dataclass
class ListResponse(Response):
    list: List[ListAddonResponse]
    next_offset: str = None


@dataclass
class RetrieveResponse(Response):
    addon: AddonResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    addon: AddonResponse


@dataclass
class CopyResponse(Response):
    is_idempotency_replayed: bool
    addon: AddonResponse


@dataclass
class UnarchiveResponse(Response):
    is_idempotency_replayed: bool
    addon: AddonResponse
