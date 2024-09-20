from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.models import enums


class Address:

    class RetrieveParams(TypedDict):
        subscription_id: Required[str]
        label: Required[str]

    class UpdateParams(TypedDict):
        subscription_id: Required[str]
        label: Required[str]
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        email: NotRequired[str]
        company: NotRequired[str]
        phone: NotRequired[str]
        addr: NotRequired[str]
        extended_addr: NotRequired[str]
        extended_addr2: NotRequired[str]
        city: NotRequired[str]
        state_code: NotRequired[str]
        state: NotRequired[str]
        zip: NotRequired[str]
        country: NotRequired[str]
        validation_status: NotRequired[enums.ValidationStatus]

    @staticmethod
    def retrieve(params: RetrieveParams, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("addresses"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def update(params: UpdateParams, env=None, headers=None) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("addresses"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )
