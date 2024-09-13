from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class DifferentialPrice:

    class CreateParams(TypedDict):
        parent_item_id: Required[str]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]
        parent_periods: Required[List[CreateParentPeriodParams]]
        tiers: NotRequired[List[CreateTierParams]]

    class RetrieveParams(TypedDict):
        item_price_id: Required[str]

    class UpdateParams(TypedDict):
        item_price_id: Required[str]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]
        parent_periods: Required[List[UpdateParentPeriodParams]]
        tiers: NotRequired[List[UpdateTierParams]]

    class DeleteParams(TypedDict):
        item_price_id: Required[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        item_price_id: NotRequired[Filters.StringFilter]
        item_id: NotRequired[Filters.StringFilter]
        id: NotRequired[Filters.StringFilter]
        parent_item_id: NotRequired[Filters.StringFilter]

    @staticmethod
    def create(id, params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("item_prices", id, "differential_prices"),
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
            request.uri_path("differential_prices", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def update(id, params: UpdateParams, env=None, headers=None) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("differential_prices", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def delete(id, params: DeleteParams, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("differential_prices", id, "delete"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("differential_prices"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )
