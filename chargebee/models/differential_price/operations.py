from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


class DifferentialPrice:
    class Status(Enum):
        ACTIVE = "active"
        DELETED = "deleted"

        def __str__(self):
            return self.value

    class ParentPeriodPeriodUnit(Enum):
        DAY = "day"
        WEEK = "week"
        MONTH = "month"
        YEAR = "year"

        def __str__(self):
            return self.value

    class Tier(TypedDict):
        starting_unit: Required[int]
        ending_unit: NotRequired[int]
        price: Required[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]

    class ParentPeriod(TypedDict):
        period_unit: Required["DifferentialPrice.ParentPeriodPeriodUnit"]
        period: NotRequired[List[Dict[Any, Any]]]

    class CreateParentPeriodParams(TypedDict):
        period_unit: Required["DifferentialPrice.ParentPeriodPeriodUnit"]
        period: NotRequired[List[Dict[Any, Any]]]

    class CreateTierParams(TypedDict):
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]

    class UpdateParentPeriodParams(TypedDict):
        period_unit: Required["DifferentialPrice.ParentPeriodPeriodUnit"]
        period: NotRequired[List[Dict[Any, Any]]]

    class UpdateTierParams(TypedDict):
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]

    class CreateParams(TypedDict):
        parent_item_id: Required[str]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]
        parent_periods: Required[List["DifferentialPrice.CreateParentPeriodParams"]]
        tiers: NotRequired[List["DifferentialPrice.CreateTierParams"]]

    class RetrieveParams(TypedDict):
        item_price_id: Required[str]

    class UpdateParams(TypedDict):
        item_price_id: Required[str]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]
        parent_periods: Required[List["DifferentialPrice.UpdateParentPeriodParams"]]
        tiers: NotRequired[List["DifferentialPrice.UpdateTierParams"]]

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
