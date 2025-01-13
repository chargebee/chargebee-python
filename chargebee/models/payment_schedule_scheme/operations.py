from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class PaymentScheduleScheme:

    env: environment.Environment

    class PeriodUnit(Enum):
        DAY = "day"
        WEEK = "week"
        MONTH = "month"

        def __str__(self):
            return self.value

    class PreferredSchedule(TypedDict):
        period: NotRequired[int]
        amount_percentage: NotRequired[float]

    class CreateFlexibleScheduleParams(TypedDict):
        period: NotRequired[int]
        amount_percentage: NotRequired[float]

    class CreateParams(TypedDict):
        number_of_schedules: Required[int]
        period_unit: Required["PaymentScheduleScheme.PeriodUnit"]
        period: NotRequired[int]
        name: Required[str]
        flexible_schedules: NotRequired[
            List["PaymentScheduleScheme.CreateFlexibleScheduleParams"]
        ]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("payment_schedule_schemes"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("payment_schedule_schemes", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("payment_schedule_schemes", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
        )
