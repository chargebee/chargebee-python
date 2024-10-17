from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.filters import Filters
from chargebee.models import enums


@dataclass
class Usage:

    env: environment.Environment

    class PdfInvoiceParams(TypedDict):
        id: Required[str]

    class CreateParams(TypedDict):
        id: NotRequired[str]
        item_price_id: Required[str]
        quantity: Required[str]
        usage_date: Required[int]
        dedupe_option: NotRequired[enums.DedupeOption]
        note: NotRequired[str]

    class RetrieveParams(TypedDict):
        id: Required[str]

    class DeleteParams(TypedDict):
        id: Required[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        subscription_id: NotRequired[Filters.StringFilter]
        usage_date: NotRequired[Filters.TimestampFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        item_price_id: NotRequired[Filters.StringFilter]
        invoice_id: NotRequired[Filters.StringFilter]
        source: NotRequired[Filters.EnumFilter]
        sort_by: NotRequired[Filters.SortFilter]

    class PdfParams(TypedDict):
        invoice: Required["Usage.PdfInvoiceParams"]
        disposition_type: NotRequired[enums.DispositionType]

    def create(self, id, params: CreateParams, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "usages"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
        )

    def retrieve(self, id, params: RetrieveParams, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "usages"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveResponse,
        )

    def delete(self, id, params: DeleteParams, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "delete_usage"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeleteResponse,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("usages"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
        )

    def pdf(self, params: PdfParams, headers=None) -> PdfResponse:
        return request.send(
            "post",
            request.uri_path("usages", "pdf"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PdfResponse,
        )
