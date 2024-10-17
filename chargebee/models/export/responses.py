from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


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
    headers: Dict[str, str] = None


@dataclass
class RevenueRecognitionResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class DeferredRevenueResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class PlansResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class AddonsResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class CouponsResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class CustomersResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class SubscriptionsResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class InvoicesResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class CreditNotesResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class TransactionsResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class OrdersResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class ItemFamiliesResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class ItemsResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class ItemPricesResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class AttachedItemsResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class DifferentialPricesResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None


@dataclass
class PriceVariantsResponse(Response):
    export: ExportResponse
    headers: Dict[str, str] = None
