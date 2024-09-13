from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class Usage:

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
        invoice: Required[PdfInvoiceParams]
        disposition_type: NotRequired[enums.DispositionType]

    @staticmethod
    def create(id, params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "usages"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def retrieve(
        id, params: RetrieveParams, env=None, headers=None
    ) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "usages"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def delete(id, params: DeleteParams, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "delete_usage"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("usages"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def pdf(params: PdfParams, env=None, headers=None) -> PdfResponse:
        return request.send(
            "post",
            request.uri_path("usages", "pdf"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            PdfResponse,
        )
