from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class DifferentialPrice:

    env: environment.Environment

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

    def create(self, id, params: CreateParams, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("item_prices", id, "differential_prices"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
        )

    def retrieve(self, id, params: RetrieveParams, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("differential_prices", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveResponse,
        )

    def update(self, id, params: UpdateParams, headers=None) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("differential_prices", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
        )

    def delete(self, id, params: DeleteParams, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("differential_prices", id, "delete"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeleteResponse,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("differential_prices"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
        )
