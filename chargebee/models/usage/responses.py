from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
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
class CreateResponse(Response):
    is_idempotency_replayed: bool
    usage: UsageResponse


@dataclass
class RetrieveResponse(Response):
    usage: UsageResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    usage: UsageResponse


@dataclass
class ListUsageResponse:
    usage: UsageResponse


@dataclass
class ListResponse(Response):
    list: List[ListUsageResponse]
    next_offset: str = None


@dataclass
class PdfResponse(Response):
    is_idempotency_replayed: bool
    download: "download.DownloadResponse"
