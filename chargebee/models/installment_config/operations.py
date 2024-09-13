from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any


class InstallmentConfig:

    class CreateParams(TypedDict):
        number_of_installments: Required[int]
        period_unit: Required[PeriodUnit]
        period: NotRequired[int]
        preferred_day: NotRequired[int]
        description: NotRequired[str]
        installments: NotRequired[List[CreateInstallmentParams]]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("installment_configs"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("installment_configs", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("installment_configs", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )
