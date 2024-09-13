from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class DownloadResponse(Model):
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
class RetrieveResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RevenueRecognitionResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class DeferredRevenueResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class PlansResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class AddonsResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CouponsResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CustomersResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class SubscriptionsResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class InvoicesResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CreditNotesResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class TransactionsResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class OrdersResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ItemFamiliesResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ItemsResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ItemPricesResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class AttachedItemsResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class DifferentialPricesResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class PriceVariantsResponse:
    export: ExportResponse
    response_headers: Dict[Any, Any] = None
