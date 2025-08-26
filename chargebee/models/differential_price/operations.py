from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


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
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

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
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

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
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

    class CreateParams(TypedDict):
        parent_item_id: Required[str]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]
        parent_periods: Required[List["DifferentialPrice.CreateParentPeriodParams"]]
        tiers: NotRequired[List["DifferentialPrice.CreateTierParams"]]
        business_entity_id: NotRequired[str]

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
        jsonKeys = {
            "period": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("item_prices", id, "differential_prices"),
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
            request.uri_path("differential_prices", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update(self, id, params: UpdateParams, headers=None) -> UpdateResponse:
        jsonKeys = {
            "period": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("differential_prices", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
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
            request.uri_path("differential_prices", id, "delete"),
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
            request.uri_path("differential_prices"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )
