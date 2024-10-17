from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import item


@dataclass
class TierResponse(Model):
    starting_unit: int = None
    ending_unit: int = None
    price: int = None
    starting_unit_in_decimal: str = None
    ending_unit_in_decimal: str = None
    price_in_decimal: str = None


@dataclass
class TaxDetailResponse(Model):
    tax_profile_id: str = None
    avalara_sale_type: str = None
    avalara_transaction_type: int = None
    avalara_service_type: int = None
    avalara_tax_code: str = None
    hsn_code: str = None
    taxjar_product_code: str = None


@dataclass
class TaxProvidersFieldResponse(Model):
    provider_name: str = None
    field_id: str = None
    field_value: str = None


@dataclass
class AccountingDetailResponse(Model):
    sku: str = None
    accounting_code: str = None
    accounting_category1: str = None
    accounting_category2: str = None
    accounting_category3: str = None
    accounting_category4: str = None


@dataclass
class ItemPriceResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    item_family_id: str = None
    item_id: str = None
    description: str = None
    status: str = None
    external_name: str = None
    price_variant_id: str = None
    proration_type: str = None
    pricing_model: str = None
    price: int = None
    price_in_decimal: str = None
    period: int = None
    currency_code: str = None
    period_unit: str = None
    trial_period: int = None
    trial_period_unit: str = None
    trial_end_action: str = None
    shipping_period: int = None
    shipping_period_unit: str = None
    billing_cycles: int = None
    free_quantity: int = None
    free_quantity_in_decimal: str = None
    channel: str = None
    resource_version: int = None
    updated_at: int = None
    created_at: int = None
    usage_accumulation_reset_frequency: str = None
    archived_at: int = None
    invoice_notes: str = None
    tiers: List[TierResponse] = None
    is_taxable: bool = None
    tax_detail: TaxDetailResponse = None
    tax_providers_fields: List[TaxProvidersFieldResponse] = None
    accounting_detail: AccountingDetailResponse = None
    metadata: Dict[Any, Any] = None
    item_type: str = None
    archivable: bool = None
    parent_item_id: str = None
    show_description_in_invoices: bool = None
    show_description_in_quotes: bool = None


@dataclass
class CreateResponse(Response):
    item_price: ItemPriceResponse
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    item_price: ItemPriceResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateResponse(Response):
    item_price: ItemPriceResponse
    headers: Dict[str, str] = None


@dataclass
class ListItemPriceResponse:
    item_price: ItemPriceResponse


@dataclass
class ListResponse:
    list: List[ListItemPriceResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class DeleteResponse(Response):
    item_price: ItemPriceResponse
    headers: Dict[str, str] = None


@dataclass
class FindApplicableItemsItemPriceResponse:
    item: "item.ItemResponse"


@dataclass
class FindApplicableItemsResponse:
    list: List[FindApplicableItemsItemPriceResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class FindApplicableItemPricesItemPriceResponse:
    item_price: ItemPriceResponse


@dataclass
class FindApplicableItemPricesResponse:
    list: List[FindApplicableItemPricesItemPriceResponse]
    next_offset: str = None
    headers: Dict[str, str] = None
