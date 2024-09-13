from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.models import download


@dataclass
class UsageResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    usage_date: int = None
    subscription_id: str = None
    item_price_id: str = None
    invoice_id: str = None
    line_item_id: str = None
    quantity: str = None
    source: str = None
    note: str = None
    resource_version: int = None
    updated_at: int = None
    created_at: int = None


@dataclass
class CreateResponse:
    usage: UsageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveResponse:
    usage: UsageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class DeleteResponse:
    usage: UsageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ListUsageResponse:
    usage: UsageResponse


@dataclass
class ListResponse:
    list: List[ListUsageResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None


@dataclass
class PdfResponse:
    download: "download.DownloadResponse"
    response_headers: Dict[Any, Any] = None
