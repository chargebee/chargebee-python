from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.filters import Filters


@dataclass
class GatewayWebhookLog:
    env: environment.Environment

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        webhook_id: NotRequired[Filters.StringFilter]
        gateway: NotRequired[Filters.StringFilter]
        status_code: NotRequired[Filters.StringFilter]
        method: NotRequired[Filters.StringFilter]
        url: NotRequired[Filters.StringFilter]
        id_at_gateway: NotRequired[Filters.StringFilter]
        customer_handle: NotRequired[Filters.StringFilter]
        invoice_handle: NotRequired[Filters.StringFilter]
        transaction_handle: NotRequired[Filters.StringFilter]
        payment_method_handle: NotRequired[Filters.StringFilter]
        gateway_credential_handle: NotRequired[Filters.StringFilter]
        payment_attempt_handle: NotRequired[Filters.StringFilter]
        payment_intent_handle: NotRequired[Filters.StringFilter]
        received_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("gateway_webhook_logs"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="gatewayWebhookLog",
            operation="list",
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("gateway_webhook_logs", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="gatewayWebhookLog",
            operation="retrieve",
        )
