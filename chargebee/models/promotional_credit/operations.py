from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


class PromotionalCredit:
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

    @staticmethod
    def add(params: AddParams, env=None, headers=None) -> AddResponse:
        return request.send(
            "post",
            request.uri_path("promotional_credits", "add"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AddResponse,
        )

    @staticmethod
    def deduct(params: DeductParams, env=None, headers=None) -> DeductResponse:
        return request.send(
            "post",
            request.uri_path("promotional_credits", "deduct"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            DeductResponse,
        )

    @staticmethod
    def set(params: SetParams, env=None, headers=None) -> SetResponse:
        return request.send(
            "post",
            request.uri_path("promotional_credits", "set"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            SetResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("promotional_credits"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("promotional_credits", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )
