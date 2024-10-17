from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


@dataclass
class PromotionalCredit:

    env: environment.Environment

    class Type(Enum):
        INCREMENT = "increment"
        DECREMENT = "decrement"

        def __str__(self):
            return self.value

    class AddParams(TypedDict):
        customer_id: Required[str]
        amount: NotRequired[int]
        amount_in_decimal: NotRequired[str]
        currency_code: NotRequired[str]
        description: Required[str]
        credit_type: NotRequired[enums.CreditType]
        reference: NotRequired[str]

    class DeductParams(TypedDict):
        customer_id: Required[str]
        amount: NotRequired[int]
        amount_in_decimal: NotRequired[str]
        currency_code: NotRequired[str]
        description: Required[str]
        credit_type: NotRequired[enums.CreditType]
        reference: NotRequired[str]

    class SetParams(TypedDict):
        customer_id: Required[str]
        amount: NotRequired[int]
        amount_in_decimal: NotRequired[str]
        currency_code: NotRequired[str]
        description: Required[str]
        credit_type: NotRequired[enums.CreditType]
        reference: NotRequired[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        type: NotRequired[Filters.EnumFilter]
        customer_id: NotRequired[Filters.StringFilter]

    def add(self, params: AddParams, headers=None) -> AddResponse:
        return request.send(
            "post",
            request.uri_path("promotional_credits", "add"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AddResponse,
        )

    def deduct(self, params: DeductParams, headers=None) -> DeductResponse:
        return request.send(
            "post",
            request.uri_path("promotional_credits", "deduct"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeductResponse,
        )

    def set(self, params: SetParams, headers=None) -> SetResponse:
        return request.send(
            "post",
            request.uri_path("promotional_credits", "set"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            SetResponse,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("promotional_credits"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("promotional_credits", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
        )
