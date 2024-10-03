from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


class PaymentScheduleScheme:
    class PeriodUnit(Enum):
        DAY = "day"
        WEEK = "week"
        MONTH = "month"

        def __str__(self):
            return self.value

    class PreferredSchedule(TypedDict):
        period: NotRequired[int]
        amount_percentage: NotRequired[float]

    class CreateParams(TypedDict):
        number_of_schedules: Required[int]
        period_unit: Required["PaymentScheduleScheme.PeriodUnit"]
        period: NotRequired[int]
        description: NotRequired[str]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("payment_schedule_schemes"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("payment_schedule_schemes", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("payment_schedule_schemes", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )
