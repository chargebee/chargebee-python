from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class Dispute:
    env: environment.Environment

    class Status(Enum):
        INITIATED = "initiated"
        FUNDS_WITHDRAWN = "funds_withdrawn"
        IN_REVIEW = "in_review"
        CANCELLED = "cancelled"
        LOST = "lost"
        WON = "won"

        def __str__(self):
            return self.value

    class Type(Enum):
        CHARGEBACK = "chargeback"
        INQUIRY = "inquiry"

        def __str__(self):
            return self.value

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]
        type: NotRequired[Filters.EnumFilter]
        customer_id: NotRequired[Filters.StringFilter]
        transaction_id: NotRequired[Filters.StringFilter]
        amount: NotRequired[Filters.NumberFilter]
        created_at: NotRequired[Filters.TimestampFilter]

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("disputes", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="dispute",
            operation="retrieve",
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("disputes"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="dispute",
            operation="list",
        )
