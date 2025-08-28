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
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "usages"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve(self, id, params: RetrieveParams, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "usages"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def delete(self, id, params: DeleteParams, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "delete_usage"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("usages"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def pdf(self, params: PdfParams, headers=None) -> PdfResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("usages", "pdf"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PdfResponse,
            None,
            False,
            jsonKeys,
            options,
        )
