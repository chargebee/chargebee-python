from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class ApplicableItemResponse(Model):
    id: str = None


@dataclass
class BundleItemResponse(Model):
    item_id: str = None
    item_type: str = None
    quantity: int = None
    price_allocation: float = None


@dataclass
class BundleConfigurationResponse(Model):
    type: str = None


@dataclass
class ItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    external_name: str = None
    description: str = None
    status: str = None
    resource_version: int = None
    updated_at: int = None
    item_family_id: str = None
    type: str = None
    is_shippable: bool = None
    is_giftable: bool = None
    redirect_url: str = None
    enabled_for_checkout: bool = None
    enabled_in_portal: bool = None
    included_in_mrr: bool = None
    item_applicability: str = None
    gift_claim_redirect_url: str = None
    unit: str = None
    metered: bool = None
    usage_calculation: str = None
    archived_at: int = None
    channel: str = None
    applicable_items: List[ApplicableItemResponse] = None
    bundle_items: List[BundleItemResponse] = None
    bundle_configuration: BundleConfigurationResponse = None
    metadata: Dict[Any, Any] = None


@dataclass
class CreateResponse(Response):
    item: ItemResponse
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    item: ItemResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateResponse(Response):
    item: ItemResponse
    headers: Dict[str, str] = None


@dataclass
class ListItemResponse:
    item: ItemResponse


@dataclass
class ListResponse:
    list: List[ListItemResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class DeleteResponse(Response):
    item: ItemResponse
    headers: Dict[str, str] = None
