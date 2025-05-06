from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class DownloadResponse(Model):
    raw_data: Dict[Any, Any] = None
    download_url: str = None
    valid_till: int = None
    mime_type: str = None


@dataclass
class ExportResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    operation_type: str = None
    mime_type: str = None
    status: str = None
    created_at: int = None
    download: DownloadResponse = None


@dataclass
class RetrieveResponse(Response):

    export: ExportResponse


@dataclass
class RevenueRecognitionResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class DeferredRevenueResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class PlansResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class AddonsResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class CouponsResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class CustomersResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class SubscriptionsResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class InvoicesResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class CreditNotesResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class TransactionsResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class OrdersResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class ItemFamiliesResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class ItemsResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class ItemPricesResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class AttachedItemsResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class DifferentialPricesResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse


@dataclass
class PriceVariantsResponse(Response):
    is_idempotency_replayed: bool
    export: ExportResponse
