from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class PriceRamp:
    env: environment.Environment

    class Status(Enum):
        ACTIVE = "active"
        ARCHIVED = "archived"
        DELETED = "deleted"

        def __str__(self):
            return self.value

    class RampInterval(TypedDict):
        starting_billing_cycle: Required[int]
        ending_billing_cycle: NotRequired[int]
        apply_catalog_price: NotRequired[bool]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]

    class CreateRampIntervalParams(TypedDict):
        starting_billing_cycle: Required[int]
        ending_billing_cycle: NotRequired[int]
        apply_catalog_price: NotRequired[bool]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]

    class UpdateRampIntervalParams(TypedDict):
        starting_billing_cycle: Required[int]
        ending_billing_cycle: NotRequired[int]
        apply_catalog_price: NotRequired[bool]
        price: NotRequired[int]
        price_in_decimal: NotRequired[str]

    class CreateParams(TypedDict):
        item_price_id: Required[str]
        business_entity_id: NotRequired[str]
        ramp_intervals: NotRequired[List["PriceRamp.CreateRampIntervalParams"]]

    class UpdateParams(TypedDict):
        status: NotRequired["PriceRamp.Status"]
        ramp_intervals: NotRequired[List["PriceRamp.UpdateRampIntervalParams"]]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        item_price_id: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        business_entity_id: NotRequired[Filters.StringFilter]
        include_site_level_resources: NotRequired[Filters.BooleanFilter]
        sort_by: NotRequired[Filters.SortFilter]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("price_ramps"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="priceRamp",
            operation="create",
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("price_ramps", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="priceRamp",
            operation="retrieve",
        )

    def update(self, id, params: UpdateParams, headers=None) -> UpdateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("price_ramps", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="priceRamp",
            operation="update",
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("price_ramps", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="priceRamp",
            operation="delete",
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("price_ramps"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="priceRamp",
            operation="list",
        )
