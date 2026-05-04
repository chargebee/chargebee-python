from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums, filter_condition


@dataclass
class Alert:
    env: environment.Environment

    class Status(Enum):
        ENABLED = "enabled"
        DISABLED = "disabled"

        def __str__(self):
            return self.value

    class CreateThresholdParams(TypedDict):
        mode: Required[enums.Mode]
        value: Required[float]

    class CreateFilterConditionParams(TypedDict):
        field: NotRequired["filter_condition.FilterCondition.Field"]
        operator: NotRequired["filter_condition.FilterCondition.Operator"]
        value: NotRequired[str]

    class UpdateThresholdParams(TypedDict):
        mode: NotRequired[enums.Mode]
        value: NotRequired[float]

    class CreateParams(TypedDict):
        type: Required[enums.Type]
        name: Required[str]
        description: NotRequired[str]
        metered_feature_id: Required[str]
        subscription_id: NotRequired[str]
        threshold: Required["Alert.CreateThresholdParams"]
        meta: NotRequired[str]
        filter_conditions: NotRequired[List["Alert.CreateFilterConditionParams"]]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        type: NotRequired[Filters.EnumFilter]
        subscription_id: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]

    class UpdateParams(TypedDict):
        threshold: NotRequired["Alert.UpdateThresholdParams"]
        status: NotRequired["Alert.Status"]

    class ApplicationAlertsForSubscriptionParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        status: NotRequired[Filters.EnumFilter]
        type: NotRequired[Filters.EnumFilter]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("alerts"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("alerts", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
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
            request.uri_path("alerts"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update(self, id, params: UpdateParams = None, headers=None) -> UpdateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("alerts", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("alerts", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def application_alerts_for_subscription(
        self, id, params: ApplicationAlertsForSubscriptionParams = None, headers=None
    ) -> ApplicationAlertsForSubscriptionResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "applicable_alerts"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ApplicationAlertsForSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )
