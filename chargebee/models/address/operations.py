from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.models import enums


@dataclass
class Address:

    env: environment.Environment

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

    def retrieve(self, params: RetrieveParams, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("addresses"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveResponse,
        )

    def update(self, params: UpdateParams, headers=None) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("addresses"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
        )
